import random

import prompt


def is_even(number):  # Проверка на четность-нечетность
    return number % 2 == 0


def play_even_game():  # Логика игры
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers = 0

    while correct_answers < 3:
        number = random.randint(1, 100)  # Генерируем случайное число
        print(f"Question: {number}")
        answer = prompt.string("Your answer: ").strip().lower()

        correct_answer = "yes" if is_even(number) else "no"

        if answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. ")
            print(f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def main():
    """Точка входа в игру."""
    play_even_game()


if __name__ == "__main__":
    main()