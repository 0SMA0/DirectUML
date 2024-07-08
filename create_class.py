import readfile_java

text_list = readfile_java.read_entire_file_list("testing.java")
seperated_text_list = readfile_java.split_text_list(text_list)
methods = readfile_java.get_methods(seperated_text_list)

class Field:
    def __init__(self,visibility, isFinal, isStatic, returnType, name):
        self.visibility = visibility
        self.isFinal = isFinal
        self.isStatic = isStatic
        self.retunType = returnType
        self.name = name

class Method:
    def __init__(self, visibility, isFInal, isStatic, returnType, name):
        self.visibility = visibility
        self.isFinal = isFInal
        self.isStatic = isStatic
        self.retunType = returnType
        self.name = name
    
class ClassUML:
    def __init__(self, fields: Field, methods: Method):
        self.field = fields
        self.method = methods