import random
import string
from datetime import datetime


def resposta_booleana(texto):
    resposta = input(texto).strip().lower()
    return resposta in ["s", "sim", "y", "yes"]


def gerar_senha(tamanho, usar_maiusculas, usar_numeros, usar_simbolos):
    caracteres = string.ascii_lowercase

    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += "!@#$%&*_-+=?"

    return "".join(random.choices(caracteres, k=tamanho))


print("=== Gerador de Senhas ===")
tamanho = int(input("Digite o tamanho da senha: "))
usar_maiusculas = resposta_booleana("Usar letras maiusculas? (s/n): ")
usar_numeros = resposta_booleana("Usar numeros? (s/n): ")
usar_simbolos = resposta_booleana("Usar simbolos? (s/n): ")

if tamanho <= 0:
    print("Digite um tamanho maior que zero.")
else:
    senhas = []
    for _ in range(5):
        senhas.append(gerar_senha(tamanho, usar_maiusculas, usar_numeros, usar_simbolos))

    print()
    print("Senhas geradas:")
    for indice, senha in enumerate(senhas, start=1):
        print(f"{indice}. {senha}")

    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("senhas.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"Gerado em: {data_hora}\n")
        for senha in senhas:
            arquivo.write(senha + "\n")
        arquivo.write("\n")

    print()
    print("As senhas foram salvas em senhas.txt")
