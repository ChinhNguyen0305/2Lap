# Square a list
import math

the_list = [2, 7, 5, 4]

print(list(map(lambda item: item ** 2, the_list)))

# List sorting
a = [(0, 2), (4, 3, 5), (9, 9, 7, 3), (10, -1)]
a.sort(key=lambda tup: tup[len(tup) - 1], reverse=False)
print(a)

tuple_a = (3, 3, 4, 5, 6)
print(tuple_a[2])
