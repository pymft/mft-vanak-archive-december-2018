class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    @area.setter
    def area(self, value):
        ratio = (value / self.area) ** 0.5
        self.height *= ratio
        self.width *= ratio

    @property
    def perimeter(self):
        return  2 * (self.width + self.height)

    @perimeter.setter
    def perimeter(self, value):
        ratio = value / self.perimeter
        self.height *= ratio
        self.width *= ratio

    # def __repr__(self):
    #     out = '+' + '-' * self.width + '+ \n'
    #     for i in range(self.height-2):
    #         out += '|' + ' '*(self.width) + '| \n'
    #     out += '+' + '-' * self.width + '+ \n'
    #     return out


rec = Rectangle(2, 4)
print(rec.width, rec.height)
print(rec.area, rec.perimeter)

rec.width = 1
print(rec.width, rec.height)
print(rec.area, rec.perimeter)

rec.area = 16

print(rec.width, rec.height)
print(rec.area, rec.perimeter)

rec.perimeter = 3
print(rec.width, rec.height)
print(rec.area, rec.perimeter)