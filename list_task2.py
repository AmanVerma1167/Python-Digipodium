#(1) wap to create a list of 5 names taken from the user and then display each name in reverse

#(2) wap to print a fibonacci series using the concept of list (0,1,1,2,3,5,8,11....)

#(3) wap to generate a new list that contains squares of each numbers from existing list
# "ex" 'x= [2,3,4,5] => [4,8,16,25]

#(4) wap to generate a new list from an existing list of numbers that contains only odd numbers

#(5) wap to generate a new list adding 2 list elementwise

# (1)

x = []
for i in range(5):
    n= input("Enter the name:")
    x.append(n)

print("Name List:")    
print(x)

for name in x:
    print(name[::-1])

# (2)

fib = [0,1]
for i in range(15):
    fib.append(fib[-1] + fib[-2])
print(fib)    

# (3)

x = [1,2,3,3,4,5,6,7]
x2 = []
for num in x:
    x2.append(num ** 2)

print(x)  
print(x2) 

# (4)

xodd = []
for i in x:
    if i % 2 != 0:
        xodd.append(i)

print(xodd)        
# list comprehension
xodd = [i for i in x if i % 2 == 0 ]

# (5)

x = [1,2,3,4,5,6]
y = [6,4,3,2,1,2]
z = []

for i,j in zip(x,y):
    z.append(i + j)
print(x)   
print(y) 
print(z)






