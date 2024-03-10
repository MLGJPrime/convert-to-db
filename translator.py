"""
This module provides a function to translate French phrases to German.
It includes a main function for testing purposes.
"""

from googletrans import Translator
from tqdm import tqdm
from httpcore import ReadTimeout


def translate_to_german(word_tuples, retries=3):
    """Translates a list of French phrases to German."""
    translator = Translator()
    pbar = tqdm(range(len(word_tuples)), desc="Translating phrases")
    for i in pbar:
        phrase, translation = word_tuples[i]
        for _ in range(retries):
            try:
                translated_phrase = translator.translate(phrase.lower(), src='fr', dest='de').text  # noqa: E501
                word_tuples[i] = (translated_phrase.lower(), translation)
                break
            except AttributeError:
                tqdm.write(f"Error translating phrase: {phrase}")
                break
            except ReadTimeout:
                tqdm.write(f"Timeout error translating phrase: {phrase}. Retrying...")  # noqa: E501
        else:
            tqdm.write(f"Failed to translate phrase: {phrase} after {retries} attempts.")  # noqa: E501
    return [word_tuple for word_tuple in word_tuples if word_tuple[0] is not None]  # noqa: E501


def main():
    """Main function for testing the translate_to_german function."""
    word_tuples = [
        ("je suis allé au marché", "i went to the market"),  # noqa: E501
        ("il fait très chaud aujourd'hui", "it's very hot today"),  # noqa: E501
        ("j'aime manger des fruits", "i like eating fruits"),  # noqa: E501
        ("elle a un joli sourire", "she has a nice smile"),  # noqa: E501
        ("nous allons à la plage demain", "we are going to the beach tomorrow"),  # noqa: E501
        ("c'est une belle journée pour une promenade", "it's a beautiful day for a walk"),  # noqa: E501
        ("je suis content de te voir", "i am happy to see you"),  # noqa: E501
    ]
    translated_tuples = translate_to_german(word_tuples)
    for word_tuple in translated_tuples:
        print(word_tuple)


if __name__ == "__main__":
    main()
