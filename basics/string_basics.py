# defining strings in Python
# all of the following are equivalent

my_string1 ='Hello'
print(my_string1)

my_string2 = "Hello"
print(my_string2)

my_string3 = '''Hello'''
print(my_string3)

# triple quotes string can extend multiple lines

my_string4 = """Hello, welcome to 
the world of python"""
print(my_string4)     

print(my_string1[0]) # first char
print(my_string1[1]) # second char
print(my_string1[-1]) # last char
print(my_string1[-3]) # third last char

print(my_string1[0], my_string1[2], my_string1[3])

# string slicling

name = 'Vijay Dinanath Chauhan'
for i,c in enumerate(name):
     print(i,c)
mname = name[6:-8]
print(mname)
fname = name[:5]
print(fname)
lname = name[-7:]
print(lname)
mmname = name[10:15]
print(mmname)

# reverse the string

print(name[::-1])

print(name[:5][::-1])

# every even index char

print(name[::2]) #vjy

# every odd index char

print(name[1::2])

# Bulitin function for Strings

x = chr(65)
print(x)

x = chr(2365)
print(x)

x = chr(12365)
print(x)

for i in range(200,15000):
    print(i, chr(i))

for i in range(15000,20000):
    print(i, chr(i))

y = ord('A')
print(y)

y = ord('a')
print(y)

y = ord('{')
print(y)

# String Operations

a = 'Apple'
b = 'Juice'
ab = a + b
print(ab)

ab = a + ' ' + b
print(ab)

w1 = 'This'
w2 = 'Is'
w3 = 'Amazing'
msg = w1 + w2 + w3
print(msg)

# adding space between string

msg = w1 + ' ' + w2 + ' ' + w3
print(msg)

# Duplication

word = 'Hi'
print(word * 3)

print('-'*25)



     

