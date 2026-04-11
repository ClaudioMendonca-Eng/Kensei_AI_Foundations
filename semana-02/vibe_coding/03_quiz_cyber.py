import queue
import threading


def ler_com_tempo_limite(texto, tempo_limite):
    respostas = queue.Queue()

    def capturar_resposta():
        resposta = input(texto)
        respostas.put(resposta)

    thread = threading.Thread(target=capturar_resposta, daemon=True)
    thread.start()

    try:
        return respostas.get(timeout=tempo_limite)
    except queue.Empty:
        return None


perguntas = [
    {
        "pergunta": "O que e phishing?",
        "opcoes": ["a) Um antivirus", "b) Um golpe por mensagem ou email", "c) Um firewall"],
        "resposta": "b",
    },
    {
        "pergunta": "Para que serve um firewall?",
        "opcoes": ["a) Filtrar e controlar trafego", "b) Criar senhas", "c) Apagar arquivos"],
        "resposta": "a",
    },
    {
        "pergunta": "O que e uma senha forte?",
        "opcoes": ["a) 123456", "b) nomeesobrenome", "c) Mistura de letras, numeros e simbolos"],
        "resposta": "c",
    },
    {
        "pergunta": "O que significa 2FA?",
        "opcoes": ["a) Dois fatores de autenticacao", "b) Dois firewalls ativos", "c) Dois arquivos anexados"],
        "resposta": "a",
    },
    {
        "pergunta": "Qual destas praticas ajuda a evitar golpes?",
        "opcoes": ["a) Clicar em qualquer link", "b) Verificar remetente e URL", "c) Reutilizar a mesma senha"],
        "resposta": "b",
    },
]

pontos = 0

print("=== Quiz de Cybersecurity ===")
print("Voce tem 10 segundos para cada pergunta.")
print("Passe com 3 ou mais acertos.")
print()

for numero, item in enumerate(perguntas, start=1):
    print(f"Pergunta {numero}: {item['pergunta']}")
    for opcao in item["opcoes"]:
        print(opcao)

    resposta = ler_com_tempo_limite("Sua resposta: ", 10)

    if resposta is None:
        print("Tempo esgotado. Resposta considerada errada.")
    elif resposta.strip().lower() == item["resposta"]:
        print("Correto!")
        pontos += 1
    else:
        print(f"Errado. Resposta correta: {item['resposta']}")

    print()

print(f"Pontuacao final: {pontos} de {len(perguntas)}")

if pontos >= 3:
    print("Resultado: passou!")
else:
    print("Resultado: nao passou.")
