L=[3,2,2,1,9,1,2,3,7]
count=0
for number in L:
    if number==1:
        count+=1
print(count)

# Count the repetitive number with the integer method count() of the list

print(L.count(1))

# new_list=[]
# for number in L:
#     if not number in new_list:
#         new_list.append(number)
#     new_list.sort(reverse=False)
# print(new_list)

