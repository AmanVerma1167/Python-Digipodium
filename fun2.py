# function returning value

def getsalary():
    val = int(input('Enter Salary:'))
    fine = .09
    sal = val * fine
    return sal

print(getsalary())
ans = getsalary()
print('Salary',ans)



def get_salary():
    val = int(input('Enter Salary=>'))
    fine = .09
    return val * fine

print('Salary=>',get_salary())

final_salary = get_salary() + 1000
print('Salary=>', final_salary)

# wap to find amount in si

def amount():
    p = float(input('Enter Princial Amount=>'))
    r = float(input('Enter Rate=>'))
    t = float(input('Enter Time=>'))
    si = (p * r * t)/100
    amt = si + p
    return amt, si

print('Amount=>',amount())

# or this way

ans,si = amount()
print(f'The Amount Will Be {ans} on Simple Interest{si}')

# or this way
print(f'The Amount Will Be {amount()[0]}')


