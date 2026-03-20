print("BOT INICIANDO...")

from flask import Flask, request, jsonify, render_template
from bot import responder_mensagem

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    mensagem = data.get("mensagem")

    resposta = responder_mensagem("teste", mensagem)

    return jsonify({"resposta": resposta})

# 🔥 IMPORTANTE: não depende do __main__ pro gunicorn