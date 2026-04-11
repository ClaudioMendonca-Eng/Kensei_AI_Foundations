def calcular_area(largura, altura):
    return largura * altura


def e_maior(idade):
    return idade >= 18


def apresentar(nome, curso):
    print(f"Ola! Meu nome e {nome} e eu estudo {curso}.")


print("Area do retangulo:", calcular_area(5, 3))
print("Maior de idade?", e_maior(21))
apresentar("Jose", "AI Foundations")