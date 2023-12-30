"Gives you a random fortune"
import random
from flask import Flask, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)

app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_LANGUAGES'] = ['en', 'fr', 'es']
babel.init_app(app, locale_selector=get_locale())


def get_locale():
    return request.accept_languages.best_match(app.config['BABEL_LANGUAGES'])

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

numbers = [random.randint(1, 99) for i in range(0, 5)]

@app.route('/')
def main():
    return render_template("index.html", fortune=gettext(random.choice(get_fortunes())), numbers=numbers)

if __name__ == "__main__":
    app.run(debug=True)
