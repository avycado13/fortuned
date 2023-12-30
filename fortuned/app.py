"Gives you a random fortune"
import random
from flask import Flask, render_template



app = Flask(__name__)


def get_fortunes(file='fortunes.txt'):
    "Fortune parser"
    # opening the file in read mode
    with open(file, "r", encoding="utf-8") as file:
        # reading the file
        data = file.read()
        # replacing end splitting the text
        # when newline ('\n') is seen.
        fortunes = data.split("\n")
        file.close()
        return fortunes

@app.route('/')
def main():
    "Index"
    return render_template("index.html",fortune=random.choice(get_fortunes()))

if __name__ == "__main__" :
    app.run(debug=True,)
