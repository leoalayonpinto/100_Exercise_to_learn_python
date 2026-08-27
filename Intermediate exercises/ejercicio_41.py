# Function sub list sum the elements using the sub list
def sub_list_sum(sub_list,i,j):
    sub_sum=0
    for value in sub_list[i:j+1]:
        sub_sum+=value
        # print(sub_sum)
    return  sub_sum
print(sub_list_sum([4,10,12,16,18],2,4))
print(sub_list_sum([2,4,6,8,10,12],0,2))