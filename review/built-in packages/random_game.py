#Gererate a number
from random import randint
answer = randint(1,10)

def  guess():
    while True:
        try:
            guess = int(input('Guess a number from 1~10 '))
            if 0 < guess < 11 and guess:
                break
            else:
                print('Please try again!')
                continue
        except ValueError:
            print(f'Hey Bozo, enter a number')
            continue
    return guess



def play_game():
    while True:
        my_guess = guess()
        if my_guess == answer:
            print('You\'re genius! Congrat!')
            break
        else:
            print('Better luck next time')
            continue

play_game()


