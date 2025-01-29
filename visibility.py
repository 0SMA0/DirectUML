from enum import Enum

class Visibility(Enum):
    PUBLIC = '+'
    PRIVATE = '-'
    PROTECTED = "#"
print(Visibility.PRIVATE.name)