| O **Kensei AI Foundations** e uma jornada pratica para quem quer entrar no universo de **IA, dados, programacao e automacao**, mesmo comecando do zero. Aqui, o foco nao e so teoria: voce aprende construindo projetos reais, usando IA como copiloto e desenvolvendo as competencias que o mercado ja exige. Ao longo de 8 semanas, voce evolui com desafios mao na massa, apoio da comunidade e um portfolio que prova sua capacidade de resolver problemas reais. Se o objetivo e construir uma carreira **AI-first** com base solida e visao aplicada para tecnologia e cybersecurity, este curso e o ponto de partida. |
|:---:|
| |
|  <a href="https://kensei.seg.br/lab" target="_blank"><img style="margin: 10px" height="100" width="300" src="../img/logo_kensei.png" alt="Logos Kensei"/></a> |

---

<p align="center">
    <img src="../img/Kensei_AI_Foundations_S07_streamlit.png" alt="Semana 7 - Streamlit na pratica" width="1100">
</p>

---

# SEMANA 7 - Streamlit na pratica (projetos do PDF)

> Transformando scripts Python em apps web reais com IA e integracao.

Nesta semana o foco e construir os 5 projetos oficiais da aula:

- projeto 1: calculadora IMC
- projeto 2: dashboard de cyber attacks
- projeto 3: chatbot web com IA
- projeto 4: analisador de PDF com IA
- projeto 5: Streamlit + agente n8n

---

## O que voce vai construir

| Arquivo | Objetivo |
|---|---|
| `01_calculadora_imc.py` | Calcula IMC e classifica automaticamente |
| `02_dashboard_cyber_attacks.py` | Dashboard com dados reais de ataques ciberneticos |
| `03_chatbot_web_ia.py` | Chatbot web moderno com historico de conversas e Gemini |
| `04_analisador_pdf_ia.py` | Upload de PDF + extracao de texto + resumo com IA |
| `05_soc_streamlit_n8n.py` | Interface Streamlit para chamar webhook n8n |
| `requirements.txt` | Dependencias do projeto |
| `.streamlit/config.toml` | Configuracao visual e de servidor do Streamlit |

---

## Projeto 1 - Calculadora IMC

Arquivo: `01_calculadora_imc.py`

Conceitos:
- `st.number_input` para dados numericos
- calculo de IMC com validacao
- classificacao por faixa

Rodar:

```bash
streamlit run 01_calculadora_imc.py
```

---

## Projeto 2 - Dashboard de Cyber Attacks

Arquivo: `02_dashboard_cyber_attacks.py`

Conceitos:
- leitura do dataset `Global_Cybersecurity_Threats_2015-2024.csv`
- `@st.cache_data` para performance
- dark mode com layout moderno
- filtros por tipo de ataque, pais, setor e periodo
- KPIs de perdas financeiras e usuarios afetados
- mapa mundial interativo com detalhes por pais
- graficos com Plotly (barra, linha, treemap, scatter e heatmap)

Rodar:

```bash
streamlit run 02_dashboard_cyber_attacks.py
```
<p align="center">
    <img src="../img/Kensei_AI_Foundations_S07_Streamlit-02_dashboard_cyber_attacks.png" alt="Semana 7 - Streamlit na pratica" width="1100">
    <img src="../img/Kensei_AI_Foundations_S07_Streamlit-02_dashboard_cyber_attacks02.png" alt="Semana 7 - Streamlit na pratica" width="1100">
</p>

---

## Projeto 3 - Chatbot Web com IA

Arquivo: `03_chatbot_web_ia.py`

Conceitos:
- `st.chat_message` e `st.chat_input`
- gerenciamento de conversas na sidebar
- sugestoes clicaveis de perguntas
- integracao com Google Gemini (com fallback demo sem chave)
- continuacao automatica de respostas longas

Rodar:

```bash
streamlit run 03_chatbot_web_ia.py
```

<p align="center">
    <img src="../img/Kensei_AI_Foundations_S07_Streamlit-03_chatbot_web_ia01.png" alt="Semana 7 - Streamlit na pratica" width="1100">
    <img src="../img/Kensei_AI_Foundations_S07_Streamlit-03_chatbot_web_ia02.png" alt="Semana 7 - Streamlit na pratica" width="1100">
</p>

---

## Projeto 4 - Analisador de PDF com IA

Arquivo: `04_analisador_pdf_ia.py`

Conceitos:
- upload de arquivo com `st.file_uploader`
- extracao de texto com `pypdf`
- resumo com Google Gemini (quando `GOOGLE_API_KEY` estiver definida)

Rodar:

```bash
streamlit run 04_analisador_pdf_ia.py
```

<p align="center">
    <img src="../img/Kensei_AI_Foundations_S07_Streamlit-04_analisador_pdf_ia.png" alt="Semana 7 - Streamlit na pratica" width="1100">
</p>

---

## Projeto 5 - Streamlit + Agente n8n (Integracao)

Arquivo: `05_soc_streamlit_n8n.py`
Workflow n8n (importavel): `05_agente_n8n_soc_webhook.json`

Conceitos:
- formulario Streamlit para evento SOC
- chamada HTTP para webhook n8n com `requests`
- visualizacao da resposta JSON do agente

Importar no n8n:
1. Abra o n8n e clique em `Import from File`
2. Selecione `05_agente_n8n_soc_webhook.json`
3. Ative o workflow
4. Copie a URL de producao do webhook (formato `.../webhook/soc-triagem`)
5. Configure em `N8N_SOC_WEBHOOK_URL` no `.env`

Importante:
- Link do editor (`.../workflow/new?...`) NAO executa automacao.
- O Streamlit precisa da URL do webhook (`/webhook/...` ou `/webhook-test/...`).

Rodar:

```bash
streamlit run 05_soc_streamlit_n8n.py
```
<p align="center">
    <img src="../img/Kensei_AI_Foundations_S07_Streamlit-05_soc_streamlit_n8n01.png" alt="Semana 7 - Streamlit na pratica" width="1100">
    <img src="../img/Kensei_AI_Foundations_S07_Streamlit-05_soc_streamlit_n8n02.png" alt="Semana 7 - Streamlit na pratica" width="1100">
    <img src="../img/Kensei_AI_Foundations_S07_Streamlit-05_soc_streamlit_n8n03.png" alt="Semana 7 - Streamlit na pratica" width="1100">
</p>
---

## Instalar dependencias

```bash
pip install -r requirements.txt
```

Variaveis de ambiente opcionais:

- `GOOGLE_API_KEY` para projetos 3 e 4 (obtenha em [Google AI Studio](https://aistudio.google.com/app/apikey))
- `N8N_SOC_WEBHOOK_URL` para projeto 5

---

## Deploy rapido (Streamlit Community Cloud)

1. Suba o repositorio no GitHub
2. Acesse share.streamlit.io
3. Clique em `New app`
4. Selecione o repo e um app principal (ex.: `semana-07/02_dashboard_cyber_attacks.py`)
5. Deploy

Dica:
- Se usar APIs, configure segredos no painel da plataforma em vez de hardcode no codigo.

---

## Resultado da semana

Ao final da semana 07, voce tera:

- 5 apps oficiais da aula implementados
- dashboard real de cyber attacks
- exemplos de IA aplicados a chat, PDF e automacao com n8n
