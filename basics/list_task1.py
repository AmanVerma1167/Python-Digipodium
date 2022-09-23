# (wap to create a numerical list of 10 values
# ,taken from the user and then display)
# sum
# mean
# median
# mode

# x = []
# sum = 0
# for i in range(0,n):
#     n = float(input("Enter The Value:"))

#     x.append(n)
#     sum= sum + i


# print("The Value Entered Were")
# print(x)
# print(sum)

x=[]
y=0
for i in range(10):
    n=float(input('Enter item in the list:'))
    x.append(n)

print('the value entered is')
print(x) 

for i in range(10):
    y=y+x[i]

mean=y/10
print("mean is- ",mean)

if len(x)/2==0:
    median=(y+1)/2
    print("Median is- ",median)

else:
    median=((y/2)+((y/2)+1))/2
    print("Median is- ",median)

import math

x = [2,2,3,3,1,2,3,4,5,6]
print("Sum:",sum(x))
print("Mean:",sum(x)/len(x))
x.sort()
if len(x) % 2 == 0:
    idx = len(x)//2
    value = x[idx] + x[idx+1]
    print("Median:",value/2)

else:
    value = x[len(x)//2 + 1] 
    print("Median:",value/2)   
