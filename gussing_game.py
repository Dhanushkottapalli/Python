# gussing_game.py
secret_number = 9
guss_count=0
guss_limit=3
while guss_count<guss_limit:
    guess=int(input('Guss:-'))
    guss_count +=1
    if guess == secret_number:
        print('You win!')
        break
else:
    print("Try one more time")
