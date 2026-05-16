import os
import time

import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Projeto 5 - Agente n8n SOC", page_icon="🔌", layout="wide")

st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] { background: linear-gradient(135deg, #0d1117 0%, #161b22 100%); }
    [data-testid="stSidebar"] { background: #111827; }
    .hero-title { font-size: 2.5rem !important; font-weight: 800 !important; color: #e6edf3 !important; }
    .status-alert { background: #f85149; color: white; padding: 0.8rem; border-radius: 8px; font-weight: bold; }
    .status-ok { background: #3fb950; color: white; padding: 0.8rem; border-radius: 8px; font-weight: bold; }
    .metric-card { background: #0f1724; border: 1px solid #30363d; border-radius: 12px; padding: 1rem; color: #e6edf3; }
    .perf-good { display: inline-block; background: #238636; color: white; padding: 0.4rem 0.8rem; border-radius: 20px; font-weight: 600; margin: 0.2rem; }
    .perf-poor { display: inline-block; background: #da3633; color: white; padding: 0.4rem 0.8rem; border-radius: 20px; font-weight: 600; margin: 0.2rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<p class="hero-title">🛡️ SOC Webhook Analyzer | n8n + Gemini</p>', unsafe_allow_html=True)
st.markdown("**Envie eventos de segurança. Obtenha playbooks IA em tempo real.**")

webhook_default = os.getenv("N8N_SOC_WEBHOOK_URL", "http://localhost:5678/webhook/soc-triagem")
webhook_url = st.text_input("🔗 URL do Webhook n8n", value=webhook_default)

if "/workflow/" in webhook_url or "/workflow/new" in webhook_url:
    st.markdown('<div class="status-alert">⚠️ URL do editor (não executável). Use /webhook/soc-triagem.</div>', unsafe_allow_html=True)
elif "/webhook/" not in webhook_url:
    st.info("💡 Dica: URL deve conter '/webhook/' ou '/webhook-test/'")

col1, col2, col3, col4 = st.columns(4)
with col1:
    evento = st.text_input("🔔 Evento", "anomalia_autenticacao")
with col2:
    host = st.text_input("🖥️ Host", "vpn-gateway-01")
with col3:
    tentativas = st.number_input("📊 Tentativas", min_value=1, value=218)
with col4:
    janela = st.number_input("⏱️ Janela (min)", min_value=1, value=5)

usuario = st.text_input("👤 Usuário alvo", "admin_financeiro")

tab1, tab2 = st.tabs(["📤 Enviar Evento", "⚡ Teste de Performance"])

with tab1:
    if st.button("🚀 Enviar para n8n", use_container_width=True):
        with st.spinner("📡 Conectando ao agente n8n..."):
            payload = {
                "evento": evento,
                "host": host,
                "tentativas": tentativas,
                "janela_minutos": janela,
                "usuario_alvo": usuario,
            }

            try:
                t0 = time.time()
                response = requests.post(webhook_url, json=payload, timeout=20)
                latencia = time.time() - t0

                if response.status_code == 200:
                    st.markdown(f'<div class="status-ok">✅ Sucesso (HTTP {response.status_code}) | Latência: {latencia:.2f}s</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="status-alert">⚠️ HTTP {response.status_code} | Latência: {latencia:.2f}s</div>', unsafe_allow_html=True)

                try:
                    data = response.json()
                    st.subheader("📊 Análise e Playbook")

                    if "classificacao" in data:
                        col_a, col_b, col_c = st.columns(3)
                        with col_a:
                            pri = data["classificacao"].get("prioridade", "?")
                            icon = "🔴" if pri == "alta" else "🟡" if pri == "media" else "🟢"
                            st.markdown(f'<div class="metric-card"><b>{icon} Prioridade</b><br>{pri.upper()}</div>', unsafe_allow_html=True)
                        with col_b:
                            score = data["classificacao"].get("score_risco", 0)
                            st.markdown(f'<div class="metric-card"><b>⚡ Risco</b><br>{score}/100</div>', unsafe_allow_html=True)
                        with col_c:
                            resumo = data["classificacao"].get("resumo", "")
                            st.markdown(f'<div class="metric-card"><b>📝 Evento</b><br>{resumo[:50]}...</div>', unsafe_allow_html=True)

                    if "playbook" in data:
                        st.json(data["playbook"])

                except Exception:
                    st.code(response.text)
            except Exception as exc:
                st.markdown(f'<div class="status-alert">❌ Falha: {str(exc)[:100]}</div>', unsafe_allow_html=True)

with tab2:
    st.write("**Teste de latência e cobertura do webhook.**")

    if st.button("🔥 Executar Teste de Performance", use_container_width=True):
        with st.spinner("Testando..."):
            latencias = []
            erros = 0

            progress_bar = st.progress(0)
            for i in range(5):
                try:
                    payload_test = {
                        "evento": f"test_{i}",
                        "host": "test-host",
                        "tentativas": 10 + i * 20,
                        "janela_minutos": 1,
                        "usuario_alvo": "test-user",
                    }
                    t0 = time.time()
                    resp = requests.post(webhook_url, json=payload_test, timeout=10)
                    latencias.append(time.time() - t0)
                except Exception:
                    erros += 1
                progress_bar.progress((i + 1) / 5)
            progress_bar.empty()

            col_p1, col_p2, col_p3, col_p4 = st.columns(4)
            with col_p1:
                media = sum(latencias) / len(latencias) if latencias else 999
                cor = "perf-good" if media < 2 else "perf-poor"
                st.markdown(f'<span class="{cor}">⏱️ Média: {media:.2f}s</span>', unsafe_allow_html=True)
            with col_p2:
                minima = min(latencias) if latencias else 999
                st.markdown(f'<span class="perf-good">⬇️ Mín: {minima:.2f}s</span>', unsafe_allow_html=True)
            with col_p3:
                maxima = max(latencias) if latencias else 999
                st.markdown(f'<span class="perf-poor">⬆️ Máx: {maxima:.2f}s</span>', unsafe_allow_html=True)
            with col_p4:
                taxa_sucesso = ((5 - erros) / 5) * 100
                st.markdown(f'<span class="perf-good">✅ Taxa: {taxa_sucesso:.0f}%</span>', unsafe_allow_html=True)

            st.success(f"✅ {5 - erros}/5 requisições bem-sucedidas | {erros} falhas")
