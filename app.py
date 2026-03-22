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
        resp.message("Perfeito! 🍽️ Qual dia e horário você deseja reservar?")
    
    elif msg == "2":
        resp.message("Nosso cardápio:\n🍔 Hambúrguer\n🍕 Pizza\n🥗 Salada")
    
    else:
        resp.message("Desculpe, não entendi 🤔\nDigite 1 ou 2")

    return str(resp)