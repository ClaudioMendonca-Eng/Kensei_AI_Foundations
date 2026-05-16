from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Kensei Week 07 App", page_icon="🚀", layout="wide")


@st.cache_data
def carregar_vendas() -> pd.DataFrame:
    caminhos = [Path("../semana-04/vendas.csv"), Path("../semana-03/data/vendas.csv")]
    for caminho in caminhos:
        if caminho.exists():
            return pd.read_csv(caminho)
    return pd.DataFrame(
        {
            "produto": ["Firewall", "SIEM", "Treinamento"],
            "valor": [12000, 21000, 9000],
            "regiao": ["Sudeste", "Sul", "Nordeste"],
        }
    )


@st.cache_data
def alertas_soc() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "alerta": ["Phishing", "Bruteforce", "Malware", "Anomalia Auth"],
            "prioridade": ["alta", "media", "alta", "baixa"],
            "casos": [17, 32, 11, 24],
        }
    )


st.sidebar.title("Semana 07")
aba = st.sidebar.radio("Navegacao", ["Visao Geral", "Vendas", "SOC", "Deploy"])

if aba == "Visao Geral":
    st.title("Semana 07 | Apps web com Streamlit")
    st.write("App consolidado para demonstrar dados, SOC e preparo para deploy.")
    st.info("Use o menu lateral para navegar entre as secoes.")

if aba == "Vendas":
    st.title("Painel de Vendas")
    df = carregar_vendas()
    st.dataframe(df.head(20), use_container_width=True)

    col_num = df.select_dtypes(include="number").columns.tolist()
    col_cat = [c for c in df.columns if c not in col_num]
    if col_num and col_cat:
        eixo_x = st.selectbox("Agrupar por", col_cat)
        eixo_y = st.selectbox("Metrica", col_num)
        agrupado = df.groupby(eixo_x, as_index=False)[eixo_y].sum()
        fig = px.bar(agrupado, x=eixo_x, y=eixo_y, color=eixo_x, title=f"{eixo_y} por {eixo_x}")
        st.plotly_chart(fig, use_container_width=True)

if aba == "SOC":
    st.title("Painel SOC")
    soc = alertas_soc()
    st.dataframe(soc, use_container_width=True)
    fig = px.pie(soc, names="alerta", values="casos", title="Distribuicao de alertas")
    st.plotly_chart(fig, use_container_width=True)

if aba == "Deploy":
    st.title("Checklist de Deploy")
    st.markdown(
        """
1. Garantir que o app principal esta em `app.py`.
2. Validar dependencias em `requirements.txt`.
3. Testar local com `streamlit run app.py`.
4. Publicar no Streamlit Community Cloud conectando este repositorio.
5. Definir segredos no painel de deploy quando houver chaves/API.
        """
    )
