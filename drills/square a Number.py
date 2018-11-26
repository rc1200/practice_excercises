

# Square a number
def square_number(my_number):
    return my_number **2

print (square_number(2))


print ('check if Even ---------------------')
# check if number is even
# number % number2 give the remainder or MOD
def is_even(my_number):
    
    if my_number % 2 == 0:
        isEven = True
    else:
        isEven = False

    return isEven

print(is_even(1))    
print(is_even(2))
print(is_even(3))
print(is_even(5))
print(is_even(8))


print ('check if Odd ---------------------')
# check if number is even
# number % number2 give the remainder or MOD
def is_odd(my_number):
    
    if my_number % 2 >= 1:
        isEven = True
    else:
        isEven = False

    return isEven

print(is_odd(1))    
print(is_odd(2))
print(is_odd(3))
print(is_odd(5))
print(is_odd(8))
