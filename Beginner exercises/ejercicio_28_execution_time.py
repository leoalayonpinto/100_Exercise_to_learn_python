# execution time using time https://docs.python.org/3/library/time.html#time.asctime
# https://docs.python.org/3/library/time.html#time.time
# https://docs.python.org/3/library/time.html#time.strftime

import time
init=time.time()
for i in range(11):
    print(f"8 x {i} = {8*i}")
final=time.time()
total=(final-init)*1000
print(f'the total execution time is of this scr2ipt is {total} ms and was executed ´{time.asctime()}´')