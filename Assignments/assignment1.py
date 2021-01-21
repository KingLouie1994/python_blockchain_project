# Create two variables - one with your name and one with your age (if you want make it through inputs)
user_name = input("Please tell me your name:")
user_age = input("How old are you:")

# Create a function which prints your data as one string
def print_data_as_one_string():
    print("Hi my name is " + user_name + " and I'm " + user_age + " years old")

# Create a function which prints any data (two arguments) as one string
def print_any_data(name, age):
    print("Hi my name is " + name + " and I'm " + age + " years old")

# Create a function which calculates and returns the number of decades lived by the person
def calculate_decades(age):
    return "You already lived " + str(int(age)//10) + " decades"


print_data_as_one_string()

print_any_data(user_name, user_age)

print(calculate_decades(26))
