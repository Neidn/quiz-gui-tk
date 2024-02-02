from .data import question_data
from .quiz_brain import QuizBrain
from .ui import QuizUI


# data = get_data()
# print(data)

def next_question():
    if quiz.still_has_questions():
        question = quiz.next_question()
        ui.update_question(question)
    else:
        ui.game_over(quiz.question_number)


def check_answer(answer):
    is_right = quiz.check_answer(answer)
    if is_right:
        ui.update_score(quiz.score)

    ui.give_feedback(is_right, next_question)


quiz = QuizBrain(question_data)
ui = QuizUI()
ui.set_true_button_command(lambda: check_answer("True"))
ui.set_false_button_command(lambda: check_answer("False"))

next_question()

ui.mainloop()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
