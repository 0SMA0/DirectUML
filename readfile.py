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
    class_name = ""
    for text in seperated_text:
        if(text is 'public'):
            class_name += text
            



def main():
    text = read_entire_file("testing.java")
    # print(type(text))
    split_text(text)

if __name__ == "__main__":
    main()