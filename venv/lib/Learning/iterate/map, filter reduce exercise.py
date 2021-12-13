from functools import reduce

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def capitaliz(li):
    return li.upper()


print(list(map(capitaliz, my_pets)))

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]
my_numbers.sort()
print(list(zip(my_strings, my_numbers)))

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def over50(score):
    return score >= max(scores) / 2


print(list(filter(over50, scores)))

# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
# scores.extend(my_numbers)
# print(scores)
# def total(a,b):
#     return a + b
# print(reduce(total,scores))

# Andrei's way. Notice that we can combine two list just by plus(+)
# def accumulate (acc, item):
#     return acc + item

# print(reduce(accumulate, my_numbers + scores))

# trying using accumulate
from itertools import accumulate
def total(a,b):
    return a + b

see_step = accumulate(scores,total)
print(list(see_step))
print(sum(scores))