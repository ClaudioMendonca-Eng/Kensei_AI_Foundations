from api_provider import ask_llm

print("=" * 70)
print("PROJETO 1 V2: PRIMEIRA CONVERSA MULTI-API")
print("=" * 70)

system = "Voce e um especialista em ciberseguranca. Responda de forma curta e clara em portugues do Brasil."
prompt = "Explique phishing em 2 frases e diga uma boa pratica para evitar golpe."

resp = ask_llm(prompt=prompt, system=system)
print(f"\nProvider usado: {resp['provider']}")
print("\nResposta inicial:\n")
print(resp["text"])

print("\n" + "=" * 70)
pergunta = input("Digite sua pergunta (ENTER para sair): ").strip()
if pergunta:
    r2 = ask_llm(prompt=pergunta, system=system)
    print(f"\nProvider usado: {r2['provider']}")
    print("\nResposta:\n")
    print(r2["text"])
