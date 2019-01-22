class Color:
    COLORS = {
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
    }

    def __init__(self, color):
        if not color in self.COLORS:
            raise Exception
        self.color = self.COLORS[color]

    def __call__(self, f):
        def inner(*args, **kwargs):
            res = f(*args, **kwargs)
            return "{c}{res}\033[0m".format(c=self.color, res=res)
        return inner



class ColorGenerator:
    # def __call__(self, c):
    #     decorator = Color(c)
    #     return decorator
    def __getattr__(self, item):
        if item in Color.COLORS:
            return Color(item)
        else:
            return super().__getattr__(item)


colorizer = ColorGenerator()


@Color('blue')
def echo(s):
    return s

print(echo("Hello"))