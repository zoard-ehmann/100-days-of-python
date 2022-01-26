from tkinter import *


BACKGROUND_COLOR = "#B1DDC6"
FONT = "Arial"


# --------------------------------------------- CREATE UI --------------------------------------------- #
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady= 50, bg=BACKGROUND_COLOR)

card_back = PhotoImage(file="Day31/images/card_back.png")
card_front = PhotoImage(file="Day31/images/card_front.png")
checkmark = PhotoImage(file="Day31/images/right.png")
cross = PhotoImage(file="Day31/images/wrong.png")

card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card.create_image(400, 263, image=card_front)
card.create_text(400, 150, text="German", font=(FONT, 40, "italic"))
card.create_text(400, 263, text="Ich", font=(FONT, 60, "bold"))
card.grid(row=0, column=0, columnspan=2)

wrong_ans = Button(image=cross, highlightthickness=0, borderwidth=0)
wrong_ans.grid(row=1, column=0)

correct_ans = Button(image=checkmark, highlightthickness=0, borderwidth=0)
correct_ans.grid(row=1, column=1)


window.mainloop()