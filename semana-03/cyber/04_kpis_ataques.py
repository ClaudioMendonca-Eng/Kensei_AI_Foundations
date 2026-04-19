import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
arquivo = BASE_DIR / "data" / "cybersecurity_attacks.csv"

df = pd.read_csv(arquivo)
df["Timestamp"] = pd.to_datetime(df["Timestamp"])
df["Malware Indicators"] = df["Malware Indicators"].fillna("Nenhum")

print("=== KPIs DE SEGURANCA ===\n")

# KPI 1: Total de ataques
total = len(df)
print(f"Total de eventos registrados : {total}")

# KPI 2: Taxa de bloqueio
bloqueados = len(df[df["Action Taken"] == "Blocked"])
taxa_bloqueio = bloqueados / total * 100
print(f"Ataques bloqueados           : {bloqueados} ({taxa_bloqueio:.1f}%)")

# KPI 3: Ataques critical/high
alta_sev = len(df[df["Severity Level"] == "High"])
print(f"Ataques alta severidade (High): {alta_sev}")

# KPI 4: Eventos com IoC detectado
ioc_count = len(df[df["Malware Indicators"] == "IoC Detected"])
taxa_ioc = ioc_count / total * 100
print(f"Eventos com IoC detectado    : {ioc_count} ({taxa_ioc:.1f}%)")

# KPI 5: Anomaly Score medio por protocolo
print("\n=== ANOMALY SCORE MEDIO POR PROTOCOLO ===")
score_protocolo = df.groupby("Protocol")["Anomaly Scores"].mean().sort_values(ascending=False)
print(score_protocolo.round(2))

# KPI 6: Tipo de ataque mais comum
tipo_mais_comum = df["Attack Type"].value_counts().idxmax()
print(f"\nTipo de ataque mais frequente: {tipo_mais_comum}")

# KPI 7: Segmento de rede mais atacado
segmento_top = df["Network Segment"].value_counts().idxmax()
print(f"Segmento mais atacado        : {segmento_top}")

# KPI 8: Distribuicao de ataques por ano
df["Ano"] = df["Timestamp"].dt.year
print("\n=== ATAQUES POR ANO ===")
print(df["Ano"].value_counts().sort_index())

# KPI 9: Protocolo mais usado em ataques bloqueados
bloq_df = df[df["Action Taken"] == "Blocked"]
print("\n=== PROTOCOLO EM ATAQUES BLOQUEADOS ===")
print(bloq_df["Protocol"].value_counts())
