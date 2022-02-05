import requests

PARAMS= {
    'amount':"10",
    'type':"boolean"
}

response = requests.get("https://opentdb.com/api.php?",params=PARAMS)
question_data=response.json()['results']
