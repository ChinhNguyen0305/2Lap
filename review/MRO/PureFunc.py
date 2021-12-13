def multiple_2(li):
    new_list = []
    for num in li:
        # num *= 2
        # new_list.append(num)
        new_list.append(num*2)

    return new_list

my_list = [1,2,3,4,5,6]
print(multiple_2(my_list))