# birth_year=input('Birth year:-')
# age = 2024 - birth_year
# print(age)
              #if you run the above written code, You will get error because in 2nd line "birth_year" is in string, So Python intreptor Cant add or sub number and string it will give an error.
#So in python we have some "Type Conversion" which converts from one type to another.
int()   #int() is used to convert string to inteager.
float() #float() is used to convert string to floating point.
bool()  #bool() is used to convert string to Boolian value.



birth_year=input('Birth year:-')
print(type(birth_year))           #type() is used to show whioch kind of data is stored in a variable.
age = 2024 - int(birth_year)
print(type(age))
print(age)

# Write a program to ask a user their weight in KG, Convert it to grams and print on the terminal.

weight=float(input("Please enter your weight in kilogrammes:-")) #we should use float because if user enter weight in floting point it will throw an error.
gram=weight*1000
print("Your weight in grammes is:-",gram)
