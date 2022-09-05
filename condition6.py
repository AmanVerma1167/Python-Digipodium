email = input("Enter your email=>")

if '@' not in email:
    print("Your email does not have @") 
elif len(email) < 11:
    print("Length of email not valid")  
elif '.com' not in email and 'org' not in email:
    print("Invalid domain") 
else:
    print("Your email is look valid")    


