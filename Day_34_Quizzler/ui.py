from tkinter import *
import time

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady= 20,bg=THEME_COLOR)
        self.score_numeral=0
        self.score = Label(text="Score: "+str(self.score_numeral),bg=THEME_COLOR, padx=20, pady = 20,fg="White",font=("Arial", 15))
        self.score.grid(column=1, row = 0)


        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question = self.canvas.create_text(150, 80, text="The best questions are the one we never asked", fill="black", font=("Arial", 20, "italic"), width=250)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)
        true_img = PhotoImage(file="images/true.png")
        self.btrue = Button(image=true_img, highlightthickness=0,highlightbackground=THEME_COLOR,command=self.process_answer_true)
        self.btrue.grid(column=0,row=3,padx=10,pady=10)

        false_img = PhotoImage(file="images/false.png")
        self.bfalse = Button(image=false_img, highlightthickness=0, highlightbackground=THEME_COLOR,command=self.process_answer_false)
        self.bfalse.grid(column=1, row=3,padx=10,pady=10)
        self.next_question()
        self.window.mainloop()

    def next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question,text=self.quiz.next_question())
            self.canvas.configure(bg="white")
            self.window.update()
        else:
            self.canvas.itemconfig(self.question, text="Your final score is "+str(self.score_numeral))
            self.canvas.configure(bg="white")
            self.btrue.destroy()
            self.bfalse.destroy()
            self.window.update()


    def process_answer_true(self):
        is_correct_answer = self.quiz.check_answer("True")
        if is_correct_answer:
            self.canvas.configure(bg="green")
            self.window.update()
            self.score_numeral += 1
            self.score.config(text="Score: "+str(self.score_numeral))
            time.sleep(1)
            self.next_question()
        else:
            self.canvas.configure(bg="red")
            self.window.update()
            time.sleep(1)
            self.next_question()


    def process_answer_false(self):
        is_correct_answer = self.quiz.check_answer("False")
        if is_correct_answer:
            self.canvas.configure(bg="green")
            self.window.update()
            self.score_numeral += 1
            self.score.config(text="Score: " + str(self.score_numeral))
            time.sleep(1)
            self.next_question()
        else:
            self.canvas.configure(bg="red")
            self.window.update()
            time.sleep(1)
            self.next_question()
