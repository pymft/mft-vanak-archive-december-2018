class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

v1 = Vector(1, 2)
v2 = Vector(5, 8)

print(v1.x, v1.y, v1.length())
print(v2.x, v2.y, v2.length())