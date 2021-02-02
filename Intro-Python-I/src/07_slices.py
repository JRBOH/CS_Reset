"""
Python exposes a terse and intuitive syntax for performing
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string.

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

"""
a[start:stop]  <<< items start through stop-1
a[start:]      <<< items start through the rest of the array
a[:stop]       <<< items from the beginning through stop-1(inc,excl)
a[:]           <<< a copy of the whole array
a[start:stop:step]
START is INCLUSIVE
STOP is EXCLUSIVE
"""

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
# print(a[n]) where n is a given elements position from head
print(a[1]) # Accessing the SECOND element in the list "a"

# Output the second-to-last element: 9
# print(a[-n]) where n is a given elements position from tail
print(a[-2]) # accessing from the tail, 2 positions

# Output the last three elements in the array: [7, 9, 6]
# a[start:]
print(a[3:]) # pos indexing
print(a[-3:]) # negative indexing

# Output the two middle elements in the array: [1, 7]
# a[start:stop]
print(a[2:4]) # positive indexing
print(a[-4:4]) # mixed indexing
print(a[2:-2]) # mixed indexing
print(a[-4:-2]) # negative indexing

# Output every element except the first one: [4, 1, 7, 9, 6]
# a[start:]
print(a[1:])
print(a[-5:])

# Output every element except the last one: [2, 4, 1, 7, 9]
print(a[:5])
print(a[:-1])

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
print(s[7:12])
print(s[-6:-1])
