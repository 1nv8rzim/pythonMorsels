class MutableString:
    def __init__(self, string):
        self.string = list(str(string))

    def __str__(self):
        return str().join(element for element in self.string)

    def __repr__(self):
        return "'" + str(self) + "'"

    def __getitem__(self, key):
        return MutableString(str().join(element for element in self.string[key]))

    def __setitem__(self, key, value):
        self.string[key] = value

    def __delitem__(self, key):
        del self.string[key]

    def endswith(self, value):
        return str(self).endswith(value)

    def __add__(self, value):
        return MutableString(str(self) + value)

    def __radd__(self, value):
        return MutableString(value + str(self))

    def lower(self):
        return MutableString(str(self).lower())

    def upper(self):
        return MutableString(str(self).upper())

    def __contains__(self, value):
        return value in str(self)

    def __len__(self):
        return len(self.string)

    def __eq__(self, value):
        return value == str(self)

    def replace(self, key, value):
        return MutableString(str(self).replace(key, value))

    def append(self, value):
        self.string += value

    def insert(self, element, value):
        self.string.insert(element, value)

    def pop(self, element=None):
        return MutableString(self.string.pop(element)) if element is not None else MutableString(self.string.pop())
