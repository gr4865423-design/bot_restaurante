print("BOT INICIANDO...")

from flask import Flask, request, jsonify, render_template
from bot import responder_mensagem

app = Flask(__name__)

# Página principal (interface)
@app.route('/')
def home():
    return render_template("index.html")

# Rota do chat
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    mensagem = data.get("mensagem")

    resposta = responder_mensagem("teste", mensagem)

    return jsonify({"resposta": resposta})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)