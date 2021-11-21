from flask import Flask, jsonify
import requests
import random

app = Flask(__name__)


@app.route('/words')
def randomWords():
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = requests.get(word_site)
    WORDS = response.content.splitlines()
    word = random.choice(WORDS)
    stringWord = word.decode("utf-8")
    if len(stringWord) < 4:
        randomWords()

    return jsonify({'Word': stringWord})


if __name__ == '__main__':
    app.run(debug=True)
