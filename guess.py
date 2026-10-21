import random

secret = random.randint(1, 20)
attempts = 0
MAX_ATTEMPTS = 5

while attempts <=MAX_ATTEMPTS:
    num=int(input("Enter your number:"))
    if secret==num:
        print("You guess the right number")
        break

    elif secret<num:
        print("you are higher then number")

    elif secret>num:
        print("you are lower then the number")
    attempts+=1

if attempts<MAX_ATTEMPTS:
    print("You ran out of the guess")
        
