from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password = ' '
    result = ' '
    nr_letters=4
    nr_symbols=4
    nr_numbers=2
    for letter in range((nr_letters + nr_symbols + nr_numbers)):
        if nr_letters:
            password += random.choice(letters)
            nr_letters = nr_letters - 1
        if nr_symbols:
            password += random.choice(symbols)
            nr_symbols = nr_symbols - 1
        if nr_numbers:
            password += random.choice(numbers)
            nr_numbers = nr_numbers - 1
    password_list = list(password)
    random.shuffle(password_list)
    result = ''.join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0,result)
    window.clipboard_clear()
    window.clipboard_append(result)
    return

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website=website_entry.get()
    email=email_entry.get()
    passwd=password_entry.get()
    line=website+" | "+email+" | "+passwd
    is_ok = False
    if not website or not passwd:
        messagebox.showerror(title="Alert",message="The fields cannot be empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"On {website}, \nemail : {email}\npassword : {passwd}\nIs it ok to save?")

    if is_ok:
        with open("mypasswds.txt", mode='a') as file:
            file.write(line+"\n")
        password_entry.delete(0, END)
        website_entry.delete(0, END)
    return

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
#window.minsize(width=500, height=500)
window.config(padx=20,pady=20)



canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_image)
canvas.grid(column=2,row=0)

website_label = Label(text="Website : ")
website_label.grid(column=1,row=1)
website_entry = Entry(width=36)
website_entry.grid(column=2,row=1,columnspan=2)
website_entry.focus()

email_label= Label(text="Email/Username :")
email_label.grid(column=1,row=2)
email_entry=  Entry(width=36)
email_entry.grid(column=2,row=2,columnspan=2)
email_entry.insert(0,"prajwal.pai@gmail.com")



password_label= Label(text="Password : ")
password_label.grid(column=1,row=3)
password_entry=  Entry(width=22)
password_entry.grid(column=2,row=3)

gen_passwd_button = Button(text="Generate Password",width=10,command=generate_password)
gen_passwd_button.grid(column=3,row=3)

add_button= Button(text="Add",width=34,command = save_password)
add_button.grid(column=2,row=4,columnspan=2)



window.mainloop()