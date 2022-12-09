from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/second_route")
def second_hello():
    return "Second Hello World 1!"


app.run(debug=True)
