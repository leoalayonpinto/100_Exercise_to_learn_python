#List Assignation
L=[1,2,3,4,5,6,7,8,9,10]
L1=[i+1 for i in L if i%3==0]
L1.insert(0,1)
print(L1)
#the method 'insert' insert an item at a given
# position, in this case is included the number 1 at the beginning of the list

