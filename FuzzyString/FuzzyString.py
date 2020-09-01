class FuzzyString:
    def __init__(self, string):
        self.string = string

    def __eq__(self, other):
        if not isinstance(other, str):
            return False
        return self.string.upper() == other.upper()

    def __str__(self):
        return self.string

    def __repr__(self):
        return f"'{self.string}'"

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        return self.string.upper() > other.upper()

    def __lt__(self, other):
        return self.string.upper() < other.upper()

    def __ge__(self, other):
        return self.string.upper() >= other.upper()

    def __le__(self, other):
        return self.string.upper() <= other.upper()