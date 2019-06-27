
import os
from flask import Flask
from meaning import meaning_of_life

app = Flask(__name__)

@app.route("/")
def get_meaning():
    page = '<html><body><h1>'
    page += str(meaning_of_life())
    page += '</h1></body></html>'
    return page

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
