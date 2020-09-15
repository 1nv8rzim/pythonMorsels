class Vector:

    __slots__ = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

    def __eq__(self, other):
        if isinstance(other, Vector):
            if (self.x == other.x and self.y == other.y and self.z == other.z):
                return True
        return False