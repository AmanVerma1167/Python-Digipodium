# dictionary with integer key
my_dict = {1: 'apple', 2: 'ball'}
print(my_dict)

val = ['Rajendra Singh', 30, 10, 'Accounts','Staff Officer', 600000, 7]

val_dict = {
    'Employee': 'Rajendra Singh', 'Age': 30,
    'Experience': 10, 'Dept': 'Accounts',
    'Designation': 'Staff Officer', 'Salary': 600000,
    'Team_Size': 7
}

# displaying a dict
print(val_dict)

# retrieval of value
ans = val_dict['Designation'] # key in square brackets
print(ans)
print(val_dict['Salary']) # correct
print(val_dict['Experience']) # correct

# adding a data inside dict
val_dict['Company'] = 'Acme.inc'

print(val_dict)

from pprint import pp

pp(val_dict)