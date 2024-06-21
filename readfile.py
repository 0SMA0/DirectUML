def read_entire_file(filename):
    lines = ""
    file = open(filename,'r')
    text = file.readlines()
    for line in text:
        lines += line
    file.close
    return lines

def split_text(texts):
    seperated = texts.split()
    return seperated

def get_class_name(seperated_text):
    index = 0
    for text in seperated_text:
        if text == 'class':
            index+=1

    class_name = seperated_text[index+1]
    return class_name

            



def main():
    text = read_entire_file("testing.java")
    # print(type(text))
    seperated = split_text(text)
    print(get_class_name(seperated))

if __name__ == "__main__":
    main()