# (1) Create a string and print it.

my_string = "Hello World"
print(my_string)

# (2) Take a string input and print it's length.

my_string1 = input("Enter The String:")
print(len(my_string1))

# (3) Print the last word of the string Python is great using slices.

name = "Python Is Great"
lname = name[-5:]
print(lname)

# (4) Print the each word in different line of string python is everywhere.

my_string2 = """Python Is Everywhere"""
print(*my_string2.split(),sep='\n')

# (5) Print the string Hello World! in reverse.

my_strings = "Hello World"
print(my_strings[::-1])

# (6) Convert the string How are you? in uppercase.

my_string3 = "How are you?"
print(my_string3.upper())

# (7) Convert the string How are you? in uppercase.

my_strings4 = "How It Is Going?"
print(my_strings4.lower())

# (8) Join the following list by spaces( ) and print the result.
# words = ['Python', 'is', 'easy', 'to', 'learn']

words = ['Python','is','easy','to','learn']
content = " ".join(words)
print(content)

# (9) Print a multiline string using a single print

data = ''
while True:
    line = input()
    if not line:
        break
    data += line + '\n'
print('------>OUTPUT<------')  
print(len(data),'chars')  


# (10) Print this string to move to newline '\n' is used. (results should look exactly like the provided string)

my_strings6 = "to move to newline '\\n' is used"
print(my_strings6)

# (11) Print a variable with some text using a single print function, output should look like following
# the variable is 15

a =15
print("the variable is ",a)

# (12) concatenate the following strings and print the result
# s1 = 'python '
# s2 = 'is '
# s3 = 'great.'


s1 = 'python '
s2 = 'is '
s3 = 'great.'
s = s1 + s2 + s3
print(s)
 
# second type
print(f'{s1}{s2}{s3}')

# third type
strlist = " ".join(s)
print(s)

# (13) Print # 20 times without using a loop

a = '#'
print(a*20) 


# (14) Print numbers from 1 to 9, each on a seperate line, followed by a dot, output should look like the following-
# 1.
# 2.
# 3.

for i in range(1,9+1):
    print(i,".")

# (15) Ask user to input a sentence and print each word on a different line

my_strings7 = input("Enter The Sentence:")
print(*my_strings7.split(),sep='\n')

# (16) Ask user to input a string and check if the string ends with '?'

my_strings8 = input("Enter The Sentence:")
if my_strings8[len(my_strings8)-1]=='?':
    print("The entered strng has '?' in the end of the String")
else:
    print("The entered sentance does not have '?' in it. ")

# (17) Ask user to input a string and print how many times e appeared in the string

my_strings9 = input("Enter The Sentence:")
print(my_strings9.count('e'))

# (18) Check if the user input is a number

my_strings10 = input("Enter The Number:") 
print(my_strings10.isnumeric())

# (19) Remove the extra spaces in beginning and in the end of the following string-
# text = '   this is not a good string

text="    this is not a good String     "
sen=text.lstrip()
print(sen.rstrip())

# (20) Ask user to input string, print found if any of the character is upper case.

my_string11 =  input("Enter The Sentence:") 
for i in my_string11:
    if i.isupper():
        print("Found")

# (21) Extract names from the following string and store them in a list.
# names = 'Joe, David, Mark, Tom, Chris, Robert'

names = 'Joe, David, Mark, Tom, Chris, Robert'
l=[]
l=names.split(',')
print(l)

# (22) In the following string, add aye in the end of every word and print the results.
# text = 'this is some text'

text = 'this is some text'
a=text.split( )
a.insert(1,'aye')
a.insert(3,'aye')
a.insert(5,'aye')
a.insert(7,'aye')
print(a)

# (23) ask user to enter a string and check if the string contains fyi

str=input("enter string to check the 'fyi' in the string:")
if "fyi" in str:
    print("yes , entered string have 'fyi' in the string")
else:
    print("No , entered string does not have 'fyi' in the string")


# (24) Remove all the special characters and numbers from the following string
# text = '%p34@y!*-*!t68h#&on404'

text = '%p34@y!-!t68h#&on404'
from string import punctuation
for p in punctuation:
    text=text.replace(p,'')
print(text)

# (25) calculate the average word length of the following paragraph
# this is a paragraph which is written just for the purpose of providing content to let the average word length be calculated

str1="this is a paragraph which is written just for the purpose of providing content to let the average word length be calculated"
w=str1.split()
print("number of words in the given string is",len(w))
