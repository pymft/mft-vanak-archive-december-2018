class Pizza:
    def __init__(self, *ingredients):
        self.ingredients = ingredients


class PizzaMakerMaker:
    INFO = {
        'margarita': ('cheese', 'tomato'),
        'pepperoni': ('mushroom', 'cheese', 'pepper')
    }

    def __init__(self, pizza_type):
        if not pizza_type in self.INFO:
            raise ValueError

        self.input = self.INFO[pizza_type]

    def __call__(self):
        return Pizza(*self.input)


MargaritaMaker = PizzaMakerMaker('margarita')
PepperoniMaker = PizzaMakerMaker('pepperoni')

m1 = MargaritaMaker()
p1 = PepperoniMaker()