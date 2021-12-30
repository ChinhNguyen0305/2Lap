print(f'This is {__name__}')
def multiple(num1, num2):
    return num1 * num2


def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return f'Can\'t be devided by zero'

def max():
    return  f'oops'
if __name__ == '__main__':
    print('This is main modules')