# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i*2)
#     return result

# my_list1 = list(range(10))
# my_list = make_list(10)
# print(my_list)
# print(my_list1)


def generator_function(num):
    for i in range(num):
        yield i * 2


# for item in generator_function(10):
#     print(item)

g = generator_function(2)
next(g)
# next(g)
print(next(g))
