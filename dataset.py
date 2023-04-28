from googletrans import LANGUAGES, Translator
import pandas as pd
import os
from datetime import datetime
from tqdm import tqdm

print("")
print('''

████████▄     ▄████████     ███        ▄████████    ▄████████    ▄████████     ███             ▄██████▄     ▄████████ ███▄▄▄▄      ▄████████    ▄████████    ▄████████     ███      ▄██████▄     ▄████████ 
███   ▀███   ███    ███ ▀█████████▄   ███    ███   ███    ███   ███    ███ ▀█████████▄        ███    ███   ███    ███ ███▀▀▀██▄   ███    ███   ███    ███   ███    ███ ▀█████████▄ ███    ███   ███    ███ 
███    ███   ███    ███    ▀███▀▀██   ███    ███   ███    █▀    ███    █▀     ▀███▀▀██        ███    █▀    ███    █▀  ███   ███   ███    █▀    ███    ███   ███    ███    ▀███▀▀██ ███    ███   ███    ███ 
███    ███   ███    ███     ███   ▀   ███    ███   ███         ▄███▄▄▄         ███   ▀       ▄███         ▄███▄▄▄     ███   ███  ▄███▄▄▄      ▄███▄▄▄▄██▀   ███    ███     ███   ▀ ███    ███  ▄███▄▄▄▄██▀ 
███    ███ ▀███████████     ███     ▀███████████ ▀███████████ ▀▀███▀▀▀         ███          ▀▀███ ████▄  ▀▀███▀▀▀     ███   ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   ▀███████████     ███     ███    ███ ▀▀███▀▀▀▀▀   
███    ███   ███    ███     ███       ███    ███          ███   ███    █▄      ███            ███    ███   ███    █▄  ███   ███   ███    █▄  ▀███████████   ███    ███     ███     ███    ███ ▀███████████ 
███   ▄███   ███    ███     ███       ███    ███    ▄█    ███   ███    ███     ███            ███    ███   ███    ███ ███   ███   ███    ███   ███    ███   ███    ███     ███     ███    ███   ███    ███ 
████████▀    ███    █▀     ▄████▀     ███    █▀   ▄████████▀    ██████████    ▄████▀          ████████▀    ██████████  ▀█   █▀    ██████████   ███    ███   ███    █▀     ▄████▀    ▀██████▀    ███    ███ 
                                                                                                                                               ███    ███                                       ███    ███ 
---------------------------c̲o̲d̲e̲d̲ b̲y̲ w̲h̲i̲t̲e̲d̲e̲v̲i̲l̲--------------------------------------------------------------------------------------------------------------------------------------------------------------
''')
print("")
translator = Translator()

available_languages = sorted(list(LANGUAGES.values()))
n = len(available_languages)
mid = n // 2
lang_str = ""
for i in range(mid):
    lang_str += f"{available_languages[i]:<25}{available_languages[i+mid]:<25}\n"
if n % 2 != 0:
    lang_str += f"{available_languages[-1]:<25}"

print("Available languages:\n" + lang_str)

source_lang = input(f"Enter the source language : ")
while source_lang not in available_languages:
    source_lang = input(f"Invalid language. Please enter a valid source language : ")

target_lang = input(f"Enter the target language : ")
while target_lang not in available_languages:
    target_lang = input(f"Invalid language. Please enter a valid target language : ")

filename = input("Enter the filename of the text file containing the source sentences: ")

with open(filename, "r", encoding="utf-8") as file:
    source_sentences = file.read().splitlines()

output_file = input("Enter the filename for the output CSV file: ")

if os.path.exists(output_file):
    df = pd.read_csv(output_file)
    progress = len(df.index)
else:
    df = pd.DataFrame(columns=["Source", "Target"])
    progress = 0

if os.path.exists("progress.txt"):
    choice = input("Do you want to start from the beginning (B) or continue from a saved progress file (C)? ")
    if choice.lower() == "c":
        with open("progress.txt", "r") as file:
            progress = int(file.read().strip())

error_count = 0
error_details = []

pbar = tqdm(total=len(source_sentences), desc=f"Translating (Errors: {error_count})", unit="sentence", ncols=100)

for line_num, sentence in enumerate(source_sentences[progress:], start=progress+1):
    while True:
        try:
            translation = translator.translate(sentence, src=source_lang, dest=target_lang)
            translated_sentence = translation.text if translation and translation.text else ""
            df = pd.concat([df, pd.DataFrame({"Source": [sentence], "Target": [translated_sentence]})], ignore_index=True)
            pbar.update(1)
            break
        except Exception as e:
            error_details.append((line_num, str(e)))
            error_count += 1
            pbar.set_description(f"Translating (Errors: {error_count})")
            pbar.update(1)
            break

    if line_num % 10 == 0:
        df.to_csv(output_file, index=False)
        with open("progress.txt", "w") as file:
            file.write(str(line_num))

pbar.close()

df.to_csv(output_file, index=False)
if os.path.exists("progress.txt") and progress == len(source_sentences):
    os.remove("progress.txt")

print("Dataset saved to", output_file)

if error_count > 0:
    print(f"\nTotal Errors: {error_count}")
    print("Error Details:")
    for error in error_details:
        print(f"Line {error[0]}: {error[1]}")
else:
    print("No errors occurred during translation.")

