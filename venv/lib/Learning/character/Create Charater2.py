class User():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print(f'welcome to Grimdawn world {self.name}')

    def attack(self):
        return print('do nothing')


class Wizard(User):
    def __init__(self, name, AP, email):
        # super().__init__(email)
        # User.__init__(self, email. Suy nghi ban dau, super().email (hoan toan sai, de them email vao 1 obj, can __init__)
        self.name = name
        self.AP = AP

    def attack(self):
        print(f'{self.name} attacks with {self.AP}, Take this !!')
    def run(self):
        print ('Get out, get out!!!')


class Archer(User):
    def __init__(self, name, arrows_left, email):
        # super().__init__(email)  # .__init__(self,email)
        self.name = name
        self.arrows_left = arrows_left

    def attack(self):
        User.attack(self)
        print(f'{self.name} will pierce {self.arrows_left} through your heart')

    def run(self):
        print('逃げるんだうう')


class Hybrid(Wizard, Archer):
    pass


Gandaft = Wizard('Gandaft', 50, 'Gandaft@gmail.com')
Neo = Archer('Neo', 100, 'Neo@Gmail.com')
Cyber = Hybrid('Cyber', 50, 'Cyer@HybridCharacter.com')
print(Neo.attack())
print(isinstance(Neo, Wizard))


def play_attack(char):
    char.attack()


for ch in [Gandaft, Neo]:
    ch.attack()

# Above thing called polymorphism.
# Thing about function, the thing in bracket will replace in front of the dot (.) and execute the method, function
play_attack(Neo)
play_attack(Gandaft)
print(Neo.sign_in())  # The children class can be called in the Parents class

# my_character_list = [Archer('Robin',30,'Robin@gmail.com),Wizard('Merlin',1000, 'Merlingmail.com')] can't instantiate an obj by this
print(Neo.attack())
# print(Gandaft.email)
print(Cyber.run())
