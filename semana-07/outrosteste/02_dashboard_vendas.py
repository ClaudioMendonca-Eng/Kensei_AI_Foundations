from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Dashboard de Vendas", layout="wide")
st.title("Dashboard de Vendas | Semana 07")


@st.cache_data
def carregar_vendas() -> pd.DataFrame:
    candidatos = [
        Path("../semana-04/vendas.csv"),
        Path("../semana-03/data/vendas.csv"),
    ]
    for caminho in candidatos:
        if caminho.exists():
            return pd.read_csv(caminho)
    return pd.DataFrame(
        {
            "produto": ["Firewall", "EDR", "Treinamento"],
            "valor": [12000, 18000, 8000],
            "regiao": ["Sudeste", "Sul", "Nordeste"],
        }
    )


df = carregar_vendas()

st.subheader("Preview dos dados")
st.dataframe(df.head(10), use_container_width=True)

colunas_numericas = df.select_dtypes(include="number").columns.tolist()
colunas_categoricas = [c for c in df.columns if c not in colunas_numericas]

if colunas_numericas and colunas_categoricas:
    eixo_x = st.selectbox("Eixo X", colunas_categoricas, index=0)
    eixo_y = st.selectbox("Eixo Y", colunas_numericas, index=0)

    fig = px.bar(df, x=eixo_x, y=eixo_y, color=eixo_x, title=f"{eixo_y} por {eixo_x}")
    st.plotly_chart(fig, use_container_width=True)

if colunas_numericas:
    metrica = colunas_numericas[0]
    st.metric("Total", f"{df[metrica].sum():,.2f}")
