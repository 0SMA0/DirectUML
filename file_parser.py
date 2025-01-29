from __future__ import annotations
from abc import ABC, abstractmethod
import re
from class_uml import ClassUML

# Current Idea is to use Abstract Factory

# Abstract Factory solves the problem of creating entire product families without specifying their concrete classes.

# Does not take in ADT into account yet


class FileParserFactory(ABC):

    @abstractmethod
    def create_parser(self) -> AbstractParserJava:
        pass


class JavaParserFactory(FileParserFactory):

    def create_parser(self) -> AbstractParserJava:
        return ConcreteJavaParser()


class AbstractParserJava(ABC):
    @abstractmethod
    def parse(self) -> str:
        pass


class ConcreteJavaParser(AbstractParserJava):
    def parse(self, file_name) -> str:
        important_lines = {
            "class_name": [],
            "public_fields": [],
            "private_fields": [],
            "protected_fields": []
        }

        lines = self.read_file(file_name)
        for line in lines:
            if class_name := self.find_class_name(line):
                important_lines["class_name"].append(class_name)
            elif public_field := self.find_field(line, "public"):
                important_lines["public_fields"].append(public_field)
            elif private_field := self.find_field(line, "private"):
                important_lines["private_fields"].append(private_field)
            elif protected_field := self.find_field(line, "protected"):
                important_lines["protected_fields"].append(protected_field)

        return important_lines

    def read_file(self, file_name) -> list[str]:
        """Reads the file and returns a list of lines."""
        with open(file_name, 'r') as file:
            return file.readlines()

    def find_class_name(self, line: str) -> str | None:
        """Extracts the class name if the line defines a class."""
        pattern = r"public\s+class\s+(\w+)\s*\{"
        match = re.search(pattern, line)
        return match.group(1) if match else None

    def find_field(self, line: str, access_modifier: str) -> str | None:
        """Extracts fields based on the access modifier."""
        pattern = rf"{access_modifier}\s+\w+\s+\w+\s*;"
        adt_field_pattern = rf"{access_modifier}\s+\w+<\w+(,\s*\w+)*>\s+\w+\s*;"
        adt_initialization_pattern = rf"{access_modifier}\s+\w+<\w+(,\s*\w+)*>\s+\w+\s*=\s*new\s+\w+<.*?>\s*\(\s*\)\s*;"
        match = re.search(pattern, line) or re.search(adt_field_pattern, line) or re.search(adt_initialization_pattern, line)
        return match.group(0).strip() if match else None
    
    
    


if __name__ == "__main__":
    javafactory = JavaParserFactory()
    javaparser = javafactory.create_parser()
    dict = javaparser.parse("Dog.java")
    class_name = dict["class_name"]
    public_fields = dict["public_fields"]
    private_fields = dict["private_fields"]
    protected_fields = dict["protected_fields"]
    states = [public_fields, private_fields, protected_fields]
    methods = None
    example_uml = ClassUML(class_name, states, methods)
    print(example_uml.get_states())
    