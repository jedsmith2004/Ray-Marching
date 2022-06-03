import math


class Vector2:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __add__(a ,b):
        if type(b) == Vector2:
            return Vector2(a. x + b.x, a. y + b.y)
        return Vector2(a. x +b, a. y + b)

    def __sub__(a ,b):
        if type(b) == Vector2:
            return Vector2(a. x -b.x ,a. y -b.y)
        return Vector2(a. x -b ,a. y -b)

    def __mul__(a ,b):
        if type(b) == Vector2:
            return Vector2(a. x *b.x ,a. y *b.y)
        return Vector2(a. x *b ,a. y *b)

    def __truediv__(a ,b):
        if type(b) == Vector2:
            return Vector2(a. x /b.x ,a. y /b.y)
        if b == 0:
            return a

        return Vector2(a. x /b ,a. y /b)

    def get_tuple(self):
        return (self.x ,self.y)

    def __repr__(self):
        return "Instance of Vector2. Address: " +hex(id(self))

    def __str__(self):
        return f"Vector2({self.x}, {self.y})"

    def __getitem__(self, index):
        if index == 0: return self.x
        elif index == 1: return self.y
        else: raise IndexError

    def dot(self ,b):
        return sum((self * b).get_tuple())

    def cross(self ,b):
        if type(b) == Vector2: return ((self.x*b.y)-(self.y*b.x))
        elif type(b) == list or type(b) == tuple:
            if len(b) == 2: return ((self.x*b[1])-(self.y*b[0]))

    def max(self, b):
        return Vector2(max(self.x, b.x), max(self.y, b.y))

    def min(self, b):
        return Vector2(min(self.x, b.x), min(self.y, b.y))

    def abs(self):
        return Vector2(abs(self.x), abs(self.y))

    def length(self):
        return math.sqrt(self.x**2 + self.y**2)

    def normalized(self):
        return self / self.length()