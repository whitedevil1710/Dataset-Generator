# Dataset-Generator

This repository contains code for generating datasets from English text files. The process involves two main steps - extracting English sentences from a text file, and translating those sentences into another language using the Google Translate API.
## Requirements
To run the code, you will need to have the following installed on your machine:

+ Python 3.x
+ pip
+ Required Python libraries (googletrans, pandas, tqdm)
You can install the required Python libraries by running the setup.sh script:
```
bash setup.sh
```
## Usage

- Step 1: Extract English sentences from text file
To extract English sentences from a text file, run the extractor.py script:
```
python3 extractor.py
```
You will be prompted to enter the filename of the text file containing the source sentences. The extracted sentences will be saved to a file called output.txt.

- Step 2: Translate sentences into another language
To translate the extracted English sentences into another language, run the dataset.py script:

```
python3 dataset.py
```
You will be prompted to enter the source language, target language, filename of the text file containing the source sentences, and filename for the output CSV file. The translated sentences will be saved to the output CSV file.

> ### Notes
> + The Google Translate API has usage limits. If you encounter errors during translation, try reducing the number of sentences you are translating at a
> time, or wait a while before trying again.
> + If you need to continue the translation process from where you left off, run the dataset.py script again and choose to continue from a saved progress
> file when prompted. This will resume the translation process from where it was last saved.
> + If you encounter errors during the translation process, the script will continue translating the remaining sentences. Any sentences that were 
> successfully translated before the error occurred will be saved to the output CSV file. A log of the errors will be printed to the console at the end 
> of the process.
> + The extracted English sentences may contain duplicates. These duplicates are removed before the sentences are translated.

## Author

This script was created by [white_devil](https://github.com/whitedevil1710).
