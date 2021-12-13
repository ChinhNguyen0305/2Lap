def multiple_2(item):
    return item * 2


def cap(i):
    return i.capitalize()


# We dont know the type of paramaeter so the method simply does'n show up. but it still there

my_list = [1, 2, 3, 4, 5, 6]
character_name = ['merlin', 'genshin','rurou']
print('abc' + 'ridiculous'.capitalize())

print(list(map(cap, character_name)))
print(list(map(multiple_2, my_list)))
print(my_list)
