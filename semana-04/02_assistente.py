from openai import OpenAI
from dotenv import load_dotenv
import os

# Carrega .env
load_dotenv()

# Cria cliente OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("=" * 60)
print("PROJETO 2: ASSISTENTE DE TERMINAL COM MEMÓRIA")
print("=" * 60)
print("💬 Digite suas perguntas. Digite 'sair' para encerrar.")
print("=" * 60)

# Histórico com system prompt (personalidade da IA)
historico = [
    {
        "role": "system",
        "content": "Você é um assistente especializado em cibersegurança da Kensei. Responda de forma técnica mas acessível. Use português brasileiro."
    }
]

tokens_totais = 0

while True:
    pergunta = input("\n👤 Você: ").strip()
    
    if pergunta.lower() == "sair":
        print("\n✅ Encerrando conversa...")
        print(f"📊 Total de tokens gastos: {tokens_totais}")
        break
    
    if not pergunta:
        continue
    
    # Adiciona pergunta ao histórico
    historico.append({
        "role": "user",
        "content": pergunta
    })
    
    # Chama API com histórico completo (mantém memória)
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=historico
    )
    
    resposta = resp.choices[0].message.content
    tokens_totais += resp.usage.total_tokens
    
    # Adiciona resposta ao histórico
    historico.append({
        "role": "assistant",
        "content": resposta
    })
    
    # Exibe com cores (simulado)
    print(f"\n🤖 IA: {resposta}")
    print(f"   [tokens nesta resposta: {resp.usage.total_tokens}]")
