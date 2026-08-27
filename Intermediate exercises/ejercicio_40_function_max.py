#Create a function that returns the maximum value of a list

def max_value_option_1(listed_0):
    value_max = None
    for value_1 in listed_0:
        if value_max is None:
            value_max = value_1
        if value_max < value_1:
            value_max=value_1
    return value_max
print(max_value_option_1([100, 2, -3, -5, 20]))
print(max_value_option_1([-9,2,4,1,8]))
print(max_value_option_1([-3,1,7,6,2,3]))

def max_value_option_2(listed_0):
    value_max = listed_0[0]
    for value_1 in listed_0:
        if value_1 > value_max:
            value_max = value_1
    return value_max
print(max_value_option_2([100, 2, -3, -5, 20]))
print(max_value_option_2([-9,2,4,1,8]))
print(max_value_option_2([-3,1,7,6,2,3]))