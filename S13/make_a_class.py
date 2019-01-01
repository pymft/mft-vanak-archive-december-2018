class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(self.name, "says hello!")


p1 = Person('Jack')
p2 = Person('John')
p1.say_hello()
p2.say_hello()
