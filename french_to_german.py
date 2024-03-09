from extract_words import (
    extract_word_classes,
    generate_class_id_map,
    generate_word_class_dicts,
    generate_word_pair_dicts
)


def process_french_file(input_file_path):
    with open(input_file_path, 'r') as file:
        content = file.read()

    word_classes = extract_word_classes(input_file_path)
    class_id_map = generate_class_id_map(word_classes)

    word_class_dicts = generate_word_class_dicts(word_classes)
    word_pair_dicts = generate_word_pair_dicts(
        word_classes, class_id_map, content
    )

    return word_class_dicts, word_pair_dicts


def main():
    input_file_path = 'french.txt'
    word_class_dicts, word_pair_dicts = process_french_file(input_file_path)
    return word_class_dicts, word_pair_dicts


if __name__ == "__main__":
    main()
