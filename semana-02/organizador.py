entrada = input("Digite varios nomes separados por virgula: ").strip()

if entrada == "":
    print("Nenhum nome foi informado.")
else:
    nomes = [nome.strip() for nome in entrada.split(",") if nome.strip()]
    nomes_ordenados = sorted(nomes, key=str.lower)

    print("Nomes em ordem alfabetica:")
    for nome in nomes_ordenados:
        print("-", nome)