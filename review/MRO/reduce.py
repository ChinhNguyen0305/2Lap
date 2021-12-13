from functools import reduce

my_list = [1, 2, 3, 4, 5, 6]
string_list = ['hallo', 'konnichiwa', 'hallu']

def accumulate(acc, item):
    return acc * item


def total_acc(acc, item):
    return acc + item


def multiple_by_2(item):
    return item * 2


print(f'giai thua cua list su dung reduce {reduce(accumulate, my_list)}')
print(f'total    cua list su dung reduce {reduce(total_acc, map(multiple_by_2,my_list), 0)}')

giai_thua = 1
for num in range(len(my_list)):
    giai_thua *= my_list[num]

print(giai_thua)

total = 0
for num in range(len(my_list)):
    total += my_list[num]

print(f'Giai thua cua list la: {giai_thua}')
print(f'Summary of list is {total}')

print(f'Testing lambda: {list(map(lambda item: item*2,my_list))}')
print(f'testing lamda with string {list(map(lambda item: item.capitalize(),string_list))}')