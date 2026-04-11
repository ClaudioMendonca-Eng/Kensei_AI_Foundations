nota = float(input("Digite a nota do aluno (0 a 10): "))

if nota < 0 or nota > 10:
    print("Nota invalida. Digite um valor entre 0 e 10.")
elif nota >= 7:
    print("Aprovado!")
elif nota >= 5:
    print("Recuperacao.")
else:
    print("Reprovado.")