#!/bin/bash
set -euo pipefail

# This script is copied from https://github.com/yomidevs/yomitan-import/blob/main/scripts/build_dicts.sh with little modifications.

mkdir -p data
mkdir -p dst
mkdir -p binaries

if [ ! -f "binaries/yomitan" ]; then
    wget "https://github.com/yomidevs/yomitan-import/releases/latest/download/yomitan-import-linux.zip"
    unzip -j "yomitan-import-linux.zip" -d binaries
fi
chmod +x ./binaries/yomitan

function refresh_source () {
    local source="$1"
    local target="data/$source"
    local yesterday=$(( $(date '+%s') - 86400 ))
    if [[ -s "$target" ]] && [[ "$yesterday" -le $(date -r "$target" '+%s') ]]; then
        return
    fi

    # Keep the previous source intact until download and decompression succeed.
    # A failed gunzip redirect must never leave an empty file in the cache.
    local work
    work=$(mktemp -d "data/.download.XXXXXX")
    if ! wget --timeout=30 --tries=3 -O "$work/source.gz" "https://www.edrdg.org/pub/Nihongo/$source.gz"; then
        rm -rf "$work"
        echo "Failed to download $source" >&2
        return 1
    fi
    if ! gunzip -c "$work/source.gz" > "$work/source" || [[ ! -s "$work/source" ]]; then
        rm -rf "$work"
        echo "Invalid or empty compressed source: $source" >&2
        return 1
    fi
    mv "$work/source" "$target"
    rm -rf "$work"
}

refresh_source "JMdict_e_examp"
./binaries/yomitan -language="english_extra" -title="JMdict" data/JMdict_e_examp dst/JMdict_english_with_examples.zip

refresh_source "JMdict_b"
./binaries/yomitan -language="english_extra" -format="edict" -title="JMdict"          data/JMdict_b dst/JMdict_english_without_proper_names.zip
./binaries/yomitan -language="english"       -format="edict" -title="JMdict (Legacy)" data/JMdict_b dst/JMdict_english_legacy_without_proper_names.zip

refresh_source "JMdict"
./binaries/yomitan -language="english_extra" -title="JMdict"         data/JMdict dst/JMdict_english.zip
./binaries/yomitan -language="english"   -title="JMdict (Legacy)"    data/JMdict dst/JMdict_english_legacy.zip
./binaries/yomitan -language="dutch"     -title="JMdict (Dutch)"     data/JMdict dst/JMdict_dutch.zip
./binaries/yomitan -language="french"    -title="JMdict (French)"    data/JMdict dst/JMdict_french.zip
./binaries/yomitan -language="german"    -title="JMdict (German)"    data/JMdict dst/JMdict_german.zip
./binaries/yomitan -language="hungarian" -title="JMdict (Hungarian)" data/JMdict dst/JMdict_hungarian.zip
./binaries/yomitan -language="russian"   -title="JMdict (Russian)"   data/JMdict dst/JMdict_russian.zip
./binaries/yomitan -language="slovenian" -title="JMdict (Slovenian)" data/JMdict dst/JMdict_slovenian.zip
./binaries/yomitan -language="spanish"   -title="JMdict (Spanish)"   data/JMdict dst/JMdict_spanish.zip
./binaries/yomitan -language="swedish"   -title="JMdict (Swedish)"   data/JMdict dst/JMdict_swedish.zip

./binaries/yomitan -format="forms"       -title="JMdict Forms"       data/JMdict dst/JMdict_forms.zip

refresh_source "JMnedict.xml"
./binaries/yomitan data/JMnedict.xml dst/JMnedict.zip

refresh_source "kanjidic2.xml"
./binaries/yomitan -language="english"    -title="KANJIDIC"              data/kanjidic2.xml dst/KANJIDIC_english.zip
./binaries/yomitan -language="french"     -title="KANJIDIC (French)"     data/kanjidic2.xml dst/KANJIDIC_french.zip
./binaries/yomitan -language="portuguese" -title="KANJIDIC (Portuguese)" data/kanjidic2.xml dst/KANJIDIC_portuguese.zip
./binaries/yomitan -language="spanish"    -title="KANJIDIC (Spanish)"    data/kanjidic2.xml dst/KANJIDIC_spanish.zip

python3 src/validate_dictionaries.py dst
