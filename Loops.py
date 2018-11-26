# Loops 
# range (start,stop, step)

# will show 0 - 4
for i in range (5):
    print(i)

print('------------------------------')    
# will show 20 - 30
for i in range (20,31):
    print(i)

print('------------------------------')    
# will show 20 - 30 by 2
for i in range (20,31,2):
    print(i)

print('------------------------------')    
# will show 20 - 5 by 5
for i in range (20,4,-5):
    print(i)

print('count ------------------------------')    
count = 0
for i in range (1,5):
    count += i
    print(count)

print('------------------------------')    
# funciton that sums all elements of a list and returns it


def sum_list(my_list):
    count = 0
    for number in my_list:
        count += number

    return count

ron_list = [1,2,3]
print (sum_list(ron_list))

