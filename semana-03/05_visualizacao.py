import pandas as pd
from pathlib import Path
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


BASE_DIR = Path(__file__).resolve().parent
arquivo = BASE_DIR / "data" / "vendas.csv"
out_dir = BASE_DIR / "graficos"
out_dir.mkdir(exist_ok=True)

df = pd.read_csv(arquivo)

df["desconto"] = df["desconto"].fillna(0)
df["valor_total"] = (df["quantidade"] * df["preco_unitario"]) * (1 - df["desconto"])

concluidas = df[df["status"] == "concluida"].copy()

fat_categoria = concluidas.groupby("categoria")["valor_total"].sum().sort_values(ascending=False)
pedidos_cidade = concluidas.groupby("cidade")["id"].count().sort_values(ascending=False)

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
fat_categoria.plot(kind="bar")
plt.title("Faturamento por categoria")
plt.ylabel("R$")
plt.xticks(rotation=30)
plt.savefig(out_dir / "faturamento_por_categoria.png", dpi=150)

plt.subplot(1, 2, 2)
pedidos_cidade.plot(kind="bar", color="orange")
plt.title("Pedidos por cidade")
plt.ylabel("Quantidade")
plt.xticks(rotation=30)
plt.savefig(out_dir / "pedidos_por_cidade.png", dpi=150)

plt.tight_layout()
plt.savefig(out_dir / "dashboard_semana03.png", dpi=150)
print(f"Graficos salvos em: {out_dir}")
