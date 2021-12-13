class SuperList(list):
    # def __init__(self, my_list):
    #     super().__init__()
    #     self.the_list = my_list

    def __len__(self):
        return 1000


# my_list = SuperList([1,2,3,4,5,6])
# print(my_list.__len__())
# print(my_list.the_list.__len__())
my_list = SuperList()
my_list.append(5)
add_list = [1,2,3,4,5]
my_list.extend(add_list)
print(my_list)
print(len(my_list))
print(my_list.__len__())
print(issubclass(SuperList,list))