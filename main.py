import json

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/sample")
def get_hello():
    return json.dumps({
        "hello": "world"
    })


if __name__ == '__main__':
    app.run(port=8000)
