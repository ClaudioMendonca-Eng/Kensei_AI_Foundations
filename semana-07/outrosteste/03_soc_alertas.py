from datetime import datetime, timedelta

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="SOC Monitor", layout="wide")
st.title("SOC Monitor | Alertas em Tempo Quase Real")


@st.cache_data
def gerar_alertas() -> pd.DataFrame:
    base = datetime.now().replace(minute=0, second=0, microsecond=0)
    dados = []
    prioridades = ["alta", "media", "baixa"]
    tipos = ["phishing", "malware", "bruteforce", "anomalia_auth"]

    for i in range(48):
        dados.append(
            {
                "timestamp": base - timedelta(hours=47 - i),
                "prioridade": prioridades[i % 3],
                "tipo": tipos[i % 4],
                "quantidade": (i % 7) + 1,
            }
        )

    return pd.DataFrame(dados)


df = gerar_alertas()

prioridade = st.multiselect("Filtrar prioridade", sorted(df["prioridade"].unique()), default=sorted(df["prioridade"].unique()))
df_filtrado = df[df["prioridade"].isin(prioridade)]

col1, col2 = st.columns(2)
with col1:
    st.subheader("Volume por hora")
    fig_linha = px.line(df_filtrado, x="timestamp", y="quantidade", color="prioridade")
    st.plotly_chart(fig_linha, use_container_width=True)

with col2:
    st.subheader("Top tipos de alerta")
    top_tipos = df_filtrado.groupby("tipo", as_index=False)["quantidade"].sum().sort_values("quantidade", ascending=False)
    fig_barra = px.bar(top_tipos, x="tipo", y="quantidade", color="tipo")
    st.plotly_chart(fig_barra, use_container_width=True)

st.subheader("Tabela operacional")
st.dataframe(df_filtrado.sort_values("timestamp", ascending=False), use_container_width=True)
