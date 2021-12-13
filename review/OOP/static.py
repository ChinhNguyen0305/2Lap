class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shout(self):
        print(f'I am {self.name}!! take thiss!!')

    @classmethod
    def adding_things(cls, name,num1, num2):
        return cls(name,num1+num2)

Player1 = PlayerCharacter('Sun',20)
Player2 = PlayerCharacter.adding_things('heo',2,3)
# print(Player1.adding_things(2, 3))
# print(PlayerCharacter.adding_things(2,3))

print(Player1.name)
print(Player1.age)
print(Player2.name)
print(Player2.age)
