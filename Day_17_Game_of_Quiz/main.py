from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank=[]
for question in question_data:
    question_bank.append(Question(question['text'],question['answer']))


quiz = QuizBrain(question_bank)


correct_answer = True

while quiz.still_has_questions():
    quiz.next_question()

print(f"\nWell Played. Your final Quiz score is {quiz.score}\n")