#
# from time import time
# def performance(fn):
#     def wrapper(*args,**kwargs):
#         t1 = time()
#         result = fn(*args,**kwargs)
#         t2=time()
#         result = t2-t1
#         print(f'run time {result}')
#         return result
#     return wrapper
#
# def long_time():
#     print('1')
#     for i in range(1000000):
#         i*5
#
# @performance
# def long_time2():
#     print('2')
#     for i in list(range(1000000)):
#         i*5

#Andrei Neagoi
from time import time
def performance(fn):
    def wrapper(*args, **kawrgs):
        t1 = time()
        result = fn(*args, **kawrgs)
        t2 = time()
        print(f'took {t2-t1} s')
        return result
    return wrapper

@performance
def long_time():
    print('1')
    for i in range(200000):
        i*5
@performance
def long_time2():
    print('2')
    for i in list(range(200000)):
        i*5


long_time()
long_time2()