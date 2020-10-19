class MutableString:
    def __init__(self, string):
        self.string = list(string)

    def __str__(self):
        return str().join(element for element in self.string)

    def __repr__(self):
        return str(self)

    def __getitem__(self, key):
        return str().join(element for element in self.string[key])

    def __setitem__(self, key, value):
        self.string[key] = value

    def endswith(self, value):
        return self.string[-1] == value

    def __add__(self, value):
        return self.string + value

    def lower(self):
        return str(self).lower()

    def __in__(self, value):
        return value in str(self)

    def len(self):
        return len(self.string)
