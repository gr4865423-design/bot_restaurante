etapas = {}

def responder_mensagem(numero, mensagem):
    mensagem = mensagem.lower()

    if numero not in etapas:
        etapas[numero] = {"etapa": 1}

    etapa = etapas[numero]["etapa"]

    if etapa == 1:
        etapas[numero]["etapa"] = 2
        return "Olá! Bem-vindo ao restaurante 🍽️\nQual seu nome?"

    elif etapa == 2:
        etapas[numero]["nome"] = mensagem
        etapas[numero]["etapa"] = 3
        return f"Prazer, {mensagem}! Para qual dia deseja a reserva?"

    elif etapa == 3:
        etapas[numero]["dia"] = mensagem
        etapas[numero]["etapa"] = 4
        return "Qual horário?"

    elif etapa == 4:
        etapas[numero]["hora"] = mensagem
        etapas[numero]["etapa"] = 5
        return "Para quantas pessoas?"

    elif etapa == 5:
        etapas[numero]["pessoas"] = mensagem

        # salvar reserva
        with open("reservas.txt", "a") as f:
            f.write(
                f"Nome: {etapas[numero]['nome']}, "
                f"Dia: {etapas[numero]['dia']}, "
                f"Hora: {etapas[numero]['hora']}, "
                f"Pessoas: {mensagem}\n"
            )

        etapas[numero]["etapa"] = 1

        return "✅ Reserva confirmada! Te esperamos 🍽️"

    return "Digite algo válido."