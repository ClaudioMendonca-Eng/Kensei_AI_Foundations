import pandas as pd
from pathlib import Path
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


BASE_DIR = Path(__file__).resolve().parent.parent
arquivo = BASE_DIR / "data" / "cybersecurity_attacks.csv"
out_dir = BASE_DIR / "graficos"
out_dir.mkdir(exist_ok=True)

df = pd.read_csv(arquivo)
df["Timestamp"] = pd.to_datetime(df["Timestamp"])
df["Malware Indicators"] = df["Malware Indicators"].fillna("Nenhum")

# --- Grafico 1: Ataques por tipo (barras) ---
por_tipo = df["Attack Type"].value_counts()

plt.figure(figsize=(7, 4))
por_tipo.plot(kind="bar", color=["#e74c3c", "#e67e22", "#3498db"])
plt.title("Quantidade de Ataques por Tipo")
plt.xlabel("Tipo de Ataque")
plt.ylabel("Quantidade")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(out_dir / "cyber_ataques_por_tipo.png", dpi=150)
print("Salvo: cyber_ataques_por_tipo.png")
plt.close()

# --- Grafico 2: Acoes tomadas por severidade (barras agrupadas) ---
por_acao_sev = df.groupby(["Severity Level", "Action Taken"]).size().unstack(fill_value=0)

por_acao_sev.plot(kind="bar", figsize=(8, 5))
plt.title("Acoes Tomadas por Nivel de Severidade")
plt.xlabel("Severidade")
plt.ylabel("Quantidade")
plt.xticks(rotation=0)
plt.legend(title="Acao")
plt.tight_layout()
plt.savefig(out_dir / "cyber_acoes_por_severidade.png", dpi=150)
print("Salvo: cyber_acoes_por_severidade.png")
plt.close()

# --- Grafico 3: Proporcao de tipos de trafego (pizza) ---
trafego = df["Traffic Type"].value_counts()

plt.figure(figsize=(6, 6))
trafego.plot(kind="pie", autopct="%1.1f%%", startangle=140)
plt.title("Proporcao por Tipo de Trafego")
plt.ylabel("")
plt.tight_layout()
plt.savefig(out_dir / "cyber_trafego_pizza.png", dpi=150)
print("Salvo: cyber_trafego_pizza.png")
plt.close()

# --- Dashboard (3 graficos em 1) ---
fig, axes = plt.subplots(1, 3, figsize=(16, 5))
fig.suptitle("Dashboard Ciberseguranca - Semana 3", fontsize=14, fontweight="bold")

por_tipo.plot(ax=axes[0], kind="bar", color=["#e74c3c", "#e67e22", "#3498db"])
axes[0].set_title("Ataques por Tipo")
axes[0].set_xlabel("")
axes[0].tick_params(axis="x", rotation=0)

por_acao_sev.plot(ax=axes[1], kind="bar")
axes[1].set_title("Acoes x Severidade")
axes[1].set_xlabel("")
axes[1].tick_params(axis="x", rotation=0)
axes[1].legend(title="Acao", fontsize=8)

axes[2].pie(trafego, labels=trafego.index, autopct="%1.1f%%", startangle=140)
axes[2].set_title("Tipo de Trafego")

plt.tight_layout()
plt.savefig(out_dir / "cyber_dashboard.png", dpi=150)
print(f"Dashboard salvo: cyber_dashboard.png")
print(f"\nTodos os graficos em: {out_dir}")
plt.close()
