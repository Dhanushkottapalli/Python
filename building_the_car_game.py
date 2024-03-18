# building_the_car_game
# command = ""
# while command != "QUIT":
#     command=input("> ").lower()
#     if command == "start":
#         print("Car started....")
#     elif command == "stop":
#         print("Car stopped.")
#     elif command == "help":
#         print('''
# Start -- To start the car
# Stop -- To stop the car
# Quit -- To quit
#         ''')
#     elif command == "quit":
#         break
#     else:
#         print("Sorry I dont under stand that")


command = ""
status= False
while True:
    command=input("> ").lower()
    if command == "start":
        if status:
            print("Car is already started....")
        else:
            status= True
            print("Car started....")
    elif command == "stop":
        if status:
            print("Car is already stopped...")
        else:
            status = True
            print("Car stopped!")
    elif command == "help":
        print('''
Start -- To start the car
Stop -- To stop the car
Quit -- To quit
        ''')
    elif command == "quit":
        break
    else:
        print("Sorry I dont under stand that")
