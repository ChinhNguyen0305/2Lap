i = 0
li = [1, 2, 3, 4,5]
while i < 5:
    respone = input('Greeting: ')
    if respone.lower() == "bye" or respone.upper() == "Bye":
        break

while i < 5:
    print(li[i])
    i += 1
