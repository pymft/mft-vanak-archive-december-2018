import time


def sum_test1():
    inp = list(range(10000000))
    t1=time.time()
    var = sum(inp)
    t2 = time.time()
    print(t2-t1)


def sum_test2():
    sum_new = sum
    inp = list(range(10000000))
    t1=time.time()
    var = sum_new(inp)
    t2 = time.time()
    print(t2-t1)




sum_test1()
sum_test2()
