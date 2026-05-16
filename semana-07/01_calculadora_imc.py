import streamlit as st

st.set_page_config(page_title="Projeto 1 - Calculadora IMC", page_icon="⚕️", layout="centered")

st.title("Projeto 1 | Calculadora IMC")
st.write("Calcule rapidamente o IMC e veja a classificacao.")

peso = st.number_input("Peso (kg)", min_value=0.0, step=0.1)
altura = st.number_input("Altura (m)", min_value=0.0, step=0.01, format="%.2f")

if st.button("Calcular IMC"):
    if peso <= 0 or altura <= 0:
        st.error("Informe peso e altura validos.")
    else:
        imc = peso / (altura ** 2)
        if imc < 18.5:
            classe = "Abaixo do peso"
        elif imc < 25:
            classe = "Peso normal"
        elif imc < 30:
            classe = "Sobrepeso"
        else:
            classe = "Obesidade"

        st.metric("IMC", f"{imc:.2f}")
        st.info(f"Classificacao: {classe}")
