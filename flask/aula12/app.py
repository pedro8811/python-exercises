import os
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, send_file

app = Flask(__name__, template_folder="templates")
UPLOAD_FOLDER = os.path.join(os.getcwd(), "upload")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["imagem"]
    savePath = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
    file.save(savePath)
    return "Upload feito com sucesso"


@app.route("/get-file/<filename>")
def getFile(filename):
    file = os.path.join(UPLOAD_FOLDER, filename + ".png")
    return send_file(filename, mimetype="imagem/jpg")


if __name__ == "__main__":
    app.run()
