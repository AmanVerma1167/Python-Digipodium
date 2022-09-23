email = input("Enter your email=>")

if '@' in email:
    if len(email) >=11:
        if '.com' in email or 'org' in email:
            print("Your email look valid")
        else:
            print("Invalid domain")    
    else:
        print("Length of email not valid")    
else:
    print("Your email does not have @")            