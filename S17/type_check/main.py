val = "rfdfgdfgdfgdfg"
res = type(val)
print(res)

try:
    val = int(val)
    for i in range(val):
        print(i)
except ValueError:
    print(val[::-1])


