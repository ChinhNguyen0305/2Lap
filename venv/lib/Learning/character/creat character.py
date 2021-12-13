class Character:
    def __init__(self, name, race , weapon):
        self._name = name
        self._race = race
        self._weapon = weapon
    def self_introduce(self):
        print(f'Hello Master, I\'m {self._name}, a {self._race}, I\'m interested in using {self._weapon}. Choosing me is a wise decision')
    def war_cry(self):
        if self._race == 'orc':
            print(f'{self._race}{self._race},  {self._race} born for this moment, we came here, to reign this up !!! Grrrr')
        elif self._race == 'fairy':
            print(f'We are {self._race},the assemble of the eternal, you have no chance!!')
        elif self._race == 'undying':
            print(f'Kneel before {self._race}, or Dieeeee ')
        else:
            print(f'We, {self._race} will protect our jungle, you dare to destroy it, {self._race} will bring extinction to you')

DeathVader = Character('Death Vader','Undying','serrate sword')
NarcKull = Character('NarcKull','orc','Giant axes')
Enel = Character('Enel', 'fairy','Long bow')
Tug = Character('Tug', 'elf', 'Magic-stick')
DeathVader.name = 'Raknarok'
print(Tug.war_cry())
print(Tug.self_introduce())
print(Enel.self_introduce())
print(Enel.war_cry())
print(DeathVader.name)
# we can use an underscore as a convention, but there's no guarantee