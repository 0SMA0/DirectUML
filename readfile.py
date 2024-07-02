import re


def read_entire_file(filename):
    lines = ""
    file = open(filename, 'r')
    text = file.readlines()
    for line in text:
        lines += line
    file.close
    return lines


def read_entire_file_list(filename):
    each_line = []
    file = open(filename, 'r')
    text = file.readlines()
    for line in text:
        each_line.append(line)
    file.close
    return each_line


def split_text_list(text):
    updated_list = []
    no_imports = text[1:]
    # print(no_imports)
    for line in no_imports:
        striped_line = line.strip()
        updated_list.append(striped_line)
    return updated_list


def split_text(texts):
    # seperated text contains imports
    seperated = texts.split()

    # find the index where it has the first public and then copy everything from there by slicing everything before it
    index = seperated.index('public')
    no_import_text = seperated[index:]

    return no_import_text


def get_class_name(seperated_text):
    index = 1

    for text in seperated_text:
        if text == 'class':
            index += 1

    class_name = seperated_text[index]
    return class_name


def get_fields(list_text):
    private_fields_list = []
    public_fields_list = []
    enumerated_list = enumerate(list_text)
    for words in enumerated_list:
        public_fields = re.search("^public.*;$", str(words[1]))
        private_fields = re.search("^private.*;$", str(words[1]))
        if public_fields:
            public_fields_list.append(words[1])
        elif private_fields:
            private_fields_list.append(words[1])
    return public_fields_list, private_fields_list

def get_methods(list_text):
    private_methods_list = []
    public_methods_list = []
    enumerated_list = enumerate(list_text)
    for words in enumerated_list:
        # later in the future will need to change this so that it can look at other formats
        public_methods = re.search("^public.*{$", str(words[1]))
        private_fields = re.search("^private.*{$", str(words[1]))
        if public_methods:
            public_methods_list.append(words[1])
        elif private_fields:
            private_methods_list.append(words[1])
    return public_methods_list, private_methods_list


def main():
    file = "testing.java"
    text = read_entire_file(file)
    text_list = read_entire_file_list(file)
    seperated_text = split_text(text)
    print("class name: ", get_class_name(seperated_text))
    seperated_list = split_text_list(text_list)
    print("fields: ", get_fields(seperated_list))
    print("methods: ", get_methods(seperated_list))


if __name__ == "__main__":
    main()
