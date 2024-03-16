from flask import Flask
import requests
import random

app = Flask(__name__)

def get_random_quote():
    response = requests.get("https://type.fit/api/quotes")
    data = response.json()
    random_quote = random.choice(data)['text']
    return random_quote

@app.route('/')
def home():
    random_quote = get_random_quote()
    return f"<h1>{random_quote}</h1>"

if __name__ == '__main__':
    app.run(debug=True)
