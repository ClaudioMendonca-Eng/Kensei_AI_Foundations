from openai import OpenAI
from dotenv import load_dotenv
import os

# Carrega .env
load_dotenv()

# Cria cliente OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Primeira conversa com a API
print("=" * 50)
print("PROJETO 1: PRIMEIRA CONVERSA COM A API")
print("=" * 50)

resp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": "O que é phishing em 2 frases?"
        }
    ]
)

print("\n🤖 IA:", resp.choices[0].message.content)

# Variação: usuário digita a pergunta
print("\n" + "=" * 50)
print("ENTRADA DO USUÁRIO:")
print("=" * 50)

pergunta = input("\n📝 Digite sua pergunta: ")

resp2 = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": pergunta
        }
    ]
)

print("\n🤖 IA:", resp2.choices[0].message.content)
print(f"\n📊 Tokens usados: {resp2.usage.total_tokens}")
