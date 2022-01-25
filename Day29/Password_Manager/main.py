from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle

import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list += [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)
    password = "".join(password_list)
    
    entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_website.get()
    username = entry_username.get()
    password = entry_password.get()
    
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(title="Blank Fields", message="One or more fields are empty.")
    else:
        is_correct = messagebox.askokcancel(title=website, message=f"Email: {username}\nPassword: {password}\nIs it correct?")
        
        if is_correct:
            with open("Day29/Password_Manager/data.txt", mode="a") as data:
                data.write(f"{website} | {username} | {password}\n")
            entry_website.delete(0, END)
            entry_password.delete(0, END)
            entry_website.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo = PhotoImage(file="Day29/Password_Manager/logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
label_website = Label(text="Website:", width=15, anchor="e")
label_username = Label(text="Email / Username:", width=15, anchor="e")
label_password = Label(text="Password:", width=15, anchor="e")

# Entries
entry_website = Entry(width=54)
entry_username = Entry(width=54)
entry_password = Entry(width=35)

# Buttons
button_generate = Button(text="Generate Password", command=generate_password)
button_add = Button(text="Add", width=45, command=save)

# Layout
label_website.grid(row=1, column=0)
entry_website.grid(row=1, column=1, columnspan=2)
entry_website.focus()
label_username.grid(row=2, column=0)
entry_username.grid(row=2, column=1, columnspan=2)
entry_username.insert(0, "mail@example.com")
label_password.grid(row=3, column=0)
entry_password.grid(row=3, column=1)
button_generate.grid(row=3, column=2)
button_add.grid(row=4, column=1, columnspan=2, pady=10)

window.mainloop()