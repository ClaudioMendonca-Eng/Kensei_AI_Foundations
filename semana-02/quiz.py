perguntas = [
    {
        "pergunta": "Qual linguagem estamos aprendendo nesta aula?",
        "resposta": "python",
    },
    {
        "pergunta": "Qual comando usamos para mostrar algo na tela em Python?",
        "resposta": "print",
    },
    {
        "pergunta": "Qual estrutura usamos para decidir entre caminhos no codigo?",
        "resposta": "if",
    },
    {
        "pergunta": "Qual estrutura usamos para repetir varias vezes?",
        "resposta": "for",
    },
    {
        "pergunta": "Como se chama um bloco reutilizavel de codigo em Python?",
        "resposta": "funcao",
    },
]

acertos = 0

print("Quiz rapido de Python")
print("Responda com palavras simples.")
print()

for numero, item in enumerate(perguntas, start=1):
    resposta_usuario = input(f"{numero}. {item['pergunta']} ").strip().lower()

    if resposta_usuario == item["resposta"]:
        print("Correto!")
        acertos += 1
    else:
        print("Resposta esperada:", item["resposta"])

    print()

print(f"Voce acertou {acertos} de {len(perguntas)} perguntas.")