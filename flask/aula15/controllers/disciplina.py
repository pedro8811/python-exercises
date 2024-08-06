from flask import Blueprint, Response, request
from models.estudante import db, Disciplina
import json

app = Blueprint("disciplina", __name__)


@app.route("/")
def index():
    disciplinas = Disciplina.query.all()
    result = [e.to_dict() for e in disciplinas]
    return Response(
        response=json.dumps(result), status=200, content_type="application/json"
    )


@app.route("/view/<int:id>", methods=["GET"])
def view(id):
    disciplina = Disciplina.query.get(id)
    if disciplina:
        return Response(
            response=json.dumps(disciplina.to_dict()),
            status=200,
            content_type="application/json",
        )
    else:
        return Response(
            response=json.dumps(
                {"status": "error", "message": "Disciplina não encontrado"}
            ),
            status=404,
            content_type="application/json",
        )


@app.route("/add", methods=["POST"])
def add():
    try:
        nome = request.form["nome"]
    except KeyError as e:
        return Response(
            response=json.dumps(
                {"status": "error", "message": f"Missing field: {str(e)}"}
            ),
            status=400,
            content_type="application/json",
        )

    disciplina = Disciplina(nome)
    db.session.add(disciplina)
    db.session.commit()
    return Response(
        response=json.dumps({"status": "success", "data": disciplina.to_dict()}),
        status=200,
        content_type="application/json",
    )


@app.route("/delete/<int:id>", methods=["GET", "DELETE"])
def delete(id):
    disciplina = Disciplina.query.get(id)
    db.session.delete(disciplina)
    db.session.commit()
    return Response(
        response=json.dumps({"status": "deleted", "data": disciplina.to_dict()}),
        status=200,
        content_type="application/json",
    )


@app.route("/edit/<int:id>", methods=["PUT", "POST"])
def edit(id):
    disciplina = Disciplina.query.get(id)
    disciplina.nome = request.form["nome"]
    db.session.commit()
    return Response(
        response=json.dumps(disciplina.to_dict()),
        status=200,
        content_type="application/json",
    )
