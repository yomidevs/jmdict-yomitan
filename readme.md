# JMdict for Yomitan

[![](https://img.shields.io/github/v/tag/marvnc/jmdict-yomitan?style=for-the-badge&label=Last%20Release)](https://github.com/MarvNC/jmdict-yomitan/releases/latest)

This repository contains automatically generated dictionaries for use with [Yomitan](https://github.com/themoeway/yomitan)/[Yomichan](https://foosoft.net/projects/yomichan/), a free Japanese dictionary browser extension. They are built using information from the [JMdict](https://www.edrdg.org/wiki/index.php/JMdict-EDICT_Dictionary_Project) project, which is a freely available Japanese dictionary in maintained by the [Electronic Dictionary Research and Development Group](http://www.edrdg.org/). There are also releases for [JMnedict](https://www.edrdg.org/enamdict/enamdict_doc.html) and [KANJIDIC](https://www.edrdg.org/wiki/index.php/KANJIDIC_Project), which are respectively a Japanese proper names dictionary and a kanji dictionary.

This repository is updated monthly via a GitHub Action and is built from the JMdict project files using the [Yomitan-import](https://github.com/themoeway/yomitan-import) tool and a `build_dicts.sh` script provided with the tool.

## JMdict for Yomitan

- [JMdict English w/ example sentences](https://github.com/MarvNC/jmdict-yomitan/releases/latest/download/JMDict_english_with_examples.zip): This is the version of JMdict with example sentences from the [Tanaka Corpus maintained by the Tatoeba Project](http://tatoeba.org/home).
- [JMdict English](https://github.com/MarvNC/jmdict-yomitan/releases/latest/download/JMdict_english.zip): This is the same JMdict but without example sentences.
- [JMdict English (Legacy)](https://github.com/MarvNC/jmdict-yomitan/releases/latest/download/JMdict_english_legacy.zip): This is JMdict with legacy formatting. It is not recommended for use; see the FAQ below.
- [JMdict Dutch](https://github.com/MarvNC/jmdict-yomitan/releases/latest/download/JMdict_dutch.zip)
- [JMdict French](https://github.com/MarvNC/jmdict-yomitan/releases/latest/download/JMdict_french.zip)
- [JMdict German](https://github.com/MarvNC/jmdict-yomitan/releases/latest/download/JMdict_german.zip)
- [JMdict Hungarian](https://github.com/MarvNC/jmdict-yomitan/releases/latest/download/JMdict_hungarian.zip)
- [JMdict Russian](https://github.com/MarvNC/jmdict-yomitan/releases/latest/download/JMdict_russian.zip)
- [JMdict Slovenian](https://github.com/MarvNC/jmdict-yomitan/releases/latest/download/JMdict_slovenian.zip)
- [JMdict Spanish](https://github.com/MarvNC/jmdict-yomitan/releases/latest/download/JMdict_spanish.zip)
- [JMdict Swedish](https://github.com/MarvNC/jmdict-yomitan/releases/latest/download/JMdict_swedish.zip)

## JMnedict for Yomitan

- [JMnedict](https://github.com/MarvNC/jmdict-yomitan/releases/latest/download/JMnedict.zip)

## KANJIDIC for Yomitan

- [KANJIDIC English](https://github.com/MarvNC/jmdict-yomitan/releases/latest/download/KANJIDIC_english.zip)
- [KANJIDIC French](https://github.com/MarvNC/jmdict-yomitan/releases/latest/download/KANJIDIC_french.zip)
- [KANJIDIC Portuguese](https://github.com/MarvNC/jmdict-yomitan/releases/latest/download/KANJIDIC_portuguese.zip)
- [KANJIDIC Spanish](https://github.com/MarvNC/jmdict-yomitan/releases/latest/download/KANJIDIC_spanish.zip)

## FAQ

### Legacy vs Extra/Regular JMdict

The legacy JMdict for Yomitan is a version of JMdict for Yomichan with legacy formatting and with lots of information missing. The so-called "extra" version of JMdict was [introduced by stephenmk](https://github.com/FooSoft/yomichan-import/pull/40) to modernize the formatting and add vital missing information such as notes, type information, source languages, references, antonyms, other forms, and more.

The terminology of "Extra" is confusing since it implies that the extra version is a marginal improvement to the legacy version, so we will just call it the "regular" JMdict. The legacy version is available for download as some third-party apps do not yet support new structured-content features, but we recommend using the regular version if possible as you will be missing out on a lot of important information otherwise.

### How Often Should I Update?

- The **JMdict** project [is quite active](https://www.edrdg.org/jmwsgi/updates.py?svc=jmdict&i=1) so we recommend you update your JMdict files at least once a year - many entries are added and improved upon every single day by contributers. You can even [contribute yourself here](https://www.edrdg.org/jmwsgi/edhelpq.py?svc=jmdict&sid=).

- The **JMnedict** project is [also quite active](https://www.edrdg.org/jmwsgi/updates.py?svc=jmdict&i=1) although arguably less relevant. However, there is an old version of JMnedict from before it was [updated by stephenmk](https://github.com/FooSoft/yomichan-import/pull/41); the old version is structured in such a way that you get a lot of search bloat when searching any kanji or kana so we strongly recommend you download the newest JMnedict at least once.

- The **KANJIDIC** project [does not appear to be as active](https://www.edrdg.org/wiki/index.php/KANJIDIC_Project), so it is probably fine not to update it.
