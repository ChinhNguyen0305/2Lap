class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cat(Pet):
    def __init__(self,legs):
        super(Cat, self).__init__()
        self.legs = legs

    def sing(self):
        print(f'{self.name} is singing')


Tom = Cat(4)
print(Tom.name)
