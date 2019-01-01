class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __add__(self, other):
        x_new = self.x + other.x
        y_new = self.y + other.y
        return Vector(x_new, y_new)

v1 = Vector(1, 2)
v2 = Vector(5, 8)

v3 = v1 + v2    #  v1.__add__(v2)
print(v1.x, v1.y, v1.length())
print(v2.x, v2.y, v2.length())
print(v3.x, v3.y, v3.length())