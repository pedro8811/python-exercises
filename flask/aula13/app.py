from flask import Flask, render_template, request, send_file, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

if not os.path.exists("instance"):
    os.makedirs("instance")

instance_path = os.path.abspath("instance")

app = Flask(__name__, template_folder="templates")
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{instance_path}/estudantes.db"
db = SQLAlchemy(app)


class Estudante(db.Model):
    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150))
    idade = db.Column(db.Integer)

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


@app.route("/")
def index():
    db.create_all()
    estudantes = Estudante.query.all()
    return render_template("index.html", estudantes=estudantes)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        estudante = Estudante(request.form["nome"], request.form["idade"])
        db.session.add(estudante)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("add.html")


@app.route("/delete/<int:id>")
def delete(id):
    estudante = Estudante.query.get(id)
    db.session.delete(estudante)
    db.session.commit()
    return redirect(url_for("index"))

@app.route('/edit/<int:id>', methods=["GET", "POST"])
def edit(id):
    estudante = Estudante.query.get(id)
    if request.method == 'POST':
        estudante.nome = request.form['nome']
        estudante.idade = request.form['idade']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', estudante=estudante)


if __name__ == "__main__":
    app.run(debug=True)
