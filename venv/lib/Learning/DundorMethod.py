class Toy():
    def __init__(self, color , age):
        self.color = color
        self.age = age
        self.mydict = {
            'Name': 'JoJO',
            'power': 'Star Platinum'
        }
    def __str__(self):
        return f'{self.color}'
    def __call__(self):
        return 'Yess!!!'
    def __getitem__(self, key):
        return self.mydict[key]

action_figure = Toy('red',0)
print(action_figure.__str__())
print('action figure'.__str__())
print('hello'.__len__())
print(action_figure.__call__())
print(action_figure['Name'])
