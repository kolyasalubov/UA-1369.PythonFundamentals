import random

random_number = random.randint(1, 100)

print("TRY TO GUESS A NUMBER GAME\nYou have 7 tries.\n")
input_value = int(input("Enter a number between 1 and 100: "))
tries = 7

while tries > 0:
    tries -= 1

    if input_value > random_number:
        print("Too high!")
    elif input_value < random_number:
        print("Too low!")
    else:
        print("Congratulations! You guessed it! "
              "The number was {}".format(random_number))
        break

    print(f"Attempts left: {tries}\n")
    if tries >0:
        input_value = int(input("Enter a number between 1 and 100: "))
    else:
        print(f"Sorry, you lost! The number was {random_number}")
