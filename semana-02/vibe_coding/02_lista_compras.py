lista = []

while True:
    print()
    print("--- LISTA DE COMPRAS ---")
    print("1. Adicionar item")
    print("2. Ver lista")
    print("3. Remover item")
    print("4. Sair e salvar")

    opcao = input("Escolha: ").strip()

    if opcao == "1":
        item = input("Digite o item: ").strip()
        if item:
            lista.append(item)
            print("Item adicionado com sucesso.")
        else:
            print("Item vazio nao foi adicionado.")

    elif opcao == "2":
        if not lista:
            print("A lista esta vazia.")
        else:
            print("Itens na lista:")
            for indice, item in enumerate(lista, start=1):
                print(f"{indice}. {item}")

    elif opcao == "3":
        if not lista:
            print("Nao ha itens para remover.")
        else:
            for indice, item in enumerate(lista, start=1):
                print(f"{indice}. {item}")

            posicao = input("Digite o numero do item para remover: ").strip()
            if posicao.isdigit():
                indice = int(posicao) - 1
                if 0 <= indice < len(lista):
                    removido = lista.pop(indice)
                    print(f"Item removido: {removido}")
                else:
                    print("Numero invalido.")
            else:
                print("Digite apenas numeros.")

    elif opcao == "4":
        with open("lista_compras.txt", "w", encoding="utf-8") as arquivo:
            for item in lista:
                arquivo.write(item + "\n")

        print("Lista salva em lista_compras.txt")
        print("Encerrando programa.")
        break

    else:
        print("Opcao invalida.")
