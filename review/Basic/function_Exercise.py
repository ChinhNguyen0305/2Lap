# Function Exercise

my_list = [2    ,10, 2, 3, 5, 9, 5, 11, 30]


def highest_even(li):
    max_even = 0
    for item in range(len(li)):
        if li[item] % 2 != 0 and li[item] > max_even:
            max_even = li[item]
    return max_even


print(highest_even(my_list))


def highest_even2(li):
    even_list = []
    max = 0

    for item in li:
        if item % 2 == 0:
            even_list.append(item)

    for item in even_list:
        if item > max:
            max = item
    return max


print(highest_even2(my_list))
