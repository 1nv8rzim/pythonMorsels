from collections.abc import MutableSet, Sequence


class OrderedSet(MutableSet):
    def __init__(self, items):
        self.items = dict.fromkeys(items, None)

    def __iter__(self):
        for item in self.items:
            yield item

    def __len__(self):
        return len(self.items)

    def __contains__(self, item):
        return item in self.items

    def add(self, item):
        self.items[item] = None

    def discard(self, item):
        self.items.pop(item, None)

    def __eq__(self, other):
        if not isinstance(other, OrderedSet):
            return self.items.keys() == other
        return tuple(self.items.keys()) == tuple(other.items.keys())

    def __getitem__(self, i):
        return list(self.items.items())[i][0]
