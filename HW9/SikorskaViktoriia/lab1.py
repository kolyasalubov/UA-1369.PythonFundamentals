import random


number_to_guess = random.randint(1, 100)


attempts = 10

print("Welcome to the Guessing Game!")
print("I have selected a number between 1 and 100. You have 10 attempts to guess it.")

for attempt in range(1, attempts + 1):

    user_guess = int(input(f"Attempt {attempt}/{attempts}: Enter your guess: "))

   
    if user_guess == number_to_guess:
        print(f"Congratulations! You guessed the number {number_to_guess} correctly in {attempt} attempts!")
        break
    
    elif user_guess < number_to_guess:
        print("Your guess is too low. Try again.")
    else:
        print("Your guess is too high. Try again.")


else:
    print(f"Sorry, you've used all your attempts. The correct number was {number_to_guess}. Better luck next time!")
