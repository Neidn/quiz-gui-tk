import requests

from .config import *

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
