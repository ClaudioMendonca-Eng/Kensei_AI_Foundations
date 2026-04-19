import json
from api_provider import ask_llm


def analisar_texto(texto):
    system = "Voce e um analista de texto. Responda somente JSON valido."
    prompt = (
        "Analise o texto abaixo e retorne apenas JSON com as chaves: "
        "resumo, sentimento, palavras_chave, complexidade, recomendacao.\n\n"
        f"Texto:\n{texto}"
    )

    resp = ask_llm(prompt=prompt, system=system, temperature=0.1)
    bruto = resp["text"].strip()

    # Tenta parsear JSON puro e fallback removendo markdown
    try:
        data = json.loads(bruto)
    except json.JSONDecodeError:
        clean = bruto.replace("```json", "").replace("```", "").strip()
        data = json.loads(clean)

    return resp["provider"], data


if __name__ == "__main__":
    exemplo = "Phishing explora engenharia social para roubar credenciais. O usuario clica em links falsos e entrega dados."
    provider, resultado = analisar_texto(exemplo)

    print(f"Provider usado: {provider}")
    print(json.dumps(resultado, ensure_ascii=False, indent=2))

    with open("analise_v2.json", "w", encoding="utf-8") as f:
        json.dump(resultado, f, ensure_ascii=False, indent=2)
    print("Arquivo salvo: analise_v2.json")
