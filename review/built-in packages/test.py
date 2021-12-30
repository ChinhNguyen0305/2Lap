import random_game
from random_game import shuffle


print(random.randint(2,10))
my_list = [1,2,3,4,5,6]
shuffle(my_list)
print(my_list)
print(random.choice(my_list))
random.seed()