class MutableString:
    def __init__(self, string):
        self.string = list(string)

    def __str__(self):
        return str().join(element for element in self.string)

    def __repr__(self):
        return str(self)
