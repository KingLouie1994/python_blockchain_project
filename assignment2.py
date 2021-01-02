# Create a list of names and use a for loop to output the length of each name
names = ["Luis", "Felix", "Susanne", "Dirk", "Nadine"]

print("Length of all 5 names:")
for name in names:
    print(len(name))

print("-" * 30)
# Add an if check inside the loop to only output names longer than 5 characters
print("Names longer then 5 characters:")
for name in names:
    if len(name) > 5:
        print(name)

print("-" * 30)
# Add another if check to see whether the name includes a "n" or "N" character
print("Names that include n or N:")
for name in names:
    if len(name) > 5 and ("n" in name or "N" in name):
        print(name)

print("-" * 30)
# Use a while loop tp empty the list of names
while len(names) > 0:
    names.pop()
    print(names)
