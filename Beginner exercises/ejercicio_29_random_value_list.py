# to choice a random element in a 'list' it could use random.choice or random.shuffle
# https://docs.python.org/3/library/random.html#random.choice
# https://docs.python.org/3/library/random.html#random.shuffle
import random
import time
# method 1
init=time.time()
list=[3,6,8,7,2,'s','ch','d'] #The list can be named also sequence
randon_list=[]
for i in list:
    randon_list.append(random.choice(list))
final=time.time()
print(randon_list,(final-init)*1000)

# method 2 it is import to choice the best method to reduce the script execution time
list=[3,6,8,7,2,'s','ch','d']
init=time.time()
random.shuffle(list)
final=time.time()
print(list,(final-init)*1000)