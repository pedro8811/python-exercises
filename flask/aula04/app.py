from flask import Flask, request

app = Flask(__name__, static_folder="public")
from json import dumps

@app.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        return dumps(request.form)
    return "Ok get"


if __name__ == "__main__":
    app.run()
