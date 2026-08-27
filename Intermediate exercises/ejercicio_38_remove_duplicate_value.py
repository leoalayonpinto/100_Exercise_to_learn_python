# function to remove the duplicate values in a list
# https://docs.python.org/3/library/stdtypes.html#list.sort

def remove_duplicates(list_1):
    list_2=[]
    for i in range(len(list_1)): #loop in the length of the list
        if list_1[i] not in list_2: #boolean to verify is the value is in the list
            list_2.append(list_1[i]) #added the value in the list_2
            list_2.sort(reverse = False) #sort the list_2
    return list_2
    # return list_2.sort(reverse = False) this is not correct due it's not returning the sorted list
print(remove_duplicates([0,3,5,7,3,5,1,-1]))
print(remove_duplicates([0,5,9,10,3.2,1,-3]))

