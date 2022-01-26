import random
from tkinter import *

import pandas


BACKGROUND_COLOR = "#B1DDC6"
FONT = "Arial"
WORD_LIST = pandas.read_csv("Day31/data/german_words.csv")
SECONDS = 3 * 1000

unknown_words = WORD_LIST.to_dict(orient="records")


def flip_card(word, side):
    if side == 0:
        lang = list(word.keys())[0]
        card_side = card_front
        text_color = "black"
        wrong_ans["state"] = "disabled"
        correct_ans["state"] = "disabled"
    else:
        lang = list(word.keys())[1]
        card_side = card_back
        text_color = "white"
        wrong_ans["state"] = "normal"
        correct_ans["state"] = "normal"

    card.itemconfig(card_body, image=card_side)
    card.itemconfig(card_title, text=lang, fill=text_color)
    card.itemconfig(card_word, text=word[lang], fill=text_color)


def next_card():
    random_word = random.choice(unknown_words)
    flip_card(random_word, 0)
    window.after(SECONDS, flip_card, random_word, 1)


window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady= 50, bg=BACKGROUND_COLOR)

card_back = PhotoImage(file="Day31/images/card_back.png")
card_front = PhotoImage(file="Day31/images/card_front.png")
checkmark = PhotoImage(file="Day31/images/right.png")
cross = PhotoImage(file="Day31/images/wrong.png")

card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_body = card.create_image(400, 263, image=card_front)
card_title = card.create_text(400, 150, font=(FONT, 40, "italic"))
card_word = card.create_text(400, 263, font=(FONT, 60, "bold"))
card.grid(row=0, column=0, columnspan=2)

wrong_ans = Button(image=cross, highlightthickness=0, borderwidth=0, command=next_card)
wrong_ans.grid(row=1, column=0)

correct_ans = Button(image=checkmark, highlightthickness=0, borderwidth=0, command=next_card)
correct_ans.grid(row=1, column=1)

next_card()
window.mainloop()