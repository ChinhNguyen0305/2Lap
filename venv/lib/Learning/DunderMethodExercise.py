class SuperList(list):
    # def __init__(self):
    def __len__(self):
        return 1000


# Andrei want to creat a super list that have every function of a list but __len__ return 1000 no matter what
# I will first thing about creat every function, but that doesn't sound very good, so, in here we inherit Superlist(list), so SupList has every function of "list", How cool this that
list1=SuperList([1,2,3,4,5])
print(len(list1))