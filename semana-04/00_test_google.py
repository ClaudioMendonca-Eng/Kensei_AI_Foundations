"""
TESTE: Google Gemini API
Testa conexão com a API gratuita do Google (Gemini)
"""

import os
from dotenv import load_dotenv

load_dotenv()

print("=" * 70)
print("🧪 TESTE: Google Gemini API")
print("=" * 70)

google_key = os.getenv("GOOGLE_API_KEY")

if not google_key:
    print("\n❌ GOOGLE_API_KEY não encontrada em .env")
    print("\n📝 Para usar Google Gemini:")
    print("   1. Acesse: https://aistudio.google.com/apikey")
    print("   2. Clique 'Create API Key'")
    print("   3. Copie a chave")
    print("   4. Adicione em .env: GOOGLE_API_KEY=sua-chave")
    exit(1)

print("\n✅ GOOGLE_API_KEY carregada!")
print(f"   Chave: {google_key[:20]}...***")

# Testa importação
try:
    import google.generativeai as genai
    print("✅ google-generativeai importado")
except ImportError:
    print("❌ google-generativeai não instalado")
    print("   Execute: pip install google-generativeai")
    exit(1)

# Configura API
genai.configure(api_key=google_key)

print("\n⏳ Testando conexão com Gemini...")

try:
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content("O que é uma API em uma frase?")
    
    print("\n✅ CONEXÃO FUNCIONANDO!")
    print("\n🤖 Resposta do Gemini:")
    print(f"   {response.text}")
    
except Exception as e:
    erro = str(e)
    print(f"\n❌ Erro: {erro}")
    if "429" in erro or "quota" in erro.lower() or "rate" in erro.lower():
        print("   Causa provável: limite de cota/rate limit no projeto Google AI Studio.")
        print("   Confira uso e limites em: https://ai.google.dev/gemini-api/docs/rate-limits")
    else:
        print("   Verifique se a chave está correta e se a Gemini API está habilitada.")
    exit(1)

print("\n" + "=" * 70)
print("✨ Google Gemini API testada com sucesso!")
print("=" * 70)
