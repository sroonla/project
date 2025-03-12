import random

OPERATORS = ['+', '-', '*']
MIN_NUMBER = 1
MAX_NUMBER = 20

def get_question_and_answer():
    num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    operator = random.choice(OPERATORS)

    question = f"{num1} {operator} {num2}"
    correct_answer = str(eval(question))  # Вычисляем верный ответ

    return question, correct_answer