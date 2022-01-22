from tkinter import *


def button_clicked():
    my_label.config(text=input.get())


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="Just a Label", font=("Arial", 24, "bold"))
my_label.pack()

# Button
button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
input = Entry(width=10)
input.pack()






window.mainloop()