import random
import string

quantidade = int(input("Digite o tamanho da senha: "))

if quantidade <= 0:
    print("Digite um numero maior que zero.")
else:
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ""

    for _ in range(quantidade):
        senha += random.choice(caracteres)

    print("Senha gerada:", senha)