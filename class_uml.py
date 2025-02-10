from visibility import Visibility
class ClassUML:

    # Will need to take care of how to know that things are connected
    def __init__(self, name, states, methods):
        self.__name = name
        self.__states = states
        self.__methods = methods

    def get_name(self):
        return self.__name[0]

    def get_public_states(self):
        return self.__states[0]

    def get_private_states(self):
        return self.__states[1]

    def get_protected_states(self):
        return self.__states[2]

    def iterate_state_names(self, lst):
        state_names_lst = []
        for state in lst:
            state_name = state[2]
            checked_word = ""
            for letter in state_name:
                if letter != ";":
                    checked_word += letter
            state_names_lst.append(checked_word)
        return state_names_lst

    def get_public_states_name_lst(self):
        names = [Visibility.PUBLIC.value]
        public_states_lst = self.get_public_states()
        names.append(self.iterate_state_names(public_states_lst))
        return names if len(names)!=0 else None

    def get_private_states_name_lst(self):
        names = [Visibility.PRIVATE.value]
        private_states_lst = self.get_private_states()
        names.append(self.iterate_state_names(private_states_lst))
        return names if len(names)!=0 else None

    def get_protected_states_name_lst(self):
        names = [Visibility.PUBLIC.value]
        protected_states_lst = self.get_protected_states()
        names = self.iterate_state_names(protected_states_lst)
        return names if len(names)!=0 else None

    def iterate_state_return_types(self, lst):
        return_type_lst = []
        for state in lst:
            return_type_lst.append(state[1])
        return return_type_lst

    def get_public_return_types(self):
        public_states_lst = self.get_public_states()
        return_types = [Visibility.PUBLIC.value]
        return_types.append(self.iterate_state_return_types(public_states_lst))
        return return_types if len(return_types)!=0 else None
    
    def get_private_return_type(self):
        private_states_lst = self.get_private_states()
        return_types = [Visibility.PRIVATE.value]
        return_types.append(self.iterate_state_return_types(private_states_lst))
        return return_types if len(return_types)!=0 else None
    
    def get_protected_return_types(self):
        protected_states_lst = self.get_protected_states()
        return_types = [Visibility.PROTECTED.value]
        return_types.append(self.iterate_state_return_types(protected_states_lst))
        return return_types if len(return_types)!=0 else None
    
# print(example_uml.get_public_states_name_lst())
# print(example_uml.get_public_return_types())
        # ['body', 'leg']
        # ['String', 'String']

# Because we parsed it with the thought of the visablity, we can just add it as public
