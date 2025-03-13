from brain_games.engine import run_game
from brain_games.games.calc import RULE, get_question_and_answer

def main():
    run_game(RULE, get_question_and_answer)

if __name__ == "__main__":
    main()