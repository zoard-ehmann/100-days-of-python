import html
from question_model import Question

class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.current_question: Question
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        sanitized_q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {sanitized_q_text}"

    def check_answer(self, user_answer: str):
        if user_answer.lower() == self.current_question.answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print()