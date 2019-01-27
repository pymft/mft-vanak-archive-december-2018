def fun1(x, y, z):
    return (x + y + z) ** 2


fun2 = lambda x, y, z: (x + y + z) ** 2

lst = [211, -4352, 233, 4, 5, 6, 7]

lst.sort(key=lambda x: x**2)
print(lst)