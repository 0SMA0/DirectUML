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
    enumerated_list = enumerate(list_text)
    for words in enumerated_list:
        public_fields = re.search("^public.*;$", str(words[1]))
        private_fields = re.search("^private.*;$", str(words[1]))
        if public_fields:
            print("Public Found")
            print(words[1])
        elif private_fields:
            print("Private Found")
            print(words[1])
        

def main():
    file = "testing.java"
    text = read_entire_file(file)
    text_list = read_entire_file_list(file)
    # print(type(text))
    seperated = split_text(text)
    seperated_list = split_text_list(text_list)
    # print(seperated_list)
    # print(get_class_name(seperated))
    get_fields(seperated_list)


if __name__ == "__main__":
    main()
