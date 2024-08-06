from flask import Flask
import os
from models.estudante import db
from controllers.estudante import app as estudante_controller
from controllers.disciplina import app as disciplina_controller


if not os.path.exists("instance"):
    os.makedirs("instance")

instance_path = os.path.abspath("instance")

app = Flask(__name__, template_folder="templates")
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{instance_path}/estudantes.db"

app.register_blueprint(estudante_controller, url_prefix="/estudante/")
app.register_blueprint(disciplina_controller, url_prefix="/disciplina/")

db.init_app(app=app)
with app.test_request_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
