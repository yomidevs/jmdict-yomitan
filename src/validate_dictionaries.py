"""Reject incomplete dictionary releases before they become auto-updates."""
import json
import re
import sys
from pathlib import Path
from zipfile import BadZipFile, ZipFile

EXPECTED = (
    'JMdict_english_with_examples', 'JMdict_english_without_proper_names',
    'JMdict_english_legacy_without_proper_names', 'JMdict_english',
    'JMdict_english_legacy', 'JMdict_dutch', 'JMdict_french', 'JMdict_german',
    'JMdict_hungarian', 'JMdict_russian', 'JMdict_slovenian', 'JMdict_spanish',
    'JMdict_swedish', 'JMdict_forms', 'JMnedict', 'KANJIDIC_english',
    'KANJIDIC_french', 'KANJIDIC_portuguese', 'KANJIDIC_spanish',
)


def validate_archive(path):
    bank_type = 'kanji' if path.name.startswith('KANJIDIC_') else 'term'
    pattern = re.compile(rf'{bank_type}_bank_[1-9][0-9]*\.json')
    with ZipFile(path) as archive:
        names = archive.namelist()
        if len(names) != len(set(names)):
            raise ValueError(f'{path.name}: duplicate ZIP members')
        index = json.loads(archive.read('index.json'))
        if not isinstance(index, dict) or not index.get('title'):
            raise ValueError(f'{path.name}: invalid index.json')
        banks = [name for name in names if pattern.fullmatch(name)]
        if not banks:
            raise ValueError(f'{path.name}: no {bank_type} banks')
        count = 0
        for name in banks:
            entries = json.loads(archive.read(name))
            if not isinstance(entries, list) or not entries:
                raise ValueError(f'{path.name}/{name}: empty or invalid bank')
            if any(not isinstance(entry, list) or not entry for entry in entries):
                raise ValueError(f'{path.name}/{name}: invalid entry')
            count += len(entries)
        return count


def validate_directory(directory):
    for name in EXPECTED:
        path = Path(directory) / f'{name}.zip'
        count = validate_archive(path)
        print(f'{path.name}: {count} entries')


if __name__ == '__main__':
    try:
        validate_directory(sys.argv[1] if len(sys.argv) > 1 else 'dst')
    except (OSError, ValueError, KeyError, BadZipFile) as error:
        sys.exit(f'Dictionary validation failed: {error}')
