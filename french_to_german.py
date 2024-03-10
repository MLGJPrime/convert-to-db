"""
This script translates phrases from French to German. It reads phrases
from an input file, translates them, and writes the translated phrases
to an output file.
"""

import time
from translator import translate_to_german


def translate_phrases(input_file_path):
    """Reads phrases from a file and translates them to German."""
    phrases = []

    with open(input_file_path, 'r') as f_in:
        for line in f_in:
            if '-' in line:
                try:
                    translation, phrase = line.split(' - ')
                except ValueError:
                    print(f"Error processing line: {line}")
                    continue
                if '*' in translation:
                    translation = translation.replace('*', '').strip() + '*'
                    phrase = '*' + phrase.replace('*', '').strip()
                phrases.append((phrase, translation))

    translated_phrases = translate_to_german(phrases)

    return translated_phrases


def write_translated_phrases(output_file_path, translated_phrases):
    """Writes translated phrases to a file."""
    with open(output_file_path, 'w') as f_out:
        for i, (phrase, translation) in enumerate(translated_phrases):
            if '*' in translation:
                if i == 0:
                    f_out.write(f'{phrase} - {translation}\n')
                else:
                    f_out.write(f'\n{phrase} - {translation}\n')
            else:
                f_out.write(f'{phrase} - {translation}\n')


def main():
    """Main function that orchestrates the translation process."""
    start_time = time.time()

    input_file_path = 'french.txt'
    output_file_path = 'german.txt'
    translated_phrases = translate_phrases(input_file_path)
    write_translated_phrases(output_file_path, translated_phrases)

    end_time = time.time()
    print(f"Time elapsed: {end_time - start_time} s")


if __name__ == "__main__":
    main()
