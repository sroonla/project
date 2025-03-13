import math
import random


def find_gcd(a, b):   # Вычисляет наибольший общий делитель двух чисел.
    return math.gcd(a, b)


def main():
    """Основная логика игры."""
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the greatest common divisor of given numbers.")

    rounds = 3  # Количество раундов
    for _ in range(rounds):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        correct_answer = find_gcd(num1, num2)

        print(f"Question: {num1} {num2}")
        user_answer = input("Your answer: ")

        if user_answer.isdigit() and int(user_answer) == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. ")
            print(f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return  # Завершает игру при ошибке

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()