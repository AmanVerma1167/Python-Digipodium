#tuple- set - list(interchangeable)

x = [1,2,3,4,5,5,6,6,7]
xt = tuple(x) # list -> tuple
xl = list(xt) # tuple -> list
xs = set(x) # list -> set
xls = list(xs) # set -> list
xst = set(xt) # tuple -> set
y = tuple(xs) # set -> tuple

print(xt)
print(xl)
print(xs)
print(xls)
print(xst)
print(y)

# wap to create a tuple, by taking ten inputs from the user

x = []

for i in range(10):
    n = input("Enter The Number:")
    x.append(n)

print(x)
xl = tuple(x)
print(xl)