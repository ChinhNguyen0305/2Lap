some_list = ['a', 'b', 'c', 'a', 'd', 'b', 'd']

duplicate = []

for char in some_list:
    if some_list.count(char) > 1:
        if duplicate.count(char) == 0:
            duplicate.append(char)

print(duplicate)

# duplicate2 = list({char for char in some_list if some_list.count(char) > 1})
duplicate2 = list(set([char for char in some_list if some_list.count(char) > 1]))
print(duplicate2)
