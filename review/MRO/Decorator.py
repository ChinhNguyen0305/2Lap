# Decorator
def my_decorator(func):
    def wrap_func(string):
        print('*****')
        func(string)
        print('*****')

    return wrap_func


@my_decorator  #this way modify the function
def hello():
    print('helllo')


# hello()
# my_decorator(hello)() # There are two ways to excute a moderator. this is the way that use decorator, not modify the function

# hello()

@my_decorator
def hello2():
    print('helllo2')


# hello2()


# Explain what decorator do underneath the hood
# my_decorator(greet)()
@my_decorator
def greet(string):
    print(f'hello {string}')

greet('cdz')