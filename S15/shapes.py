class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        print("rectangle area")
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2


class Square(Rectangle):
    def __init__(self, width):
        super().__init__(width, width)

    def area(self):
        print("square area")
        # super().area()
        return self.width ** 2


s = Square(10)
print(s.area())
