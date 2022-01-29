from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface


question_bank = []
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface()

for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"]))

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}.")