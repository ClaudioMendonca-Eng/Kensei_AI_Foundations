| O **Kensei AI Foundations** e uma jornada pratica para quem quer entrar no universo de **IA, dados, programacao e automacao**, mesmo comecando do zero. Aqui, o foco nao e so teoria: voce aprende construindo projetos reais, usando IA como copiloto e desenvolvendo as competencias que o mercado ja exige. Ao longo de 8 semanas, voce evolui com desafios mao na massa, apoio da comunidade e um portfolio que prova sua capacidade de resolver problemas reais. Se o objetivo e construir uma carreira **AI-first** com base solida e visao aplicada para tecnologia e cybersecurity, este curso e o ponto de partida. |
|:---:|
| |
|  <a href="https://kensei.seg.br/lab" target="_blank"><img style="margin: 10px" height="100" width="300" src="../img/logo_kensei.png" alt="Logos Kensei"/></a> |

---

<p align="center">
    <img src="../img/Kensei_AI_Foundations_S05_n8n.png" alt="Semana 5 - Automação com n8n" width="1100">
</p>

---

# SEMANA 5 — Automação com n8n

> **Conectando o mundo sem escrever código**
> *Workflows visuais que fazem o trabalho repetitivo por você*

---

## O Que é Automação?

**Automação = computador fazendo trabalho repetitivo por você, 24h por dia.**

Toda tarefa manual que você faz mais de uma vez por semana é candidata a ser automatizada. Email de relatório? Backup? Notificação? Coleta de dados? Tudo automatizável.

| Trigger | O que faz |
|---------|-----------|
| *"Toda segunda 9h"* | Coleta dados de vendas, gera relatório e manda no email do chefe |
| *"Quando chegar email"* | IA classifica, salva anexos, e responde se for urgente |
| *"Se site cair"* | Notifica equipe no Slack e abre ticket automaticamente |
| *"Novo registro CRM"* | Cria contato no Mailchimp, planilha e envia welcome |

---

## O Que é o n8n?

n8n é uma ferramenta **visual** de automação. Você conecta caixinhas (nodes) na tela e cria fluxos.

Pense num quebra-cabeça: cada peça faz uma coisa (ler email, enviar mensagem, chamar IA, salvar no banco). Você monta o fluxo arrastando e conectando.

**No-code (sem código) ou Low-code (pouco código)** — a IA pode te ajudar a configurar tudo.

### Por que n8n e não Zapier/Make?

| Vantagem | Detalhe |
|----------|---------|
| **Open Source** | Código aberto, gratuito self-hosted |
| **Roda na sua máquina** | Seus dados ficam com você |
| **400+ integrações** | Slack, Email, Sheets, Telegram, OpenAI... |
| **Lógica avançada** | IFs, loops, transformações — sem limite |

---

## Conceitos Essenciais

| Conceito | Descrição |
|----------|-----------|
| **Workflow** | O fluxo completo. Uma sequência de ações que executam juntas. Ex: "enviar relatório diário" |
| **Node** | Cada caixinha = uma ação. Ex: "ler email", "chamar OpenAI", "salvar no Sheets". Cada node faz UMA coisa |
| **Trigger** | O que dispara o workflow. Pode ser horário (toda 9h), evento (chegou email) ou manual |
| **Connection** | A linha que liga os nodes. Define a ordem e passa dados de um node para outro |

> **Estrutura:** `Trigger → Node → Node → Node = Workflow`. Simples assim!

---

## Como Instalar o n8n

### Opção 1: n8n Cloud (mais fácil)

Direto no navegador, sem instalar nada.

