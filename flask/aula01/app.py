from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
  return "Hello Index!"

def teste():
  return "<p>Testando!</p>"
app.add_url_rule("/teste", "teste", teste)

if __name__ == "__main__":
  app.run(debug=True, port="3000")