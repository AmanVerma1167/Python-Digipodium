books = ["The Discovery Of India","The Secret",
"The Power Of Your Subconsious Mind","The Mahabharat Secret"]

books.append('The Final Empire') # add the value
books.append('Lost Horizon')
books.append('The Mahabharat Quest')
books.append('Inferno')

print(books)

print('idx\t| book')
for i,b in enumerate(books):
    print(f'{i}\t| {b}')

books[6] = 'The Well Of Ascention' # update the value
books[-1] = 'The Hero Of Ages'
books[2] = 'Legion'

print('idx\t| book')
for i,b in enumerate(books):
    print(f'{i}\t| {b}')

books.insert(3,'Legion:Skin Deep') # insert the value at particular index
books.insert(5,'Elantris')

print('idx\t| book')
for i,b in enumerate(books):
    print(f'{i}\t| {b}')

books.remove('Legion:Skin Deep') # remove the value
books.remove('Legion')

print('idx\t| book')
for i,b in enumerate(books):
    print(f'{i}\t| {b}')

# Extend Function

fruits = ['Apple','Banana','Cherry','Guava']
dry_fruits = ['Almond','Cashew','Walnut']
fruits.extend(dry_fruits)
print(fruits)