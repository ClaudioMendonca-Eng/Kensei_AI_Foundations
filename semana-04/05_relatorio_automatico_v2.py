from pathlib import Path
from datetime import datetime
import pandas as pd
from api_provider import ask_llm


def gerar_relatorio_para_csv(csv_path, out_dir):
    df = pd.read_csv(csv_path)
    resumo = df.describe(include="all").fillna("").to_string()
    amostra = df.head(10).to_string(index=False)

    system = "Voce e um analista de negocios. Gere relatorio objetivo em markdown."
    prompt = (
        f"Arquivo: {csv_path.name}\n"
        f"Linhas: {len(df)} | Colunas: {len(df.columns)}\n\n"
        f"Amostra:\n{amostra}\n\n"
        f"Estatisticas:\n{resumo}\n\n"
        "Gere um relatorio com: resumo executivo, insights, riscos e recomendacoes."
    )

    resp = ask_llm(prompt=prompt, system=system, temperature=0.2)

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_file = out_dir / f"relatorio_{csv_path.stem}_{ts}.md"
    out_file.write_text(resp["text"], encoding="utf-8")
    return resp["provider"], out_file


if __name__ == "__main__":
    base = Path(".")
    out_dir = base / "outputs"
    out_dir.mkdir(exist_ok=True)

    csv_files = sorted(base.glob("*.csv"))
    if not csv_files:
        raise SystemExit("Nenhum CSV encontrado na pasta atual.")

    print(f"CSVs encontrados: {len(csv_files)}")
    for csv_file in csv_files:
        provider, out_file = gerar_relatorio_para_csv(csv_file, out_dir)
        print(f"[{provider}] Relatorio gerado: {out_file}")
