class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def compute_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)


vec1 = Vector(10, 6)  # instantiation, construction
vec2 = Vector(1, 2)
print(vec1.x)
print(vec1.y)
print(vec1.compute_length())

# adding instances together
vec3 = vec1 + vec2
# # from instance point of view
# vec1.__add__(vec2)
#
# # from class point of view
# Vector.__add__(vec1, vec2)
