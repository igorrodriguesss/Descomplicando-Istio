import requests
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    try:
        r = requests.get("http://backend:5000/")
        return f"Frontend recebeu: {r.text}"
    except Exception as e:
        return f"Erro ao acessar o backend: {str(e)}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
