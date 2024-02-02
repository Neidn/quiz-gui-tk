from tkinter import *

from .config import *


class QuizUI(Tk):

    def __init__(self):
        super().__init__()

        self.title("Quiz")
        self.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg=LABEL_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some question text",
            fill=THEME_COLOR,
            font=QUESTION_FONT
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file=TRUE_IMAGE_PATH)
        self.true_button = Button(image=true_image, highlightthickness=0)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file=FALSE_IMAGE_PATH)
        self.false_button = Button(image=false_image, highlightthickness=0)
        self.false_button.grid(row=2, column=1)

        self.mainloop()
