import os
import shutil


categorias = {
    "imagens": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "documentos": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "videos": [".mp4", ".avi", ".mov", ".mkv"],
    "compactados": [".zip", ".rar", ".7z"],
}


def encontrar_categoria(extensao):
    for categoria, extensoes in categorias.items():
        if extensao in extensoes:
            return categoria
    return "outros"


entrada = input("Digite o caminho da pasta para organizar ou pressione Enter para usar a pasta atual: ").strip()

if entrada:
    pasta = entrada
else:
    pasta = os.getcwd()

if not os.path.isdir(pasta):
    print("Pasta invalida.")
else:
    movidos_por_categoria = {}

    for nome_arquivo in os.listdir(pasta):
        caminho_origem = os.path.join(pasta, nome_arquivo)

        if os.path.isdir(caminho_origem):
            continue

        _, extensao = os.path.splitext(nome_arquivo)
        extensao = extensao.lower()

        categoria = encontrar_categoria(extensao)
        pasta_destino = os.path.join(pasta, categoria)
        os.makedirs(pasta_destino, exist_ok=True)

        caminho_destino = os.path.join(pasta_destino, nome_arquivo)

        if os.path.abspath(caminho_origem) == os.path.abspath(caminho_destino):
            continue

        if os.path.exists(caminho_destino):
            nome_base, extensao_original = os.path.splitext(nome_arquivo)
            contador = 1
            while True:
                novo_nome = f"{nome_base}_{contador}{extensao_original}"
                caminho_destino = os.path.join(pasta_destino, novo_nome)
                if not os.path.exists(caminho_destino):
                    break
                contador += 1

        shutil.move(caminho_origem, caminho_destino)
        movidos_por_categoria[categoria] = movidos_por_categoria.get(categoria, 0) + 1

    print()
    print("Organizacao concluida.")
    if movidos_por_categoria:
        print("Arquivos movidos por categoria:")
        for categoria, quantidade in movidos_por_categoria.items():
            print(f"- {categoria}: {quantidade}")
    else:
        print("Nenhum arquivo foi movido.")
