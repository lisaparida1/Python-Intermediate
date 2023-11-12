from tkinter import *
import pandas
import random


choice = {}
data_dict = {}
BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")


def next_word():
    global choice, flip_timer
    # Cancels the 'after' timer running
    window.after_cancel(flip_timer)
    choice = random.choice(data_dict)
    word_french = choice["French"]
    canvas.itemconfig(canvas_image, image=french_card)
    canvas.itemconfig(title_lang, text="French", fill="black")
    canvas.itemconfig(word_lang, text=word_french, fill="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    global choice
    word_english = choice["English"]
    canvas.itemconfig(canvas_image, image=english_card)
    canvas.itemconfig(title_lang, text="English", fill="white")
    canvas.itemconfig(word_lang, text=word_english, fill="white")


def right_button():
    data_dict.remove(choice)
    data1 = pandas.DataFrame(data_dict)
    data1.to_csv("data/words_to_learn.csv", index=False)
    next_word()


window = Tk()
window.title("Learn With Fun 😃")
frame = Frame(master=window, width=750, height=540, background=BACKGROUND_COLOR)
frame.pack()
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=600, height=400, highlightthickness=0, background=BACKGROUND_COLOR)
french_card = PhotoImage(file="images/card_front.png")
english_card = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(300, 200, image=french_card)
title_lang = canvas.create_text(300, 100, text="", font=("Arial", 30, "italic"))
word_lang = canvas.create_text(300, 210, text="", font=("Arial", 25, "bold"))
canvas.place(x=88, y=35)


img_right = PhotoImage(file="images/right.png")
btn_right = Button(image=img_right, highlightthickness=0, command=right_button)
btn_right.place(x=500, y=440)

img_wrong = PhotoImage(file="images/wrong.png")
btn_wrong = Button(image=img_wrong, highlightthickness=0, command=next_word)
btn_wrong.place(x=200, y=440)

next_word()

window.mainloop()