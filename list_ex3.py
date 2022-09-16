x = [1,2,3,4,5,1,3,4,21,3,11,21,1,1,1,1,1,2,2,2,3]

x_one =  x.count(1) # count function
x_two =  x.count(2)
x_three = x.count(3)
x_four = x.count(4) 
print('1 occurred',x_one,'times')
print('2 occurred',x_two,'times')
print('3 occurred',x_three,'times')
print('4 occurred',x_four,'times')

y = [21,32,43,5,45,56,5,6,7,8,9]
z = [31,33,4,45,6,3,2,4,5,6,7,8,9]

print('x adding y')
x.extend(y)
print(x)

print('x adding z')
x.extend(z)
print(x)

a = ['Apple','Banana','Cherry','Dragonfruit','Elaichi']
v = a.pop(3) # pop can remove value from an index
print(a)
print(v)
lv = a.pop() # pop remove last value by default
print(a)
print(lv)
