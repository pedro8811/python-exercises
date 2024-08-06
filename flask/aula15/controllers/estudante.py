from flask import Blueprint, Response, request
from models.estudante import db, Estudante
import json

app = Blueprint("estudantes", __name__)


@app.route("/")
def index():
    estudantes = Estudante.query.all()
    result = [e.to_dict() for e in estudantes]
    return Response(
        response=json.dumps(result), status=200, content_type="application/json"
    )


@app.route("/view/<int:id>", methods=["GET"])
def view(id):
    estudante = Estudante.query.get(id)
    if estudante:
        return Response(
            response=json.dumps(estudante.to_dict()),
            status=200,
            content_type="application/json",
        )
    else:
        return Response(
            response=json.dumps(
                {"status": "error", "message": "Estudante não encontrado"}
            ),
            status=404,
            content_type="application/json",
        )


@app.route("/add", methods=["POST"])
def add():
    try:
        nome = request.form["nome"]
        idade = request.form["idade"]
    except KeyError as e:
        return Response(
            response=json.dumps(
                {"status": "error", "message": f"Missing field: {str(e)}"}
            ),
            status=400,
            content_type="application/json",
        )

    estudante = Estudante(nome, idade)
    db.session.add(estudante)
    db.session.commit()
    return Response(
        response=json.dumps({"status": "success", "data": estudante.to_dict()}),
        status=200,
        content_type="application/json",
    )


@app.route("/delete/<int:id>", methods=["GET", "DELETE"])
def delete(id):
    estudante = Estudante.query.get(id)
    db.session.delete(estudante)
    db.session.commit()
    return Response(
        response=json.dumps({"status": "deleted", "data": estudante.to_dict()}),
        status=200,
        content_type="application/json",
    )


@app.route("/edit/<int:id>", methods=["PUT", "POST"])
def edit(id):
    estudante = Estudante.query.get(id)
    estudante.nome = request.form["nome"]
    estudante.idade = request.form["idade"]
    db.session.commit()
    return Response(
        response=json.dumps(estudante.to_dict()),
        status=200,
        content_type="application/json",
    )
