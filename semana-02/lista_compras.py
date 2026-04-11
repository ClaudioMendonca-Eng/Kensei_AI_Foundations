lista_compras = []

print("Monte sua lista de compras.")
print("Digite um item por vez. Para encerrar, pressione Enter sem digitar nada.")

while True:
    item = input("Adicionar item: ").strip()

    if item == "":
        break

    lista_compras.append(item)
    print("Item adicionado.")

print()
print("Lista final de compras:")

if lista_compras:
    for indice, item in enumerate(lista_compras, start=1):
        print(f"{indice}. {item}")
else:
    print("Nenhum item foi adicionado.")