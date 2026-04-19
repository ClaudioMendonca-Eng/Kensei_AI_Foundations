import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
arquivo = BASE_DIR / "data" / "cybersecurity_attacks.csv"

df = pd.read_csv(arquivo)

print("=== PRIMEIRAS LINHAS ===")
print(df.head())

print("\n=== SHAPE (linhas x colunas) ===")
print(df.shape)

print("\n=== INFO (tipos e nulos) ===")
print(df.info())

print("\n=== ESTATISTICAS NUMERICAS ===")
print(df.describe())

print("\n=== COLUNAS ===")
print(df.columns.tolist())

print("\n=== VALORES NULOS POR COLUNA ===")
print(df.isnull().sum())

print("\n=== TIPOS DE ATAQUE ===")
print(df["Attack Type"].value_counts())

print("\n=== SEVERITY LEVELS ===")
print(df["Severity Level"].value_counts())
