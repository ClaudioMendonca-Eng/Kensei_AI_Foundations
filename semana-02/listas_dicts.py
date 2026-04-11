ferramentas_cyber = ["nmap", "wireshark", "burpsuite", "metasploit", "sqlmap"]

pessoa = {
    "nome": "Seu Nome",
    "idade": 25,
    "cidade": "Sua Cidade",
    "email": "seuemail@exemplo.com",
}

print("Ferramentas de cyber:")
for ferramenta in ferramentas_cyber:
    print("-", ferramenta)

print()
print("Primeira ferramenta:", ferramentas_cyber[0])
print("Quantidade de ferramentas:", len(ferramentas_cyber))

ferramentas_cyber.append("aircrack-ng")

print()
print("Lista atualizada:", ferramentas_cyber)

print()
print("Dados pessoais:")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")