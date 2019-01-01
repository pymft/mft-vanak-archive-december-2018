from turtle import Turtle


# t1 = Turtle()
# t3 = Turtle()
# t4 = Turtle()
# t5 = Turtle()
# t6 = Turtle()
#
# t1.color('red')
# t2.color('blue')
# t3.color('purple')
# t4.color('yellow')
# t5.color('green')
#
# t1.right(10)
# t1.forward(100)
# t2.right(20)
# t2.forward(150)
# t3.right(30)
# t3.forward(200)
# t4.right(40)
# t4.forward(250)
# t5.right(50)
# t5.forward(300)
# print(t1._pencolor)

t = Turtle()

t.speed(0)
colors = ['red', 'green', 'blue', 'black']
for i in range(200):
    t.forward(250-0.5*i)
    t.color(colors[i % 4])
    t.left(101)

input('press Enter to exit')