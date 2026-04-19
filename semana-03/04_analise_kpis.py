import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
arquivo = BASE_DIR / "data" / "vendas.csv"
df = pd.read_csv(arquivo)

df["desconto"] = df["desconto"].fillna(0)
df["valor_total"] = (df["quantidade"] * df["preco_unitario"]) * (1 - df["desconto"])

concluidas = df[df["status"] == "concluida"].copy()

faturamento_total = concluidas["valor_total"].sum()
ticket_medio = concluidas["valor_total"].mean()
pedidos_concluidos = concluidas["id"].nunique()

top_categorias = (
    concluidas.groupby("categoria", as_index=False)["valor_total"]
    .sum()
    .sort_values(by="valor_total", ascending=False)
)

print("=== KPIs ===")
print(f"Faturamento total: R$ {faturamento_total:.2f}")
print(f"Ticket medio: R$ {ticket_medio:.2f}")
print(f"Pedidos concluidos: {pedidos_concluidos}")

print("\n=== TOP CATEGORIAS ===")
print(top_categorias)
