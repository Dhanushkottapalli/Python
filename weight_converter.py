# weight_converter
weight = int(input("Please enter your weight:-"))
unit= input("(k/K)kg or (g/G)grams:-")
if unit.upper() == 'K':
    x = weight*1000
    print(f"Your weight is {x}grams")
elif unit.upper() == 'G':
    y=weight/1000
    print(f"Your weight is {y}Kg")
else:
    print("Thank you.")
