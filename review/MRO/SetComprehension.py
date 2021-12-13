my_list = {char for char in 'hello world'}
print(my_list)



# Using comprehension

# my_list2 = [char for char in 'hello']
# print(f'my list 2 {my_list2}')

my_list3 = {num for num in range(10)}
print(f'my list 3 {my_list3}')

my_list4 = [num * 3 for num in range(20)]
print(f'my list 4 {my_list4}')

my_list5 = [num * 3 for num in range(20) if num % 2 == 0]
print(f'my list 5, just even of my list 4 {my_list5}')
