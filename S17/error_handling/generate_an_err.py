def fact(n):
    f = 1
    while n > 0:
        f *= n
        n -= 1
    return f


out = fact(5)
print(out)