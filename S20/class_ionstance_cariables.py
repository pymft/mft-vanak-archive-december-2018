class A:
    num = 1
    def __init__(self):
        self.var = 100


a = A()
a.num   # 1
print(a.__dict__)
a.num = 100     # self.num
a.num
print(a.__dict__)

a2 = A()
a.num   # 1


A.num   # 1
A.num = 1001
a2.num
