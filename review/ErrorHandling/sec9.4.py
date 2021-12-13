while True:
    try:
        age = int(input('what is your age?'))
        10/age
    except ValueError:
        print('Please enter a number.')

    except ZeroDivisionError:
        print('Please enter age higher than 0')
        break
    else:
        print('Thank you!')
        break
    finally:
        print('Ok, I am finnlly done')
    print('Can you hear me?')
