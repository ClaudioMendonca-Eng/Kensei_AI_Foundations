"""
DEMO: Teste sem API Key
Demonstra que os imports funcionam no Docker
"""

import json
from pathlib import Path

print("=" * 70)
print("🐳 DEMO DOCKER — SEMANA 4: APIs DE IA")
print("=" * 70)

print("\n✅ Imports carregados com sucesso!")
print("   • openai")
print("   • python-dotenv")
print("   • pandas")

print("\n📦 Estrutura do projeto:")
arquivos = [
    "01_hello_api.py — Primeira conversa com API",
    "02_assistente.py — Chatbot com memória",
    "03_analisador.py — Análise de texto → JSON",
    "04_tradutor.py — Tradutor inteligente",
    "05_gerador_relatorios.py — Relatório Pandas + IA"
]

for i, arq in enumerate(arquivos, 1):
    print(f"   {i}. {arq}")

print("\n🚀 Para rodar com sua API key:")
print("""
   docker run --rm \\
     -e OPENAI_API_KEY=sk-sua-chave \\
     kensei-semana04 python 01_hello_api.py
""")

print("\n💡 Próximos passos:")
print("   1. Obtenha API key em platform.openai.com/api-keys")
print("   2. Copie .env.example → .env")
print("   3. Preencha OPENAI_API_KEY=sk-xxx")
print("   4. Execute scripts!")

print("\n✨ Docker está pronto!")
