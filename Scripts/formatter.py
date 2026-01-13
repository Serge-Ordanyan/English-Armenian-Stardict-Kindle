import re
import os

SOURCE = "Source/dictionary_source.txt"
OUTPUT = "Source/formatted_en_hy.txt"

def build_production_file():
    if not os.path.exists(SOURCE):
        print(f"Error: {SOURCE} not found.")
        return

    with open(SOURCE, "r", encoding="utf-8") as f_in, \
         open(OUTPUT, "w", encoding="utf-8") as f_out:

        for line in f_in:
            if line.startswith("#") or "\t" not in line:
                continue


            arm_part, eng_html = line.split("\t", 1)


            clean_text = re.sub(r'<[^>]+>', ' ', eng_html)


            clean_text = re.sub(r'\b(noun|verb|adj|adverb|initialism)\b', '', clean_text, flags=re.IGNORECASE)



            clean_eng = clean_text.strip()

            clean_eng = re.sub(r'^\d+\.', '', clean_eng).strip()

            if clean_eng and arm_part:

                f_out.write(f"{clean_eng}\t{arm_part.strip()}\n")

if __name__ == "__main__":
    build_production_file()
    print(f"DONE: {OUTPUT} is ready for Kindle conversion.")
