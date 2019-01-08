a = [1, 2]


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    @length.setter
    def length(self, value):
        ratio = value / self.length
        self.x *= ratio
        self.y *= ratio




v = Vector(3, 4)
print(v.length)

v.length = 100
print(v.length, v.x, v.y)