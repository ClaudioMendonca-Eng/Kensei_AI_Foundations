from openai import OpenAI
from dotenv import load_dotenv
import os
import json

# Carrega .env
load_dotenv()

# Cria cliente OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("=" * 60)
print("PROJETO 3: ANALISADOR DE TEXTO COM IA")
print("=" * 60)

def analisar_texto(texto):
    """Analisa texto e retorna resumo, sentimento e palavras-chave em JSON"""
    
    prompt = f"""Analise o seguinte texto:

"{texto}"

Retorne APENAS um JSON válido (sem explicações) com:
- resumo: resumo em 3 frases
- sentimento: positivo, negativo ou neutro
- palavras_chave: lista de 5 palavras mais importantes
- complexidade: fácil, médio ou difícil (basado no texto)

Exemplo de formato:
{{"resumo": "...", "sentimento": "...", "palavras_chave": [...], "complexidade": "..."}}"""
    
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    
    try:
        resultado = json.loads(resp.choices[0].message.content)
        return resultado
    except json.JSONDecodeError:
        return {"erro": "Não foi possível parsear resposta"}

# Teste com exemplo
texto_exemplo = """
Phishing é um tipo de ataque cibernético onde criminosos fingem ser empresas legítimas 
para enganar usuários e roubar informações sensíveis como senhas e dados bancários. 
Os emails de phishing são muito convincentes e pedem ação urgente. A melhor defesa 
é desconfiar de links suspeitos e verificar o domínio do email.
"""

print("\n📝 TEXTO ANALISADO:")
print(f'"{texto_exemplo[:60]}..."')

resultado = analisar_texto(texto_exemplo)

print("\n✅ RESULTADO DA ANÁLISE (JSON):")
print(json.dumps(resultado, ensure_ascii=False, indent=2))

# Salva resultado em arquivo
with open("analise.json", "w", encoding="utf-8") as f:
    json.dump(resultado, f, ensure_ascii=False, indent=2)
print("\n💾 Resultado salvo em 'analise.json'")

# Teste com entrada do usuário
print("\n" + "=" * 60)
print("TESTE COM SEU TEXTO:")
print("=" * 60)

seu_texto = input("\n📝 Cole um texto para análise (ou ENTER para pular): ").strip()

if seu_texto:
    print("\n⏳ Analisando...")
    seu_resultado = analisar_texto(seu_texto)
    print("\n✅ RESULTADO:")
    print(json.dumps(seu_resultado, ensure_ascii=False, indent=2))
