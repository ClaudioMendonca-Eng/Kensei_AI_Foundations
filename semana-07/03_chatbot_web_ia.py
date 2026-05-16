import os
from datetime import datetime
from uuid import uuid4

import streamlit as st
from dotenv import load_dotenv

load_dotenv()

try:
    import google.generativeai as genai
except Exception:
    genai = None

st.set_page_config(page_title="Projeto 3 - Chatbot Web com IA", page_icon="💬", layout="wide")

st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] { background: radial-gradient(circle at 0% 0%, #182233 0%, #0d1117 35%, #0b0f14 100%); }
    [data-testid="stSidebar"] { background: #111827; border-right: 1px solid #243244; }
    .hero-title { font-size: 3rem !important; font-weight: 800 !important; color: #e6edf3 !important; margin-bottom: .2rem; line-height: 1.15 !important; }
    .hero-sub { color: #9fb2c8; margin-bottom: 1rem; }
    .chat-hint { background: #111827; border: 1px solid #243244; border-radius: 12px; padding: .8rem; color: #c7d6e8; }
    .meta-card { background: #0f1724; border: 1px solid #243244; border-radius: 12px; padding: .8rem; color: #dce7f4; }
    </style>
    """,
    unsafe_allow_html=True,
)

api_key = os.getenv("GOOGLE_API_KEY", "")
SUGESTOES = [
    "Quais indicadores sugerem phishing ativo na rede?",
    "Monte um playbook rapido para resposta a ransomware.",
    "Como priorizar alertas SOC com poucos analistas?",
    "Resuma boas praticas de hardening para Windows e Linux.",
]


def make_new_chat(title: str = "Nova conversa") -> dict:
    return {
        "id": str(uuid4()),
        "title": title,
        "created_at": datetime.now().strftime("%d/%m %H:%M"),
        "messages": [
            {"role": "system", "content": "Voce e um assistente SOC focado em ciberseguranca."}
        ],
    }


if "conversations" not in st.session_state:
    st.session_state.conversations = [make_new_chat()]

if "active_chat_id" not in st.session_state:
    st.session_state.active_chat_id = st.session_state.conversations[0]["id"]

if "prompt_from_suggestion" not in st.session_state:
    st.session_state.prompt_from_suggestion = None


def get_active_chat() -> dict:
    for chat in st.session_state.conversations:
        if chat["id"] == st.session_state.active_chat_id:
            return chat
    fallback = st.session_state.conversations[0]
    st.session_state.active_chat_id = fallback["id"]
    return fallback


def is_max_tokens_stop(response) -> bool:
    """Detecta se o modelo parou por limite de tokens."""
    try:
        if response.candidates:
            reason = str(response.candidates[0].finish_reason)
            return "MAX_TOKENS" in reason
    except Exception:
        return False
    return False


with st.sidebar:
    st.markdown("## Conversas")
    if st.button("+ Nova conversa", use_container_width=True):
        novo_chat = make_new_chat()
        st.session_state.conversations.insert(0, novo_chat)
        st.session_state.active_chat_id = novo_chat["id"]
        st.rerun()

    st.markdown("---")
    for chat in st.session_state.conversations:
        label = f"{chat['title']} - {chat['created_at']}"
        if st.button(label, key=f"chat_{chat['id']}", use_container_width=True):
            st.session_state.active_chat_id = chat["id"]
            st.rerun()

    st.markdown("---")
    st.markdown('<div class="meta-card">Modelo: Gemini 2.5 Flash<br>Perfil: Analista SOC</div>', unsafe_allow_html=True)

chat_atual = get_active_chat()

st.markdown('<p class="hero-title">Projeto 3 | Chat IA Moderno para SOC</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="hero-sub">Historico por conversa, sugestoes rapidas e respostas com Gemini.</p>',
    unsafe_allow_html=True,
)

if not api_key:
    st.markdown(
        '<div class="chat-hint">Modo demo ativo: defina GOOGLE_API_KEY no arquivo .env para respostas reais.</div>',
        unsafe_allow_html=True,
    )

for msg in chat_atual["messages"]:
    if msg["role"] in ("user", "assistant"):
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

st.markdown("### Sugestoes de perguntas")
s1, s2 = st.columns(2)
with s1:
    if st.button(SUGESTOES[0], use_container_width=True):
        st.session_state.prompt_from_suggestion = SUGESTOES[0]
    if st.button(SUGESTOES[1], use_container_width=True):
        st.session_state.prompt_from_suggestion = SUGESTOES[1]
with s2:
    if st.button(SUGESTOES[2], use_container_width=True):
        st.session_state.prompt_from_suggestion = SUGESTOES[2]
    if st.button(SUGESTOES[3], use_container_width=True):
        st.session_state.prompt_from_suggestion = SUGESTOES[3]

prompt_input = st.chat_input("Pergunte algo sobre ciberseguranca, SOC, playbooks, riscos...")
prompt = st.session_state.prompt_from_suggestion or prompt_input
st.session_state.prompt_from_suggestion = None

if prompt:
    chat_atual["messages"].append({"role": "user", "content": prompt})

    if chat_atual["title"] == "Nova conversa":
        chat_atual["title"] = prompt[:38] + ("..." if len(prompt) > 38 else "")

    with st.chat_message("user"):
        st.write(prompt)

    if not api_key or genai is None:
        resposta = (
            "Modo demo ativo: defina GOOGLE_API_KEY para respostas reais. "
            "Pergunta recebida e registrada no historico."
        )
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel("gemini-2.5-flash")
            gemini_history = []
            for item in chat_atual["messages"]:
                if item["role"] == "user":
                    gemini_history.append({"role": "user", "parts": [item["content"]]})
                elif item["role"] == "assistant":
                    gemini_history.append({"role": "model", "parts": [item["content"]]})

            chat = model.start_chat(history=gemini_history[:-1])
            with st.spinner("Gerando resposta..."):
                response = chat.send_message(
                    prompt,
                    generation_config=genai.types.GenerationConfig(
                        temperature=0.2,
                        max_output_tokens=4096,
                    ),
                )
                partes = [response.text or ""]

                # Continua automaticamente se a resposta parou por limite de tokens.
                for _ in range(2):
                    if not is_max_tokens_stop(response):
                        break
                    response = chat.send_message(
                        "Continue exatamente de onde parou, sem repetir.",
                        generation_config=genai.types.GenerationConfig(
                            temperature=0.2,
                            max_output_tokens=4096,
                        ),
                    )
                    partes.append(response.text or "")

            resposta = "\n".join(p.strip() for p in partes if p and p.strip())
        except Exception as e:
            # Fallback quando quota/rate limit/erro
            if "429" in str(e) or "quota" in str(e).lower() or "ResourceExhausted" in str(e):
                st.warning(
                    "⚠️ Quota de Gemini API esgotada. Aguarde alguns minutos e tente novamente. "
                    "[Detalhes](https://ai.google.dev/gemini-api/docs/rate-limits)"
                )
                resposta = f"[Modo demo por quota esgotada] Sua pergunta era: '{prompt}'\n\nTente novamente em alguns minutos ou aumente sua quota."
            else:
                st.error(f"Erro ao chamar Gemini: {str(e)[:200]}")
                resposta = "Erro ao processar. Verifique GOOGLE_API_KEY e tente novamente."

    chat_atual["messages"].append({"role": "assistant", "content": resposta})
    with st.chat_message("assistant"):
        st.write(resposta)
