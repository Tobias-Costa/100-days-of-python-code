from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
#----------------------STARTING THE PROOGRAM----------------------#
try:
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
#-------------------RUNS IF USER KNOWS THE WORD------------------#
def remove_know_word():
    to_learn.remove(current_card)
    new_data = pd.DataFrame(to_learn)
    new_data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()
#-------------------------PASS THE CARD-------------------------#
def next_card():
    global current_card, flip_timer
    current_card = random.choice(to_learn)
    window.after_cancel(flip_timer)
    card_canvas.itemconfig(card_background, image=card_front_img)
    card_canvas.itemconfig(title_text, text="Francês", fill="black")
    card_canvas.itemconfig(word_text, text=current_card["french"], fill="black")
    flip_timer = window.after(3000, flip_card)
#-------------------------FLIP THE CARD-------------------------#
def flip_card():
    card_canvas.itemconfig(card_background, image=card_back_img)
    card_canvas.itemconfig(title_text, text="Português", fill="white")
    card_canvas.itemconfig(word_text, text=current_card["portuguese"], fill="white")

#-------------------------UI SETUP-------------------------#
window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

#Images
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
check_img = PhotoImage(file="./images/right.png")
cross_img = PhotoImage(file="./images/wrong.png")

#Canvas
card_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_background = card_canvas.create_image(400, 263, image=card_front_img)
card_canvas.grid(column=0, row=0, columnspan=2)

#Text
title_text = card_canvas.create_text(400, 150,font=("Arial", 40, "italic"))
word_text = card_canvas.create_text(400, 263,font=("Arial", 60, "bold"))

#Buttons
cross_button = Button(image=cross_img, highlightthickness=0, command=next_card)
cross_button.grid(column=0, row=1)

check_button = Button(image=check_img, highlightthickness=0, command=remove_know_word)
check_button.grid(column=1, row=1)

next_card()
window.mainloop()