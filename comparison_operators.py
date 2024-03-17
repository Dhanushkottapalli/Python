# comparison_operators
'''
if the temperature is greater than 30
   it's a hot day
otherwise if it's less than 10
   it's a cold day
otherwise
   It's neither hot nor cold
'''
temperature=30
if temperature>30:
    print("It's a hod day")
else:
    print("It's not a hot day")

temperature=30
if temperature<30:
    print("It's a hod day")
else:
    print("It's not a hot day")


temp=int(input("Enter the temperature:-"))
if temp>30:
    print("It's a hot day")
elif temp<10:
    print("It's a cold day")
else:
    print("It's neither hot nor cold")

'''
if name is less than 3 characters long
    name must be at least 3 characters
otherwise if it's more than 50 characters long
    name can be a maximum of 50 characters
otherwise
    name looks good!
'''
name=input("Please enter your name:-")
if len(name)<3: #In this line len() function will count the number of characters in a sring which is stored in a cvariable name called "Name".
    print("Name must be at least 3 characters")
elif len(name)>50:
    print("Name can be a maximum of 50 characters")
else:
    print(f"{name} looks good!")
