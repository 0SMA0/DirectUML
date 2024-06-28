def read_entire_file(filename):
    lines = ""
    file = open(filename, 'r')
    text = file.readlines()
    for line in text:
        lines += line
    file.close
    print(lines)
    return lines

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

def get_fields(seperated_text):
    for word in seperated_text:
        for char in word:
            if char == ";":
                print(word)
    print("done")            
    return None

def main():
    text = read_entire_file("testing.java")
    # print(type(text))
    seperated = split_text(text)
    print(get_class_name(seperated))
    get_fields(seperated)


if __name__ == "__main__":
    main()
