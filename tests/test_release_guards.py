import gzip
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
from zipfile import BadZipFile, ZipFile

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('validator', ROOT / 'src/validate_dictionaries.py')
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class ArchiveTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)

    def archive(self, name='JMdict_english.zip', banks=None):
        path = self.root / name
        with ZipFile(path, 'w') as z:
            z.writestr('index.json', json.dumps({'title': 'test'}))
            for key, value in (banks or {}).items():
                z.writestr(key, value)
        return path

    def test_valid_terms(self):
        self.assertEqual(validator.validate_archive(self.archive(banks={'term_bank_1.json': '[["word"]]'})), 1)

    def test_valid_kanji(self):
        self.assertEqual(validator.validate_archive(self.archive('KANJIDIC_english.zip', {'kanji_bank_1.json': '[["字"]]'})), 1)

    def test_missing_banks(self):
        with self.assertRaises(ValueError):
            validator.validate_archive(self.archive())

    def test_noncontiguous_banks(self):
        for numbers in ((2,), (1, 3)):
            with self.subTest(numbers=numbers), self.assertRaises(ValueError):
                validator.validate_archive(self.archive(banks={
                    f'term_bank_{number}.json': '[["entry"]]' for number in numbers
                }))

    def test_multiple_banks(self):
        self.assertEqual(validator.validate_archive(self.archive(banks={
            'term_bank_2.json': '[["second"]]', 'term_bank_1.json': '[["first"]]'
        })), 2)

    def test_wrong_bank_type(self):
        with self.assertRaises(ValueError):
            validator.validate_archive(self.archive(banks={'kanji_bank_1.json': '[["字"]]'}))

    def test_invalid_banks(self):
        for value in ('[]', '{}', 'null', 'bad JSON', '[[]]', '["word"]'):
            with self.subTest(value=value), self.assertRaises(ValueError):
                validator.validate_archive(self.archive(banks={'term_bank_1.json': value}))

    def test_corrupt_archive(self):
        path = self.root / 'JMdict_english.zip'
        path.write_bytes(b'not a zip')
        with self.assertRaises(BadZipFile):
            validator.validate_archive(path)

    def test_invalid_index(self):
        for value in ('null', '{}', 'bad JSON'):
            with self.subTest(value=value):
                path = self.root / 'JMdict_english.zip'
                with ZipFile(path, 'w') as z:
                    z.writestr('index.json', value)
                    z.writestr('term_bank_1.json', '[["entry"]]')
                with self.assertRaises(ValueError):
                    validator.validate_archive(path)

    def test_missing_expected_archive(self):
        with self.assertRaises(FileNotFoundError):
            validator.validate_directory(self.root)

    def test_complete_set(self):
        for name in validator.EXPECTED:
            kind = 'kanji' if name.startswith('KANJIDIC_') else 'term'
            self.archive(f'{name}.zip', {f'{kind}_bank_1.json': '[["entry"]]'})
        validator.validate_directory(self.root)


class BuildTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        shutil.copytree(ROOT / 'src', self.root / 'src')
        (self.root / 'data').mkdir()
        (self.root / 'binaries').mkdir()
        (self.root / 'mock-bin').mkdir()
        self.env = os.environ.copy()
        self.env['PATH'] = str(self.root / 'mock-bin') + os.pathsep + self.env['PATH']
        self.script(self.root / 'mock-bin/wget', '''#!/usr/bin/env python3
import gzip, os, sys
from pathlib import Path
mode=os.environ.get('DOWNLOAD_MODE', 'ok')
output=Path(sys.argv[sys.argv.index('-O')+1])
if mode=='failed':
    output.write_bytes(b'partial')
    sys.exit(1)
output.write_bytes(b'corrupt' if mode=='corrupt' else gzip.compress(b'' if mode=='empty' else b'source data'))
''')
        self.script(self.root / 'binaries/yomitan', '''#!/usr/bin/env python3
import json, os, sys
from pathlib import Path
from zipfile import BadZipFile, ZipFile
Path('converter-called').touch()
mode=os.environ.get('CONVERTER_MODE', 'ok')
if mode=='failed': sys.exit(1)
path=Path(sys.argv[-1])
with ZipFile(path, 'w') as z:
    z.writestr('index.json', json.dumps({'title':'test'}))
    if mode!='empty':
        kind='kanji' if path.name.startswith('KANJIDIC_') else 'term'
        z.writestr(kind+'_bank_1.json', '[["entry"]]')
''')

    def script(self, path, text):
        path.write_text(text)
        path.chmod(0o755)

    def run_build(self):
        return subprocess.run(['bash', 'src/build_dicts.sh'], cwd=self.root, env=self.env, capture_output=True, text=True)

    def test_download_failures_stop_before_conversion(self):
        for mode in ('failed', 'corrupt', 'empty'):
            with self.subTest(mode=mode):
                self.env['DOWNLOAD_MODE'] = mode
                result = self.run_build()
                self.assertNotEqual(result.returncode, 0, result.stdout)
                self.assertFalse((self.root / 'converter-called').exists())
                self.assertFalse((self.root / 'data/JMdict_e_examp').exists())
                self.assertEqual(list((self.root / 'data').glob('.download.*')), [])

    def test_failed_refresh_preserves_previous_source(self):
        path = self.root / 'data/JMdict_e_examp'
        path.write_text('previous valid source')
        os.utime(path, (0, 0))
        self.env['DOWNLOAD_MODE'] = 'failed'
        self.assertNotEqual(self.run_build().returncode, 0)
        self.assertEqual(path.read_text(), 'previous valid source')

    def test_empty_cache_is_redownloaded(self):
        (self.root / 'data/JMdict_e_examp').touch()
        result = self.run_build()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((self.root / 'data/JMdict_e_examp').read_text(), 'source data')

    def test_converter_failure_stops_build(self):
        self.env['CONVERTER_MODE'] = 'failed'
        self.assertNotEqual(self.run_build().returncode, 0)
        self.assertFalse((self.root / 'data/JMdict_b').exists())

    def test_empty_converter_output_rejected(self):
        self.env['CONVERTER_MODE'] = 'empty'
        result = self.run_build()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('no term banks', result.stderr)

    def test_successful_build_validates_all_outputs(self):
        result = self.run_build()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(len(list((self.root / 'dst').glob('*.zip'))), len(validator.EXPECTED))


if __name__ == '__main__':
    unittest.main()
