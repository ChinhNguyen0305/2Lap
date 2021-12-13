class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
def get_the_oldest_cat(*args):
    return max(args)


Lucy = Cat('Lucy', 3)
Meow = Cat('Meow', 1.5)
tarou = Cat('太郎', 4)

cat_age = [Lucy.age,Meow.age,tarou.age]
max(cat_age)
print(max(cat_age))
print(f'The oldest cat is {get_the_oldest_cat(Lucy.age,Meow.age,tarou.age)} years old')

# 1 Instantiate the Cat object with 3 cats



# 2 Create a function that finds the oldest cat



# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2