1. Acesse [n8n.io/cloud](https://n8n.io/cloud)
2. Criar conta grátis (14 dias trial)
3. Pronto, começa a usar!

> *Boa para: testar e aprender rápido. Após trial: a partir de US$20/mês.*

### Opção 2: n8n Local via Docker (grátis sempre) ✅ Recomendado

Roda no seu computador. Dados ficam com você.

```bash
# Forma básica (sem persistência de dados)
docker run -it --rm \
  -p 5678:5678 \
  n8nio/n8n

# Com volume para persistir workflows (recomendado)
docker run -it --rm \
  -p 5678:5678 \
  -v n8n_data:/home/node/.n8n \
  n8nio/n8n
```

Depois acesse: **http://localhost:5678**

> **Windows (PowerShell):**
> ```powershell
> docker run -it --rm -p 5678:5678 -v n8n_data:/home/node/.n8n n8nio/n8n
> ```

---

## Os 4 Workflows desta Semana

### Workflow 01 — Frase Motivacional → Google Sheets

**Arquivo:** [`01_primeiro_workflow.json`](01_primeiro_workflow.json)

**Fluxo:** `Manual Trigger → OpenAI → Google Sheets`

```
[▶ Manual Trigger] → [🤖 OpenAI] → [📊 Google Sheets]
```

| Node | Tipo | O que faz |
|------|------|-----------|
| Manual Trigger | Trigger | Botão "Execute workflow" para testar |
| OpenAI | Action | Gera frase motivacional para cyber |
| Google Sheets | Action | Append row: data + frase gerada |

**Como importar:**
1. No n8n: `+ New Workflow → ⋮ → Import from file`
2. Selecione `01_primeiro_workflow.json`
3. Configure credenciais: OpenAI API key + Google Sheets OAuth

---

### Workflow 02 — Notificador de Site Down

**Arquivo:** [`02_notificador_site.json`](02_notificador_site.json)

**Fluxo:** `Schedule (5min) → HTTP Request → IF → Telegram`

```
[⏰ Schedule] → [🌐 HTTP Request] → [? IF] → [📱 Telegram - DOWN]
                                          ↘ [📱 Telegram - OK]
```

| Node | Tipo | O que faz |
|------|------|-----------|
| Schedule | Trigger | Dispara a cada 5 minutos |
| HTTP Request | Action | GET no site, retorna status code |
| IF | Logic | Se status != 200 → site fora do ar |
| Telegram | Action | Manda alerta DOWN ou mensagem de OK |

**Credenciais necessárias:**
- Bot do Telegram (criar em @BotFather)
- Seu Chat ID do Telegram

---

### Workflow 03 — Threat Intel Diário com IA

**Arquivo:** [`03_threat_intel_diario.json`](03_threat_intel_diario.json)

**Fluxo:** `Schedule (8h) → 3x RSS Feeds → Merge → Filter 24h → OpenAI → Aggregate → Email`

```
[⏰ 8h] → [📰 THN RSS  ] ↘
          [📰 Bleeping ] → [Merge] → [Filter 24h] → [🤖 OpenAI] → [Aggregate] → [📧 Email]
          [📰 Krebs    ] ↗
```

| Node | Tipo | O que faz |
|------|------|-----------|
| Schedule | Trigger | Toda manhã às 8h |
| RSS (x3) | Action | The Hacker News, BleepingComputer, KrebsOnSecurity |
| Filter | Logic | Só notícias das últimas 24h |
| OpenAI | Action | Resume + classifica criticidade (🔴🟡🟢) |
| Aggregate | Transform | Une todos os resumos |
| Email | Action | Digest com links das fontes |

> **Briefing diário de cyber em 30 segundos.** Você começa o dia já sabendo o que está acontecendo no mundo.

---

### Workflow 04 — API Pessoal com Webhook

**Arquivo:** [`04_api_sentimento.json`](04_api_sentimento.json)

**Fluxo:** `Webhook (POST) → OpenAI → Code → Respond JSON`

```
[🪝 Webhook POST] → [🤖 OpenAI] → [</> Code] → [📤 Respond JSON]
```

| Node | Tipo | O que faz |
|------|------|-----------|
| Webhook | Trigger | Recebe POST com campo `texto` |
| OpenAI | Action | Classifica sentimento + extrai palavras-chave |
| Code | Transform | Parseia JSON da IA, trata erros |
| Respond | Action | Retorna JSON estruturado ao chamador |

**Como testar a API:**

```bash
# No terminal (Linux/Mac/Git Bash):
curl -X POST http://localhost:5678/webhook/sentiment \
  -H "Content-Type: application/json" \
  -d '{"texto":"Adorei o curso da Kensei! Aprendi muito sobre IA."}'

# PowerShell (Windows):
Invoke-RestMethod -Method POST `
  -Uri "http://localhost:5678/webhook/sentiment" `
  -ContentType "application/json" `
  -Body '{"texto":"Adorei o curso da Kensei! Aprendi muito sobre IA."}'
```

**Resposta esperada:**
```json
{
  "sentimento": "positivo",
  "confianca": 0.97,
  "palavras_chave": ["Kensei", "curso", "IA", "aprendi"],
  "resumo": "Texto expressa entusiasmo e satisfação com o aprendizado",
  "texto_recebido": "Adorei o curso da Kensei! ...",
  "processado_em": "2026-05-04T21:00:00.000Z",
  "powered_by": "Kensei AI Foundations - n8n"
}
```

---

## Como Importar Workflows no n8n

### Método 1: Interface Web

1. Abra o n8n no navegador (`http://localhost:5678`)
2. Clique em `+ New Workflow`
3. Menu `⋮` (três pontos) → `Import from file`
4. Selecione o arquivo `.json` desejado
5. Configure as credenciais nos nodes destacados em vermelho
6. Clique em `Save`

### Método 2: Copiar e Colar JSON

1. Abra o arquivo `.json` e copie todo o conteúdo
2. No n8n: `+ New Workflow`
3. Menu `⋮` → `Import from clipboard`
4. Cole o JSON

---

## Configurando Credenciais

### OpenAI
1. Acesse [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. Crie uma API key
3. No n8n: `Settings → Credentials → + Add credential → OpenAI`
4. Cole a API key

### Google Sheets (OAuth2)
1. No n8n: `Settings → Credentials → + Add credential → Google Sheets OAuth2`
2. Configure o OAuth seguindo as instruções (necessário conta Google)
3. Autorize o acesso à planilha

### Telegram Bot
1. Abra o Telegram e busque `@BotFather`
2. Envie `/newbot` e siga as instruções
3. Guarde o token do bot
4. Para seu Chat ID: busque `@userinfobot` e envie qualquer mensagem
5. No n8n: `Settings → Credentials → + Add credential → Telegram`

---

## Boas Práticas e Cuidados

| Prática | Por quê |
|---------|---------|
| **Trate erros** | Adicione node "Error Trigger" para alertas quando algo falhar |
| **Cuidado com credenciais** | n8n armazena suas API keys — configure backup e segurança |
| **Não automatize tudo** | Só automatize processos estáveis e repetitivos |
| **Teste antes de agendar** | Rode manualmente várias vezes antes de deixar rodando sozinho. Bug em loop = caos |

---

## Estrutura da Pasta

```
semana-05/
├── 01_primeiro_workflow.json      ← Manual Trigger → OpenAI → Sheets
├── 02_notificador_site.json       ← Monitor de site down com Telegram
├── 03_threat_intel_diario.json    ← RSS feeds → IA → Email digest
├── 04_api_sentimento.json         ← Webhook API → OpenAI → JSON
├── README.md                      ← Este arquivo
└── bonus/
    ├── pack_1999_templates/       ← 1999 templates prontos para n8n
    │   ├── pack_1999_templates_parte_01.md
    │   ├── ...
    │   └── pack_1999_templates_parte_10.md
    └── pack_mais_58_super_fluxos_templates/   ← 57 super fluxos documentados
        ├── pack_mais_58_super_fluxos_templates_parte_01_03_a_12.md
        ├── ...
        └── pack_mais_58_super_fluxos_templates_parte_06_53_a_59.md
```

---

## Bônus — Packs de Templates

A pasta `bonus/` contém dois packs extras com centenas de workflows prontos para importar no n8n.

### Pack 1999 Templates

Mais de 1999 templates organizados em 10 partes, cobrindo automações de:

- WhatsApp, Telegram, Instagram, YouTube
- Google Sheets, Gmail, Google Drive
- CRM, leads, vendas e SDR
- Cybersecurity, threat intel e monitoramento
- IA com OpenAI, Gemini e outros modelos
- E muito mais...

| Arquivo | Conteúdo |
|---------|----------|
| [`pack_1999_templates_parte_01.md`](bonus/pack_1999_templates/pack_1999_templates_parte_01.md) | Parte 1 |
| [`pack_1999_templates_parte_02.md`](bonus/pack_1999_templates/pack_1999_templates_parte_02.md) | Parte 2 |
| [`pack_1999_templates_parte_03.md`](bonus/pack_1999_templates/pack_1999_templates_parte_03.md) | Parte 3 |
| [`pack_1999_templates_parte_04.md`](bonus/pack_1999_templates/pack_1999_templates_parte_04.md) | Parte 4 |
| [`pack_1999_templates_parte_05.md`](bonus/pack_1999_templates/pack_1999_templates_parte_05.md) | Parte 5 |
| [`pack_1999_templates_parte_06.md`](bonus/pack_1999_templates/pack_1999_templates_parte_06.md) | Parte 6 |
| [`pack_1999_templates_parte_07.md`](bonus/pack_1999_templates/pack_1999_templates_parte_07.md) | Parte 7 |
| [`pack_1999_templates_parte_08.md`](bonus/pack_1999_templates/pack_1999_templates_parte_08.md) | Parte 8 |
| [`pack_1999_templates_parte_09.md`](bonus/pack_1999_templates/pack_1999_templates_parte_09.md) | Parte 9 |
| [`pack_1999_templates_parte_10.md`](bonus/pack_1999_templates/pack_1999_templates_parte_10.md) | Parte 10 |

### Pack 57 Super Fluxos

57 fluxos avançados documentados com diagrama visual (Mermaid) e JSON copiável diretamente para o n8n.

**Como usar:**
1. Abra uma das partes abaixo (Parte 1 a Parte 6)
2. Encontre o fluxo desejado no sumário da parte
3. Copie o bloco `json` da seção **Fluxo (.json)**
4. No n8n: `+ New Workflow → ⋮ → Import from clipboard`

| Arquivo | Conteúdo |
|---------|----------|
| [`pack_mais_58_super_fluxos_templates_parte_01_03_a_12.md`](bonus/pack_mais_58_super_fluxos_templates/pack_mais_58_super_fluxos_templates_parte_01_03_a_12.md) | Templates 3–12 |
| [`pack_mais_58_super_fluxos_templates_parte_02_13_a_22.md`](bonus/pack_mais_58_super_fluxos_templates/pack_mais_58_super_fluxos_templates_parte_02_13_a_22.md) | Templates 13–22 |
| [`pack_mais_58_super_fluxos_templates_parte_03_23_a_32.md`](bonus/pack_mais_58_super_fluxos_templates/pack_mais_58_super_fluxos_templates_parte_03_23_a_32.md) | Templates 23–32 |
| [`pack_mais_58_super_fluxos_templates_parte_04_33_a_42.md`](bonus/pack_mais_58_super_fluxos_templates/pack_mais_58_super_fluxos_templates_parte_04_33_a_42.md) | Templates 33–42 |
| [`pack_mais_58_super_fluxos_templates_parte_05_43_a_52.md`](bonus/pack_mais_58_super_fluxos_templates/pack_mais_58_super_fluxos_templates_parte_05_43_a_52.md) | Templates 43–52 |
| [`pack_mais_58_super_fluxos_templates_parte_06_53_a_59.md`](bonus/pack_mais_58_super_fluxos_templates/pack_mais_58_super_fluxos_templates_parte_06_53_a_59.md) | Templates 53–59 |

**Exemplos de fluxos incluídos:**

| Template | Descrição |
|----------|-----------|
| Template 3 | Relatório Meta por range com Evolution |
| Template 8 | Fluxo Vendedor IA |
| Template 9 | Relatórios Google Ads para múltiplos clientes |
| Template 21 | Resumidor de Grupos WhatsApp |
| Template 46 | Scrape YouTube e Resumo Automático |
| Template 48 | Agente WhatsApp com Planner e pesquisa |
| Template 52 | Corretor imobiliário AI |
| Template 53 | Extração de dados de PDFs com IA |
| Template 57 | Atendimento IA via Telegram |
| Template 59 | Assistente Ana: Presente de Natal |

---

## Para Casa

- [x] Importar e configurar os 4 workflows
- [ ] Criar **UM workflow seu** (resolve um problema real do seu dia a dia)
- [ ] Testar e deixar rodando 1 semana
- [ ] Adicionar prints de cada fluxo funcionando a este README

---

> **Kensei CyberSec Lab | AI Foundations 2026**
> *No-Code = Mais Tempo Pra Pensar.*
> `voce.tempo += horas_economizadas`
