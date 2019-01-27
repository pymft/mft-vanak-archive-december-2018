num = 1


def fun():
    return 1


class Rectangle:
    num = 1

    def __init__(self, w, h):
        self.w = w
        self.h = h
        # init will return None

    # def __getitem__(self, item):

    @property
    def area(self):
        return self.w * self.h

    def fun(self):
        return 1


rect = Rectangle(2, 3)
rect.area = 100
rect.fun()
lst = [1, 2, 3, 4]
tup = (1,2, 3)
dct = {'a': 100}
lst[0]   # lst.__getitem__(0)
dct['a']

Rectangle.fun(rect)