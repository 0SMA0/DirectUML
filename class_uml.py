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
        public_states_lst = self.get_public_states()
        names = self.iterate_state_names(public_states_lst)
        return names if len(names)!=0 else None

    def get_private_states_name_lst(self):
        private_states_lst = self.get_private_states()
        names = self.iterate_state_names(private_states_lst)
        return names if len(names)!=0 else None

    def get_protected_states_name_lst(self):
        protected_states_lst = self.get_protected_states()
        names = self.iterate_state_names(protected_states_lst)
        return names if len(names)!=0 else None

    def get_states_return_type_lst(self):
        return_type_lst = []
        for state in self.__states:
            for thing in state:
                return_type_lst.append(thing[1])
        return return_type_lst

    def get_methods(self):
        return self.__methods

    def set_name(self, new_name):
        self.__name = new_name

    def set_states(self, new_states):
        self._states = new_states

    def set_methods(self, new_methods):
        self.__methods = new_methods
