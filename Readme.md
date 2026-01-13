# English-Armenian Wiktionary Dictionary for Kindle

This project provides a professional English-Armenian dictionary in StarDict format, specifically optimized for Kindle (KOReader). It maps English headwords to their corresponding Armenian inflections (declensions and conjugations).

## 📂 Project Structure
- `Dictionaries/Armenian-English/`: Original source files.
- `Dictionaries/English-Armenian/`: Final production files for Kindle.
- `Scripts/`: Automation and formatting scripts.
- `Source/`: Intermediate data files.

## 🚀 Installation
1. Copy the files from `Dictionaries/English-Armenian/` to your Kindle:
   `koreader/data/dict/English-Armenian/`
2. In KOReader, enable the dictionary in **Dictionary Settings**.

## 🛠 Build from Source
If you wish to rebuild the dictionary:
1. Run `./Scripts/convert.sh` (requires PyGlossary and Python 3).
