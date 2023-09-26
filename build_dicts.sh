# This script is copied from https://github.com/themoeway/yomitan-import/blob/main/scripts/build_dicts.sh with little modifications.

#!/bin/bash

mkdir -p src
mkdir -p dst

function refresh_source () {
    NOW=$(date '+%s')
    YESTERDAY=$((NOW - 86400)) # 86,400 seconds in 24 hours
    if [ ! -f "src/$1" ]; then
        wget "ftp.edrdg.org/pub/Nihongo/$1.gz"
        gunzip -c "$1.gz" > "src/$1"
    elif [[ $YESTERDAY -gt $(date -r "src/$1" '+%s') ]]; then
        rsync "ftp.edrdg.org::nihongo/$1" "src/$1"
    fi
}

refresh_source "JMdict_e_examp"
./binaries/yomitan -language="english_extra" -title="JMdict" src/JMdict_e_examp dst/JMdict_english_with_examples.zip

refresh_source "JMdict"
./binaries/yomitan -language="english_extra" -title="JMdict"         src/JMdict dst/JMdict_english.zip
./binaries/yomitan -language="english"   -title="JMdict (Legacy)"    src/JMdict dst/JMdict_english_legacy.zip
./binaries/yomitan -language="dutch"     -title="JMdict (Dutch)"     src/JMdict dst/JMdict_dutch.zip
./binaries/yomitan -language="french"    -title="JMdict (French)"    src/JMdict dst/JMdict_french.zip
./binaries/yomitan -language="german"    -title="JMdict (German)"    src/JMdict dst/JMdict_german.zip
./binaries/yomitan -language="hungarian" -title="JMdict (Hungarian)" src/JMdict dst/JMdict_hungarian.zip
./binaries/yomitan -language="russian"   -title="JMdict (Russian)"   src/JMdict dst/JMdict_russian.zip
./binaries/yomitan -language="slovenian" -title="JMdict (Slovenian)" src/JMdict dst/JMdict_slovenian.zip
./binaries/yomitan -language="spanish"   -title="JMdict (Spanish)"   src/JMdict dst/JMdict_spanish.zip
./binaries/yomitan -language="swedish"   -title="JMdict (Swedish)"   src/JMdict dst/JMdict_swedish.zip

./binaries/yomitan -format="forms"       -title="JMdict Forms"       src/JMdict dst/JMdict_forms.zip

refresh_source "JMnedict.xml"
./binaries/yomitan src/JMnedict.xml dst/JMnedict.zip

refresh_source "kanjidic2.xml"
./binaries/yomitan -language="english"    -title="KANJIDIC"              src/kanjidic2.xml dst/KANJIDIC_english.zip
./binaries/yomitan -language="french"     -title="KANJIDIC (French)"     src/kanjidic2.xml dst/KANJIDIC_french.zip
./binaries/yomitan -language="portuguese" -title="KANJIDIC (Portuguese)" src/kanjidic2.xml dst/KANJIDIC_portuguese.zip
./binaries/yomitan -language="spanish"    -title="KANJIDIC (Spanish)"    src/kanjidic2.xml dst/KANJIDIC_spanish.zip
