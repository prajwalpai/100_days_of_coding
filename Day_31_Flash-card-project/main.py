from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

def flip_card():
    global current_card, flip_timer
    canvas.itemconfig(card_image,image=rear_img)
    canvas.itemconfig(frnt_language_text, text='English',fill = "white")
    canvas.itemconfig(frnt_word_text, text=current_card['English'],fill = "white")

def pick_random_word():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(card_image, image=frnt_img)
    canvas.itemconfig(frnt_language_text, text='French',fill = "black")
    canvas.itemconfig(frnt_word_text,text=current_card['French'],fill = "black")
    flip_timer = window.after(3000,func=flip_card)


def pick_next_word():
    global current_card, flip_timer, df_learnt
    window.after_cancel(flip_timer)
    df_learnt = df_learnt.append(df[df.French == current_card['French']])
    print(df_learnt)
    df.drop(df[df.French == current_card['French']].index, inplace=True)
    df_learnt.to_csv("data/french_words_learnt.csv")
    df.to_csv("data/french_words.csv")
    pick_random_word()


df = pd.read_csv("data/french_words.csv")
data_dict = df.to_dict(orient='records')
current_card = random.choice(data_dict)
try:
    df_learnt = pd.read_csv("data/french_words_learnt.csv")
except FileNotFoundError:
    df_learnt = pd.DataFrame()

window= Tk()
window.title("Flashy")
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,func=flip_card)


canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
frnt_img=PhotoImage(file="images/card_front.png")
rear_img = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400,263,image=frnt_img)
frnt_language_text = canvas.create_text(400, 150, text="French",fill = "black", font=(FONT_NAME, 40, "italic"))
frnt_word_text= canvas.create_text(400, 263, text="trouve",fill = "black", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0,row=0,columnspan=2)
pick_random_word()
right_img = PhotoImage(file="images/right.png")
r_button = Button(image=right_img, highlightthickness=0,highlightbackground=BACKGROUND_COLOR,command=pick_next_word)
r_button.grid(column=1,row=1)

wrong_img = PhotoImage(file="images/wrong.png")
w_button = Button(image=wrong_img, highlightthickness=0,highlightbackground=BACKGROUND_COLOR,command=pick_random_word)
w_button.grid(column=0,row=1)



window.mainloop()