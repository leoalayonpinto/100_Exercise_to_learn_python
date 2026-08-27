#List Assignation list comprehensions are faster taht equivalent loops
L=[3,6,9,12,15,18,21,24]
L1=[int(l/3) for l in L ]
print(L1)
# position, in this case is included the number 1 at the beginning of the list