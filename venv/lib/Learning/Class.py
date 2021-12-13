# class MyOwnProject:
#     pass
#
#
# obj1 = MyOwnProject
# print(type(obj1()))
#
# my_list = [ 1,2,3,4,5]
# my_list[2] = 4
# print(my_list)

class PlayerCharacter:
    # Class object membership
    GoldMembership = True

    def __init__(self, name='Andrei', race='Human', attack=False, age=0):
        if age >= 18:
            self.age = age
            self.name = name  # This called class attribute
            self.race = race
            self.attack = attack

    def shout(self):
        print(f'俺は {self.name} だあああ！')

    @classmethod
    def adding_thing(cls, num1, num2):
        return num1 + num2


player1 = PlayerCharacter('Cindy', 'Death Vader', False, 20)
player2 = PlayerCharacter('Scepter', 'Troll', 50, 2)
player3 = PlayerCharacter('DarkMatter', 'archer', 400, 30)
print(PlayerCharacter.adding_thing(2, 3))
print(player1.shout())
print(PlayerCharacter.adding_thing(2,3))

# If age > 10 is a sample of the power of __init__ we can control a lot of things
