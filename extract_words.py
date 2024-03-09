"""
This script processes a text file containing French phrases
and their translations. It extracts word classes and word pairs,
generates unique IDs for them, and saves the results into separate text files.
"""

import re


def extract_word_classes(file_path):
    """Extracts word classes from the given file."""
    with open(file_path, 'r') as file:
        content = file.read()
    word_classes = re.findall(r'\*([^*]*)\*', content)
    return word_classes


def extract_word_pairs(content):
    """Extracts word pairs from the given content."""
    pattern = r'(\b\w+\b)\s*-\s*(.*)'
    word_pairs = re.findall(pattern, content)
    return word_pairs


def generate_class_id_map(word_classes):
    """Generates a map from word classes to unique IDs."""
    return {word_class: idx+1 for idx, word_class in enumerate(word_classes)}


def print_and_save(word_dicts, headers, file_name):
    """Prints the word dictionaries and saves them to a file."""
    max_widths = [len(header) for header in headers]
    for word_dict in word_dicts:
        max_widths = [
            max(max_width, len(str(word_dict[header])))
            for max_width, header in zip(max_widths, headers)
        ]

    header_line = " | ".join(
        f"{header}{' ' * (max_width - len(header))}"
        for header, max_width in zip(headers, max_widths)
    )

    print(header_line)
    for word_dict in word_dicts:
        print(" | ".join(
            f"{word_dict[header]:{max_width}}"
            for header, max_width in zip(headers, max_widths)
        ))

    with open(file_name, 'w') as f:
        f.write(header_line + "\n")
        for word_dict in word_dicts:
            f.write(" | ".join(
                f"{word_dict[header]:{max_width}}"
                for header, max_width in zip(headers, max_widths)
            ) + "\n")


def generate_word_class_dicts(word_classes):
    """Generates a list of dictionaries."""
    word_class_dicts = []
    for idx, word_class in enumerate(word_classes):
        name, translation = map(str.strip, word_class.split('-'))
        word_class_dicts.append({
            "Class ID": idx+1,
            "Name": name,
            "Translation": translation
        })
    return word_class_dicts


def generate_word_pair_dicts(word_classes, class_id_map, content):
    """.Generates a list of dictionaries."""
    word_pair_dicts = []
    for idx, word_class in enumerate(word_classes):
        if idx < len(word_classes) - 1:
            pattern = re.escape(word_class) + r'(.*?)' \
                      + re.escape(word_classes[idx+1])
        else:
            pattern = re.escape(word_class) + r'(.*)$'
        word_class_content = re.search(pattern, content, re.DOTALL).group(1)
        word_pairs = extract_word_pairs(word_class_content)
        for original, translation in word_pairs:
            class_id = class_id_map[word_class]
            unique_id = word_pairs.index((original, translation)) + 1
            word_pair_dicts.append({
                "Word Pair ID": unique_id,
                "Class ID": class_id,
                "Phrase": original,
                "Translation": translation
            })
    return word_pair_dicts


def process_file(input_file_path):
    """Extracts word classes and word pairs, and saves the results."""
    with open(input_file_path, 'r') as file:
        content = file.read()

    word_classes = extract_word_classes(input_file_path)
    class_id_map = generate_class_id_map(word_classes)

    word_class_dicts = generate_word_class_dicts(word_classes)
    word_pair_dicts = generate_word_pair_dicts(
        word_classes, class_id_map, content)

    print_and_save(
        word_class_dicts,
        ["Class ID", "Name", "Translation"],
        'word_classes.txt'
    )
    print_and_save(
        word_pair_dicts,
        ["Word Pair ID", "Class ID", "Phrase", "Translation"],
        'word_pairs.txt'
    )


def main():
    input_file_path = 'french.txt'
    process_file(input_file_path)


if __name__ == "__main__":
    main()
