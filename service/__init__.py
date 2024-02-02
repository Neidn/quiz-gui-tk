from .data import question_data
from .quiz_brain import QuizBrain
from .ui import QuizUI

# data = get_data()
# print(data)

quiz = QuizBrain(question_data)
ui = QuizUI()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
