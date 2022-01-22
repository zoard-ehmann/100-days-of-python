from tkinter import *


def button_clicked():
    my_label.config(text=input.get())


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="Just a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Buttons
button1 = Button(text="Click Me", command=button_clicked)
button1.grid(column=1, row=1)

button2 = Button(text="Another", command=button_clicked)
button2.grid(column=2, row=0)

# Entry
input = Entry(width=10)
input.grid(column=3, row=2)






window.mainloop()