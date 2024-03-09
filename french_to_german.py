import time
from translator import translate_to_german


def translate_phrases(input_file_path):
    phrases = []

    with open(input_file_path, 'r') as f_in:
        for line in f_in:
            if '-' in line:
                translation, phrase = line.split('-')
                if '*' in translation:
                    translation = translation.replace('*', '').strip() + '*'
                    phrase = '*' + phrase.replace('*', '').strip()
                phrases.append((phrase, translation))

    translated_phrases = translate_to_german(phrases)

    return translated_phrases


def write_translated_phrases(output_file_path, translated_phrases):
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
    start_time = time.time()

    input_file_path = 'french.txt'
    output_file_path = 'german.txt'
    translated_phrases = translate_phrases(input_file_path)
    write_translated_phrases(output_file_path, translated_phrases)

    end_time = time.time()
    print(f"Time elapsed: {end_time - start_time} s")


if __name__ == "__main__":
    main()
