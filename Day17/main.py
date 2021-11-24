from art import *
import time
from os import system as sys
from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

def quizbrain():
    question_bank = []

    for item in question_data:
        question_bank.append(Question(item['text'], item['answer']))

    tprint("WELCOME")
    time.sleep(1)
    tprint("TO")
    time.sleep(1)
    tprint("!QuizBrain!")
    time.sleep(1)
    sys('cls')
    quiz = QuizBrain(question_bank)
    while quiz.still_has_questions(): 
        quiz.next_question()
        time.sleep(2)
        sys('cls')

    tprint("\n\n--- GAME OVER ---\n\n")

quizbrain()
while (input("Do you want to play again? Enter -n- for yes and -y- for no: ") == "y"):
    sys('cls')
    quizbrain()