from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path
import os

# Carrega .env
load_dotenv()

# Cria cliente OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("=" * 60)
print("PROJETO 4: TRADUTOR INTELIGENTE")
print("=" * 60)

# Glossário de termos técnicos que NÃO devem ser traduzidos
GLOSSARIO = ["phishing", "malware", "ransomware", "exploit", "payload", "firewall", "VPN"]

def traduzir(texto, idioma_destino="português brasileiro"):
    """Traduz texto detectando idioma original"""
    
    glossario_str = ", ".join(GLOSSARIO)
    
    prompt = f"""Traduza o seguinte texto para {idioma_destino}.

IMPORTANTE: NÃO traduza estes termos técnicos (deixe como estão): {glossario_str}

Texto a traduzir:
"{texto}"

Retorne apenas:
1. A tradução completa
2. Uma linha em branco
3. Idioma detectado"""
    
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    
    return resp.choices[0].message.content

# Exemplo 1: Texto pré-definido
texto_ing = """
Phishing is a cybersecurity attack where criminals impersonate legitimate companies 
to trick users into revealing sensitive information. Always verify the sender's email domain 
before clicking links. A strong password and two-factor authentication provide additional protection.
"""

print("\n📝 TEXTO ORIGINAL (Inglês):")
print(texto_ing)

print("\n⏳ Traduzindo...")
resultado = traduzir(texto_ing, "português brasileiro")

print("\n✅ TRADUÇÃO:")
print(resultado)

# Exemplo 2: Arquivo
arquivo_exemplo = "documento.txt"
if Path(arquivo_exemplo).exists():
    with open(arquivo_exemplo, "r", encoding="utf-8") as f:
        conteudo = f.read()
    
    print(f"\n{'=' * 60}")
    print(f"📄 TRADUZINDO ARQUIVO: {arquivo_exemplo}")
    traducao_arquivo = traduzir(conteudo, "português brasileiro")
    
    # Salva tradução com sufixo _pt
    arquivo_saida = arquivo_exemplo.replace(".txt", "_pt.txt")
    with open(arquivo_saida, "w", encoding="utf-8") as f:
        f.write(traducao_arquivo)
    
    print(f"✅ Salvo em: {arquivo_saida}")
else:
    print(f"\n💡 Dica: Crie um arquivo 'documento.txt' para testar tradução de arquivo")

# Teste interativo
print(f"\n{'=' * 60}")
print("TESTE INTERATIVO:")
print("=" * 60)

seu_texto = input("\n📝 Digite um texto para traduzir (ou ENTER para pular): ").strip()

if seu_texto:
    print("\n⏳ Traduzindo...")
    sua_traducao = traduzir(seu_texto, "português brasileiro")
    print("\n✅ TRADUÇÃO:")
    print(sua_traducao)
