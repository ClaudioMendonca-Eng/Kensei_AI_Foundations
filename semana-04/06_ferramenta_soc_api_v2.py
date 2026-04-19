from pathlib import Path
import pandas as pd
from api_provider import ask_llm


# Ferramenta propria: triagem automatica de incidentes de ciberseguranca usando IA.
def carregar_alertas(caminho_csv):
    df = pd.read_csv(caminho_csv)
    cols = [
        "Timestamp",
        "Attack Type",
        "Severity Level",
        "Action Taken",
        "Anomaly Scores",
        "Source IP Address",
        "Destination IP Address",
    ]
    disponiveis = [c for c in cols if c in df.columns]
    return df[disponiveis].copy()


def gerar_triagem(df):
    top = df.sort_values(by="Anomaly Scores", ascending=False).head(25)
    tabela = top.to_string(index=False)

    system = "Voce e lider SOC. Responda de forma acionavel e priorizada."
    prompt = (
        "Analise os alertas abaixo e produza um plano de resposta a incidentes com:\n"
        "1) Top 5 riscos\n2) Acoes imediatas (0-24h)\n3) Acoes de curto prazo (7 dias)\n"
        "4) Indicadores para monitoramento\n5) Resumo executivo\n\n"
        f"Alertas:\n{tabela}"
    )

    return ask_llm(prompt=prompt, system=system, temperature=0.2)


if __name__ == "__main__":
    default_csv = Path("..") / "semana-03" / "data" / "cybersecurity_attacks.csv"
    csv_path = default_csv if default_csv.exists() else Path("cybersecurity_attacks.csv")

    if not csv_path.exists():
        raise SystemExit("Nao encontrei cybersecurity_attacks.csv. Coloque o arquivo na pasta atual ou mantenha semana-03/data.")

    df_alertas = carregar_alertas(csv_path)
    resultado = gerar_triagem(df_alertas)

    out = Path("outputs")
    out.mkdir(exist_ok=True)
    out_file = out / "plano_triagem_soc_v2.md"
    out_file.write_text(resultado["text"], encoding="utf-8")

    print(f"Provider: {resultado['provider']}")
    print(f"Plano gerado em: {out_file}")
