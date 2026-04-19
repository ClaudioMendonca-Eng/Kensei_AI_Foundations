"""
Projeto 1 MELHORADO: Primeira Conversa com a API
Suporta OpenAI (ChatGPT), Anthropic (Claude) e Google (Gemini)
"""

import os
from dotenv import load_dotenv

load_dotenv()

print("=" * 70)
print("PROJETO 1: PRIMEIRA CONVERSA COM A API")
print("=" * 70)

# Detecta qual API está configurada
openai_key = os.getenv("OPENAI_API_KEY")
anthropic_key = os.getenv("ANTHROPIC_API_KEY")
google_key = os.getenv("GOOGLE_API_KEY")

apis_disponiveis = []
if openai_key:
    apis_disponiveis.append("OpenAI")
if anthropic_key:
    apis_disponiveis.append("Anthropic")
if google_key:
    apis_disponiveis.append("Google Gemini")

if not apis_disponiveis:
    print("\n❌ Nenhuma API key encontrada!")
    print("\n📝 Configure uma das APIs em .env:")
    print("   • OPENAI_API_KEY=sk-...")
    print("   • ANTHROPIC_API_KEY=sk-ant-...")
    print("   • GOOGLE_API_KEY=AIza...")
    exit(1)

print(f"\n✅ APIs disponíveis: {', '.join(apis_disponiveis)}\n")

# Usa OpenAI por padrão
if openai_key:
    print("🔌 Usando: OpenAI (ChatGPT)")
    print("-" * 70)
    
    from openai import OpenAI
    client = OpenAI(api_key=openai_key)
    
    # Pergunta fixa
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": "O que é phishing em 2 frases?"
            }
        ]
    )
    
    print("\n🤖 Resposta:")
    print(resp.choices[0].message.content)
    print(f"\n📊 Tokens: {resp.usage.total_tokens}")

# Testa Google Gemini se disponível
elif google_key:
    print("🔌 Usando: Google Gemini")
    print("-" * 70)
    
    import google.generativeai as genai
    genai.configure(api_key=google_key)
    
    model = genai.GenerativeModel('gemini-pro')
    resp = model.generate_content("O que é phishing em 2 frases?")
    
    print("\n🤖 Resposta:")
    print(resp.text)

# Entrada do usuário
print("\n" + "=" * 70)
print("TESTE COM ENTRADA DO USUÁRIO")
print("=" * 70)

pergunta = input("\n📝 Digite sua pergunta: ")

if not pergunta.strip():
    print("❌ Pergunta vazia!")
    exit(1)

# OpenAI
if openai_key:
    print("\n⏳ Consultando ChatGPT...")
    resp2 = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": pergunta}]
    )
    print("\n🤖 Resposta:")
    print(resp2.choices[0].message.content)
    print(f"\n📊 Tokens: {resp2.usage.total_tokens}")

# Google Gemini
elif google_key:
    print("\n⏳ Consultando Gemini...")
    resp2 = model.generate_content(pergunta)
    print("\n🤖 Resposta:")
    print(resp2.text)

print("\n✅ Teste concluído!")
