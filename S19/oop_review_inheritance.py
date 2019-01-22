import random
from turtle import Turtle


class SuperTurtle(Turtle):
    MY_COLORS = ['red', 'black', 'blue', 'green', 'yellow', 'cyan']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        tmp_color = random.choice(self.MY_COLORS)
        self.color(tmp_color)

    def spiral2(self, l, n, a):
        if n == 1:
            self.forward(n)
        else:
            self.forward(l)
            self.left(90)
            self.spiral2(l*a, n-1, a)

    def spiral(self, n, a):
        self.speed(0)
        for i in range(n):
            self.forward(100 - i * a)
            self.left(90)



t1 = SuperTurtle()
t2 = SuperTurtle()

t1.spiral(20,5)

t2.spiral2(300, 40, 0.9)
input("press RETURN to exit")