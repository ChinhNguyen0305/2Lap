class User():
    # def __init__(self, email, address):
    #     self.email = email
    #     self.address = address

    def sign_in(self):
        print('logged in')


class Archer(User):
    def __init__(self, name, arrows):
        # super().__init__(email, address)
        self.name = name
        self.arrows = arrows
        # self.email =  email
        # self.address = address  # Có thể có hoặc không, nhưng không nên có

    def shoot(self):
        print(f'{self.name} will pierce you to raw meat with {self.arrows} arrows')

    def check_arrows(self):
        print(f'Caitlyn\'s arrows are {self.arrows}')

    def run(self):
        print('Ran really fast')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
        # self.email = email

    def attack(self):
        print(f'{self.name} will burn you alive with {self.power} fire balls')


class HybridCarry(Archer, Wizard):
    def __init__(self, name, arrows, power ):
        Wizard.__init__(self, name, power)
        Archer.__init__(self,name, arrows)




Caitlyn = HybridCarry('Caitlyn', 50, 30)
# print(Caitlyn.arrows)
Caitlyn.attack()
print(Caitlyn.arrows)
print(Caitlyn.power)
Caitlyn.check_arrows()
Caitlyn.shoot()
Caitlyn.sign_in()
# archer1 = Archer('False@gmail.com', 'Hawk', 20, 'h17lich doi')
# wizard1 = Wizard('Merlin', 10, 'a')
# wizard1.attack()
# print(archer1.email + archer1.address)
# print(wizard1.email)
