"""
This module provides a function to translate French phrases to German.
It includes a main function for testing purposes.
"""

from googletrans import Translator


def translate_to_german(word_tuples):
    """Translates a list of French phrases to German."""
    translator = Translator()
    for i in range(len(word_tuples)):
        phrase, translation = word_tuples[i]
        translated_phrase = translator.translate(
            phrase.lower(), src='fr', dest='de').text
        word_tuples[i] = (translated_phrase.lower(), translation)
    return word_tuples


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
