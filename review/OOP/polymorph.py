class User():
    def __init__(self, email):
        self.email = email
    def sign_in(self):
        print('logged in')
    def attack(self):
        print('do nothing')


class Archer(User):
    def __init__(self,name, arrows):
        self.name = name
        self.arrows = arrows

    def attack(self):
        # User.attack(self)
        print(f'{self.name} will pierce you to raw meat with {self.arrows} arrows')

class Wizard(User):
    def __init__(self,name, AP):
        self.name = name
        self.AP = AP

    def attack(self):
        print(f'{self.name} will burn you alive with {self.AP} fire balls')


archer1 = Archer('Hawk',20)
wizard1 = Wizard('Merlin',10)
wizard1.attack()
archer1.attack()

def player_attack(hero):
    hero.attack()


# player_attack(archer1)
