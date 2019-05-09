import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setxy(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # __truediv__ overrides /, ie 5/2 == 2.5
    # __floordiv__ overrides //, ie 5//2 == 2 (integer division)
    def __truediv__(self, divisor):
        return Vector(self.x / divisor, self.y / divisor)

    def __mul__(self, multiplier):
        return Vector(self.x * multiplier, self.y * multiplier)

    def mag(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def arg(self):
        """ returns in degrees
        """
        return math.atan(self.y / self.x) * 180 / math.pi

    def unit_vector(self):
        return self / self.mag()

    @staticmethod
    def createUnitVectorFromAngle(angle):
        """ angle in degrees
        """
        radians = angle * math.pi / 180
        return Vector(math.cos(angle), math.sin(angle))

    @staticmethod
    def createUnitVector(x, y):
        return (Vector(x, y)).unit_vector()
