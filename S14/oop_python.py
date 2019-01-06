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

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)

    # ** __pow__  , *   __mul__  , /  __div__, + __add__, - __sub__
    # >  __gt__   , >=  __ge__
    # <  __lt__   , <=  __le__
    # == __eq__   , !=  __ne__

    

vec1 = Vector(10, 6)  # instantiation, construction
vec2 = Vector(1, 2)

vec3 = vec1 + vec2
# vec1 > vec2
print(vec3.compute_length())
