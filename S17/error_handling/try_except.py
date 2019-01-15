def test_try(num1, dct):
    try:
        res = num1 / dct['a']
        return res
        
    except ZeroDivisionError as e:
        print("plan B for zero division error")
        return e
        
    except IndexError as e:
        print("plan C for index error")
        return e

    except KeyError as e:
        print("plan D for key error")
        print("you've chosen key '{}' which is not exists ".format(e.args[0]))
        return e

    finally:
        print("finally")
        return 0

    print("after try-except-finally block")
    
    
    
num1 = 10
lst = [0, 1, 2, 3, 4]
dct = {'a': 0, 'b': 100}

out = test_try(num1, dct)
print(out)

# Syntax Error    < easiest to detect
# Runtime Error   < most common, easy to detect
# logical Error


