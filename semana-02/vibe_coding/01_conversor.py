print("=== Conversor de Temperatura ===")
print("1. Celsius para Fahrenheit")
print("2. Fahrenheit para Celsius")

opcao = input("Escolha uma opcao: ").strip()

if opcao == "1":
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius:.1f}C = {fahrenheit:.1f}F")
elif opcao == "2":
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit:.1f}F = {celsius:.1f}C")
else:
    print("Opcao invalida.")
