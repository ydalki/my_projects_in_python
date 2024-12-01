import random
import time
print("""

NUMBER GUESSİNG GAME
 GUESS THE NUMBER BETWEEN 20 AND 40

""")

random_number=random.randint(20,40)
chance_of_guessing=5
while True:
    guess=int(input("your gues:"))
    if(guess<random_number):
        print("being looked at")
        time.sleep(1)
        print("nooo go up")
        chance_of_guessing-=1
    elif(guess>random_number):
        print("being looked at")
        time.sleep(1)
        print("nooo go down")
        chance_of_guessing -= 1
    else:
        print("being looked at")
        time.sleep(1)
        print("congratulations! the number:",random_number)
        break
    if (chance_of_guessing==0):
            print("your chances are finished")
            print("the number is",random_number)

