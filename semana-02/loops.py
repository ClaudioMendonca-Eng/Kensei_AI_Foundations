print("Numeros de 1 a 10:")
for numero in range(1, 11):
    print(numero)

print()
nomes = ["Ana", "Bruno", "Carla", "Diego"]
print("Lista de nomes:")
for nome in nomes:
    print("Ola,", nome)

print()
numero_tabuada = int(input("Digite um numero para ver a tabuada: "))
contador = 1

while contador <= 10:
    resultado = numero_tabuada * contador
    print(f"{numero_tabuada} x {contador} = {resultado}")
    contador += 1