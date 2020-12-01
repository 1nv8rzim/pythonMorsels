class OrderedSet:
    def __init__(self, *args):
        self._list = list()
        self._set = set()
        if len(args) == 0:
            pass
        elif len(args) == 1:
            if hasattr(args[0], '__iter__'):
                for element in args[0]:
                    if element not in self._set:
                        self._set.add(element)
                        self._list.append(element)
            else:
                self._set.add(args[0])
                self._list.append(args[0])
        else:
            for element in args:
                self._set.add(args[0])
                self._list.append(args[0])

    def __contains__(self, element):
        return element in self._set

    def __len__(self):
        return len(self._list)

    def __iter__(self):
        for element in self._list:
            yield element

    def add(self, element):
        if element not in self._set:
            self._set.add(element)
            self._list.append(element)

    def discard(self, element):
        if element in self._set:
            self._set.discard(element)
            self._list.remove(element)

    def __eq__(self, other):
        if hasattr(other, '__iter__'):
            for i, j in zip(self._list, other):
                if i != j:
                    return False
        else:
            return False
        return True

    def __str__(self):
        return str(self._list)

    def __repr__(self):
        return repr(self._list)
