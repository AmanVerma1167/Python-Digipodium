# union operation
A = {1,2,3,4,5}
B = {4,5,6,7,8}

# use | operator
# output: {1, 2, 3, 4, 5, 6, 7, 8}
print(A | B)

# use union function on A
print(A.union(B))

# use union function on B
print(B.union(A))

# intersection operation

# use & operator
# output: {4, 5}
print(A & B)

# output: {4, 5}
print(A.intersection(B))

# Set Difference Operation

# use - operator on A
# output: {4, 5}
print(A - B)

# use difference function on A
# output: {1, 2, 3}
print(A.difference(B))

# use - operator on B
# output: {8, 6, 7}
print(B - A)

# Set Symmetric Difference

# use ^ operator
# output: {1, 2, 3, 6, 7, 8}
print(A ^ B)

# use symmetric_difference function on A
# output: {1, 2, 3, 6, 7, 8}
print(A.symmetric_difference(B))


