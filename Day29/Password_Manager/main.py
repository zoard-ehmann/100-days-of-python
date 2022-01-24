from tkinter import *

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

# Labels
label_website = Label(text="Website:", width=15, anchor="e")
label_username = Label(text="Email / Username:", width=15, anchor="e")
label_password = Label(text="Password:", width=15, anchor="e")

# Entries
entry_website = Entry(width=54)
entry_username = Entry(width=54)
entry_password = Entry(width=36)

# Buttons
button_generate = Button(text="Generate Password")
button_add = Button(text="Add", width=46)

# Layout
label_website.grid(row=1, column=0)
entry_website.grid(row=1, column=1, columnspan=2)
label_username.grid(row=2, column=0)
entry_username.grid(row=2, column=1, columnspan=2)
label_password.grid(row=3, column=0)
entry_password.grid(row=3, column=1)
button_generate.grid(row=3, column=2)
button_add.grid(row=4, column=1, columnspan=2, pady=10)

window.mainloop()