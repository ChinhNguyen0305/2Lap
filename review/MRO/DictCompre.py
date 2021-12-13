simple_dict = {
    'a': 1,
    'b':2,
    'c':3,
    'd':4
}

#Dictionary comprehension

my_dict = {k:v**2 for k,v in simple_dict.items() if v % 2 == 0}

print(my_dict)

my_dict2 = {num:num*2 for num in [1,2,3,4,5,6]}
print(my_dict2)