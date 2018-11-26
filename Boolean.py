# Boolean
# comparison operators
# == < > >= <= !=
# and, or, not


print(not True)
print(True or False)
#Not statement
print(not(True or False))


# Conditionals and control flow

def square(condition_1,condition_2):
    if condition_1 and condition_2:
        print("Person did both")
    elif not(condition_1 and condition_2):
        print("Person didn't do both")
    else:
        print("should never go here")


johnny_homework = True
johnny_throw_out_garbage = True

square(johnny_homework,johnny_throw_out_garbage)

johnny_homework = True
johnny_throw_out_garbage = False

square(johnny_homework,johnny_throw_out_garbage)
