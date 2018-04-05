from flask import Flask
from os import environ

app = Flask(__name__)


@app.route("/")
def index():
    return 'Home Page'


if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['HOST']))