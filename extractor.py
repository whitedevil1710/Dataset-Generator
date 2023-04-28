import csv
import re

filename = input("Enter the CSV file name (with extension): ")

with open(filename, 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    extracted_sentences = []

    for row in reader:
        english_sentence = row[0]
        sentences = re.split(r'(?<=[.!?])\s+', english_sentence)
        for sentence in sentences:
            extracted_sentences.append(sentence)

extracted_sentences = list(set(extracted_sentences))

with open('output.txt', 'w', encoding='utf-8') as txtfile:
    for sentence in extracted_sentences:
        txtfile.write(sentence + '\n')

print("Extracted English sentences (with duplicates removed) have been saved to 'output.txt'")

