# StarDict Flip: English-to-Many Languages Dictionary Converter

## 🌟 Why this project?
I encountered a recurring problem when using **KOReader** on Kindle: while there are many excellent dictionaries for translating **various languages to English**, there is a significant lack of high-quality dictionaries for the reverse—**English to other languages** (like Armenian, etc.).

Most available tools work great for the "native-to-English" direction, but finding an "English-to-Native" dictionary with full inflection support is often a challenge. 

This repository provides a framework and specific scripts to bridge this gap. It allows you to take existing **Target-to-English** StarDict files and "flip" them into fully functional, searchable **English-to-Target** dictionaries, specifically optimized for Kindle and KOReader.

## 📂 Project Structure
- `Dictionaries/Armenian-English/`: The original source database (used here as the primary example).
- `Dictionaries/English-Armenian/`: The final converted "flipped" files ready for Kindle.
- `Scripts/`: 
  - `formatter.py`: A specialized parser that extracts English headwords from complex HTML/Inflections and swaps columns.
  - `convert.sh`: A shell script to automate the entire export, flip, and rebuild process.
- `Source/`: Intermediate raw data and formatted text files.

## 🚀 Installation for Kindle Users
If you just want the **English-Armenian** dictionary:
1. Connect your Kindle to your PC.
2. Navigate to your KOReader dictionary folder: `.adds/koreader/data/dict/`.
3. Create a new folder named `English-Armenian`.
4. Copy the `.dict`, `.idx`, and `.ifo` files from `Dictionaries/English-Armenian/` into that folder.
5. In KOReader, go to **Dictionary Settings** -> **Manage Dictionaries** and ensure it is selected.

## 🛠 For Developers: Global Conversion (Flip any language)
You can use these scripts to flip any StarDict dictionary:
1. Place your StarDict files in `Dictionaries/[Target]-English/`.
2. Update the paths in `Scripts/convert.sh`.
3. Run the automation script:
   ```bash
   sh Scripts/convert.sh
