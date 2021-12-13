# 18/06/20201
class User():
    def sign_in(self):
        print(f'welcome to Grimdawn world {self.name}')

    def attack(self):
        return print('do nothing')


class Wizard(User):
    def __init__(self, name, AP):
        self.name = name
        self.AP = AP

    def attack(self):
        print(f'{self.name} attacks with {self.AP}, Take this !!')

    def run(self):
        print('Get out, get out!!!')


class Archer(User):
    def __init__(self, name, arrows_left):
        self.name = name
        self.arrows_left = arrows_left

    def attack(self):
        User.attack(self)  #The different between Archer and Wizzard, Archer has User.attack(self)
        print(f'{self.name} will pierce {self.arrows_left} through your heart')

    def run(self):
        print('逃げるんだうう')


class Hybrid(Wizard, Archer):
    def __init__(self,name, AP, arrows_left):
        Archer.__init__(self,name,arrows_left)
        Wizard.__init__(self,name,AP)


def play_attack(char):
    char.attack()

Gandaft = Wizard('Gandaft', 50)
Neo = Archer('Neo', 100)


# for ch in [Gandaft, Neo]:
#     ch.attack()

#
# play_attack(Neo)
# play_attack(Gandaft)
print(Neo.sign_in())  # The children class can be called in the Parents class
print(Neo.attack())
Hyper = Hybrid('Hyper',75 ,100)
print(Hyper.arrows_left)
