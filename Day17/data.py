import requests

question_data = requests.get('https://opentdb.com/api.php?amount=50&type=boolean').json().get('results')
