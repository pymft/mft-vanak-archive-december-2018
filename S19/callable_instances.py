


class Multiply:
    def __init__(self, n):
        self.n = n

    def __call__(self, f):
        def inner(inp):
            return f(inp) * self.n
        return inner


def multiply(n):
    def decorator(f):
        def inner(inp):
            return n * f(inp)
        return inner
    return decorator

# multiply(10)(echo)

@multiply(10)
#@Multiply(10)
def echo(s):
    return s

print(echo("hello "))


# m10 = Multiply(10)
# d10 = decorator_multiply(10)
#
# res = m10(20)
# print(res)
#
# res = d10(20)
# print(res)