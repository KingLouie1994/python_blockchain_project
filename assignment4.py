# Write a normal function that accepts another function as an argument. Output the result of that other function in your 'normal' function
def normal_function(other_fnctn):
    print(other_fnctn(10))


# Call your 'normal' function by passing a lambda function - which performs any operation of your choice - as an argument
normal_function(lambda el: el * 2)


# Tweak your normal function by allowing an infinite amount of arguments on which your lambda function will be executed
def normal_function2(other_fnctn, *args):
    for arg in args:
        print(other_fnctn(arg))

normal_function2(lambda el: el * 2, 1, 2, 3, 4, 5)


# Format the output of your 'normal' function such that numbers look nice and are centered in a 20 character column
def normal_function3(fn, *args):
    for arg in args:
        print('Result: {:^20.2f}'.format(fn(arg)))

normal_function3(lambda el: el * 2, 1, 2, 3, 4, 5)
