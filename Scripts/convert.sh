cd ~/Desktop/dict/English-Armenian/English-Target\ dict/dict

python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install pyglossary



#!/bin/bash


pyglossary "Dictionaries/Armenian-English/Armenian-English Wiktionary dictionary.ifo" "Source/dictionary_source.txt"


python3 Scripts/formatter.py


pyglossary "Source/formatted_en_hy.txt" \
           "Dictionaries/English-Armenian/English-Armenian_Wiktionary.ifo" \
           --write-format=Stardict \
           --sort \
           --write-options="dictzip=false"
