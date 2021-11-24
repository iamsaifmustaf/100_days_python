class QuizBrain:

    score = 0
    question_number = 0

    def __init__(self,list):
        self.question_number = 0
        self.question_list = list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"\nQ.{self.question_number}: {current_question.text} (T/F): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("\nYou Got it Right :)\n")
            self.score += 1
        else:
            print("\nThat's wrong :(\n")
        print(f"\nThe correct answer was: {correct_answer}. ")
        print(f"Your current score is : {self.score}/{self.question_number}.")