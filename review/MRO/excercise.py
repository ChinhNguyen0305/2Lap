# from functools import reduce
from functools import reduce

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def capital(value):
    return value.capitalize()


print(list(map(lambda item: item.capitalize(), my_pets)))

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

print(list(zip(my_strings, sorted(my_numbers))))
my_numbers.sort()
print(my_numbers)   # a very important point, the difference between method and built-in function
# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def higher_grade(mark):
    return  mark > 50

print(list(filter(higher_grade,scores)))
print(f'Filter using Lambda: {sorted(list(filter(lambda item : item> 50,scores)))}')
# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

def summary(acc,item):
    return acc + item

print(reduce(summary,scores))
print(f'Reduce using lambda: {reduce(lambda acc,index: acc+index,scores)}')

