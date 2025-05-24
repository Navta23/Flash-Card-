from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn={}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
    

def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_title,text="French",fill="black")
    canvas.itemconfig(canvas_word,text=current_card["French"],fill="black")
    canvas.itemconfig(canvas_image, image=front_image)
    flip_timer = window.after(3000,func=flip)
    
    
def flip():
    canvas.itemconfig(canvas_image,image =back_image)
    canvas.itemconfig(canvas_title,text="English",fill="white")
    canvas.itemconfig(canvas_word,text=current_card["English"],fill="white")
    
def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False) # no index will appear before row and column
    next_card()
    
window = Tk()
window.title("Flash Card Program")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000,func = flip)

canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
back_image = PhotoImage(file="images/card_back.png")
front_image = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400,263,image=front_image)
canvas_title = canvas.create_text(400,150,text="",font=("Arial",40,"italic"))
canvas_word = canvas.create_text(400,263,text="",font=("Arial",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

right_image = PhotoImage(file = "images/right.png")
button1 = Button(image=right_image,highlightthickness=0,command=is_known )
button1.grid(row=1,column=1)
wrong_image = PhotoImage(file = "images/wrong.png")
button2 = Button(image=wrong_image,highlightthickness=0,command=next_card)
button2.grid(row=1,column=0)

next_card()
window.mainloop()