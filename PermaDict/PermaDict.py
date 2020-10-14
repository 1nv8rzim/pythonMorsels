from collections import UserDict


class PermaDict(UserDict):

    def __init__(self, *args):
        super().__init__(*args)

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(f"'{key}' already in dictionary")
        super().__setitem__(key, value)
