from tkinter import *
# from turtledemo.nim import randomrow

# from charset_normalizer.utils import iana_name

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Question" ,fill=THEME_COLOR)
        # Creating screens


        # Creating Buttons
        right_img = PhotoImage(file="images/true.png")
        r_btn = Button(image=right_img, bg=THEME_COLOR, highlightthickness=0)
        r_btn.grid(row=3, column=1)

        false_img = PhotoImage(file='images/false.png')
        false_btn = Button(image=false_img, bg=THEME_COLOR, highlightthickness=0)
        false_btn.grid(row=3 ,column=2)

        self.window.mainloop()

Demo = QuizInterface()
