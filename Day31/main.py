import random
from tkinter import *
from tkinter import messagebox

import pandas


BACKGROUND_COLOR = "#B1DDC6"
FONT = "Arial"
SECONDS = 3 * 1000


def load_words():
    try:
        WORD_LIST = pandas.read_csv("Day31/data/words_to_learn.csv")
    except FileNotFoundError:
        WORD_LIST = pandas.read_csv("Day31/data/german_words.csv")
    finally:
        try:
            return WORD_LIST.to_dict(orient="records")
        except UnboundLocalError:
            messagebox.showinfo(title="Finished", message="You've learned all the words! Congratulations!")
            exit()


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
    global current_card
    if len(words_to_learn) > 0:
        current_card = random.choice(words_to_learn)
        flip_card(current_card, 0)
        window.after(SECONDS, flip_card, current_card, 1)
    else:
        messagebox.showinfo(title="Well Done", message="You've learned all the words! Congratulations!")
        window.destroy()


def known():
    words_to_learn.remove(current_card)
    df = pandas.DataFrame(words_to_learn)
    df.to_csv("Day31/data/words_to_learn.csv", index=False)
    next_card()


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

correct_ans = Button(image=checkmark, highlightthickness=0, borderwidth=0, command=known)
correct_ans.grid(row=1, column=1)

current_card = {}
words_to_learn = load_words()
next_card()

window.mainloop()