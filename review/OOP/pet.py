class Pets():
    animals123 = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

    def sing(self):
        for animal in self.animals:
            print(animal.sing())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'
      
    def sing(self):
        return f'{self.name} is singing {self.sound}'



class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Jimmy (Cat):
    def sing(self,sounds):
        return f'{sounds}'
# 1 Add nother Cat

# 2 Create a list of all of the pets (create 3 cat instances from the above)
my_cats = [Simon('Simon',2),Sally('Sally',0.5),Jimmy('Jimmy',3)]

# 3 Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets(my_cats)
# 4 Output all of the cats walking using the my_pets instance
my_pets.walk()
my_pets.sing()
