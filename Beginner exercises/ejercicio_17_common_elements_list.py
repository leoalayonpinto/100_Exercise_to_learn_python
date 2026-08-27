List_1=[9,8,7,14,3,2,'a','p','hola','b']
List_2=['b',1,9.2,6,3,9,'p']
List_3=[]
# method 1
for value_1 in List_1:
    for value_2 in List_2:
        if value_1==value_2:
            List_3.append(value_1)
print(List_3)

# method 2 see https://docs.python.org/3/library/stdtypes.html#set
# https://docs.python.org/3/library/stdtypes.html#set.intersection

List_1=[9,8,7,14,3,2,'a','p','hola','b']
List_2=['b',1,9.2,6,3,9,'p']
List_3=set(List_2).intersection(List_1)
print(List_3)