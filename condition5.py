email = input("Enter your email=>")

if '@' in email and len(email) >=11 and ('.com' in email or 'org' in email):
    print("Badiya email hai")
else:
    print("Ye email to ni lg rha")    