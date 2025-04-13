import random

def guess_the_number():
    """Гра вгадай число."""

    secret_number = random.randint(1, 100)
    attempts = 10

    print("Я загадав число від 1 до 100. Спробуйте вгадати його за 10 спроб.")

    while attempts > 0:
        try:
            guess = int(input(f"Спроба {11 - attempts}: Введіть ваше число: "))
        except ValueError:
            print("Будь ласка, введіть ціле число.")
            continue

        if guess == secret_number:
            print(f"Вітаємо! Ви вгадали число {secret_number} за {11 - attempts} спроб!")
            return
        elif guess < secret_number:
            print("Загадане число більше.")
        else:
            print("Загадане число менше.")

        attempts -= 1

    print(f"Ви не вгадали число. Я загадав {secret_number}.")

if __name__ == "__main__":
    guess_the_number()