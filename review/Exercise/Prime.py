import math


def check_prime():
    while True:
        try:
            numb = int(input('Enter your number: '))
            break
        except:
            print('Please enter a number')

    is_prime = True
    if numb < 2:
        print(f'{numb} is not prime number')
    elif numb == 2:
        print(f'{numb} is a prime number')
    elif numb > 2:
        for div in range(2, int(math.sqrt(numb))):
            if numb % div == 0:
                is_prime = False
                # break

    if is_prime == False:
        if numb > 2:
            print(f'{numb} is not prime number')
        else:
            print(f'{numb} is a prime number')
    # print(f'{numb} is a prime number') if is_prime == True  else print(f'{numb} is not a prime number')
    '''
    Can't use ternary here, go back when have time

    '''



check_prime()
