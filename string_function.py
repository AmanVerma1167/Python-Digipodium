from helper import read

data = read('pride_n_prejudice.txt')

print(len(data))

newData = data[3:53]
print(newData)

# ...
#  formatting functions
# -lower
# -uppar
# -swapcase
# -capitalize
# -title
# -casefold


print(newData.lower())
print(newData.upper())
print(newData.swapcase())
print(newData.capitalize())
print(newData.title())
print(newData.casefold())


print('lower =>',newData.lower())
print('upper =>',newData.upper())
print('swapcase =>',newData.swapcase())
print('capitalize =>',newData.capitalize())
print('title =>',newData.title())
print('casefold  =>',newData.casefold())

# -ljust
# -rjust
# -center
# ...


word = 'Hello'
spacing = 20

ljust = word.ljust(spacing)
print(ljust)

word = 'Hello'
spacing = 20

ljust = word.ljust(spacing,'*')
print(ljust)

rjust = word.rjust(spacing,'-')
print(rjust)

cen = word.center(spacing,'😊')
print(cen)

# validation function - either True or False
w = 'Hello'

print(w)
print(w.isupper())
print(w.isalpha())
print(newData.isupper())
print(newData.islower())
print(newData.isalpha())
print(newData.isnumeric())
print(newData.isalnum())
print(newData.isidentifier())


# utility functions

idx = newData.find("Pride")
if idx==-1:
    print('Not Found')
else:
    print(f'Pride was found at index {idx}')

idx2 = data.index("in")
print(f'is was found at index {idx2}')

start_idx=0
for i in range(5):
    idx3 = data.find('in',start_idx)
    print(f'is was found at {idx3}')
    start_idx = idx3+1

num_of_in = data.count('in')    
print(f'in occurs {num_of_in} times')