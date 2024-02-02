import requests

from .config import *


def get_data():
    api_url = f"{QUESTION_API_DEFAULT_URL}?amount={QUESTION_AMOUNT}&category={QUESTION_CATEGORY}&type={QUESTION_TYPE}"
    response = requests.get(api_url)

    # If the response was successful, no Exception will be raised
    response.raise_for_status()

    # parse the response
    response = response.json()

    return response["results"]
