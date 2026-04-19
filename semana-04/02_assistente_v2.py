from api_provider import ask_llm

print("=" * 70)
print("PROJETO 2 V2: ASSISTENTE DE TERMINAL COM COMANDOS")
print("Comandos: /sair, /limpar, /stats, /salvar")
print("=" * 70)

system = "Voce e um assistente tecnico de ciberseguranca e IA. Responda de forma pratica."
historico = []
turnos = 0

while True:
    entrada = input("\nVoce: ").strip()
    if not entrada:
        continue

    if entrada == "/sair":
        print("\nEncerrando.")
        break

    if entrada == "/limpar":
        historico.clear()
        turnos = 0
        print("Historico limpo.")
        continue

    if entrada == "/stats":
        print(f"Turnos: {turnos}")
        print(f"Mensagens salvas: {len(historico)}")
        continue

    if entrada == "/salvar":
        with open("chat_historico_v2.txt", "w", encoding="utf-8") as f:
            for role, msg in historico:
                f.write(f"[{role}] {msg}\n\n")
        print("Historico salvo em chat_historico_v2.txt")
        continue

    historico.append(("user", entrada))
    contexto = "\n".join([f"{r}: {m}" for r, m in historico[-12:]])
    prompt = f"Contexto da conversa:\n{contexto}\n\nResponda a ultima pergunta do usuario."

    resposta = ask_llm(prompt=prompt, system=system)
    texto = resposta["text"].strip()
    historico.append(("assistant", texto))
    turnos += 1

    print(f"\nIA ({resposta['provider']}): {texto}")
