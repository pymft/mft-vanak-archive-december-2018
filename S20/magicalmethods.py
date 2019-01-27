class MySequence:
    def __init__(self, *args):
        self.seq = args

    def __getitem__(self, item):
        return self.seq[item-1]

    def __getattr__(self, item):
        if item.startswith('___'):
            num = int(item[3:])
            return self[num]
        super().__getattribute__(item)

m = MySequence('hello', 2, True, 4, 5)

print(m.___3)

print(m.seq[0])
print(m[1], m[2])
