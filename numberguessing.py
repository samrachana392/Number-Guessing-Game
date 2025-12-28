import random

print("Welcome to Number Guessing Game")

# Difficulty SElection
print("Choose Difficulty:")
print("1 - Easy (0-50, 10 attempts)")
print("2 - Medium (0-200, 15 attempts)")
print("3 - Hard (0-500, 20 attempts)")
choice = int(input("Enter 1, 2 or 3: "))

if choice == 1:
    max_num = 50
    maximun_attempts = 10
elif choice == 2:
    max_num = 200
    maximun_attempts=15
elif choice == 3:
    max_num = 500
    maximun_attempts=20
else:
    print("Invalid Input")
    exit()


secret_number = random.randint(0,max_num)
attempt = 0


while attempt< maximun_attempts:
    try: 
        guess= int(input(f"Enter your Guuess from 0 to {max_num}: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
   
    if guess < 0 or guess > max_num:
        print("Number out of range, Try again.")
        continue   
   
    attempt +=1

    if guess < secret_number:
        print("OPPS! Your guess is low.")
    elif guess > secret_number:
        print("OPPS! Your guess is high.")
    else:
        print("Congratulations! You guessed it right!")
        print(f"You guessed in {attempt} attempts")
        break
    

    # Hint System
    diff = abs(secret_number - guess)
    if diff<=5:
        print("Very close!!")
    elif diff<=15:
        print("Close!")
    else:
        print("far away!")

else:
    print("Sorry! you ran out of attempts.")
    print(f"Secret number was {secret_number}")

print("Thank you for playing!")