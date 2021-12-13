my_list = [1, 2, 3, 4]


def filt_even(item):
    # if item % 2 ==0: return item  # Day la cach lam cua minh
    return item % 2 == 0


print(list(filter(filt_even, my_list)))
