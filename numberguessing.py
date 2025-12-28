import random

maximun_attempts=20
attempt = 0

secret_number = random.randint(0,500)

while attempt< maximun_attempts:
    guess= int(input("Enter your Guuess from 0 to 500: "))
    attempt +=1

    if guess < secret_number:
        print(" OPPS! Your guess is low, Try again!!")
    elif guess > secret_number:
        print("OPPS! Your guess is high, Try again!!")
    else:
        print("Congratulations! You guessed it right!")
        print(f"You guessed in {attempt} attempts")
        exit()
    
print("Sorry! you ran out of attempts.")
print(f"Secret number was {secret_number}")