from flask import Flask
from os import environ

app = Flask(__name__)


@app.route("/")
def index():
    return 'Home Page'


@app.route("/hello/<name>")
def person(name):
    html = """
        <h1>
            Hello {}!
        </h1>
        
        <p>
        How are you doing!
        </p>
    """
    return html.format(name.title())


@app.route("/jedi/<fname>/<lname>")
def jedi(fname, lname):
    name = lname[0:3] + fname[0:2]
    return "Your Jedi Name is {}".format(name)


if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['HOST']))