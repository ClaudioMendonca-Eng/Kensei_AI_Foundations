import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
arquivo = BASE_DIR / "data" / "vendas.csv"
df = pd.read_csv(arquivo)

# Preenche desconto nulo com zero para facilitar o calculo do total.
df["desconto"] = df["desconto"].fillna(0)

# Garante que quantidade e preco sejam validos para analise.
df = df[(df["quantidade"] > 0) & (df["preco_unitario"] > 0)]

df["valor_bruto"] = df["quantidade"] * df["preco_unitario"]
df["valor_total"] = df["valor_bruto"] * (1 - df["desconto"])

print("=== DADOS LIMPOS ===")
print(df[["id", "produto", "quantidade", "preco_unitario", "desconto", "valor_total"]].head(10))
