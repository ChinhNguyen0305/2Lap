while True:
    try:
        age = int(input('what is your age?'))
        10/age
    except ValueError:
        print('Please enter a number.')
    except ZeroDivisionError:
        print('Please enter age higher than 0')
    else:
        print('Thank you!')
        break
