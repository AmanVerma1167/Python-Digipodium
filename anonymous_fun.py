

num = [1,2,3,4,5,6,7,8,90,10,34,2,12,33,331,45,15,87]
names = ['Ajay Singh','Vijay Pratap','Gunja Thakur']

num_sqr = list(map(lambda i: i**2, num))
print(num_sqr)

num_eq1 = list(map(lambda i: i+4 * i**2,num))
print(num_eq1)

first_names = tuple(map(lambda nm: nm.split()[0], names))
print(first_names)

