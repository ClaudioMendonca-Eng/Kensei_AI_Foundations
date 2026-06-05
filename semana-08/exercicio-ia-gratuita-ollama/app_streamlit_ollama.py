import time
import os
from typing import Dict, List, Tuple

import requests
import streamlit as st

def _default_host() -> str:
    env_host = os.getenv("OLLAMA_HOST")
    if env_host:
        return env_host

    # Dev containers usually need host.docker.internal to reach host services.
    if os.path.exists("/.dockerenv"):
        return "http://host.docker.internal:11434"

    return "http://localhost:11434"


DEFAULT_HOST = _default_host()
DEFAULT_MODEL = "llama3.2:3b"


def check_ollama(host: str, timeout: int = 10) -> Tuple[bool, List[str], str]:
    """Check Ollama availability and return installed model names."""
    try:
        response = requests.get(f"{host}/api/tags", timeout=timeout)
        response.raise_for_status()
        payload = response.json()
        models = [item.get("name", "") for item in payload.get("models", [])]
        return True, models, "Conexao OK"
    except requests.RequestException as exc:
        return False, [], f"Falha ao conectar: {exc}"


def candidate_hosts() -> List[str]:
    """Return possible Ollama endpoints for host/container setups."""
    candidates = [
        os.getenv("OLLAMA_HOST", "").strip(),
        "http://host.docker.internal:11434",
        "http://172.17.0.1:11434",
        "http://172.18.0.1:11434",
        "http://localhost:11434",
    ]
    # Keep order but remove empty/duplicates.
    seen = set()
    deduped = []
    for host in candidates:
        if host and host not in seen:
            deduped.append(host)
            seen.add(host)
    return deduped


def auto_detect_host() -> Tuple[str, List[Dict[str, str]]]:
    """Probe candidate endpoints and return first working host plus report."""
    report = []
    for host in candidate_hosts():
        ok, models, msg = check_ollama(host, timeout=3)
        report.append(
            {
                "host": host,
                "status": "ok" if ok else "erro",
                "detalhe": msg,
                "modelos": str(len(models)) if ok else "0",
            }
        )
        if ok:
            return host, report
    return "", report


def generate_text(
    host: str,
    model: str,
    prompt: str,
    temperature: float,
    timeout: int = 120,
) -> Tuple[str, float, str]:
    """Call Ollama /api/generate and return text, latency and status."""
    started = time.perf_counter()
    try:
        payload = {
            "model": model,
            "prompt": prompt,
            "stream": False,
            "options": {"temperature": temperature},
        }
        response = requests.post(
            f"{host}/api/generate",
            json=payload,
            timeout=timeout,
        )
        response.raise_for_status()
        data = response.json()
        elapsed = time.perf_counter() - started
        return data.get("response", ""), elapsed, "ok"
    except requests.RequestException as exc:
        elapsed = time.perf_counter() - started
        return "", elapsed, f"erro: {exc}"


def run_battery(host: str, model: str, temperature: float) -> List[Dict[str, str]]:
    """Run a small local benchmark battery for the exercise."""
    prompts = [
        "Resuma em 3 bullet points o que e phishing para iniciantes.",
        "Classifique o texto 'Recebi email pedindo senha urgente' como risco baixo, medio ou alto e explique.",
        "Gere uma recomendacao curta para melhorar a seguranca de senha em uma empresa pequena.",
    ]

    results = []
    for idx, prompt in enumerate(prompts, start=1):
        answer, latency, status = generate_text(host, model, prompt, temperature)
        results.append(
            {
                "teste": f"T{idx}",
                "status": status,
                "latencia_s": f"{latency:.2f}",
                "prompt": prompt,
                "resposta": answer.strip()[:700] if answer else "",
            }
        )
    return results


st.set_page_config(page_title="Exercicio IA Gratuita - Ollama", page_icon="🧪", layout="wide")
st.title("🧪 Exercicio IA Gratuita com Ollama Local")
st.caption("Teste local com Docker + Streamlit para validar uso real de IA gratuita.")

with st.sidebar:
    st.header("Configuracao")
    host = st.text_input("Ollama host", value=DEFAULT_HOST, key="ollama_host_input")
    st.caption("Se estiver em dev container, tente: http://host.docker.internal:11434")
    if st.button("Auto detectar host", use_container_width=True):
        detected_host, probe_report = auto_detect_host()
        st.dataframe(probe_report, use_container_width=True)
        if detected_host:
            st.session_state["ollama_host_input"] = detected_host
            host = detected_host
            st.success(f"Host detectado: {detected_host}")
        else:
            st.error("Nenhum endpoint respondeu. Verifique se o Ollama esta rodando no host.")
    model = st.text_input("Modelo", value=DEFAULT_MODEL)
    temperature = st.slider("Temperature", 0.0, 1.5, 0.3, 0.1)

col_a, col_b = st.columns(2)

with col_a:
    st.subheader("1) Verificacao de ambiente")
    if st.button("Checar Ollama", use_container_width=True):
        ok, models, msg = check_ollama(host)
        if ok:
            st.success(msg)
            if models:
                st.write("Modelos encontrados:")
                st.code("\n".join(models))
            else:
                st.warning("Sem modelos instalados. Execute: ollama pull llama3.2:3b")
        else:
            st.error(msg)

    st.subheader("2) Prompt livre")
    user_prompt = st.text_area(
        "Digite um prompt para testar:",
        value="Explique em 5 linhas a diferenca entre Red Team e Blue Team.",
        height=140,
    )

    if st.button("Executar prompt", type="primary", use_container_width=True):
        answer, latency, status = generate_text(host, model, user_prompt, temperature)
        if status == "ok":
            st.success(f"Resposta gerada em {latency:.2f}s")
            st.write(answer)
        else:
            st.error(status)

with col_b:
    st.subheader("3) Bateria de testes do exercicio")
    st.write("Executa 3 testes padrao para comparar qualidade e velocidade.")
    if st.button("Rodar bateria", use_container_width=True):
        rows = run_battery(host, model, temperature)
        st.dataframe(rows, use_container_width=True)

        ok_count = sum(1 for row in rows if row["status"] == "ok")
        avg_latency = 0.0
        if rows:
            avg_latency = sum(float(row["latencia_s"]) for row in rows) / len(rows)

        st.info(f"Testes ok: {ok_count}/{len(rows)} | Latencia media: {avg_latency:.2f}s")

st.divider()
st.markdown(
    """
### Passo rapido para preparar o ambiente
1. Rode o Ollama no host (fora do dev container), via Docker ou instalacao local.
2. Garanta que a API esteja acessivel em `http://host.docker.internal:11434`.
3. Instale deps Python: `pip install -r requirements.txt`.
4. Rode o app: `streamlit run app_streamlit_ollama.py`.
"""
)
