def my_decorator(func):
    def wrap_func():
        print('****')
        func()
        print('****')

    return wrap_func


@my_decorator
def hello(greeting):
    print(greeting)

hello()