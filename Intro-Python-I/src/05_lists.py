"""
For the exercise, look up the methods and functions that are available for use
with Python lists.
"""


"""!!!For the following, DO NOT USE AN ASSIGNMENT (=)."""

x = [1, 2, 3]
y = [8, 9, 10]

# Change x so that it is [1, 2, 3, 4]
x.append(4) # just like "push" in js
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
x.extend(y)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
x.remove(8) # better
"""
pop method "saves" the value that you remove and can recall
ir
"""
# x.pop(x.index(8)) # Another way
# below, best?
# x.pop(-3) # Negative indexing
# x.pop(4) # Positive indexing
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
x.insert(-1, 99) # negative indexing
# x.insert(4, 99) # positive indexing
print(x)

# Print the length of list x
print(len(x))

# Print all the values in x multiplied by 1000
print([num for num in x])
print([num * 1000 for num in x])

print()

"""long way"""
for num in x:
    print(num * 1000)

print()

for i in range(len(x)):
    print(x[i] * 1000)
