class Unpacker:
    def __init__(self, dict):
        for element in dict:
            self.__setattr__(element, dict[element])

    def __getitem__(self, element):
        return
