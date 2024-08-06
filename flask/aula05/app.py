from flask import Flask, request

app = Flask(__name__, static_folder="public")
import json


@app.route("/", methods=["GET", "POST"])
def index():
    # print(request.method, request.args)
    t1 = request.args.to_dict()
    t2 = dict(request.args)
    return json.dumps([t1, t2])


if __name__ == "__main__":
    app.run()
