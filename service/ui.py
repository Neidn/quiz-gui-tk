from tkinter import *

from .config import *


def check_answer(current_question, answer):
    return answer.lower() == current_question.answer.lower()


class QuizUI(Tk):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.true_image = PhotoImage(file=TRUE_IMAGE_PATH)
        self.false_image = PhotoImage(file=FALSE_IMAGE_PATH)

        self.title("Quiz")
        self.config(padx=20, pady=20, bg=THEME_COLOR)

        self.__create_score_label()
        self.__create_canvas()
        self.__create_buttons()

    def __create_score_label(self) -> None:
        self.score_label = Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg=LABEL_COLOR)
        self.score_label.grid(row=0, column=1)

    def update_score(self, score: int) -> None:
        self.score = score
        self.score_label.config(text=f"Score: {self.score}")

    def __create_canvas(self) -> None:
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

    def update_question(self, question: str) -> None:
        self.canvas.itemconfig(self.question_text, text=question)

    def __create_buttons(self) -> None:
        self.false_button = Button(image=self.false_image, highlightthickness=0)
        self.false_button.grid(row=2, column=0)

        self.true_button = Button(image=self.true_image, highlightthickness=0)
        self.true_button.grid(row=2, column=1)

    def set_true_button_command(self, command: callable) -> None:
        self.true_button.config(command=command)

    def set_false_button_command(self, command: callable) -> None:
        self.false_button.config(command=command)

    def give_feedback(self, is_right: bool, command: callable) -> None:
        if is_right:
            self.canvas.config(bg=QUESTION_RIGHT_BG_COLOR)
            self.canvas.itemconfig(self.question_text, fill=QUESTION_RIGHT_FONT_COLOR)
        else:
            self.canvas.config(bg=QUESTION_WRONG_BG_COLOR)
            self.canvas.itemconfig(self.question_text, fill=QUESTION_WRONG_FONT_COLOR)

        self.after(1000, self.__clear_feedback, command)

    def __clear_feedback(self, command: callable) -> None:
        self.canvas.config(bg=QUESTION_BG_COLOR)
        self.canvas.itemconfig(self.question_text, fill=FONT_COLOR)
        command()

    def game_over(self, question_number: int) -> None:
        self.canvas.itemconfig(self.question_text, text="You've completed the quiz")
        self.score_label.config(text=f"Your final score was: {self.score}/{question_number}")
        self.true_button.config(command=self.quit)
        self.false_button.config(command=self.quit)
