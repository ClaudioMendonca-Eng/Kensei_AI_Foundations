import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
arquivo = BASE_DIR / "data" / "cybersecurity_attacks.csv"

df = pd.read_csv(arquivo)

print("=== ANTES DA LIMPEZA ===")
print(f"Linhas: {len(df)}")
print(f"Duplicados: {df.duplicated().sum()}")
print(f"Nulos por coluna:\n{df.isnull().sum()}")

# Remove duplicados
df = df.drop_duplicates()
print(f"\nApos remover duplicados: {len(df)} linhas")

# Converte Timestamp para datetime
df["Timestamp"] = pd.to_datetime(df["Timestamp"])
print(f"\nTipo de Timestamp apos conversao: {df['Timestamp'].dtype}")

# Preenche campos nulos com valor padrao
df["Alerts/Warnings"] = df["Alerts/Warnings"].fillna("Nenhum")
df["Proxy Information"] = df["Proxy Information"].fillna("Sem proxy")
df["Malware Indicators"] = df["Malware Indicators"].fillna("Nenhum")
df["IDS/IPS Alerts"] = df["IDS/IPS Alerts"].fillna("Nenhum")
df["Firewall Logs"] = df["Firewall Logs"].fillna("Nenhum")

# Normaliza coluna de severidade para maiusculas padrao
df["Severity Level"] = df["Severity Level"].str.capitalize()

print("\n=== APOS LIMPEZA ===")
print(f"Nulos restantes:\n{df.isnull().sum()}")
print(f"\nSeveridade normalizada:\n{df['Severity Level'].value_counts()}")
print(f"\nDataset limpo: {df.shape[0]} linhas, {df.shape[1]} colunas")
