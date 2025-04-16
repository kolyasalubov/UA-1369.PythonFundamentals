import random

number_to_guess = random.randint(1, 100)

attempts = 10

print("I have selected a number between 1 and 100. Try to guess it. You have 10 attempts.")

for attempt in range(1, attempts + 1):

    user_guess = int(input(f"Attempt {attempt}/{attempts}: Enter your number: "))

    if user_guess == number_to_guess:
        print(f"You guessed the number {number_to_guess} correctly in {attempt} attempts!")
        break

    elif user_guess < number_to_guess:
        print("Your number is too low. Try again.")
    else:
        print("Your number is too high. Try again.")

else:
    print(f"Sorry, you've used all your attempts. The correct number was {number_to_guess}")