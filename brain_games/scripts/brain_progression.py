import random
from brain_games.engine import run_game

RULE = "What number is missing in the progression?"

def get_question_and_answer():
    start = random.randint(1, 20)
    step = random.randint(2, 10)
    length = random.randint(5, 10)

    progression = [start + i * step for i in range(length)]
    hidden_index = random.randint(0, length - 1)

    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = ".."
    
    question = " ".join(map(str, progression))
    return question, correct_answer

# Создаём объект с атрибутом `get_question_and_answer`
game = type("Game", (), {"get_question_and_answer": get_question_and_answer})

def main():
    run_game(game)  # Передаём объект, а не функцию

if __name__ == "__main__":
    main()