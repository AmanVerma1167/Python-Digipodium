# for i in range(100):
#     print("Hello")

# for i in range(100):
#     print("Hello",i)   

# for i in range(100):
#     print(i, end=' ')

# for i in range(1,24):
#     print(i)  

# for i in range(10,21):
#     print(i, end='x')  

# for i in range(1,11,2):
#     print(i, end=' ')   

# reverse loop
# for i in range(10, 0, -1): 
#     print(i, end=' ')   

# print("=>")
# data = [1,2,3,4,5,6,7,7,8,9]
# for i,d in enumerate(data):
#     print(i, d)

# print("=>")
# data = ['apple','cherry','guava','banana','samosa']
# for i,d in enumerate(data):
#     print(i, d)

# print("=>")
# data = ['apple','cherry','guava','banana','samosa']
# for i in enumerate(data):
#     print(i)    

names = ['apple','banana','cherry']
price = [100, 40, 65]

for n,p in zip(names, price):
    print(f'{n} => ${p}')
