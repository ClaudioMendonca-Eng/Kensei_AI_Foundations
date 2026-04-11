primeiro_numero = float(input("Digite o primeiro numero: "))
segundo_numero = float(input("Digite o segundo numero: "))
operacao = input("Digite a operacao (+, -, *, /): ")

if operacao == "+":
    resultado = primeiro_numero + segundo_numero
elif operacao == "-":
    resultado = primeiro_numero - segundo_numero
elif operacao == "*":
    resultado = primeiro_numero * segundo_numero
elif operacao == "/":
    if segundo_numero == 0:
        resultado = None
        print("Erro: divisao por zero nao e permitida.")
    else:
        resultado = primeiro_numero / segundo_numero
else:
    resultado = None
    print("Operacao invalida.")

if resultado is not None:
    print("Resultado:", resultado)