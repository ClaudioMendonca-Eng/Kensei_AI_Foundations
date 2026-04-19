from pathlib import Path
from api_provider import ask_llm

GLOSSARIO_PADRAO = [
    "phishing",
    "malware",
    "ransomware",
    "exploit",
    "payload",
    "firewall",
    "vpn",
]


def traduzir(texto, idioma_destino="portugues brasileiro", glossario=None):
    glossario = glossario or GLOSSARIO_PADRAO
    termos = ", ".join(glossario)

    system = "Voce e tradutor tecnico. Preserve termos do glossario sem traduzir."
    prompt = (
        f"Traduza para {idioma_destino}.\n"
        f"Nao traduza estes termos: {termos}.\n\n"
        f"Texto:\n{texto}"
    )

    return ask_llm(prompt=prompt, system=system, temperature=0.2)


if __name__ == "__main__":
    entrada = input("Digite um texto para traduzir (ou caminho de arquivo .txt): ").strip()
    if not entrada:
        raise SystemExit("Entrada vazia")

    if entrada.lower().endswith(".txt") and Path(entrada).exists():
        conteudo = Path(entrada).read_text(encoding="utf-8")
        resp = traduzir(conteudo)
        saida = Path(entrada).with_name(Path(entrada).stem + "_traduzido_v2.txt")
        saida.write_text(resp["text"], encoding="utf-8")
        print(f"Provider: {resp['provider']}")
        print(f"Arquivo salvo: {saida}")
    else:
        resp = traduzir(entrada)
        print(f"Provider: {resp['provider']}")
        print("\nTradução:\n")
        print(resp["text"])
