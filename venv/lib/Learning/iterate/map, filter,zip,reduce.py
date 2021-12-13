# map, filter , zip , reduce

def multiple_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list


def times_2(item):
    return item * 2


def check_odd(li):
    return li % 2 != 0


the_list = [1, 2, 3, 4, 5]
the_tuple = (1, 2, 3, 4, 5, 6)
# print(list(map(multiple_by2, [1, 2, 3, 4, 5]))) # just give map function, map do the rest
print(multiple_by2(the_list))
print(f'map {list(map(times_2, the_list))}')
print(f'filter check odd {list(filter(check_odd, the_list))}')

# Zip

my_list = [1, 2, 3, 50]
your_list = [10, 20, 30, 6]
tho_list = [6, 9, 9, 6]
print(f'the zip {list(zip(my_list, your_list, tho_list))}')  # works even with others data structure
from functools import reduce

first_list = [1, 2, 3, 4, 5]


def accumulator(acc, item):
    print(acc, item)
    return acc * item


print(f'reduce {reduce(accumulator, first_list, 1)}')

from itertools import accumulate


def Sum(a, b):
    return a+b


list1 = [1, 2, 5, 7, 12, 6, 8]
sumlist1= accumulate(list1,Sum)
print(list(sumlist1))

tho_list = [6, 9, 9, 6]
def tinhtonglist(a,b):
    return a + b
tongtinh=reduce(tinhtonglist,tho_list,10)
print(tongtinh)
# khi muon tinh tong 1 list, thi cong thuc neu khong dung reduce se nhu the nao? sum(bao nhieu bien?)