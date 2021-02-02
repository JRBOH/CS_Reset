"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated.

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array
# [1, 2, 3, 4, 5]

y_01 = [i for i in range(1, 6)]
print ("Short version:", y_01)


long_version = []

for i in range(1, 6):
    long_version.append(i)

print("Long version:", long_version)


# Write a list comprehension to produce the cubes of the
# numbers 0-9: [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y_02 = [num**3 for num in range(10)] # <<< because we start at zero
                                  # we can place single value in
                                  # "range()""

print(y_02)

# Write a list comprehension to produce the uppercase
# version of all the elements in array "a".
# Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

y_03 = [item.upper() for item in a]

print(y_03)

# Use a list comprehension to create a list containing
# only the _even_ elements the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it
# work?
y_04 = [num for num in x if int(num) % 2 == 0]

print(y_04)