from docx import Document


def convert_word_to_txt(word_file_path, txt_file_path):
    doc = Document(word_file_path)
    output = []

    for para in doc.paragraphs:
        for run in para.runs:
            if run.bold:
                output.append(f"*{run.text}*")
            else:
                output.append(run.text)

    with open(txt_file_path, 'w') as f:
        f.write('\n'.join(output))


def main():
    # Usage
    convert_word_to_txt('french.docx', 'french.txt')


if __name__ == "__main__":
    main()
