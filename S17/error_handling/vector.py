class Vector:
    def __init__(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise ValueError
            # print("Error Not Valid!!!")

        self.x = x
        self.y = y


try:
    v = Vector(43,  345)
    print(v.x, v.y)
except ValueError:
    print("it's not a valid vector")