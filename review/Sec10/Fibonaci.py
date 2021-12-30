# def fib(index):
#     for i in range(index):
#         yield i
from time import time


def performance(fn):
    def wrapper(*args):
        t1 = time()
        fn(*args)
        t2 = time()

    return fn


def fibo(index):
    a = 0
    b = 1
    for num in range(index):
        yield a
        t = a + b
        a = b
        b = t


for x in fibo(20):
    print(x)
