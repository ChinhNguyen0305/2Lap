class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'pet': 'cat',
            'status': 'sadness is gone'
        }

    def __str__(self):
        return 'Try harder for a brighter future'

    def __len__(self):
        return 5

    def __call__(self):
        print('This is amazing')


    def __getitem__(self, i):
        return self.my_dict[i]  #Hoat dong nhu call, khong goi thong qua function, ma goi qua [] ()


action_figure = Toy('red', 2)
print(str(action_figure))
print(action_figure.__str__())

print([1, 2, 3, 4].remove(1))
# print(str(4))
print(len(action_figure))
print(len([1,23,3,4,5,6]))
print(action_figure['status'])
