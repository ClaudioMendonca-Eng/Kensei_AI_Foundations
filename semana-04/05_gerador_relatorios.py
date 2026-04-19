from openai import OpenAI
from dotenv import load_dotenv
import pandas as pd
import os

# Carrega .env
load_dotenv()

# Cria cliente OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("=" * 70)
print("PROJETO 5: GERADOR DE RELATÓRIO COM DADOS + IA")
print("=" * 70)

def gerar_relatorio(csvfile="vendas.csv"):
    """Combina Pandas + API de IA para gerar relatório executivo em Markdown"""
    
    # Carrega dados com Pandas
    try:
        df = pd.read_csv(csvfile)
    except FileNotFoundError:
        print(f"❌ Arquivo '{csvfile}' não encontrado!")
        print("💡 Dica: crie um CSV com dados de vendas/análise")
        return None
    
    print(f"\n📊 Carregados {len(df)} registros de '{csvfile}'")
    
    # Prepara dados para enviar à IA
    resumo_stats = df.describe().to_string()
    
    # Se houver coluna numérica, pega top 5
    top5 = ""
    if len(df) > 0:
        # Tenta encontrar coluna numérica
        colunas_numericas = df.select_dtypes(include=['number']).columns
        if len(colunas_numericas) > 0:
            col_valor = colunas_numericas[0]
            top5 = df.nlargest(5, col_valor).to_string()
    
    # Cria prompt para gerar relatório profissional
    prompt = f"""Baseado nos seguintes dados de vendas/análise:

ESTATÍSTICAS GERAIS:
{resumo_stats}

TOP 5 RESULTADOS:
{top5}

Gere um relatório executivo em Markdown com:
1. Título e resumo executivo (2-3 frases)
2. Métricas principais (use dados acima)
3. Insights e tendências
4. Recomendações acionáveis
5. Conclusão

Use linguagem profissional e direta. Formato Markdown completo."""
    
    print("\n⏳ Gerando relatório com IA...")
    
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    
    relatorio = resp.choices[0].message.content
    
    return relatorio

# Gera relatório
relatorio = gerar_relatorio()

if relatorio:
    print("\n" + "=" * 70)
    print("📋 RELATÓRIO GERADO:")
    print("=" * 70)
    print(relatorio)
    
    # Salva em arquivo
    with open("relatorio_gerado.md", "w", encoding="utf-8") as f:
        f.write("# Relatório Executivo\n\n")
        f.write("*Gerado automaticamente com Pandas + OpenAI API*\n\n")
        f.write(relatorio)
    
    print("\n✅ Relatório salvo em 'relatorio_gerado.md'")
    print("📌 Abra no VS Code para visualizar melhor!")
