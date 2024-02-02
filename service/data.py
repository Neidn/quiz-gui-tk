import requests

from .config import *
from .question_model import Question

params = {
    "amount": QUESTION_AMOUNT,
    "category": QUESTION_CATEGORY,
    "type": QUESTION_TYPE
}


def get_data():
    response = requests.get(
        QUESTION_API_DEFAULT_URL,
        params=params,
    )

    # If the response was successful, no Exception will be raised
    response.raise_for_status()

    # parse the response
    response = response.json()

    return response["results"]


def convert_data():
    data = get_data()
    new_data = []
    for question in data:
        new_question = Question(
            q_text=question["question"],
            q_answer=question["correct_answer"],
        )
        new_data.append(new_question)

    return new_data


question_data = convert_data()
