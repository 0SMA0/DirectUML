class PlantUML_fields:
    def __init__(self, visability, name, return_type):
        self.__visability = visability
        self.__name = name
        self.__return_type = return_type
    
    def create_field(self, index):
        # __return_type is a list
        result = self.__visability + " " + self.__name + " : " + self.__return_type[index]
        return result
    
class CreateUML:

    def format_fields(states_name_lst, return_types_lst):    
        print("name:", states_name_lst)
        print("return types:", return_types_lst)
        
        # Validate inputs
        if len(states_name_lst) < 2 or len(return_types_lst) < 2:
            return None
        if not states_name_lst[1]:  # If field names list is empty
            return None

        visibility = states_name_lst[0]  # Extract visibility
        field_names = states_name_lst[1]  # Extract field names
        return_types = return_types_lst[1]  # Extract return types

        fields = []

        for i, name in enumerate(field_names):
            # Ensure a return type exists at the same index, otherwise default to None
            return_type = return_types[i] if i < len(return_types) else None
            if return_type is None:
                continue  # Skip if return type is missing

            # Create a PlantUML field
            field = PlantUML_fields(visibility, name, return_type).create_field(i)
            fields.append(field)

        return fields


    def write(class_name, ):

        stuff = f"""@startuml
skinparam classAttributeIconSize 0
class {class_name} {{



}}

                       
@enduml
            """

        with open('text.txt', "w") as file:

            # start the file
            file.write(stuff)
            # will need to move to the next line to start writting the required information

            pass


if __name__ == "__main__":
    CreateUML.format_fields()
