import random

print("""Welcome to the Game.
Try to guess the randomly generated number from range of 1 to 100 in 10 tries.
Good luck!""")

tries = 10
random_number = random.randint(1,100)

for i in range(1, tries + 1):

    user_number = int(input("Enter the number: "))

    if random_number == user_number:
        print(f"Congratulation! You are right! The number needed to guess was {random_number}")
        break
    elif random_number > user_number:
        print("Nice try. The entered number is less than the number needed to guess. Try again.")
    else:
        print("Nice try. The entered number is bigger than the number needed to guess. Try again.")

else:
    print(f"You did 10 tries. Unfortunately, you did not guess the number. The number needed to guess was {random_number}")