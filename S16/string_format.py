text = "number : {2} and a text = {1}, another number = {0}"

text_new = text.format(100, "something", 10000)
print(text_new)


text2 = "It's {lastname}, {firstname} {lastname}".format(firstname="James", lastname="Bond")
print(text2)


text2 = "|{firstname:^30}|{lastname:^20}|{age:<10}|".format(firstname="James", lastname="Bond", age=30)
print(text2)


for i in range(1, 51, 2):
    print("{pat:^51}".format(pat="*" * i))