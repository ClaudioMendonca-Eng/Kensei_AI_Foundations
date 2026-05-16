import streamlit as st

st.set_page_config(page_title="Semana 07 - Hello Streamlit", layout="centered")

st.title("Semana 07 | Hello Streamlit")
st.write("Primeiro app da semana 07 rodando com Streamlit.")

nome = st.text_input("Qual seu nome?", placeholder="Digite seu nome")
area = st.selectbox("Qual area te interessa mais?", ["SOC", "Threat Intel", "Automacao", "Dados"])

if st.button("Gerar mensagem"):
    if nome.strip():
        st.success(f"Ola, {nome}! Bora construir apps de {area} com Streamlit.")
    else:
        st.warning("Digite seu nome para gerar a mensagem.")
