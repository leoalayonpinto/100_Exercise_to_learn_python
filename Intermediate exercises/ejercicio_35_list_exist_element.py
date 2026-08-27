#Create a function that receive a list and return true or false if there exists an even number
def verify_even_number(number,list):
        if number in list:
            return True
        else:
            return False
print(verify_even_number(6,[3,6,9,7,'abcr']))