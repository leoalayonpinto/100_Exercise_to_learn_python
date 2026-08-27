# exercise to sum the digits of the number
#method 1 is changing the number to string and then split him with a for loop
number_1=str(3018)
_sum_=0
for digit in number_1:
    _sum_= _sum_ + int(digit)
print(_sum_)

def last_digit(_sum_, number):
    while number>0:
        #print(number%10) number%10 return the remainder (resto_spanish) of the division, for example, 3018%10=8, and then the number is added to the sum
        _sum_= _sum_ + number % 10
        number//=10     #number=number//10, Discard the fractional part, example 3018/10=301 the eight is discarded
       #print(number)
    return _sum_
ini=0
number_2=3018
print(last_digit(ini,number_2))