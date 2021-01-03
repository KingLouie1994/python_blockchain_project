import copy

# Create a list "person" dictionaries with a name, age and list of hobbies for each person. Fill in any data you want.
persons = [
    {'name': 'Luis', 'age': 26, 'hobbies': ['golf', 'tennis', 'coding']},
    {'name': 'Felix', 'age': 23, 'hobbies': ['running', 'harry potter', 'barbecue']},
    {'name': 'Susanne', 'age': 54, 'hobbies': ['skiing', 'reading', 'hiking']}
]


# Use a list comprehension to convert this list of persons into a list of names as strings
names = [person['name'] for person in persons]
print(names)


# Use a list comprehension to check whether all persons are older than 20
old_enough = all([person['age'] >= 20 for person in persons])
print(old_enough)


# Copy the person list such that you can safely edit the name of the first person without changing the original list.
copied_persons = []
for person in persons:
    copied_person = copy.deepcopy(person)
    copied_persons.append(copied_person)

copied_persons[0]['name'] = 'Manolo'
print(copied_persons[0]['name'])
print(persons[0]['name'])


# Unpack the porsons of the original list into different variables and output these variables
a,b,c = persons
print(a)
print(b)
print(c)