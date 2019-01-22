class Square:
    instances = []

    def __new__(cls, a):
        for instance in cls.instances:
            if instance.a == a:
                return instance
        return super().__new__(cls)


    def __init__(self, a):
        self.instances.append(self)
        print(a)
        self.a = a

    def cal_area(self):
        return self.a ** 2



s1 = Square(1)
print(id(s1))

s2 = Square(1)
print(id(s2))