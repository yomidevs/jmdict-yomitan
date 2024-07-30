# JMdict for Yomitan <!-- omit in toc -->

[![](https://img.shields.io/github/v/tag/marvnc/jmdict-yomitan?style=for-the-badge&label=Last%20Release)](#downloads)

This repository contains automatically generated dictionaries for use with [Yomitan](https://github.com/themoeway/yomitan) (formerly [Yomichan](https://foosoft.net/projects/yomichan/)), a free Japanese dictionary browser extension. They are built using information from the [JMdict](https://www.edrdg.org/wiki/index.php/JMdict-EDICT_Dictionary_Project) project, which is a freely available Japanese dictionary maintained by the [Electronic Dictionary Research and Development Group](http://www.edrdg.org/). There are also releases for [JMnedict](https://www.edrdg.org/enamdict/enamdict_doc.html) and [KANJIDIC](https://www.edrdg.org/wiki/index.php/KANJIDIC_Project), which are respectively a Japanese proper names dictionary and a kanji dictionary.

This repository is automatically updated daily and the dictionary files are built from JMdict using the [Yomitan Import](https://github.com/themoeway/yomitan-import) tool.

- [Downloads](#downloads)
  - [JMdict for Yomitan](#jmdict-for-yomitan)
  - [JMnedict for Yomitan](#jmnedict-for-yomitan)
  - [KANJIDIC for Yomitan](#kanjidic-for-yomitan)
- [FAQ](#faq)
  - [Legacy vs Extra/Regular JMdict](#legacy-vs-extraregular-jmdict)
  - [How Often Should I Update?](#how-often-should-i-update)
  - [漢字使い参考 vs JMdict Forms](#漢字使い参考-vs-jmdict-forms)
- [Acknowledgements](#acknowledgements)
- [License](#license)

## Downloads

The download links below will always point toward the latest release.

### JMdict for Yomitan

> [!IMPORTANT]
> Stephenmk who had worked extensively on creating these dictionaries has now created [Jitendex](https://jitendex.org/), a further improved Yomitan dictionary built using JMdict and Tatoeba data. We recommend you try it out instead of the English JMdict in this repository.

To see your current version of JMdict, hover over this entry:

> ＪＭｄｉｃｔ

- JMdict (English)
  - [JMdict_english_with_examples.zip](https://github.com/themoeway/jmdict-yomitan/releases/latest/download/JMdict_english_with_examples.zip)
    - This is the version of JMdict with example sentences from the [Tatoeba Project](http://tatoeba.org/home).
  - [JMdict_english.zip](https://github.com/themoeway/jmdict-yomitan/releases/latest/download/JMdict_english.zip)
    - This is the same JMdict but without example sentences.
  - [JMdict_english_legacy.zip](https://github.com/themoeway/jmdict-yomitan/releases/latest/download/JMdict_english_legacy.zip)
    - This is JMdict with legacy formatting. It is not recommended for use; see the FAQ below.
- JMdict (Other Languages)
  - [JMdict_dutch.zip](https://github.com/themoeway/jmdict-yomitan/releases/latest/download/JMdict_dutch.zip)
  - [JMdict_french.zip](https://github.com/themoeway/jmdict-yomitan/releases/latest/download/JMdict_french.zip)
  - [JMdict_german.zip](https://github.com/themoeway/jmdict-yomitan/releases/latest/download/JMdict_german.zip)
  - [JMdict_hungarian.zip](https://github.com/themoeway/jmdict-yomitan/releases/latest/download/JMdict_hungarian.zip)
  - [JMdict_russian.zip](https://github.com/themoeway/jmdict-yomitan/releases/latest/download/JMdict_russian.zip)
  - [JMdict_slovenian.zip](https://github.com/themoeway/jmdict-yomitan/releases/latest/download/JMdict_slovenian.zip)
  - [JMdict_spanish.zip](https://github.com/themoeway/jmdict-yomitan/releases/latest/download/JMdict_spanish.zip)
  - [JMdict_swedish.zip](https://github.com/themoeway/jmdict-yomitan/releases/latest/download/JMdict_swedish.zip)
- JMdict Forms
  - [JMdict_forms.zip](https://github.com/themoeway/jmdict-yomitan/releases/latest/download/JMdict_forms.zip)
    - This is a version of JMdict that includes only the alternate forms of each entry. This is useful for conjugation lookup for those who do not wish to have any dictionary definitons, and is unnecessary if you are using the regular JMdict.

### JMnedict for Yomitan

- [JMnedict.zip](https://github.com/themoeway/jmdict-yomitan/releases/latest/download/JMnedict.zip)

### KANJIDIC for Yomitan

- [KANJIDIC_english.zip](https://github.com/themoeway/jmdict-yomitan/releases/latest/download/KANJIDIC_english.zip)
- [KANJIDIC_french.zip](https://github.com/themoeway/jmdict-yomitan/releases/latest/download/KANJIDIC_french.zip)
- [KANJIDIC_portuguese.zip](https://github.com/themoeway/jmdict-yomitan/releases/latest/download/KANJIDIC_portuguese.zip)
- [KANJIDIC_spanish.zip](https://github.com/themoeway/jmdict-yomitan/releases/latest/download/KANJIDIC_spanish.zip)

## FAQ

### Legacy vs Extra/Regular JMdict

The legacy JMdict for Yomitan is a version of JMdict for Yomichan with legacy formatting and with lots of information missing. The so-called "extra" version of JMdict was [introduced by stephenmk](https://github.com/FooSoft/yomichan-import/pull/40) to modernize the formatting and add vital missing information such as notes, type information, source languages, references, antonyms, other forms, and more.

The terminology of "Extra" is confusing since it implies that the extra version is a marginal improvement to the legacy version, so we will just call it the "regular" JMdict. The legacy version is available for download as some third-party apps do not yet support new structured-content features, but we recommend using the regular version if possible as you will be missing out on a lot of important information otherwise.

### How Often Should I Update?

- The **JMdict** project [is quite active](https://www.edrdg.org/jmwsgi/updates.py?svc=jmdict&i=1) so we recommend you update your JMdict files every few months as lots of entries are added and improved upon every single day by contributers. You can even [contribute to the project here](https://www.edrdg.org/jmwsgi/edhelpq.py?svc=jmdict&sid=).

- The **JMnedict** project is [also somewhat active](https://www.edrdg.org/jmwsgi/updates.py?svc=jmdict&i=1) although arguably less relevant. However, there is an old version of JMnedict from before it was [updated by stephenmk](https://github.com/FooSoft/yomichan-import/pull/41); the old version is structured in such a way that you get a lot of search bloat when searching any kanji or kana so we strongly recommend you download the newest JMnedict at least once.

- The **KANJIDIC** project [does not appear to be as active](https://www.edrdg.org/wiki/index.php/KANJIDIC_Project), so it is probably fine not to update it.

### 漢字使い参考 vs JMdict Forms

There is a very old version of the JMdict Forms dictionary floating around under the name 漢字使い参考 dating back to 2021 or so. We recommend you update to the latest version of JMdict Forms from that so that you get the benefits of the latest JMdict data.

## Acknowledgements

This repository was heavily inspired by Aquafina-water-bottle's [JMdict for Yomichan](https://github.com/Aquafina-water-bottle/jmdict-english-yomichan) repository.

## License

The code in this repository is licensed under the MIT license. The released dictionaries are licensed under the [Creative Commons Attribution-ShareAlike Licence (V4.0)](https://creativecommons.org/licenses/by-sa/4.0/) that [JMdict is](https://www.edrdg.org/edrdg/licence.html).

This repository uses the [JMdict/EDICT](https://www.edrdg.org/wiki/index.php/JMdict-EDICT_Dictionary_Project) and [KANJIDIC](https://www.edrdg.org/wiki/index.php/KANJIDIC_Project) dictionary files. These files are the property of the [Electronic Dictionary Research and Development Group](https://www.edrdg.org/), and are used in conformance with the Group's licence.
