#creat an empty list
L = []
while True:
    value = input('Introduce a value ')
    if value == 'done':
        print('End of program')
        break   #break the cycle 'while' when the condition is not meet
    if value !='':
        L.append(value) #append method introduce a new value at the final of the list
    else:
        print('invalid input')
        break
print(L)