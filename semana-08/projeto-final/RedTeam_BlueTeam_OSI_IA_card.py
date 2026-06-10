"""
08_RedTeam_BlueTeam_OSI_IA_card.py
Kensei AI Foundations - Semana 07

Card game educacional de estrategia cibernetica inspirado em
Red Team vs Blue Team e visual de trading card game.
"""

from __future__ import annotations

import base64
import html
import json
import os
import random
import re
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime
from functools import lru_cache
from pathlib import Path
from typing import Any

import streamlit as st
import streamlit.components.v1 as components

BASE_DIR = Path(__file__).resolve().parent
CARD_ART_DIR = BASE_DIR / "img"
CARD_ART_THUMBS_DIR = CARD_ART_DIR / "thumbs"
CARD_ART_ALIASES = {
    "dns_tunneler": "c2_beacon.png",
}

st.set_page_config(
    page_title="Red Team vs Blue Team // Card Arena",
    page_icon="🃏",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700;800&family=Crimson+Text:ital,wght@0,400;0,600;1,400&family=JetBrains+Mono:wght@400;600&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;800&family=Rajdhani:wght@500;700&family=JetBrains+Mono:wght@400;600&display=swap');

:root {
    --bg-1: #070b16;
    --bg-2: #090e1f;
    --ink: #d6ebff;
    --cyan: #37e7ff;
    --pink: #ff4fd8;
    --lime: #b8ff4f;
    --panel: rgba(8, 14, 33, 0.88);
    --line: #2a4f7d;
}

[data-testid="stAppViewContainer"] {
  background:
        radial-gradient(900px 500px at 8% -8%, rgba(55, 231, 255, 0.23), transparent 55%),
        radial-gradient(900px 500px at 92% -12%, rgba(255, 79, 216, 0.20), transparent 58%),
        linear-gradient(180deg, var(--bg-1) 0%, var(--bg-2) 62%, #060912 100%);
}

.main-title {
    font-family: 'Orbitron', sans-serif;
  font-size: 2.2rem;
    letter-spacing: 2px;
  font-weight: 800;
    color: #dcf4ff;
    text-shadow: 0 0 16px rgba(55, 231, 255, 0.55);
  margin: 0;
}

.sub-title {
    font-family: 'Rajdhani', sans-serif;
    color: #85d8ff;
    font-size: 1.1rem;
    letter-spacing: 0.6px;
  margin-top: 0;
}

.info-chip {
  display: inline-block;
    border: 1px solid #355f93;
  border-radius: 999px;
  padding: 0.2rem 0.7rem;
  margin: 0.1rem;
    background: rgba(10, 19, 42, 0.78);
    color: #d7f1ff;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.78rem;
    box-shadow: inset 0 0 0 1px rgba(55, 231, 255, 0.18);
}

.log-box {
    border: 1px solid #284f7f;
    background: #090f22;
  border-radius: 10px;
    min-height: 420px;
    max-height: 540px;
  overflow-y: auto;
  padding: 0.8rem;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.78rem;
  line-height: 1.45;
}

.battle-strip {
    border: 1px solid #305986;
  border-radius: 12px;
  padding: 0.55rem;
    background: linear-gradient(180deg, rgba(12, 22, 45, 0.82), rgba(8, 14, 29, 0.82));
  margin-bottom: 0.6rem;
    box-shadow: 0 0 0 1px rgba(55, 231, 255, 0.15) inset;
}

.zone-title {
    color: #8de7ff;
    font-family: 'Orbitron', sans-serif;
  font-size: 0.95rem;
    letter-spacing: 0.7px;
  margin-bottom: 0.45rem;
}

.card-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.55rem;
}

.mtg-card {
  width: 208px;
  min-height: 290px;
  border-radius: 12px;
    border: 1px solid #2b578c;
    box-shadow: 0 8px 22px rgba(0, 0, 0, 0.48), inset 0 0 0 1px rgba(55, 231, 255, 0.14);
  overflow: hidden;
  position: relative;
  animation: cardIn 240ms ease-out;
}

.mtg-card.red { background: linear-gradient(180deg, #36132f 0%, #170f21 100%); }
.mtg-card.blue { background: linear-gradient(180deg, #102846 0%, #0a162c 100%); }
.mtg-card.black { background: linear-gradient(180deg, #181a35 0%, #0e1328 100%); }
.mtg-card.green { background: linear-gradient(180deg, #11373b 0%, #0a1f26 100%); }
.mtg-card.white { background: linear-gradient(180deg, #2b3448 0%, #161d2d 100%); }
.mtg-card.neutral { background: linear-gradient(180deg, #1d2740 0%, #0f1729 100%); }

.mtg-card.tapped {
  transform: rotate(90deg);
  transform-origin: center;
}

.mtg-head {
  display: flex;
  justify-content: space-between;
  gap: 0.35rem;
  padding: 0.45rem 0.5rem 0.28rem 0.5rem;
    color: #d9eeff;
    font-family: 'Orbitron', sans-serif;
  font-size: 0.76rem;
  font-weight: 700;
    letter-spacing: 0.5px;
}

.mana-cost {
  white-space: nowrap;
    color: #b9f4ff;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.72rem;
}

.card-art {
  height: 84px;
  margin: 0 0.5rem;
    border: 1px solid rgba(55, 231, 255, 0.32);
  border-radius: 7px;
    overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.9rem;
    background: linear-gradient(140deg, rgba(55, 231, 255, 0.12), rgba(255, 79, 216, 0.1));
}

.card-art img {
    width: 100%;
    height: 100%;
    display: block;
    object-fit: cover;
}

.type-line {
  margin: 0.3rem 0.5rem;
    border: 1px solid rgba(94, 170, 255, 0.34);
  border-radius: 6px;
  padding: 0.18rem 0.38rem;
    color: #cde8ff;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.68rem;
}

.text-box {
  margin: 0 0.5rem;
    border: 1px solid rgba(94, 170, 255, 0.28);
  border-radius: 6px;
  min-height: 102px;
  padding: 0.32rem 0.4rem;
    color: #e5f2ff;
    font-family: 'Rajdhani', sans-serif;
  font-size: 0.77rem;
  line-height: 1.2;
}

.flavor {
    color: #82d6f8;
  font-style: italic;
  font-size: 0.72rem;
  margin-top: 0.28rem;
}

.bottom-line {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 0.35rem 0.5rem 0.45rem 0.5rem;
}

.rarity {
    color: #9de5ff;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.68rem;
}

.pt-badge {
    border: 1px solid #3e6ea8;
  border-radius: 6px;
    background: rgba(10, 16, 31, 0.85);
    color: #d2eeff;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.72rem;
  padding: 0.08rem 0.35rem;
}

.stat-bar {
  height: 14px;
  border: 1px solid #644f2d;
  border-radius: 7px;
  background: #21170d;
  overflow: hidden;
}

.stat-fill {
  height: 100%;
  background: linear-gradient(90deg, #7f2a21, #c9553f, #dca568);
}

.small-note {
    color: #9ed6ff;
  font-size: 0.8rem;
}

.story-box {
        border: 1px solid #2d5588;
        border-radius: 10px;
        background: linear-gradient(180deg, rgba(10, 17, 34, 0.9), rgba(8, 13, 25, 0.9));
        padding: 0.75rem 0.85rem;
        margin-top: 0.55rem;
        color: #d8ecff;
        font-family: 'Rajdhani', sans-serif;
        font-size: 0.95rem;
        line-height: 1.45;
}

.provider-guide-box {
    border: 1px solid #355b8e;
    border-radius: 12px;
    background: linear-gradient(180deg, rgba(10, 22, 45, 0.94), rgba(7, 14, 31, 0.94));
    padding: 0.75rem 0.85rem;
    margin: 0.55rem auto 0.85rem auto;
    max-width: 860px;
    box-shadow: inset 0 0 0 1px rgba(55, 231, 255, 0.12), 0 6px 18px rgba(0, 0, 0, 0.25);
}

.provider-guide-title {
    text-align: center;
    font-family: 'Orbitron', sans-serif;
    color: #ccedff;
    font-size: 0.92rem;
    letter-spacing: 0.7px;
    margin-bottom: 0.5rem;
}

.provider-guide-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 0.42rem;
}

.provider-guide-item {
    border: 1px solid #2e4e79;
    border-radius: 10px;
    background: rgba(7, 14, 29, 0.82);
    padding: 0.5rem 0.55rem;
}

.provider-guide-item.active {
    border-color: #45d8ff;
    box-shadow: inset 0 0 0 1px rgba(69, 216, 255, 0.35);
    background: linear-gradient(180deg, rgba(8, 23, 45, 0.92), rgba(8, 18, 34, 0.92));
}

.provider-guide-name {
    font-family: 'JetBrains Mono', monospace;
    color: #9ee8ff;
    font-size: 0.76rem;
    margin-bottom: 0.2rem;
}

.provider-guide-copy {
    color: #dbeeff;
    font-size: 0.78rem;
    line-height: 1.32;
}

.modal-shell {
    border: 1px solid #325a8f;
    border-radius: 12px;
    padding: 0.75rem;
    background: linear-gradient(180deg, rgba(9, 16, 34, 0.92), rgba(7, 12, 24, 0.94));
}

.modal-panel {
    border: 1px solid #2f5588;
    border-radius: 10px;
    padding: 0.8rem;
    background: rgba(10, 17, 35, 0.76);
}

.modal-title {
    font-family: 'Orbitron', sans-serif;
    color: #c6ecff;
    font-size: 1.05rem;
    margin-bottom: 0.35rem;
}

.modal-badge {
    display: inline-block;
    border: 1px solid #3b6ca7;
    border-radius: 999px;
    padding: 0.15rem 0.55rem;
    margin-right: 0.28rem;
    margin-bottom: 0.3rem;
    background: rgba(15, 26, 48, 0.8);
    color: #d0ecff;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
}

.modal-copy {
    color: #e1f2ff;
    font-size: 0.9rem;
    line-height: 1.45;
}

.osi-progress-track {
    width: 100%;
    height: 12px;
    border-radius: 999px;
    border: 1px solid #2e4e79;
    background: #0b1731;
    overflow: hidden;
    margin: 0.25rem 0 0.4rem 0;
}

.osi-progress-fill {
    height: 100%;
    border-radius: 999px;
}

.osi-blue {
    background: linear-gradient(90deg, #2d8cff, #56b8ff);
}

.osi-orange {
    background: linear-gradient(90deg, #ff8b2b, #ffc15e);
}

.osi-red {
    background: linear-gradient(90deg, #ff4d4d, #ff8a5c);
}

.osi-layer-note {
    border: 1px solid #27466f;
    border-radius: 8px;
    background: rgba(8, 16, 33, 0.68);
    padding: 0.45rem 0.55rem;
    margin-bottom: 0.45rem;
    color: #cfe8ff;
    font-size: 0.8rem;
    line-height: 1.35;
}

.modal-card-wrap {
    display: flex;
    justify-content: center;
    align-items: flex-start;
    padding-top: 0.35rem;
    min-height: 460px;
}

.modal-card-scale {
    transform: scale(1.5);
    transform-origin: top center;
}

.modal-sub {
    color: #7cd9ff;
    font-family: 'Orbitron', sans-serif;
    font-size: 0.82rem;
    margin-top: 0.55rem;
    margin-bottom: 0.2rem;
}

.hero-shell {
    border: 1px solid #315b90;
    border-radius: 14px;
    background: linear-gradient(180deg, rgba(10, 18, 37, 0.92), rgba(8, 13, 26, 0.95));
    padding: 0.95rem;
    margin-top: 0.45rem;
    margin-bottom: 0.7rem;
}

.image-slot {
    min-height: 250px;
    border: 1px dashed #4472ac;
    border-radius: 12px;
    background: linear-gradient(140deg, rgba(55, 231, 255, 0.08), rgba(255, 79, 216, 0.07));
    color: #b9e7ff;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 0.85rem;
    font-family: 'Rajdhani', sans-serif;
    font-size: 1rem;
}

.team-panel {
    border: 1px solid #2f5789;
    border-radius: 12px;
    background: rgba(10, 17, 35, 0.74);
    padding: 0.7rem;
    margin-bottom: 0.55rem;
}

.team-title {
    text-align: center;
}

.team-title-red {
    color: #ff6b6b;
}

.team-title-blue {
    color: #6ec8ff;
}

.team-copy {
    color: #d8efff;
    font-size: 0.9rem;
    line-height: 1.35;
    text-align: center;
}

.wizard-heading {
    color: #8be5ff;
    font-family: 'Orbitron', sans-serif;
    letter-spacing: 0.7px;
    font-size: 0.95rem;
    margin-top: 0.25rem;
}

.doctrine-card {
    border: 1px solid #2f588b;
    border-radius: 12px;
    background: linear-gradient(180deg, rgba(12, 21, 41, 0.92), rgba(9, 15, 31, 0.92));
    padding: 0.75rem;
    min-height: 420px;
}

.doctrine-name {
    color: #d4eeff;
    font-family: 'Orbitron', sans-serif;
    font-size: 0.88rem;
    margin-bottom: 0.3rem;
}

.doctrine-copy {
    color: #deefff;
    font-size: 1.15rem;
    line-height: 1.35;
    min-height: 62px;
    text-align: center;
}

.mini-status {
    color: #9ddcff;
    font-size: 0.82rem;
    margin-top: 0.25rem;
}

@media (max-width: 900px) {
    .main-title {
        font-size: 1.6rem;
    }

    .image-slot {
        min-height: 190px;
    }

    .doctrine-card {
        min-height: auto;
    }
}

@keyframes cardIn {
  from { opacity: 0; transform: translateY(6px); }
  to { opacity: 1; transform: translateY(0); }
}

.stButton > button {
  border-radius: 8px !important;
    border: 1px solid #355c91 !important;
    background: #101c35 !important;
    color: #d6efff !important;
  font-family: 'JetBrains Mono', monospace !important;
}

.stButton > button:hover {
    border-color: #5de2ff !important;
    box-shadow: 0 0 0 1px #5de2ff55 !important;
}

.stTextInput input, .stSelectbox div[data-baseweb="select"] > div {
    background: #0c152b !important;
    color: #d5edff !important;
    border: 1px solid #355b8e !important;
}

[class*="st-key-open_card_head_click_"] .stButton > button,
[class*="st-key-open_board_head_click_"] .stButton > button,
[class*="st-key-quick_play_click_"] .stButton > button {
    width: auto !important;
    min-width: 54px !important;
    height: 34px !important;
    min-height: 34px !important;
    margin-top: 0.35rem !important;
    margin-left: 0 !important;
    margin-right: 0 !important;
    padding: 0 0.55rem !important;
    border: 1px solid #3f6baa !important;
    background: rgba(12, 22, 44, 0.96) !important;
    box-shadow: 0 0 0 1px rgba(55, 231, 255, 0.2) inset !important;
    opacity: 1 !important;
    color: #d5eeff !important;
    font-size: 1rem !important;
    line-height: 1 !important;
    outline: none !important;
    cursor: pointer !important;
}

[class*="st-key-open_card_head_click_"],
[class*="st-key-open_board_head_click_"] {
    margin-top: -74px !important;
    margin-bottom: 36px !important;
    position: relative;
    z-index: 8;
}

[class*="st-key-open_card_head_click_"] .stButton,
[class*="st-key-open_board_head_click_"] .stButton {
    display: flex !important;
    justify-content: center !important;
}

[class*="st-key-open_card_head_click_"] .stButton > button,
[class*="st-key-open_board_head_click_"] .stButton > button {
    width: 30px !important;
    min-width: 30px !important;
    height: 30px !important;
    min-height: 30px !important;
    padding: 0 !important;
    border-radius: 999px !important;
    border: 1px solid #63dcff !important;
    background: rgba(8, 20, 41, 0.95) !important;
    box-shadow: 0 0 0 1px rgba(99, 220, 255, 0.22) inset !important;
    font-size: 0.9rem !important;
    line-height: 1 !important;
}

[class*="st-key-open_card_head_click_"] .stButton > button:hover,
[class*="st-key-open_board_head_click_"] .stButton > button:hover {
    border-color: #8aeaff !important;
    background: rgba(10, 26, 52, 0.98) !important;
    box-shadow: 0 0 0 1px rgba(138, 234, 255, 0.36) inset !important;
}

[class*="st-key-open_card_click_"] .stButton {
    display: flex !important;
    justify-content: flex-start !important;
}

[class*="st-key-quick_play_click_"] .stButton {
    display: flex !important;
    justify-content: flex-end !important;
}

[class*="st-key-open_card_click_"] .stButton > button:hover,
[class*="st-key-quick_play_click_"] .stButton > button:hover {
    border-color: #6ee6ff !important;
    background: rgba(18, 30, 58, 0.98) !important;
    box-shadow: 0 0 0 1px rgba(110, 230, 255, 0.35) inset !important;
}

[class*="st-key-wizard_open_team_modal"] {
    margin-top: -230px !important;
    margin-bottom: 170px !important;
    position: relative;
    z-index: 6;
}

[class*="st-key-wizard_open_team_modal"] .stButton {
    display: flex !important;
    justify-content: center !important;
}

[class*="st-key-wizard_open_team_modal"] .stButton > button {
    width: 280px !important;
    max-width: 80vw !important;
    height: 46px !important;
    font-size: 1.02rem !important;
    font-weight: 700 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.8px !important;
    border: 1px solid #65e7ff !important;
    box-shadow: 0 0 24px rgba(55, 231, 255, 0.25), inset 0 0 0 1px rgba(101, 231, 255, 0.25) !important;
}

[class*="st-key-wizard_reset_flow"] {
    margin-top: -155px !important;
    margin-bottom: 115px !important;
    position: relative;
    z-index: 6;
}

[class*="st-key-wizard_reset_flow"] .stButton {
    display: flex !important;
    justify-content: center !important;
}

[class*="st-key-wizard_reset_flow"] .stButton > button {
    width: 280px !important;
    max-width: 80vw !important;
    height: 44px !important;
    font-size: 0.96rem !important;
    font-weight: 700 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.7px !important;
    border: 1px solid #5ad9ff !important;
    box-shadow: 0 0 20px rgba(90, 217, 255, 0.22), inset 0 0 0 1px rgba(90, 217, 255, 0.2) !important;
}

.stDialog div[role="dialog"] {
    width: min(1320px, 97vw) !important;
    max-width: min(1320px, 97vw) !important;
}

[class*="st-key-modal_back_from_doctrine"],
[class*="st-key-modal_back_from_ai"] {
    position: absolute !important;
    top: 1.875rem !important;
    right: 3.4rem !important;
    z-index: 30 !important;
}

[class*="st-key-modal_back_from_doctrine"] .stButton > button,
[class*="st-key-modal_back_from_ai"] .stButton > button {
    width: 24px !important;
    height: 24px !important;
    min-width: 24px !important;
    min-height: 24px !important;
    padding: 0 !important;
    border: 1px solid transparent !important;
    border-radius: 4px !important;
    background: transparent !important;
    box-shadow: none !important;
    color: #fafafa !important;
    font-size: 0.95rem !important;
    line-height: 1 !important;
}

[class*="st-key-modal_back_from_doctrine"] .stButton > button:hover,
[class*="st-key-modal_back_from_ai"] .stButton > button:hover {
    border-color: #66e6ff !important;
    background: rgba(23, 40, 74, 0.7) !important;
}
</style>
""",
    unsafe_allow_html=True,
)

MANA_COLORS = {
    "R": {"name": "Scarlet", "css": "red"},
    "U": {"name": "Cobalt", "css": "blue"},
    "B": {"name": "Void", "css": "black"},
    "G": {"name": "Grid", "css": "green"},
    "W": {"name": "Signal", "css": "white"},
    "C": {"name": "Neutral", "css": "neutral"},
}

RED_DOCTRINES = {
    "apt": "Baixo ruido, persistencia longa e objetivo estrategico.",
    "ransom": "Velocidade e impacto com foco em indisponibilidade.",
    "mercenario": "Ataque oportunista com retorno rapido.",
    "hacktivista": "Acoes simbolicas para visibilidade publica.",
}

BLUE_DOCTRINES = {
    "zero_trust": "Microsegmentacao e bloqueio agressivo.",
    "soc_paranoico": "Deteccao antecipada com alta vigilancia.",
    "compliance": "Mudancas graduais e rastreabilidade.",
    "militar": "Resposta rapida com isolamento severo.",
}

TEAM_EXPLANATIONS = {
    "Red Team": "Equipe ofensiva focada em exploracao, evasao e pressao por impacto.",
    "Blue Team": "Equipe defensiva focada em deteccao, contencao e resiliencia operacional.",
}

TEAM_DOCTRINES = {
    "Red Team": RED_DOCTRINES,
    "Blue Team": BLUE_DOCTRINES,
}

ONBOARDING_IMAGE_DEFAULTS = {
    "presentation_image": str(CARD_ART_DIR / "capa_apresentacao_card_arena.png"),
    "team_red_image": str(CARD_ART_DIR / "team_red_apresentacao.png"),
    "team_blue_image": str(CARD_ART_DIR / "team_blue_apresentacao.png"),
    "ai_setup_image": str(CARD_ART_DIR / "ia_setup_background.png"),
    "doctrine_image_red_team_apt": str(CARD_ART_DIR / "red_doctrine_apt.png"),
    "doctrine_image_red_team_ransom": str(CARD_ART_DIR / "red_doctrine_ransom.png"),
    "doctrine_image_red_team_mercenario": str(CARD_ART_DIR / "red_doctrine_mercenario.png"),
    "doctrine_image_red_team_hacktivista": str(CARD_ART_DIR / "red_doctrine_hacktivista.png"),
    "doctrine_image_blue_team_zero_trust": str(CARD_ART_DIR / "blue_doctrine_zero_trust.png"),
    "doctrine_image_blue_team_soc_paranoico": str(CARD_ART_DIR / "blue_doctrine_soc_paranoico.png"),
    "doctrine_image_blue_team_compliance": str(CARD_ART_DIR / "blue_doctrine_compliance.png"),
    "doctrine_image_blue_team_militar": str(CARD_ART_DIR / "blue_doctrine_militar.png"),
}

CARD_DB: dict[str, dict[str, Any]] = {
    "node_l1": {"name": "Nodo Fisico", "type": "Node", "cost": {}, "produce": "W", "text": "Gera 1 mana W.", "flavor": "Toda guerra digital nasce no mundo fisico.", "rarity": "C", "osi": "L1", "art": "🔌", "color": "W"},
    "node_l2": {"name": "Hub de Enlace", "type": "Node", "cost": {}, "produce": "U", "text": "Gera 1 mana U.", "flavor": "Segmentacao corta a propagacao lateral.", "rarity": "C", "osi": "L2", "art": "🧩", "color": "U"},
    "node_l3": {"name": "Gateway de Rede", "type": "Node", "cost": {}, "produce": "R", "text": "Gera 1 mana R.", "flavor": "Roteamento define o campo de batalha.", "rarity": "C", "osi": "L3", "art": "🌐", "color": "R"},
    "node_l4": {"name": "Servidor TCP", "type": "Node", "cost": {}, "produce": "G", "text": "Gera 1 mana G.", "flavor": "Conexao e disponibilidade sao armas.", "rarity": "C", "osi": "L4", "art": "🖧", "color": "G"},
    "node_l5": {"name": "Broker de Sessao", "type": "Node", "cost": {}, "produce": "B", "text": "Gera 1 mana B.", "flavor": "Sessao comprometida vira persistencia.", "rarity": "C", "osi": "L5", "art": "🪪", "color": "B"},
    "node_l6": {"name": "Modulo TLS", "type": "Node", "cost": {}, "produce": "W", "text": "Gera 1 mana W.", "flavor": "Cripto boa reduz risco real.", "rarity": "C", "osi": "L6", "art": "🔐", "color": "W"},
    "node_l7": {"name": "Endpoint App", "type": "Node", "cost": {}, "produce": "R", "text": "Gera 1 mana R.", "flavor": "A superficie humana nunca dorme.", "rarity": "C", "osi": "L7", "art": "🧠", "color": "R"},
    "script_kiddie": {"name": "Script Kiddie", "type": "Agent", "cost": {"R": 1}, "atk": 2, "hp": 1, "text": "Ataque rapido de baixa sofisticacao.", "flavor": "Barulho nao e estrategia, mas as vezes funciona.", "rarity": "C", "osi": "L7", "art": "🧨", "color": "R"},
    "phishing_maestro": {"name": "Phishing Maestro", "type": "Agent", "cost": {"R": 1, "B": 1}, "atk": 2, "hp": 2, "text": "Ao entrar, causa 1 de dano ao oponente.", "flavor": "Clique errado, noite longa.", "rarity": "U", "osi": "L7", "art": "🎣", "color": "B", "on_play": "ping_opponent"},
    "zero_day_hunter": {"name": "Zero Day Hunter", "type": "Agent", "cost": {"R": 2}, "atk": 3, "hp": 2, "text": "Pressao ofensiva direta.", "flavor": "Uma janela curta muda toda a partida.", "rarity": "U", "osi": "L3", "art": "🕳️", "color": "R"},
    "apt_operative": {"name": "APT Operative", "type": "Agent", "cost": {"B": 2, "R": 1}, "atk": 2, "hp": 3, "text": "Dificil de rastrear e remover.", "flavor": "Nao corre. Infiltra.", "rarity": "R", "osi": "L5", "art": "🥷", "color": "B"},
    "botnet_commander": {"name": "Botnet Commander", "type": "Agent", "cost": {"R": 2, "G": 1}, "atk": 4, "hp": 3, "text": "Todos os seus Agents ganham +1 ATK neste turno.", "flavor": "Escala e sincroniza o caos.", "rarity": "R", "osi": "L4", "art": "🤖", "color": "G", "on_play": "buff_all_attack"},
    "sql_injection": {"name": "SQL Injection", "type": "Exploit", "cost": {"R": 2}, "text": "Causa 3 de dano ao Agent inimigo; se nao houver, causa ao oponente.", "flavor": "Um campo sem filtro vira porta aberta.", "rarity": "U", "osi": "L7", "art": "💉", "color": "R", "spell": "damage_3"},
    "cve_critical": {"name": "CVE Critical", "type": "Exploit", "cost": {"R": 2, "B": 1}, "text": "Destroi um Agent inimigo com HP 3 ou menos.", "flavor": "Divulgacao publica, impacto imediato.", "rarity": "R", "osi": "L3", "art": "📛", "color": "B", "spell": "destroy_small"},
    "arp_poison": {"name": "ARP Poison", "type": "Script", "cost": {"R": 1}, "text": "Seu Agent com maior ATK recebe +2/+0 ate o fim do turno.", "flavor": "Confundir caminho e dominar segmento.", "rarity": "C", "osi": "L2", "art": "☣️", "color": "R", "spell": "boost_attack"},
    "rootkit": {"name": "Rootkit", "type": "Malware", "cost": {"B": 2, "R": 1}, "text": "Ao entrar, compre 1 carta.", "flavor": "Presenca silenciosa, impacto continuo.", "rarity": "R", "osi": "L5", "art": "🕶️", "color": "B", "on_play": "draw_1"},
    "soc_analyst": {"name": "SOC Analyst", "type": "Agent", "cost": {"U": 1}, "atk": 1, "hp": 3, "text": "Defensor de linha inicial.", "flavor": "Quem monitora cedo, responde melhor.", "rarity": "C", "osi": "L7", "art": "🛡️", "color": "U"},
    "siem_monitor": {"name": "SIEM Monitor", "type": "Agent", "cost": {"U": 2}, "atk": 1, "hp": 4, "text": "Ao entrar, compre 1 carta.", "flavor": "Log sem contexto e ruido.", "rarity": "U", "osi": "L3", "art": "📡", "color": "U", "on_play": "draw_1"},
    "threat_hunter": {"name": "Threat Hunter", "type": "Agent", "cost": {"U": 2, "W": 1}, "atk": 2, "hp": 3, "text": "Ao entrar, destrua um Malware inimigo.", "flavor": "Cacar o invisivel exige disciplina.", "rarity": "R", "osi": "L5", "art": "🛰️", "color": "U", "on_play": "destroy_enemy_malware"},
    "waf_guardian": {"name": "WAF Guardian", "type": "Agent", "cost": {"W": 2, "U": 1}, "atk": 1, "hp": 6, "text": "Parede robusta para proteger vida.", "flavor": "Nem tudo precisa cair para entrar.", "rarity": "R", "osi": "L7", "art": "🧱", "color": "W"},
    "incident_responder": {"name": "Incident Responder", "type": "Agent", "cost": {"U": 2, "W": 1}, "atk": 2, "hp": 4, "text": "Ao entrar, voce ganha 2 de vida.", "flavor": "Conter, erradicar, recuperar.", "rarity": "U", "osi": "L4", "art": "🚑", "color": "W", "on_play": "gain_2_life"},
    "patch_deployed": {"name": "Patch Deployed", "type": "Script", "cost": {"U": 2}, "text": "Destroi Agent inimigo com ATK 2 ou menos.", "flavor": "Correcoes simples evitam crises caras.", "rarity": "C", "osi": "L3", "art": "🩹", "color": "U", "spell": "destroy_weak_attack"},
    "firewall_rule": {"name": "Firewall Rule", "type": "Script", "cost": {"U": 1}, "text": "Vira um Agent inimigo. Ele nao ataca neste turno.", "flavor": "Negar trafego tambem e estrategia.", "rarity": "C", "osi": "L4", "art": "🔥", "color": "U", "spell": "tap_enemy"},
    "honeypot_network": {"name": "Honeypot Network", "type": "Tool", "cost": {"U": 2, "W": 1}, "text": "Ao entrar, compre 1 carta e ganhe 1 vida.", "flavor": "Armadilha boa gera inteligencia.", "rarity": "R", "osi": "L2", "art": "🍯", "color": "W", "on_play": "draw_1_gain_1"},
    "mfa_enforcement": {"name": "MFA Enforcement", "type": "Tool", "cost": {"W": 2}, "text": "Seus Agents recebem +0/+1.", "flavor": "Uma camada a mais muda a equacao.", "rarity": "U", "osi": "L5", "art": "🔒", "color": "W", "on_play": "buff_all_hp"},
    "lateral_movement": {"name": "Lateral Movement", "type": "Script", "cost": {"R": 1}, "text": "Seu Agent com maior ATK recebe +2/+0 ate o fim do turno.", "flavor": "Movimento lateral transforma acesso em dominio.", "rarity": "C", "osi": "L3", "art": "🧭", "color": "R", "spell": "boost_attack"},
    "credential_dumper": {"name": "Credential Dumper", "type": "Malware", "cost": {"B": 1, "R": 1}, "atk": 2, "hp": 2, "text": "Ao entrar, causa 1 de dano ao oponente.", "flavor": "Credenciais vazadas aceleram escalacao.", "rarity": "U", "osi": "L5", "art": "🗝️", "color": "B", "on_play": "ping_opponent"},
    "dns_tunneler": {"name": "DNS Tunneler", "type": "Agent", "cost": {"R": 1, "B": 1}, "atk": 2, "hp": 3, "text": "Especialista em exfiltracao por canais discretos.", "flavor": "Quando parece DNS normal, talvez nao seja.", "rarity": "U", "osi": "L3", "art": "🛰", "color": "B"},
    "c2_beacon": {"name": "C2 Beacon", "type": "Tool", "cost": {"B": 2}, "text": "Ao entrar, causa 1 de dano ao oponente.", "flavor": "Um unico beacon ja basta para coordenar a ofensiva.", "rarity": "U", "osi": "L4", "art": "📍", "color": "B", "on_play": "ping_opponent"},
    "ransom_encryptor": {"name": "Ransom Encryptor", "type": "Malware", "cost": {"R": 2, "B": 1}, "atk": 3, "hp": 2, "text": "Pressao alta para forcar resposta imediata.", "flavor": "Primeiro cifra, depois negocia.", "rarity": "R", "osi": "L6", "art": "💀", "color": "R"},
    "privilege_escalation": {"name": "Privilege Escalation", "type": "Exploit", "cost": {"R": 2}, "text": "Seu Agent com maior ATK recebe +2/+0 ate o fim do turno.", "flavor": "Um salto de privilegio pode decidir a rodada.", "rarity": "U", "osi": "L5", "art": "⬆️", "color": "R", "spell": "boost_attack"},
    "edr_sentinel": {"name": "EDR Sentinel", "type": "Agent", "cost": {"U": 1, "W": 1}, "atk": 2, "hp": 3, "text": "Ao entrar, destrua um Malware inimigo.", "flavor": "Telemetria e acao em ciclo curto.", "rarity": "R", "osi": "L5", "art": "👁️", "color": "U", "on_play": "destroy_enemy_malware"},
    "soar_automation": {"name": "SOAR Automation", "type": "Tool", "cost": {"U": 2}, "text": "Ao entrar, compre 1 carta.", "flavor": "Orquestrar rapido reduz janela de ataque.", "rarity": "U", "osi": "L4", "art": "⚙️", "color": "U", "on_play": "draw_1"},
    "threat_intel_feed": {"name": "Threat Intel Feed", "type": "Script", "cost": {"U": 1}, "text": "Compre 1 carta.", "flavor": "Contexto certo no minuto certo vale ouro.", "rarity": "C", "osi": "L7", "art": "📰", "color": "U", "spell": "draw_1"},
    "quarantine_vlan": {"name": "Quarantine VLAN", "type": "Script", "cost": {"U": 1, "W": 1}, "text": "Vira um Agent inimigo. Ele nao ataca neste turno.", "flavor": "Isolar rapido limita propagacao.", "rarity": "U", "osi": "L2", "art": "🧪", "color": "W", "spell": "tap_enemy"},
    "forensic_specialist": {"name": "Forensic Specialist", "type": "Agent", "cost": {"U": 2}, "atk": 1, "hp": 4, "text": "Especialista em trilha de evidencias e resposta.", "flavor": "Sem forense, repetimos os mesmos erros.", "rarity": "U", "osi": "L6", "art": "🔬", "color": "U"},
    "backup_restore": {"name": "Backup Restore", "type": "Tool", "cost": {"W": 2}, "text": "Ao entrar, compre 1 carta e ganhe 1 vida.", "flavor": "Recuperar rapido e metade da defesa.", "rarity": "U", "osi": "L7", "art": "💾", "color": "W", "on_play": "draw_1_gain_1"},
    "edge_sensor_grid": {"name": "Edge Sensor Grid", "type": "Node", "cost": {}, "produce": "U", "text": "Gera 1 mana U.", "flavor": "Sensores na borda encurtam o tempo de deteccao.", "rarity": "C", "osi": "L2", "art": "📶", "color": "U"},
    "dark_fiber_link": {"name": "Dark Fiber Link", "type": "Node", "cost": {}, "produce": "B", "text": "Gera 1 mana B.", "flavor": "Canal opaco para trafego dificil de inspecionar.", "rarity": "C", "osi": "L1", "art": "🕸️", "color": "B"},
    "zero_trust_segment": {"name": "Zero Trust Segment", "type": "Tool", "cost": {"W": 1, "U": 1}, "text": "Seus Agents recebem +0/+1.", "flavor": "Confianca minima, verificacao maxima.", "rarity": "U", "osi": "L4", "art": "🧱", "color": "W", "on_play": "buff_all_hp"},
    "vulnerability_scanner": {"name": "Vulnerability Scanner", "type": "Agent", "cost": {"U": 1}, "atk": 1, "hp": 2, "text": "Mapeia superficies de ataque com precisao.", "flavor": "Quem encontra primeiro corrige primeiro.", "rarity": "C", "osi": "L7", "art": "🧰", "color": "U"},
    "incident_timeline": {"name": "Incident Timeline", "type": "Script", "cost": {"C": 1}, "text": "Compre 1 carta, depois descarte 1 carta aleatoria.", "flavor": "Entender a sequencia evita reincidencia.", "rarity": "C", "osi": "L6", "art": "🗂️", "color": "C", "spell": "loot_1"},
    "secure_bastion": {"name": "Secure Bastion", "type": "Agent", "cost": {"W": 1}, "atk": 1, "hp": 3, "text": "Defensor resiliente para segurar o frontline.", "flavor": "Fortificar cedo reduz dano acumulado.", "rarity": "C", "osi": "L4", "art": "🏰", "color": "W"},
}

RED_DECK_BASE = [
    "node_l1", "node_l2", "node_l3", "node_l4", "node_l5", "node_l6", "node_l7",
    "dark_fiber_link", "node_l3", "node_l4",
    "script_kiddie", "script_kiddie", "phishing_maestro", "phishing_maestro", "zero_day_hunter", "zero_day_hunter",
    "apt_operative", "botnet_commander", "dns_tunneler", "credential_dumper", "c2_beacon", "ransom_encryptor",
    "sql_injection", "sql_injection", "cve_critical", "arp_poison", "lateral_movement", "privilege_escalation",
    "rootkit", "rootkit", "script_kiddie", "zero_day_hunter", "phishing_maestro", "apt_operative", "arp_poison",
]

BLUE_DECK_BASE = [
    "node_l1", "node_l2", "node_l3", "node_l4", "node_l5", "node_l6", "node_l7",
    "edge_sensor_grid", "node_l2", "node_l6",
    "soc_analyst", "soc_analyst", "siem_monitor", "siem_monitor", "threat_hunter", "waf_guardian",
    "incident_responder", "patch_deployed", "patch_deployed", "firewall_rule", "firewall_rule",
    "honeypot_network", "mfa_enforcement", "edr_sentinel", "soar_automation", "threat_intel_feed", "quarantine_vlan",
    "forensic_specialist", "backup_restore", "zero_trust_segment", "vulnerability_scanner", "incident_timeline", "secure_bastion",
    "threat_hunter", "incident_responder", "siem_monitor", "patch_deployed", "honeypot_network", "soc_analyst",
]

AI_TAUNTS = [
    "Sua curva de mana ficou previsivel.",
    "Nao e sorte. E leitura de padrao.",
    "Seu battlefield esta aberto demais.",
    "Cada turno deixa rastros.",
]

OSI_LAYERS = ["L1", "L2", "L3", "L4", "L5", "L6", "L7"]

ATTACK_GUIDE = {
    "L1": "Ataque de base fisica e canais de transporte para abrir acesso inicial.",
    "L2": "Manipule enlace e segmentacao para ampliar movimento lateral.",
    "L3": "Explore roteamento e pontos de passagem para romper fronteiras de rede.",
    "L4": "Pressione servicos e sessoes de transporte para reduzir disponibilidade.",
    "L5": "Capture contexto de sessao e autenticacao para ganhar persistencia.",
    "L6": "Mire em criptografia e transformacao de dados para criar pontos cegos.",
    "L7": "Ataque aplicacao e superficie humana para impacto direto no negocio.",
}

DEFENSE_GUIDE = {
    "L1": "Fortaleça ativos fisicos e redundancia de conectividade.",
    "L2": "Use segmentacao e isolamento para conter propagacao de ameacas.",
    "L3": "Reforce bordas, rotas e controle de trafego para bloquear avancos.",
    "L4": "Aplique firewall e politicas de transporte para reduzir janela de ataque.",
    "L5": "Proteja sessao e identidade com validacoes continuas.",
    "L6": "Padronize criptografia e integridade de dados para reduzir exposicao.",
    "L7": "Eleve hardening de app, monitoramento e resposta ao usuario final.",
}

OSI_LAYER_EXAMPLES = {
    "L1": {
        "hardware": "cabos, fibra optica, transceivers, patch panel",
        "protocolos": "Ethernet fisico (1000BASE-T), sinais opticos",
    },
    "L2": {
        "hardware": "switches, bridges, NICs",
        "protocolos": "Ethernet (802.3), VLAN (802.1Q), ARP",
    },
    "L3": {
        "hardware": "roteadores, gateways L3",
        "protocolos": "IPv4/IPv6, ICMP, OSPF/BGP",
    },
    "L4": {
        "hardware": "firewalls stateful, load balancers",
        "protocolos": "TCP, UDP, QUIC",
    },
    "L5": {
        "hardware": "servidores de sessao, proxies de autenticacao",
        "protocolos": "TLS session resumption, NetBIOS session",
    },
    "L6": {
        "hardware": "HSM, appliances de criptografia",
        "protocolos": "TLS/SSL, formatos de criptografia e codificacao",
    },
    "L7": {
        "hardware": "WAF, API gateways, servidores de aplicacao",
        "protocolos": "HTTP/HTTPS, DNS, SMTP, APIs REST",
    },
}


def ts() -> str:
    return datetime.now().strftime("%H:%M:%S")


def add_log(text: str, style: str = "info") -> None:
    st.session_state.logs_card.append({"ts": ts(), "text": text, "style": style})
    if len(st.session_state.logs_card) > 220:
        st.session_state.logs_card = st.session_state.logs_card[-220:]


def style_to_color(style: str) -> str:
    colors = {
        "ok": "#90f2ba",
        "err": "#ff9d9d",
        "warn": "#ffd37a",
        "info": "#e8d4ad",
        "ai": "#b9b7ff",
        "data": "#7fd8ff",
    }
    return colors.get(style, "#e8d4ad")


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


def provider_uses_openai_compatible(provider: str) -> bool:
    return provider in ("OpenAI", "OpenAI Compatible", "Ollama", "LM Studio", "vLLM")


def provider_requires_api_key(provider: str) -> bool:
    return provider not in ("Local Offline", "Ollama", "LM Studio", "vLLM")


GEMINI_MODEL_FALLBACKS = (
    "gemini-2.5-flash",
    "gemini-2.5-flash-lite",
    "gemini-1.5-flash",
)


def gemini_model_candidates(model: str) -> list[str]:
    preferred = normalize_gemini_model_name(model)
    ordered: list[str] = []
    if preferred:
        ordered.append(preferred)
    for candidate in GEMINI_MODEL_FALLBACKS:
        if candidate not in ordered:
            ordered.append(candidate)
    return ordered


def is_gemini_model_deprecated_error(http_code: int, body: str) -> bool:
    if http_code != 404:
        return False
    lowered = body.lower()
    return (
        "no longer available" in lowered
        or '"status": "not_found"' in lowered
        or '"status":"not_found"' in lowered
    )


def provider_defaults(provider: str) -> tuple[str, str]:
    local_host = "host.docker.internal" if os.path.exists("/.dockerenv") else "localhost"
    defaults: dict[str, tuple[str, str]] = {
        "Local Offline": ("", ""),
        "OpenAI": ("gpt-4o-mini", "https://api.openai.com/v1/chat/completions"),
        "Gemini": ("gemini-2.5-flash", "https://generativelanguage.googleapis.com/v1beta/models"),
        "OpenAI Compatible": ("gpt-4o-mini", "https://api.openai.com/v1/chat/completions"),
        "Ollama": ("llama3.1:8b", f"http://{local_host}:11434/v1/chat/completions"),
        "LM Studio": ("local-model", "http://localhost:1234/v1/chat/completions"),
        "vLLM": ("meta-llama/Llama-3.1-8B-Instruct", "http://localhost:8000/v1/chat/completions"),
    }
    return defaults.get(provider, ("gpt-4o-mini", "https://api.openai.com/v1/chat/completions"))


def normalize_openai_endpoint(provider: str, endpoint: str) -> str:
    clean = endpoint.strip().rstrip("/")
    if not clean:
        return clean

    # Permite colar base URL (/v1) sem obrigar caminho completo.
    if clean.endswith("/v1"):
        clean = clean + "/chat/completions"

    # Em dev container, localhost aponta para o proprio container.
    if provider == "Ollama" and os.path.exists("/.dockerenv"):
        clean = clean.replace("http://localhost:", "http://host.docker.internal:")
        clean = clean.replace("http://127.0.0.1:", "http://host.docker.internal:")

    return clean


def is_likely_valid_api_key(provider: str, api_key: str) -> bool:
    if not api_key:
        return False
    if len(api_key) > 200:
        return False
    if provider == "Gemini":
        return api_key.startswith("AIza") and bool(re.match(r"^[A-Za-z0-9_\-.]+$", api_key))
    return bool(re.match(r"^[A-Za-z0-9_\-.]+$", api_key))


def call_openai_compatible(
    endpoint: str,
    api_key: str,
    model: str,
    messages: list[dict[str, str]],
    temperature: float = 0.35,
    max_tokens: int = 220,
    provider: str = "",
) -> str:
    payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    data = json.dumps(payload).encode("utf-8")

    endpoints_to_try = [endpoint]
    if provider == "Ollama":
        base = endpoint.strip()
        candidates = [
            base,
            base.replace("host.docker.internal", "172.17.0.1"),
            base.replace("host.docker.internal", "172.18.0.1"),
            base.replace("localhost", "172.17.0.1"),
            base.replace("127.0.0.1", "172.17.0.1"),
            base.replace("localhost", "host.docker.internal"),
            base.replace("127.0.0.1", "host.docker.internal"),
        ]
        # Preserva ordem e remove duplicados.
        seen = set()
        endpoints_to_try = []
        for item in candidates:
            if item and item not in seen:
                endpoints_to_try.append(item)
                seen.add(item)

    raw = None
    last_exc: Exception | None = None
    for candidate_endpoint in endpoints_to_try:
        try:
            req = urllib.request.Request(candidate_endpoint, data=data, method="POST")
            req.add_header("Content-Type", "application/json")
            if api_key:
                req.add_header("Authorization", f"Bearer {api_key}")
            with urllib.request.urlopen(req, timeout=20) as resp:
                raw = resp.read().decode("utf-8")
            break
        except Exception as exc:
            last_exc = exc

    if raw is None:
        if last_exc:
            raise last_exc
        raise RuntimeError("Falha ao obter resposta do endpoint de IA")

    parsed = json.loads(raw)
    return parsed["choices"][0]["message"]["content"].strip()


def call_gemini_generate_content(api_key: str, model: str, prompt: str) -> str:
    safe_key = urllib.parse.quote_plus(api_key)
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": 0.3, "maxOutputTokens": 180},
    }
    data = json.dumps(payload).encode("utf-8")

    last_exc: Exception | None = None
    for model_name in gemini_model_candidates(model):
        endpoint = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={safe_key}"
        req = urllib.request.Request(endpoint, data=data, method="POST")
        req.add_header("Content-Type", "application/json")

        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                raw = resp.read().decode("utf-8")
            break
        except urllib.error.HTTPError as exc:
            body = ""
            try:
                body = exc.read().decode("utf-8", errors="ignore")
            except Exception:
                body = ""
            if is_gemini_model_deprecated_error(getattr(exc, "code", 0), body):
                last_exc = exc
                continue
            raise
        except Exception as exc:
            last_exc = exc
            raise
    else:
        if last_exc:
            raise last_exc
        raise RuntimeError("Falha ao obter resposta do Gemini")

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


def test_ai_connection(provider: str, model: str, endpoint: str, api_key: str) -> tuple[bool, str]:
    if provider == "Local Offline":
        return True, "Modo Local Offline ativo. A IA local da partida esta pronta para uso."

    clean_model = model.strip()
    clean_endpoint = normalize_openai_endpoint(provider, endpoint)
    clean_key = sanitize_api_key(api_key)

    if not clean_model:
        return False, "Informe o modelo antes de testar."
    if provider_requires_api_key(provider):
        if not clean_key:
            return False, "Informe a API Key para testar este provedor."
        if not is_likely_valid_api_key(provider, clean_key):
            return False, "API Key em formato invalido para o provedor selecionado."
    if provider_uses_openai_compatible(provider) and not clean_endpoint:
        return False, "Informe o endpoint para o teste do provedor selecionado."

    prompt = "Responda somente com a frase: Conexao IA OK"
    try:
        if provider_uses_openai_compatible(provider):
            answer = call_openai_compatible(
                endpoint=clean_endpoint,
                api_key=clean_key,
                model=clean_model,
                messages=[
                    {"role": "system", "content": "Teste rapido de conectividade."},
                    {"role": "user", "content": prompt},
                ],
                temperature=0,
                max_tokens=30,
                provider=provider,
            )
        elif provider == "Gemini":
            answer = call_gemini_generate_content(
                api_key=clean_key,
                model=clean_model,
                prompt=prompt,
            )
        else:
            return False, "Provedor nao suportado para teste."

        answer = answer.strip().replace("\n", " ")
        if not answer:
            return False, "Conexao realizada, mas o modelo retornou resposta vazia."
        return True, f"Teste OK. Resposta do modelo: {answer[:140]}"
    except urllib.error.HTTPError as exc:
        try:
            body = exc.read().decode("utf-8", errors="ignore")
            body = re.sub(r"\s+", " ", body).strip()
        except Exception:
            body = ""
        detail = f" HTTP {exc.code}." if hasattr(exc, "code") else ""
        if body:
            return False, f"Falha no teste de IA.{detail} Detalhe: {body[:220]}"
        return False, f"Falha no teste de IA.{detail}"
    except Exception as exc:
        return False, f"Falha no teste de IA: {str(exc)[:220]}"


def mana_to_str(cost: dict[str, int]) -> str:
    if not cost:
        return "0"
    order = ["W", "U", "B", "R", "G", "C"]
    chunks = []
    for m in order:
        if m in cost:
            chunks.append(f"{cost[m]}{m}")
    return " ".join(chunks)


def make_permanent(card_id: str) -> dict[str, Any]:
    card = CARD_DB[card_id]
    return {
        "uid": f"{card_id}_{random.randint(1000, 9999)}",
        "card_id": card_id,
        "tapped": False,
        "summon_sick": card["type"] == "Agent",
        "atk": card.get("atk", 0),
        "hp": card.get("hp", 0),
        "max_hp": card.get("hp", 0),
        "temp_atk": 0,
    }


def get_game() -> dict[str, Any]:
    return st.session_state.card_game


def side_to_label(side: str) -> str:
    return "Jogador" if side == "player" else "IA"


def opposite(side: str) -> str:
    return "ai" if side == "player" else "player"


def deck_for_team(team: str) -> list[str]:
    return list(RED_DECK_BASE if team == "red" else BLUE_DECK_BASE)


def empty_mana_pool() -> dict[str, int]:
    return {"W": 0, "U": 0, "B": 0, "R": 0, "G": 0, "C": 0}


def can_pay(pool: dict[str, int], cost: dict[str, int]) -> bool:
    for c, v in cost.items():
        if pool.get(c, 0) < v:
            return False
    return True


def pay_cost(pool: dict[str, int], cost: dict[str, int]) -> None:
    for c, v in cost.items():
        pool[c] -= v


def gain_mana_from_nodes(board: list[dict[str, Any]]) -> dict[str, int]:
    pool = empty_mana_pool()
    for perm in board:
        card = CARD_DB[perm["card_id"]]
        if card["type"] == "Node":
            produced = card.get("produce", "C")
            pool[produced] += 1
    return pool


def draw_card(side: str, n: int = 1) -> None:
    game = get_game()
    deck_key = f"deck_{side}"
    hand_key = f"hand_{side}"
    for _ in range(n):
        if not game[deck_key]:
            game["ended"] = True
            game["winner"] = opposite(side)
            add_log(f"{side_to_label(side)} ficou sem cartas para comprar.", "warn")
            return
        game[hand_key].append(game[deck_key].pop(0))


def remove_dead(board: list[dict[str, Any]], grave: list[str]) -> None:
    alive = []
    for perm in board:
        card = CARD_DB[perm["card_id"]]
        if card["type"] == "Agent" and perm["hp"] <= 0:
            grave.append(perm["card_id"])
        else:
            alive.append(perm)
    board[:] = alive


def destroy_enemy_malware(owner: str) -> None:
    game = get_game()
    enemy = opposite(owner)
    board_key = f"board_{enemy}"
    grave_key = f"grave_{enemy}"
    for idx, perm in enumerate(game[board_key]):
        c = CARD_DB[perm["card_id"]]
        if c["type"] == "Malware":
            dead = game[board_key].pop(idx)
            game[grave_key].append(dead["card_id"])
            add_log(f"{side_to_label(owner)} removeu malware inimigo: {c['name']}", "ok")
            return


def apply_on_play(side: str, card: dict[str, Any]) -> None:
    game = get_game()
    on_play = card.get("on_play")
    if on_play == "ping_opponent":
        game[f"life_{opposite(side)}"] -= 1
    elif on_play == "buff_all_attack":
        for perm in game[f"board_{side}"]:
            c = CARD_DB[perm["card_id"]]
            if c["type"] == "Agent":
                perm["temp_atk"] += 1
    elif on_play == "draw_1":
        draw_card(side, 1)
    elif on_play == "gain_2_life":
        game[f"life_{side}"] += 2
    elif on_play == "draw_1_gain_1":
        draw_card(side, 1)
        game[f"life_{side}"] += 1
    elif on_play == "buff_all_hp":
        for perm in game[f"board_{side}"]:
            c = CARD_DB[perm["card_id"]]
            if c["type"] == "Agent":
                perm["hp"] += 1
                perm["max_hp"] += 1
    elif on_play == "destroy_enemy_malware":
        destroy_enemy_malware(side)


def spell_damage_3(side: str) -> None:
    game = get_game()
    enemy = opposite(side)
    board = game[f"board_{enemy}"]
    targets = [p for p in board if CARD_DB[p["card_id"]]["type"] == "Agent"]
    if targets:
        target = max(targets, key=lambda x: x["atk"])
        target["hp"] -= 3
        add_log(f"{side_to_label(side)} causou 3 de dano a {CARD_DB[target['card_id']]['name']}", "info")
    else:
        game[f"life_{enemy}"] -= 3
        add_log(f"{side_to_label(side)} causou 3 de dano direto.", "info")


def spell_destroy_small(side: str) -> None:
    game = get_game()
    enemy = opposite(side)
    board_key = f"board_{enemy}"
    grave_key = f"grave_{enemy}"
    for idx, perm in enumerate(game[board_key]):
        card = CARD_DB[perm["card_id"]]
        if card["type"] == "Agent" and perm["hp"] <= 3:
            dead = game[board_key].pop(idx)
            game[grave_key].append(dead["card_id"])
            add_log(f"{side_to_label(side)} destruiu {card['name']}.", "ok")
            return


def spell_boost_attack(side: str) -> None:
    game = get_game()
    agents = [p for p in game[f"board_{side}"] if CARD_DB[p["card_id"]]["type"] == "Agent"]
    if not agents:
        return
    best = max(agents, key=lambda x: x["atk"])
    best["temp_atk"] += 2
    add_log(f"{side_to_label(side)} reforcou ataque de {CARD_DB[best['card_id']]['name']}.", "info")


def spell_destroy_weak_attack(side: str) -> None:
    game = get_game()
    enemy = opposite(side)
    board_key = f"board_{enemy}"
    grave_key = f"grave_{enemy}"
    for idx, perm in enumerate(game[board_key]):
        card = CARD_DB[perm["card_id"]]
        if card["type"] == "Agent" and perm["atk"] <= 2:
            dead = game[board_key].pop(idx)
            game[grave_key].append(dead["card_id"])
            add_log(f"{side_to_label(side)} removeu {card['name']} com patch defensivo.", "ok")
            return


def spell_tap_enemy(side: str) -> None:
    game = get_game()
    enemy = opposite(side)
    for perm in game[f"board_{enemy}"]:
        card = CARD_DB[perm["card_id"]]
        if card["type"] == "Agent" and not perm["tapped"]:
            perm["tapped"] = True
            add_log(f"{side_to_label(side)} travou {card['name']} com regra de firewall.", "warn")
            return


def spell_draw_1(side: str) -> None:
    draw_card(side, 1)
    add_log(f"{side_to_label(side)} comprou 1 carta.", "info")


def spell_loot_1(side: str) -> None:
    game = get_game()
    draw_card(side, 1)
    hand_key = f"hand_{side}"
    if game[hand_key]:
        discard_idx = random.randrange(len(game[hand_key]))
        discarded = game[hand_key].pop(discard_idx)
        game[f"grave_{side}"].append(discarded)
        add_log(f"{side_to_label(side)} refinou a mao e descartou {CARD_DB[discarded]['name']}.", "info")


def cast_spell(side: str, card: dict[str, Any]) -> None:
    spell = card.get("spell", "")
    if spell == "damage_3":
        spell_damage_3(side)
    elif spell == "destroy_small":
        spell_destroy_small(side)
    elif spell == "boost_attack":
        spell_boost_attack(side)
    elif spell == "destroy_weak_attack":
        spell_destroy_weak_attack(side)
    elif spell == "tap_enemy":
        spell_tap_enemy(side)
    elif spell == "draw_1":
        spell_draw_1(side)
    elif spell == "loot_1":
        spell_loot_1(side)


def check_endgame() -> None:
    game = get_game()
    if game["ended"]:
        return

    winner = None
    if game["life_player"] <= 0 and game["life_ai"] <= 0:
        winner = "draw"
    elif game["life_player"] <= 0:
        winner = "ai"
    elif game["life_ai"] <= 0:
        winner = "player"
    elif game["turn"] > game["max_turns"]:
        if game["life_player"] > game["life_ai"]:
            winner = "player"
        elif game["life_player"] < game["life_ai"]:
            winner = "ai"
        else:
            winner = "draw"

    if winner:
        game["ended"] = True
        game["winner"] = winner
        announce_endgame_story(game)


def build_endgame_story(game: dict[str, Any]) -> str:
    life_player = game.get("life_player", 0)
    life_ai = game.get("life_ai", 0)
    turn = game.get("turn", "?")
    winner = game.get("winner")

    recent_logs = [entry["text"] for entry in st.session_state.logs_card[-8:] if isinstance(entry, dict) and "text" in entry]
    events = _sanitize_story_events(recent_logs)
    highlights = " ".join(f"{evt}." for evt in events[-3:]) if events else "Os ultimos movimentos foram rapidos e decisivos."

    if winner == "player":
        opening = "Vitoria confirmada para o comandante humano"
        closing = "A ofensiva foi bem dosada e a pressao final quebrou a defesa da IA no momento certo."
    elif winner == "ai":
        opening = "A IA venceu a operacao e assumiu controle da arena"
        closing = "A resposta automatizada manteve consistencia tática e neutralizou as janelas de contra-ataque do jogador."
    else:
        opening = "Empate tecnico na arena"
        closing = "Nenhum lado conseguiu vantagem suficiente antes do limite de turnos, encerrando a disputa em equilibrio."

    return (
        f"{opening} no turno {turn}. Placar final de integridade: Jogador {life_player} x IA {life_ai}. "
        f"Momentos decisivos: {highlights} {closing}"
    )


def announce_endgame_story(game: dict[str, Any]) -> None:
    if game.get("end_story_announced"):
        return

    final_story = _sanitize_story_text(build_endgame_story(game))
    game["last_story"] = final_story
    game["story_history"].append(
        {
            "turn": game.get("turn"),
            "story": final_story,
            "life_player": game.get("life_player"),
            "life_ai": game.get("life_ai"),
            "kind": "endgame",
        }
    )
    add_log(f"[Narrador] {final_story}", "ai")
    game["end_story_announced"] = True


def begin_turn(side: str) -> None:
    game = get_game()
    game["active_side"] = side
    game["phase"] = "main"
    game[f"nodes_played_turn_{side}"] = 0

    for perm in game[f"board_{side}"]:
        perm["tapped"] = False
        if perm["summon_sick"]:
            perm["summon_sick"] = False
        perm["temp_atk"] = 0

    game[f"mana_{side}"] = gain_mana_from_nodes(game[f"board_{side}"])
    draw_card(side, 1)
    add_log(f"Turno de {side_to_label(side)}: mana {game[f'mana_{side}']}", "info")
    if side == "player":
        game["turn_log_start"] = max(0, len(st.session_state.logs_card) - 1)


def playable_cards(side: str) -> list[int]:
    game = get_game()
    result = []
    for idx, card_id in enumerate(game[f"hand_{side}"]):
        card = CARD_DB[card_id]
        if card["type"] == "Node" and game[f"nodes_played_turn_{side}"] >= 1:
            continue
        if card["type"] != "Node" and not can_pay(game[f"mana_{side}"], card.get("cost", {})):
            continue
        result.append(idx)
    return result


def play_card(side: str, hand_index: int) -> bool:
    game = get_game()
    if game["ended"]:
        return False
    if game["active_side"] != side or game["phase"] != "main":
        return False

    hand = game[f"hand_{side}"]
    if hand_index < 0 or hand_index >= len(hand):
        return False

    card_id = hand[hand_index]
    card = CARD_DB[card_id]
    cost_txt = mana_to_str(card.get("cost", {}))

    if card["type"] == "Node":
        if game[f"nodes_played_turn_{side}"] >= 1:
            return False
        hand.pop(hand_index)
        game[f"board_{side}"].append(make_permanent(card_id))
        game[f"nodes_played_turn_{side}"] += 1
        add_log(
            f"{side_to_label(side)} baixou Node: {card['name']} e reforcou sua base de recursos.",
            "ok",
        )
        return True

    if not can_pay(game[f"mana_{side}"], card.get("cost", {})):
        return False

    pay_cost(game[f"mana_{side}"], card.get("cost", {}))
    hand.pop(hand_index)

    if card["type"] in {"Agent", "Malware", "Tool"}:
        game[f"board_{side}"].append(make_permanent(card_id))
        add_log(
            f"{side_to_label(side)} conjurou {card['name']} (custo {cost_txt}) | Mana restante: {game[f'mana_{side}']}",
            "ok",
        )
        apply_on_play(side, card)
    else:
        add_log(
            f"{side_to_label(side)} usou {card['name']} (custo {cost_txt}) | Mana restante: {game[f'mana_{side}']}",
            "ok",
        )
        cast_spell(side, card)
        game[f"grave_{side}"].append(card_id)

    remove_dead(game["board_player"], game["grave_player"])
    remove_dead(game["board_ai"], game["grave_ai"])
    check_endgame()
    return True


def creature_indices(board: list[dict[str, Any]]) -> list[int]:
    idxs = []
    for i, perm in enumerate(board):
        c = CARD_DB[perm["card_id"]]
        if c["type"] == "Agent":
            idxs.append(i)
    return idxs


def combat(attacker_side: str, attacker_indices: list[int]) -> None:
    game = get_game()
    defender_side = opposite(attacker_side)
    atk_board = game[f"board_{attacker_side}"]
    def_board = game[f"board_{defender_side}"]
    add_log(
        f"{side_to_label(attacker_side)} iniciou combate com {len(attacker_indices)} atacante(s).",
        "data",
    )

    available_blockers = [i for i in creature_indices(def_board) if not def_board[i]["tapped"]]

    for atk_idx in attacker_indices:
        if atk_idx >= len(atk_board):
            continue
        attacker = atk_board[atk_idx]
        attacker_card = CARD_DB[attacker["card_id"]]
        if attacker_card["type"] != "Agent" or attacker["tapped"] or attacker["summon_sick"]:
            continue

        attack_value = max(0, attacker["atk"] + attacker.get("temp_atk", 0))
        attacker["tapped"] = True

        if available_blockers:
            blocker_idx = max(available_blockers, key=lambda i: def_board[i]["hp"])
            available_blockers.remove(blocker_idx)
            blocker = def_board[blocker_idx]
            blocker_card = CARD_DB[blocker["card_id"]]

            old_attacker_hp = attacker["hp"]
            old_blocker_hp = blocker["hp"]

            blocker["hp"] -= attack_value
            attacker["hp"] -= blocker["atk"]

            attacker_fell = attacker["hp"] <= 0
            blocker_fell = blocker["hp"] <= 0
            outcome_parts = []
            if blocker_fell:
                outcome_parts.append(f"{blocker_card['name']} foi neutralizado")
            if attacker_fell:
                outcome_parts.append(f"{attacker_card['name']} caiu na troca")
            outcome_txt = " | ".join(outcome_parts) if outcome_parts else "ambos permaneceram ativos"

            add_log(
                f"{attacker_card['name']} atacou {blocker_card['name']} | dano {attack_value} x {blocker['atk']} | HP {old_blocker_hp}->{blocker['hp']} e {old_attacker_hp}->{attacker['hp']} | {outcome_txt}.",
                "info",
            )
        else:
            game[f"life_{defender_side}"] -= attack_value
            add_log(
                f"{attacker_card['name']} rompeu a defesa e causou {attack_value} de dano direto em {side_to_label(defender_side)} (vida agora: {game[f'life_{defender_side}']}).",
                "warn",
            )

    remove_dead(game["board_player"], game["grave_player"])
    remove_dead(game["board_ai"], game["grave_ai"])
    add_log(f"Fim do combate: Vida Jogador {game['life_player']} | Vida IA {game['life_ai']}", "data")
    check_endgame()


def local_ai_play_actions() -> None:
    game = get_game()
    if game["ended"]:
        return

    for _ in range(3):
        playables = playable_cards("ai")
        if not playables:
            break

        hand = game["hand_ai"]
        node_option = None
        for idx in playables:
            if CARD_DB[hand[idx]]["type"] == "Node":
                node_option = idx
                break
        if node_option is not None:
            play_card("ai", node_option)
            continue

        # IA joga carta de maior custo total para pressionar curva.
        def card_weight(hidx: int) -> int:
            card = CARD_DB[hand[hidx]]
            return sum(card.get("cost", {}).values()) + card.get("atk", 0)

        best = max(playables, key=card_weight)
        if not play_card("ai", best):
            break

    ai_attackers = []
    for idx in creature_indices(game["board_ai"]):
        p = game["board_ai"][idx]
        if not p["tapped"] and not p["summon_sick"]:
            ai_attackers.append(idx)

    if ai_attackers:
        total = sum(max(0, game["board_ai"][i]["atk"] + game["board_ai"][i].get("temp_atk", 0)) for i in ai_attackers)
        if total >= 3 or game["life_ai"] <= 8 or random.random() > 0.35:
            combat("ai", ai_attackers)
            add_log(f"[IA] {random.choice(AI_TAUNTS)}", "ai")


def local_ai_decision() -> None:
    game = get_game()
    if game["ended"]:
        return

    begin_turn("ai")
    if game["ended"]:
        return
    local_ai_play_actions()


def request_llm_card_decision() -> dict[str, Any] | None:
    game = get_game()
    setup = game["setup"]
    provider = setup.get("provider", "Local Offline")
    if provider == "Local Offline":
        return None

    api_key = sanitize_api_key(setup.get("api_key", ""))
    model = setup.get("model", "").strip()
    endpoint = normalize_openai_endpoint(provider, setup.get("endpoint", ""))

    if not model:
        return None
    if provider_requires_api_key(provider):
        if not api_key:
            return None
        if not is_likely_valid_api_key(provider, api_key):
            return None
    if provider_uses_openai_compatible(provider) and not endpoint:
        return None

    payload = {
        "turn": game["turn"],
        "life_ai": game["life_ai"],
        "life_player": game["life_player"],
        "ai_mana": game["mana_ai"],
        "ai_hand": [CARD_DB[c]["name"] for c in game["hand_ai"]],
        "ai_board": [CARD_DB[p["card_id"]]["name"] for p in game["board_ai"]],
        "player_board": [CARD_DB[p["card_id"]]["name"] for p in game["board_player"]],
    }
    system_msg = (
        "Voce controla IA de card game. Responda apenas JSON com chaves: "
        "play_indexes (lista de ate 3 indices da mao) e attack_all (true/false)."
    )

    try:
        if provider_uses_openai_compatible(provider):
            answer = call_openai_compatible(
                endpoint=endpoint,
                api_key=api_key,
                model=model,
                messages=[
                    {"role": "system", "content": system_msg},
                    {"role": "user", "content": json.dumps(payload, ensure_ascii=False)},
                ],
                provider=provider,
            )
        elif provider == "Gemini":
            answer = call_gemini_generate_content(
                api_key=api_key,
                model=model,
                prompt=system_msg + "\n" + json.dumps(payload, ensure_ascii=False),
            )
        else:
            return None

        parsed = extract_json_block(answer)
        if not parsed:
            return None
        return parsed
    except Exception:
        return None


def ai_turn() -> None:
    game = get_game()
    if game["ended"]:
        return

    begin_turn("ai")
    if game["ended"]:
        return

    llm = request_llm_card_decision()
    if not llm:
        local_ai_play_actions()
        return

    play_indexes = llm.get("play_indexes", [])
    if not isinstance(play_indexes, list):
        local_ai_play_actions()
        return

    played = 0
    for idx in play_indexes:
        if played >= 3:
            break
        if isinstance(idx, int) and 0 <= idx < len(game["hand_ai"]):
            if play_card("ai", idx):
                played += 1

    # Fallback quando o LLM sugeriu jogadas mas nao conseguiu executar nenhuma.
    if play_indexes and played == 0:
        local_ai_play_actions()
        return

    if llm.get("attack_all", True):
        attackers = []
        for idx in creature_indices(game["board_ai"]):
            p = game["board_ai"][idx]
            if not p["tapped"] and not p["summon_sick"]:
                attackers.append(idx)
        if attackers:
            combat("ai", attackers)


def request_llm_turn_story(game: dict[str, Any], events: list[str]) -> str | None:
    setup = game["setup"]
    provider = setup.get("provider", "Local Offline")
    if provider == "Local Offline":
        return None

    api_key = sanitize_api_key(setup.get("api_key", ""))
    model = setup.get("model", "").strip()
    endpoint = normalize_openai_endpoint(provider, setup.get("endpoint", ""))

    if not model:
        return None
    if provider_requires_api_key(provider):
        if not api_key:
            return None
        if not is_likely_valid_api_key(provider, api_key):
            return None
    if provider_uses_openai_compatible(provider) and not endpoint:
        return None

    payload = {
        "turno": game["turn"],
        "contexto": {
            "time_jogador": game.get("player_team", "red").upper(),
            "time_ia": game.get("ai_team", "blue").upper(),
        },
        "eventos": events[-12:],
    }
    system_msg = (
        "Voce e narrador educacional de ciberseguranca em um jogo red team vs blue team. "
        "Escreva 1 unico paragrafo em portugues do Brasil (90 a 130 palavras), com tom de conto curto, "
        "explicando o que aconteceu com sistema e/ou usuario. "
        "Transforme os eventos em narrativa didatica: descreva ataque, impacto, resposta defensiva e uma licao pratica final. "
        "PROIBIDO citar status tecnicos crus, mana, custo, json, listas, placar numerico ou formato de log. "
        "Sem markdown."
    )

    try:
        if provider_uses_openai_compatible(provider):
            answer = call_openai_compatible(
                endpoint=endpoint,
                api_key=api_key,
                model=model,
                messages=[
                    {"role": "system", "content": system_msg},
                    {"role": "user", "content": json.dumps(payload, ensure_ascii=False)},
                ],
                temperature=0.7,
                max_tokens=180,
                provider=provider,
            )
        elif provider == "Gemini":
            answer = call_gemini_generate_content(
                api_key=api_key,
                model=model,
                prompt=system_msg + "\n" + json.dumps(payload, ensure_ascii=False),
            )
        else:
            return None

        return answer.strip().replace("\n", " ")
    except Exception:
        return None


def build_local_turn_story(game: dict[str, Any], events: list[str]) -> str:
    life_player = game.get("life_player", 0)
    life_ai = game.get("life_ai", 0)
    mana_player_total = sum(game.get("mana_player", {}).values())

    last_events = events[-3:] if events else []

    cast_events = [e for e in last_events if "conjurou" in e.lower() or "usou" in e.lower()]
    hit_events = [e for e in last_events if "rompeu a defesa" in e.lower() or "causou" in e.lower()]

    if life_player > life_ai:
        pressure = "o Time do Jogador fechou o turno com vantagem clara"
    elif life_player < life_ai:
        pressure = "a IA manteve o controle da pressao no fim da rodada"
    else:
        pressure = "os dois lados terminaram em equilibrio tatico"

    setup = game.get("setup", {})
    side_name = setup.get("side", "Red Team")
    enemy_name = "Blue Team" if side_name == "Red Team" else "Red Team"
    turn = game.get("turn", "?")

    prev_entry = game.get("story_history", [])[-1] if game.get("story_history") else {}
    prev_life_player = prev_entry.get("life_player")
    prev_life_ai = prev_entry.get("life_ai")
    life_changed = (prev_life_player != life_player) or (prev_life_ai != life_ai)

    opening = (
        f"No turno {turn}, a arena neon entrou em alerta: o {side_name} pressionou as linhas de defesa, "
        f"enquanto o {enemy_name} tentava segurar a infraestrutura critica."
    )

    if life_changed or prev_life_player is None or prev_life_ai is None:
        status_line = (
            f"No painel de status, a IA fechou com {life_ai} de vida e o Jogador com {life_player}; "
            f"a reserva tatica do Jogador ficou em {mana_player_total} de mana pronta."
        )
    else:
        status_line = (
            f"No painel de status, a integridade de vida se manteve estavel para os dois lados; "
            f"o Jogador encerrou com {mana_player_total} de mana pronta para o proximo ciclo."
        )

    if hit_events:
        highlights = " ".join(f"{evt}." for evt in hit_events)
    elif cast_events:
        highlights = " ".join(f"{evt}." for evt in cast_events)
    elif last_events:
        highlights = " ".join(f"{evt}." for evt in last_events)
    else:
        highlights = "Nesta rodada, nenhuma jogada decisiva foi registrada no log."

    closing = (
        f"No fim, {pressure}. Licao do turno: vantagem de recurso e ritmo de ataque "
        "decidem se voce domina a rede ou perde terreno no proximo ciclo."
    )

    return f"{opening} {status_line} {highlights} {closing}"


def _sanitize_story_events(events: list[str]) -> list[str]:
    sanitized: list[str] = []
    for event in events:
        txt = event.strip()
        lower = txt.lower()

        if (
            lower.startswith("turno de ")
            or "mana restante" in lower
            or "mana {" in lower
            or "fim do combate: vida" in lower
            or "deck " in lower
            or "fase:" in lower
        ):
            continue

        txt = re.sub(r"\s*\(custo[^)]*\)", "", txt, flags=re.IGNORECASE)
        txt = re.sub(r"\s*\|\s*Mana restante:.*$", "", txt, flags=re.IGNORECASE)
        txt = re.sub(r"\s+", " ", txt).strip(" .")

        if txt:
            sanitized.append(txt)

    return sanitized[-12:]


def _sanitize_story_text(story: str) -> str:
    text = story.replace("\n", " ").strip()
    text = re.sub(r"\s*\(custo[^)]*\)", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\|\s*Mana restante:[^\.|\n]*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s+", " ", text).strip(" .")
    return text


def register_turn_story() -> None:
    game = get_game()
    start = game.get("turn_log_start", 0)
    raw_events = [x["text"] for x in st.session_state.logs_card[start:]]
    events = _sanitize_story_events(raw_events)
    if not events:
        return

    # Narrativa deterministicamente baseada no estado real da rodada
    # para evitar inconsistencias com Status IA/Status Jogador.
    story = build_local_turn_story(game, events)
    story = _sanitize_story_text(story)

    game["last_story"] = story
    game["story_history"].append(
        {
            "turn": game["turn"],
            "story": story,
            "life_player": game.get("life_player"),
            "life_ai": game.get("life_ai"),
        }
    )


def start_card_match(setup: dict[str, Any]) -> None:
    player_team = "red" if setup["side"] == "Red Team" else "blue"
    ai_team = "blue" if player_team == "red" else "red"

    player_deck = deck_for_team(player_team)
    ai_deck = deck_for_team(ai_team)
    random.shuffle(player_deck)
    random.shuffle(ai_deck)

    st.session_state.card_game = {
        "turn": 1,
        "max_turns": 35,
        "phase": "main",
        "active_side": "player",
        "player_name": setup["player_name"],
        "player_team": player_team,
        "ai_team": ai_team,
        "player_doctrine": setup.get("player_doctrine", "custom"),
        "ai_doctrine": random.choice(list(BLUE_DOCTRINES if ai_team == "blue" else RED_DOCTRINES)),
        "setup": setup,
        "life_player": 20,
        "life_ai": 20,
        "mana_player": empty_mana_pool(),
        "mana_ai": empty_mana_pool(),
        "deck_player": player_deck,
        "deck_ai": ai_deck,
        "hand_player": [],
        "hand_ai": [],
        "board_player": [],
        "board_ai": [],
        "grave_player": [],
        "grave_ai": [],
        "nodes_played_turn_player": 0,
        "nodes_played_turn_ai": 0,
        "turn_log_start": 0,
        "story_history": [],
        "last_story": "",
        "end_story_announced": False,
        "ended": False,
        "winner": None,
    }

    st.session_state.logs_card = []
    add_log("=== CARD ARENA INICIADA ===", "ok")
    add_log(f"Jogador: {setup['player_name']} | Time: {player_team.upper()} | IA: {ai_team.upper()}", "info")

    draw_card("player", 4)
    draw_card("ai", 4)
    begin_turn("player")


def init_state() -> None:
    if "setup_done_card" not in st.session_state:
        st.session_state.setup_done_card = False
    if "logs_card" not in st.session_state:
        st.session_state.logs_card = []
    if "card_game" not in st.session_state:
        st.session_state.card_game = {}
    if "selected_attackers" not in st.session_state:
        st.session_state.selected_attackers = []
    if "hand_carousel_start" not in st.session_state:
        st.session_state.hand_carousel_start = 0
    if "hand_visible_count" not in st.session_state:
        st.session_state.hand_visible_count = 5
    if "hand_modal_index" not in st.session_state:
        st.session_state.hand_modal_index = None
    if "board_modal_target" not in st.session_state:
        st.session_state.board_modal_target = None
    if "onboarding_step_card" not in st.session_state:
        st.session_state.onboarding_step_card = "landing"
    if "show_team_modal_card" not in st.session_state:
        st.session_state.show_team_modal_card = False
    if "show_doctrine_modal_card" not in st.session_state:
        st.session_state.show_doctrine_modal_card = False
    if "show_ai_modal_card" not in st.session_state:
        st.session_state.show_ai_modal_card = False
    if "ai_test_result_card" not in st.session_state:
        st.session_state.ai_test_result_card = None
    if "show_story_tts_settings_card" not in st.session_state:
        st.session_state.show_story_tts_settings_card = False
    if "setup_wizard_card" not in st.session_state:
        st.session_state.setup_wizard_card = {
            "player_name": "ghost_operator",
            "side": "",
            "player_doctrine": "",
            "provider": "Local Offline",
            "model": "",
            "endpoint": "",
            "api_key": "",
            **ONBOARDING_IMAGE_DEFAULTS,
        }
    else:
        wizard = st.session_state.setup_wizard_card
        for key, value in ONBOARDING_IMAGE_DEFAULTS.items():
            if not wizard.get(key):
                wizard[key] = value


def get_responsive_hand_visible_count() -> int:
    try:
        ua = str(st.context.headers.get("user-agent", "")).lower()
    except Exception:
        return 5

    # Prioriza 5 no desktop e reduz em dispositivos menores.
    if any(token in ua for token in ("iphone", "android", "mobile", "mobi")):
        return 2
    if any(token in ua for token in ("ipad", "tablet")):
        return 3
    return 5


def reset_to_setup_flow() -> None:
    st.session_state.setup_done_card = False
    st.session_state.card_game = {}
    st.session_state.logs_card = []
    st.session_state.onboarding_step_card = "landing"
    st.session_state.show_team_modal_card = False
    st.session_state.show_doctrine_modal_card = False
    st.session_state.show_ai_modal_card = False
    st.session_state.ai_test_result_card = None


def resolve_image_source(source: str) -> tuple[str | None, str | None]:
    clean = source.strip()
    if not clean:
        return None, None
    if clean.lower().startswith(("http://", "https://")):
        return clean, None
    try:
        candidate = Path(clean).expanduser()
    except OSError:
        return None, "Caminho invalido para imagem."
    if candidate.exists():
        return str(candidate), None
    return None, "Imagem nao encontrada no caminho informado."


def render_image_slot(source: str, empty_text: str, *, min_height: int = 240, width: int | None = None) -> None:
    image_source, error = resolve_image_source(source)
    if image_source:
        if width is None:
            st.image(image_source, use_container_width=True)
        else:
            st.image(image_source, width=width)
        return
    copy = error or empty_text
    st.markdown(
        (
            f"<div class='image-slot' style='min-height:{min_height}px'>"
            f"{html.escape(copy)}"
            "</div>"
        ),
        unsafe_allow_html=True,
    )


def render_setup_team_modal_card() -> None:
    wizard = st.session_state.setup_wizard_card

    st.markdown("<div class='wizard-heading'>Escolha seu lado na operacao</div>", unsafe_allow_html=True)
    player_name = st.text_input("Codinome", value=wizard.get("player_name", "ghost_operator"), key="wizard_player_name")
    wizard["player_name"] = player_name.strip()

    c1, c2 = st.columns(2)
    with c1:
        render_image_slot(wizard["team_red_image"], "Espaco reservado para arte do Red Team.", min_height=190)
        st.markdown(f"<div class='team-copy'>{TEAM_EXPLANATIONS['Red Team']}</div>", unsafe_allow_html=True)
        if st.button("RED TEAM", key="wizard_pick_red", use_container_width=True):
            wizard["side"] = "Red Team"
            wizard["player_doctrine"] = ""
            st.session_state.onboarding_step_card = "doctrine"
            st.session_state.show_team_modal_card = False
            st.session_state.show_doctrine_modal_card = True
            st.rerun()

    with c2:
        render_image_slot(wizard["team_blue_image"], "Espaco reservado para arte do Blue Team.", min_height=190)
        st.markdown(f"<div class='team-copy'>{TEAM_EXPLANATIONS['Blue Team']}</div>", unsafe_allow_html=True)
        if st.button("BLUE TEAM", key="wizard_pick_blue", use_container_width=True):
            wizard["side"] = "Blue Team"
            wizard["player_doctrine"] = ""
            st.session_state.onboarding_step_card = "doctrine"
            st.session_state.show_team_modal_card = False
            st.session_state.show_doctrine_modal_card = True
            st.rerun()


def render_setup_ai_modal_card() -> None:
    wizard = st.session_state.setup_wizard_card

    provider_guide = {
        "Local Offline": "Roda sem API externa. Configure apenas Modelo/Endpoint se quiser integrar motor local compatível.",
        "Ollama": "Use endpoint local (ex.: http://localhost:11434/v1); modelo validado em teste de compatibilidade: llama3.1:8b.",
        "LM Studio": "Ative servidor local e use endpoint OpenAI-compatible (ex.: http://localhost:1234/v1).",
        "vLLM": "Aponte para endpoint /v1 do vLLM e informe um modelo disponível no servidor.",
        "OpenAI": "Informe API Key válida e modelo OpenAI (ex.: gpt-4o-mini). Endpoint padrão é automático.",
        "Gemini": "Informe API Key do Google AI Studio. Modelo/endpoint são preenchidos automaticamente.",
        "OpenAI Compatible": "Use para provedores compatíveis com API OpenAI (endpoint + modelo + chave, quando exigido).",
    }

    st.markdown("<div class='wizard-heading'>Configurando IA adversaria</div>", unsafe_allow_html=True)
    image_col, form_col = st.columns([1.0, 1.5], vertical_alignment="top")

    with image_col:
        render_image_slot(
            wizard["ai_setup_image"],
            "Espaco reservado para arte da IA adversaria.",
            min_height=180,
            width=509,
        )

    with form_col:
        provider_options = ["Local Offline", "Ollama", "LM Studio", "vLLM", "OpenAI", "Gemini", "OpenAI Compatible"]
        current_provider = wizard.get("provider", "Local Offline")
        if current_provider not in provider_options:
            current_provider = "Local Offline"
        provider = st.selectbox("IA adversaria", provider_options, index=provider_options.index(current_provider))

        guide_html = "".join(
            (
                f"<div class='provider-guide-item{' active' if name == provider else ''}'>"
                f"<div class='provider-guide-name'>{html.escape(name)}</div>"
                f"<div class='provider-guide-copy'>{html.escape(provider_guide.get(name, ''))}</div>"
                "</div>"
            )
            for name in provider_options
        )
        st.markdown(
            (
                "<div class='provider-guide-box'>"
                "<div class='provider-guide-title'>COMO ESCOLHER E CONFIGURAR CADA PROVEDOR</div>"
                f"<div class='provider-guide-grid'>{guide_html}</div>"
                "</div>"
            ),
            unsafe_allow_html=True,
        )

        if provider != wizard.get("provider"):
            default_model, default_endpoint = provider_defaults(provider)
            wizard["provider"] = provider
            wizard["model"] = default_model
            wizard["endpoint"] = default_endpoint
            st.session_state["wizard_model"] = default_model
            st.session_state["wizard_endpoint"] = default_endpoint
            st.session_state.ai_test_result_card = None
            st.rerun()
        wizard["provider"] = provider

        default_model, default_endpoint = provider_defaults(provider)
        if not wizard.get("model"):
            wizard["model"] = default_model
        if provider_uses_openai_compatible(provider) and not wizard.get("endpoint"):
            wizard["endpoint"] = default_endpoint
        if provider == "Gemini" and not wizard.get("endpoint"):
            wizard["endpoint"] = default_endpoint

        pending_model = st.session_state.pop("pending_wizard_model", None)
        if pending_model is not None:
            wizard["model"] = pending_model
            st.session_state["wizard_model"] = pending_model

        pending_endpoint = st.session_state.pop("pending_wizard_endpoint", None)
        if pending_endpoint is not None:
            wizard["endpoint"] = pending_endpoint
            st.session_state["wizard_endpoint"] = pending_endpoint

        if "wizard_model" not in st.session_state:
            st.session_state["wizard_model"] = wizard.get("model", default_model)
        if not st.session_state.get("wizard_model"):
            st.session_state["wizard_model"] = wizard.get("model", default_model)
        st.text_input("Modelo", key="wizard_model")
        wizard["model"] = str(st.session_state.get("wizard_model", "")).strip()

        if "wizard_endpoint" not in st.session_state:
            st.session_state["wizard_endpoint"] = wizard.get("endpoint", default_endpoint)
        if provider_uses_openai_compatible(provider) and not st.session_state.get("wizard_endpoint"):
            st.session_state["wizard_endpoint"] = wizard.get("endpoint", default_endpoint)
        if provider == "Gemini" and not st.session_state.get("wizard_endpoint"):
            st.session_state["wizard_endpoint"] = wizard.get("endpoint", default_endpoint)
        st.text_input("Endpoint", key="wizard_endpoint")
        wizard["endpoint"] = str(st.session_state.get("wizard_endpoint", "")).strip()

        api_key = st.text_input("API Key", value=wizard.get("api_key", ""), type="password", key="wizard_api_key")
        clean_api_key = sanitize_api_key(api_key)
        wizard["api_key"] = clean_api_key

        if provider_requires_api_key(provider):
            previous_key = wizard.get("_last_api_key_for_autofill", "")
            if clean_api_key and clean_api_key != previous_key:
                auto_model, auto_endpoint = provider_defaults(provider)
                wizard["model"] = auto_model
                wizard["endpoint"] = auto_endpoint
                st.session_state["pending_wizard_model"] = auto_model
                st.session_state["pending_wizard_endpoint"] = auto_endpoint
                wizard["_last_api_key_for_autofill"] = clean_api_key
                st.rerun()
        else:
            wizard["_last_api_key_for_autofill"] = ""

        if provider_requires_api_key(provider):
            st.caption("Informe API Key e pressione Enter para autoajustar modelo e endpoint.")
        else:
            st.caption("Provedor local selecionado: API Key opcional.")

        test_col, close_col = st.columns([2, 1])
        with test_col:
            if st.button("Testar IA", use_container_width=True, key="test_ai_setup_modal"):
                ok, message = test_ai_connection(
                    provider=provider,
                    model=wizard["model"],
                    endpoint=wizard["endpoint"],
                    api_key=wizard["api_key"],
                )
                st.session_state.ai_test_result_card = {"ok": ok, "message": message, "at": ts()}
        with close_col:
            if st.button("Fechar", use_container_width=True, key="close_ai_modal"):
                st.session_state.show_ai_modal_card = False
                st.rerun()

    result = st.session_state.get("ai_test_result_card")
    if result:
        prefix = f"[{result['at']}] "
        if result["ok"]:
            st.success(prefix + result["message"])
        else:
            st.error(prefix + result["message"])

    ready_to_start = bool(
        wizard.get("player_name", "").strip()
        and wizard.get("side")
        and wizard.get("player_doctrine")
    )
    if st.button("Iniciar", use_container_width=True, disabled=not ready_to_start, key="wizard_start_game"):
        setup = {
            "player_name": wizard["player_name"].strip(),
            "side": wizard["side"],
            "player_doctrine": wizard["player_doctrine"],
            "provider": wizard["provider"],
            "model": wizard["model"],
            "endpoint": wizard["endpoint"],
            "api_key": sanitize_api_key(wizard["api_key"]),
        }
        st.session_state.setup_done_card = True
        st.session_state.onboarding_step_card = "completed"
        st.session_state.show_team_modal_card = False
        st.session_state.show_doctrine_modal_card = False
        st.session_state.show_ai_modal_card = False
        start_card_match(setup)
        st.rerun()


def render_doctrine_selection_step() -> None:
    wizard = st.session_state.setup_wizard_card
    side = wizard.get("side", "")
    doctrines = TEAM_DOCTRINES.get(side, {})

    if not side or not doctrines:
        st.warning("Escolha primeiro RED TEAM ou BLUE TEAM.")
        if st.button("Abrir escolha de time", key="open_team_modal_from_doctrine"):
            st.session_state.show_doctrine_modal_card = False
            st.session_state.show_team_modal_card = True
            st.rerun()
        return

    st.markdown(f"<div class='wizard-heading'>Doutrinas do {side}</div>", unsafe_allow_html=True)
    st.caption("Selecione seu personagem doutrinario. Cada doutrina altera sua abordagem tatico-educacional.")

    cols = st.columns(len(doctrines))
    side_slug = side.lower().replace(" ", "_")
    for idx, (doctrine_key, doctrine_text) in enumerate(doctrines.items()):
        with cols[idx]:
            with st.container(border=True):
                image_field = f"doctrine_image_{side_slug}_{doctrine_key}"
                render_image_slot(
                    wizard[image_field],
                    f"Espaco reservado para {doctrine_key.upper()}.",
                    min_height=255,
                    width=246,
                )
                st.markdown(f"<div class='doctrine-copy'>{doctrine_text}</div>", unsafe_allow_html=True)
                if st.button(f"{doctrine_key.upper()}", use_container_width=True, key=f"choose_doctrine_{side_slug}_{doctrine_key}"):
                    wizard["player_doctrine"] = doctrine_key
                    st.session_state.onboarding_step_card = "ai_config"
                    st.session_state.show_doctrine_modal_card = False
                    st.session_state.show_ai_modal_card = True
                    st.rerun()


def is_card_playable(side: str, card: dict[str, Any]) -> bool:
    game = get_game()
    if game["phase"] != "main" or game["active_side"] != side or game["ended"]:
        return False
    if card["type"] == "Node" and game[f"nodes_played_turn_{side}"] >= 1:
        return False
    if card["type"] != "Node" and not can_pay(game[f"mana_{side}"], card.get("cost", {})):
        return False
    return True


def card_css_class(card: dict[str, Any]) -> str:
    color = card.get("color", "C")
    return MANA_COLORS.get(color, MANA_COLORS["C"])["css"]


def slugify_card_name(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")


@lru_cache(maxsize=None)
def get_card_art_data_uri(card_id: str, card_name: str, variant: str = "full") -> str | None:
    file_name = CARD_ART_ALIASES.get(card_id, f"{slugify_card_name(card_name)}.png")
    if variant == "thumb":
        image_path = CARD_ART_THUMBS_DIR / file_name
        if not image_path.exists():
            image_path = CARD_ART_DIR / file_name
    else:
        image_path = CARD_ART_DIR / file_name
    if not image_path.exists():
        return None
    encoded = base64.b64encode(image_path.read_bytes()).decode("ascii")
    return f"data:image/png;base64,{encoded}"


def render_card_html(card_id: str, perm: dict[str, Any] | None = None, art_variant: str = "full") -> str:
    c = CARD_DB[card_id]
    css_class = card_css_class(c)
    tapped_cls = " tapped" if perm and perm.get("tapped") else ""
    pt = ""
    if c["type"] == "Agent":
        atk = perm["atk"] + perm.get("temp_atk", 0) if perm else c.get("atk", 0)
        hp = perm["hp"] if perm else c.get("hp", 0)
        pt = f"<span class='pt-badge'>{atk}/{hp}</span>"

    art_data_uri = get_card_art_data_uri(card_id, c["name"], art_variant)
    art_html = (
        f"<img src='{art_data_uri}' alt='{html.escape(c['name'])}'>"
        if art_data_uri
        else c.get("art", "🃏")
    )

    return (
        f"<div class='mtg-card {css_class}{tapped_cls}'>"
        f"<div class='mtg-head'><span>{c['name']}</span><span class='mana-cost'>{mana_to_str(c.get('cost', {}))}</span></div>"
        f"<div class='card-art'>{art_html}</div>"
        f"<div class='type-line'>{c['type']} - {c.get('osi', '?')}</div>"
        f"<div class='text-box'>{c.get('text', '')}<div class='flavor'>{c.get('flavor', '')}</div></div>"
        f"<div class='bottom-line'><span class='rarity'>Rarity {c.get('rarity', 'C')}</span>{pt}</div>"
        "</div>"
    )


def card_role_text(card: dict[str, Any]) -> str:
    t = card["type"]
    if t == "Node":
        return "Base de recurso. Define sua curva de mana e a consistencia da partida."
    if t == "Agent":
        return "Unidade de campo. Pressiona vida inimiga e controla o ritmo de combate."
    if t in {"Exploit", "Script"}:
        return "Magia tatica de impacto imediato. Melhor usada no timing certo para virar trocas."
    if t == "Malware":
        return "Pressao persistente. Gera valor por tempo e pode forcar resposta do oponente."
    if t == "Tool":
        return "Utilitario de suporte. Fortalece sua posicao e melhora eficiencia do plano."
    return "Carta de suporte estrategico."


def card_timing_hint(card: dict[str, Any]) -> str:
    t = card["type"]
    if t == "Node":
        return "Priorize nos primeiros turnos para nao travar suas jogadas mais caras."
    if t == "Agent":
        return "Jogue quando puder proteger ou extrair valor imediato no combate."
    if t in {"Exploit", "Script"}:
        return "Guarde para responder uma ameaca chave ou abrir janela de dano letal."
    if t in {"Malware", "Tool"}:
        return "Ideal em mid game, quando o valor continuo supera jogadas pontuais."
    return "Use quando maximizar sinergia com seu board atual."


def card_impact_hint(card: dict[str, Any]) -> str:
    if card["type"] == "Agent":
        return f"Impacto direto de combate: {card.get('atk', 0)}/{card.get('hp', 0)}."
    if card["type"] == "Node":
        return f"Acelera recurso gerando mana {card.get('produce', 'C')} por turno."
    if card.get("spell"):
        return "Gera swing de mesa imediato ao resolver o efeito de magia."
    if card.get("on_play"):
        return "Ativa um efeito de entrada que pode mudar o tempo da partida."
    return "Impacto situacional com foco tatico."


def mana_hack_legend_html() -> str:
    return (
        "<div class='modal-sub'>Mana no Estudo Hack</div>"
        "<div class='modal-copy'>"
        "W/Signal: visibilidade, governanca e controle defensivo.<br>"
        "U/Cobalt: rede, protocolos e analise tecnica.<br>"
        "B/Void: furtividade, evasao e persistencia ofensiva.<br>"
        "R/Scarlet: agressao direta, exploracao e impacto rapido.<br>"
        "G/Grid: infraestrutura, operacao e resiliencia.<br>"
        "C/Neutral: recurso generico sem especializacao de dominio."
        "</div>"
    )


def analyze_osi_layer_activity(log_entries: list[dict[str, Any]], team: str) -> tuple[dict[str, int], list[str]]:
    team_card_ids = set(RED_DECK_BASE if team == "red" else BLUE_DECK_BASE)
    layer_hits = {layer: 0 for layer in OSI_LAYERS}
    highlights: list[str] = []

    for entry in log_entries[-160:]:
        text = entry.get("text", "")
        lowered = text.lower()

        matched = False
        for card_id in team_card_ids:
            card = CARD_DB.get(card_id)
            if not card:
                continue
            card_name = card.get("name", "").lower()
            if card_name and card_name in lowered:
                layer = card.get("osi", "L7")
                if layer in layer_hits:
                    layer_hits[layer] += 1
                if len(highlights) < 6:
                    highlights.append(text)
                matched = True
                break

        if not matched and team == "red" and ("rompeu a defesa" in lowered or "dano direto" in lowered):
            layer_hits["L7"] += 1
            if len(highlights) < 6:
                highlights.append(text)
        if not matched and team == "blue" and ("ganhou" in lowered or "travou" in lowered or "destruiu" in lowered):
            layer_hits["L4"] += 1
            if len(highlights) < 6:
                highlights.append(text)

    return layer_hits, highlights


def render_osi_lore_panel(game: dict[str, Any]) -> None:
    player_team = game.get("player_team", "red")
    mode = "attack" if player_team == "red" else "defense"
    guide_map = ATTACK_GUIDE if mode == "attack" else DEFENSE_GUIDE
    activity, highlights = analyze_osi_layer_activity(st.session_state.logs_card, player_team)

    if mode == "attack":
        st.markdown("### 🔥 Campanha Ofensiva por Camada")
        st.caption("Voce esta no lado atacante. O progresso mostra quais camadas OSI ja receberam mais pressao durante a partida.")
        st.markdown("**Como atacar melhor:** combine ruptura de L3/L4 com finalizacao em L7 para converter vantagem em dano direto.")
    else:
        st.markdown("### 🛡️ Processo Defensivo por Camada")
        st.caption("Voce esta no lado defensor. O progresso mostra em quais camadas sua protecao esta mais ativa nesta partida.")
        st.markdown("**Como proteger melhor:** estabilize L2/L4 para conter propagacao e preserve L7 para segurar impacto no usuario final.")

    st.divider()

    cols = st.columns(2)
    for i, layer in enumerate(OSI_LAYERS):
        with cols[i % 2]:
            count = activity.get(layer, 0)
            # Cada acao relevante aumenta 25% ate o maximo de 100%.
            progress = min(1.0, count / 4.0)
            pct = int(progress * 100)
            action_word = "ataque" if mode == "attack" else "protecao"
            st.markdown(f"**{layer} · {action_word} {pct}%**")

            if layer in ("L1", "L2"):
                color_class = "osi-blue"
            elif layer in ("L3", "L4", "L5"):
                color_class = "osi-orange"
            else:
                color_class = "osi-red"

            st.markdown(
                (
                    "<div class='osi-progress-track'>"
                    f"<div class='osi-progress-fill {color_class}' style='width:{pct}%;'></div>"
                    "</div>"
                ),
                unsafe_allow_html=True,
            )
            st.caption(guide_map[layer])

            examples = OSI_LAYER_EXAMPLES[layer]
            st.markdown(
                (
                    "<div class='osi-layer-note'>"
                    f"<b>Exemplo de hardware:</b> {examples['hardware']}<br>"
                    f"<b>Protocolos de comunicacao:</b> {examples['protocolos']}"
                    "</div>"
                ),
                unsafe_allow_html=True,
            )

    st.divider()
    st.markdown("### 🎯 Leitura Tática da Partida")
    if highlights:
        for line in highlights[:5]:
            st.markdown(f"- {line}")
    else:
        st.caption("Ainda sem eventos suficientes para leitura tática. Avance alguns turnos para preencher o painel.")


def build_player_status_metrics(game: dict[str, Any]) -> dict[str, Any]:
    logs = st.session_state.logs_card
    player_team = game.get("player_team", "red")
    mode = "attack" if player_team == "red" else "defense"

    direct_damage = 0
    breach_hits = 0
    containment_actions = 0
    malware_removed = 0
    offensive_actions = 0

    for entry in logs[-220:]:
        text = entry.get("text", "")
        lower = text.lower()

        if "rompeu a defesa" in lower and "em ia" in lower:
            breach_hits += 1
            dmg_match = re.search(r"causou\s+(\d+)\s+de dano", lower)
            if dmg_match:
                direct_damage += int(dmg_match.group(1))

        if lower.startswith("jogador causou") and "dano direto" in lower:
            dmg_match = re.search(r"causou\s+(\d+)\s+de dano", lower)
            if dmg_match:
                direct_damage += int(dmg_match.group(1))

        if lower.startswith("jogador usou") or "jogador reforcou ataque" in lower:
            offensive_actions += 1

        if lower.startswith("jogador removeu") or lower.startswith("jogador travou") or lower.startswith("jogador destruiu"):
            containment_actions += 1
        if "jogador removeu malware inimigo" in lower:
            malware_removed += 1

    life_player = game.get("life_player", 0)
    life_ai = game.get("life_ai", 0)
    pressure_score = max(0, min(100, int(((life_player - life_ai) + 20) * 2.5)))
    integrity_score = max(0, min(100, int((life_player / 20) * 100)))

    player_board = game.get("board_player", [])
    active_agents = sum(1 for p in player_board if CARD_DB[p["card_id"]]["type"] == "Agent")
    support_tools = sum(1 for p in player_board if CARD_DB[p["card_id"]]["type"] in ("Tool", "Node"))

    return {
        "mode": mode,
        "direct_damage": direct_damage,
        "breach_hits": breach_hits,
        "offensive_actions": offensive_actions,
        "containment_actions": containment_actions,
        "malware_removed": malware_removed,
        "pressure_score": pressure_score,
        "integrity_score": integrity_score,
        "active_agents": active_agents,
        "support_tools": support_tools,
    }


def render_status_dashboard_panel(game: dict[str, Any]) -> None:
    metrics = build_player_status_metrics(game)
    mode = metrics["mode"]

    if mode == "attack":
        st.markdown("### 📊 Dashboard de Status de Ataque")
        st.caption("Painel tatico para quem esta no papel atacante: impacto, ritmo ofensivo e pressao sobre a IA.")

        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Dano Direto Total", metrics["direct_damage"])
        m2.metric("Rupturas de Defesa", metrics["breach_hits"])
        m3.metric("Acoes Ofensivas", metrics["offensive_actions"])
        m4.metric("Agentes Ativos", metrics["active_agents"])

        st.markdown("**Pressao de Ataque sobre a IA**")
        st.progress(metrics["pressure_score"] / 100)
        st.caption(f"Score de pressao: {metrics['pressure_score']}%")

        st.markdown("**Como atacar melhor agora**")
        st.markdown("- Continue forçando ruptura em L3/L7 para converter vantagem em dano direto.")
        st.markdown("- Combine Agents ativos com scripts de boost para maximizar cada janela de combate.")
        st.markdown("- Se a IA estabilizar campo, priorize remover bloqueadores antes do proximo push.")
    else:
        st.markdown("### 📊 Dashboard de Status de Protecao")
        st.caption("Painel tatico para quem esta no papel defensor: contencao, resiliência e seguranca operacional.")

        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Acoes de Contencao", metrics["containment_actions"])
        m2.metric("Malwares Removidos", metrics["malware_removed"])
        m3.metric("Integridade Atual", f"{metrics['integrity_score']}%")
        m4.metric("Ferramentas de Suporte", metrics["support_tools"])

        st.markdown("**Nivel de Protecao da Operacao**")
        st.progress(metrics["integrity_score"] / 100)
        st.caption(f"Score de protecao: {metrics['integrity_score']}%")

        st.markdown("**Como proteger melhor agora**")
        st.markdown("- Mantenha contencao ativa em L2/L4 para reduzir propagacao de ataques.")
        st.markdown("- Priorize remocao de malware e neutralizacao de agentes com maior dano.")
        st.markdown("- Preserve recursos para resposta imediata quando houver ruptura de defesa.")


def render_board(side: str, title: str) -> None:
    game = get_game()

    _, head_c, _ = st.columns([1, 1, 1])
    with head_c:
        if side == "player":
            if st.button("Passar turno", use_container_width=True, disabled=game["ended"], key="pass_turn_board_top"):
                end_player_turn()
                st.rerun()

    st.markdown(f"<div class='battle-strip'><div class='zone-title'>{title}</div></div>", unsafe_allow_html=True)

    board_cards = game[f"board_{side}"]
    if not board_cards:
        st.markdown("<div class='small-note'>Sem permanentes em campo.</div>", unsafe_allow_html=True)
        return

    cards_per_row = 5
    for row_start in range(0, len(board_cards), cards_per_row):
        row_indices = list(range(row_start, min(row_start + cards_per_row, len(board_cards))))
        missing_slots = cards_per_row - len(row_indices)
        if missing_slots > 0:
            side_gap = missing_slots / 2
            row_cols = st.columns([side_gap] + [1] * len(row_indices) + [side_gap])
            active_cols = row_cols[1:-1]
        else:
            active_cols = st.columns(cards_per_row)

        for col, idx in zip(active_cols, row_indices):
            perm = board_cards[idx]
            card_id = perm["card_id"]
            card = CARD_DB[card_id]
            with col:
                st.markdown(render_card_html(card_id, perm), unsafe_allow_html=True)
                with st.container(key=f"open_board_head_click_{side}_{idx}"):
                    if st.button("🔍", key=f"open_board_card_{side}_{idx}"):
                        st.session_state.board_modal_target = {"side": side, "index": idx}
                        st.rerun()

                _, action_r = st.columns(2)
                with action_r:
                    has_mana_for_attack = can_pay(game.get("mana_player", {}), card.get("cost", {}))
                    can_quick_attack = (
                        side == "player"
                        and card["type"] == "Agent"
                        and not perm.get("tapped", False)
                        and not perm.get("summon_sick", False)
                        and game["phase"] == "main"
                        and game["active_side"] == "player"
                        and not game["ended"]
                        and has_mana_for_attack
                    )
                    if can_quick_attack:
                        if st.button("↷", key=f"quick_attack_{side}_{idx}"):
                            combat("player", [idx])
                            check_endgame()
                            st.rerun()

def render_log() -> None:
    html = ""
    for line in st.session_state.logs_card:
        color = style_to_color(line["style"])
        html += f"<div><span style='color:#8f9bb4'>[{line['ts']}]</span> <span style='color:{color}'>{line['text']}</span></div>"
    st.markdown(f"<div class='log-box'>{html}</div>", unsafe_allow_html=True)


def render_story_audio_controls(story: str) -> None:
    if "story_tts_nonce" not in st.session_state:
        st.session_state.story_tts_nonce = 0
    if "story_tts_action" not in st.session_state:
        st.session_state.story_tts_action = "idle"
    if "story_tts_last_text" not in st.session_state:
        st.session_state.story_tts_last_text = ""
    if "story_tts_auto" not in st.session_state:
        st.session_state.story_tts_auto = True
    if "story_tts_rate" not in st.session_state:
        st.session_state.story_tts_rate = 0.94
    if "story_tts_pitch" not in st.session_state:
        st.session_state.story_tts_pitch = 1.02
    if "story_tts_volume" not in st.session_state:
        st.session_state.story_tts_volume = 1.0
    if "story_tts_voice_mode" not in st.session_state:
        st.session_state.story_tts_voice_mode = "Automatico"
    if "story_tts_voice_hint" not in st.session_state:
        st.session_state.story_tts_voice_hint = ""

    st.session_state.story_tts_auto = st.toggle(
        "Auto narrar quando a narrativa mudar",
        value=st.session_state.story_tts_auto,
        key="story_tts_auto_toggle",
        help="Quando ativo, a narracao toca automaticamente sempre que a Narrativa da Rodada for atualizada.",
    )

    # Dispara TTS automatico apenas quando o texto realmente mudou.
    if story and st.session_state.story_tts_auto and story != st.session_state.story_tts_last_text:
        st.session_state.story_tts_nonce += 1
        st.session_state.story_tts_action = "speak"
        st.session_state.story_tts_last_text = story
    elif story and story != st.session_state.story_tts_last_text:
        # Mantem controle de mudanca sem tocar audio quando auto estiver desligado.
        st.session_state.story_tts_last_text = story

    c1, c2 = st.columns(2)
    with c1:
        if st.button("🔊 Ouvir narracao", use_container_width=True, disabled=not story):
            st.session_state.story_tts_nonce += 1
            st.session_state.story_tts_action = "speak"
    with c2:
        if st.button("⏹ Parar", use_container_width=True):
            st.session_state.story_tts_nonce += 1
            st.session_state.story_tts_action = "stop"

    payload = {
        "action": st.session_state.story_tts_action,
        "nonce": st.session_state.story_tts_nonce,
        "text": story or "",
        "rate": st.session_state.story_tts_rate,
        "pitch": st.session_state.story_tts_pitch,
        "volume": st.session_state.story_tts_volume,
        "voice_mode": st.session_state.get("story_tts_voice_mode", "Automatico"),
        "voice_hint": st.session_state.get("story_tts_voice_hint", ""),
    }

    components.html(
        f"""
        <script>
        (function() {{
            const payload = {json.dumps(payload)};
            const synth = window.speechSynthesis;
            if (!synth) {{
                return;
            }}

            function scoreVoice(v) {{
                const lang = (v.lang || "").toLowerCase();
                const name = (v.name || "").toLowerCase();
                const mode = String(payload.voice_mode || "Automatico").toLowerCase();
                const voiceHint = String(payload.voice_hint || "").toLowerCase().trim();
                let score = 0;
                if (lang === "pt-br") score += 100;
                else if (lang.startsWith("pt-br")) score += 95;
                else if (lang.startsWith("pt")) score += 80;
                if (/natural|neural|premium/.test(name)) score += 20;
                if (/google|microsoft|luciana|francisca|heloisa|maria/.test(name)) score += 10;
                if (mode === "edge natural") {{
                    if (/microsoft|edge|online|natural|neural/.test(name)) score += 45;
                    if (lang.startsWith("pt-br")) score += 20;
                }}
                if (voiceHint) {{
                    if (name.includes(voiceHint)) score += 120;
                    else if (voiceHint.split(/\\s+/).some(token => token && name.includes(token))) score += 40;
                }}
                if (v.localService) score += 4;
                return score;
            }}

            function normalizeKey(txt) {{
                return String(txt || "")
                    .toLowerCase()
                    .normalize("NFD")
                    .replace(/[\u0300-\u036f]/g, "")
                    .trim();
            }}

            function pickVoiceByHint(voices) {{
                const hint = normalizeKey(payload.voice_hint || "");
                if (!hint || !voices || !voices.length) return null;

                const ptVoices = voices.filter(v => String(v.lang || "").toLowerCase().startsWith("pt"));
                const source = ptVoices.length ? ptVoices : voices;

                const exact = source.find(v => normalizeKey(v.name) === hint);
                if (exact) return exact;

                const contains = source.find(v => normalizeKey(v.name).includes(hint));
                if (contains) return contains;

                const tokens = hint.split(/\s+/).filter(Boolean);
                if (!tokens.length) return null;
                return source.find(v => tokens.every(t => normalizeKey(v.name).includes(t))) || null;
            }}

            function pickBestPortugueseVoice(voices) {{
                if (!voices || !voices.length) return null;
                const hinted = pickVoiceByHint(voices);
                if (hinted) return hinted;
                const ranked = voices
                    .map(v => ({{ v, score: scoreVoice(v) }}))
                    .filter(item => item.score > 0)
                    .sort((a, b) => b.score - a.score);
                return ranked.length ? ranked[0].v : null;
            }}

            function normalizeNarrationText(text) {{
                return String(text || "")
                    .replace(/\bIA\b/g, "inteligencia artificial")
                    .replace(/\bSOC\b/g, "S O C")
                    .replace(/\bOSI\b/g, "O S I");
            }}

            window.__storyTtsLastNonce = window.__storyTtsLastNonce || -1;
            if (payload.nonce === window.__storyTtsLastNonce) {{
                return;
            }}
            window.__storyTtsLastNonce = payload.nonce;

            if (payload.action === "stop") {{
                synth.cancel();
                return;
            }}

            if (payload.action === "speak" && payload.text) {{
                synth.cancel();
                const speak = (tries) => {{
                    if (synth.speaking) {{
                        if (tries > 0) setTimeout(() => speak(tries - 1), 80);
                        return;
                    }}
                    const utt = new SpeechSynthesisUtterance(normalizeNarrationText(payload.text));
                    utt.lang = "pt-BR";
                    utt.rate = Number(payload.rate || 0.94);
                    utt.pitch = Number(payload.pitch || 1.02);
                    utt.volume = Number(payload.volume || 1.0);
                    const voices = synth.getVoices ? synth.getVoices() : [];
                    const bestVoice = pickBestPortugueseVoice(voices);
                    if (bestVoice) {{
                        utt.voice = bestVoice;
                    }}
                    utt.onstart = () => {{
                        window.__storyTtsLastVoiceName = bestVoice ? bestVoice.name : "default";
                    }};
                    synth.speak(utt);
                }};

                speak(6);
                if (synth.getVoices && synth.getVoices().length === 0) {{
                    setTimeout(() => speak(6), 150);
                }}
            }}
        }})();
        </script>
        """,
        height=0,
    )


@st.dialog("Configuracoes da Narracao")
def render_story_tts_settings_modal() -> None:
    st.caption("Ajuste a naturalidade da voz em portugues para a Narrativa da Rodada.")

    voice_modes = ["Automatico", "Edge Natural"]
    current_voice_mode = str(st.session_state.get("story_tts_voice_mode", "Automatico"))
    if current_voice_mode not in voice_modes:
        current_voice_mode = "Automatico"

    selected_voice_mode = st.selectbox(
        "Preferencia de voz no navegador",
        voice_modes,
        index=voice_modes.index(current_voice_mode),
        key="story_tts_voice_mode_select",
        help="No Microsoft Edge, escolha 'Edge Natural' para priorizar vozes Microsoft Online/Natural em portugues quando instaladas.",
    )
    st.session_state.story_tts_voice_mode = selected_voice_mode

    voice_hint = st.text_input(
        "Nome da voz (opcional)",
        value=str(st.session_state.get("story_tts_voice_hint", "")),
        key="story_tts_voice_hint_input",
        help="Exemplo no Edge: Maria, Francisca, Antonio ou nome completo da voz instalada no sistema.",
    )
    st.session_state.story_tts_voice_hint = voice_hint.strip()

    presets = {
        "Lenta": 0.86,
        "Natural": 0.94,
        "Rapida": 1.04,
    }
    current_rate = float(st.session_state.get("story_tts_rate", 0.94))
    if current_rate <= 0.89:
        default_preset = "Lenta"
    elif current_rate >= 1.0:
        default_preset = "Rapida"
    else:
        default_preset = "Natural"

    preset = st.selectbox(
        "Preset de velocidade",
        list(presets.keys()),
        index=list(presets.keys()).index(default_preset),
        key="story_tts_speed_preset",
    )

    c_apply, _ = st.columns([1, 1])
    with c_apply:
        if st.button("Aplicar preset", use_container_width=True, key="story_tts_apply_preset"):
            st.session_state.story_tts_rate = presets[preset]
            st.rerun()

    st.session_state.story_tts_rate = st.slider(
        "Velocidade da fala",
        min_value=0.70,
        max_value=1.30,
        value=float(st.session_state.get("story_tts_rate", 0.94)),
        step=0.01,
        key="story_tts_rate_slider",
        help="Valores menores soam mais pausados; maiores soam mais rapidos.",
    )
    st.session_state.story_tts_pitch = st.slider(
        "Entonacao (pitch)",
        min_value=0.70,
        max_value=1.40,
        value=float(st.session_state.get("story_tts_pitch", 1.02)),
        step=0.01,
        key="story_tts_pitch_slider",
    )
    st.session_state.story_tts_volume = st.slider(
        "Volume",
        min_value=0.0,
        max_value=1.0,
        value=float(st.session_state.get("story_tts_volume", 1.0)),
        step=0.01,
        key="story_tts_volume_slider",
    )
    st.caption(
        f"Atual: velocidade {st.session_state.story_tts_rate:.2f} | "
        f"entonacao {st.session_state.story_tts_pitch:.2f} | "
        f"volume {st.session_state.story_tts_volume:.2f}"
    )
    st.caption(
        "Dica: para maior naturalidade no Edge, instale vozes PT-BR no Windows e use 'Edge Natural'."
    )

    if st.button("Fechar", use_container_width=True, key="close_story_tts_settings"):
        st.session_state.show_story_tts_settings_card = False
        st.rerun()


def end_player_turn() -> None:
    game = get_game()
    if game["ended"]:
        return
    ai_turn()
    check_endgame()
    register_turn_story()
    if not game["ended"]:
        game["turn"] += 1
        begin_turn("player")


@st.dialog("Escolha seu Time")
def render_team_modal_card() -> None:
    render_setup_team_modal_card()


@st.dialog("Escolher Doutrina")
def render_doctrine_modal_card() -> None:
    if st.button("←", key="modal_back_from_doctrine", help="Voltar para escolha de time"):
        st.session_state.onboarding_step_card = "doctrine"
        st.session_state.show_doctrine_modal_card = False
        st.session_state.show_team_modal_card = True
        st.rerun()
    render_doctrine_selection_step()


@st.dialog("Configurar IA Adversaria")
def render_ai_modal_card() -> None:
    if st.button("←", key="modal_back_from_ai", help="Voltar para escolha de doutrina"):
        st.session_state.onboarding_step_card = "doctrine"
        st.session_state.show_ai_modal_card = False
        st.session_state.show_doctrine_modal_card = True
        st.rerun()
    render_setup_ai_modal_card()


def render_setup_screen_card() -> None:
    wizard = st.session_state.setup_wizard_card

    st.markdown('<div class="main-title">RED TEAM vs BLUE TEAM // CARD ARENA</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">duelo estrategico OSI em formato de trading cards</div>', unsafe_allow_html=True)
    with st.container(border=True):
        render_image_slot(
            wizard["presentation_image"],
            "Espaco reservado para sua imagem principal da tela inicial.",
            min_height=280,
        )
    if st.button("Jogar", use_container_width=True, key="wizard_open_team_modal"):
        st.session_state.show_team_modal_card = True
        st.rerun()

    step = st.session_state.onboarding_step_card
    if step == "doctrine":
        st.divider()
        st.markdown("<div class='wizard-heading'>Doutrinas prontas para selecao</div>", unsafe_allow_html=True)
        st.caption("Abra o modal grande para escolher a doutrina do seu time.")
        if st.button("Abrir doutrinas", use_container_width=True, key="wizard_open_doctrine_modal"):
            st.session_state.show_doctrine_modal_card = True
            st.rerun()
    elif step == "ai_config":
        st.divider()
        st.markdown("<div class='wizard-heading'>Configuracao da IA pronta para revisao</div>", unsafe_allow_html=True)
        st.caption("Abra o modal para ajustar provedor, modelo e endpoint antes de iniciar.")
        if st.button("Abrir configuracao da IA", use_container_width=True, key="wizard_open_ai_modal"):
            st.session_state.show_ai_modal_card = True
            st.rerun()

    if st.session_state.show_team_modal_card:
        render_team_modal_card()

    if st.session_state.show_doctrine_modal_card:
        render_doctrine_modal_card()

    if st.session_state.show_ai_modal_card:
        render_ai_modal_card()

    if st.button("Reiniciar onboarding", use_container_width=True, key="wizard_reset_flow"):
        st.session_state.onboarding_step_card = "landing"
        st.session_state.show_team_modal_card = False
        st.session_state.show_doctrine_modal_card = False
        st.session_state.show_ai_modal_card = False
        st.session_state.ai_test_result_card = None
        st.rerun()


def render_hand_controls() -> None:
    game = get_game()

    st.markdown("### Sua Mao")
    if not game["hand_player"]:
        st.caption("Sem cartas na mao.")
        return

    total_cards = len(game["hand_player"])
    st.caption(f"Total de cartas na mao: {total_cards}")

    visible_indices = list(range(total_cards))
    cards_per_row = get_responsive_hand_visible_count()
    for row_start in range(0, len(visible_indices), cards_per_row):
        row_indices = visible_indices[row_start:row_start + cards_per_row]
        missing_slots = cards_per_row - len(row_indices)
        if missing_slots > 0:
            side_gap = missing_slots / 2
            row_cols = st.columns([side_gap] + [1] * len(row_indices) + [side_gap])
            active_cols = row_cols[1:-1]
        else:
            active_cols = st.columns(cards_per_row)

        for col, idx in zip(active_cols, row_indices):
            card_id = game["hand_player"][idx]
            card = CARD_DB[card_id]
            with col:
                _, center_col, _ = st.columns([0.2, 1, 0.2])
                with center_col:
                    st.markdown(render_card_html(card_id, art_variant="thumb"), unsafe_allow_html=True)
                    with st.container(key=f"open_card_head_click_{idx}"):
                        if st.button(
                            "🔍",
                            key=f"open_card_{idx}",
                            use_container_width=False,
                        ):
                            st.session_state.hand_modal_index = idx
                            st.rerun()
                    _, btn_r = st.columns([1, 1])
                    with btn_r:
                        playable = is_card_playable("player", card)
                        if playable:
                            with st.container(key=f"quick_play_click_{idx}"):
                                if st.button(
                                    "Jogar",
                                    key=f"quick_play_{idx}",
                                    use_container_width=False,
                                ):
                                    if play_card("player", idx):
                                        st.rerun()


@st.dialog("Carta em Destaque", dismissible=True, width="large")
def render_card_modal() -> None:
    game = get_game()
    idx = st.session_state.hand_modal_index
    if idx is None:
        return
    if idx < 0 or idx >= len(game["hand_player"]):
        st.session_state.hand_modal_index = None
        st.rerun()

    card_id = game["hand_player"][idx]
    card = CARD_DB[card_id]
    role_txt = card_role_text(card)
    timing_txt = card_timing_hint(card)
    impact_txt = card_impact_hint(card)
    affordable = can_pay(game["mana_player"], card.get("cost", {})) if card["type"] != "Node" else True

    st.markdown("<div class='modal-shell'>", unsafe_allow_html=True)
    left, right = st.columns([1.05, 1.6])
    with left:
        _, card_center, _ = st.columns([0.1, 0.8, 0.1])
        with card_center:
            st.markdown(
                f"<div class='modal-card-wrap'><div class='modal-card-scale'>{render_card_html(card_id, art_variant='full')}</div></div>",
                unsafe_allow_html=True,
            )
    with right:
        st.markdown(f"<div class='modal-title'>{card['name']}</div>", unsafe_allow_html=True)
        st.markdown(
            f"<span class='modal-badge'>Tipo: {card['type']}</span>"
            f"<span class='modal-badge'>Camada: {card.get('osi', '?')}</span>"
            f"<span class='modal-badge'>Raridade: {card.get('rarity', 'C')}</span>",
            unsafe_allow_html=True,
        )
        st.markdown(
            f"<span class='modal-badge'>Custo: {mana_to_str(card.get('cost', {}))}</span>"
            f"<span class='modal-badge'>Mana atual: {game['mana_player']}</span>"
            f"<span class='modal-badge'>Pode jogar agora: {'SIM' if affordable else 'NAO'}</span>",
            unsafe_allow_html=True,
        )
        st.markdown(mana_hack_legend_html(), unsafe_allow_html=True)
        st.markdown(f"<div class='modal-copy'><b>Efeito:</b> {card.get('text', '-')}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='modal-copy'><b>Flavor:</b> {card.get('flavor', '-')}</div>", unsafe_allow_html=True)
        st.markdown("<div class='modal-sub'>Papel Tatico</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='modal-copy'>{role_txt}</div>", unsafe_allow_html=True)
        st.markdown("<div class='modal-sub'>Quando Usar</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='modal-copy'>{timing_txt}</div>", unsafe_allow_html=True)
        st.markdown("<div class='modal-sub'>Impacto Esperado</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='modal-copy'>{impact_txt}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    playable = is_card_playable("player", card)
    if playable and st.button("Jogar carta", use_container_width=True):
        if play_card("player", idx):
            st.session_state.hand_modal_index = None
            st.rerun()


@st.dialog("Carta em Campo", dismissible=True, width="large")
def render_board_card_modal() -> None:
    game = get_game()
    target = st.session_state.board_modal_target
    if not target:
        return

    side = target.get("side")
    idx = target.get("index")
    if side not in ("player", "ai"):
        st.session_state.board_modal_target = None
        st.rerun()

    board = game.get(f"board_{side}", [])
    if not isinstance(idx, int) or idx < 0 or idx >= len(board):
        st.session_state.board_modal_target = None
        st.rerun()

    perm = board[idx]
    card_id = perm["card_id"]
    card = CARD_DB[card_id]
    role_txt = card_role_text(card)
    timing_txt = card_timing_hint(card)
    impact_txt = card_impact_hint(card)

    status_badges = []
    if card["type"] == "Agent":
        status_badges.append(f"ATK atual: {perm['atk'] + perm.get('temp_atk', 0)}")
        status_badges.append(f"HP atual: {perm['hp']}")
    status_badges.append(f"Virada: {'SIM' if perm.get('tapped') else 'NAO'}")
    status_badges.append(f"Invoc. recente: {'SIM' if perm.get('summon_sick') else 'NAO'}")

    owner = "Jogador" if side == "player" else "IA"

    st.markdown("<div class='modal-shell'>", unsafe_allow_html=True)
    left, right = st.columns([1.05, 1.6])
    with left:
        _, card_center, _ = st.columns([0.1, 0.8, 0.1])
        with card_center:
            st.markdown(
                f"<div class='modal-card-wrap'><div class='modal-card-scale'>{render_card_html(card_id, perm, art_variant='full')}</div></div>",
                unsafe_allow_html=True,
            )
    with right:
        st.markdown(f"<div class='modal-title'>{card['name']} ({owner})</div>", unsafe_allow_html=True)
        st.markdown(
            f"<span class='modal-badge'>Tipo: {card['type']}</span>"
            f"<span class='modal-badge'>Camada: {card.get('osi', '?')}</span>"
            f"<span class='modal-badge'>Raridade: {card.get('rarity', 'C')}</span>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "".join(f"<span class='modal-badge'>{html.escape(b)}</span>" for b in status_badges),
            unsafe_allow_html=True,
        )
        st.markdown(mana_hack_legend_html(), unsafe_allow_html=True)
        st.markdown(f"<div class='modal-copy'><b>Efeito:</b> {card.get('text', '-')}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='modal-copy'><b>Flavor:</b> {card.get('flavor', '-')}</div>", unsafe_allow_html=True)
        st.markdown("<div class='modal-sub'>Papel Tatico</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='modal-copy'>{role_txt}</div>", unsafe_allow_html=True)
        st.markdown("<div class='modal-sub'>Janela de Impacto</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='modal-copy'>{timing_txt}</div>", unsafe_allow_html=True)
        st.markdown("<div class='modal-sub'>Impacto Esperado</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='modal-copy'>{impact_txt}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("Fechar detalhe", use_container_width=True):
        st.session_state.board_modal_target = None
        st.rerun()


def render_attack_controls() -> None:
    game = get_game()
    st.markdown("### Combate")

    attacker_options = []
    for idx in creature_indices(game["board_player"]):
        perm = game["board_player"][idx]
        card = CARD_DB[perm["card_id"]]
        if not perm["tapped"] and not perm["summon_sick"]:
            attacker_options.append((idx, f"{card['name']} ({perm['atk'] + perm.get('temp_atk', 0)}/{perm['hp']})"))

    labels = [x[1] for x in attacker_options]
    selected_labels = st.multiselect("Declare atacantes", options=labels, default=[])
    selected_indices = [attacker_options[labels.index(lbl)][0] for lbl in selected_labels]

    can_attack = bool(selected_indices) and game["phase"] == "main" and game["active_side"] == "player" and not game["ended"]
    if st.button("Executar ataque", disabled=not can_attack):
        combat("player", selected_indices)
        check_endgame()
        st.rerun()


def render_game_screen_card() -> None:
    game = get_game()

    st.markdown('<div class="main-title">RED TEAM vs BLUE TEAM // CARD ARENA</div>', unsafe_allow_html=True)
    st.markdown(
        f"<div class='sub-title'>Turno {game['turn']}/{game['max_turns']} | Voce: {game['player_team'].upper()} | IA: {game['ai_team'].upper()}</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        f"<span class='info-chip'>Status IA</span>"
        f"<span class='info-chip'>Vida IA: {game['life_ai']}</span>"
        f"<span class='info-chip'>Deck IA: {len(game['deck_ai'])}</span>",
        unsafe_allow_html=True,
    )
    render_board("ai", "Battlefield da IA")
    render_board("player", "Seu Battlefield")
    st.markdown(
        f"<span class='info-chip'>Status Jogador</span>"
        f"<span class='info-chip'>Vida Jogador: {game['life_player']}</span>"
        f"<span class='info-chip'>Mana: {game['mana_player']}</span>"
        f"<span class='info-chip'>Deck Jogador: {len(game['deck_player'])}</span>"
        f"<span class='info-chip'>Fase: {game['phase']}</span>",
        unsafe_allow_html=True,
    )

    st.divider()
    tab_play, tab_console, tab_dashboard, tab_lore = st.tabs(["Operacoes", "Console de Batalha", "Dashboard Status", "Lore OSI"])

    with tab_play:
        render_hand_controls()
        story_title_col, story_cfg_col = st.columns([10, 1])
        with story_title_col:
            st.markdown("### Narrativa da Rodada")
        with story_cfg_col:
            if st.button("⚙️", key="open_story_tts_settings", help="Configurar narracao"):
                st.session_state.show_story_tts_settings_card = True
                st.rerun()
        story = game.get("last_story", "")
        if story:
            st.markdown(f"<div class='story-box'>{story}</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='story-box'>A narrativa da rodada surgira ao fim do primeiro turno completo.</div>", unsafe_allow_html=True)
        render_story_audio_controls(story)

        col_reset = st.columns(1)[0]
        with col_reset:
            if st.button("Resetar partida", use_container_width=True):
                reset_to_setup_flow()
                st.rerun()

    with tab_console:
        st.markdown("### Console de Batalha")
        st.caption("Registro cronologico das jogadas, combates e efeitos aplicados na partida.")
        render_log()

    with tab_dashboard:
        render_status_dashboard_panel(game)

    with tab_lore:
        render_osi_lore_panel(game)

    if game["ended"]:
        render_end_modal(game)
    elif st.session_state.show_story_tts_settings_card:
        render_story_tts_settings_modal()
    elif st.session_state.hand_modal_index is not None:
        render_card_modal()
    elif st.session_state.board_modal_target is not None:
        render_board_card_modal()


@st.dialog("Fim da Operacao")
def render_end_modal(game: dict[str, Any]) -> None:
    winner_team: str | None = None
    loser_team: str | None = None
    winner_message = ""
    loser_message = ""
    if game["winner"] == "player":
        winner_team = game.get("player_team")
        loser_team = game.get("ai_team")
        winner_message = "Vitoria! Seu plano tatico dominou o battlefield."
    elif game["winner"] == "ai":
        winner_team = game.get("ai_team")
        loser_team = game.get("player_team")
        loser_message = "Derrota. A IA controlou ritmo e recursos."
    else:
        st.warning("Empate tecnico apos limite de turnos.")

    victory_images = {
        "red": CARD_ART_DIR / "vitoria_red_team.png",
        "blue": CARD_ART_DIR / "vitoria_blue_team.png",
    }
    defeat_images = {
        "red": CARD_ART_DIR / "derrota_red_team.png",
        "blue": CARD_ART_DIR / "derrota_blue_team.png",
    }
    selected_victory_image = victory_images.get(str(winner_team).lower(), None)
    selected_defeat_image = defeat_images.get(str(loser_team).lower(), None)

    if game["winner"] == "player" and selected_victory_image and selected_victory_image.exists():
        if winner_message:
            encoded = base64.b64encode(selected_victory_image.read_bytes()).decode("ascii")
            st.markdown(
                (
                    "<div style='position:relative;border-radius:12px;overflow:hidden;border:1px solid #2f557f;'>"
                    f"<img src='data:image/png;base64,{encoded}' style='display:block;width:100%;height:auto;'/>"
                    "<div style='position:absolute;inset:0;display:flex;align-items:center;justify-content:center;"
                    "padding:1rem;text-align:center;background:linear-gradient(180deg,rgba(0,0,0,0.18),rgba(0,0,0,0.45));'>"
                    f"<div style='font-family:Orbitron,sans-serif;font-size:1.2rem;letter-spacing:0.4px;"
                    "font-weight:700;color:#e7f7ff;text-shadow:0 0 10px rgba(0,0,0,0.75);'>"
                    f"{html.escape(winner_message)}"
                    "</div></div></div>"
                ),
                unsafe_allow_html=True,
            )
    elif game["winner"] == "ai" and selected_defeat_image and selected_defeat_image.exists():
        st.image(str(selected_defeat_image), use_container_width=True)
        if loser_message:
            st.error(loser_message)
    elif winner_message:
        st.success(winner_message)
    elif loser_message:
        st.error(loser_message)

    st.markdown(f"**Turno final:** {game['turn']}/{game['max_turns']}")
    st.markdown(f"**Vida:** Jogador {game['life_player']} | IA {game['life_ai']}")
    st.markdown(f"**Deck restante:** Jogador {len(game['deck_player'])} | IA {len(game['deck_ai'])}")
    st.caption("Dica: priorize Node cedo para manter curva de mana forte.")

    c1, c2 = st.columns(2)
    with c1:
        if st.button("Jogar de novo", use_container_width=True):
            reset_to_setup_flow()
            st.rerun()
    with c2:
        st.button("Fechar", use_container_width=True)


init_state()

if not st.session_state.setup_done_card:
    render_setup_screen_card()
else:
    render_game_screen_card()
