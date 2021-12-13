# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats

Cat_List = [Cat('Simmi', 2), Cat('xoai', 0.5), Cat('Mit', 1),Cat('Axe',3)]
# Simmi = Cat('Simmi', 2)
# Mit = Cat('Mit', 0.5)
# Xoai = Cat('Xoai', 1)


# 2 Create a function that finds the oldest cat
cat_YO = []
cat_name = []
oldest = 0
index = 0
for age in range(len(Cat_List)):
    cat_YO.append(Cat_List[age].age)
for i in range(len(cat_YO)):
    if cat_YO[i] > oldest:
        index = i
        break;
def find_oldest_cat(li):
    return max(li)

print(cat_name)
print(find_oldest_cat(cat_YO))

# print(len(Cat_List))
# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f'The oldest cat is {find_oldest_cat(cat_YO)} years old')