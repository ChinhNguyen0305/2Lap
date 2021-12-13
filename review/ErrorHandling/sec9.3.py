def sum1(num1,num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as err:
        print(err)
    else:
        print('Thank you!')



print(sum1(2,0))
