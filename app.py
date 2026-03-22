from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def home():
    return "BOT ONLINE 🚀"

@app.route("/webhook", methods=["POST"])
def webhook():
    msg = request.values.get("Body", "").lower()

    resp = MessagingResponse()

    if "oi" in msg:
        resp.message("Olá! 👋 Bem-vindo ao restaurante.\nDigite:\n1 - Fazer reserva\n2 - Ver cardápio")

    elif msg == "1":
        resp.message("Perfeito! 📅 Qual dia e horário você deseja reservar?")

    elif msg == "2":
        resp.message("Nosso cardápio:\n🍔 Hambúrguer\n🍕 Pizza\n🥗 Salada")

    else:
        resp.message("Desculpe, não entendi 😅 Digite 'oi' para começar.")

    return str(resp)

# 👇 isso aqui é opcional no Railway, mas bom ter
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)