# Accessing tuple elements using slicing
my_tuple = ('e','x','c','a','l','i','b','u','r')

# elements 2nd and 4th
# output: ('x','c','a')
print(my_tuple[1:4])

# elements beginning to 2nd
# output: ('e', 'x')
print(my_tuple[:-7])

# elements 8th and end
# output: ('u','r')
print(my_tuple[7:])

# elements beginning to end
# output: ('e', 'x', 'c', 'a', 'l', 'i', 'b', 'u', 'r')
print(my_tuple[:])

