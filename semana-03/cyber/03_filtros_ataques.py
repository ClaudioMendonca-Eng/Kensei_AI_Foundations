import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
arquivo = BASE_DIR / "data" / "cybersecurity_attacks.csv"

df = pd.read_csv(arquivo)
df["Timestamp"] = pd.to_datetime(df["Timestamp"])
df["Alerts/Warnings"] = df["Alerts/Warnings"].fillna("Nenhum")
df["Malware Indicators"] = df["Malware Indicators"].fillna("Nenhum")

# --- Filtro 1: apenas ataques com severidade High ---
alta_severidade = df[df["Severity Level"] == "High"]
print("=== ATAQUES ALTA SEVERIDADE ===")
print(f"Total: {len(alta_severidade)}")
print(alta_severidade[["Timestamp", "Attack Type", "Source IP Address", "Action Taken"]].head(10))

# --- Filtro 2: apenas DDoS bloqueados ---
ddos_bloqueados = df[(df["Attack Type"] == "DDoS") & (df["Action Taken"] == "Blocked")]
print("\n=== DDOS BLOQUEADOS ===")
print(f"Total: {len(ddos_bloqueados)}")

# --- Filtro 3: ataques com IoC detectado ---
ioc = df[df["Malware Indicators"] == "IoC Detected"]
print("\n=== ATAQUES COM IOC DETECTADO ===")
print(f"Total: {len(ioc)}")

# --- Agrupamento: contagem por tipo de ataque ---
por_tipo = df.groupby("Attack Type").size().sort_values(ascending=False)
print("\n=== ATAQUES POR TIPO ===")
print(por_tipo)

# --- Agrupamento: contagem por acao tomada e severidade ---
por_acao = df.groupby(["Action Taken", "Severity Level"]).size().unstack(fill_value=0)
print("\n=== ACOES TOMADAS x SEVERIDADE ===")
print(por_acao)

# --- Agrupamento: media de Anomaly Score por tipo de ataque ---
media_anomalia = df.groupby("Attack Type")["Anomaly Scores"].mean().sort_values(ascending=False)
print("\n=== MEDIA DE ANOMALY SCORE POR TIPO ===")
print(media_anomalia.round(2))
