from flask import Flask, request, jsonify, render_template
from bot import responder_mensagem
import os

app = Flask(__name__)

# Interface web
@app.route('/')
def home():
    return render_template("index.html")

# API do chat
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    mensagem = data.get("mensagem")

    resposta = responder_mensagem("cliente", mensagem)

    return jsonify({"resposta": resposta})

# Rodar no Railway
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)