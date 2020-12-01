class OrderedSet:
    def __init__(self, *args):
        _list = list()
        _set = set()
        if len(args) == 0:
            pass
        elif len(args) == 1:
            if hasattr(args[0], '__iter__'):
                for element in args[0]:
                    if element not in self:
                        self._set.append(element)
                        self._list.append(element)
            else:
                self._set.append(args[0])
                self._list.append(args[0])
        else:
            for element in args:
                self._set.append(args[0])
                self._list.append(args[0])

    def __in__(self, element):
        return element in self._set

    def __len__(self):
        return len(self._list)

    def __iter__(self):
        for element in self._list:
            yield element
