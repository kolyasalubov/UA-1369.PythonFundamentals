import random
#answer = int(input("Please guess the number in the range 0 - 100, following our tips: "))
# counter and tips 
# написати перевірку якщо більше 100 введено число 
def number_game():
    number = random.randint(0,100)
    higher = 0
    lower = 0
    while (higher + lower) < 10:
        
        answer = int(input("Please guess the number in the range 0 - 100, following our tips: "))
        if answer < 0 or answer > 100:
            print("Number must be between 0 and 100. Try again.")
            continue
        if number == answer:
            print ("Congrans ! you Win a beer! Nice job")
            break
        elif number > answer:
            print ("To low, try some higher number: ") 
            lower +=1
        else: 
            print ("To High my friend, try some lower number: ")
            higher +=1
        
    print (f"Number of times too high", higher)
    print (f"Number of times too lower", lower)
    print (f"Total  attempts: {higher+lower}/10\n")
    
    if (higher + lower) >= 10 and answer != number:
        print("Game over, you've used all 10 attempts.")
        print(f"The correct number was: {number}")

number_game()