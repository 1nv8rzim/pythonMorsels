from math import pi
class Circle:
    def __init__(self, temp=1):
        if temp < 0:
            raise ValueError('Radius cannot be negative')
        else:
            self.temp = temp
    
    @property
    def diameter(self):
        return self.temp * 2
    
    @property
    def area(self):
        return self.temp ** 2 * pi

    @property
    def radius(self):
        return self.temp

    @diameter.setter
    def diameter(self, x):
        if x < 0:
            raise ValueError('Radius cannot be negative')
        else:
            self.temp = x / 2

    @area.setter
    def area(self, x):
        raise AttributeError()

    @radius.setter
    def radius(self, x):
        if x < 0:
            raise ValueError('Radius cannot be negative')
        else:
            self.temp = x
        
    def __str__(self):
        return f'Circle({self.radius})'
    
    def __repr__(self):
        return str(self)
