try:
    num=100
    denom=0
    result=num//denom
    print(result)
except IndexError:
    print("Index out of bound")
except ZeroDivisionError:
    print("denomonator cannot be zero")
finally:
    print("this is finally block")
