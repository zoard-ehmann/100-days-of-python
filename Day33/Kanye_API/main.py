import tkinter as tk

import requests


def get_quote():
    response = requests.get("https://api.kanye.rest/")
    response.raise_for_status()
    text_box.itemconfig(quote, text=response.json()["quote"])


window = tk.Tk()
window.config(padx=50, pady=50, bg="white")
window.title("Kanye Says...")

background = tk.PhotoImage(file="Day33/Kanye_API/background.png")
kanye_momoji = tk.PhotoImage(file="Day33/Kanye_API/kanye.png")

text_box = tk.Canvas(width=300, height=414, bg="white", highlightthickness=0)
text_box.create_image(150, 207, image=background)
quote = text_box.create_text(150, 207, fill="white", font=("Arial", 16, "bold"), width=260)
text_box.pack()

button = tk.Button(image=kanye_momoji, highlightthickness=0, bd=0, bg="white", command=get_quote)
button.pack()

get_quote()
window.mainloop()