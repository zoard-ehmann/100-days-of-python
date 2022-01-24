from tkinter import *
from turtle import width


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

logo = PhotoImage(file="Day29\Password_Manager\logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

label_website = Label(text="Website:")
label_website.grid(row=1, column=0)

entry_website = Entry(width=54)
entry_website.grid(row=1, column=1, columnspan=2)

label_username = Label(text="Email / Username:")
label_username.grid(row=2, column=0)

entry_username = Entry(width=54)
entry_username.grid(row=2, column=1, columnspan=2)

label_password = Label(text="Password:")
label_password.grid(row=3, column=0)

entry_password = Entry(width=36)
entry_password.grid(row=3, column=1)

button_generate = Button(text="Generate Password")
button_generate.grid(row=3, column=2)

button_add = Button(text="Add", width=60)
button_add.grid(row=4, column=0, columnspan=3, pady=10)


window.mainloop()