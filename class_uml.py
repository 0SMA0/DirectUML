class ClassUML:

    # Will need to take care of how to know that things are connected
    def __init__(self, name, states, methods):
        self.__name = name
        self.__states = states
        self.__methods = methods
        

    def get_name(self):
        return self.__name[0]
    
    def get_states(self):
        return self.__states
    
    def get_methods(self):
        return self.__methods
    
    def set_name(self, new_name):
        self.__name = new_name

    def set_states(self, new_states):
        self._states = new_states

    def set_methods(self, new_methods):
        self.__methods = new_methods
        
