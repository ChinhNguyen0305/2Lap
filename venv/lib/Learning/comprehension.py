lista = list(range(0,10))
print(lista)

list_b= [element for element in 'hello']
print(list_b)

list_c = [num*2 for num in range(0,10)]
list_d = [num for num in range(0,10)
          if num % 2==0]
print(list_c)
print(list_d)