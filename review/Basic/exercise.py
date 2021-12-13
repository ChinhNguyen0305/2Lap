some_list = ['a', 'b', 'c', 'n', 'm', 'd', 'n', 'm', 'n']
duplicate_list = []
counter = 0
i = 0
for c in some_list:
    if some_list.count(c) > 1:
        if c not in duplicate_list:
            duplicate_list.append(c)
print(duplicate_list)
