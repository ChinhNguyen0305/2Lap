class Pets():

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name    
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Gy(Cat):
    def sing(self,sounds):
        return f'{sounds}'    #f string can be used like this


print(Simon.sing(Simon,'Gau gau'))
#1 Add nother Cat
print(Simon.sing(Simon, 'Meowwww3'))
#2 Create a list of all of the pets (create 3 cat instances from the above)
my_cats = [Simon('Simon',4),Sally('Sally',2),Gy('Gy',7)]
# o day khac voi vi du cua Create Character 2. ban than ten cua moi con meo da la 1 class, class lay param tu cat,
# nen no co san tinh nang instantiate ten va tuoi cua moi con meo
#3 Instantiate the Pet class with all your cats use variable my_pets
# Simon = Pets('Cat') #sai
# Sally = Pets('Cat') #sai
# Gy = Pets('Cat')# sai
my_pets = Pets(my_cats) #This is very powerful, instantiate a class into a whole list

#4 Output all of the cats walking using the my_pets instance
#tim hieu tai vi sao khi print(Simon.sing(simon,Meow) o duoi thi khong hoat dong, co phai la do da instantiate class vao list my pet khog)
Coca = Cat('Coca',3)
print(Coca.walk())
print(Simon.sing('Simon', 'Meowwww'))
my_pets.walk()
