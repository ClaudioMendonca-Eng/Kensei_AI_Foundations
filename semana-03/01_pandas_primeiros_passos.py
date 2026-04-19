import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
arquivo = BASE_DIR / "data" / "vendas.csv"
df = pd.read_csv(arquivo)

print("=== PRIMEIRAS LINHAS ===")
print(df.head())

print("\n=== INFO ===")
print(df.info())

print("\n=== ESTATISTICAS ===")
print(df.describe(include="all"))
