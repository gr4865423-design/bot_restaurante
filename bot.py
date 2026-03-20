usuarios = {}

def responder_mensagem(numero, mensagem):
    mensagem = mensagem.lower().strip()

    # 🔁 Resetar conversa
    if mensagem == "menu":
        usuarios[numero] = {"etapa": "menu"}

    if numero not in usuarios:
        usuarios[numero] = {"etapa": "menu"}

    etapa = usuarios[numero]["etapa"]

    # 📋 MENU INICIAL
    if etapa == "menu":
        usuarios[numero]["etapa"] = "opcao"
        return """🍽️ Bem-vindo ao Restaurante!

Como posso te ajudar?

1️⃣ Fazer reserva
2️⃣ Falar com atendente

Digite o número da opção."""

    # 🔢 ESCOLHA DO MENU
    elif etapa == "opcao":
        if mensagem == "1":
            usuarios[numero]["etapa"] = "nome"
            return "Perfeito! 😊\n\nQual o seu nome?"

        elif mensagem == "2":
            return "Um atendente entrará em contato com você em breve! 📞"

        else:
            return "❌ Opção inválida. Digite 1 ou 2."

    # 🧑 NOME
    elif etapa == "nome":
        usuarios[numero]["nome"] = mensagem.title()
        usuarios[numero]["etapa"] = "data"
        return f"Prazer, {usuarios[numero]['nome']}! 😄\n\nQual a data da reserva? (Ex: 20/03)"

    # 📅 DATA
    elif etapa == "data":
        if "/" not in mensagem:
            return "❌ Informe a data no formato correto (Ex: 20/03)"

        usuarios[numero]["data"] = mensagem
        usuarios[numero]["etapa"] = "hora"
        return "Ótimo! ⏰\n\nQual o horário?"

    # ⏰ HORA
    elif etapa == "hora":
        usuarios[numero]["hora"] = mensagem
        usuarios[numero]["etapa"] = "pessoas"
        return "Perfeito! 👥\n\nPara quantas pessoas?"

    # 👥 PESSOAS
    elif etapa == "pessoas":
        if not mensagem.isdigit():
            return "❌ Informe apenas números."

        usuarios[numero]["pessoas"] = mensagem
        usuarios[numero]["etapa"] = "final"

        # 💾 SALVAR NO ARQUIVO
        with open("reservas.txt", "a", encoding="utf-8") as f:
            f.write(f"""
Nome: {usuarios[numero]['nome']}
Data: {usuarios[numero]['data']}
Hora: {usuarios[numero]['hora']}
Pessoas: {usuarios[numero]['pessoas']}
-------------------------
""")

        return f"""✅ Reserva confirmada!

📛 Nome: {usuarios[numero]['nome']}
📅 Data: {usuarios[numero]['data']}
⏰ Horário: {usuarios[numero]['hora']}
👥 Pessoas: {usuarios[numero]['pessoas']}

Aguardamos você! 🍽️✨

Digite "menu" para voltar ao início."""

    return "Digite 'menu' para começar novamente."