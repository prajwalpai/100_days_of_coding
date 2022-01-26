from tkinter import *

window = Tk()
window.title('Mile to KM convertor')
window.minsize(width=220,height=100)

my_input= Entry(width=10)
my_input.grid(column=2, row=0)

miles_label = Label(text="Miles",font=("Arial",12))
miles_label.grid(column=3, row=0)

eq_label = Label(text="is equal to",font=("Arial",12))
eq_label.grid(column=0, row=1)

ans_label = Label(text="-",font=("Arial",12))
ans_label.grid(column=2, row=1)

km_label = Label(text="Km",font=("Arial",12))
km_label.grid(column=3, row=1)


def click_me():
    inmiles=int(my_input.get())
    inkm = inmiles * 1.609
    ans_label.config(text=inkm)

my_button = Button(text="Calculate", command=click_me)
my_button.grid(column=2, row=2)


window.mainloop()