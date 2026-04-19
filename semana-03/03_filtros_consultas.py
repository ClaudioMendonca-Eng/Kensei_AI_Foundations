import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
arquivo = BASE_DIR / "data" / "vendas.csv"
df = pd.read_csv(arquivo)

df["desconto"] = df["desconto"].fillna(0)
df["valor_total"] = (df["quantidade"] * df["preco_unitario"]) * (1 - df["desconto"])

concluidas = df[df["status"] == "concluida"]
sao_paulo = df[df["cidade"] == "Sao Paulo"]
alto_valor = df[df["valor_total"] > 1000]

print("=== VENDAS CONCLUIDAS ===")
print(concluidas[["id", "cliente", "produto", "valor_total", "status"]])

print("\n=== VENDAS EM SAO PAULO ===")
print(sao_paulo[["id", "cliente", "produto", "cidade", "valor_total"]])

print("\n=== VENDAS ACIMA DE 1000 ===")
print(alto_valor[["id", "produto", "cidade", "valor_total"]])
