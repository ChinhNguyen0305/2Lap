my_list = [1, 2, 7, 13, 5, 6, 20, 8, 9, 5, 25]

print(list(map(lambda item: item * 3, my_list)))
print(list(filter(lambda item: item % 2 != 0, my_list)))
from functools import reduce

print(reduce(lambda a, b: a + b, my_list))
from itertools import accumulate

print(list(accumulate(my_list, lambda a, b: a if a > b else b)))

# excercise

the_list = [5,4,3]

print(list(map(lambda x : x*x, the_list)))

# list_sorting
a = [(0,2),(4,3),(9,9),(10,-1)]

def myfunc2(e):
    return e[1]
a.sort(key = myfunc2)
print(a)
cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]
def myfunc(e):
    return e['car']
cars.sort(key = myfunc)
print(cars)
def myFunc(e):
  return len(e)

cars2 = ['Ford', 'Mitsubishi', 'BMW', 'VW']


def carlen(e):
    return len(e)
cars2.sort(key = carlen)
print(f'sorted cars2 {cars2}')