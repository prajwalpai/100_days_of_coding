class QuizBrain():

    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)


    def next_question(self):
        q_num = self.question_number
        q_text = self.question_list[q_num].text
        q_ans = self.question_list[q_num].answer
        answer=input(f"Q.{q_num}: {q_text}. (True/False)? : ")
        if answer == q_ans:
            self.score += 1
            print("You got it right!")
        else:
            print("You got it wrong!")
        print(f"The correct answer was {q_ans}")
        self.question_number += 1
        print(f"Your current score is {self.score}\n\n")