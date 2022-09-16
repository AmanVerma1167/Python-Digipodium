# split function

msg = "We will be seeing the horizon"

words = msg.split()
print(words)

words = msg.split('e')
print(words)

# replace function

updated_msg = msg.replace('seeing','viewing')
print(updated_msg)

updated_msg = msg.replace('e','')
print(updated_msg)

# join function

path = ['jitni','tu','milti','jaye','utni','lge','thodi','thodi']

content = " ".join(path)
print(content)

# strip function

name = "   hello chris   "
cleaned_name = name.strip()
print(cleaned_name)
print(len(name),len(cleaned_name))

msg2 = '''

we are venom

'''
cleaned_msg2 = name.strip()
print(cleaned_name)
print(len(msg2),len(cleaned_msg2))

# wap to find frequency of all the vowels in the ''data'

from helper import read

data = read('pride_n_prejudice.txt')

for vowel in 'aeiou':
    print(f'{vowel} => {data.lower().count(vowel)} times')


# wap to remove all the punctuations from the string
str = 'he@#11%o!@ adnqihiudfhu $@%!#^%&^'

str = 'he@#ll%!o $w@o%!r#l^d%&^'

from string import punctuation
for p in punctuation:
    str = str.replace(p,'')
print(str)
