import re


def extract_word_classes(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    word_classes = re.findall(r'\*([^*]*)\*', content)
    return word_classes


def extract_word_pairs(content):
    pattern = r'(\b\w+\b)\s*-\s*(.*)'
    word_pairs = re.findall(pattern, content)
    return word_pairs


def generate_class_id_map(word_classes):
    return {word_class: idx+1 for idx, word_class in enumerate(word_classes)}


def main():
    input_file_path = 'french.txt'
    with open(input_file_path, 'r') as file:
        content = file.read()

    word_classes = extract_word_classes(input_file_path)
    class_id_map = generate_class_id_map(word_classes)

    word_class_dicts = []
    max_id_width = max_name_width = max_translation_width = len("Class ID")
    for idx, word_class in enumerate(word_classes):
        name, translation = map(str.strip, word_class.split('-'))
        word_class_dicts.append({"id": idx+1, "name": name, "translation": translation})
        max_name_width = max(max_name_width, len(name))
        max_translation_width = max(max_translation_width, len(translation))

    word_pair_dicts = []
    max_id_width_pair = max_phrase_width = max_translation_width_pair = len("Word Pair ID")
    for idx, word_class in enumerate(word_classes):
        if idx < len(word_classes) - 1:
            pattern = re.escape(word_class) + r'(.*?)' + re.escape(word_classes[idx+1])
        else:
            pattern = re.escape(word_class) + r'(.*)$'
        word_class_content = re.search(pattern, content, re.DOTALL).group(1)
        word_pairs = extract_word_pairs(word_class_content)
        for original, translation in word_pairs:
            class_id = class_id_map[word_class]
            unique_id = word_pairs.index((original, translation)) + 1
            word_pair_dicts.append({"id": unique_id, "class_id": class_id, "phrase": original, "translation": translation})
            max_id_width_pair = max(max_id_width_pair, len(str(unique_id)))
            max_phrase_width = max(max_phrase_width, len(original))
            max_translation_width_pair = max(max_translation_width_pair, len(translation))

    # Print word classes with headers
    print("Class ID" + " " * (max_id_width - len("Class ID") + 1) +
          "| Name" + " " * (max_name_width - len("Name") + 1) +
          "| Translation")
    for word_class_dict in word_class_dicts:
        print(f"{word_class_dict['id']:{max_id_width}} | {word_class_dict['name']:{max_name_width}} | {word_class_dict['translation']}")

    # Print word pairs with headers
    print("\nWord Pair ID" + " " * (max_id_width_pair - len("Word Pair ID") + 1) +
          "| Class ID" + " " * (max_id_width - len("Class ID") + 1) +
          "| Phrase" + " " * (max_phrase_width - len("Phrase") + 1) +
          "| Translation")
    for word_pair_dict in word_pair_dicts:
        print(f"{word_pair_dict['id']:{max_id_width_pair}} | {word_pair_dict['class_id']:{max_id_width}} | {word_pair_dict['phrase']:{max_phrase_width}} | {word_pair_dict['translation']}")

    # Save word classes into a text file
    with open('word_classes.txt', 'w') as f:
        f.write("Class ID" + " " * (max_id_width - len("Class ID") + 1) +
                "| Name" + " " * (max_name_width - len("Name") + 1) +
                "| Translation\n")
        for word_class_dict in word_class_dicts:
            f.write(f"{word_class_dict['id']:{max_id_width}} | {word_class_dict['name']:{max_name_width}} | {word_class_dict['translation']}\n")

    # Save word pairs into a text file
    with open('word_pairs.txt', 'w') as f:
        f.write("Word Pair ID" + " " * (max_id_width_pair - len("Word Pair ID") + 1) +
                "| Class ID" + " " * (max_id_width - len("Class ID") + 1) +
                "| Phrase" + " " * (max_phrase_width - len("Phrase") + 1) +
                "| Translation\n")
        for word_pair_dict in word_pair_dicts:
            f.write(f"{word_pair_dict['id']:{max_id_width_pair}} | {word_pair_dict['class_id']:{max_id_width}} | {word_pair_dict['phrase']:{max_phrase_width}} | {word_pair_dict['translation']}\n")


if __name__ == "__main__":
    main()
