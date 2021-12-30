'''
So hoan hao
'''

def check_perfect():
    while True:
        try:
            numb = int(input('Enter a number: '))
            break
        except ValueError:
            print('Please enter an interger!')
    total = 0
    for i in range(1,int(numb/2)+1):
        if numb % i == 0:
                total += i

    if total == numb and total > 0:
        print(f'{numb} is a perfect number')
    else:
        print(f'{numb} is not a perfect number')


check_perfect()