"""
07_RedTeam_BlueTeam_OSI_IA.py
Kensei AI Foundations - Semana 07

Jogo educacional de estrategia cibernetica inspirado em Red Team vs Blue Team.
- Ambiente ficticio para aprendizado.
- IA adversaria com modo offline e opcao de API externa.
"""

from __future__ import annotations

import json
import random
import re
import http.client
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from datetime import datetime
from typing import Any

import streamlit as st

st.set_page_config(
    page_title="Red Team vs Blue Team // OSI IA",
    page_icon="AI",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
<style>
[data-testid="stAppViewContainer"] {
    background:
      radial-gradient(1200px 600px at 15% -10%, rgba(255, 66, 66, 0.13), transparent 50%),
      radial-gradient(1200px 600px at 85% -10%, rgba(64, 137, 255, 0.13), transparent 50%),
      linear-gradient(180deg, #07090f 0%, #0a0f19 55%, #0b0c11 100%);
}
.main-title {
    font-family: 'Courier New', monospace;
    font-size: 2rem;
    font-weight: 800;
    color: #d8e4ff;
    letter-spacing: 2px;
    margin-bottom: 0;
}
.sub-title {
    font-family: 'Courier New', monospace;
    color: #7ea8ff;
    font-size: 0.85rem;
    margin-top: 0;
}
.panel {
    background: rgba(14, 18, 28, 0.92);
    border: 1px solid #263149;
    border-radius: 10px;
    padding: 0.9rem 1rem;
}
.terminal {
    background: #05070c;
    border: 1px solid #2f3855;
    border-radius: 8px;
    min-height: 360px;
    max-height: 460px;
    overflow-y: auto;
    padding: 0.9rem;
    font-family: 'Courier New', monospace;
    white-space: pre-wrap;
    line-height: 1.5;
}
.layer-card {
    background: rgba(12, 14, 22, 0.96);
    border: 1px solid #24314a;
    border-radius: 8px;
    padding: 0.65rem 0.8rem;
    margin: 0.25rem 0;
    font-family: 'Courier New', monospace;
    font-size: 0.78rem;
}
.osi-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 0.6rem;
}
.osi-card {
    background: linear-gradient(180deg, rgba(13, 20, 34, 0.95) 0%, rgba(9, 13, 22, 0.98) 100%);
    border: 1px solid #2a3751;
    border-radius: 10px;
    padding: 0.75rem 0.85rem;
    position: relative;
    overflow: hidden;
    animation: cardFadeIn 0.45s ease-out;
}
.osi-card::before {
    content: "";
    position: absolute;
    inset: 0;
    background: linear-gradient(120deg, transparent 0%, rgba(130, 170, 255, 0.08) 45%, transparent 100%);
    transform: translateX(-120%);
    animation: shine 4.5s linear infinite;
}
.osi-title {
    color: #d8e6ff;
    font-family: 'Courier New', monospace;
    font-size: 0.88rem;
    font-weight: 700;
    margin-bottom: 0.35rem;
    position: relative;
    z-index: 1;
}
.osi-meta {
    color: #9cb6e8;
    font-size: 0.75rem;
    margin: 0.15rem 0;
    position: relative;
    z-index: 1;
}
.osi-badge {
    display: inline-block;
    border: 1px solid #34507a;
    border-radius: 999px;
    padding: 0.12rem 0.5rem;
    color: #c4d8ff;
    font-size: 0.7rem;
    margin-right: 0.25rem;
    margin-bottom: 0.25rem;
    position: relative;
    z-index: 1;
}
.osi-flow {
    margin-top: 0.55rem;
    height: 6px;
    border-radius: 6px;
    background: #1a2438;
    border: 1px solid #2b3a59;
    overflow: hidden;
    position: relative;
    z-index: 1;
}
.osi-flow > span {
    display: block;
    height: 100%;
    background: linear-gradient(90deg, #4b76c8, #8bd2ff);
    animation: pulseFlow 2.2s ease-in-out infinite;
}
@keyframes pulseFlow {
    0% { opacity: 0.45; }
    50% { opacity: 1.0; }
    100% { opacity: 0.45; }
}
@keyframes shine {
    from { transform: translateX(-120%); }
    to { transform: translateX(120%); }
}
@keyframes cardFadeIn {
    from { opacity: 0; transform: translateY(8px); }
    to { opacity: 1; transform: translateY(0); }
}
.layer-card.red {
    border-color: #8a2f3c;
    box-shadow: inset 0 0 0 1px rgba(138, 47, 60, 0.25);
}
.layer-card.blue {
    border-color: #2c5ba7;
    box-shadow: inset 0 0 0 1px rgba(44, 91, 167, 0.28);
}
.layer-card.neutral {
    border-color: #3a455f;
}
.stat-chip {
    display: inline-block;
    border: 1px solid #30405b;
    border-radius: 999px;
    padding: 0.25rem 0.75rem;
    margin: 0.1rem;
    font-family: 'Courier New', monospace;
    font-size: 0.8rem;
    color: #c3d2f7;
    background: #0d1320;
}
.small-note {
    color: #8ca2cd;
    font-size: 0.77rem;
}
.end-modal-overlay {
    position: fixed;
    inset: 0;
    background: rgba(4, 8, 16, 0.74);
    backdrop-filter: blur(3px);
    z-index: 1200;
}
.end-modal-card {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: min(760px, 92vw);
    background: linear-gradient(180deg, #0c1220 0%, #0a101b 100%);
    border: 1px solid #35507a;
    border-radius: 14px;
    padding: 1rem 1.1rem;
    z-index: 1201;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.55);
    font-family: 'Courier New', monospace;
}
.end-modal-title {
    font-size: 1.15rem;
    font-weight: 700;
    color: #dce8ff;
    margin-bottom: 0.45rem;
}
.end-modal-title.win {
    color: #6ef2aa;
}
.end-modal-title.lose {
    color: #ff9da3;
}
.end-modal-line {
    color: #a9c3f5;
    font-size: 0.85rem;
    margin: 0.2rem 0;
}
.stButton > button {
    border-radius: 6px !important;
    border: 1px solid #2f4266 !important;
    background: #0e1626 !important;
    color: #c6dbff !important;
    font-family: 'Courier New', monospace !important;
}
.stButton > button:hover {
    border-color: #5d8de6 !important;
    box-shadow: 0 0 0 1px #5d8de650 !important;
}
.stTextInput input, .stSelectbox div[data-baseweb="select"] > div {
    background: #0d1320 !important;
    color: #d5e3ff !important;
    border: 1px solid #2d3f60 !important;
}
</style>
""",
    unsafe_allow_html=True,
)

LAYER_META = [
    ("L1", "Fisica", "Dispositivos, energia, acesso fisico"),
    ("L2", "Enlace", "Switches, VLAN, ARP, segmentacao"),
    ("L3", "Rede", "IP, roteamento, firewall, pivoting"),
    ("L4", "Transporte", "TCP/UDP, portas, sessoes de conexao"),
    ("L5", "Sessao", "Persistencia e autenticacao ativa"),
    ("L6", "Apresentacao", "Criptografia, TLS, codificacao"),
    ("L7", "Aplicacao", "APIs, usuarios, engenharia social"),
]

LAYER_DIFFICULTY = {"L1": 0.8, "L2": 0.9, "L3": 1.0, "L4": 1.0, "L5": 1.1, "L6": 1.15, "L7": 1.2}

OSI_DIDACTIC = {
    "L1": {
        "title": "Camada Fisica",
        "focus": "Hardware, energia, cabos e acesso presencial.",
        "red": "Sabotagem eletrica, USB malicioso, RFID clone.",
        "blue": "Controle de acesso, CCTV, sensores de anomalia eletrica.",
        "learn": "Seguranca nao comeca no software; comeca no ambiente fisico.",
    },
    "L2": {
        "title": "Camada de Enlace",
        "focus": "Switches, MAC, ARP e segmentacao local.",
        "red": "ARP poisoning, VLAN hopping, MAC spoofing.",
        "blue": "Port security, VLAN hardening, inspeccao ARP.",
        "learn": "Segmentacao de rede reduz impacto lateral no inicio do ataque.",
    },
    "L3": {
        "title": "Camada de Rede",
        "focus": "IP, roteamento, firewalls e caminhos de trafego.",
        "red": "Recon, tunelamento, pivoting e rota alternativa.",
        "blue": "ACLs, geoblocking, regras adaptativas de firewall.",
        "learn": "Visibilidade de rotas e telemetria define o campo de batalha.",
    },
    "L4": {
        "title": "Camada de Transporte",
        "focus": "TCP/UDP, portas e controle de conexoes.",
        "red": "Flooding, abuse de portas e takeover de sessoes.",
        "blue": "Rate limit, timeout, hardening de superficie exposta.",
        "learn": "Disponibilidade depende de disciplina de sessao e trafego.",
    },
    "L5": {
        "title": "Camada de Sessao",
        "focus": "Persistencia, autenticacao e continuidade de conexao.",
        "red": "Session hijacking, token replay, persistencia furtiva.",
        "blue": "Invalidacao de sessao, MFA, deteccao de comportamento anomalo.",
        "learn": "Controle de sessao protege identidade e continuidade operacional.",
    },
    "L6": {
        "title": "Camada de Apresentacao",
        "focus": "Criptografia, encoding e formato de dados.",
        "red": "Downgrade TLS, payload ofuscado, exfiltracao disfarcada.",
        "blue": "Rotacao de chaves, pinning, analise criptografica.",
        "learn": "Cripto ruim cria falsa sensacao de seguranca.",
    },
    "L7": {
        "title": "Camada de Aplicacao",
        "focus": "APIs, usuarios, interfaces e logica de negocio.",
        "red": "Phishing, fake login, abuso de API, engenharia social.",
        "blue": "Awareness, WAF, deteccao comportamental com IA.",
        "learn": "A maior superficie de ataque costuma ser humana e aplicada.",
    },
}

RED_ACTIONS = {
    "recon": {"label": "Recon", "type": "intel", "power": 1.0},
    "exploit": {"label": "Exploit", "type": "offense", "power": 1.3},
    "lateral_move": {"label": "Lateral Move", "type": "offense", "power": 1.2},
    "persistence": {"label": "Persistencia", "type": "offense", "power": 1.1},
    "social": {"label": "Engenharia Social", "type": "deception", "power": 1.15},
    "exfiltrate": {"label": "Exfiltracao", "type": "objective", "power": 1.25},
    "obfuscate": {"label": "Obfuscacao", "type": "stealth", "power": 1.0},
}

BLUE_ACTIONS = {
    "monitor": {"label": "Monitoramento", "type": "intel", "power": 1.0},
    "patch": {"label": "Patch", "type": "defense", "power": 1.2},
    "segment": {"label": "Segmentacao", "type": "defense", "power": 1.15},
    "hunt": {"label": "Threat Hunting", "type": "offense", "power": 1.25},
    "rotate_keys": {"label": "Rotacao de Chaves", "type": "defense", "power": 1.1},
    "awareness": {"label": "Awareness", "type": "deception", "power": 1.0},
    "honeypot": {"label": "Deploy Honeypot", "type": "deception", "power": 1.3},
}

ACTION_EDU = {
    "recon": {"when": "Inicio da operacao e leitura do terreno.", "effect": "Aumenta intel e melhora jogadas seguintes."},
    "exploit": {"when": "Quando identificar brecha exploravel.", "effect": "Avanco ofensivo com impacto alto no dominio."},
    "lateral_move": {"when": "Apos ponto inicial comprometido.", "effect": "Expande alcance para outras camadas/hosts."},
    "persistence": {"when": "Depois de obter acesso estavel.", "effect": "Mantem presenca e reduz perda de terreno."},
    "social": {"when": "Quando alvo humano e vetor relevante.", "effect": "Pode abrir brechas sem ataque direto."},
    "exfiltrate": {"when": "Quando ja existe caminho de saida.", "effect": "Converte controle em progresso de vitoria."},
    "obfuscate": {"when": "Ao notar aumento de deteccao.", "effect": "Reduz threat e mascara movimentacao."},
    "monitor": {"when": "Defesa inicial e vigilancia continua.", "effect": "Eleva visibilidade para antecipar ataques."},
    "patch": {"when": "Ao confirmar superficie vulneravel.", "effect": "Reduz sucesso do atacante na camada."},
    "segment": {"when": "Para conter propagacao lateral.", "effect": "Limita alcance do adversario."},
    "hunt": {"when": "Com indicio de comprometimento ativo.", "effect": "Busca sinais ocultos e remove presenca inimiga."},
    "rotate_keys": {"when": "Suspeita de vazamento criptografico.", "effect": "Invalida acessos e sessoes antigas."},
    "awareness": {"when": "Engenharia social em alta.", "effect": "Reduz eficacia de ataques humanos."},
    "honeypot": {"when": "Para atrair ofensiva previsivel.", "effect": "Cria armadilha e coleta inteligencia."},
}

BLUE_DOCTRINES = {
    "zero_trust": "Controle estrito, microsegmentacao, bloqueio agressivo.",
    "soc_paranoico": "Prioriza deteccao, falsos positivos aceitos.",
    "compliance": "Mudancas graduais, foco em auditoria e rastreabilidade.",
    "militar": "Resposta rapida, isolamento pesado e contra-medidas.",
}

RED_DOCTRINES = {
    "apt": "Baixo ruido, persistencia longa, objetivo estrategico.",
    "ransom": "Velocidade e impacto, pressao por indisponibilidade.",
    "mercenario": "Ataque oportunista, foco em retorno rapido.",
    "hacktivista": "Acoes simbolicas e visibilidade publica.",
}


def ts() -> str:
    return datetime.now().strftime("%H:%M:%S")


def add_log(text: str, style: str = "info") -> None:
    st.session_state.logs.append({"ts": ts(), "text": text, "style": style})
    if len(st.session_state.logs) > 220:
        st.session_state.logs = st.session_state.logs[-220:]


def style_to_color(style: str) -> str:
    colors = {
        "ok": "#6ef2aa",
        "err": "#ff8a8a",
        "warn": "#ffcc66",
        "info": "#9fc2ff",
        "cmd": "#dce8ff",
        "ai": "#bba8ff",
        "data": "#8ee5ff",
    }
    return colors.get(style, "#9fc2ff")


def get_actions(team: str) -> dict[str, dict[str, Any]]:
    return RED_ACTIONS if team == "red" else BLUE_ACTIONS


def opposite(team: str) -> str:
    return "blue" if team == "red" else "red"


def build_initial_layers() -> dict[str, dict[str, Any]]:
    layers: dict[str, dict[str, Any]] = {}
    for lid, name, desc in LAYER_META:
        layers[lid] = {
            "name": name,
            "desc": desc,
            "control": 0,
            "exposure": random.randint(30, 70),
            "intel_player": 0,
            "intel_ai": 0,
            "trap": None,
        }
    return layers


def init_game_state() -> None:
    if "setup_done" not in st.session_state:
        st.session_state.setup_done = False

    if "logs" not in st.session_state:
        st.session_state.logs = []

    if "game" not in st.session_state:
        st.session_state.game = {}



def start_match(setup: dict[str, Any]) -> None:
    player_team = "red" if setup["side"] == "Red Team" else "blue"
    ai_team = opposite(player_team)

    if ai_team == "blue":
        doctrine = random.choice(list(BLUE_DOCTRINES.keys()))
    else:
        doctrine = random.choice(list(RED_DOCTRINES.keys()))

    st.session_state.game = {
        "turn": 1,
        "max_turns": 30,
        "player_name": setup["player_name"],
        "player_team": player_team,
        "ai_team": ai_team,
        "player_doctrine": setup.get("player_doctrine", "custom"),
        "ai_doctrine": doctrine,
        "layers": build_initial_layers(),
        "core_integrity": 100,
        "red_progress": 0,
        "blue_progress": 0,
        "tempo": 100,
        "threat_level": 50,
        "winner": None,
        "ended": False,
        "player_history": [],
        "ai_history": [],
        "setup": setup,
    }

    st.session_state.logs = []
    add_log("=== OPERACAO INICIADA ===", "ok")
    add_log(
        f"Jogador: {setup['player_name']} | Time: {setup['side']} | IA adversaria: {ai_team.upper()} ({doctrine})",
        "info",
    )
    add_log("Mapa de batalha baseado no modelo OSI carregado.", "info")



def extract_json_block(text: str) -> dict[str, Any] | None:
    match = re.search(r"\{.*\}", text, flags=re.DOTALL)
    if not match:
        return None
    try:
        parsed = json.loads(match.group(0))
        if isinstance(parsed, dict):
            return parsed
    except json.JSONDecodeError:
        return None
    return None


def call_openai_compatible(
    endpoint: str,
    api_key: str,
    model: str,
    messages: list[dict[str, str]],
    temperature: float = 0.4,
    max_tokens: int = 260,
) -> str:
    payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    data = json.dumps(payload).encode("utf-8")

    req = urllib.request.Request(endpoint, data=data, method="POST")
    req.add_header("Content-Type", "application/json")
    req.add_header("Authorization", f"Bearer {api_key}")

    with urllib.request.urlopen(req, timeout=20) as resp:
        raw = resp.read().decode("utf-8")

    parsed = json.loads(raw)
    return parsed["choices"][0]["message"]["content"].strip()


def normalize_gemini_model_name(model: str) -> str:
    cleaned = model.strip()
    if cleaned.startswith("models/"):
        cleaned = cleaned.split("/", 1)[1]
    if " " in cleaned:
        cleaned = cleaned.split()[0]
    return cleaned


def sanitize_api_key(raw: str) -> str:
    cleaned = raw.strip()
    if not cleaned:
        return ""
    if any(ch.isspace() for ch in cleaned):
        cleaned = cleaned.split()[0]
    return cleaned


def is_likely_valid_api_key(provider: str, api_key: str) -> bool:
    if not api_key:
        return False
    if any(ord(ch) < 32 for ch in api_key):
        return False
    if len(api_key) > 200:
        return False
    if provider == "Gemini":
        return api_key.startswith("AIza") and bool(re.match(r"^[A-Za-z0-9_\-.]+$", api_key))
    return bool(re.match(r"^[A-Za-z0-9_\-.]+$", api_key))


def list_gemini_models(api_key: str) -> list[str]:
    safe_key = urllib.parse.quote_plus(api_key)
    endpoint = f"https://generativelanguage.googleapis.com/v1beta/models?key={safe_key}"
    req = urllib.request.Request(endpoint, method="GET")

    with urllib.request.urlopen(req, timeout=20) as resp:
        raw = resp.read().decode("utf-8")

    parsed = json.loads(raw)
    models = parsed.get("models", [])

    available: list[str] = []
    for item in models:
        name = str(item.get("name", ""))
        methods = item.get("supportedGenerationMethods", [])
        if "generateContent" not in methods:
            continue
        if not name:
            continue
        available.append(normalize_gemini_model_name(name))

    return sorted(set(available))


def pick_best_gemini_model(models: list[str]) -> str | None:
    if not models:
        return None

    preferred = [
        "gemini-2.5-flash",
        "gemini-2.5-pro",
        "gemini-2.0-flash",
        "gemini-2.0-flash-001",
        "gemini-2.0-flash-lite",
        "gemini-2.0-flash-lite-001",
        "gemini-1.5-pro",
        "gemini-1.5-flash",
        "gemini-pro",
    ]
    for p in preferred:
        if p in models:
            return p

    for m in models:
        if "gemini" in m.lower():
            return m

    return models[0]


def get_gemini_candidate_models(user_model: str, available_models: list[str]) -> list[str]:
    candidates: list[str] = []

    normalized_user = normalize_gemini_model_name(user_model) if user_model else ""
    if normalized_user:
        candidates.append(normalized_user)

    preferred = [
        "gemini-2.5-flash",
        "gemini-2.5-pro",
        "gemini-2.0-flash",
        "gemini-1.5-flash",
        "gemini-1.5-pro",
        "gemini-pro",
    ]
    for p in preferred:
        if p in available_models and p not in candidates:
            candidates.append(p)

    for m in available_models:
        if "gemini" in m.lower() and m not in candidates:
            candidates.append(m)

    for m in available_models:
        if m not in candidates:
            candidates.append(m)

    return candidates


def find_working_gemini_model(api_key: str, user_model: str) -> tuple[str | None, list[str], str | None]:
    """Retorna (modelo_funcional, lista_disponivel, erro_detalhe)."""
    try:
        available_models = list_gemini_models(api_key)
    except Exception as exc:
        return None, [], f"Nao foi possivel listar modelos Gemini: {exc}"

    if not available_models:
        return None, [], "Nenhum modelo com suporte a generateContent foi encontrado para esta chave."

    candidates = get_gemini_candidate_models(user_model=user_model, available_models=available_models)
    for candidate in candidates:
        try:
            _ = call_gemini_generate_content(api_key=api_key, model=candidate, prompt="Responda apenas OK")
            return candidate, available_models, None
        except Exception:
            continue

    return None, available_models, "Nenhum dos modelos candidatos respondeu ao generateContent."


def call_gemini_generate_content(api_key: str, model: str, prompt: str) -> str:
    model_name = normalize_gemini_model_name(model)
    safe_key = urllib.parse.quote_plus(api_key)
    endpoint = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={safe_key}"
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": 0.3, "maxOutputTokens": 220},
    }
    data = json.dumps(payload).encode("utf-8")

    req = urllib.request.Request(endpoint, data=data, method="POST")
    req.add_header("Content-Type", "application/json")

    with urllib.request.urlopen(req, timeout=20) as resp:
        raw = resp.read().decode("utf-8")

    parsed = json.loads(raw)
    candidates = parsed.get("candidates", [])
    if not candidates:
        raise KeyError("Gemini sem candidates")
    parts = candidates[0].get("content", {}).get("parts", [])
    if not parts:
        raise KeyError("Gemini sem parts")
    text = parts[0].get("text", "").strip()
    if not text:
        raise KeyError("Gemini resposta vazia")
    return text


def test_provider_connection(setup: dict[str, Any]) -> tuple[bool, str, str | None]:
    provider = setup.get("provider", "")
    if provider == "Local Offline":
        return True, "Modo Local Offline ativo. Conexao externa nao e necessaria.", None

    api_key = sanitize_api_key(setup.get("api_key", ""))
    model = setup.get("model", "").strip()
    endpoint = setup.get("endpoint", "").strip()

    if not api_key:
        return False, "API Key vazia.", None
    if not is_likely_valid_api_key(provider, api_key):
        return False, "API Key invalida para o provedor selecionado. Revise e cole somente a chave.", None

    try:
        if provider in ("OpenAI", "OpenAI Compatible"):
            if not endpoint:
                return False, "Endpoint de Chat Completions vazio.", None
            resolved_model = model or "gpt-4o-mini"
            _ = call_openai_compatible(
                endpoint=endpoint,
                api_key=api_key,
                model=resolved_model,
                messages=[
                    {"role": "system", "content": "Responda apenas OK."},
                    {"role": "user", "content": "Teste de conectividade."},
                ],
                temperature=0.0,
                max_tokens=8,
            )
            return True, "Conexao com endpoint OpenAI/OpenAI-compatible validada.", resolved_model

        if provider == "Gemini":
            resolved_model, available, err = find_working_gemini_model(api_key=api_key, user_model=model)
            if resolved_model:
                return True, f"Conexao com Gemini validada. Modelo configurado: {resolved_model}", resolved_model

            if available:
                sample = ", ".join(available[:8])
                return (
                    False,
                    f"{err} Modelos disponiveis na sua chave: {sample}",
                    pick_best_gemini_model(available),
                )

            return False, err or "Falha ao detectar modelo Gemini.", None

        return False, f"Provider nao suportado: {provider}", None
    except urllib.error.HTTPError as exc:
        body = ""
        try:
            body = exc.read().decode("utf-8")[:220]
        except Exception:
            body = "sem detalhe"

        if provider == "Gemini" and exc.code == 404:
            try:
                resolved_model, options, err = find_working_gemini_model(api_key=api_key, user_model=model)
                if resolved_model:
                    return (
                        True,
                        f"Modelo informado indisponivel. Ajuste automatico aplicado: {resolved_model}",
                        resolved_model,
                    )

                if options:
                    best = pick_best_gemini_model(options)
                    sample = ", ".join(options[:8])
                    return (
                        False,
                        f"{err or 'Modelo Gemini nao encontrado para generateContent.'} "
                        f"Use um destes modelos disponiveis na sua chave: {sample}",
                        best,
                    )
                return False, "Modelo Gemini nao encontrado e nenhum modelo generateContent foi listado para esta chave.", None
            except Exception:
                return (
                    False,
                    "Modelo Gemini nao encontrado (404). Verifique o nome do modelo e tente sem prefixo 'models/'.",
                    None,
                )

        return False, f"HTTP {exc.code}: {body}", None
    except (urllib.error.URLError, TimeoutError) as exc:
        return False, f"Falha de rede: {exc}", None
    except http.client.InvalidURL:
        return False, "API Key ou modelo contem caracteres invalidos. Cole apenas a chave, sem mensagens de erro.", None
    except (KeyError, json.JSONDecodeError) as exc:
        return False, f"Resposta invalida do provedor: {exc}", None


def request_llm_decision(game: dict[str, Any]) -> dict[str, Any] | None:
    setup = game["setup"]
    provider = setup["provider"]
    if provider == "Local Offline":
        return None

    api_key = sanitize_api_key(setup.get("api_key", ""))
    model = setup.get("model", "").strip()
    endpoint = setup.get("endpoint", "").strip()

    if not api_key or not model or not endpoint:
        return None
    if not is_likely_valid_api_key(provider, api_key):
        return None

    ai_team = game["ai_team"]
    actions = list(get_actions(ai_team).keys())
    layers = [lid for lid, _, _ in LAYER_META]

    recent_player = game["player_history"][-4:]
    recent_ai = game["ai_history"][-4:]

    system_msg = (
        "Voce e um comandante tatico de simulacao ciber. "
        "Responda APENAS JSON valido com chaves: action, layer, taunt."
    )
    user_msg = {
        "turn": game["turn"],
        "ai_team": ai_team,
        "ai_doctrine": game["ai_doctrine"],
        "core_integrity": game["core_integrity"],
        "threat_level": game["threat_level"],
        "allowed_actions": actions,
        "allowed_layers": layers,
        "recent_player_actions": recent_player,
        "recent_ai_actions": recent_ai,
        "control_by_layer": {k: v["control"] for k, v in game["layers"].items()},
    }

    try:
        if provider in ("OpenAI", "OpenAI Compatible"):
            answer = call_openai_compatible(
                endpoint=endpoint,
                api_key=api_key,
                model=model,
                messages=[
                    {"role": "system", "content": system_msg},
                    {"role": "user", "content": json.dumps(user_msg, ensure_ascii=True)},
                ],
            )
        elif provider == "Gemini":
            prompt = (
                "Voce e comandante tatico ciber. Retorne APENAS JSON valido com chaves action, layer, taunt.\n"
                f"Contexto: {json.dumps(user_msg, ensure_ascii=True)}"
            )
            answer = call_gemini_generate_content(api_key=api_key, model=model, prompt=prompt)
        else:
            return None

        parsed = extract_json_block(answer)
        if not parsed:
            return None

        action = str(parsed.get("action", "")).strip()
        layer = str(parsed.get("layer", "")).strip()
        taunt = str(parsed.get("taunt", "")).strip()

        if action not in actions or layer not in layers:
            return None

        return {"action": action, "layer": layer, "taunt": taunt}
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, KeyError, json.JSONDecodeError, http.client.InvalidURL):
        return None


def local_ai_decision(game: dict[str, Any]) -> dict[str, str]:
    ai_team = game["ai_team"]
    allowed_actions = list(get_actions(ai_team).keys())

    hist = game["player_history"]
    layer_counts = Counter(x["layer"] for x in hist) if hist else Counter()
    action_counts = Counter(x["action"] for x in hist) if hist else Counter()

    if layer_counts:
        focus_layer = layer_counts.most_common(1)[0][0]
    else:
        focus_layer = random.choice([lid for lid, _, _ in LAYER_META])

    if action_counts:
        dominant_action = action_counts.most_common(1)[0][0]
    else:
        dominant_action = ""

    if ai_team == "blue":
        if dominant_action in {"exploit", "lateral_move", "exfiltrate"}:
            action = random.choice(["hunt", "segment", "honeypot"])
        elif dominant_action in {"social", "obfuscate"}:
            action = random.choice(["awareness", "monitor", "honeypot"])
        else:
            action = random.choice(["monitor", "patch", "segment"])
    else:
        if game["core_integrity"] > 85:
            action = random.choice(["recon", "social", "exploit"])
        elif game["blue_progress"] > game["red_progress"]:
            action = random.choice(["lateral_move", "exploit", "exfiltrate"])
        else:
            action = random.choice(["persistence", "obfuscate", "exfiltrate"])

    if action not in allowed_actions:
        action = random.choice(allowed_actions)

    # Se camada favorita esta muito dominada pela IA, tenta outra para expandir.
    layer_obj = game["layers"][focus_layer]
    if ai_team == "red" and layer_obj["control"] > 3:
        focus_layer = random.choice([lid for lid, _, _ in LAYER_META])
    if ai_team == "blue" and layer_obj["control"] < -3:
        focus_layer = random.choice([lid for lid, _, _ in LAYER_META])

    taunts = [
        "Padrao identificado. Ajustando contra-estrategia.",
        "Nao e forca bruta. E geometria tatico-operacional.",
        "Seu ultimo movimento deixou rastros.",
        "Eu nao reajo, eu antecipo.",
    ]

    return {"action": action, "layer": focus_layer, "taunt": random.choice(taunts)}


def resolve_action(actor: str, team: str, action: str, layer_id: str) -> dict[str, Any]:
    game = st.session_state.game
    layer = game["layers"][layer_id]
    layer_diff = LAYER_DIFFICULTY[layer_id]

    actions = get_actions(team)
    meta = actions[action]

    base = 0.52
    power = meta["power"]
    intel_key = "intel_player" if actor == "player" else "intel_ai"
    intel_bonus = min(0.18, layer[intel_key] * 0.03)

    control = layer["control"]
    control_modifier = 0.0
    if team == "red":
        control_modifier = 0.03 * control
    else:
        control_modifier = -0.03 * control

    trap_penalty = 0.0
    if layer.get("trap") == team:
        trap_penalty = 0.12

    success_chance = base + (power - 1.0) * 0.22 + intel_bonus + control_modifier - (layer_diff - 1.0) * 0.18 - trap_penalty
    success_chance = max(0.15, min(0.9, success_chance))

    roll = random.random()
    success = roll <= success_chance

    impact = random.randint(1, 3)
    if meta["type"] in {"objective", "offense"}:
        impact += 1

    # Efeitos por tipo de acao
    if success:
        if meta["type"] == "intel":
            layer[intel_key] = min(5, layer[intel_key] + 2)
        elif meta["type"] == "deception":
            # Honeypot/blefe impacta chance do inimigo na proxima jogada da camada.
            layer["trap"] = opposite(team)
            if team == "blue":
                layer[intel_key] = min(5, layer[intel_key] + 1)
        elif meta["type"] == "stealth":
            game["threat_level"] = max(0, game["threat_level"] - 4)
            layer[intel_key] = min(5, layer[intel_key] + 1)

        if team == "red" and meta["type"] in {"offense", "objective", "deception"}:
            layer["control"] = min(5, layer["control"] + 1)
            game["red_progress"] += impact
            game["core_integrity"] = max(0, game["core_integrity"] - impact * 2)
            game["threat_level"] = min(100, game["threat_level"] + impact * 2)

        if team == "blue" and meta["type"] in {"defense", "offense", "deception"}:
            layer["control"] = max(-5, layer["control"] - 1)
            game["blue_progress"] += impact
            game["core_integrity"] = min(100, game["core_integrity"] + impact)
            game["threat_level"] = max(0, game["threat_level"] - impact * 2)

        if team == "blue" and meta["type"] == "intel":
            game["blue_progress"] += 1
        if team == "red" and meta["type"] == "intel":
            game["red_progress"] += 1
    else:
        # Falha gera vantagem passiva para o oponente.
        if team == "red":
            game["blue_progress"] += 1
            game["threat_level"] = min(100, game["threat_level"] + 2)
        else:
            game["red_progress"] += 1
            game["threat_level"] = max(0, game["threat_level"] - 1)

    game["tempo"] = max(0, game["tempo"] - random.randint(2, 5))

    return {
        "success": success,
        "chance": success_chance,
        "roll": roll,
        "impact": impact,
        "type": meta["type"],
        "label": meta["label"],
        "layer_name": layer["name"],
    }


def check_endgame() -> None:
    game = st.session_state.game
    if game["ended"]:
        return

    red_won = game["red_progress"] >= 20 or game["core_integrity"] <= 0
    blue_won = game["blue_progress"] >= 20 or (game["turn"] > game["max_turns"] and not red_won)

    if red_won:
        game["ended"] = True
        game["winner"] = "red"
    elif blue_won:
        game["ended"] = True
        game["winner"] = "blue"


def ai_turn() -> None:
    game = st.session_state.game
    if game["ended"]:
        return

    llm_decision = request_llm_decision(game)
    decision = llm_decision or local_ai_decision(game)

    action = decision["action"]
    layer = decision["layer"]
    taunt = decision.get("taunt", "")

    result = resolve_action(actor="ai", team=game["ai_team"], action=action, layer_id=layer)

    outcome = "SUCESSO" if result["success"] else "FALHA"
    add_log(
        f"[IA:{game['ai_team'].upper()}] {result['label']} em {layer} ({result['layer_name']}) -> {outcome}",
        "ai" if result["success"] else "warn",
    )
    if taunt:
        add_log(f"[IA] {taunt}", "ai")

    game["ai_history"].append({"turn": game["turn"], "action": action, "layer": layer, "success": result["success"]})


def play_turn(player_action: str, layer_id: str) -> None:
    game = st.session_state.game
    if game["ended"]:
        return

    player_team = game["player_team"]
    result = resolve_action(actor="player", team=player_team, action=player_action, layer_id=layer_id)

    outcome = "SUCESSO" if result["success"] else "FALHA"
    add_log(f"[PLAYER] {result['label']} em {layer_id} ({result['layer_name']}) -> {outcome}", "ok" if result["success"] else "err")
    add_log(
        f"[DADO] chance={result['chance']:.2f} roll={result['roll']:.2f} impacto={result['impact']}",
        "data",
    )

    game["player_history"].append(
        {"turn": game["turn"], "action": player_action, "layer": layer_id, "success": result["success"]}
    )

    check_endgame()
    if not game["ended"]:
        ai_turn()
        game["turn"] += 1
        check_endgame()



def dominant_player_style(game: dict[str, Any]) -> tuple[str, str]:
    if not game["player_history"]:
        return "sem dados", "sem dados"
    action = Counter(x["action"] for x in game["player_history"]).most_common(1)[0][0]
    layer = Counter(x["layer"] for x in game["player_history"]).most_common(1)[0][0]
    return action, layer


def render_osi_didactic_map(game: dict[str, Any]) -> None:
    cards = []
    for lid, _, _ in LAYER_META:
        layer = game["layers"][lid]
        did = OSI_DIDACTIC[lid]
        control = layer["control"]
        if control > 0:
            owner = f"RED +{control}"
            width = min(100, 45 + control * 10)
        elif control < 0:
            owner = f"BLUE {control}"
            width = min(100, 45 + abs(control) * 10)
        else:
            owner = "NEUTRO"
            width = 38

        intel = layer["intel_player"]
        exposure = str(layer["exposure"]) if intel >= 2 else "unknown"
        trap = "detectado" if layer.get("trap") == game["player_team"] else "unknown"

        cards.append(
            f'<div class="osi-card">'
            f'<div class="osi-title">{lid} - {did["title"]}</div>'
            f'<div class="osi-meta"><b>Dominio:</b> {owner} | <b>Intel:</b> {intel}/5 | <b>Exposure:</b> {exposure}</div>'
            f'<div class="osi-meta"><b>Foco:</b> {did["focus"]}</div>'
            f'<div class="osi-meta"><b>Red Team:</b> {did["red"]}</div>'
            f'<div class="osi-meta"><b>Blue Team:</b> {did["blue"]}</div>'
            f'<div class="osi-meta"><b>O que aprender:</b> {did["learn"]}</div>'
            f'<span class="osi-badge">trap: {trap}</span>'
            f'<span class="osi-badge">camada ativa</span>'
            f'<div class="osi-flow"><span style="width:{width}%"></span></div>'
            f'</div>'
        )

    st.markdown('<div class="osi-grid">' + "".join(cards) + '</div>', unsafe_allow_html=True)


def render_setup_screen() -> None:
    st.markdown('<div class="main-title">RED TEAM vs BLUE TEAM // OSI WAR IA</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">xadrez cibernetico por camadas OSI, com adversario IA adaptativo</div>', unsafe_allow_html=True)
    st.divider()

    c1, c2 = st.columns([1.2, 1])

    with c1:
        with st.container(border=True):
            st.markdown("### Cadastro da Operacao")
            player_name = st.text_input("Codinome", value="ghost_operator")
            side = st.radio("Escolha seu lado", ["Red Team", "Blue Team"], horizontal=True)

            if side == "Red Team":
                doctrine = st.selectbox("Sua doutrina", list(RED_DOCTRINES.keys()))
            else:
                doctrine = st.selectbox("Sua doutrina", list(BLUE_DOCTRINES.keys()))

            provider = st.selectbox(
                "IA adversaria",
                ["Local Offline", "OpenAI", "Gemini", "OpenAI Compatible"],
                help="OpenAI usa endpoint padrao. OpenAI Compatible aceita endpoint custom.",
            )

            default_model = "gpt-4o-mini"
            if provider == "Gemini":
                default_model = "gemini-2.0-flash"

            if "setup_last_provider" not in st.session_state:
                st.session_state.setup_last_provider = provider
            if "model_input" not in st.session_state:
                st.session_state.model_input = default_model
            if "pending_model_input" not in st.session_state:
                st.session_state.pending_model_input = None
            if "api_test_status" not in st.session_state:
                st.session_state.api_test_status = None

            if st.session_state.setup_last_provider != provider:
                st.session_state.model_input = default_model
                st.session_state.setup_last_provider = provider

            # Aplica autoajuste de modelo antes de instanciar o widget do campo.
            if st.session_state.pending_model_input:
                st.session_state.model_input = st.session_state.pending_model_input
                st.session_state.pending_model_input = None

            model = st.text_input("Modelo", key="model_input")
            if provider == "Gemini":
                st.caption("Dica: use nome sem prefixo 'models/'. Ex.: gemini-2.0-flash")

            default_endpoint = "https://api.openai.com/v1/chat/completions"
            if provider == "OpenAI Compatible":
                endpoint = st.text_input("Endpoint de Chat Completions", value=default_endpoint)
            elif provider == "OpenAI":
                endpoint = default_endpoint
                st.caption(default_endpoint)
            elif provider == "Gemini":
                endpoint = "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
                st.caption(endpoint)
            else:
                endpoint = ""

            api_key = st.text_input("API Key", type="password")

            if provider == "Gemini":
                st.markdown(
                    "**Onde obter API Key (Gemini):** [Google AI Studio](https://aistudio.google.com/app/apikey)"
                )
            elif provider == "OpenAI":
                st.markdown(
                    "**Onde obter API Key (OpenAI):** [OpenAI Platform Keys](https://platform.openai.com/api-keys)"
                )
            elif provider == "OpenAI Compatible":
                st.markdown(
                    "**API Key OpenAI-compatible:** use o portal do provedor configurado no endpoint (ex.: OpenRouter, Together, Groq)."
                )

            st.caption("A chave fica apenas na sessao do app e nao e gravada em arquivo.")

            status = st.session_state.api_test_status
            if status:
                kind, message, resolved = status
                if kind == "ok":
                    st.success(message)
                else:
                    st.error(message)
                if resolved:
                    st.info(f"Modelo configurado automaticamente: {resolved}")
                st.session_state.api_test_status = None

            setup_preview = {
                "provider": provider,
                "model": model.strip(),
                "endpoint": endpoint.strip(),
                "api_key": api_key,
            }

            test_col, start_col = st.columns(2)
            with test_col:
                if st.button("Testar conexao API", use_container_width=True):
                    ok, message, resolved_model = test_provider_connection(setup_preview)
                    status_kind = "ok" if ok else "err"
                    if resolved_model and resolved_model != model.strip():
                        st.session_state.pending_model_input = resolved_model
                        st.session_state.api_test_status = (status_kind, message, resolved_model)
                        st.rerun()

                    st.session_state.api_test_status = (status_kind, message, resolved_model)
                    st.rerun()

            can_start = bool(player_name.strip())
            with start_col:
                start_btn = st.button("Iniciar Guerra OSI", use_container_width=True, disabled=not can_start)

            if start_btn:
                setup = {
                    "player_name": player_name.strip(),
                    "side": side,
                    "player_doctrine": doctrine,
                    "provider": provider,
                    "model": model.strip(),
                    "endpoint": endpoint.strip(),
                    "api_key": api_key,
                }
                st.session_state.setup_done = True
                start_match(setup)
                st.rerun()

    with c2:
        with st.container(border=True):
            st.markdown("### Conceito do Jogo")
            st.markdown(
                """
- Cada camada OSI e um territorio de guerra.
- Voce joga por turnos; a IA responde com contra-estrategia.
- A IA observa seu padrao de jogadas e adapta a doutrina.
- Red Team vence por dominacao e exfiltracao.
- Blue Team vence por contencao, hardening e resiliencia.
                """
            )
            st.markdown("### Condicao de Vitoria")
            st.markdown(
                """
- Red vence: progresso red >= 20 ou integridade do core <= 0.
- Blue vence: progresso blue >= 20 ou fim dos turnos sem vitoria red.
                """
            )


@st.dialog("Resultado da Operacao")
def render_end_game_modal(game: dict[str, Any], player_team: str) -> None:
    winner = game["winner"]
    if winner == player_team:
        st.success(f"Vitoria {winner.upper()}! A estrategia da sua equipe prevaleceu.")
    else:
        st.error(f"Derrota. {winner.upper()} dominou o teatro cibernetico.")

    st.markdown(f"**Turnos:** {game['turn']}/{game['max_turns']}")
    st.markdown(f"**Placar:** RED {game['red_progress']} | BLUE {game['blue_progress']}")
    st.markdown(f"**Core/Threat:** {game['core_integrity']}% | {game['threat_level']}")
    st.caption("Dica: revise o Console Tatico para entender as jogadas decisivas.")

    c1, c2 = st.columns(2)
    with c1:
        if st.button("Fechar modal", key="close_end_modal_dialog", use_container_width=True):
            st.session_state.end_modal_open = False
            st.rerun()
    with c2:
        if st.button("Recomecar jogo", key="restart_end_modal_dialog", use_container_width=True):
            st.session_state.setup_done = False
            st.session_state.game = {}
            st.session_state.logs = []
            st.session_state.end_modal_open = False
            st.rerun()


def render_game_screen() -> None:
    game = st.session_state.game
    player_team = game["player_team"]

    st.markdown('<div class="main-title">RED TEAM vs BLUE TEAM // OSI WAR IA</div>', unsafe_allow_html=True)
    st.markdown(
        f'<div class="sub-title">Turno {game["turn"]}/{game["max_turns"]} | Voce: {player_team.upper()} | IA: {game["ai_team"].upper()}</div>',
        unsafe_allow_html=True,
    )

    paction, player_focus_layer = dominant_player_style(game)

    stat1, stat2, stat3, stat4, stat5 = st.columns(5)
    stat1.markdown(f'<span class="stat-chip">CORE {game["core_integrity"]}%</span>', unsafe_allow_html=True)
    stat2.markdown(f'<span class="stat-chip">RED {game["red_progress"]}</span>', unsafe_allow_html=True)
    stat3.markdown(f'<span class="stat-chip">BLUE {game["blue_progress"]}</span>', unsafe_allow_html=True)
    stat4.markdown(f'<span class="stat-chip">THREAT {game["threat_level"]}</span>', unsafe_allow_html=True)
    stat5.markdown(f'<span class="stat-chip">ESTILO {paction} @ {player_focus_layer}</span>', unsafe_allow_html=True)

    st.divider()

    tab_ops, tab_map, tab_intel, tab_story = st.tabs(["Operacoes", "Mapa OSI", "Intel", "Narrativa"])

    with tab_ops:
        st.markdown("### Console Tatico")
        html = ""
        for line in st.session_state.logs:
            color = style_to_color(line["style"])
            safe_text = (
                line["text"].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            )
            html += f'<span style="color:{color}">[{line["ts"]}] {safe_text}</span>\n'
        st.markdown(f'<div class="terminal">{html}</div>', unsafe_allow_html=True)

        st.markdown("### Seu Turno")
        disabled_play = game["ended"] or game["turn"] > game["max_turns"]

        if "turn_selected_layer" not in st.session_state:
            st.session_state.turn_selected_layer = "L3"

        st.markdown("**Camada alvo (cards didaticos):**")
        for start in range(0, len(LAYER_META), 3):
            layer_chunk = LAYER_META[start:start + 3]
            layer_cols = st.columns(len(layer_chunk))
            for col, (lid, lname, _) in zip(layer_cols, layer_chunk):
                did = OSI_DIDACTIC.get(lid, {})
                with col:
                    with st.container(border=True):
                        selected = st.session_state.turn_selected_layer == lid
                        st.markdown(f"**{lid} - {did.get('title', lname)}**")
                        st.caption(did.get("focus", ""))
                        st.markdown(f"Red: {did.get('red', '-')}")
                        st.markdown(f"Blue: {did.get('blue', '-')}")
                        btn_label = "Selecionada" if selected else "Selecionar camada"
                        if st.button(btn_label, key=f"layer_btn_{lid}", use_container_width=True, disabled=disabled_play):
                            st.session_state.turn_selected_layer = lid
                            st.rerun()

        chosen_layer = st.session_state.turn_selected_layer
        st.caption(f"Camada selecionada: {chosen_layer} - {game['layers'][chosen_layer]['name']}")

        st.markdown("**Acoes (cards didaticos):**")
        actions = get_actions(player_team)
        action_items = list(actions.items())
        for start in range(0, len(action_items), 3):
            row = action_items[start:start + 3]
            row_cols = st.columns(3)
            for col, (action_id, meta) in zip(row_cols, row):
                with col:
                    with st.container(border=True):
                        edu = ACTION_EDU.get(action_id, {})
                        st.markdown(f"**{meta['label']}**")
                        st.caption(f"Tipo: {meta['type']} | Potencia: {meta['power']:.2f}")
                        st.markdown(f"Quando usar: {edu.get('when', '-')}")
                        st.markdown(f"Efeito esperado: {edu.get('effect', '-')}")
                        if st.button(f"Executar {meta['label']}", key=f"act_btn_{action_id}", use_container_width=True, disabled=disabled_play):
                            add_log(f"$ turno {game['turn']}: {action_id} {chosen_layer}", "cmd")
                            play_turn(action_id, chosen_layer)
                            st.rerun()

        ctrl1, ctrl2 = st.columns([1, 1])
        with ctrl1:
            if st.button("Resetar Partida", use_container_width=True):
                st.session_state.setup_done = False
                st.session_state.game = {}
                st.session_state.logs = []
                st.session_state.end_modal_open = False
                st.rerun()

        if "end_modal_open" not in st.session_state:
            st.session_state.end_modal_open = False
        if "end_modal_token" not in st.session_state:
            st.session_state.end_modal_token = ""

        if game["ended"]:
            token = f"{game['winner']}_{game['turn']}_{game['red_progress']}_{game['blue_progress']}"
            if st.session_state.end_modal_token != token:
                st.session_state.end_modal_token = token
                st.session_state.end_modal_open = True

            if st.session_state.end_modal_open:
                render_end_game_modal(game, player_team)

    with tab_map:
        st.markdown("### Dominio por Camada OSI")
        st.caption("controle > 0 favorece RED, controle < 0 favorece BLUE")
        render_osi_didactic_map(game)

    with tab_intel:
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("### Doutrinas")
            st.markdown(f"- Seu perfil: **{game['player_doctrine']}**")
            st.markdown(f"- IA adversaria: **{game['ai_doctrine']}**")

            if game["ai_team"] == "blue":
                st.markdown(f"- Descricao IA: {BLUE_DOCTRINES[game['ai_doctrine']]}")
            else:
                st.markdown(f"- Descricao IA: {RED_DOCTRINES[game['ai_doctrine']]}")

            st.markdown("### Padrao detectado")
            st.markdown(f"- Acao dominante: **{paction}**")
            st.markdown(f"- Camada favorita: **{player_focus_layer}**")

        with col_b:
            st.markdown("### Regras de Impacto")
            st.markdown(
                """
- Acoes de intel revelam informacao e melhoram chance de sucesso.
- Acoes de deception podem armar traps na camada.
- Acoes ofensivas alteram dominio da camada.
- Integridade do core oscila conforme ofensiva e defesa.
                """
            )
            st.markdown('<p class="small-note">Dica: variar camada e tipo de acao reduz previsibilidade contra IA adaptativa.</p>', unsafe_allow_html=True)

    with tab_story:
        st.markdown("### Diario de Campanha")
        latest = st.session_state.logs[-12:]
        if not latest:
            st.info("Sem eventos ainda.")
        else:
            for item in latest:
                st.write(f"[{item['ts']}] {item['text']}")

        st.markdown("### Prompt de Comando Manual")
        cmd = st.text_input("Comando rapido", placeholder="ex: hint, doctrine, summary")
        if st.button("Executar comando narrativo"):
            low = cmd.strip().lower()
            if low == "hint":
                add_log("[NARRADOR] Sugestao: execute uma acao de intel antes de ofensiva em L6/L7.", "info")
            elif low == "doctrine":
                add_log(f"[NARRADOR] A IA esta seguindo doutrina {game['ai_doctrine']}.", "info")
            elif low == "summary":
                add_log(
                    f"[NARRADOR] RED={game['red_progress']} BLUE={game['blue_progress']} CORE={game['core_integrity']} THREAT={game['threat_level']}",
                    "data",
                )
            else:
                add_log("[NARRADOR] Comando nao reconhecido. Tente: hint, doctrine, summary.", "warn")
            st.rerun()


# App flow
init_game_state()

if not st.session_state.setup_done:
    render_setup_screen()
else:
    render_game_screen()
