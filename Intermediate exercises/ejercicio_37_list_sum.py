# write a function sum to calculate the total in the list

def cal_sum(_list_):
    total = 0
    for num in _list_:
        total+=num
    return total
print(cal_sum([3,2,6,9,-1,5]))
print(cal_sum([-3,-6,0,1,2,7]))