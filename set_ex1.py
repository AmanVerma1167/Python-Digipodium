# we can make set from a list
# output: {1, 2, 3, 4}
my_set = set([1,2,3,4])
print(my_set)

# Set cannot have duplicates
# output: {1, 2, 3, 4}
my_set = {1,2,3,4,3,2}
print(my_set)

# my_set = {1,2,[3,4]}

# initialize my_set()
my_set = set()
print(my_set)

# add an element
# output:{2}
my_set.add(2)
print(my_set)

# add multiple elements
# output:{2, 3, 4}
my_set.update([2,3,4])
print(my_set)

# add list and set
# output:{1, 2, 3, 4, 5, 6, 8}
my_set.update([4,5],{1,6,8})
print(my_set)

# initialize my_set
my_set = {1,3,4,5,6}
print(my_set)

# discard an element
# output: {1, 3, 5, 6}
my_set.discard(4)
print(my_set)

# remove an element
# output: {1, 3, 5}
my_set.remove(6)
print(my_set)

# pops a random item
# output: {3, 5}
my_set.pop()
print(my_set)

# clear my_set
# output: set()
my_set.clear()
print(my_set)