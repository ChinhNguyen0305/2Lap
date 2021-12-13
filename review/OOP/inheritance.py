class User():
    def __init__(self, email,address):
        self.email = email
        self.address=address

    def sign_in(self):
        print('logged in')


class Archer(User):
    def __init__(self, email, name, attack,address):
        super().__init__(email,address)
        self.name = name
        self.attack = attack
        self.email = email


    def attack(self):
        print(f'{self.name} will pierce you to raw meat with {self.attack()} arrows')


class Wizard(User):
    def __init__(self, name, AP, email):
        self.name = name
        self.AP = AP
        self.email = email

    def attack(self):
        print(f'{self.name} will burn you alive with {self.AP} fire balls')


archer1 = Archer('False@gmail.com', 'Hawk', 20,'h17lich doi')
wizard1 = Wizard('Merlin', 10,'a')
wizard1.attack()
print(archer1.email + archer1.address)
print(wizard1.email)
