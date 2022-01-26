from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checks = "👍🏻"
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    global checks
    reps=0
    checks=''
    window.after_cancel(timer)
    check_marks.config(text=checks)
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text=f"00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps in list(range(1,8,2)):
        title_label.config(text="Work",fg=GREEN)
        countdown(WORK_MIN*60)
    if reps in list(range(2,7,2)):
        title_label.config(text="Short Break",fg=PINK)
        countdown(SHORT_BREAK_MIN*60)
    if reps == 8:
        title_label.config(text="Long Break", fg=RED)
        countdown(LONG_BREAK_MIN*60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):

    min,sec = divmod(count,60)
    canvas.itemconfig(timer_text,text=f"{min:02d}:{sec:02d}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown,count-1)
    else:
        start_timer()
        if reps%2 ==0:
            global checks
            check_marks.config(text=checks)
            checks = checks+"👍🏻"

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pai Pomodoro Timer")
window.minsize(width=400,height=100)
window.config(padx=20,pady=20, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg= YELLOW, font=(FONT_NAME, 40, "bold"))
title_label.grid(column=2,row=1)

canvas = Canvas(width=270, height=270, bg=YELLOW, highlightthickness=0)
tomoto_img = PhotoImage(file="tomato.png")
canvas.create_image(150,150, image=tomoto_img)
timer_text = canvas.create_text(150, 170, text="00:00",fill = "white", font=(FONT_NAME, 40, "bold"))
canvas.grid(column=2,row=2)

start_butt = Button(text="Start",highlightbackground=YELLOW, command=start_timer)
start_butt.grid(column=1,row=3)

reset_butt = Button(text="Reset",highlightbackground=YELLOW, command=reset_timer)
reset_butt.grid(column=3,row=3)

check_marks = Label(bg=YELLOW)
check_marks.grid(column=2,row=3)

window.mainloop()