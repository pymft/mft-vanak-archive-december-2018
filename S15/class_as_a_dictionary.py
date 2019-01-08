class Example:
    """
    this is docstring
    """
    var = 10

    def __init__(self, x):
        self.x = x
        self.y = 100



example = Example(10)
print(Example.__dict__.keys())
print(example.__dict__.keys())