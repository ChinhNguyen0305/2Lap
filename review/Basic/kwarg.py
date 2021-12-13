def super_func(*arg, **kwarg):
    print(kwarg.items())
    print(arg)
    total = 0
    for value in kwarg.values():
        total += value
        # return  sum(arg) + sum(kwarg.values())
    return sum(arg) + total


print(super_func(5, 6, 7, number1=1, number2=2, so3=3,number0 = 2))
