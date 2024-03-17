'''
if it's hot
otherwise if it's cold day
    It's a cold day
    Wear warm clothes
otherwise
    It's a lovely day
    It's a hot day
    Drink plenty of water
'''
is_hot= True
if is_hot:                   #if this statement is true then it will execute the code written in if statement.
    print("It's a hot day")
    print("Drink plenty of water")
print("Enjoy your day")

is_hot= False
if is_hot:                   #this statement will not execute because if statement is false.
     print("It's a hot day")
print("Enjoy your day")

is_hot= True
if is_hot:                   #if this statement is true then it will execute the code written in if statement.
    print("It's a hot day")
    print("Drink plenty of water")
else:                        #if the 'if' statement is false then it will execute 'else' statement.
    print("It's a cold day")
    print("Wear warm clothes")
print("Enjoy your day")

is_hot= False
if is_hot:                   #if this statement is true then it will execute the code written in if statement.
    print("It's a hot day")
    print("Drink plenty of water")
else:                        #if the 'if' statement is false then it will execute 'else' statement.
    print("It's a cold day")
    print("Wear warm clothes")
print("Enjoy your day")

print("New")

is_hot= False
is_cold=False
if is_hot:                   #if this statement is true then it will execute the code written in if statement.
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("Enjoy your day")


'''
Price of a house is $1M
if buyer has good credit,
   they need to put down 10%
otherwise
   they need to put down 20%
'''
price=1000000
good_credits=False
if good_credits:
   down_payment=0.1*price
else:
    down_payment=0.2*price
print(f'Down payment:${down_payment}')
