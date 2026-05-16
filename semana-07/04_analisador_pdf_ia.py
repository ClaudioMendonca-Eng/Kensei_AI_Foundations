import os

import streamlit as st
from dotenv import load_dotenv

load_dotenv()

try:
    from pypdf import PdfReader
except Exception:
    PdfReader = None

try:
    import google.generativeai as genai
except Exception:
    genai = None

st.set_page_config(page_title="Projeto 4 - Analisador de PDF com IA", page_icon="📄", layout="wide")
st.title("Projeto 4 | Analisador de PDF com IA")

uploaded = st.file_uploader("Envie um PDF", type=["pdf"])
api_key = os.getenv("GOOGLE_API_KEY", "")

if uploaded is not None:
    if PdfReader is None:
        st.error("Dependencia pypdf nao instalada. Rode: pip install -r requirements.txt")
        st.stop()

    reader = PdfReader(uploaded)
    pages_text = []

    for page in reader.pages[:10]:
        txt = page.extract_text() or ""
        pages_text.append(txt)

    full_text = "\n\n".join(pages_text).strip()
    st.subheader("Texto extraido (amostra)")
    st.text_area("Conteudo", full_text[:4000] if full_text else "Nenhum texto extraido.", height=250)

    if st.button("Resumir com IA"):
        if not full_text:
            st.warning("Nao foi possivel extrair texto util do PDF.")
        elif not api_key or genai is None:
            st.info("Modo demo: configure GOOGLE_API_KEY para resumo real com IA.")
            st.write("Resumo demo: o documento foi carregado e o texto foi extraido com sucesso.")
        else:
            try:
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel("gemini-2.5-flash")
                prompt_resumo = f"Resuma este documento de forma objetiva para analistas SOC:\n\n{full_text[:12000]}"
                response = model.generate_content(
                    prompt_resumo,
                    generation_config=genai.types.GenerationConfig(
                        temperature=0.2,
                        max_output_tokens=2048,
                    ),
                )
                st.subheader("Resumo")
                st.write(response.text)
            except Exception as e:
                if "429" in str(e) or "quota" in str(e).lower() or "ResourceExhausted" in str(e):
                    st.warning(
                        "⚠️ Quota de Gemini API esgotada. Aguarde alguns minutos. "
                        "[Detalhes](https://ai.google.dev/gemini-api/docs/rate-limits)"
                    )
                else:
                    st.error(f"Erro ao chamar Gemini: {str(e)[:200]}")
