Basic_salary = float(input("Enter Employee Basic Salary:"))

if Basic_salary > 100000:
    Gross_salary = Basic_salary+((Basic_salary*3.5)/100)+((Basic_salary*9.1)/100)
    print("Gross Salary Of Employee:",Gross_salary)

elif Basic_salary > 80000 or Basic_salary <= 100000:
    Gross_salary = Basic_salary+((Basic_salary*3.2)/100)+((Basic_salary*9)/100)
    print("Gross Salary Of Employee:",Gross_salary)    

elif Basic_salary > 60000 or Basic_salary <= 80000:
    Gross_salary = Basic_salary+((Basic_salary*2.8)/100)+((Basic_salary*9)/100)
    print("Gross Salary Of Employee:",Gross_salary) 

elif Basic_salary > 50000 or Basic_salary <= 60000:
    Gross_salary = Basic_salary+((Basic_salary*2.5)/100)+((Basic_salary*8)/100)
    print("Gross Salary Of Employee:",Gross_salary)  

elif Basic_salary > 40000 or Basic_salary <= 50000:
    Gross_salary = Basic_salary+((Basic_salary*2.5)/100)+((Basic_salary*7.7)/100)
    print("Gross Salary Of Employee:",Gross_salary) 

elif Basic_salary > 30000 or Basic_salary <= 40000:
    Gross_salary = Basic_salary+((Basic_salary*2.2)/100)+((Basic_salary*8)/100)
    print("Gross Salary Of Employee:",Gross_salary)            

elif Basic_salary > 20000  or Basic_salary <= 30000:
    Gross_salary = Basic_salary+((Basic_salary*2.2)/100)+((Basic_salary*7)/100)
    print("Gross Salary Of Employee:",Gross_salary) 

elif Basic_salary > 10000 or Basic_salary <= 20000:
    Gross_salary = Basic_salary+((Basic_salary*2.2)/100)+((Basic_salary*6)/100)
    print("Gross Salary Of Employee:",Gross_salary) 

else:
    print("Wrong information entered.")    