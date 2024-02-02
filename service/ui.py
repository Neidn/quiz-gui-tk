from tkinter import Tk

from .config import *


class QuizUI(Tk):
    def __init__(self):
        super().__init__()

        self.title("Quiz")

        self.mainloop()
