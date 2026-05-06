# PACK 1999 TEMPLATES PARTE 05 - Bloco 6

Templates neste bloco: 20

## Sumário

- [Template 902 - Agente Analista de Dados CoinMarketCap](#template-902)
- [Template 903 - Resposta automática de e-mail com IA e registro em planilha](#template-903)
- [Template 904 - Geração de vídeos com prompts e movimentos de câmera](#template-904)
- [Template 905 - Extração e análise de documentos com Mistral OCR](#template-905)
- [Template 906 - Sincronização de leads de PostgreSQL para Google Sheets](#template-906)
- [Template 907 - Resumo semanal de UX no Slack](#template-907)
- [Template 908 - Chatbot AI para páginas do Confluence](#template-908)
- [Template 909 - Gmail para Notion: criação automática de páginas a partir de emails](#template-909)
- [Template 910 - Resumo horário de mercado cripto (BTC/ETH/SOL)](#template-910)
- [Template 911 - Alerta de bug urgente (Linear → Slack)](#template-911)
- [Template 912 - Verificação por chamadas TTS e email](#template-912)
- [Template 913 - Exportar pedidos Squarespace para Google Sheets](#template-913)
- [Template 914 - Análise de posts do Reddit para oportunidades de negócio](#template-914)
- [Template 915 - Servidor MCP para pesquisa e transcrição do YouTube](#template-915)
- [Template 916 - Busca de emails com Icypeas a partir de planilha](#template-916)
- [Template 917 - Criação automática de rascunhos de resposta Fastmail](#template-917)
- [Template 918 - Varredura de domínios com Icypeas (bulk search)](#template-918)
- [Template 919 - Auto-categorizar posts WordPress](#template-919)
- [Template 920 - Automação de captação e follow-up de leads](#template-920)
- [Template 921 - Batch processing of email verifications with Icypeas](#template-921)

---

<a id="template-902"></a>

## Template 902 - Agente Analista de Dados CoinMarketCap

- **Nome:** Agente Analista de Dados CoinMarketCap
- **Descrição:** Agente multiagente de IA que recebe consultas via Telegram, consulta múltiplas fontes de dados da CoinMarketCap (centralizadas e descentralizadas), sintetiza insights e retorna resultados ao usuário.
- **Funcionalidade:** • Recepção de mensagens via Telegram: recebe consultas dos usuários em tempo real.
• Gestão de sessão: adiciona e rastreia sessionId para manter contexto entre interações.
• Interpretação de linguagem natural: um modelo de IA processa a pergunta do usuário e define ações.
• Memória de contexto: armazena histórico de conversa para consultas sequenciais e contexto de sessão.
• Roteamento para sub-agentes: encaminha solicitações aos agentes especializados (Crypto, Exchange & Community, DEXScan) conforme necessário.
• Consultas a mercados centralizados: obtém listas, cotações, conversões e metadados de criptomoedas.
• Consultas a exchanges e sentimento: recupera informações de exchanges, holdings, índices (ex.: CMC100) e Fear & Greed.
• Consultas a mercados descentralizados: busca pares spot, trades recentes, liquidez e OHLCV histórico/atual de DEXs.
• Coordenação multi-consulta: combina resultados de várias fontes, usa IDs ou símbolos recuperados para chamadas subsequentes e compara dados entre CEX e DEX.
• Validação e prevenção de erros: aplica regras para evitar requisições inválidas (parâmetros obrigatórios, formatos, paginação).
• Entrega de resultados ao usuário: formata e envia a resposta sintetizada de volta pelo Telegram.
- **Ferramentas:** • Telegram: plataforma de mensagens usada para receber perguntas dos usuários e enviar respostas.
• OpenAI (modelo GPT-4o Mini): modelo de linguagem que interpreta consultas, orquestra chamadas aos sub-agentes e sintetiza respostas.
• CoinMarketCap Crypto API: fonte de dados para cotações, listagens, metadados e conversões de criptomoedas.
• CoinMarketCap Exchange & Community API: fonte de dados sobre exchanges, holdings, índices e indicadores de sentimento.
• CoinMarketCap DEXScan API: fonte de dados para pares DEX, liquidez, trades e séries históricas de OHLCV.

## Fluxo visual

```mermaid
flowchart LR
    N1["Telegram Send Message"]
    N2["Adds SessionId"]
    N3["CoinMarketCap AI Data Analyst Agent"]
    N4["CoinMarketCap Agent Brain"]
    N5["CoinMarketCap Memory"]
    N6["CoinMarketCap Crypto Agent Tool"]
    N7["CoinMarketCap Exchange and Community Agent Tool"]
    N8["CoinMarketCap DEXScan Agent Tool"]
    N9["Telegram Input"]
    N10["CMC Multi-Agent Guide"]
    N11["CMC Sticky Note2"]
    N12["CMC Sticky Note"]

    N2 --> N3
    N9 --> N2
    N3 --> N1
```

## Fluxo (.json) :

```json
{
  "id": "mE7Zvhv1lOd4Q3xY",
  "meta": {
    "instanceId": "a5283507e1917a33cc3ae615b2e7d5ad2c1e50955e6f831272ddd5ab816f3fb6"
  },
  "name": "CoinMarketCap_AI_Data_Analyst_Agent",
  "tags": [],
  "nodes": [
    {
      "id": "1eab0bd5-8f9c-4bc4-92b7-50779baa505c",
      "name": "Telegram Send Message",
      "type": "n8n-nodes-base.telegram",
      "position": [
        1180,
        0
      ],
      "webhookId": "0eeae020-ed6f-4900-ae38-d646d893171d",
      "parameters": {
        "text": "={{ $json.output }}",
        "chatId": "={{ $('Telegram Input').item.json.message.chat.id }}",
        "additionalFields": {}
      },
      "credentials": {
        "telegramApi": {
          "id": "R3vpGq0SURbvEw2Z",
          "name": "Telegram account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "fd89fa7e-c4e1-4559-a0cc-42beaeccefb4",
      "name": "Adds SessionId",
      "type": "n8n-nodes-base.set",
      "position": [
        280,
        0
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "b5c25cd4-226b-4778-863f-79b13b4a5202",
              "name": "sessionId",
              "type": "string",
              "value": "={{ $json.message.chat.id }}"
            }
          ]
        },
        "includeOtherFields": true
      },
      "typeVersion": 3.4
    },
    {
      "id": "aea9adc8-8215-4459-9bf0-5a6b6364ffcc",
      "name": "CoinMarketCap AI Data Analyst Agent",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "notes": "{{ $json.sessionId }}",
      "position": [
        660,
        0
      ],
      "parameters": {
        "text": "={{ $json.message.text }}",
        "options": {
          "systemMessage": "You are the **CoinMarketCap AI Data Analyst**, a powerful, multi-source crypto intelligence system that integrates three specialized agents:  \n- **CoinMarketCap Crypto Agent**  \n- **CoinMarketCap Exchange & Community Agent**  \n- **CoinMarketCap DEXScan Agent**\n\nYour job is to provide accurate, real-time, and strategic insights into the cryptocurrency landscape across centralized and decentralized platforms.\n\n---\n\n### 🛠️ Tools and Agent Capabilities\n\nYou have access to a suite of **live CoinMarketCap APIs** organized by sub-agents. Each tool is mapped to an endpoint and validated for parameter safety to avoid 400 errors.\n\n---\n\n#### 🔹 1. CoinMarketCap Crypto Agent\n\n**Focus:** Cryptocurrency-level data, listings, quotes, and conversions.\n\n**Tools:**\n- `Crypto Map` – Get coin IDs, names, symbols  \n- `Crypto Info` – Metadata like whitepapers, socials  \n- `Crypto Listings` – Top market cap coins  \n- `Quotes Latest` – Live price, volume, market cap  \n- `Global Metrics` – Total market stats, BTC dominance  \n- `Price Conversion` – Convert one asset to another  \n\n✅ Use for:  \n“Top 10 coins by market cap,” “Convert 5 ETH to USD,” “BTC volume today,” “Whitepaper for SOL”\n\n---\n\n#### 🔹 2. CoinMarketCap Exchange & Community Agent\n\n**Focus:** Exchange intel, community sentiment, and market behavior.\n\n**Tools:**\n- `Exchange Map` – Discover exchanges and get IDs  \n- `Exchange Info` – Metadata like launch date, country, links  \n- `Exchange Assets` – Exchange token holdings & wallets  \n- `CMC 100 Index` – Latest CMC 100 index constituents  \n- `Fear and Greed Index` – Market sentiment tracker  \n\n✅ Use for:  \n“Which tokens does Binance hold?” “Current crypto sentiment” “Top 100 CMC coins”\n\n---\n\n#### 🔹 3. CoinMarketCap DEXScan Agent\n\n**Focus:** Decentralized trading data (spot pairs, pools, liquidity, OHLCV, trades).\n\n**Tools:**\n- `DEX Metadata` – Info for any DEX (logo, date, description)  \n- `DEX Networks List` – All blockchain networks  \n- `DEX Listings Quotes` – DEXs with live trading stats  \n- `DEX Pair Quotes Latest` – Live price/liquidity for spot pairs  \n- `DEX OHLCV Historical` – Historical OHLCV (e.g., 1h, 1d)  \n- `DEX OHLCV Latest` – Real-time OHLCV for current UTC day  \n- `DEX Trades Latest` – Up to 100 recent trades  \n- `DEX Spot Pairs Latest` – All active spot pairs with filters  \n\n✅ Use for:  \n“Price history of USDT/ETH on Uniswap,” “Show DEXs with highest volume,” “Get liquidity of token pair,” “Security scan for PancakeSwap pools”\n\n---\n\n### ⚙️ Multi-Agent Coordination (Advanced Multi-Query Reasoning)\n\nYou are empowered with **advanced multi-query analysis** capabilities:\n- Chain data between agents (e.g., map → quote → historical chart)\n- Use outputs from one tool as inputs for another\n- Automatically fetch required IDs (e.g., exchange ID, contract address) before making a final API call\n- Combine centralized (CEX) and decentralized (DEX) insights into one unified response\n- Filter and compare across timeframes, assets, exchanges, and networks\n\n---\n\n### ⚠️ Validation & Error Prevention Guidelines\n\nTo prevent 400 Bad Request errors:\n- Always include at least **one required field** per endpoint  \n- Use **valid slugs, symbols, or CoinMarketCap IDs**  \n- Don’t use `convert` and `convert_id` together  \n- Use **comma-separated lists** for multi-inputs (if allowed)  \n- Use documented `aux`, `sort`, `interval` fields only  \n- Handle pagination via `scroll_id` or `start/limit` properly  \n\nIf output is too large:\n> ⚠️ “The requested data exceeds the model’s context limit. Please reduce the scope using filters, limits, or sort.”\n\n---\n\n### ✅ Example Tasks You Can Perform\n- “Get liquidity and 24h volume for ETH/USDC on Polygon”\n- “Compare BTC price on Binance vs Uniswap”\n- “Show top 5 DEXs by volume and their top pairs”\n- “Analyze historical price of SHIBA on Ethereum over last 7 days”\n- “Get CoinMarketCap’s sentiment index and top index coins”\n- “List active spot pairs on Arbitrum with volume > $1M and return price, liquidity, and last 24h % change”\n\n---\n\nYou are a **real-time, multi-source AI analyst** purpose-built to extract deep insights from CoinMarketCap’s centralized and decentralized datasets. Use your agents intelligently, validate your queries, and return precise, structured results.\n\nLet’s analyze the crypto world. 🌍📊🧠\n"
        },
        "promptType": "define"
      },
      "typeVersion": 1.7
    },
    {
      "id": "955f82c6-ce76-4d56-9714-4926a4936cbf",
      "name": "CoinMarketCap Agent Brain",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        420,
        280
      ],
      "parameters": {
        "model": {
          "__rl": true,
          "mode": "list",
          "value": "gpt-4o-mini"
        },
        "options": {}
      },
      "credentials": {
        "openAiApi": {
          "id": "yUizd8t0sD5wMYVG",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "2c253e1f-5a34-4334-8a8a-98c1e9e937cd",
      "name": "CoinMarketCap Memory",
      "type": "@n8n/n8n-nodes-langchain.memoryBufferWindow",
      "position": [
        580,
        280
      ],
      "parameters": {},
      "typeVersion": 1.3
    },
    {
      "id": "0878a84b-14a3-4f8e-b94d-339b1c759f4d",
      "name": "CoinMarketCap Crypto Agent Tool",
      "type": "@n8n/n8n-nodes-langchain.toolWorkflow",
      "position": [
        740,
        280
      ],
      "parameters": {
        "name": "CoinMarketCap_Crypto_Agent_Tool",
        "workflowId": {
          "__rl": true,
          "mode": "list",
          "value": "R4EuB1gx1IpMXCJM",
          "cachedResultName": "JayaFamily Assistant — CoinMarketCap_Crypto_Agent_Tool"
        },
        "workflowInputs": {
          "value": {
            "message": "={{ $fromAI(\"message\",\"Populate this with a relevant message to this subagent\")}}",
            "sessionId": "={{ $json.sessionId }}"
          },
          "schema": [
            {
              "id": "message",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "message",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "sessionId",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "sessionId",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            }
          ],
          "mappingMode": "defineBelow",
          "matchingColumns": [],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "4a6e4ae9-5ba5-48ab-8198-a7cd8c84b0ee",
      "name": "CoinMarketCap Exchange and Community Agent Tool",
      "type": "@n8n/n8n-nodes-langchain.toolWorkflow",
      "position": [
        900,
        280
      ],
      "parameters": {
        "name": "CoinMarketCap_Exchange_and_Community_Agent_Tool",
        "workflowId": {
          "__rl": true,
          "mode": "list",
          "value": "kbJb4VMD3SZlcS2u",
          "cachedResultName": "JayaFamily Assistant — CoinMarketCap_Exchange_and_Community_Agent_Tool"
        },
        "workflowInputs": {
          "value": {
            "message": "={{ $fromAI(\"message\",\"Populate this with a relevant message to this subagent\")}}",
            "sessionId": "={{ $json.sessionId }}"
          },
          "schema": [
            {
              "id": "sessionId",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "sessionId",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "message",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "message",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            }
          ],
          "mappingMode": "defineBelow",
          "matchingColumns": [],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "77ffefe3-9671-4155-baed-d782035b6079",
      "name": "CoinMarketCap DEXScan Agent Tool",
      "type": "@n8n/n8n-nodes-langchain.toolWorkflow",
      "position": [
        1080,
        280
      ],
      "parameters": {
        "name": "CoinMarketCap_DEXScan_Agent_Tool",
        "workflowId": {
          "__rl": true,
          "mode": "list",
          "value": "ImiznkEUWCkKbg1w",
          "cachedResultName": "JayaFamily Assistant — CoinMarketCap_DEXScan_Agent_Tool"
        },
        "workflowInputs": {
          "value": {
            "message": "={{ $fromAI(\"message\",\"Populate this with a relevant message to this subagent\")}}",
            "sessionId": "={{ $json.sessionId }}"
          },
          "schema": [
            {
              "id": "sessionId",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "sessionId",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "message",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "message",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            }
          ],
          "mappingMode": "defineBelow",
          "matchingColumns": [],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "d3fc4697-478b-4e6e-8d42-8138ec614748",
      "name": "Telegram Input",
      "type": "n8n-nodes-base.telegramTrigger",
      "position": [
        -220,
        0
      ],
      "webhookId": "b33d2025-01c2-4386-b677-206a87a1856b",
      "parameters": {
        "updates": [
          "message"
        ],
        "additionalFields": {}
      },
      "credentials": {
        "telegramApi": {
          "id": "R3vpGq0SURbvEw2Z",
          "name": "Telegram account"
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "d1108256-43c3-403f-bb7d-181c6de62f2a",
      "name": "CMC Multi-Agent Guide",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -1600,
        -1600
      ],
      "parameters": {
        "width": 1180,
        "height": 1960,
        "content": "# 📊 CoinMarketCap AI Analyst Agent (n8n Workflow)\n\n## 🧠 Multi-Agent System Overview\nThis is the **primary supervisor agent** for the **CoinMarketCap AI Analyst Workflow**, designed using **modular AI agent architecture** in **n8n**.\n\n⚠️ **This workflow requires 3 external tool workflows to function properly.** You must download, install, and connect the following:\n\n### 🔌 Required Sub-Agent Tools:\n1. **CoinMarketCap_Crypto_Agent_Tool** – Handles cryptocurrency quotes, listings, conversions\n2. **CoinMarketCap_Exchange_and_Community_Agent_Tool** – Handles exchanges, trending tokens, Fear & Greed Index\n3. **CoinMarketCap_DEXScan_Agent_Tool** – Handles decentralized liquidity, pair quotes, OHLCV analysis\n\nOnce installed, these agents enable advanced capabilities:\n\n### ✅ Key AI Functions:\n- Analyze market caps, volumes, supply metrics across coins\n- Track new listings and top gainers/losers\n- Evaluate trading pairs and liquidity in CEX and DEX markets\n- Retrieve sentiment indicators and trending discussions\n\n---\n\n## 🧠 Node Structure Summary\n\n### **1️⃣ Analyst Brain**\n- **Model**: GPT-4o Mini\n- **Function**: Understands user queries, delegates tasks to agents\n\n### **2️⃣ Memory Buffer**\n- Stores session state and context between prompts\n\n### **3️⃣ Tool Triggers**\n- **toolWorkflow()** function calls: \n   - `CoinMarketCap_Crypto_Agent_Tool`\n   - `CoinMarketCap_Exchange_and_Community_Agent_Tool`\n   - `CoinMarketCap_DEXScan_Agent_Tool`\n\n---\n\n## ⚠️ Notes:\n- 📎 Make sure API credentials are installed and valid for each agent\n- 📍 Each tool runs independently but feeds results to the supervisor for synthesis\n- 🧩 Use `message` and `sessionId` parameters consistently in every sub-agent call\n\n# 📊 CoinMarketCap AI Analyst Agent Tools (n8n Workflow) Guide\n\n## 🚀 Workflow Overview\nThe **CoinMarketCap AI Analyst Agent** is a modular AI-powered system built on **n8n** to deliver **real-time crypto market insights**. It connects directly to CoinMarketCap APIs across three specialized agents:\n\n- **Cryptocurrency Agent** – Market listings, quotes, conversions, and token info.\n- **Exchange & Community Agent** – Trending topics, exchange performance, and sentiment.\n- **DEXScan Agent** – Liquidity, trading volume, and OHLC data on decentralized markets.\n\n### 🎯 **Key Capabilities**:\n- Fetch latest token listings and rank movements\n- Track real-time price quotes and convert values between currencies\n- Compare metrics like market cap, volume, and dominance\n- Monitor exchange market pairs and volume\n- Analyze community sentiment and Fear & Greed Index\n- Visualize DEX liquidity and historical trading trends\n\n---\n\n## 🔗 Node Architecture Summary\n\n### **1️⃣ AI Analyst Brain**\n- **Type**: GPT-4o Mini\n- **Function**: Interprets prompts and queries, routes requests to proper sub-agent.\n\n### **2️⃣ Session Memory**\n- **Type**: Memory Buffer\n- **Function**: Maintains query context during conversation.\n\n### **3️⃣ Tool Agents**\n- **Type**: Tool Workflow\n- Cryptocurrency / Exchange / DEXScan agent endpoints trigger APIs with mapped params.\n\n"
      },
      "typeVersion": 1
    },
    {
      "id": "5800cdc3-7d4b-4385-8401-b5913a43a28d",
      "name": "CMC Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1260,
        -1600
      ],
      "parameters": {
        "color": 3,
        "width": 680,
        "height": 600,
        "content": "## ⚠️ Error Handling Guide\n\n| **Error Code** | **Meaning** |\n|---------------|------------|\n| `200` | Success |\n| `400` | Bad Request (invalid query/params) |\n| `401` | Unauthorized (missing or invalid API key) |\n| `429` | Rate Limit Exceeded |\n| `500` | CoinMarketCap server error |\n\n### 🔍 Common Fixes\n- Ensure `symbol`, `slug`, or `id` match valid CoinMarketCap entries\n- Use correct `timestamp`, `network`, and pagination parameters\n- Rate-limit high-frequency queries to avoid 429 errors\n\n---\n\n## 🚀 Need Help?\nFor custom CoinMarketCap agent support, dashboards, or token data automation, connect:\n\n🌐 **Don Jayamaha — LinkedIn**  \n🔗 [http://linkedin.com/in/donjayamahajr](http://linkedin.com/in/donjayamahajr)\n\n© 2025 Treasurium Capital Limited Company. All rights reserved.\nThis AI workflow architecture, including logic, design, and prompt structures, is the intellectual property of Treasurium Capital Limited Company. Unauthorized reproduction, redistribution, or resale is prohibited under U.S. copyright law. Licensed use only.\n"
      },
      "typeVersion": 1
    },
    {
      "id": "068e7732-d92e-4a1d-a4b5-c0ee6363f3fb",
      "name": "CMC Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        0,
        -1600
      ],
      "parameters": {
        "color": 5,
        "width": 900,
        "height": 1500,
        "content": "## 📌 How to Use the Workflow\n\n### ✅ Step 1: Provide Inputs\n- Use token `symbol`, `slug`, or `ID`\n- Set timestamps (`before`, `after`) in **Unix format** for historical data\n- Use `chain`, `limit`, and `start` for pagination when needed\n\n### ✅ Step 2: Execute API Tools\n- The AI routes queries to sub-agents: **Cryptocurrency**, **Exchange**, or **DEXScan**\n\n### ✅ Step 3: Get Response & Output\n- Results can be output to Telegram, dashboards, or n8n HTTP Response nodes\n\n---\n\n## 🗣️ Example Questions to Ask the CMC AI Analyst\n\n### 💬 Market Intelligence\n- \"What are the top 5 tokens by trading volume right now?\"\n- \"Which coins gained the most in the last 24 hours?\"\n- \"What’s the total crypto market cap today?\"\n\n### 💬 Token Insights\n- \"What’s the price of SOL in USD?\"\n- \"How much is 1000 USDT in BTC?\"\n- \"Show me the description and whitepaper link for Dogecoin.\"\n\n### 💬 Exchange & Sentiment\n- \"What’s the Fear & Greed index today?\"\n- \"List exchanges with the highest asset holdings.\"\n- \"Give me info about Binance – when was it launched?\"\n\n### 💬 DEX Data\n- \"Show me the top DEX spot pairs on Ethereum.\"\n- \"What’s the OHLCV data for SOL-USDT on Solana over the last 7 days?\"\n- \"What trades just occurred on PancakeSwap?\"\n\n---\n\n## ⚠️ Example API Queries\n\n### 1️⃣ Get Top 5 Tokens by Volume\n```plaintext\nGET /v1/cryptocurrency/listings/latest?sort=volume_24h&limit=5\n```\n\n### 2️⃣ Convert 1000 USDT to BTC\n```plaintext\nGET /v1/tools/price-conversion?amount=1000&symbol=USDT&convert=BTC\n```\n\n### 3️⃣ Check Fear & Greed Index\n```plaintext\nGET /v3/fear-and-greed/latest\n```\n\n### 4️⃣ Get OHLCV of DEX Pair\n```plaintext\nGET /v4/dex/pairs/ohlcv/historical?network=solana&pair=SOL-USDT&interval=1d\n```\n\n---"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "ed2f29c5-293a-4796-8986-9c5f9980c6c6",
  "connections": {
    "Adds SessionId": {
      "main": [
        [
          {
            "node": "CoinMarketCap AI Data Analyst Agent",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Telegram Input": {
      "main": [
        [
          {
            "node": "Adds SessionId",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "CoinMarketCap Memory": {
      "ai_memory": [
        [
          {
            "node": "CoinMarketCap AI Data Analyst Agent",
            "type": "ai_memory",
            "index": 0
          }
        ]
      ]
    },
    "CoinMarketCap Agent Brain": {
      "ai_languageModel": [
        [
          {
            "node": "CoinMarketCap AI Data Analyst Agent",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "CoinMarketCap Crypto Agent Tool": {
      "ai_tool": [
        [
          {
            "node": "CoinMarketCap AI Data Analyst Agent",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "CoinMarketCap DEXScan Agent Tool": {
      "ai_tool": [
        [
          {
            "node": "CoinMarketCap AI Data Analyst Agent",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "CoinMarketCap AI Data Analyst Agent": {
      "main": [
        [
          {
            "node": "Telegram Send Message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "CoinMarketCap Exchange and Community Agent Tool": {
      "ai_tool": [
        [
          {
            "node": "CoinMarketCap AI Data Analyst Agent",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-903"></a>

## Template 903 - Resposta automática de e-mail com IA e registro em planilha

- **Nome:** Resposta automática de e-mail com IA e registro em planilha
- **Descrição:** Fluxo que, ao receber um e-mail de destinatários configurados, gera uma resposta personalizada usando IA, envia a resposta de volta ao remetente e registra a interação e a resposta gerada em uma planilha. Também permite registrar feedback para futuras melhorias.
- **Funcionalidade:** • Detecção de email recebido: Inicia o fluxo quando chega um e-mail de destinatários configurados e atende aos critérios definidos.
• Extração de conteúdo da mensagem: Obtém o conteúdo relevante da mensagem para processar a resposta.
• Geração de resposta com IA: Cria uma resposta usando o modelo de IA com limites de tokens configuráveis.
• Verificação de limite de tokens: Garante que o reply cabe no limite de tokens; se exceder, procede conforme as regras definidas.
• Envio da resposta: Envia a resposta gerada de volta ao remetente original.
• Acompanhamento com link de feedback: Inclui link de feedback na mensagem para avaliação.
• Armazenamento em planilha: Cria ou utiliza uma planilha para registrar o e-mail original, a resposta gerada e o feedback recebido; adiciona registros para cada interação.
• Geração de UUID: Atribui identificador único para cada interação.
• Página de confirmação de feedback: Gera uma página HTML/explicita para confirmação, quando aplicável.
• Fluxo com gatilho de feedback: Aceita feedback via link para melhoria contínua.
- **Ferramentas:** • Gmail: Serviço de recebimento e envio de e-mails.
• Google Sheets: Serviço de armazenamento de dados e respostas em planilhas.
• OpenAI: Serviço de geração de textos e respostas com IA.

## Fluxo visual

```mermaid
flowchart LR
    N1["Generate reply"]
    N2["On email received"]
    N3["Only continue for specific emails"]
    N4["Configure"]
    N5["Note5"]
    N6["Send reply to recipient"]
    N7["Generate UUID"]
    N8["Thanks for your response!"]
    N9["Extract message content (advanced)"]
    N10["If spreadsheet doesn't exist"]
    N11["Successfully created or updated row"]
    N12["Note1"]
    N13["Note2"]
    N14["Note3"]
    N15["Create spreadsheet"]
    N16["Store spreadsheet ID"]
    N17["Paste data"]
    N18["If no sheet IDs"]
    N19["Create or update rows"]
    N20["Get data from `Format data`"]
    N21["Get data from `Format data` node"]
    N22["Format data"]
    N23["Send email reply"]
    N24["On feedback given"]
    N25["Send feedback for fine-tuned data"]
    N26["Show HTML page"]
    N27["Get sheet IDs #1"]
    N28["Note"]
    N29["If no spreadsheet in configuration #2"]
    N30["Store specific sheet IDs #2"]
    N31["Get sheet IDs #2"]
    N32["If no spreadsheet in configuration #1"]
    N33["Store specific sheet IDs #1"]
    N34["Email template"]
    N35["Record feedback"]
    N36["Fallback route"]
    N37["Identify trigger #2"]
    N38["Identify trigger #1"]
    N39["Do not send unfinished email reply"]
    N40["If reply is complete"]
    N41["Sticky Note"]
    N42["Do not send email to this recipient"]
    N43["Send reply to database"]
    N44["Sticky Note1"]
    N45["Determine which trigger ran"]
    N46["Sticky Note2"]
    N47["Is text within token limit?"]
    N48["Do nothing"]
    N49["Sticky Note3"]

    N4 --> N45
    N22 --> N32
    N7 --> N9
    N34 --> N6
    N1 --> N43
    N1 --> N40
    N26 --> N29
    N18 --> N15
    N18 --> N20
    N35 --> N8
    N27 --> N18
    N31 --> N25
    N23 --> N34
    N2 --> N38
    N24 --> N37
    N15 --> N16
    N38 --> N4
    N37 --> N4
    N40 --> N23
    N40 --> N39
    N16 --> N21
    N19 --> N10
    N43 --> N22
    N8 --> N26
    N45 --> N3
    N45 --> N35
    N45 --> N36
    N20 --> N19
    N47 --> N1
    N47 --> N48
    N33 --> N18
    N30 --> N25
    N10 --> N15
    N10 --> N11
    N21 --> N17
    N3 --> N7
    N3 --> N42
    N9 --> N47
    N32 --> N27
    N32 --> N33
    N29 --> N31
    N29 --> N30
```

## Fluxo (.json) :

```json
{
  "meta": {
    "instanceId": "a2434c94d549548a685cca39cc4614698e94f527bcea84eefa363f1037ae14cd"
  },
  "nodes": [
    {
      "id": "88c0f64c-a7cd-4f35-96dd-9eee4b1d6a1a",
      "name": "Generate reply",
      "type": "n8n-nodes-base.openAi",
      "position": [
        -480,
        2260
      ],
      "parameters": {
        "prompt": "=From: {{ $json.from.value }}\nTo: {{ $json.to.value }}\nSubject: {{ $json.subject }}\nBody: {{ $json.reply }}\n\n\nReply: ",
        "options": {
          "maxTokens": "={{ $('Configure').first().json.replyTokenSize }}"
        }
      },
      "credentials": {
        "openAiApi": {
          "id": "27",
          "name": "[UPDATE ME]"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "7105b689-9f9c-4354-aad9-8f1abb6c0a06",
      "name": "On email received",
      "type": "n8n-nodes-base.gmailTrigger",
      "position": [
        -2460,
        2680
      ],
      "parameters": {
        "simple": false,
        "filters": {},
        "options": {},
        "pollTimes": {
          "item": [
            {
              "mode": "everyMinute"
            }
          ]
        }
      },
      "credentials": {
        "gmailOAuth2": {
          "id": "26",
          "name": "[UPDATE ME]"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "ea18ed9a-0158-45e1-ac1b-1993ace4ff2c",
      "name": "Only continue for specific emails",
      "type": "n8n-nodes-base.if",
      "position": [
        -1360,
        2460
      ],
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{ $('Configure').first().json.recipients.split(',') }}",
              "value2": "*",
              "operation": "contains"
            },
            {
              "value1": "={{ $('Configure').first().json.recipients.split(',') }}",
              "value2": "={{ $json.from.value[0].address }}",
              "operation": "contains"
            }
          ]
        },
        "combineOperation": "any"
      },
      "typeVersion": 1
    },
    {
      "id": "d1425dff-0fc1-4a4b-9202-418ce30d7cd9",
      "name": "Configure",
      "type": "n8n-nodes-base.set",
      "position": [
        -1940,
        2800
      ],
      "parameters": {
        "values": {
          "number": [
            {
              "name": "maxTokenSize",
              "value": 4000
            },
            {
              "name": "replyTokenSize",
              "value": 300
            }
          ],
          "string": [
            {
              "name": "spreadsheetId"
            },
            {
              "name": "worksheetId"
            },
            {
              "name": "spreadsheetName",
              "value": "ChatGPT responses"
            },
            {
              "name": "worksheetName",
              "value": "Database"
            },
            {
              "name": "recipients",
              "value": "[UPDATE ME]"
            }
          ]
        },
        "options": {}
      },
      "typeVersion": 1
    },
    {
      "id": "594f77e6-9e7e-4e93-b6e0-95fad57e42f0",
      "name": "Note5",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -2060,
        2480
      ],
      "parameters": {
        "width": 330.0279884670691,
        "height": 929.4540475960038,
        "content": "### Configuration\nIf you decide to use your own spreadsheet, it is up to you to ensure all columns are present before running this workflow. A good way to do this is to run this workflow once with **empty** `spreadsheetid` and `worksheetId` variables (see the `Configure` node). Then map the output from `Store spreadsheet ID` to this node.\n\nIt is recommended that you specify the `spreadsheetId` and `worksheetId`, since relying solely on a workflow's static data is considered bad practice.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n__`spreadsheetId`__: The ID of the spreadsheet where Pipedrive deals will be stored.\n__`worksheetId`__: The ID of the worksheet where Pipedrive deals will be stored.\n__`spreadsheetName`(required)__: The human readable name of the spreadsheet where Pipedrive deals will be stored.\n__`worksheetName`(required)__: The human readable name of the worksheet in the spreadsheet where Pipedrive deals will be stored.\n__`recipients`(required)__: Comma-separated list of email recipients to send ChatGPT emails to. Use `*` to send ChatGPT response to every email address.\n__`maxTokenSize`(required)__: The maximum token size for the model you choose. See possible models from OpenAI [here](https://platform.openai.com/docs/models/gpt-3).\n__`replyTokenSize`(required)__: The reply's maximum token size. Default is 300. This determines how much text the AI will reply with."
      },
      "typeVersion": 1
    },
    {
      "id": "2dc3e403-f2a0-43c2-a1e4-187d901d692f",
      "name": "Send reply to recipient",
      "type": "n8n-nodes-base.gmail",
      "position": [
        360,
        1860
      ],
      "parameters": {
        "message": "={{ $json.html }}",
        "options": {},
        "emailType": "html",
        "messageId": "={{ $node[\"On email received\"].json.id }}",
        "operation": "reply"
      },
      "credentials": {
        "gmailOAuth2": {
          "id": "26",
          "name": "[UPDATE ME]"
        }
      },
      "typeVersion": 2
    },
    {
      "id": "f845aa4d-5542-4126-a42d-4e5afa1893d1",
      "name": "Generate UUID",
      "type": "n8n-nodes-base.crypto",
      "position": [
        -1140,
        2360
      ],
      "parameters": {
        "action": "generate",
        "dataPropertyName": "uuid"
      },
      "typeVersion": 1
    },
    {
      "id": "3c468585-4546-439b-9e8a-efb7231277d8",
      "name": "Thanks for your response!",
      "type": "n8n-nodes-base.html",
      "position": [
        -1140,
        2980
      ],
      "parameters": {
        "html": "<!DOCTYPE html>\n\n<html>\n<head>\n  <meta charset=\"UTF-8\" />\n  <title>Thanks for your response!</title>\n</head>\n<body>\n  <div class=\"container\">\n    <h1>Thanks for your response!</h1>\n    <h2>You can safely close this window.</h2>\n  </div>\n</body>\n</html>\n\n<style>\n.container {\n  background-color: #ffffff;\n  text-align: center;\n  padding: 16px;\n  border-radius: 8px;\n}\n\nh1 {\n  color: #ff6d5a;\n  font-size: 24px;\n  font-weight: bold;\n  padding: 8px;\n}\n\nh2 {\n  color: #909399;\n  font-size: 18px;\n  font-weight: bold;\n  padding: 8px;\n}\n</style>\n\n<script>\nconsole.log(\"Hello World!\");\n</script>"
      },
      "typeVersion": 1
    },
    {
      "id": "6b0bfa33-84ca-4b9c-98ec-c1bc08a1230d",
      "name": "Extract message content (advanced)",
      "type": "n8n-nodes-base.code",
      "position": [
        -920,
        2360
      ],
      "parameters": {
        "jsCode": "// source: https://gist.github.com/ikbelkirasan/2462073f6c7c760faa6fad7c6a0c4dc3\nvar EmailParser=function(t){var r={};function n(e){if(r[e])return r[e].exports;var o=r[e]={i:e,l:!1,exports:{}};return t[e].call(o.exports,o,o.exports,n),o.l=!0,o.exports}return n.m=t,n.c=r,n.d=function(t,r,e){n.o(t,r)||Object.defineProperty(t,r,{enumerable:!0,get:e})},n.r=function(t){\"undefined\"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:\"Module\"}),Object.defineProperty(t,\"__esModule\",{value:!0})},n.t=function(t,r){if(1&r&&(t=n(t)),8&r)return t;if(4&r&&\"object\"==typeof t&&t&&t.__esModule)return t;var e=Object.create(null);if(n.r(e),Object.defineProperty(e,\"default\",{enumerable:!0,value:t}),2&r&&\"string\"!=typeof t)for(var o in t)n.d(e,o,function(r){return t[r]}.bind(null,o));return e},n.n=function(t){var r=t&&t.__esModule?function(){return t.default}:function(){return t};return n.d(r,\"a\",r),r},n.o=function(t,r){return Object.prototype.hasOwnProperty.call(t,r)},n.p=\"\",n(n.s=59)}([function(t,r){var n=Array.isArray;t.exports=n},function(t,r,n){var e=n(31),o=\"object\"==typeof self&&self&&self.Object===Object&&self,u=e||o||Function(\"return this\")();t.exports=u},function(t,r,n){var e=n(74),o=n(79);t.exports=function(t,r){var n=o(t,r);return e(n)?n:void 0}},function(t,r){t.exports=function(t){return null!=t&&\"object\"==typeof t}},function(t,r){t.exports=function(t){var r=typeof t;return null!=t&&(\"object\"==r||\"function\"==r)}},function(t,r,n){var e=n(6),o=n(75),u=n(76),i=e?e.toStringTag:void 0;t.exports=function(t){return null==t?void 0===t?\"[object Undefined]\":\"[object Null]\":i&&i in Object(t)?o(t):u(t)}},function(t,r,n){var e=n(1).Symbol;t.exports=e},function(t,r,n){var e=n(35),o=n(99),u=n(14);t.exports=function(t){return u(t)?e(t):o(t)}},function(t,r,n){var e=n(64),o=n(65),u=n(66),i=n(67),c=n(68);function a(t){var r=-1,n=null==t?0:t.length;for(this.clear();++r<n;){var e=t[r];this.set(e[0],e[1])}}a.prototype.clear=e,a.prototype.delete=o,a.prototype.get=u,a.prototype.has=i,a.prototype.set=c,t.exports=a},function(t,r,n){var e=n(18);t.exports=function(t,r){for(var n=t.length;n--;)if(e(t[n][0],r))return n;return-1}},function(t,r,n){var e=n(2)(Object,\"create\");t.exports=e},function(t,r,n){var e=n(88);t.exports=function(t,r){var n=t.__data__;return e(r)?n[\"string\"==typeof r?\"string\":\"hash\"]:n.map}},function(t,r,n){var e=n(33),o=n(34);t.exports=function(t,r,n,u){var i=!n;n||(n={});for(var c=-1,a=r.length;++c<a;){var s=r[c],f=u?u(n[s],t[s],s,n,t):void 0;void 0===f&&(f=t[s]),i?o(n,s,f):e(n,s,f)}return n}},function(t,r){t.exports=function(t){return t.webpackPolyfill||(t.deprecate=function(){},t.paths=[],t.children||(t.children=[]),Object.defineProperty(t,\"loaded\",{enumerable:!0,get:function(){return t.l}}),Object.defineProperty(t,\"id\",{enumerable:!0,get:function(){return t.i}}),t.webpackPolyfill=1),t}},function(t,r,n){var e=n(30),o=n(22);t.exports=function(t){return null!=t&&o(t.length)&&!e(t)}},function(t,r,n){var e=n(109),o=n(19),u=n(110),i=n(111),c=n(112),a=n(5),s=n(32),f=s(e),p=s(o),l=s(u),v=s(i),b=s(c),h=a;(e&&\"[object DataView]\"!=h(new e(new ArrayBuffer(1)))||o&&\"[object Map]\"!=h(new o)||u&&\"[object Promise]\"!=h(u.resolve())||i&&\"[object Set]\"!=h(new i)||c&&\"[object WeakMap]\"!=h(new c))&&(h=function(t){var r=a(t),n=\"[object Object]\"==r?t.constructor:void 0,e=n?s(n):\"\";if(e)switch(e){case f:return\"[object DataView]\";case p:return\"[object Map]\";case l:return\"[object Promise]\";case v:return\"[object Set]\";case b:return\"[object WeakMap]\"}return r}),t.exports=h},function(t,r,n){var e=n(29);t.exports=function(t){if(\"string\"==typeof t||e(t))return t;var r=t+\"\";return\"0\"==r&&1/t==-1/0?\"-0\":r}},function(t,r,n){var e=n(8),o=n(69),u=n(70),i=n(71),c=n(72),a=n(73);function s(t){var r=this.__data__=new e(t);this.size=r.size}s.prototype.clear=o,s.prototype.delete=u,s.prototype.get=i,s.prototype.has=c,s.prototype.set=a,t.exports=s},function(t,r){t.exports=function(t,r){return t===r||t!=t&&r!=r}},function(t,r,n){var e=n(2)(n(1),\"Map\");t.exports=e},function(t,r,n){var e=n(80),o=n(87),u=n(89),i=n(90),c=n(91);function a(t){var r=-1,n=null==t?0:t.length;for(this.clear();++r<n;){var e=t[r];this.set(e[0],e[1])}}a.prototype.clear=e,a.prototype.delete=o,a.prototype.get=u,a.prototype.has=i,a.prototype.set=c,t.exports=a},function(t,r,n){(function(t){var e=n(1),o=n(97),u=r&&!r.nodeType&&r,i=u&&\"object\"==typeof t&&t&&!t.nodeType&&t,c=i&&i.exports===u?e.Buffer:void 0,a=(c?c.isBuffer:void 0)||o;t.exports=a}).call(this,n(13)(t))},function(t,r){t.exports=function(t){return\"number\"==typeof t&&t>-1&&t%1==0&&t<=9007199254740991}},function(t,r){t.exports=function(t){return function(r){return t(r)}}},function(t,r,n){(function(t){var e=n(31),o=r&&!r.nodeType&&r,u=o&&\"object\"==typeof t&&t&&!t.nodeType&&t,i=u&&u.exports===o&&e.process,c=function(){try{var t=u&&u.require&&u.require(\"util\").types;return t||i&&i.binding&&i.binding(\"util\")}catch(t){}}();t.exports=c}).call(this,n(13)(t))},function(t,r){var n=Object.prototype;t.exports=function(t){var r=t&&t.constructor;return t===(\"function\"==typeof r&&r.prototype||n)}},function(t,r,n){var e=n(41),o=n(42),u=Object.prototype.propertyIsEnumerable,i=Object.getOwnPropertySymbols,c=i?function(t){return null==t?[]:(t=Object(t),e(i(t),(function(r){return u.call(t,r)})))}:o;t.exports=c},function(t,r,n){var e=n(48);t.exports=function(t){var r=new t.constructor(t.byteLength);return new e(r).set(new e(t)),r}},function(t,r,n){var e=n(0),o=n(29),u=/\\.|\\[(?:[^[\\]]*|([\"'])(?:(?!\\1)[^\\\\]|\\\\.)*?\\1)\\]/,i=/^\\w*$/;t.exports=function(t,r){if(e(t))return!1;var n=typeof t;return!(\"number\"!=n&&\"symbol\"!=n&&\"boolean\"!=n&&null!=t&&!o(t))||(i.test(t)||!u.test(t)||null!=r&&t in Object(r))}},function(t,r,n){var e=n(5),o=n(3);t.exports=function(t){return\"symbol\"==typeof t||o(t)&&\"[object Symbol]\"==e(t)}},function(t,r,n){var e=n(5),o=n(4);t.exports=function(t){if(!o(t))return!1;var r=e(t);return\"[object Function]\"==r||\"[object GeneratorFunction]\"==r||\"[object AsyncFunction]\"==r||\"[object Proxy]\"==r}},function(t,r){var n=\"object\"==typeof global&&global&&global.Object===Object&&global;t.exports=n},function(t,r){var n=Function.prototype.toString;t.exports=function(t){if(null!=t){try{return n.call(t)}catch(t){}try{return t+\"\"}catch(t){}}return\"\"}},function(t,r,n){var e=n(34),o=n(18),u=Object.prototype.hasOwnProperty;t.exports=function(t,r,n){var i=t[r];u.call(t,r)&&o(i,n)&&(void 0!==n||r in t)||e(t,r,n)}},function(t,r,n){var e=n(93);t.exports=function(t,r,n){\"__proto__\"==r&&e?e(t,r,{configurable:!0,enumerable:!0,value:n,writable:!0}):t[r]=n}},function(t,r,n){var e=n(95),o=n(36),u=n(0),i=n(21),c=n(37),a=n(38),s=Object.prototype.hasOwnProperty;t.exports=function(t,r){var n=u(t),f=!n&&o(t),p=!n&&!f&&i(t),l=!n&&!f&&!p&&a(t),v=n||f||p||l,b=v?e(t.length,String):[],h=b.length;for(var y in t)!r&&!s.call(t,y)||v&&(\"length\"==y||p&&(\"offset\"==y||\"parent\"==y)||l&&(\"buffer\"==y||\"byteLength\"==y||\"byteOffset\"==y)||c(y,h))||b.push(y);return b}},function(t,r,n){var e=n(96),o=n(3),u=Object.prototype,i=u.hasOwnProperty,c=u.propertyIsEnumerable,a=e(function(){return arguments}())?e:function(t){return o(t)&&i.call(t,\"callee\")&&!c.call(t,\"callee\")};t.exports=a},function(t,r){var n=/^(?:0|[1-9]\\d*)$/;t.exports=function(t,r){var e=typeof t;return!!(r=null==r?9007199254740991:r)&&(\"number\"==e||\"symbol\"!=e&&n.test(t))&&t>-1&&t%1==0&&t<r}},function(t,r,n){var e=n(98),o=n(23),u=n(24),i=u&&u.isTypedArray,c=i?o(i):e;t.exports=c},function(t,r){t.exports=function(t,r){return function(n){return t(r(n))}}},function(t,r,n){var e=n(35),o=n(102),u=n(14);t.exports=function(t){return u(t)?e(t,!0):o(t)}},function(t,r){t.exports=function(t,r){for(var n=-1,e=null==t?0:t.length,o=0,u=[];++n<e;){var i=t[n];r(i,n,t)&&(u[o++]=i)}return u}},function(t,r){t.exports=function(){return[]}},function(t,r,n){var e=n(44),o=n(45),u=n(26),i=n(42),c=Object.getOwnPropertySymbols?function(t){for(var r=[];t;)e(r,u(t)),t=o(t);return r}:i;t.exports=c},function(t,r){t.exports=function(t,r){for(var n=-1,e=r.length,o=t.length;++n<e;)t[o+n]=r[n];return t}},function(t,r,n){var e=n(39)(Object.getPrototypeOf,Object);t.exports=e},function(t,r,n){var e=n(47),o=n(26),u=n(7);t.exports=function(t){return e(t,u,o)}},function(t,r,n){var e=n(44),o=n(0);t.exports=function(t,r,n){var u=r(t);return o(t)?u:e(u,n(t))}},function(t,r,n){var e=n(1).Uint8Array;t.exports=e},function(t,r,n){var e=n(41),o=n(125),u=n(51),i=n(0);t.exports=function(t,r){return(i(t)?e:o)(t,u(r,3))}},function(t,r,n){var e=n(126),o=n(129)(e);t.exports=o},function(t,r,n){var e=n(130),o=n(143),u=n(153),i=n(0),c=n(154);t.exports=function(t){return\"function\"==typeof t?t:null==t?u:\"object\"==typeof t?i(t)?o(t[0],t[1]):e(t):c(t)}},function(t,r,n){var e=n(132),o=n(3);t.exports=function t(r,n,u,i,c){return r===n||(null==r||null==n||!o(r)&&!o(n)?r!=r&&n!=n:e(r,n,u,i,t,c))}},function(t,r,n){var e=n(133),o=n(136),u=n(137);t.exports=function(t,r,n,i,c,a){var s=1&n,f=t.length,p=r.length;if(f!=p&&!(s&&p>f))return!1;var l=a.get(t);if(l&&a.get(r))return l==r;var v=-1,b=!0,h=2&n?new e:void 0;for(a.set(t,r),a.set(r,t);++v<f;){var y=t[v],x=r[v];if(i)var d=s?i(x,y,v,r,t,a):i(y,x,v,t,r,a);if(void 0!==d){if(d)continue;b=!1;break}if(h){if(!o(r,(function(t,r){if(!u(h,r)&&(y===t||c(y,t,n,i,a)))return h.push(r)}))){b=!1;break}}else if(y!==x&&!c(y,x,n,i,a)){b=!1;break}}return a.delete(t),a.delete(r),b}},function(t,r,n){var e=n(4);t.exports=function(t){return t==t&&!e(t)}},function(t,r){t.exports=function(t,r){return function(n){return null!=n&&(n[t]===r&&(void 0!==r||t in Object(n)))}}},function(t,r,n){var e=n(57),o=n(16);t.exports=function(t,r){for(var n=0,u=(r=e(r,t)).length;null!=t&&n<u;)t=t[o(r[n++])];return n&&n==u?t:void 0}},function(t,r,n){var e=n(0),o=n(28),u=n(145),i=n(148);t.exports=function(t,r){return e(t)?t:o(t,r)?[t]:u(i(t))}},function(t,r){t.exports=function(t,r){for(var n=-1,e=null==t?0:t.length,o=Array(e);++n<e;)o[n]=r(t[n],n,t);return o}},function(t,r,n){var e=n(60);t.exports=function(t,r){var n=(new e).parse(t);return r?n?n.getVisibleText():\"\":n}},function(t,r,n){var e=n(61),o=n(159),u=n(160),i=n(49),c=n(161);const a=/(?:^\\s*--|^\\s*__|^-\\w|^-- $)|(?:^Sent from my (?:\\s*\\w+){1,4}$)|(?:^={30,}$)$/,s=/>+$/,f=[/^\\s*(On(?:(?!.*On\\b|\\bwrote:)[\\s\\S])+wrote:)$/m,/^\\s*(Le(?:(?!.*Le\\b|\\bécrit:)[\\s\\S])+écrit :)$/m,/^\\s*(El(?:(?!.*El\\b|\\bescribió:)[\\s\\S])+escribió:)$/m,/^\\s*(Il(?:(?!.*Il\\b|\\bscritto:)[\\s\\S])+scritto:)$/m,/^\\s*(Op\\s[\\S\\s]+?schreef[\\S\\s]+:)$/m,/^\\s*((W\\sdniu|Dnia)\\s[\\S\\s]+?(pisze|napisał(\\(a\\))?):)$/mu,/^\\s*(Den\\s.+\\sskrev\\s.+:)$/m,/^\\s*(Am\\s.+\\sum\\s.+\\sschrieb\\s.+:)$/m,/^(在[\\S\\s]+写道：)$/m,/^(20[0-9]{2}\\..+\\s작성:)$/m,/^(20[0-9]{2}/.+のメッセージ:)$/m,/^(.+\\s<.+>\\sschrieb:)$/m,/^\\s*(From\\s?:.+\\s?(\\[|<).+(\\]|>))/mu,/^\\s*(De\\s?:.+\\s?(\\[|<).+(\\]|>))/mu,/^\\s*(Van\\s?:.+\\s?(\\[|<).+(\\]|>))/mu,/^\\s*(Da\\s?:.+\\s?(\\[|<).+(\\]|>))/mu,/^(20[0-9]{2}-(?:0?[1-9]|1[012])-(?:0?[0-9]|[1-2][0-9]|3[01]|[1-9])\\s[0-2]?[0-9]:\\d{2}\\s[\\S\\s]+?:)$/m,/^\\s*([a-z]{3,4}\\.[\\s\\S]+\\sskrev[\\s\\S]+:)$/m];\n/**\n * Represents a fragment that hasn't been constructed (yet)\n * @license MIT License\n */\nclass p{constructor(){this.lines=[],this.isHidden=!1,this.isSignature=!1,this.isQuoted=!1}toFragment(){var t=c.reverse(this.lines.join(\"\\n\")).replace(/^\\n/,\"\");return new o(t,this.isHidden,this.isSignature,this.isQuoted)}}t.exports=class{constructor(t,r,n){this._signatureRegex=t||a,this._quotedLineRegex=r||s,this._quoteHeadersRegex=n||f}parse(t){if(\"string\"!=typeof t)return new e([]);var r=[];for(var n of(t=t.replace(\"\\r\\n\",\"\\n\"),this._quoteHeadersRegex)){var o=t.match(n);o&&o.length>=2&&(t=t.replace(o[1],o[1].replace(/\\n/g,\" \")))}var i=null;for(var a of c.reverse(t).split(\"\\n\")){if(a=a.replace(/\\n+$/,\"\"),this._isSignature(a)||(a=a.replace(/^\\s+/,\"\")),i){var s=i.lines[i.lines.length-1];this._isSignature(s)?(i.isSignature=!0,this._addFragment(i,r),i=null):0===a.length&&this._isQuoteHeader(s)&&(i.isQuoted=!0,this._addFragment(i,r),i=null)}var f=this._isQuote(a);null!==i&&this._isFragmentLine(i,a,f)||(i&&this._addFragment(i,r),(i=new p).isQuoted=f),i.lines.push(a)}i&&this._addFragment(i,r);var l=[];for(var v of r)l.push(v.toFragment());return new e(u(l))}_addFragment(t,r){(t.isQuoted||t.isSignature||0===t.lines.join(\"\").length)&&(t.isHidden=!0),r.push(t)}_isFragmentLine(t,r,n){return t.isQuoted===n||!!t.isQuoted&&(this._isQuoteHeader(r)||0===r.length)}_isSignature(t){return this._signatureRegex.test(c.reverse(t))}_isQuote(t){return this._quotedLineRegex.test(t)}_isQuoteHeader(t){return i(this._quoteHeadersRegex,r=>r.test(c.reverse(t))).length>0}}},function(t,r,n){var e=n(62),o=n(49),u=n(157);t.exports=class{constructor(t){this._fragments=t}getFragments(){return e(this._fragments)}getVisibleText(){var t=o(this._fragments,t=>!t.isHidden());return u(t,t=>t.getContent()).join(\"\\n\")}}},function(t,r,n){var e=n(63);t.exports=function(t){return e(t,5)}},function(t,r,n){var e=n(17),o=n(92),u=n(33),i=n(94),c=n(101),a=n(104),s=n(105),f=n(106),p=n(107),l=n(46),v=n(108),b=n(15),h=n(113),y=n(114),x=n(119),d=n(0),j=n(21),_=n(121),g=n(4),m=n(123),O=n(7),w={};w[\"[object Arguments]\"]=w[\"[object Array]\"]=w[\"[object ArrayBuffer]\"]=w[\"[object DataView]\"]=w[\"[object Boolean]\"]=w[\"[object Date]\"]=w[\"[object Float32Array]\"]=w[\"[object Float64Array]\"]=w[\"[object Int8Array]\"]=w[\"[object Int16Array]\"]=w[\"[object Int32Array]\"]=w[\"[object Map]\"]=w[\"[object Number]\"]=w[\"[object Object]\"]=w[\"[object RegExp]\"]=w[\"[object Set]\"]=w[\"[object String]\"]=w[\"[object Symbol]\"]=w[\"[object Uint8Array]\"]=w[\"[object Uint8ClampedArray]\"]=w[\"[object Uint16Array]\"]=w[\"[object Uint32Array]\"]=!0,w[\"[object Error]\"]=w[\"[object Function]\"]=w[\"[object WeakMap]\"]=!1,t.exports=function t(r,n,F,A,S,D){var $,P=1&n,z=2&n,E=4&n;if(F&&($=S?F(r,A,S,D):F(r)),void 0!==$)return $;if(!g(r))return r;var k=d(r);if(k){if($=h(r),!P)return s(r,$)}else{var B=b(r),M=\"[object Function]\"==B||\"[object GeneratorFunction]\"==B;if(j(r))return a(r,P);if(\"[object Object]\"==B||\"[object Arguments]\"==B||M&&!S){if($=z||M?{}:x(r),!P)return z?p(r,c($,r)):f(r,i($,r))}else{if(!w[B])return S?r:{};$=y(r,B,P)}}D||(D=new e);var I=D.get(r);if(I)return I;D.set(r,$),m(r)?r.forEach((function(e){$.add(t(e,n,F,e,r,D))})):_(r)&&r.forEach((function(e,o){$.set(o,t(e,n,F,o,r,D))}));var C=E?z?v:l:z?keysIn:O,Q=k?void 0:C(r);return o(Q||r,(function(e,o){Q&&(e=r[o=e]),u($,o,t(e,n,F,o,r,D))})),$}},function(t,r){t.exports=function(){this.__data__=[],this.size=0}},function(t,r,n){var e=n(9),o=Array.prototype.splice;t.exports=function(t){var r=this.__data__,n=e(r,t);return!(n<0)&&(n==r.length-1?r.pop():o.call(r,n,1),--this.size,!0)}},function(t,r,n){var e=n(9);t.exports=function(t){var r=this.__data__,n=e(r,t);return n<0?void 0:r[n][1]}},function(t,r,n){var e=n(9);t.exports=function(t){return e(this.__data__,t)>-1}},function(t,r,n){var e=n(9);t.exports=function(t,r){var n=this.__data__,o=e(n,t);return o<0?(++this.size,n.push([t,r])):n[o][1]=r,this}},function(t,r,n){var e=n(8);t.exports=function(){this.__data__=new e,this.size=0}},function(t,r){t.exports=function(t){var r=this.__data__,n=r.delete(t);return this.size=r.size,n}},function(t,r){t.exports=function(t){return this.__data__.get(t)}},function(t,r){t.exports=function(t){return this.__data__.has(t)}},function(t,r,n){var e=n(8),o=n(19),u=n(20);t.exports=function(t,r){var n=this.__data__;if(n instanceof e){var i=n.__data__;if(!o||i.length<199)return i.push([t,r]),this.size=++n.size,this;n=this.__data__=new u(i)}return n.set(t,r),this.size=n.size,this}},function(t,r,n){var e=n(30),o=n(77),u=n(4),i=n(32),c=/^\\[object .+?Constructor\\]$/,a=Function.prototype,s=Object.prototype,f=a.toString,p=s.hasOwnProperty,l=RegExp(\"^\"+f.call(p).replace(/[\\\\^$.*+?()[\\]{}|]/g,\"\\\\$&\").replace(/hasOwnProperty|(function).*?(?=\\\\\\()| for .+?(?=\\\\\\])/g,\"$1.*?\")+\"$\");t.exports=function(t){return!(!u(t)||o(t))&&(e(t)?l:c).test(i(t))}},function(t,r,n){var e=n(6),o=Object.prototype,u=o.hasOwnProperty,i=o.toString,c=e?e.toStringTag:void 0;t.exports=function(t){var r=u.call(t,c),n=t[c];try{t[c]=void 0;var e=!0}catch(t){}var o=i.call(t);return e&&(r?t[c]=n:delete t[c]),o}},function(t,r){var n=Object.prototype.toString;t.exports=function(t){return n.call(t)}},function(t,r,n){var e,o=n(78),u=(e=/[^.]+$/.exec(o&&o.keys&&o.keys.IE_PROTO||\"\"))?\"Symbol(src)_1.\"+e:\"\";t.exports=function(t){return!!u&&u in t}},function(t,r,n){var e=n(1)[\"__core-js_shared__\"];t.exports=e},function(t,r){t.exports=function(t,r){return null==t?void 0:t[r]}},function(t,r,n){var e=n(81),o=n(8),u=n(19);t.exports=function(){this.size=0,this.__data__={hash:new e,map:new(u||o),string:new e}}},function(t,r,n){var e=n(82),o=n(83),u=n(84),i=n(85),c=n(86);function a(t){var r=-1,n=null==t?0:t.length;for(this.clear();++r<n;){var e=t[r];this.set(e[0],e[1])}}a.prototype.clear=e,a.prototype.delete=o,a.prototype.get=u,a.prototype.has=i,a.prototype.set=c,t.exports=a},function(t,r,n){var e=n(10);t.exports=function(){this.__data__=e?e(null):{},this.size=0}},function(t,r){t.exports=function(t){var r=this.has(t)&&delete this.__data__[t];return this.size-=r?1:0,r}},function(t,r,n){var e=n(10),o=Object.prototype.hasOwnProperty;t.exports=function(t){var r=this.__data__;if(e){var n=r[t];return\"__lodash_hash_undefined__\"===n?void 0:n}return o.call(r,t)?r[t]:void 0}},function(t,r,n){var e=n(10),o=Object.prototype.hasOwnProperty;t.exports=function(t){var r=this.__data__;return e?void 0!==r[t]:o.call(r,t)}},function(t,r,n){var e=n(10);t.exports=function(t,r){var n=this.__data__;return this.size+=this.has(t)?0:1,n[t]=e&&void 0===r?\"__lodash_hash_undefined__\":r,this}},function(t,r,n){var e=n(11);t.exports=function(t){var r=e(this,t).delete(t);return this.size-=r?1:0,r}},function(t,r){t.exports=function(t){var r=typeof t;return\"string\"==r||\"number\"==r||\"symbol\"==r||\"boolean\"==r?\"__proto__\"!==t:null===t}},function(t,r,n){var e=n(11);t.exports=function(t){return e(this,t).get(t)}},function(t,r,n){var e=n(11);t.exports=function(t){return e(this,t).has(t)}},function(t,r,n){var e=n(11);t.exports=function(t,r){var n=e(this,t),o=n.size;return n.set(t,r),this.size+=n.size==o?0:1,this}},function(t,r){t.exports=function(t,r){for(var n=-1,e=null==t?0:t.length;++n<e&&!1!==r(t[n],n,t););return t}},function(t,r,n){var e=n(2),o=function(){try{var t=e(Object,\"defineProperty\");return t({},\"\",{}),t}catch(t){}}();t.exports=o},function(t,r,n){var e=n(12),o=n(7);t.exports=function(t,r){return t&&e(r,o(r),t)}},function(t,r){t.exports=function(t,r){for(var n=-1,e=Array(t);++n<t;)e[n]=r(n);return e}},function(t,r,n){var e=n(5),o=n(3);t.exports=function(t){return o(t)&&\"[object Arguments]\"==e(t)}},function(t,r){t.exports=function(){return!1}},function(t,r,n){var e=n(5),o=n(22),u=n(3),i={};i[\"[object Float32Array]\"]=i[\"[object Float64Array]\"]=i[\"[object Int8Array]\"]=i[\"[object Int16Array]\"]=i[\"[object Int32Array]\"]=i[\"[object Uint8Array]\"]=i[\"[object Uint8ClampedArray]\"]=i[\"[object Uint16Array]\"]=i[\"[object Uint32Array]\"]=!0,i[\"[object Arguments]\"]=i[\"[object Array]\"]=i[\"[object ArrayBuffer]\"]=i[\"[object Boolean]\"]=i[\"[object DataView]\"]=i[\"[object Date]\"]=i[\"[object Error]\"]=i[\"[object Function]\"]=i[\"[object Map]\"]=i[\"[object Number]\"]=i[\"[object Object]\"]=i[\"[object RegExp]\"]=i[\"[object Set]\"]=i[\"[object String]\"]=i[\"[object WeakMap]\"]=!1,t.exports=function(t){return u(t)&&o(t.length)&&!!i[e(t)]}},function(t,r,n){var e=n(25),o=n(100),u=Object.prototype.hasOwnProperty;t.exports=function(t){if(!e(t))return o(t);var r=[];for(var n in Object(t))u.call(t,n)&&\"constructor\"!=n&&r.push(n);return r}},function(t,r,n){var e=n(39)(Object.keys,Object);t.exports=e},function(t,r,n){var e=n(12),o=n(40);t.exports=function(t,r){return t&&e(r,o(r),t)}},function(t,r,n){var e=n(4),o=n(25),u=n(103),i=Object.prototype.hasOwnProperty;t.exports=function(t){if(!e(t))return u(t);var r=o(t),n=[];for(var c in t)(\"constructor\"!=c||!r&&i.call(t,c))&&n.push(c);return n}},function(t,r){t.exports=function(t){var r=[];if(null!=t)for(var n in Object(t))r.push(n);return r}},function(t,r,n){(function(t){var e=n(1),o=r&&!r.nodeType&&r,u=o&&\"object\"==typeof t&&t&&!t.nodeType&&t,i=u&&u.exports===o?e.Buffer:void 0,c=i?i.allocUnsafe:void 0;t.exports=function(t,r){if(r)return t.slice();var n=t.length,e=c?c(n):new t.constructor(n);return t.copy(e),e}}).call(this,n(13)(t))},function(t,r){t.exports=function(t,r){var n=-1,e=t.length;for(r||(r=Array(e));++n<e;)r[n]=t[n];return r}},function(t,r,n){var e=n(12),o=n(26);t.exports=function(t,r){return e(t,o(t),r)}},function(t,r,n){var e=n(12),o=n(43);t.exports=function(t,r){return e(t,o(t),r)}},function(t,r,n){var e=n(47),o=n(43),u=n(40);t.exports=function(t){return e(t,u,o)}},function(t,r,n){var e=n(2)(n(1),\"DataView\");t.exports=e},function(t,r,n){var e=n(2)(n(1),\"Promise\");t.exports=e},function(t,r,n){var e=n(2)(n(1),\"Set\");t.exports=e},function(t,r,n){var e=n(2)(n(1),\"WeakMap\");t.exports=e},function(t,r){var n=Object.prototype.hasOwnProperty;t.exports=function(t){var r=t.length,e=new t.constructor(r);return r&&\"string\"==typeof t[0]&&n.call(t,\"index\")&&(e.index=t.index,e.input=t.input),e}},function(t,r,n){var e=n(27),o=n(115),u=n(116),i=n(117),c=n(118);t.exports=function(t,r,n){var a=t.constructor;switch(r){case\"[object ArrayBuffer]\":return e(t);case\"[object Boolean]\":case\"[object Date]\":return new a(+t);case\"[object DataView]\":return o(t,n);case\"[object Float32Array]\":case\"[object Float64Array]\":case\"[object Int8Array]\":case\"[object Int16Array]\":case\"[object Int32Array]\":case\"[object Uint8Array]\":case\"[object Uint8ClampedArray]\":case\"[object Uint16Array]\":case\"[object Uint32Array]\":return c(t,n);case\"[object Map]\":return new a;case\"[object Number]\":case\"[object String]\":return new a(t);case\"[object RegExp]\":return u(t);case\"[object Set]\":return new a;case\"[object Symbol]\":return i(t)}}},function(t,r,n){var e=n(27);t.exports=function(t,r){var n=r?e(t.buffer):t.buffer;return new t.constructor(n,t.byteOffset,t.byteLength)}},function(t,r){var n=/\\w*$/;t.exports=function(t){var r=new t.constructor(t.source,n.exec(t));return r.lastIndex=t.lastIndex,r}},function(t,r,n){var e=n(6),o=e?e.prototype:void 0,u=o?o.valueOf:void 0;t.exports=function(t){return u?Object(u.call(t)):{}}},function(t,r,n){var e=n(27);t.exports=function(t,r){var n=r?e(t.buffer):t.buffer;return new t.constructor(n,t.byteOffset,t.length)}},function(t,r,n){var e=n(120),o=n(45),u=n(25);t.exports=function(t){return\"function\"!=typeof t.constructor||u(t)?{}:e(o(t))}},function(t,r,n){var e=n(4),o=Object.create,u=function(){function t(){}return function(r){if(!e(r))return{};if(o)return o(r);t.prototype=r;var n=new t;return t.prototype=void 0,n}}();t.exports=u},function(t,r,n){var e=n(122),o=n(23),u=n(24),i=u&&u.isMap,c=i?o(i):e;t.exports=c},function(t,r,n){var e=n(15),o=n(3);t.exports=function(t){return o(t)&&\"[object Map]\"==e(t)}},function(t,r,n){var e=n(124),o=n(23),u=n(24),i=u&&u.isSet,c=i?o(i):e;t.exports=c},function(t,r,n){var e=n(15),o=n(3);t.exports=function(t){return o(t)&&\"[object Set]\"==e(t)}},function(t,r,n){var e=n(50);t.exports=function(t,r){var n=[];return e(t,(function(t,e,o){r(t,e,o)&&n.push(t)})),n}},function(t,r,n){var e=n(127),o=n(7);t.exports=function(t,r){return t&&e(t,r,o)}},function(t,r,n){var e=n(128)();t.exports=e},function(t,r){t.exports=function(t){return function(r,n,e){for(var o=-1,u=Object(r),i=e(r),c=i.length;c--;){var a=i[t?c:++o];if(!1===n(u[a],a,u))break}return r}}},function(t,r,n){var e=n(14);t.exports=function(t,r){return function(n,o){if(null==n)return n;if(!e(n))return t(n,o);for(var u=n.length,i=r?u:-1,c=Object(n);(r?i--:++i<u)&&!1!==o(c[i],i,c););return n}}},function(t,r,n){var e=n(131),o=n(142),u=n(55);t.exports=function(t){var r=o(t);return 1==r.length&&r[0][2]?u(r[0][0],r[0][1]):function(n){return n===t||e(n,t,r)}}},function(t,r,n){var e=n(17),o=n(52);t.exports=function(t,r,n,u){var i=n.length,c=i,a=!u;if(null==t)return!c;for(t=Object(t);i--;){var s=n[i];if(a&&s[2]?s[1]!==t[s[0]]:!(s[0]in t))return!1}for(;++i<c;){var f=(s=n[i])[0],p=t[f],l=s[1];if(a&&s[2]){if(void 0===p&&!(f in t))return!1}else{var v=new e;if(u)var b=u(p,l,f,t,r,v);if(!(void 0===b?o(l,p,3,u,v):b))return!1}}return!0}},function(t,r,n){var e=n(17),o=n(53),u=n(138),i=n(141),c=n(15),a=n(0),s=n(21),f=n(38),p=\"[object Object]\",l=Object.prototype.hasOwnProperty;t.exports=function(t,r,n,v,b,h){var y=a(t),x=a(r),d=y?\"[object Array]\":c(t),j=x?\"[object Array]\":c(r),_=(d=\"[object Arguments]\"==d?p:d)==p,g=(j=\"[object Arguments]\"==j?p:j)==p,m=d==j;if(m&&s(t)){if(!s(r))return!1;y=!0,_=!1}if(m&&!_)return h||(h=new e),y||f(t)?o(t,r,n,v,b,h):u(t,r,d,n,v,b,h);if(!(1&n)){var O=_&&l.call(t,\"__wrapped__\"),w=g&&l.call(r,\"__wrapped__\");if(O||w){var F=O?t.value():t,A=w?r.value():r;return h||(h=new e),b(F,A,n,v,h)}}return!!m&&(h||(h=new e),i(t,r,n,v,b,h))}},function(t,r,n){var e=n(20),o=n(134),u=n(135);function i(t){var r=-1,n=null==t?0:t.length;for(this.__data__=new e;++r<n;)this.add(t[r])}i.prototype.add=i.prototype.push=o,i.prototype.has=u,t.exports=i},function(t,r){t.exports=function(t){return this.__data__.set(t,\"__lodash_hash_undefined__\"),this}},function(t,r){t.exports=function(t){return this.__data__.has(t)}},function(t,r){t.exports=function(t,r){for(var n=-1,e=null==t?0:t.length;++n<e;)if(r(t[n],n,t))return!0;return!1}},function(t,r){t.exports=function(t,r){return t.has(r)}},function(t,r,n){var e=n(6),o=n(48),u=n(18),i=n(53),c=n(139),a=n(140),s=e?e.prototype:void 0,f=s?s.valueOf:void 0;t.exports=function(t,r,n,e,s,p,l){switch(n){case\"[object DataView]\":if(t.byteLength!=r.byteLength||t.byteOffset!=r.byteOffset)return!1;t=t.buffer,r=r.buffer;case\"[object ArrayBuffer]\":return!(t.byteLength!=r.byteLength||!p(new o(t),new o(r)));case\"[object Boolean]\":case\"[object Date]\":case\"[object Number]\":return u(+t,+r);case\"[object Error]\":return t.name==r.name&&t.message==r.message;case\"[object RegExp]\":case\"[object String]\":return t==r+\"\";case\"[object Map]\":var v=c;case\"[object Set]\":var b=1&e;if(v||(v=a),t.size!=r.size&&!b)return!1;var h=l.get(t);if(h)return h==r;e|=2,l.set(t,r);var y=i(v(t),v(r),e,s,p,l);return l.delete(t),y;case\"[object Symbol]\":if(f)return f.call(t)==f.call(r)}return!1}},function(t,r){t.exports=function(t){var r=-1,n=Array(t.size);return t.forEach((function(t,e){n[++r]=[e,t]})),n}},function(t,r){t.exports=function(t){var r=-1,n=Array(t.size);return t.forEach((function(t){n[++r]=t})),n}},function(t,r,n){var e=n(46),o=Object.prototype.hasOwnProperty;t.exports=function(t,r,n,u,i,c){var a=1&n,s=e(t),f=s.length;if(f!=e(r).length&&!a)return!1;for(var p=f;p--;){var l=s[p];if(!(a?l in r:o.call(r,l)))return!1}var v=c.get(t);if(v&&c.get(r))return v==r;var b=!0;c.set(t,r),c.set(r,t);for(var h=a;++p<f;){var y=t[l=s[p]],x=r[l];if(u)var d=a?u(x,y,l,r,t,c):u(y,x,l,t,r,c);if(!(void 0===d?y===x||i(y,x,n,u,c):d)){b=!1;break}h||(h=\"constructor\"==l)}if(b&&!h){var j=t.constructor,_=r.constructor;j==_||!(\"constructor\"in t)||!(\"constructor\"in r)||\"function\"==typeof j&&j instanceof j&&\"function\"==typeof _&&_ instanceof _||(b=!1)}return c.delete(t),c.delete(r),b}},function(t,r,n){var e=n(54),o=n(7);t.exports=function(t){for(var r=o(t),n=r.length;n--;){var u=r[n],i=t[u];r[n]=[u,i,e(i)]}return r}},function(t,r,n){var e=n(52),o=n(144),u=n(150),i=n(28),c=n(54),a=n(55),s=n(16);t.exports=function(t,r){return i(t)&&c(r)?a(s(t),r):function(n){var i=o(n,t);return void 0===i&&i===r?u(n,t):e(r,i,3)}}},function(t,r,n){var e=n(56);t.exports=function(t,r,n){var o=null==t?void 0:e(t,r);return void 0===o?n:o}},function(t,r,n){var e=n(146),o=/[^.[\\]]+|\\[(?:(-?\\d+(?:\\.\\d+)?)|([\"'])((?:(?!\\2)[^\\\\]|\\\\.)*?)\\2)\\]|(?=(?:\\.|\\[\\])(?:\\.|\\[\\]|$))/g,u=/\\\\(\\\\)?/g,i=e((function(t){var r=[];return 46===t.charCodeAt(0)&&r.push(\"\"),t.replace(o,(function(t,n,e,o){r.push(e?o.replace(u,\"$1\"):n||t)})),r}));t.exports=i},function(t,r,n){var e=n(147);t.exports=function(t){var r=e(t,(function(t){return 500===n.size&&n.clear(),t})),n=r.cache;return r}},function(t,r,n){var e=n(20);function o(t,r){if(\"function\"!=typeof t||null!=r&&\"function\"!=typeof r)throw new TypeError(\"Expected a function\");var n=function(){var e=arguments,o=r?r.apply(this,e):e[0],u=n.cache;if(u.has(o))return u.get(o);var i=t.apply(this,e);return n.cache=u.set(o,i)||u,i};return n.cache=new(o.Cache||e),n}o.Cache=e,t.exports=o},function(t,r,n){var e=n(149);t.exports=function(t){return null==t?\"\":e(t)}},function(t,r,n){var e=n(6),o=n(58),u=n(0),i=n(29),c=e?e.prototype:void 0,a=c?c.toString:void 0;t.exports=function t(r){if(\"string\"==typeof r)return r;if(u(r))return o(r,t)+\"\";if(i(r))return a?a.call(r):\"\";var n=r+\"\";return\"0\"==n&&1/r==-1/0?\"-0\":n}},function(t,r,n){var e=n(151),o=n(152);t.exports=function(t,r){return null!=t&&o(t,r,e)}},function(t,r){t.exports=function(t,r){return null!=t&&r in Object(t)}},function(t,r,n){var e=n(57),o=n(36),u=n(0),i=n(37),c=n(22),a=n(16);t.exports=function(t,r,n){for(var s=-1,f=(r=e(r,t)).length,p=!1;++s<f;){var l=a(r[s]);if(!(p=null!=t&&n(t,l)))break;t=t[l]}return p||++s!=f?p:!!(f=null==t?0:t.length)&&c(f)&&i(l,f)&&(u(t)||o(t))}},function(t,r){t.exports=function(t){return t}},function(t,r,n){var e=n(155),o=n(156),u=n(28),i=n(16);t.exports=function(t){return u(t)?e(i(t)):o(t)}},function(t,r){t.exports=function(t){return function(r){return null==r?void 0:r[t]}}},function(t,r,n){var e=n(56);t.exports=function(t){return function(r){return e(r,t)}}},function(t,r,n){var e=n(58),o=n(51),u=n(158),i=n(0);t.exports=function(t,r){return(i(t)?e:u)(t,o(r,3))}},function(t,r,n){var e=n(50),o=n(14);t.exports=function(t,r){var n=-1,u=o(t)?Array(t.length):[];return e(t,(function(t,e,o){u[++n]=r(t,e,o)})),u}},function(t,r){t.exports=class{constructor(t,r,n,e){this._content=t,this._isHidden=r,this._isSignature=n,this._isQuoted=e}getContent(){return this._content}isHidden(){return this._isHidden}isSignature(){return this._isSignature}isQuoted(){return this._isQuoted}isEmpty(){return 0===this.getContent().replace(\"\\n\",\"\").length}}},function(t,r){var n=Array.prototype.reverse;t.exports=function(t){return null==t?t:n.call(t)}},function(t,r,n){(function(t){var e;/*! https://mths.be/esrever v0.2.0 by @mathias */!function(o){var u=r,i=(t&&t.exports,\"object\"==typeof global&&global);i.global!==i&&i.window;var c=/([\\0-\\˿\\Ͱ-\\᪯\\ᬀ-\\ᶿ\\Ḁ-\\⃏\\℀-\\퟿\\-\\︟\\︰-\\￿]|[\\�-\\�][\\�-\\�]|[\\�-\\�](?![\\�-\\�])|(?:[^\\�-\\�]|^)[\\�-\\�])([\\̀-\\ͯ\\᪰-\\᫿\\᷀-\\᷿\\⃐-\\⃿\\︠-\\︯]+)/g,a=/([\\�-\\�])([\\�-\\�])/g,s=function(t){for(var r=\"\",n=(t=t.replace(c,(function(t,r,n){return s(n)+r})).replace(a,\"$2$1\")).length;n--;)r+=t.charAt(n);return r},f={version:\"0.2.0\",reverse:s};void 0===(e=function(){return f}.call(r,n,r,t))||(t.exports=e)}()}).call(this,n(13)(t))}]);\n\nfunction extractReplyContent(message) {\n  const email = EmailParser(message);\n  const reply = (email.getFragments()[0].getContent().trim());\n  return reply;\n}\n\nfor (const item of $input.all()) {\n  item.json.reply = extractReplyContent(item.json.text);\n}\n\nreturn $input.all();"
      },
      "typeVersion": 1
    },
    {
      "id": "4f6998f6-88a8-4b8b-acea-33c3f33d04dd",
      "name": "If spreadsheet doesn't exist",
      "type": "n8n-nodes-base.if",
      "position": [
        1420,
        2500
      ],
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{ $json[\"error\"] }}",
              "value2": "The resource you are requesting could not be found"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "id": "f3564023-a1c5-42f5-923d-a8e98c95c284",
      "name": "Successfully created or updated row",
      "type": "n8n-nodes-base.noOp",
      "position": [
        1660,
        2640
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "55869b16-3a98-4127-83ec-bcfdf21c2daf",
      "name": "Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        980,
        2140
      ],
      "parameters": {
        "width": 778.177339901478,
        "height": 289.16256157635416,
        "content": "### Create spreadsheet and populate with headers and deal information\nA spreadsheet is created if the spreadsheet does not exist. The spreadsheet ID is stored in the `$getWorkflowStaticData('global')` variable. Using `Extract current deal` node, the deal information is formatted for the sending to the new spreadsheet."
      },
      "typeVersion": 1
    },
    {
      "id": "8994f1e7-dd0d-4247-89fd-befcc9c511b0",
      "name": "Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1220,
        2680
      ],
      "parameters": {
        "width": 301.18226600985224,
        "height": 114.67980295566498,
        "content": "### Tip: Deleting old spreadsheets\nIf you ever want to start over, delete the old spreadsheet, __making sure that it is also deleted from Google Drive's trash__."
      },
      "typeVersion": 1
    },
    {
      "id": "cd8c9657-3380-4e25-907e-baa1c02c0793",
      "name": "Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        400,
        2140
      ],
      "parameters": {
        "width": 260.3940886699507,
        "height": 333.34975369458095,
        "content": "### `Get spreadsheet ID`\n\n\n\n\n\n\n\n\n\n\n\n\n\nThe spreadsheet ID is stored in this workflow's static data. If you want to refresh the static data you will need to copy this entire workflow into a new workflow."
      },
      "typeVersion": 1
    },
    {
      "id": "ab0348c2-f688-42d3-815b-63290e95baad",
      "name": "Create spreadsheet",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        1020,
        2260
      ],
      "parameters": {
        "title": "={{ $(\"Configure\").first().json[\"spreadsheetName\"] }}",
        "options": {},
        "resource": "spreadsheet",
        "sheetsUi": {
          "sheetValues": [
            {
              "title": "={{ $(\"Configure\").first().json[\"worksheetName\"] }}"
            }
          ]
        }
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "7",
          "name": "[UPDATE ME]"
        }
      },
      "typeVersion": 3
    },
    {
      "id": "c56522b2-5eca-497d-afbb-d713abd8d810",
      "name": "Store spreadsheet ID",
      "type": "n8n-nodes-base.code",
      "position": [
        1220,
        2260
      ],
      "parameters": {
        "jsCode": "const staticData = $getWorkflowStaticData('global');\n\nstaticData.googleSheetsSpreadsheetId = $('Create spreadsheet').first().json.spreadsheetId\nstaticData.googleSheetsWorksheetId = $('Create spreadsheet').first().json.sheets[0].properties.sheetId\n\nreturn {\n  \"spreadsheetId\": staticData.googleSheetsSpreadsheetId,\n  \"worksheetId\": staticData.googleSheetsWorksheetId\n}"
      },
      "typeVersion": 1
    },
    {
      "id": "ba62fd4d-912b-4b37-9fda-2f80cdeb65f8",
      "name": "Paste data",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        1620,
        2260
      ],
      "parameters": {
        "options": {
          "cellFormat": "RAW"
        },
        "dataMode": "autoMapInputData",
        "operation": "append",
        "sheetName": {
          "__rl": true,
          "mode": "id",
          "value": "={{ $node[\"Store spreadsheet ID\"].json[\"worksheetId\"] }}"
        },
        "documentId": {
          "__rl": true,
          "mode": "id",
          "value": "={{ $node[\"Store spreadsheet ID\"].json[\"spreadsheetId\"] }}"
        }
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "7",
          "name": "[UPDATE ME]"
        }
      },
      "typeVersion": 3
    },
    {
      "id": "a8be831a-f2be-48c9-a661-bc8c5cde6444",
      "name": "If no sheet IDs",
      "type": "n8n-nodes-base.if",
      "position": [
        800,
        2380
      ],
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{ $json[\"spreadsheetId\"] }}",
              "operation": "isEmpty"
            },
            {
              "value1": "={{ $json[\"worksheetId\"] }}",
              "operation": "isEmpty"
            }
          ]
        },
        "combineOperation": "any"
      },
      "typeVersion": 1
    },
    {
      "id": "efdb343d-f5bf-4ba4-bc27-850b9e7935ac",
      "name": "Create or update rows",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        1220,
        2500
      ],
      "parameters": {
        "options": {
          "cellFormat": "RAW"
        },
        "dataMode": "autoMapInputData",
        "operation": "appendOrUpdate",
        "sheetName": {
          "__rl": true,
          "mode": "id",
          "value": "={{ $node[\"If no sheet IDs\"].json[\"worksheetId\"] }}"
        },
        "documentId": {
          "__rl": true,
          "mode": "id",
          "value": "={{ $node[\"If no sheet IDs\"].json[\"spreadsheetId\"] }}"
        },
        "columnToMatchOn": "ID"
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "7",
          "name": "[UPDATE ME]"
        }
      },
      "typeVersion": 3,
      "continueOnFail": true
    },
    {
      "id": "091ad4fa-21aa-42e0-abc5-17221cdf8fb7",
      "name": "Get data from `Format data`",
      "type": "n8n-nodes-base.code",
      "position": [
        1020,
        2500
      ],
      "parameters": {
        "jsCode": "return $('Format data').all()"
      },
      "typeVersion": 1
    },
    {
      "id": "97071540-59b2-48dd-8f88-ab44446832fc",
      "name": "Get data from `Format data` node",
      "type": "n8n-nodes-base.code",
      "position": [
        1420,
        2260
      ],
      "parameters": {
        "jsCode": "return $('Format data').all()"
      },
      "typeVersion": 1
    },
    {
      "id": "ecf03802-51c8-43b1-84d8-5ed5826fd444",
      "name": "Format data",
      "type": "n8n-nodes-base.set",
      "position": [
        -40,
        2380
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "ID",
              "value": "={{ $node[\"Generate UUID\"].json.uuid }}"
            },
            {
              "name": "Initial message",
              "value": "={{ $node[\"Extract message content (advanced)\"].json.reply }}"
            },
            {
              "name": "Generated reply",
              "value": "={{ $node[\"Generate reply\"].json.text }}"
            },
            {
              "name": "Good response?"
            }
          ]
        },
        "options": {},
        "keepOnlySet": true
      },
      "typeVersion": 1
    },
    {
      "id": "9eedd7b7-ec4e-4dbf-a257-33e73bdff9c1",
      "name": "Send email reply",
      "type": "n8n-nodes-base.noOp",
      "position": [
        -40,
        1860
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "8e2f4a3b-d224-4248-9682-184a646e022f",
      "name": "On feedback given",
      "type": "n8n-nodes-base.webhook",
      "position": [
        -2460,
        2940
      ],
      "webhookId": "e2aa55fb-618a-4478-805d-d6da46b908d1",
      "parameters": {
        "path": "e2aa55fb-618a-4478-805d-d6da46b908d1",
        "options": {},
        "responseMode": "responseNode"
      },
      "typeVersion": 1
    },
    {
      "id": "87506e44-21aa-4f08-82f9-f47a24ddb9ce",
      "name": "Send feedback for fine-tuned data",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        -100,
        2980
      ],
      "parameters": {
        "options": {},
        "fieldsUi": {
          "values": [
            {
              "column": "Good response?",
              "fieldValue": "={{ $node[\"On feedback given\"].json.query.feedback }}"
            }
          ]
        },
        "operation": "update",
        "sheetName": {
          "__rl": true,
          "mode": "id",
          "value": "={{ $json[\"worksheetId\"] }}"
        },
        "documentId": {
          "__rl": true,
          "mode": "id",
          "value": "={{ $json[\"spreadsheetId\"] }}"
        },
        "valueToMatchOn": "={{ $node[\"On feedback given\"].json.query.id }}",
        "columnToMatchOn": "ID"
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "7",
          "name": "[UPDATE ME]"
        }
      },
      "typeVersion": 3
    },
    {
      "id": "d2a720d4-8487-4dfa-bdb8-6b59368e44bc",
      "name": "Show HTML page",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        -920,
        2980
      ],
      "parameters": {
        "options": {
          "responseCode": 200
        },
        "respondWith": "text",
        "responseBody": "={{ $json.html }}"
      },
      "typeVersion": 1
    },
    {
      "id": "2da7a7b1-e96d-4759-b3cb-13558e2ad1d4",
      "name": "Get sheet IDs #1",
      "type": "n8n-nodes-base.code",
      "position": [
        480,
        2200
      ],
      "parameters": {
        "jsCode": "const staticData = $getWorkflowStaticData('global');\n\nreturn {\n  \"spreadsheetId\": staticData.googleSheetsSpreadsheetId,\n  \"worksheetId\": staticData.googleSheetsWorksheetId\n}"
      },
      "typeVersion": 1
    },
    {
      "id": "08ddeed5-fefe-4acd-918a-00d1fd5a5392",
      "name": "Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -480,
        2780
      ],
      "parameters": {
        "width": 260.3940886699507,
        "height": 333.34975369458095,
        "content": "### `Get spreadsheet ID`\n\n\n\n\n\n\n\n\n\n\n\n\n\nThe spreadsheet ID is stored in this workflow's static data. If you want to refresh the static data you will need to copy this entire workflow into a new workflow."
      },
      "typeVersion": 1
    },
    {
      "id": "49d77f89-3c1e-4e86-93e8-ae7a566802b7",
      "name": "If no spreadsheet in configuration #2",
      "type": "n8n-nodes-base.if",
      "position": [
        -700,
        2980
      ],
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{ $('Configure').first().json.spreadsheetId }}",
              "operation": "isEmpty"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "id": "e3b8f696-41eb-46e1-a4b1-6ba2d219aa45",
      "name": "Store specific sheet IDs #2",
      "type": "n8n-nodes-base.code",
      "position": [
        -400,
        3180
      ],
      "parameters": {
        "jsCode": "const staticData = $getWorkflowStaticData('global');\n\nstaticData.googleSheetsSpreadsheetId = $('Configure').all()[0].json.spreadsheetId\nstaticData.googleSheetsWorksheetId = $('Configure').all()[0].json.worksheetId\n\nreturn {\n  \"spreadsheetId\": staticData.googleSheetsSpreadsheetId,\n  \"worksheetId\": staticData.googleSheetsWorksheetId\n}"
      },
      "typeVersion": 1
    },
    {
      "id": "44d37f76-af16-4507-b1a1-76fadf530806",
      "name": "Get sheet IDs #2",
      "type": "n8n-nodes-base.code",
      "position": [
        -400,
        2840
      ],
      "parameters": {
        "jsCode": "const staticData = $getWorkflowStaticData('global');\n\nreturn {\n  \"spreadsheetId\": staticData.googleSheetsSpreadsheetId,\n  \"worksheetId\": staticData.googleSheetsWorksheetId\n}"
      },
      "typeVersion": 1
    },
    {
      "id": "fae8cbc5-7462-4eb0-9f60-85e8e7cfd10e",
      "name": "If no spreadsheet in configuration #1",
      "type": "n8n-nodes-base.if",
      "position": [
        180,
        2380
      ],
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{ $('Configure').first().json.spreadsheetId }}",
              "operation": "isEmpty"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "id": "67312347-74c0-4ce4-a78c-615da6937bcf",
      "name": "Store specific sheet IDs #1",
      "type": "n8n-nodes-base.code",
      "position": [
        480,
        2540
      ],
      "parameters": {
        "jsCode": "const staticData = $getWorkflowStaticData('global');\n\nstaticData.googleSheetsSpreadsheetId = $('Configure').all()[0].json.spreadsheetId\nstaticData.googleSheetsWorksheetId = $('Configure').all()[0].json.worksheetId\n\nreturn {\n  \"spreadsheetId\": staticData.googleSheetsSpreadsheetId,\n  \"worksheetId\": staticData.googleSheetsWorksheetId\n}"
      },
      "typeVersion": 1
    },
    {
      "id": "400eae76-7b17-48de-a49f-8b0cbc9db1f8",
      "name": "Email template",
      "type": "n8n-nodes-base.html",
      "position": [
        160,
        1860
      ],
      "parameters": {
        "html": "<html>\n  <head>\n    <meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" />\n    <title>Template for ChatGPT email</title>\n    <style>\n      /* cspell:disable-file */\n      /* webkit printing magic: print all background colors */\n      html {\n        -webkit-print-color-adjust: exact;\n      }\n      * {\n        box-sizing: border-box;\n        -webkit-print-color-adjust: exact;\n      }\n\n      html,\n      body {\n        margin: 0;\n        padding: 0;\n      }\n      @media only screen {\n        body {\n          margin: 2em auto;\n          max-width: 900px;\n          color: rgb(55, 53, 47);\n        }\n      }\n\n      body {\n        line-height: 1.5;\n        white-space: pre-wrap;\n      }\n\n      a,\n      a.visited {\n        color: inherit;\n        text-decoration: underline;\n      }\n\n      .pdf-relative-link-path {\n        font-size: 80%;\n        color: #444;\n      }\n\n      h1,\n      h2,\n      h3 {\n        letter-spacing: -0.01em;\n        line-height: 1.2;\n        font-weight: 600;\n        margin-bottom: 0;\n      }\n\n      .page-title {\n        font-size: 2.5rem;\n        font-weight: 700;\n        margin-top: 0;\n        margin-bottom: 0.75em;\n      }\n\n      h1 {\n        font-size: 1.875rem;\n        margin-top: 1.875rem;\n      }\n\n      h2 {\n        font-size: 1.5rem;\n        margin-top: 1.5rem;\n      }\n\n      h3 {\n        font-size: 1.25rem;\n        margin-top: 1.25rem;\n      }\n\n      .source {\n        border: 1px solid #ddd;\n        border-radius: 3px;\n        padding: 1.5em;\n        word-break: break-all;\n      }\n\n      .callout {\n        border-radius: 3px;\n        padding: 1rem;\n      }\n\n      figure {\n        margin: 1.25em 0;\n        page-break-inside: avoid;\n      }\n\n      figcaption {\n        opacity: 0.5;\n        font-size: 85%;\n        margin-top: 0.5em;\n      }\n\n      mark {\n        background-color: transparent;\n      }\n\n      .indented {\n        padding-left: 1.5em;\n      }\n\n      hr {\n        background: transparent;\n        display: block;\n        width: 100%;\n        height: 1px;\n        visibility: visible;\n        border: none;\n        border-bottom: 1px solid rgba(55, 53, 47, 0.09);\n      }\n\n      img {\n        max-width: 100%;\n      }\n\n      @media only print {\n        img {\n          max-height: 100vh;\n          object-fit: contain;\n        }\n      }\n\n      @page {\n        margin: 1in;\n      }\n\n      .collection-content {\n        font-size: 0.875rem;\n      }\n\n      .column-list {\n        display: flex;\n        justify-content: space-between;\n      }\n\n      .column {\n        padding: 0 1em;\n      }\n\n      .column:first-child {\n        padding-left: 0;\n      }\n\n      .column:last-child {\n        padding-right: 0;\n      }\n\n      .table_of_contents-item {\n        display: block;\n        font-size: 0.875rem;\n        line-height: 1.3;\n        padding: 0.125rem;\n      }\n\n      .table_of_contents-indent-1 {\n        margin-left: 1.5rem;\n      }\n\n      .table_of_contents-indent-2 {\n        margin-left: 3rem;\n      }\n\n      .table_of_contents-indent-3 {\n        margin-left: 4.5rem;\n      }\n\n      .table_of_contents-link {\n        text-decoration: none;\n        opacity: 0.7;\n        border-bottom: 1px solid rgba(55, 53, 47, 0.18);\n      }\n\n      table,\n      th,\n      td {\n        border: 1px solid rgba(55, 53, 47, 0.09);\n        border-collapse: collapse;\n      }\n\n      table {\n        border-left: none;\n        border-right: none;\n      }\n\n      th,\n      td {\n        font-weight: normal;\n        padding: 0.25em 0.5em;\n        line-height: 1.5;\n        min-height: 1.5em;\n        text-align: left;\n      }\n\n      th {\n        color: rgba(55, 53, 47, 0.6);\n      }\n\n      ol,\n      ul {\n        margin: 0;\n        margin-block-start: 0.6em;\n        margin-block-end: 0.6em;\n      }\n\n      li > ol:first-child,\n      li > ul:first-child {\n        margin-block-start: 0.6em;\n      }\n\n      ul > li {\n        list-style: disc;\n      }\n\n      ul.to-do-list {\n        text-indent: -1.7em;\n      }\n\n      ul.to-do-list > li {\n        list-style: none;\n      }\n\n      .to-do-children-checked {\n        text-decoration: line-through;\n        opacity: 0.375;\n      }\n\n      ul.toggle > li {\n        list-style: none;\n      }\n\n      ul {\n        padding-inline-start: 1.7em;\n      }\n\n      ul > li {\n        padding-left: 0.1em;\n      }\n\n      ol {\n        padding-inline-start: 1.6em;\n      }\n\n      ol > li {\n        padding-left: 0.2em;\n      }\n\n      .mono ol {\n        padding-inline-start: 2em;\n      }\n\n      .mono ol > li {\n        text-indent: -0.4em;\n      }\n\n      .toggle {\n        padding-inline-start: 0em;\n        list-style-type: none;\n      }\n\n      /* Indent toggle children */\n      .toggle > li > details {\n        padding-left: 1.7em;\n      }\n\n      .toggle > li > details > summary {\n        margin-left: -1.1em;\n      }\n\n      .selected-value {\n        display: inline-block;\n        padding: 0 0.5em;\n        background: rgba(206, 205, 202, 0.5);\n        border-radius: 3px;\n        margin-right: 0.5em;\n        margin-top: 0.3em;\n        margin-bottom: 0.3em;\n        white-space: nowrap;\n      }\n\n      .collection-title {\n        display: inline-block;\n        margin-right: 1em;\n      }\n\n      .simple-table {\n        margin-top: 1em;\n        font-size: 0.875rem;\n        empty-cells: show;\n      }\n      .simple-table td {\n        height: 29px;\n        min-width: 120px;\n      }\n\n      .simple-table th {\n        height: 29px;\n        min-width: 120px;\n      }\n\n      .simple-table-header-color {\n        background: rgb(247, 246, 243);\n        color: black;\n      }\n      .simple-table-header {\n        font-weight: 500;\n      }\n\n      time {\n        opacity: 0.5;\n      }\n\n      .icon {\n        display: inline-block;\n        max-width: 1.2em;\n        max-height: 1.2em;\n        text-decoration: none;\n        vertical-align: text-bottom;\n        margin-right: 0.5em;\n      }\n\n      img.icon {\n        border-radius: 3px;\n      }\n\n      .user-icon {\n        width: 1.5em;\n        height: 1.5em;\n        border-radius: 100%;\n        margin-right: 0.5rem;\n      }\n\n      .user-icon-inner {\n        font-size: 0.8em;\n      }\n\n      .text-icon {\n        border: 1px solid #000;\n        text-align: center;\n      }\n\n      .page-cover-image {\n        display: block;\n        object-fit: cover;\n        width: 100%;\n        max-height: 30vh;\n      }\n\n      .page-header-icon {\n        font-size: 3rem;\n        margin-bottom: 1rem;\n      }\n\n      .page-header-icon-with-cover {\n        margin-top: -0.72em;\n        margin-left: 0.07em;\n      }\n\n      .page-header-icon img {\n        border-radius: 3px;\n      }\n\n      .link-to-page {\n        margin: 1em 0;\n        padding: 0;\n        border: none;\n        font-weight: 500;\n      }\n\n      p > .user {\n        opacity: 0.5;\n      }\n\n      td > .user,\n      td > time {\n        white-space: nowrap;\n      }\n\n      input[type=\"checkbox\"] {\n        transform: scale(1.5);\n        margin-right: 0.6em;\n        vertical-align: middle;\n      }\n\n      p {\n        margin-top: 0.5em;\n        margin-bottom: 0.5em;\n      }\n\n      .image {\n        border: none;\n        margin: 1.5em 0;\n        padding: 0;\n        border-radius: 0;\n        text-align: center;\n      }\n\n      .code,\n      code {\n        background: rgba(135, 131, 120, 0.15);\n        border-radius: 3px;\n        padding: 0.2em 0.4em;\n        border-radius: 3px;\n        font-size: 85%;\n        tab-size: 2;\n      }\n\n      code {\n        color: #eb5757;\n      }\n\n      .code {\n        padding: 1.5em 1em;\n      }\n\n      .code-wrap {\n        white-space: pre-wrap;\n        word-break: break-all;\n      }\n\n      .code > code {\n        background: none;\n        padding: 0;\n        font-size: 100%;\n        color: inherit;\n      }\n\n      blockquote {\n        font-size: 1.25em;\n        margin: 1em 0;\n        padding-left: 1em;\n        border-left: 3px solid rgb(55, 53, 47);\n      }\n\n      .bookmark {\n        text-decoration: none;\n        max-height: 8em;\n        padding: 0;\n        display: flex;\n        width: 100%;\n        align-items: stretch;\n      }\n\n      .bookmark-title {\n        font-size: 0.85em;\n        overflow: hidden;\n        text-overflow: ellipsis;\n        height: 1.75em;\n        white-space: nowrap;\n      }\n\n      .bookmark-text {\n        display: flex;\n        flex-direction: column;\n      }\n\n      .bookmark-info {\n        flex: 4 1 180px;\n        padding: 12px 14px 14px;\n        display: flex;\n        flex-direction: column;\n        justify-content: space-between;\n      }\n\n      .bookmark-image {\n        width: 33%;\n        flex: 1 1 180px;\n        display: block;\n        position: relative;\n        object-fit: cover;\n        border-radius: 1px;\n      }\n\n      .bookmark-description {\n        color: rgba(55, 53, 47, 0.6);\n        font-size: 0.75em;\n        overflow: hidden;\n        max-height: 4.5em;\n        word-break: break-word;\n      }\n\n      .bookmark-href {\n        font-size: 0.75em;\n        margin-top: 0.25em;\n      }\n\n      .sans {\n        font-family: ui-sans-serif, -apple-system, BlinkMacSystemFont,\n          \"Segoe UI\", Helvetica, \"Apple Color Emoji\", Arial, sans-serif,\n          \"Segoe UI Emoji\", \"Segoe UI Symbol\";\n      }\n      .code {\n        font-family: \"SFMono-Regular\", Menlo, Consolas, \"PT Mono\",\n          \"Liberation Mono\", Courier, monospace;\n      }\n      .serif {\n        font-family: Lyon-Text, Georgia, ui-serif, serif;\n      }\n      .mono {\n        font-family: iawriter-mono, Nitti, Menlo, Courier, monospace;\n      }\n      .pdf .sans {\n        font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont,\n          \"Segoe UI\", Helvetica, \"Apple Color Emoji\", Arial, sans-serif,\n          \"Segoe UI Emoji\", \"Segoe UI Symbol\", \"Twemoji\", \"Noto Color Emoji\",\n          \"Noto Sans CJK JP\";\n      }\n      .pdf:lang(zh-CN) .sans {\n        font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont,\n          \"Segoe UI\", Helvetica, \"Apple Color Emoji\", Arial, sans-serif,\n          \"Segoe UI Emoji\", \"Segoe UI Symbol\", \"Twemoji\", \"Noto Color Emoji\",\n          \"Noto Sans CJK SC\";\n      }\n      .pdf:lang(zh-TW) .sans {\n        font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont,\n          \"Segoe UI\", Helvetica, \"Apple Color Emoji\", Arial, sans-serif,\n          \"Segoe UI Emoji\", \"Segoe UI Symbol\", \"Twemoji\", \"Noto Color Emoji\",\n          \"Noto Sans CJK TC\";\n      }\n      .pdf:lang(ko-KR) .sans {\n        font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont,\n          \"Segoe UI\", Helvetica, \"Apple Color Emoji\", Arial, sans-serif,\n          \"Segoe UI Emoji\", \"Segoe UI Symbol\", \"Twemoji\", \"Noto Color Emoji\",\n          \"Noto Sans CJK KR\";\n      }\n      .pdf .code {\n        font-family: Source Code Pro, \"SFMono-Regular\", Menlo, Consolas,\n          \"PT Mono\", \"Liberation Mono\", Courier, monospace, \"Twemoji\",\n          \"Noto Color Emoji\", \"Noto Sans Mono CJK JP\";\n      }\n      .pdf:lang(zh-CN) .code {\n        font-family: Source Code Pro, \"SFMono-Regular\", Menlo, Consolas,\n          \"PT Mono\", \"Liberation Mono\", Courier, monospace, \"Twemoji\",\n          \"Noto Color Emoji\", \"Noto Sans Mono CJK SC\";\n      }\n      .pdf:lang(zh-TW) .code {\n        font-family: Source Code Pro, \"SFMono-Regular\", Menlo, Consolas,\n          \"PT Mono\", \"Liberation Mono\", Courier, monospace, \"Twemoji\",\n          \"Noto Color Emoji\", \"Noto Sans Mono CJK TC\";\n      }\n      .pdf:lang(ko-KR) .code {\n        font-family: Source Code Pro, \"SFMono-Regular\", Menlo, Consolas,\n          \"PT Mono\", \"Liberation Mono\", Courier, monospace, \"Twemoji\",\n          \"Noto Color Emoji\", \"Noto Sans Mono CJK KR\";\n      }\n      .pdf .serif {\n        font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, \"Twemoji\",\n          \"Noto Color Emoji\", \"Noto Serif CJK JP\";\n      }\n      .pdf:lang(zh-CN) .serif {\n        font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, \"Twemoji\",\n          \"Noto Color Emoji\", \"Noto Serif CJK SC\";\n      }\n      .pdf:lang(zh-TW) .serif {\n        font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, \"Twemoji\",\n          \"Noto Color Emoji\", \"Noto Serif CJK TC\";\n      }\n      .pdf:lang(ko-KR) .serif {\n        font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, \"Twemoji\",\n          \"Noto Color Emoji\", \"Noto Serif CJK KR\";\n      }\n      .pdf .mono {\n        font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace,\n          \"Twemoji\", \"Noto Color Emoji\", \"Noto Sans Mono CJK JP\";\n      }\n      .pdf:lang(zh-CN) .mono {\n        font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace,\n          \"Twemoji\", \"Noto Color Emoji\", \"Noto Sans Mono CJK SC\";\n      }\n      .pdf:lang(zh-TW) .mono {\n        font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace,\n          \"Twemoji\", \"Noto Color Emoji\", \"Noto Sans Mono CJK TC\";\n      }\n      .pdf:lang(ko-KR) .mono {\n        font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace,\n          \"Twemoji\", \"Noto Color Emoji\", \"Noto Sans Mono CJK KR\";\n      }\n      .highlight-default {\n        color: rgba(55, 53, 47, 1);\n      }\n      .highlight-gray {\n        color: rgba(120, 119, 116, 1);\n        fill: rgba(120, 119, 116, 1);\n      }\n      .highlight-brown {\n        color: rgba(159, 107, 83, 1);\n        fill: rgba(159, 107, 83, 1);\n      }\n      .highlight-orange {\n        color: rgba(217, 115, 13, 1);\n        fill: rgba(217, 115, 13, 1);\n      }\n      .highlight-yellow {\n        color: rgba(203, 145, 47, 1);\n        fill: rgba(203, 145, 47, 1);\n      }\n      .highlight-teal {\n        color: rgba(68, 131, 97, 1);\n        fill: rgba(68, 131, 97, 1);\n      }\n      .highlight-blue {\n        color: rgba(51, 126, 169, 1);\n        fill: rgba(51, 126, 169, 1);\n      }\n      .highlight-purple {\n        color: rgba(144, 101, 176, 1);\n        fill: rgba(144, 101, 176, 1);\n      }\n      .highlight-pink {\n        color: rgba(193, 76, 138, 1);\n        fill: rgba(193, 76, 138, 1);\n      }\n      .highlight-red {\n        color: rgba(212, 76, 71, 1);\n        fill: rgba(212, 76, 71, 1);\n      }\n      .highlight-gray_background {\n        background: rgba(241, 241, 239, 1);\n      }\n      .highlight-brown_background {\n        background: rgba(244, 238, 238, 1);\n      }\n      .highlight-orange_background {\n        background: rgba(251, 236, 221, 1);\n      }\n      .highlight-yellow_background {\n        background: rgba(251, 243, 219, 1);\n      }\n      .highlight-teal_background {\n        background: rgba(237, 243, 236, 1);\n      }\n      .highlight-blue_background {\n        background: rgba(231, 243, 248, 1);\n      }\n      .highlight-purple_background {\n        background: rgba(244, 240, 247, 0.8);\n      }\n      .highlight-pink_background {\n        background: rgba(249, 238, 243, 0.8);\n      }\n      .highlight-red_background {\n        background: rgba(253, 235, 236, 1);\n      }\n      .block-color-default {\n        color: inherit;\n        fill: inherit;\n      }\n      .block-color-gray {\n        color: rgba(120, 119, 116, 1);\n        fill: rgba(120, 119, 116, 1);\n      }\n      .block-color-brown {\n        color: rgba(159, 107, 83, 1);\n        fill: rgba(159, 107, 83, 1);\n      }\n      .block-color-orange {\n        color: rgba(217, 115, 13, 1);\n        fill: rgba(217, 115, 13, 1);\n      }\n      .block-color-yellow {\n        color: rgba(203, 145, 47, 1);\n        fill: rgba(203, 145, 47, 1);\n      }\n      .block-color-teal {\n        color: rgba(68, 131, 97, 1);\n        fill: rgba(68, 131, 97, 1);\n      }\n      .block-color-blue {\n        color: rgba(51, 126, 169, 1);\n        fill: rgba(51, 126, 169, 1);\n      }\n      .block-color-purple {\n        color: rgba(144, 101, 176, 1);\n        fill: rgba(144, 101, 176, 1);\n      }\n      .block-color-pink {\n        color: rgba(193, 76, 138, 1);\n        fill: rgba(193, 76, 138, 1);\n      }\n      .block-color-red {\n        color: rgba(212, 76, 71, 1);\n        fill: rgba(212, 76, 71, 1);\n      }\n      .block-color-gray_background {\n        background: rgba(241, 241, 239, 1);\n      }\n      .block-color-brown_background {\n        background: rgba(244, 238, 238, 1);\n      }\n      .block-color-orange_background {\n        background: rgba(251, 236, 221, 1);\n      }\n      .block-color-yellow_background {\n        background: rgba(251, 243, 219, 1);\n      }\n      .block-color-teal_background {\n        background: rgba(237, 243, 236, 1);\n      }\n      .block-color-blue_background {\n        background: rgba(231, 243, 248, 1);\n      }\n      .block-color-purple_background {\n        background: rgba(244, 240, 247, 0.8);\n      }\n      .block-color-pink_background {\n        background: rgba(249, 238, 243, 0.8);\n      }\n      .block-color-red_background {\n        background: rgba(253, 235, 236, 1);\n      }\n      .select-value-color-pink {\n        background-color: rgba(245, 224, 233, 1);\n      }\n      .select-value-color-purple {\n        background-color: rgba(232, 222, 238, 1);\n      }\n      .select-value-color-green {\n        background-color: rgba(219, 237, 219, 1);\n      }\n      .select-value-color-gray {\n        background-color: rgba(227, 226, 224, 1);\n      }\n      .select-value-color-opaquegray {\n        background-color: rgba(255, 255, 255, 0.0375);\n      }\n      .select-value-color-orange {\n        background-color: rgba(250, 222, 201, 1);\n      }\n      .select-value-color-brown {\n        background-color: rgba(238, 224, 218, 1);\n      }\n      .select-value-color-red {\n        background-color: rgba(255, 226, 221, 1);\n      }\n      .select-value-color-yellow {\n        background-color: rgba(253, 236, 200, 1);\n      }\n      .select-value-color-blue {\n        background-color: rgba(211, 229, 239, 1);\n      }\n\n      .checkbox {\n        display: inline-flex;\n        vertical-align: text-bottom;\n        width: 16;\n        height: 16;\n        background-size: 16px;\n        margin-left: 2px;\n        margin-right: 5px;\n      }\n\n      .checkbox-on {\n        background-image: url(\"data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%0A%3Crect%20width%3D%2216%22%20height%3D%2216%22%20fill%3D%22%2358A9D7%22%2F%3E%0A%3Cpath%20d%3D%22M6.71429%2012.2852L14%204.9995L12.7143%203.71436L6.71429%209.71378L3.28571%206.2831L2%207.57092L6.71429%2012.2852Z%22%20fill%3D%22white%22%2F%3E%0A%3C%2Fsvg%3E\");\n      }\n\n      .checkbox-off {\n        background-image: url(\"data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%0A%3Crect%20x%3D%220.75%22%20y%3D%220.75%22%20width%3D%2214.5%22%20height%3D%2214.5%22%20fill%3D%22white%22%20stroke%3D%22%2336352F%22%20stroke-width%3D%221.5%22%2F%3E%0A%3C%2Fsvg%3E\");\n      }\n    </style>\n  </head>\n  <body>\n    <article id=\"f2b31a8e-f32a-474c-bf3e-baf4928f6c1c\" class=\"page sans\">\n      <div class=\"page-body\">\n        <p id=\"937a899c-eec7-4aaa-9ec3-631b13c30fb5\" class=\"\">\n          {{ $json.text }}\n        </p>\n        <hr id=\"fc51a942-226f-4411-b001-b5376a835e0c\" />\n        <!--\n            Was this message helpful? Yes • No.\n            If the user clicks \"Yes\", a webhook will be sent to the URL specified in the \"Yes\" button's \"Webhook URL\" field.\n            If the user clicks \"No\", a webhook will be sent to the URL specified in the \"No\" button's \"Webhook URL\" field.\n            Include the following in the webhook URL:\n            - initial message content\n            - reply content\n            use links\n        -->\n        <p id=\"c28c1c98-621b-4169-a7de-90d85d36ca90\" class=\"\">\n          Was this message helpful? <a href={{ $env.WEBHOOK_URL + 'webhook/' + $node[\"On feedback given\"].parameter[\"path\"] }}?id={{ $node[\"Generate UUID\"].json.uuid }}&feedback=Yes>Yes</a> <strong>•</strong> <a href={{ $env.WEBHOOK_URL + 'webhook/' + $node[\"On feedback given\"].parameter[\"path\"] }}?id={{ $node[\"Generate UUID\"].json.uuid }}&feedback=No>No</a>\n        </p>\n        <p id=\"7138639a-e639-4eb8-b80d-3d40bfc5c102\" class=\"\"></p>\n      </div>\n    </article>\n  </body>\n</html>\n"
      },
      "typeVersion": 1
    },
    {
      "id": "38e0f992-a461-4bc1-9f5c-2ceb0e461708",
      "name": "Record feedback",
      "type": "n8n-nodes-base.noOp",
      "position": [
        -1360,
        2980
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "899a0c63-0333-4dc4-ba83-5615a38ae431",
      "name": "Fallback route",
      "type": "n8n-nodes-base.noOp",
      "position": [
        -1360,
        3280
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "2fd5b109-8a54-4684-a8a3-3f7b2d961ae3",
      "name": "Identify trigger #2",
      "type": "n8n-nodes-base.set",
      "position": [
        -2240,
        2940
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "triggeredFrom",
              "value": "webhook"
            }
          ]
        },
        "options": {}
      },
      "typeVersion": 1
    },
    {
      "id": "8c27f798-d947-432c-bfc9-d22727d0159e",
      "name": "Identify trigger #1",
      "type": "n8n-nodes-base.set",
      "position": [
        -2240,
        2680
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "triggeredFrom",
              "value": "gmail"
            }
          ]
        },
        "options": {}
      },
      "typeVersion": 1
    },
    {
      "id": "bd8cc1dd-3643-4d2f-9527-cfd740a4072a",
      "name": "Do not send unfinished email reply",
      "type": "n8n-nodes-base.noOp",
      "position": [
        -40,
        2060
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "c8b68fdb-c1c0-4f94-b712-e0570a3ad53c",
      "name": "If reply is complete",
      "type": "n8n-nodes-base.if",
      "position": [
        -260,
        1960
      ],
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{ $json.finish_reason }}",
              "value2": "stop"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "id": "f9d56d42-aa4e-4394-8c83-8d39164a784e",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -100,
        2020
      ],
      "parameters": {
        "width": 225.59802712700315,
        "height": 314.2786683107279,
        "content": "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nIf your workflow reaches this stage, you will need to consider increasing the tokens in `Generate reply` node."
      },
      "typeVersion": 1
    },
    {
      "id": "039714b3-88ac-4ca8-86fc-ec1c109110c3",
      "name": "Do not send email to this recipient",
      "type": "n8n-nodes-base.noOp",
      "position": [
        -1140,
        2560
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "330c67dd-e538-414d-a144-e05dbf5effb3",
      "name": "Send reply to database",
      "type": "n8n-nodes-base.noOp",
      "position": [
        -260,
        2380
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "6e7586db-f437-4450-a1c7-e5ea7e8767b0",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -3060,
        2520
      ],
      "parameters": {
        "width": 516.6954377311955,
        "height": 680.5491163173024,
        "content": "## Send a ChatGPT email reply when email received and save responses to Google Sheets\nThis workflow sends a OpenAI GPT reply when an email is received from specific email recipients. It then saves the initial email and the GPT response to an automatically generated Google spreadsheet. Subsequent GPT responses will be added to the same spreadsheet. Additionally, when feedback is given for any of the GPT responses, it will be recorded to the spreasheet, which can then be used later to fine-tune the GPT model.\n\n### How it works\nThis workflow is essentially a two-in-one workflow. It triggers off from two different nodes and have very different functionality from each trigger.\n\n**`On email received`**:\n1. Triggers off on the `On email received` node.\n2. Extract the email body from the email.\n3. Generate a response from the email body using the `OpenAI` node.\n4. Reply to the email sender using the `Send reply to recipient` node. A feedback link is also included in the email body which will trigger the `On feedback given` node. This is used to fine-tune the GPT model.\n5. Save the email body and OpenAI response to a Google Sheet. If a sheet does not exist, it will be created.\n\n\n**`On feedback given`**:\n1. Triggers off when a feedback link is clicked in the emailed GPT response.\n2. The feedback, either positive or negative, for that specific GPT response is then recorded to the Google Sheet.\n"
      },
      "typeVersion": 1
    },
    {
      "id": "9d5e780e-4282-4c7e-b083-3f769f7dc740",
      "name": "Determine which trigger ran",
      "type": "n8n-nodes-base.switch",
      "position": [
        -1660,
        2800
      ],
      "parameters": {
        "rules": {
          "rules": [
            {
              "value2": "gmail"
            },
            {
              "output": 1,
              "value2": "webhook"
            }
          ]
        },
        "value1": "={{ $json.triggeredFrom }}",
        "dataType": "string",
        "fallbackOutput": 3
      },
      "typeVersion": 1
    },
    {
      "id": "2c6c604c-7f59-42cc-9ed2-6d55f342f0ae",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -1420,
        3240
      ],
      "parameters": {
        "width": 225.59802712700315,
        "height": 289.61775585696694,
        "content": "\n\n\n\n\n\n\n\n\n\n\n\n\n\nThis workflow should never reach this node. It is only here for extending the functionality of this workflow if needed."
      },
      "typeVersion": 1
    },
    {
      "id": "3defbf98-0caa-49b1-9bfd-f4640b43d64b",
      "name": "Is text within token limit?",
      "type": "n8n-nodes-base.if",
      "position": [
        -700,
        2360
      ],
      "parameters": {
        "conditions": {
          "boolean": [
            {
              "value1": "={{ $json.reply.length() / 4 <= $('Configure').first().json.maxTokenSize - $('Configure').first().json.replyTokenSize }}",
              "value2": true
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "id": "b268b8a3-6361-4515-a995-320cd0979688",
      "name": "Do nothing",
      "type": "n8n-nodes-base.noOp",
      "position": [
        -480,
        2460
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "413588d1-ede0-4a51-85fa-c9035ec2e605",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -540,
        2420
      ],
      "parameters": {
        "width": 225.59802712700315,
        "height": 288.2949081608216,
        "content": "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nThe email that was received is too large to process, as it exceeds token limit. See more on [token limits](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them)."
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Configure": {
      "main": [
        [
          {
            "node": "Determine which trigger ran",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Format data": {
      "main": [
        [
          {
            "node": "If no spreadsheet in configuration #1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Generate UUID": {
      "main": [
        [
          {
            "node": "Extract message content (advanced)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Email template": {
      "main": [
        [
          {
            "node": "Send reply to recipient",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Generate reply": {
      "main": [
        [
          {
            "node": "Send reply to database",
            "type": "main",
            "index": 0
          },
          {
            "node": "If reply is complete",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Show HTML page": {
      "main": [
        [
          {
            "node": "If no spreadsheet in configuration #2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "If no sheet IDs": {
      "main": [
        [
          {
            "node": "Create spreadsheet",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Get data from `Format data`",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Record feedback": {
      "main": [
        [
          {
            "node": "Thanks for your response!",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get sheet IDs #1": {
      "main": [
        [
          {
            "node": "If no sheet IDs",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get sheet IDs #2": {
      "main": [
        [
          {
            "node": "Send feedback for fine-tuned data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Send email reply": {
      "main": [
        [
          {
            "node": "Email template",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "On email received": {
      "main": [
        [
          {
            "node": "Identify trigger #1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "On feedback given": {
      "main": [
        [
          {
            "node": "Identify trigger #2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Create spreadsheet": {
      "main": [
        [
          {
            "node": "Store spreadsheet ID",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Identify trigger #1": {
      "main": [
        [
          {
            "node": "Configure",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Identify trigger #2": {
      "main": [
        [
          {
            "node": "Configure",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "If reply is complete": {
      "main": [
        [
          {
            "node": "Send email reply",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Do not send unfinished email reply",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Store spreadsheet ID": {
      "main": [
        [
          {
            "node": "Get data from `Format data` node",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Create or update rows": {
      "main": [
        [
          {
            "node": "If spreadsheet doesn't exist",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Send reply to database": {
      "main": [
        [
          {
            "node": "Format data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Thanks for your response!": {
      "main": [
        [
          {
            "node": "Show HTML page",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Determine which trigger ran": {
      "main": [
        [
          {
            "node": "Only continue for specific emails",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Record feedback",
            "type": "main",
            "index": 0
          }
        ],
        null,
        [
          {
            "node": "Fallback route",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get data from `Format data`": {
      "main": [
        [
          {
            "node": "Create or update rows",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Is text within token limit?": {
      "main": [
        [
          {
            "node": "Generate reply",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Do nothing",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Store specific sheet IDs #1": {
      "main": [
        [
          {
            "node": "If no sheet IDs",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Store specific sheet IDs #2": {
      "main": [
        [
          {
            "node": "Send feedback for fine-tuned data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "If spreadsheet doesn't exist": {
      "main": [
        [
          {
            "node": "Create spreadsheet",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Successfully created or updated row",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get data from `Format data` node": {
      "main": [
        [
          {
            "node": "Paste data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Only continue for specific emails": {
      "main": [
        [
          {
            "node": "Generate UUID",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Do not send email to this recipient",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract message content (advanced)": {
      "main": [
        [
          {
            "node": "Is text within token limit?",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "If no spreadsheet in configuration #1": {
      "main": [
        [
          {
            "node": "Get sheet IDs #1",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Store specific sheet IDs #1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "If no spreadsheet in configuration #2": {
      "main": [
        [
          {
            "node": "Get sheet IDs #2",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Store specific sheet IDs #2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-904"></a>

## Template 904 - Geração de vídeos com prompts e movimentos de câmera

- **Nome:** Geração de vídeos com prompts e movimentos de câmera
- **Descrição:** Automatiza a geração de vídeos a partir de prompts personalizados com movimentos de câmera aleatórios, registrando os resultados com metadados em uma base.
- **Funcionalidade:** • Início manual do fluxo: O fluxo é iniciado quando o usuário aciona Test workflow.
• Definição de parâmetros globais de geração: Configura prompt, aspecto, duração, loop, cluster ID e informações de integração (base e tabela do Airtable, callback).
• Seleção de movimento de câmera aleatório: Escolhe aleatoriamente um movimento de câmera entre opções pré-definidas.
• Geração de vídeo via API com prompt enriquecido: Envia requisição POST para a API de geração de vídeos com o prompt combinado, modelo e parâmetros, usando autenticação.
• Armazenamento de metadados da geração: Registra modelo, aspecto, duração, prompt, status, cluster ID, ID de geração e URLs na Airtable.
• Registro de dados de execução: Encaminha os resultados ao fluxo para rastreamento e histórico.
- **Ferramentas:** • Luma Dream Machine API: Serviço externo para geração de vídeos a partir de prompts e parâmetros de geração.
• Airtable: Base de dados para registrar informações de cada geração, incluindo status e IDs.

## Fluxo visual

```mermaid
flowchart LR
    N1["When clicking ‘Test workflow’"]
    N2["Text 2 Video"]
    N3["RANDOM Camera Motion"]
    N4["Sticky Note"]
    N5["Global SETTINGS"]
    N6["ADD Video Info"]
    N7["Execution Data"]
    N8["Sticky Note1"]

    N2 --> N7
    N7 --> N6
    N5 --> N3
    N3 --> N2
    N1 --> N5
```

## Fluxo (.json) :

```json
{
  "id": "2pMoIW58KP6ZeGir",
  "meta": {
    "instanceId": "ecc960f484e18b0e09045fd93acf0d47f4cfff25cc212ea348a08ac3aae81850",
    "templateCredsSetupCompleted": true
  },
  "name": "Luma AI Dream Machine - Simple v1 - AK",
  "tags": [
    {
      "id": "tUlWC9t8VhwpFaci",
      "name": "Alex - WIP",
      "createdAt": "2025-02-20T17:17:53.411Z",
      "updatedAt": "2025-02-20T17:17:53.411Z"
    }
  ],
  "nodes": [
    {
      "id": "dbe1dbcc-05a0-4439-869c-157e51a99dd1",
      "name": "When clicking ‘Test workflow’",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        -440,
        0
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "603f7fdd-e590-4a51-b606-a9bb9396a0c0",
      "name": "Text 2 Video",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        220,
        0
      ],
      "parameters": {
        "url": "https://api.lumalabs.ai/dream-machine/v1/generations",
        "method": "POST",
        "options": {},
        "jsonBody": "={\n  \"model\": \"ray-2\",\n  \"prompt\": {{ JSON.stringify($('Global SETTINGS').first().json.video_prompt + \"; camera motion: \" + $json.action) }},\n  \"aspect_ratio\": \"{{ $('Global SETTINGS').first().json.aspect_ratio }}\",\n  \"duration\": \"{{ $('Global SETTINGS').item.json.duration }}\",\n  \"loop\": {{ $('Global SETTINGS').first().json.loop }},\n  \"callback_url\": \"{{ $('Global SETTINGS').first().json.callback_url }}\"\n  \n}",
        "sendBody": true,
        "sendHeaders": true,
        "specifyBody": "json",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "headerParameters": {
          "parameters": [
            {
              "name": "accept",
              "value": "application/json"
            }
          ]
        }
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "zzIlODir90EUTwHh",
          "name": "Luma Header Auth account"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "494ac05e-e0c5-465e-b805-2749683ab789",
      "name": "RANDOM Camera Motion",
      "type": "n8n-nodes-base.code",
      "position": [
        0,
        0
      ],
      "parameters": {
        "jsCode": "const items = [\n  \"Static\",\n  \"Move Left\",\n  \"Move Right\",\n  \"Move Up\",\n  \"Move Down\",\n  \"Push In\",\n  \"Pull Out\",\n  \"Zoom In\",\n  \"Zoom Out\",\n  \"Pan Left\",\n  \"Pan Right\",\n  \"Orbit Left\",\n  \"Orbit Right\",\n  \"Crane Up\",\n  \"Crane Down\"\n];\n\nconst randomItem = items[Math.floor(Math.random() * items.length)];\n\nreturn [{ json: { action: randomItem } }];\n"
      },
      "typeVersion": 2
    },
    {
      "id": "30ba7cfc-d2c3-478f-ae01-0a3397ceb439",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -260,
        -120
      ],
      "parameters": {
        "color": 3,
        "width": 180,
        "content": "## Define your SETTINGS here"
      },
      "typeVersion": 1
    },
    {
      "id": "12924397-b2a4-43a0-8ec5-1b13c0357e40",
      "name": "Global SETTINGS",
      "type": "n8n-nodes-base.set",
      "position": [
        -220,
        0
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "7064f685-d91f-4049-9fcb-dd7018c1bc8d",
              "name": "aspect_ratio",
              "type": "string",
              "value": "9:16"
            },
            {
              "id": "3d6d3fe0-4e4a-4d1b-9f6a-08037a4e2785",
              "name": "video_prompt",
              "type": "string",
              "value": "a superhero flying through a volcano"
            },
            {
              "id": "7ae48bee-0be5-487f-8d6d-ea7fe98fdd36",
              "name": "loop",
              "type": "string",
              "value": "true"
            },
            {
              "id": "82930db0-971e-4de4-911d-ff5a7fab5d67",
              "name": "duration",
              "type": "string",
              "value": "5s"
            },
            {
              "id": "b51d9834-87c8-4358-a257-6a02ebe2576d",
              "name": "cluster_id",
              "type": "string",
              "value": "={{ Date.now() + '_' + Math.random().toString(36).slice(2, 10) }}"
            },
            {
              "id": "8756fe2d-df04-48d4-9cd4-d29b8d9a3ab1",
              "name": "airtable_base",
              "type": "string",
              "value": "appvk87mtcwRve5p5"
            },
            {
              "id": "a83707ef-3a1c-4b3c-939c-1376bc43cc76",
              "name": "airtable_table_generated_videos",
              "type": "string",
              "value": "tblOzRFWgcsfttRWK"
            },
            {
              "id": "694528cd-c51e-45ac-8dbe-1b33b347f590",
              "name": "callback_url",
              "type": "string",
              "value": "https://YOURURL.com/luma-ai"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "9f4732b5-8e3e-4fb6-942f-32c72b3eb041",
      "name": "ADD Video Info",
      "type": "n8n-nodes-base.airtable",
      "position": [
        660,
        0
      ],
      "parameters": {
        "base": {
          "__rl": true,
          "mode": "id",
          "value": "={{ $('Global SETTINGS').first().json.airtable_base }}"
        },
        "table": {
          "__rl": true,
          "mode": "id",
          "value": "={{ $('Global SETTINGS').first().json.airtable_table_generated_videos }}"
        },
        "columns": {
          "value": {
            "Model": "={{ $json.model }}",
            "Aspect": "={{ $json.request.aspect_ratio }}",
            "Length": "={{ $json.request.duration }}",
            "Prompt": "={{ $('Global SETTINGS').first().json.video_prompt }}",
            "Status": "Done",
            "Cluster ID": "={{ $('Global SETTINGS').first().json.cluster_id }}",
            "Resolution": "={{ $json.request.resolution }}",
            "Generation ID": "={{ $json.id }}"
          },
          "schema": [
            {
              "id": "Generation ID",
              "type": "string",
              "display": true,
              "removed": false,
              "readOnly": false,
              "required": false,
              "displayName": "Generation ID",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Status",
              "type": "options",
              "display": true,
              "options": [
                {
                  "name": "Todo",
                  "value": "Todo"
                },
                {
                  "name": "In progress",
                  "value": "In progress"
                },
                {
                  "name": "Done",
                  "value": "Done"
                }
              ],
              "removed": false,
              "readOnly": false,
              "required": false,
              "displayName": "Status",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Content Title",
              "type": "string",
              "display": true,
              "removed": false,
              "readOnly": false,
              "required": false,
              "displayName": "Content Title",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Video URL",
              "type": "string",
              "display": true,
              "removed": false,
              "readOnly": false,
              "required": false,
              "displayName": "Video URL",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Thumb URL",
              "type": "string",
              "display": true,
              "removed": false,
              "readOnly": false,
              "required": false,
              "displayName": "Thumb URL",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Prompt",
              "type": "string",
              "display": true,
              "removed": false,
              "readOnly": false,
              "required": false,
              "displayName": "Prompt",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "VO",
              "type": "string",
              "display": true,
              "removed": false,
              "readOnly": false,
              "required": false,
              "displayName": "VO",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Aspect",
              "type": "string",
              "display": true,
              "removed": false,
              "readOnly": false,
              "required": false,
              "displayName": "Aspect",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Model",
              "type": "string",
              "display": true,
              "removed": false,
              "readOnly": false,
              "required": false,
              "displayName": "Model",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Resolution",
              "type": "string",
              "display": true,
              "removed": false,
              "readOnly": false,
              "required": false,
              "displayName": "Resolution",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Length",
              "type": "string",
              "display": true,
              "removed": false,
              "readOnly": false,
              "required": false,
              "displayName": "Length",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Created",
              "type": "string",
              "display": true,
              "removed": false,
              "readOnly": true,
              "required": false,
              "displayName": "Created",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Cluster ID",
              "type": "string",
              "display": true,
              "removed": false,
              "readOnly": false,
              "required": false,
              "displayName": "Cluster ID",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            }
          ],
          "mappingMode": "defineBelow",
          "matchingColumns": [],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {},
        "operation": "create"
      },
      "credentials": {
        "airtableTokenApi": {
          "id": "yqBrLbgHXLcwqH0p",
          "name": "AlexK Airtable Personal Access Token account"
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "9923373d-d4ce-42bb-9f2d-34350f64ac5b",
      "name": "Execution Data",
      "type": "n8n-nodes-base.executionData",
      "position": [
        440,
        0
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "5044e1f2-c985-4c3a-9386-f4fe4f85f37b",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -40,
        -120
      ],
      "parameters": {
        "color": 5,
        "width": 840,
        "content": "## This is where the magic happens... "
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "e756199d-31fc-4e2f-8937-3625295a147c",
  "connections": {
    "Text 2 Video": {
      "main": [
        [
          {
            "node": "Execution Data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "ADD Video Info": {
      "main": [
        []
      ]
    },
    "Execution Data": {
      "main": [
        [
          {
            "node": "ADD Video Info",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Global SETTINGS": {
      "main": [
        [
          {
            "node": "RANDOM Camera Motion",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "RANDOM Camera Motion": {
      "main": [
        [
          {
            "node": "Text 2 Video",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "When clicking ‘Test workflow’": {
      "main": [
        [
          {
            "node": "Global SETTINGS",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-905"></a>

## Template 905 - Extração e análise de documentos com Mistral OCR

- **Nome:** Extração e análise de documentos com Mistral OCR
- **Descrição:** Fluxo que processa PDFs e imagens para extrair texto e permitir consultas ao conteúdo, usando URLs públicos ou uploads privados para gerar links assinados e executar OCR e análise de documentos.
- **Funcionalidade:** • Processamento por URL público: Aceita URLs públicas de PDFs ou imagens e envia diretamente ao serviço de OCR/consulta para extração e análise.
• Upload e acesso privado: Baixa arquivos do Google Drive, faz upload para armazenamento na nuvem do provedor e obtém URLs assinadas para processamento seguro.
• OCR de documentos e imagens: Chama modelos OCR específicos para documentos multi-página (document_url) e para imagens (image_url), incluindo opção para retornar imagem em base64.
• Geração de URL assinada: Solicita URLs com tempo de expiração configurável para acesso seguro a arquivos privados armazenados no provedor.
• Consulta de entendimento de documento: Usa modelos de linguagem para responder perguntas sobre o conteúdo do documento ou imagem fornecida, com limites configuráveis de páginas e imagens.
• Exemplos demonstrativos: Inclui fluxos de exemplo para URL público, upload privado e comparação de modelos (ex.: uso de modelo Pixtral para imagens).
- **Ferramentas:** • Mistral Cloud: Plataforma que fornece serviços de OCR, modelos de linguagem para chat/completion e hospedagem de arquivos com suporte a upload e geração de URLs assinadas.
• Google Drive: Armazenamento na nuvem usado para buscar e baixar arquivos privados que serão enviados ao provedor de OCR.
• Hospedagem pública de arquivos (object storage): URLs públicas de arquivos (por exemplo, buckets/objetos públicos) usadas para enviar documentos e imagens diretamente ao OCR sem necessidade de upload adicional.

## Fluxo visual

```mermaid
flowchart LR
    N1["Mistral Upload"]
    N2["When clicking ‘Test workflow’"]
    N3["Mistral Signed URL"]
    N4["Import PDF"]
    N5["Import Image"]
    N6["Mistral Upload1"]
    N7["Mistral Signed URL1"]
    N8["Mistral DOC OCR"]
    N9["Mistral IMAGE OCR"]
    N10["Document URL"]
    N11["Image URL"]
    N12["Sticky Note"]
    N13["Sticky Note1"]
    N14["Mistral DOC OCR1"]
    N15["Mistral IMAGE OCR1"]
    N16["Sticky Note2"]
    N17["Sticky Note3"]
    N18["Document URL1"]
    N19["Document Understanding"]
    N20["Image URL1"]
    N21["Document Mis-Understanding?"]

    N11 --> N15
    N20 --> N21
    N4 --> N1
    N10 --> N14
    N5 --> N6
    N18 --> N19
    N1 --> N3
    N6 --> N7
    N3 --> N8
    N7 --> N9
    N2 --> N10
    N2 --> N11
```

## Fluxo (.json) :

```json
{
  "meta": {
    "instanceId": "408f9fb9940c3cb18ffdef0e0150fe342d6e655c3a9fac21f0f644e8bedabcd9",
    "templateCredsSetupCompleted": true
  },
  "nodes": [
    {
      "id": "c499b8cc-7cc8-411d-9c22-d46c7654e169",
      "name": "Mistral Upload",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        700,
        -20
      ],
      "parameters": {
        "url": "https://api.mistral.ai/v1/files",
        "method": "POST",
        "options": {},
        "sendBody": true,
        "contentType": "multipart-form-data",
        "authentication": "predefinedCredentialType",
        "bodyParameters": {
          "parameters": [
            {
              "name": "purpose",
              "value": "ocr"
            },
            {
              "name": "file",
              "parameterType": "formBinaryData",
              "inputDataFieldName": "data"
            }
          ]
        },
        "nodeCredentialType": "mistralCloudApi"
      },
      "credentials": {
        "mistralCloudApi": {
          "id": "EIl2QxhXAS9Hkg37",
          "name": "Mistral Cloud account"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "08cbe4b7-2adc-4ea0-8dfc-af107369b1dd",
      "name": "When clicking ‘Test workflow’",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        -540,
        -20
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "965f294a-5d77-4190-ad4f-ff191aba0948",
      "name": "Mistral Signed URL",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        900,
        -20
      ],
      "parameters": {
        "url": "=https://api.mistral.ai/v1/files/{{ $json.id }}/url",
        "options": {},
        "sendQuery": true,
        "sendHeaders": true,
        "authentication": "predefinedCredentialType",
        "queryParameters": {
          "parameters": [
            {
              "name": "expiry",
              "value": "24"
            }
          ]
        },
        "headerParameters": {
          "parameters": [
            {
              "name": "Accept",
              "value": "application/json"
            }
          ]
        },
        "nodeCredentialType": "mistralCloudApi"
      },
      "credentials": {
        "mistralCloudApi": {
          "id": "EIl2QxhXAS9Hkg37",
          "name": "Mistral Cloud account"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "7abfb1f8-f6c8-4fd0-a78e-9d4b97a4d6bc",
      "name": "Import PDF",
      "type": "n8n-nodes-base.googleDrive",
      "position": [
        480,
        -20
      ],
      "parameters": {
        "fileId": {
          "__rl": true,
          "mode": "id",
          "value": "15BcE6nXto9lQDHPmwjm7y9JPerAVEutY"
        },
        "options": {},
        "operation": "download"
      },
      "credentials": {
        "googleDriveOAuth2Api": {
          "id": "yOwz41gMQclOadgu",
          "name": "Google Drive account"
        }
      },
      "typeVersion": 3
    },
    {
      "id": "8942c6bf-4d86-4a95-aa4a-c819008e2534",
      "name": "Import Image",
      "type": "n8n-nodes-base.googleDrive",
      "position": [
        480,
        200
      ],
      "parameters": {
        "fileId": {
          "__rl": true,
          "mode": "id",
          "value": "1a2FcRDWHHncMO8CYxD80uNUBGH1Sy1k2"
        },
        "options": {},
        "operation": "download"
      },
      "credentials": {
        "googleDriveOAuth2Api": {
          "id": "yOwz41gMQclOadgu",
          "name": "Google Drive account"
        }
      },
      "typeVersion": 3
    },
    {
      "id": "94a1c3ca-1ca7-4bb1-9e7c-8314742423ab",
      "name": "Mistral Upload1",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        700,
        200
      ],
      "parameters": {
        "url": "https://api.mistral.ai/v1/files",
        "method": "POST",
        "options": {},
        "sendBody": true,
        "contentType": "multipart-form-data",
        "authentication": "predefinedCredentialType",
        "bodyParameters": {
          "parameters": [
            {
              "name": "purpose",
              "value": "ocr"
            },
            {
              "name": "file",
              "parameterType": "formBinaryData",
              "inputDataFieldName": "data"
            }
          ]
        },
        "nodeCredentialType": "mistralCloudApi"
      },
      "credentials": {
        "mistralCloudApi": {
          "id": "EIl2QxhXAS9Hkg37",
          "name": "Mistral Cloud account"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "9d075eec-ba0e-41e1-8bdc-a732bc0f9229",
      "name": "Mistral Signed URL1",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        900,
        200
      ],
      "parameters": {
        "url": "=https://api.mistral.ai/v1/files/{{ $json.id }}/url",
        "options": {},
        "sendQuery": true,
        "sendHeaders": true,
        "authentication": "predefinedCredentialType",
        "queryParameters": {
          "parameters": [
            {
              "name": "expiry",
              "value": "24"
            }
          ]
        },
        "headerParameters": {
          "parameters": [
            {
              "name": "Accept",
              "value": "application/json"
            }
          ]
        },
        "nodeCredentialType": "mistralCloudApi"
      },
      "credentials": {
        "mistralCloudApi": {
          "id": "EIl2QxhXAS9Hkg37",
          "name": "Mistral Cloud account"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "f623f066-fc70-40fa-b608-f28a75a8ac8c",
      "name": "Mistral DOC OCR",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1100,
        -20
      ],
      "parameters": {
        "url": "https://api.mistral.ai/v1/ocr",
        "method": "POST",
        "options": {},
        "jsonBody": "={\n  \"model\": \"mistral-ocr-latest\",\n  \"document\": {\n    \"type\": \"document_url\",\n    \"document_url\": \"{{ $json.url }}\"\n  },\n  \"include_image_base64\": true\n}",
        "sendBody": true,
        "specifyBody": "json",
        "authentication": "predefinedCredentialType",
        "nodeCredentialType": "mistralCloudApi"
      },
      "credentials": {
        "mistralCloudApi": {
          "id": "EIl2QxhXAS9Hkg37",
          "name": "Mistral Cloud account"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "15913796-e7c8-451a-8e7b-da7a3b10db02",
      "name": "Mistral IMAGE OCR",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1100,
        200
      ],
      "parameters": {
        "url": "https://api.mistral.ai/v1/ocr",
        "method": "POST",
        "options": {},
        "jsonBody": "={\n  \"model\": \"mistral-ocr-latest\",\n  \"document\": {\n    \"type\": \"image_url\",\n    \"image_url\": \"{{ $json.url }}\"\n  }\n}",
        "sendBody": true,
        "specifyBody": "json",
        "authentication": "predefinedCredentialType",
        "nodeCredentialType": "mistralCloudApi"
      },
      "credentials": {
        "mistralCloudApi": {
          "id": "EIl2QxhXAS9Hkg37",
          "name": "Mistral Cloud account"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "a79524ff-84f0-46db-bb8e-afc18f1ddd40",
      "name": "Document URL",
      "type": "n8n-nodes-base.set",
      "position": [
        -160,
        -20
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "1eb5f18b-eb06-48df-8491-d60de75b4855",
              "name": "url",
              "type": "string",
              "value": "=https://pub-d4aa9be14ae34d6ebcebe06f13af667b.r2.dev/multimodal_bank_statement_scan.pdf"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "72b89f33-a67c-4f73-9a78-e8ccd02fbc98",
      "name": "Image URL",
      "type": "n8n-nodes-base.set",
      "position": [
        -160,
        200
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "1eb5f18b-eb06-48df-8491-d60de75b4855",
              "name": "url",
              "type": "string",
              "value": "=https://pub-d4aa9be14ae34d6ebcebe06f13af667b.r2.dev/multimodal_bank_statement_2.png"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "808ccbb3-0dae-4e2c-9166-bf40c589824a",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -320,
        -160
      ],
      "parameters": {
        "color": 7,
        "width": 680,
        "height": 580,
        "content": "### Example 1. Publicly Hosted Files\nThe default way to use Mistral OCR is to give it a public URL of the file you want processed. Great for your own semi-private docs or other people's. If you rather not expose files due to privacy concerns, then you'd want to check out example 2."
      },
      "typeVersion": 1
    },
    {
      "id": "b968d6ab-9582-495d-84af-f75833701e2a",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        400,
        -160
      ],
      "parameters": {
        "color": 7,
        "width": 920,
        "height": 560,
        "content": "### Example 2. Privately Hosted via Mistral Cloud\nGive Mistral OCR private and secure access to your files by uploading them to Mistral cloud first. Retrieve the file using a signed URL and pass this to Mistral OCR. Benefit of storing via Mistral could be faster cache access and reduced latency for repeat docs."
      },
      "typeVersion": 1
    },
    {
      "id": "f2c0b30a-49be-4850-b102-f23d0feac0ec",
      "name": "Mistral DOC OCR1",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        60,
        -20
      ],
      "parameters": {
        "url": "https://api.mistral.ai/v1/ocr",
        "method": "POST",
        "options": {},
        "jsonBody": "={\n  \"model\": \"mistral-ocr-latest\",\n  \"document\": {\n    \"type\": \"document_url\",\n    \"document_url\": \"{{ $json.url }}\"\n  }\n}",
        "sendBody": true,
        "specifyBody": "json",
        "authentication": "predefinedCredentialType",
        "nodeCredentialType": "mistralCloudApi"
      },
      "credentials": {
        "mistralCloudApi": {
          "id": "EIl2QxhXAS9Hkg37",
          "name": "Mistral Cloud account"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "64a28537-e70b-48bc-b580-cc9d5a5a1b80",
      "name": "Mistral IMAGE OCR1",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        60,
        200
      ],
      "parameters": {
        "url": "https://api.mistral.ai/v1/ocr",
        "method": "POST",
        "options": {},
        "jsonBody": "={\n  \"model\": \"mistral-ocr-latest\",\n  \"document\": {\n    \"type\": \"image_url\",\n    \"image_url\": \"{{ $json.url }}\"\n  }\n}",
        "sendBody": true,
        "specifyBody": "json",
        "authentication": "predefinedCredentialType",
        "nodeCredentialType": "mistralCloudApi"
      },
      "credentials": {
        "mistralCloudApi": {
          "id": "EIl2QxhXAS9Hkg37",
          "name": "Mistral Cloud account"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "3caaa30b-21f2-4643-93dd-8dff6f3c1920",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -740,
        -440
      ],
      "parameters": {
        "width": 380,
        "height": 640,
        "content": "## Document Parsing with Mistral OCR\nUp your structured document parsing game with Mistral's latest release... **Mistral-OCR**!\n* Designed to specifically parse PDF and image files.\n* Handles multiple-page documents and images up to 10k pixels.\n* Each page is conveniently transcribed as markdown only - there is no plain text output.\n* Incredible pricing at only $0.001 per page!\n\n### Requirements\n* You'll need a Mistral Cloud API Key\n* This template only works with the Mistral Cloud API for Mistral OCR."
      },
      "typeVersion": 1
    },
    {
      "id": "bd4d0c9f-f4a6-4527-8f9d-5af90a2858c2",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1360,
        -160
      ],
      "parameters": {
        "color": 7,
        "width": 680,
        "height": 580,
        "content": "### Example 3. No need for Extraction? Talk Directly with the File!\nIt seems Mistral were also able to integrate OCR capabilities into its text models which allows you to carry out tasks such as document classification and sentiment analysis really quickly. Unfortunately, it doesn't work the same way with images - you have to use Pixtral but the results are really bad!"
      },
      "typeVersion": 1
    },
    {
      "id": "c9a9d4bb-4ee6-413a-9f08-97fdcee22bf2",
      "name": "Document URL1",
      "type": "n8n-nodes-base.set",
      "position": [
        1520,
        -20
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "1eb5f18b-eb06-48df-8491-d60de75b4855",
              "name": "url",
              "type": "string",
              "value": "=https://pub-d4aa9be14ae34d6ebcebe06f13af667b.r2.dev/multimodal_bank_statement_scan.pdf"
            },
            {
              "id": "c639fce3-6967-444d-be18-6c9ce802ef22",
              "name": "query",
              "type": "string",
              "value": "what is the total number of deposits?"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "5de4d62c-af8f-4e6d-adbd-2f591a2165f7",
      "name": "Document Understanding",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1740,
        -20
      ],
      "parameters": {
        "url": "https://api.mistral.ai/v1/chat/completions",
        "method": "POST",
        "options": {},
        "jsonBody": "={\n  \"model\": \"mistral-small-latest\",\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": [\n        {\n          \"type\": \"text\",\n          \"text\": \"{{ $json.query }}\"\n        },\n        {\n          \"type\": \"document_url\",\n          \"document_url\": \"{{ $json.url }}\"\n        }\n      ]\n    }\n  ],\n  \"document_image_limit\": 8,\n  \"document_page_limit\": 64\n}",
        "sendBody": true,
        "specifyBody": "json",
        "authentication": "predefinedCredentialType",
        "nodeCredentialType": "mistralCloudApi"
      },
      "credentials": {
        "mistralCloudApi": {
          "id": "EIl2QxhXAS9Hkg37",
          "name": "Mistral Cloud account"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "9a7bbff0-d446-469d-aa61-838e8c025ad5",
      "name": "Image URL1",
      "type": "n8n-nodes-base.set",
      "position": [
        1520,
        200
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "1eb5f18b-eb06-48df-8491-d60de75b4855",
              "name": "url",
              "type": "string",
              "value": "=https://pub-d4aa9be14ae34d6ebcebe06f13af667b.r2.dev/multimodal_bank_statement_2.png"
            },
            {
              "id": "639cd062-ebef-44ab-97a2-79ee388f8b41",
              "name": "query",
              "type": "string",
              "value": "what is the total number of deposits?"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "ca43d437-a373-4938-a0a8-8087a98d46a8",
      "name": "Document Mis-Understanding?",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1740,
        200
      ],
      "parameters": {
        "url": "https://api.mistral.ai/v1/chat/completions",
        "method": "POST",
        "options": {},
        "jsonBody": "={\n  \"model\": \"pixtral-large-latest\",\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": [\n        {\n          \"type\": \"text\",\n          \"text\": \"{{ $json.query }}\"\n        },\n        {\n          \"type\": \"image_url\",\n          \"image_url\": \"{{ $json.url }}\"\n        }\n      ]\n    }\n  ],\n  \"document_image_limit\": 8,\n  \"document_page_limit\": 64\n}",
        "sendBody": true,
        "specifyBody": "json",
        "authentication": "predefinedCredentialType",
        "nodeCredentialType": "mistralCloudApi"
      },
      "credentials": {
        "mistralCloudApi": {
          "id": "EIl2QxhXAS9Hkg37",
          "name": "Mistral Cloud account"
        }
      },
      "typeVersion": 4.2
    }
  ],
  "pinData": {},
  "connections": {
    "Image URL": {
      "main": [
        [
          {
            "node": "Mistral IMAGE OCR1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Image URL1": {
      "main": [
        [
          {
            "node": "Document Mis-Understanding?",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Import PDF": {
      "main": [
        [
          {
            "node": "Mistral Upload",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Document URL": {
      "main": [
        [
          {
            "node": "Mistral DOC OCR1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Import Image": {
      "main": [
        [
          {
            "node": "Mistral Upload1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Document URL1": {
      "main": [
        [
          {
            "node": "Document Understanding",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Mistral Upload": {
      "main": [
        [
          {
            "node": "Mistral Signed URL",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Mistral Upload1": {
      "main": [
        [
          {
            "node": "Mistral Signed URL1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Mistral DOC OCR1": {
      "main": [
        []
      ]
    },
    "Mistral Signed URL": {
      "main": [
        [
          {
            "node": "Mistral DOC OCR",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Mistral Signed URL1": {
      "main": [
        [
          {
            "node": "Mistral IMAGE OCR",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "When clicking ‘Test workflow’": {
      "main": [
        [
          {
            "node": "Document URL",
            "type": "main",
            "index": 0
          },
          {
            "node": "Image URL",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-906"></a>

## Template 906 - Sincronização de leads de PostgreSQL para Google Sheets

- **Nome:** Sincronização de leads de PostgreSQL para Google Sheets
- **Descrição:** Fluxo que detecta atualizações na tabela de usuários, filtra emails indesejados e grava usuários qualificados em uma planilha Google Sheets.
- **Funcionalidade:** • Detecção de evento de atualização na tabela de usuários: inicia o fluxo quando ocorre um UPDATE.
• Filtragem de emails indesejados: remove registros cujo email contenha @n8n.io.
• Mapeamento de dados para gravação: seleciona id, username e email para gravação na planilha.
• Gravação em planilha externa: adiciona ou atualiza registros na planilha de leads qualificados (operaçao appendOrUpdate).
• Teste com dados mock: utiliza dados simulados gerados em um nó de código para testes via trigger manual.
- **Ferramentas:** • PostgreSQL: Banco de dados que aciona o fluxo por meio de um trigger de UPDATE na tabela de usuários.
• Google Sheets: Planilha usada para armazenar os usuários qualificados.

## Fluxo visual

```mermaid
flowchart LR
    N1["Postgres Trigger"]
    N2["Filter"]
    N3["Sticky Note1"]
    N4["Sticky Note"]
    N5["Sticky Note6"]
    N6["Sticky Note2"]
    N7["On clicking 'Execute Node'"]
    N8["Code"]
    N9["Google Sheets"]

    N8 --> N2
    N2 --> N9
    N1 --> N2
    N7 --> N8
```

## Fluxo (.json) :

```json
{
  "nodes": [
    {
      "id": "678e86bc-2755-4c79-97d6-fa4da1ed9ff9",
      "name": "Postgres Trigger",
      "type": "n8n-nodes-base.postgresTrigger",
      "disabled": true,
      "position": [
        500,
        480
      ],
      "parameters": {
        "schema": {
          "__rl": true,
          "mode": "list",
          "value": "computed",
          "cachedResultName": "computed"
        },
        "firesOn": "UPDATE",
        "tableName": {
          "__rl": true,
          "mode": "list",
          "value": "users",
          "cachedResultName": "users"
        },
        "additionalFields": {}
      },
      "credentials": {
        "postgres": {
          "id": "8",
          "name": "Postgres Product Analytics"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "accecdfc-283c-4119-9b23-4cf44bc5e68c",
      "name": "Filter",
      "type": "n8n-nodes-base.filter",
      "notes": "Filter out @n8n.io emails",
      "position": [
        980,
        540
      ],
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{ $json.email }}",
              "value2": "n8n.io",
              "operation": "notContains"
            }
          ]
        }
      },
      "notesInFlow": true,
      "typeVersion": 1
    },
    {
      "id": "d16d7ae7-0c60-48f0-97fe-c7618cab73d3",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        0,
        380
      ],
      "parameters": {
        "width": 424,
        "height": 559,
        "content": "## 👋 How to use this template\nThis template shows how to sync data from one service to another. In this example we're saving a new qualified lead to a Google Sheets file. Here's how you can test the template:\n\n1. Duplicate our [Google Sheets](https://docs.google.com/spreadsheets/d/1gVfyernVtgYXD-oPboxOSJYQ-HEfAguEryZ7gTtK0V8/edit?usp=sharing) file\n2. Double click the `Google Sheets` node and create a credential by signing in.\n3. Select the correct Google Sheets document and sheet.\n4. Click the `Execute Workflow` button and double click the nodes to see the input and output data\n\n### To customize it to you needs, just do the following:\n1. Enable or exchange the `Postgres trigger` with any service that fits your use case.\n2. Change the `Filter` to fit your needs\n3. Adjust the Google Sheets node as described above\n4. Disable or remove the `On clicking \"Execute Node\"` and `Code` node\n"
      },
      "typeVersion": 1
    },
    {
      "id": "8bc7439e-d814-4960-8b75-fc77805f74c7",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        460,
        380
      ],
      "parameters": {
        "width": 344,
        "height": 562,
        "content": "### 1. Trigger step listens for new events\n\n"
      },
      "typeVersion": 1
    },
    {
      "id": "63b2bc4c-8e33-4432-af4b-4595b2012ce1",
      "name": "Sticky Note6",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        840,
        460
      ],
      "parameters": {
        "width": 462,
        "height": 407,
        "content": "### 2. Filter and transform your data\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nIn this case, we only want to save qualified users that don't have `@n8n.io` in their email address.\n\nTo edit the filter, simply drag and drop input data into the fields or change the values directly. **Besides filters, n8n has other powerful transformation nodes like [Set](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.set/?utm_source=n8n_app&utm_medium=node_settings_modal-credential_link&utm_campaign=n8n-nodes-base.set), [ItemList](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.itemlists/?utm_source=n8n_app&utm_medium=node_settings_modal-credential_link&utm_campaign=n8n-nodes-base.itemLists), [Code](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.code/?utm_source=n8n_app&utm_medium=node_settings_modal-credential_link&utm_campaign=n8n-nodes-base.code) and many more.**"
      },
      "typeVersion": 1
    },
    {
      "id": "448e2c49-aa75-405b-ba51-3acbce0fb758",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1340,
        460
      ],
      "parameters": {
        "width": 342.52886836027733,
        "height": 407.43618112665195,
        "content": "### 3. Save the user in a Google Sheet\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nFor simplicity, we're saving our qualified user in a Google Sheet.\n\n**You can replace this node with any service like [Excel](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftexcel/?utm_source=n8n_app&utm_medium=node_settings_modal-credential_link&utm_campaign=n8n-nodes-base.microsoftExcel), [HubSpot](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.hubspot/?utm_source=n8n_app&utm_medium=node_settings_modal-credential_link&utm_campaign=n8n-nodes-base.hubspot), [Pipedrive](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.pipedrive/?utm_source=n8n_app&utm_medium=node_settings_modal-credential_link&utm_campaign=n8n-nodes-base.pipedrive), [Zendesk](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.zendesk/?utm_source=n8n_app&utm_medium=node_settings_modal-credential_link&utm_campaign=n8n-nodes-base.zendesk) etc.**"
      },
      "typeVersion": 1
    },
    {
      "id": "c0ee182d-4c31-488b-a547-5f2d2ba8786e",
      "name": "On clicking \"Execute Node\"",
      "type": "n8n-nodes-base.manualTrigger",
      "notes": "For testing the workflow",
      "position": [
        500,
        680
      ],
      "parameters": {},
      "notesInFlow": true,
      "typeVersion": 1
    },
    {
      "id": "87f2a11e-f704-4c9e-ac8b-ee1f057cd347",
      "name": "Code",
      "type": "n8n-nodes-base.code",
      "notes": "Mock Data",
      "position": [
        680,
        680
      ],
      "parameters": {
        "jsCode": "return [\n  {\n    \"id\": 1,\n    \"username\": \"max_mustermann\",\n    \"email\": \"max_mustermann@acme.com\",\n    \"company_size\": \"500-999\",\n    \"role\": \"Sales\",\n    \"users\": 50\n  }\n]"
      },
      "notesInFlow": true,
      "typeVersion": 1
    },
    {
      "id": "0992077f-b6d3-47d2-94d2-c612dfbf5062",
      "name": "Google Sheets",
      "type": "n8n-nodes-base.googleSheets",
      "notes": "Add to \"Users to contact\"",
      "position": [
        1400,
        540
      ],
      "parameters": {
        "columns": {
          "value": {
            "id": "={{ $json.id }}",
            "email": "={{ $json.email }}",
            "username": "={{ $json.username }}"
          },
          "schema": [
            {
              "id": "id",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "id",
              "defaultMatch": true,
              "canBeUsedToMatch": true
            },
            {
              "id": "username",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "username",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "email",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "email",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "contacted",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "contacted",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            }
          ],
          "mappingMode": "defineBelow",
          "matchingColumns": [
            "id"
          ]
        },
        "options": {
          "cellFormat": "USER_ENTERED"
        },
        "operation": "appendOrUpdate",
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": "gid=0",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1gVfyernVtgYXD-oPboxOSJYQ-HEfAguEryZ7gTtK0V8/edit#gid=0",
          "cachedResultName": "Sheet1"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "1gVfyernVtgYXD-oPboxOSJYQ-HEfAguEryZ7gTtK0V8",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1gVfyernVtgYXD-oPboxOSJYQ-HEfAguEryZ7gTtK0V8/edit?usp=drivesdk",
          "cachedResultName": "Qualified leads to contact"
        }
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "9",
          "name": "Google Sheets account"
        }
      },
      "notesInFlow": true,
      "typeVersion": 4
    }
  ],
  "connections": {
    "Code": {
      "main": [
        [
          {
            "node": "Filter",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Filter": {
      "main": [
        [
          {
            "node": "Google Sheets",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Postgres Trigger": {
      "main": [
        [
          {
            "node": "Filter",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "On clicking \"Execute Node\"": {
      "main": [
        [
          {
            "node": "Code",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-907"></a>

## Template 907 - Resumo semanal de UX no Slack

- **Nome:** Resumo semanal de UX no Slack
- **Descrição:** Este fluxo coleta novas ideias de UX de uma base Notion, filtra apenas itens com tipo UX, gera um contador de ideias únicas e envia um resumo semanal para um canal no Slack.
- **Funcionalidade:** • Agendamento da automação: inicia o fluxo a cada semana com um Schedule Trigger.
• Carregar dados: busca itens criados nos últimos 7 dias de uma base de dados de ideias de UX no Notion.
• Filtrar UX: mantém apenas itens cujo campo de tipo inclui UX.
• Contagem de ideias únicas: soma entradas únicas com base no identificador para obter o total de novas ideias.
• Divulgação no Slack: envia uma mensagem para o canal especificado com o total de novas ideias UX.
- **Ferramentas:** • Notion: base de dados de ideias de UX de onde são carregadas as novas entradas.
• Slack: canal onde é postado o resumo semanal de novas ideias UX.

## Fluxo visual

```mermaid
flowchart LR
    N1["Schedule Trigger"]
    N2["Notion"]
    N3["Slack"]
    N4["Item Lists"]
    N5["Sticky Note"]
    N6["Sticky Note2"]
    N7["Sticky Note1"]
    N8["Sticky Note3"]
    N9["Sticky Note8"]
    N10["Filter"]
    N11["Code"]

    N11 --> N10
    N10 --> N4
    N2 --> N10
    N4 --> N3
    N1 --> N11
    N1 --> N2
```

## Fluxo (.json) :

```json
{
  "nodes": [
    {
      "id": "5eeb368d-737a-4186-afef-3072d0e9a1c7",
      "name": "Schedule Trigger",
      "type": "n8n-nodes-base.scheduleTrigger",
      "notes": "Execute WF on a schedule",
      "position": [
        940,
        280
      ],
      "parameters": {
        "rule": {
          "interval": [
            {}
          ]
        }
      },
      "notesInFlow": true,
      "typeVersion": 1.1
    },
    {
      "id": "175f3ae0-6710-4934-b6c0-ebc21e26d0b5",
      "name": "Notion",
      "type": "n8n-nodes-base.notion",
      "disabled": true,
      "position": [
        1220,
        80
      ],
      "parameters": {
        "filters": {
          "conditions": [
            {
              "key": "Created time|created_time",
              "condition": "on_or_after",
              "createdTimeValue": "={{ $now.minus(7, 'days').toISOString() }}"
            }
          ]
        },
        "options": {},
        "resource": "databasePage",
        "matchType": "allFilters",
        "operation": "getAll",
        "databaseId": {
          "__rl": true,
          "mode": "list",
          "value": "4ab15dec-f104-488e-936b-d14122106e7f",
          "cachedResultUrl": "https://www.notion.so/4ab15decf104488e936bd14122106e7f",
          "cachedResultName": "Product ideas list"
        },
        "filterType": "manual"
      },
      "credentials": {
        "notionApi": {
          "id": "5",
          "name": "Notion account"
        }
      },
      "typeVersion": 2
    },
    {
      "id": "8210582d-aae4-42b4-86d1-0513ad987c55",
      "name": "Slack",
      "type": "n8n-nodes-base.slack",
      "notes": "Post message in channel",
      "position": [
        2100,
        280
      ],
      "parameters": {
        "text": "=Yay, we added *{{ $json.unique_count_id }} new UX ideas* in the last 7 days :tada:",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "mode": "name",
          "value": "#nik-wf-testing"
        },
        "otherOptions": {}
      },
      "credentials": {
        "slackApi": {
          "id": "6",
          "name": "Idea Bot"
        }
      },
      "notesInFlow": true,
      "typeVersion": 2
    },
    {
      "id": "7db1f3c1-d1c9-4f41-a873-0f083543b4b4",
      "name": "Item Lists",
      "type": "n8n-nodes-base.itemLists",
      "position": [
        1800,
        280
      ],
      "parameters": {
        "options": {},
        "operation": "summarize",
        "fieldsToSummarize": {
          "values": [
            {
              "field": "id",
              "aggregation": "countUnique"
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "f6856a5e-d57d-43f4-986b-cd8439e4caa0",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        400,
        80
      ],
      "parameters": {
        "width": 424,
        "height": 515.6050016413932,
        "content": "## 👋 How to use this template\nThis template shows how you can create reports on data in an app and share a summary in another app. Here's how to use it:\n\n1. Double click the `Slack` node and create a credential by signing in.\n2. Change the channel name in the `Slack` node to a channel you have in Slack.\n2. Click the `Execute Workflow` button and double click the nodes to see the input and output data\n\n### To customize it to you needs, just do the following:\n1. Enable or exchange the `Notion` node with any service that fits your use case.\n2. Change the `2. Filter and transform your data` section to fit your needs\n3. Adjust the Slack node or exchange it with any node that fits your use case\n4. Disable or remove the `Mock Data` node\n"
      },
      "typeVersion": 1
    },
    {
      "id": "13386afe-01c2-4f6e-b9d5-8fc485353ff9",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2040,
        220
      ],
      "parameters": {
        "width": 317.52886836027733,
        "height": 373.04798303066787,
        "content": "### 3. Notify the right channel\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nFinally, we're sending a message to the `#ideas-overview` channel in Slack.\n\n**You can replace this node with any service like [Teams](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftteams/?utm_source=n8n_app&utm_medium=node_settings_modal-credential_link&utm_campaign=n8n-nodes-base.microsoftTeams), [Telegram](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/?utm_source=n8n_app&utm_medium=node_settings_modal-credential_link&utm_campaign=n8n-nodes-base.telegram), [Email](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sendemail/?utm_source=n8n_app&utm_medium=node_settings_modal-credential_link&utm_campaign=n8n-nodes-base.emailSend) etc.**"
      },
      "typeVersion": 1
    },
    {
      "id": "1b4108e0-9e91-4b4e-a4cf-75366d7c82c0",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        860,
        180
      ],
      "parameters": {
        "width": 282,
        "height": 415.1692017070486,
        "content": "### 1. Define a trigger that should start your wofklow\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWe added a `Schedule trigger` that starts the workflow once a week. \n\n**Double click the node to modify when it runs**"
      },
      "typeVersion": 1
    },
    {
      "id": "ba3eb63f-bdcd-4a58-949a-2d24d4c872c4",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1160,
        0
      ],
      "parameters": {
        "width": 348,
        "height": 597.3550016413941,
        "content": "### 2. Load your data\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nIn our example, we're getting all new entries from a `Notion` Database in which we save new product ideas.\n\n**You can replace product ideas with any data that you want to summarize any service you wish, like [Jira](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.jira/?utm_source=n8n_app&utm_medium=node_settings_modal-credential_link&utm_campaign=n8n-nodes-base.jira), [Airtable](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtable/?utm_source=n8n_app&utm_medium=node_settings_modal-credential_link&utm_campaign=n8n-nodes-base.airtable), [Google Sheets](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/?utm_source=n8n_app&utm_medium=node_settings_modal-credential_link&utm_campaign=n8n-nodes-base.googleSheets) etc.**"
      },
      "typeVersion": 1
    },
    {
      "id": "9ec65fe7-3264-4437-a1bf-3bdec1c886fe",
      "name": "Sticky Note8",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1540,
        160
      ],
      "parameters": {
        "width": 462,
        "height": 444.12384956830226,
        "content": "### 2. Filter and transform your data\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWe only want to count the UX ideas of the team. We use the `Filter` node to filter out all other items, and use the `Item Lists` node to summarize the data for us.\n\nTo edit the nodes, simply drag and drop input data into the fields or change the values directly. **n8n comes with a set of powerful transformation and branching tools like [Set](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.set/?utm_source=n8n_app&utm_medium=node_settings_modal-credential_link&utm_campaign=n8n-nodes-base.set), [ItemList](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.itemlists/?utm_source=n8n_app&utm_medium=node_settings_modal-credential_link&utm_campaign=n8n-nodes-base.itemLists), [Code](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.code/?utm_source=n8n_app&utm_medium=node_settings_modal-credential_link&utm_campaign=n8n-nodes-base.code), [If](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.if/?utm_source=n8n_app&utm_medium=node_settings_modal-credential_link&utm_campaign=n8n-nodes-base.if)  and many more.**"
      },
      "typeVersion": 1
    },
    {
      "id": "5597d8bb-ae15-4ea0-be16-531d8a8f7018",
      "name": "Filter",
      "type": "n8n-nodes-base.filter",
      "notes": "Only keep UX ideas",
      "position": [
        1600,
        280
      ],
      "parameters": {
        "conditions": {
          "boolean": [
            {
              "value1": "={{ $json.property_type.includes(\"UX\") }}",
              "value2": true
            }
          ]
        }
      },
      "notesInFlow": true,
      "typeVersion": 1
    },
    {
      "id": "e4a13d15-368f-42a5-b23a-736883e7c1aa",
      "name": "Code",
      "type": "n8n-nodes-base.code",
      "notes": "Mock Data",
      "position": [
        1220,
        280
      ],
      "parameters": {
        "jsCode": "return [\n  {\n    \"id\": \"32cb4a89-7735-497d-8862-fc66cb6383f2\",\n    \"name\": \"Promote credential test result to NDV, + run on NDV first open\",\n    \"url\": \"https://www.notion.so/Promote-credential-test-result-to-NDV-run-on-NDV-first-open-32cb4a897735497d8862fc66cb6383f2\",\n    \"property_tags\": [],\n    \"property_priority\": null,\n    \"property_type\": [\n      \"UX\",\n      \"Pain\",\n      \"UI\"\n    ],\n    \"property_deletion_time\": null,\n    \"property_complexity\": null,\n    \"property_area\": [\n      \"Credentials\",\n      \"Nodes\",\n      \"Node details view\"\n    ],\n    \"property_votes\": 2,\n    \"property_sync_time\": null,\n    \"property_consider_soon\": false,\n    \"property_last_edited\": \"2023-06-23T13:37:00.000Z\",\n    \"property_property\": \"\",\n    \"property_created_time\": \"2023-06-23T12:48:00.000Z\",\n    \"property_nodes_affected\": [],\n    \"property_linear_ticket\": null,\n    \"property_external_request_link\": null,\n    \"property_voters\": [\n      \"max@n8n.io\",\n      \"jon@n8n.io\"\n    ],\n    \"property_published_time\": {\n      \"start\": \"2023-06-23T15:37:00.000+02:00\",\n      \"end\": null,\n      \"time_zone\": null\n    },\n    \"property_created_by\": [\n      \"max@n8n.io\"\n    ],\n    \"property_sub_area\": [],\n    \"property_impact\": null,\n    \"property_metric_to_improve\": [],\n    \"property_status\": null,\n    \"property_name\": \"Promote credential test result to NDV, + run on NDV first open\",\n    \"property_implementation_phase\": null,\n    \"property_timeline_status\": null\n  },\n  {\n    \"id\": \"c2ab7fe1-c7ff-4cf0-881d-a039ec90306e\",\n    \"name\": \"Add “Duplicate sticky” action\",\n    \"url\": \"https://www.notion.so/Add-Duplicate-sticky-action-c2ab7fe1c7ff4cf0881da039ec90306e\",\n    \"property_tags\": [],\n    \"property_priority\": null,\n    \"property_type\": [\n      \"Tweak\",\n      \"UX\"\n    ],\n    \"property_deletion_time\": null,\n    \"property_complexity\": null,\n    \"property_area\": [\n      \"Canvas\",\n      \"Stickies\"\n    ],\n    \"property_votes\": 3,\n    \"property_sync_time\": null,\n    \"property_consider_soon\": false,\n    \"property_last_edited\": \"2023-06-23T14:15:00.000Z\",\n    \"property_property\": \"\",\n    \"property_created_time\": \"2023-06-23T11:46:00.000Z\",\n    \"property_nodes_affected\": [],\n    \"property_linear_ticket\": null,\n    \"property_external_request_link\": null,\n    \"property_voters\": [\n      \"max@n8n.io\",\n      \"jon@n8n.io\",\n      \"giulio@n8n.io\"\n    ],\n    \"property_published_time\": {\n      \"start\": \"2023-06-23T14:37:00.000+02:00\",\n      \"end\": null,\n      \"time_zone\": null\n    },\n    \"property_created_by\": [\n      \"max@n8n.io\"\n    ],\n    \"property_sub_area\": [],\n    \"property_impact\": null,\n    \"property_metric_to_improve\": [],\n    \"property_status\": null,\n    \"property_name\": \"Add “Duplicate sticky” action\",\n    \"property_implementation_phase\": null,\n    \"property_timeline_status\": null\n  },\n  {\n    \"id\": \"b3e99a3a-451b-4290-9a2b-5121755709d9\",\n    \"name\": \"Show “last used” (MVP: created) in cred dropdown; and sort by it\",\n    \"url\": \"https://www.notion.so/Show-last-used-MVP-created-in-cred-dropdown-and-sort-by-it-b3e99a3a451b42909a2b5121755709d9\",\n    \"property_tags\": [],\n    \"property_priority\": null,\n    \"property_type\": [\n      \"Tweak\"\n    ],\n    \"property_deletion_time\": null,\n    \"property_complexity\": null,\n    \"property_area\": [\n      \"Nodes\",\n      \"Credentials\"\n    ],\n    \"property_votes\": 2,\n    \"property_sync_time\": null,\n    \"property_consider_soon\": false,\n    \"property_last_edited\": \"2023-06-22T14:37:00.000Z\",\n    \"property_property\": \"\",\n    \"property_created_time\": \"2023-06-22T14:28:00.000Z\",\n    \"property_nodes_affected\": [],\n    \"property_linear_ticket\": null,\n    \"property_external_request_link\": null,\n    \"property_voters\": [\n      \"max@n8n.io\",\n      \"jon@n8n.io\"\n    ],\n    \"property_published_time\": {\n      \"start\": \"2023-06-22T16:37:00.000+02:00\",\n      \"end\": null,\n      \"time_zone\": null\n    },\n    \"property_created_by\": [\n      \"max@n8n.io\"\n    ],\n    \"property_sub_area\": [],\n    \"property_impact\": null,\n    \"property_metric_to_improve\": [],\n    \"property_status\": null,\n    \"property_name\": \"Show “last used” (MVP: created) in cred dropdown; and sort by it\",\n    \"property_implementation_phase\": null,\n    \"property_timeline_status\": null\n  },\n  {\n    \"id\": \"a26efc3e-67fe-46d5-8d75-40f125a16e39\",\n    \"name\": \"Improve naming of Google Sheets actions (use “row” consistently)\",\n    \"url\": \"https://www.notion.so/Improve-naming-of-Google-Sheets-actions-use-row-consistently-a26efc3e67fe46d58d7540f125a16e39\",\n    \"property_tags\": [],\n    \"property_priority\": null,\n    \"property_type\": [\n      \"Tweak\",\n      \"UX\"\n    ],\n    \"property_deletion_time\": null,\n    \"property_complexity\": null,\n    \"property_area\": [\n      \"Nodes\"\n    ],\n    \"property_votes\": 1,\n    \"property_sync_time\": null,\n    \"property_consider_soon\": false,\n    \"property_last_edited\": \"2023-06-22T14:37:00.000Z\",\n    \"property_property\": \"\",\n    \"property_created_time\": \"2023-06-22T14:21:00.000Z\",\n    \"property_nodes_affected\": [\n      \"n8n-nodes-base.googleSheets\"\n    ],\n    \"property_linear_ticket\": null,\n    \"property_external_request_link\": null,\n    \"property_voters\": [\n      \"max@n8n.io\"\n    ],\n    \"property_published_time\": {\n      \"start\": \"2023-06-22T16:37:00.000+02:00\",\n      \"end\": null,\n      \"time_zone\": null\n    },\n    \"property_created_by\": [\n      \"max@n8n.io\"\n    ],\n    \"property_sub_area\": [],\n    \"property_impact\": null,\n    \"property_metric_to_improve\": [],\n    \"property_status\": null,\n    \"property_name\": \"Improve naming of Google Sheets actions (use “row” consistently)\",\n    \"property_implementation_phase\": null,\n    \"property_timeline_status\": null\n  },\n  {\n    \"id\": \"a4c72db2-1c0e-45a5-934a-eed187137bc0\",\n    \"name\": \"Change Notion trigger event “Page updated in database” to convey that it also fires for page creation\",\n    \"url\": \"https://www.notion.so/Change-Notion-trigger-event-Page-updated-in-database-to-convey-that-it-also-fires-for-page-creatio-a4c72db21c0e45a5934aeed187137bc0\",\n    \"property_tags\": [],\n    \"property_priority\": null,\n    \"property_type\": [\n      \"Tweak\"\n    ],\n    \"property_deletion_time\": null,\n    \"property_complexity\": null,\n    \"property_area\": [\n      \"Nodes\"\n    ],\n    \"property_votes\": 2,\n    \"property_sync_time\": null,\n    \"property_consider_soon\": false,\n    \"property_last_edited\": \"2023-06-22T14:37:00.000Z\",\n    \"property_property\": \"\",\n    \"property_created_time\": \"2023-06-22T14:16:00.000Z\",\n    \"property_nodes_affected\": [\n      \"n8n-nodes-base.notionTrigger\"\n    ],\n    \"property_linear_ticket\": null,\n    \"property_external_request_link\": null,\n    \"property_voters\": [\n      \"max@n8n.io\",\n      \"jon@n8n.io\"\n    ],\n    \"property_published_time\": {\n      \"start\": \"2023-06-22T16:37:00.000+02:00\",\n      \"end\": null,\n      \"time_zone\": null\n    },\n    \"property_created_by\": [\n      \"max@n8n.io\"\n    ],\n    \"property_sub_area\": [],\n    \"property_impact\": null,\n    \"property_metric_to_improve\": [],\n    \"property_status\": null,\n    \"property_name\": \"Change Notion trigger event “Page updated in database” to convey that it also fires for page creation\",\n    \"property_implementation_phase\": null,\n    \"property_timeline_status\": null\n  },\n  {\n    \"id\": \"9cdaca54-eacb-4623-99e4-09e3957a75df\",\n    \"name\": \"Improve “no credential set” error in Google Sheets node\",\n    \"url\": \"https://www.notion.so/Improve-no-credential-set-error-in-Google-Sheets-node-9cdaca54eacb462399e409e3957a75df\",\n    \"property_tags\": [],\n    \"property_priority\": null,\n    \"property_type\": [\n      \"UX\",\n      \"Tweak\"\n    ],\n    \"property_deletion_time\": null,\n    \"property_complexity\": null,\n    \"property_area\": [\n      \"Nodes\",\n      \"Credentials\",\n      \"Error handling\"\n    ],\n    \"property_votes\": 1,\n    \"property_sync_time\": null,\n    \"property_consider_soon\": false,\n    \"property_last_edited\": \"2023-06-21T14:37:00.000Z\",\n    \"property_property\": \"\",\n    \"property_created_time\": \"2023-06-21T13:48:00.000Z\",\n    \"property_nodes_affected\": [\n      \"n8n-nodes-base.googleSheets\"\n    ],\n    \"property_linear_ticket\": null,\n    \"property_external_request_link\": null,\n    \"property_voters\": [\n      \"max@n8n.io\"\n    ],\n    \"property_published_time\": {\n      \"start\": \"2023-06-21T16:37:00.000+02:00\",\n      \"end\": null,\n      \"time_zone\": null\n    },\n    \"property_created_by\": [\n      \"max@n8n.io\"\n    ],\n    \"property_sub_area\": [],\n    \"property_impact\": null,\n    \"property_metric_to_improve\": [],\n    \"property_status\": null,\n    \"property_name\": \"Improve “no credential set” error in Google Sheets node\",\n    \"property_implementation_phase\": null,\n    \"property_timeline_status\": null\n  },\n  {\n    \"id\": \"dda6acab-2160-4570-b110-4f06e126af19\",\n    \"name\": \"Promote new features in docs\",\n    \"url\": \"https://www.notion.so/Promote-new-features-in-docs-dda6acab21604570b1104f06e126af19\",\n    \"property_tags\": [],\n    \"property_priority\": null,\n    \"property_type\": [\n      \"Growth\",\n      \"Monetization\"\n    ],\n    \"property_deletion_time\": null,\n    \"property_complexity\": null,\n    \"property_area\": [\n      \"Other\"\n    ],\n    \"property_votes\": 2,\n    \"property_sync_time\": null,\n    \"property_consider_soon\": false,\n    \"property_last_edited\": \"2023-06-21T09:38:00.000Z\",\n    \"property_property\": \"\",\n    \"property_created_time\": \"2023-06-21T09:03:00.000Z\",\n    \"property_nodes_affected\": [],\n    \"property_linear_ticket\": null,\n    \"property_external_request_link\": null,\n    \"property_voters\": [\n      \"max@n8n.io\",\n      \"jon@n8n.io\"\n    ],\n    \"property_published_time\": {\n      \"start\": \"2023-06-21T11:37:00.000+02:00\",\n      \"end\": null,\n      \"time_zone\": null\n    },\n    \"property_created_by\": [\n      \"max@n8n.io\"\n    ],\n    \"property_sub_area\": [],\n    \"property_impact\": null,\n    \"property_metric_to_improve\": [],\n    \"property_status\": null,\n    \"property_name\": \"Promote new features in docs\",\n    \"property_implementation_phase\": null,\n    \"property_timeline_status\": null\n  }\n]"
      },
      "notesInFlow": true,
      "typeVersion": 1
    }
  ],
  "connections": {
    "Code": {
      "main": [
        [
          {
            "node": "Filter",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Filter": {
      "main": [
        [
          {
            "node": "Item Lists",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Notion": {
      "main": [
        [
          {
            "node": "Filter",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Item Lists": {
      "main": [
        [
          {
            "node": "Slack",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Schedule Trigger": {
      "main": [
        [
          {
            "node": "Code",
            "type": "main",
            "index": 0
          },
          {
            "node": "Notion",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-908"></a>

## Template 908 - Chatbot AI para páginas do Confluence

- **Nome:** Chatbot AI para páginas do Confluence
- **Descrição:** Chatbot que responde a perguntas de usuários usando o conteúdo de páginas do Confluence como contexto, retornando respostas via Telegram.
- **Funcionalidade:** • Acionador de mensagens de chat: Inicia o fluxo quando uma mensagem de chat é recebida.
• Uso de variáveis globais de páginas: Mantém IDs de páginas predefinidos para consultas rápidas.
• Busca de página por ID: Pesquisa e recupera metadados da página usando o ID fornecido.
• Recuperação do corpo da página em formato storage: Obtém o conteúdo da página no formato de armazenamento do Confluence.
• Conversão de HTML para Markdown: Converte o conteúdo da página para Markdown para facilitar o processamento pelo agente de IA.
• Agente de IA com contexto restrito: Gera respostas baseando-se exclusivamente no conteúdo da página; se a informação não estiver no contexto, responde "I don't know.".
• Memória de sessão em janela: Mantém um buffer de contexto por sessão para conversas contextuais.
• Formatação e envio da resposta: Estrutura a saída e envia a resposta final para um chat do Telegram.
- **Ferramentas:** • Confluence (Atlassian): Fonte de conteúdo; API usada para pesquisar páginas e recuperar o corpo das páginas.
• OpenAI (modelo gpt-4o-mini): Motor de IA responsável por gerar respostas a partir do contexto fornecido.
• Telegram: Canal de envio das respostas finais para o usuário via mensagem.

## Fluxo visual

```mermaid
flowchart LR
    N1["Sticky Note"]
    N2["Sticky Note2"]
    N3["Confluence Page Storage View"]
    N4["HTML to Markdown"]
    N5["gpt-4o-mini"]
    N6["When chat message received"]
    N7["Window Buffer Memory"]
    N8["Sticky Note3"]
    N9["Chat Response"]
    N10["Globals"]
    N11["Search By ID"]
    N12["Sticky Note4"]
    N13["Page Schema"]
    N14["AI Agent"]
    N15["Send Telegram Message"]
    N16["Split Out"]

    N10 --> N11
    N14 --> N9
    N14 --> N15
    N16 --> N13
    N13 --> N3
    N11 --> N16
    N4 --> N14
    N6 --> N10
    N3 --> N4
```

## Fluxo (.json) :

```json
{
  "id": "mOcaSIUAvpt3QjQ1",
  "meta": {
    "instanceId": "31e69f7f4a77bf465b805824e303232f0227212ae922d12133a0f96ffeab4fef",
    "templateCredsSetupCompleted": true
  },
  "name": "🌐 Confluence Page AI Powered Chatbot",
  "tags": [],
  "nodes": [
    {
      "id": "f4761e1a-6430-4b3d-97f9-b91743e02ea6",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        80,
        -340
      ],
      "parameters": {
        "color": 7,
        "width": 633,
        "height": 974,
        "content": "## Confluence\nhttps://developer.atlassian.com/cloud/confluence/basic-auth-for-rest-apis/\nhttps://id.atlassian.com/manage-profile/security/api-tokens\nhttps://developer.atlassian.com/cloud/confluence/rest/v2/intro/#about\n\nSupplying basic auth headers\nYou can construct and send basic auth headers yourself, including a base64-encoded string that contains your Atlassian account email and API token.\n\nTo use basic auth headers, perform the following steps:\n\nGenerate an API Token for your Atlassian Account: https://id.atlassian.com/manage/api-tokens\nBuild a string of the form your_email@domain.com:your_user_api_token.\nYou'll need to encode your authorization credentials to Base64 encoded. You can do this locally:\nLinux/Unix/MacOS:\n\nCopy\n```\necho -n your_email@domain.com:your_user_api_token | base64\n```\nWindows 7 and later, using Microsoft Powershell:\n\nCopy\n```\n$Text = ‘your_email@domain.com:your_user_api_token’\n$Bytes = [System.Text.Encoding]::UTF8.GetBytes($Text)\n$EncodedText = [Convert]::ToBase64String($Bytes)\n$EncodedText\n```\nSupply an Authorization header with content Basic followed by the encoded string. Example: Authorization: Basic eW91cl9lbWFpbEBkb21haW4uY29tOnlvdXJfdXNlcl9hcGlfdG9rZW4=\n\nCopy\n```\ncurl -D- \\\n   -X GET \\\n   -H \"Authorization: Basic <your_encoded_string>\" \\\n   -H \"Content-Type: application/json\" \\\n   \"https://<your-domain.atlassian.net>/wiki/rest/api/space\"\n```\n\nThe above cURL command will not work as shown. You need to replace <your_encoded_string> and <your-domain.atlassian.net> with your authorization credentials encoded string and instance information before running it in the terminal."
      },
      "typeVersion": 1
    },
    {
      "id": "b2865684-687e-45a9-bb0c-e78df4dda72e",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        760,
        -340
      ],
      "parameters": {
        "color": 5,
        "width": 768.3946456283678,
        "height": 381.59428876752247,
        "content": "## Using Rest API to GET Confluence Page Body\nhttps://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/#api-pages-id-get\n\nRequest\nhttps://<your-wiki>.atlassian.net/wiki/api/v2/pages/{id}\nPath parameters\nid\ninteger\n\nRequired\nQuery parameters\n\nThe content format types to be returned in the body field of the response. \nIf available, the representation will be available under a response field of the same name under the body field.\n\nValid values: storage, atlas_doc_format, view, export_view, anonymous_export_view, styled_view, editor\n\n"
      },
      "typeVersion": 1
    },
    {
      "id": "2fae2b02-b15f-4226-86c2-f4444f10965e",
      "name": "Confluence Page Storage View",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        900,
        580
      ],
      "parameters": {
        "url": "=https://example.atlassian.net/wiki/api/v2/pages/{{ $json.id }}",
        "options": {},
        "sendQuery": true,
        "sendHeaders": true,
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "queryParameters": {
          "parameters": [
            {
              "name": "body-format",
              "value": "storage"
            }
          ]
        },
        "headerParameters": {
          "parameters": [
            {}
          ]
        }
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "KafuDlwiWOVNQcyC",
          "name": "Confluence API"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "49c5c6f7-f879-4518-aeef-922154f47ea6",
      "name": "HTML to Markdown",
      "type": "n8n-nodes-base.markdown",
      "position": [
        1100,
        580
      ],
      "parameters": {
        "html": "={{ $json.body.storage.value }}",
        "options": {}
      },
      "typeVersion": 1
    },
    {
      "id": "6ef64460-1406-43c9-9c5b-9d8ae3f51d31",
      "name": "gpt-4o-mini",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        1260,
        760
      ],
      "parameters": {
        "options": {}
      },
      "credentials": {
        "openAiApi": {
          "id": "jEMSvKmtYfzAkhe6",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "b8f998da-34b2-40d4-9816-b7a3ca33a3d9",
      "name": "When chat message received",
      "type": "@n8n/n8n-nodes-langchain.manualChatTrigger",
      "position": [
        820,
        180
      ],
      "parameters": {},
      "typeVersion": 1.1
    },
    {
      "id": "8fcfb987-3ea1-43cd-804f-dc2d629e558e",
      "name": "Window Buffer Memory",
      "type": "@n8n/n8n-nodes-langchain.memoryBufferWindow",
      "position": [
        1400,
        760
      ],
      "parameters": {
        "sessionKey": "={{ $('When chat message received').item.json.sessionId }}",
        "sessionIdType": "customKey"
      },
      "typeVersion": 1.2
    },
    {
      "id": "53fe680c-af07-4712-b3cd-ae853f19cf8a",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        760,
        420
      ],
      "parameters": {
        "color": 6,
        "width": 1163,
        "height": 515,
        "content": "## Chatbot for Confluence Pages\n\n\n"
      },
      "typeVersion": 1
    },
    {
      "id": "f37546a9-1b33-4276-9ea3-e461b53fe70a",
      "name": "Chat Response",
      "type": "n8n-nodes-base.set",
      "position": [
        1700,
        680
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "636ec5bb-141c-491b-b827-bf6c3753a531",
              "name": "output",
              "type": "string",
              "value": "={{ $json.output }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "c53f59bd-f0d9-4629-bf56-ca439ef9c7f5",
      "name": "Globals",
      "type": "n8n-nodes-base.set",
      "position": [
        1100,
        180
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "74683edb-6368-4673-95f3-2885e30595cf",
              "name": "page_id_tekla",
              "type": "string",
              "value": "688157"
            },
            {
              "id": "3a8796d7-3426-4f4a-bddf-973720b59e9d",
              "name": "page_id_n8n",
              "type": "string",
              "value": "491546"
            },
            {
              "id": "42b27698-8d11-4fb0-a308-e256e0752f4d",
              "name": "page_id_more_n8n",
              "type": "string",
              "value": "983041"
            },
            {
              "id": "62572887-e17a-4957-9ab1-3546277f79ab",
              "name": "page_id_tekla_clash_checking",
              "type": "string",
              "value": "753691"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "ee500c5b-9289-4636-8178-6235c0fe4080",
      "name": "Search By ID",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1300,
        180
      ],
      "parameters": {
        "url": "=https://example.atlassian.net/wiki/rest/api/search?limit=1&cql=id={{ $json.page_id_n8n }}",
        "options": {},
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth"
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "KafuDlwiWOVNQcyC",
          "name": "Confluence API"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "934f0c57-6184-4c85-a0dc-097b3c470be4",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1020,
        80
      ],
      "parameters": {
        "width": 872,
        "height": 297,
        "content": "## Confluence Search By ID"
      },
      "typeVersion": 1
    },
    {
      "id": "c51b8421-962d-46a1-aaf5-1b170252b7da",
      "name": "Page Schema",
      "type": "n8n-nodes-base.set",
      "position": [
        1700,
        180
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "3e8b49af-f3c6-4441-842f-9ce9a42c34b6",
              "name": "content._links.webui",
              "type": "string",
              "value": "={{ $json.content._links.webui }}"
            },
            {
              "id": "6fd53eb3-52b2-4f7b-92ca-89a26e05d52a",
              "name": "content._links.self",
              "type": "string",
              "value": "={{ $json.content._links.self }}"
            },
            {
              "id": "dfc89cbb-2f63-41ca-acfb-27b4d36d0418",
              "name": "title",
              "type": "string",
              "value": "={{ $json.title }}"
            },
            {
              "id": "0e15af12-8ae2-4337-a174-f3c3592bd0c6",
              "name": "url",
              "type": "string",
              "value": "={{ $json.url }}"
            },
            {
              "id": "6bbfa6eb-d6db-42c4-9ef6-81611fda0365",
              "name": "excerpt",
              "type": "string",
              "value": "={{ $json.excerpt }}"
            },
            {
              "id": "a5a26e42-af66-41a6-9406-7ccb86fb3386",
              "name": "id",
              "type": "string",
              "value": "={{ $json.content.id }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "2c765cad-e488-44ad-98b6-6e0a2c575fd2",
      "name": "AI Agent",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        1300,
        580
      ],
      "parameters": {
        "text": "=Answer questions from user with the context provided.  Only respond using the context.  If you do not know the answer simply respond with \"I don't know.\"\n\nUser question: {{ $('When chat message received').item.json.chatInput }}\n\nContext: {{ $json.data }}",
        "agent": "conversationalAgent",
        "options": {},
        "promptType": "define"
      },
      "typeVersion": 1.6
    },
    {
      "id": "a89508f9-fd88-4a9f-84da-a0ddef590e1b",
      "name": "Send Telegram Message",
      "type": "n8n-nodes-base.telegram",
      "position": [
        1700,
        480
      ],
      "webhookId": "3ba1ee6d-1648-4421-823b-e68ae14d769b",
      "parameters": {
        "text": "={{ $json.output}}",
        "chatId": "={{ $env.TELEGRAM_CHAT_ID }}",
        "additionalFields": {
          "parse_mode": "HTML",
          "appendAttribution": false
        }
      },
      "credentials": {
        "telegramApi": {
          "id": "pAIFhguJlkO3c7aQ",
          "name": "Telegram account"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "dae8ae00-1552-4945-948e-2556dfdd8802",
      "name": "Split Out",
      "type": "n8n-nodes-base.splitOut",
      "position": [
        1500,
        180
      ],
      "parameters": {
        "options": {},
        "fieldToSplitOut": "results"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "d57c434b-ed09-484a-bcc4-d81681001a36",
  "connections": {
    "Globals": {
      "main": [
        [
          {
            "node": "Search By ID",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "AI Agent": {
      "main": [
        [
          {
            "node": "Chat Response",
            "type": "main",
            "index": 0
          },
          {
            "node": "Send Telegram Message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Split Out": {
      "main": [
        [
          {
            "node": "Page Schema",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Page Schema": {
      "main": [
        [
          {
            "node": "Confluence Page Storage View",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "gpt-4o-mini": {
      "ai_languageModel": [
        [
          {
            "node": "AI Agent",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Search By ID": {
      "main": [
        [
          {
            "node": "Split Out",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "HTML to Markdown": {
      "main": [
        [
          {
            "node": "AI Agent",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Window Buffer Memory": {
      "ai_memory": [
        [
          {
            "node": "AI Agent",
            "type": "ai_memory",
            "index": 0
          }
        ]
      ]
    },
    "When chat message received": {
      "main": [
        [
          {
            "node": "Globals",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Confluence Page Storage View": {
      "main": [
        [
          {
            "node": "HTML to Markdown",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-909"></a>

## Template 909 - Gmail para Notion: criação automática de páginas a partir de emails

- **Nome:** Gmail para Notion: criação automática de páginas a partir de emails
- **Descrição:** Fluxo que lê emails, gera tarefas via IA a partir do conteúdo e cria páginas no Notion associadas às rotas armazenadas, com rotulagem de mensagens e notificações de erro.
- **Funcionalidade:** • Detecção de novos emails: verifica a caixa de entrada e processa mensagens não marcadas.
• Extração de dados de rotas: identifica a rota correspondente a partir do alias no remetente.
• Geração de tarefa acionável: usa IA para criar um título, descrição e itens de apoio com base no conteúdo do email.
• Criação de página no Notion: constrói e publica uma página com conteúdo e blocos derivados do resumo e dos metadados.
• Controle de rotas e etiquetagem: marca mensagens como Processed e pode desativar rotas conforme a lógica do fluxo.
• Notificações de erro: envia alertas por email quando ocorre falta de rota ou falha no processamento.
- **Ferramentas:** • Gmail: serviço de email para receber mensagens, aplicar rótulos e enviar notificações.
• Airtable: base de dados para armazenar rotas, status e mapeamento de Notion Database.
• Notion: API para criar páginas e gerenciar conteúdo em databases.
• OpenAI: serviço de IA utilizado para sumarizar o conteúdo do email e gerar tarefas acionáveis.

## Fluxo visual

```mermaid
flowchart LR
    N1["OpenAI Chat Model"]
    N2["Calculator"]
    N3["Structured Output Parser"]
    N4["Add Label 'Processed'"]
    N5["Active Routes Only"]
    N6["Extract Route ID"]
    N7["Deactivate Route"]
    N8["Add Label 'Error'"]
    N9["Send notification about deactivated route"]
    N10["Send notification about missing route"]
    N11["Get Route by ID"]
    N12["Create Notion Page"]
    N13["Gmail Trigger"]
    N14["Filter for unprocessed mails"]
    N15["When clicking ‘Test workflow’"]
    N16["Required labels"]
    N17["Globals"]
    N18["Sticky Note"]
    N19["Sticky Note1"]
    N20["Sticky Note2"]
    N21["Sticky Note3"]
    N22["Sticky Note4"]
    N23["Sticky Note5"]
    N24["Sticky Note6"]
    N25["Sticky Note7"]
    N26["Sticky Note8"]
    N27["Sticky Note9"]
    N28["No Operation, do nothing"]
    N29["Sticky Note10"]
    N30["Sticky Note11"]
    N31["Sticky Note12"]
    N32["Format Notion Page Blocks"]
    N33["Get all labels"]
    N34["Structured Output Parser1"]
    N35["Calculator1"]
    N36["OpenAI Chat Model1"]
    N37["Generate Actionable Task"]
    N38["Get Summary & Meta Data"]

    N17 --> N14
    N13 --> N17
    N33 --> N16
    N11 --> N5
    N11 --> N28
    N7 --> N9
    N6 --> N11
    N5 --> N37
    N12 --> N4
    N12 --> N7
    N38 --> N32
    N37 --> N38
    N28 --> N10
    N32 --> N12
    N14 --> N6
    N15 --> N33
    N10 --> N8
    N9 --> N8
```

## Fluxo (.json) :

```json
{
  "id": "30r9acI1XVIIwAMi",
  "meta": {
    "instanceId": "378c072a34d9e63949fd9cf26b8d28ff276a486e303f0d8963f23e1d74169c1b",
    "templateCredsSetupCompleted": true
  },
  "name": "mails2notion V2",
  "tags": [],
  "nodes": [
    {
      "id": "3f649e97-e568-47ff-b175-bf63d859d95f",
      "name": "OpenAI Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        2560,
        240
      ],
      "parameters": {
        "model": "gpt-4o",
        "options": {
          "temperature": 0,
          "responseFormat": "json_object"
        }
      },
      "credentials": {
        "openAiApi": {
          "id": "mrgqM64cM1L88xC6",
          "name": "octionicsolutions@gmail.com"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "bd60c65f-ba6c-4dcb-8d09-b29f5dd475b7",
      "name": "Calculator",
      "type": "@n8n/n8n-nodes-langchain.toolCalculator",
      "disabled": true,
      "position": [
        2700,
        240
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "d052786a-92a0-4f9b-9867-2dd64ada8034",
      "name": "Structured Output Parser",
      "type": "@n8n/n8n-nodes-langchain.outputParserStructured",
      "position": [
        2820,
        240
      ],
      "parameters": {
        "jsonSchemaExample": "{\n  \"summary\": \"Text\",\n  \"meta\": {\n    \"sender\": \"Text\",\n    \"subject\": \"Text\",\n    \"date\": \"Text\"\n  }\n}"
      },
      "typeVersion": 1.2
    },
    {
      "id": "50d396fd-d3b0-4fea-99d7-18bd4773cb20",
      "name": "Add Label \"Processed\"",
      "type": "n8n-nodes-base.gmail",
      "position": [
        3860,
        20
      ],
      "parameters": {
        "labelIds": "={{ $('Globals').item.json.processedLabelID }}",
        "messageId": "={{ $('Gmail Trigger').item.json.id }}",
        "operation": "addLabels"
      },
      "credentials": {
        "gmailOAuth2": {
          "id": "9LLNsPzyDJlQFgdw",
          "name": "Gmail (mails2notion)"
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "8a4c49f9-0c14-46ea-a475-a0d83eb9d688",
      "name": "Active Routes Only",
      "type": "n8n-nodes-base.filter",
      "position": [
        2000,
        20
      ],
      "parameters": {
        "options": {},
        "conditions": {
          "options": {
            "leftValue": "",
            "caseSensitive": true,
            "typeValidation": "strict"
          },
          "combinator": "and",
          "conditions": [
            {
              "id": "02b11920-e737-46cc-b1b9-22ffaf7f3f64",
              "operator": {
                "type": "boolean",
                "operation": "true",
                "singleValue": true
              },
              "leftValue": "={{ $json.Active }}",
              "rightValue": ""
            }
          ]
        }
      },
      "typeVersion": 2
    },
    {
      "id": "fd0f902f-4d16-4bad-8ed0-7fe02e8e879b",
      "name": "Extract Route ID",
      "type": "n8n-nodes-base.set",
      "position": [
        1560,
        220
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "acfaf63a-74de-4018-ae30-671f209878ba",
              "name": "route",
              "type": "string",
              "value": "={{ $('Gmail Trigger').item.json.to.text.match(/\\+([^@]+)@/)[1] }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "81d1dec6-aacc-480d-8cb4-1832ff27de92",
      "name": "Deactivate Route",
      "type": "n8n-nodes-base.airtable",
      "position": [
        3420,
        220
      ],
      "parameters": {
        "base": {
          "__rl": true,
          "mode": "list",
          "value": "appuqZhHVVGAcMwoA",
          "cachedResultUrl": "https://airtable.com/appuqZhHVVGAcMwoA",
          "cachedResultName": "mails2notion"
        },
        "table": {
          "__rl": true,
          "mode": "list",
          "value": "tblWL6FqfLkLHmLEo",
          "cachedResultUrl": "https://airtable.com/appuqZhHVVGAcMwoA/tblWL6FqfLkLHmLEo",
          "cachedResultName": "Routes"
        },
        "columns": {
          "value": {
            "id": "={{ $('Get Route by ID').item.json.id }}",
            "Active": false
          },
          "schema": [
            {
              "id": "id",
              "type": "string",
              "display": true,
              "removed": false,
              "readOnly": true,
              "required": false,
              "displayName": "id",
              "defaultMatch": true
            },
            {
              "id": "Name",
              "type": "string",
              "display": true,
              "removed": true,
              "readOnly": false,
              "required": false,
              "displayName": "Name",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Token",
              "type": "string",
              "display": true,
              "removed": true,
              "readOnly": false,
              "required": false,
              "displayName": "Token",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "NotionDatabase",
              "type": "string",
              "display": true,
              "removed": true,
              "readOnly": false,
              "required": false,
              "displayName": "NotionDatabase",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Email Alias",
              "type": "string",
              "display": true,
              "removed": true,
              "readOnly": true,
              "required": false,
              "displayName": "Email Alias",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "User",
              "type": "array",
              "display": true,
              "removed": true,
              "readOnly": false,
              "required": false,
              "displayName": "User",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Active",
              "type": "boolean",
              "display": true,
              "removed": false,
              "readOnly": false,
              "required": false,
              "displayName": "Active",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Status",
              "type": "string",
              "display": true,
              "removed": true,
              "readOnly": true,
              "required": false,
              "displayName": "Status",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            }
          ],
          "mappingMode": "defineBelow",
          "matchingColumns": [
            "id"
          ]
        },
        "options": {},
        "operation": "update"
      },
      "credentials": {
        "airtableTokenApi": {
          "id": "kHzLZhbAFQ1CQnQz",
          "name": "Airtable (octionicsolutions)"
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "20242505-c57e-424c-a215-2b2effac1d94",
      "name": "Add Label \"Error\"",
      "type": "n8n-nodes-base.gmail",
      "position": [
        3860,
        220
      ],
      "parameters": {
        "labelIds": "={{ $('Globals').item.json.errorLabelID }}",
        "messageId": "={{ $('Gmail Trigger').item.json.id }}",
        "operation": "addLabels"
      },
      "credentials": {
        "gmailOAuth2": {
          "id": "9LLNsPzyDJlQFgdw",
          "name": "Gmail (mails2notion)"
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "7a788a4f-f0a8-4fe8-b21d-b114a65313b1",
      "name": "Send notification about deactivated route",
      "type": "n8n-nodes-base.gmail",
      "position": [
        3640,
        220
      ],
      "parameters": {
        "sendTo": "={{ $('Gmail Trigger').item.json.from.value[0].address }}",
        "message": "=An error happened while trying to create a Notion Page. It can have various reasons, including a temporary outage of the Notion API, missing permissions to the Notion Database or a wrong Notion Database URL.\n\nThe route has been deaktivated to prevent future errors.\n\nPlease double check your configuration and enable the route again.",
        "options": {
          "appendAttribution": false
        },
        "subject": "A route has been deactivated",
        "emailType": "text"
      },
      "credentials": {
        "gmailOAuth2": {
          "id": "9LLNsPzyDJlQFgdw",
          "name": "Gmail (mails2notion)"
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "5e7cc69c-8f58-4ac8-9263-1ad206609295",
      "name": "Send notification about missing route",
      "type": "n8n-nodes-base.gmail",
      "position": [
        3640,
        420
      ],
      "parameters": {
        "sendTo": "={{ $('Gmail Trigger').item.json.from.value[0].address }}",
        "message": "=There seems to be no active route anymore which connects this Alias to a Notion Database.\n\nPlease try again later or double check your configuration.",
        "options": {
          "appendAttribution": false
        },
        "subject": "Your Message could not be processed",
        "emailType": "text"
      },
      "credentials": {
        "gmailOAuth2": {
          "id": "9LLNsPzyDJlQFgdw",
          "name": "Gmail (mails2notion)"
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "7dd9646c-3172-4b53-82c8-4df7fd5f53ea",
      "name": "Get Route by ID",
      "type": "n8n-nodes-base.airtable",
      "onError": "continueErrorOutput",
      "position": [
        1780,
        220
      ],
      "parameters": {
        "id": "={{ $json.route }}",
        "base": {
          "__rl": true,
          "mode": "list",
          "value": "appuqZhHVVGAcMwoA",
          "cachedResultUrl": "https://airtable.com/appuqZhHVVGAcMwoA",
          "cachedResultName": "mails2notion"
        },
        "table": {
          "__rl": true,
          "mode": "list",
          "value": "tblWL6FqfLkLHmLEo",
          "cachedResultUrl": "https://airtable.com/appuqZhHVVGAcMwoA/tblWL6FqfLkLHmLEo",
          "cachedResultName": "Routes"
        },
        "options": {},
        "operation": "get"
      },
      "credentials": {
        "airtableTokenApi": {
          "id": "kHzLZhbAFQ1CQnQz",
          "name": "Airtable (octionicsolutions)"
        }
      },
      "retryOnFail": true,
      "typeVersion": 2.1,
      "waitBetweenTries": 5000
    },
    {
      "id": "8ddfe273-3fda-4b71-a972-5001d4fa71c1",
      "name": "Create Notion Page",
      "type": "n8n-nodes-base.httpRequest",
      "onError": "continueErrorOutput",
      "position": [
        3200,
        20
      ],
      "parameters": {
        "url": "https://api.notion.com/v1/pages",
        "method": "POST",
        "options": {},
        "jsonBody": "={{ $json.toJsonString() }}",
        "sendBody": true,
        "sendHeaders": true,
        "specifyBody": "json",
        "headerParameters": {
          "parameters": [
            {
              "name": "Authorization",
              "value": "=Bearer {{ $('Get Route by ID').item.json.Token }}"
            },
            {
              "name": "Notion-Version",
              "value": "2022-06-28"
            }
          ]
        }
      },
      "retryOnFail": true,
      "typeVersion": 4.2,
      "waitBetweenTries": 5000
    },
    {
      "id": "f773e41f-13b7-483a-9886-90a4425a7f6a",
      "name": "Gmail Trigger",
      "type": "n8n-nodes-base.gmailTrigger",
      "position": [
        900,
        220
      ],
      "parameters": {
        "simple": false,
        "filters": {
          "labelIds": "=INBOX"
        },
        "options": {},
        "pollTimes": {
          "item": [
            {
              "mode": "everyMinute"
            }
          ]
        }
      },
      "credentials": {
        "gmailOAuth2": {
          "id": "9LLNsPzyDJlQFgdw",
          "name": "Gmail (mails2notion)"
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "918ce27c-2886-4793-81f5-e459f3299bb1",
      "name": "Filter for unprocessed mails",
      "type": "n8n-nodes-base.filter",
      "position": [
        1340,
        220
      ],
      "parameters": {
        "options": {},
        "conditions": {
          "options": {
            "leftValue": "",
            "caseSensitive": true,
            "typeValidation": "strict"
          },
          "combinator": "and",
          "conditions": [
            {
              "id": "28879541-2e66-4a31-b25f-f0419ae45f47",
              "operator": {
                "type": "array",
                "operation": "notContains",
                "rightType": "any"
              },
              "leftValue": "={{ $('Gmail Trigger').item.json.labelIds }}",
              "rightValue": "={{ $json.errorLabelID }}"
            },
            {
              "id": "259a783f-5954-467b-ad52-c1e0072c2239",
              "operator": {
                "type": "array",
                "operation": "notContains",
                "rightType": "any"
              },
              "leftValue": "={{ $('Gmail Trigger').item.json.labelIds }}",
              "rightValue": "={{ $json.processedLabelID }}"
            },
            {
              "id": "81ef1ac2-449e-44c2-a94b-2fc9b08ec934",
              "operator": {
                "type": "string",
                "operation": "exists",
                "singleValue": true
              },
              "leftValue": "={{ $('Gmail Trigger').item.json.to.text.match(/\\+([^@]+)@/)[1] }}",
              "rightValue": ""
            }
          ]
        }
      },
      "typeVersion": 2
    },
    {
      "id": "14764527-ca40-4937-baa2-368b716c6f58",
      "name": "When clicking ‘Test workflow’",
      "type": "n8n-nodes-base.manualTrigger",
      "disabled": true,
      "position": [
        920,
        600
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "5f955606-4063-4683-b242-2fc0a4fbf34a",
      "name": "Required labels",
      "type": "n8n-nodes-base.filter",
      "position": [
        1360,
        600
      ],
      "parameters": {
        "options": {},
        "conditions": {
          "options": {
            "leftValue": "",
            "caseSensitive": true,
            "typeValidation": "strict"
          },
          "combinator": "or",
          "conditions": [
            {
              "id": "9bb51a86-76d3-42f7-8362-1931244f8cd9",
              "operator": {
                "type": "string",
                "operation": "contains"
              },
              "leftValue": "={{ $json.name }}",
              "rightValue": "Error"
            },
            {
              "id": "28b3afb4-d727-4306-9e45-321c9bd688e3",
              "operator": {
                "type": "string",
                "operation": "contains"
              },
              "leftValue": "={{ $json.name }}",
              "rightValue": "Processed"
            }
          ]
        }
      },
      "typeVersion": 2
    },
    {
      "id": "697198d3-2fc2-4665-86a8-4bc16dbc3d43",
      "name": "Globals",
      "type": "n8n-nodes-base.set",
      "position": [
        1120,
        220
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "0dcfba61-ddb5-425d-a803-f88cf36d81d9",
              "name": "errorLabelID",
              "type": "string",
              "value": "Label_4248329647975725750"
            },
            {
              "id": "b1505eaa-1d7e-49d7-be2e-cd71f5ec2632",
              "name": "processedLabelID",
              "type": "string",
              "value": "Label_6498950601707174088"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "b7efe665-97d8-4a82-a3f5-e15bffd68752",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        840,
        420
      ],
      "parameters": {
        "color": 5,
        "width": 742.4418604651174,
        "height": 361.9189248985609,
        "content": "## Setup\n- Disable the Gmail Trigger and enable the manual trigger here\n- Execute the workflow once\n- Copy the Gmail Label IDs from the output of the \"Required labels\" node to the \"Globals\" node\n- Disable the manual trigger here and and enable the Gmail Trigger again\n- Activate the workflow, so it runs automatically in the background\n"
      },
      "typeVersion": 1
    },
    {
      "id": "3d035d35-3760-4393-8796-cb713338c9d7",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1060,
        60
      ],
      "parameters": {
        "width": 215.20930232558143,
        "height": 323.99999999999943,
        "content": "## Set Globals\nUse the setup instructions below to retrieve the values for both `errorLabelID` and `processedLabelID`"
      },
      "typeVersion": 1
    },
    {
      "id": "b420310e-c0d5-4168-94ad-4c5973dfb3ab",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1720,
        60
      ],
      "parameters": {
        "width": 215.49263552738452,
        "height": 324.4244486294891,
        "content": "## Select Base\nSelect the database and the table where the \"Routes\" are defined"
      },
      "typeVersion": 1
    },
    {
      "id": "c917a3cb-d745-4f37-bd8f-0350c5aef473",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        840,
        140
      ],
      "parameters": {
        "color": 7,
        "width": 216.47293010628914,
        "height": 245.005504426549,
        "content": "The Gmail inbox is checked every minute for new entries"
      },
      "typeVersion": 1
    },
    {
      "id": "9298ad5b-ae09-44c6-8da4-2d2bd473c3ea",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1500,
        140
      ],
      "parameters": {
        "color": 7,
        "width": 216.47293010628914,
        "height": 245.005504426549,
        "content": "Extract the Airtable Row ID from the Email address"
      },
      "typeVersion": 1
    },
    {
      "id": "654bbfbe-3e0f-40e0-a686-5081069d825e",
      "name": "Sticky Note5",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1280,
        140
      ],
      "parameters": {
        "color": 7,
        "width": 216.47293010628914,
        "height": 245.005504426549,
        "content": "Filter by labels to prohibit double-processing"
      },
      "typeVersion": 1
    },
    {
      "id": "31ade897-22de-4b39-8f96-37bc7b274bfb",
      "name": "Sticky Note6",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2920,
        -120
      ],
      "parameters": {
        "color": 7,
        "width": 216.47293010628914,
        "height": 305.2192252594149,
        "content": "Dynamically build request body for Notion, since dynamic auth, and content with optional fields require a custom request"
      },
      "typeVersion": 1
    },
    {
      "id": "26cf52ea-01d1-48ed-9d3d-71e4ff01983f",
      "name": "Sticky Note7",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        3140,
        -120
      ],
      "parameters": {
        "color": 7,
        "width": 216.47293010628914,
        "height": 304.5973623748489,
        "content": "The custom built request including the user specific authentication is sent to Notion to create a new Page inside of a database"
      },
      "typeVersion": 1
    },
    {
      "id": "d765c84d-9e15-44c8-b975-2c366c315bfe",
      "name": "Sticky Note8",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2160,
        -160
      ],
      "parameters": {
        "color": 7,
        "width": 755.8332895195936,
        "height": 529.1698390841688,
        "content": "The Email is processed in multiple ways:\n- An actionable task is being generated based on the content, consisting of a short title, a short description and optionally a few details as bullet points\n- A detailed Email summary is being generated\n- Meta data is being extracted - so the user has a reference to find the original Email again\n- To get more stable results, the tasks are devided between two Agents"
      },
      "typeVersion": 1
    },
    {
      "id": "0103f8bc-2a43-455a-88da-b7317821f0b3",
      "name": "Sticky Note9",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1940,
        -80
      ],
      "parameters": {
        "color": 7,
        "width": 216.47293010628914,
        "height": 249.09934448053562,
        "content": "Skip disabled routes (determined by a checkbox attribute in Airtable)"
      },
      "typeVersion": 1
    },
    {
      "id": "1d2fe867-f3d1-4702-b35e-f730f20b7251",
      "name": "No Operation, do nothing",
      "type": "n8n-nodes-base.noOp",
      "position": [
        2000,
        420
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "758d1797-0e6c-40de-a6a4-e16f8350674c",
      "name": "Sticky Note10",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        3580,
        100
      ],
      "parameters": {
        "color": 7,
        "width": 216.47293010628914,
        "height": 503.00412949500975,
        "content": "Send custom Email notifications back to sender, containing an error message and suggestions to fix it"
      },
      "typeVersion": 1
    },
    {
      "id": "56522a6d-c961-48a5-a5ef-33df96d77a22",
      "name": "Sticky Note11",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        3800,
        -60
      ],
      "parameters": {
        "color": 7,
        "width": 216.47293010628914,
        "height": 446.3164817463921,
        "content": "Add labels which prevent from double-processing"
      },
      "typeVersion": 1
    },
    {
      "id": "5b81389b-49a6-4849-becf-35c4e680b734",
      "name": "Sticky Note12",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        3360,
        120
      ],
      "parameters": {
        "color": 7,
        "width": 216.47293010628914,
        "height": 261.3816681594028,
        "content": "Disable a checkbox attribute in Airtable which determines if a route is active"
      },
      "typeVersion": 1
    },
    {
      "id": "6558328c-30cf-4f37-a0cb-d5f9f6efa7b2",
      "name": "Format Notion Page Blocks",
      "type": "n8n-nodes-base.code",
      "position": [
        2980,
        20
      ],
      "parameters": {
        "mode": "runOnceForEachItem",
        "jsCode": "function paragraph(content, annotations={}) {\n  return {\n    \"object\": \"block\",\n    \"type\": \"paragraph\",\n    \"paragraph\": {\n      \"rich_text\": [\n        {\n          \"type\": \"text\",\n          \"text\": {\n            \"content\": content\n          },\n          \"annotations\": annotations\n        }\n      ]\n    }\n  };\n}\nfunction bulletPoint(content) {\n  return {\n    \"object\": \"block\",\n    \"type\": \"bulleted_list_item\",\n    \"bulleted_list_item\": {\n      \"rich_text\": [\n        {\n          \"type\": \"text\",\n          \"text\": {\n            \"content\": content\n          }\n        }\n      ]\n    }\n  };\n}\n\n// combine AI generated content\nconst content = Object.assign({}, $('Generate Actionable Task').item.json.output, $('Get Summary & Meta Data').item.json.output);\n\nblocks = [];\n\n// append task description\nblocks.push(paragraph(content.description));\n\nif (content.bulletpoints) {\n  for (let bulletpoint of content.bulletpoints) {\n    blocks.push(bulletPoint(bulletpoint));\n  }\n}\n\n// append empty line\nblocks.push(paragraph(\"\"));\n\n// append devider\nblocks.push({\n  \"object\": \"block\",\n  \"type\": \"divider\",\n  \"divider\": {}\n});\n\n// append summary & meta data\nblocks.push(paragraph(\"Email summary:\"));\nblocks.push(paragraph(content.summary));\nblocks.push(paragraph(\"\"));\nblocks.push(paragraph(content.meta.sender + \"\\n\" + content.meta.subject + \"\\n\" + content.meta.date, {\"italic\": true}));\n\n// build final object\noutput = {\n  \"parent\": {\n    \"database_id\": $('Get Route by ID').item.json.NotionDatabase.match(/https://www\\.notion\\.so/[a-zA-Z0-9-]+/([a-zA-Z0-9]{32})/)[1]\n  },\n  \"properties\": {\n    \"Name\": {\n      \"title\": [\n        {\n          \"text\": {\n            \"content\": content.title\n          }\n        }\n      ]\n    }\n  },\n  \"children\": blocks\n};\n\nreturn { json: output };"
      },
      "typeVersion": 2
    },
    {
      "id": "133e3498-10ce-4a08-aa50-3c7d56f1b9c8",
      "name": "Get all labels",
      "type": "n8n-nodes-base.gmail",
      "position": [
        1140,
        600
      ],
      "parameters": {
        "resource": "label",
        "returnAll": true
      },
      "credentials": {
        "gmailOAuth2": {
          "id": "9LLNsPzyDJlQFgdw",
          "name": "Gmail (mails2notion)"
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "f68e66e1-9f84-498a-bfc4-f7c5b2ca42b1",
      "name": "Structured Output Parser1",
      "type": "@n8n/n8n-nodes-langchain.outputParserStructured",
      "position": [
        2440,
        240
      ],
      "parameters": {
        "jsonSchemaExample": "{\n  \"title\": \"Title\",\n  \"description\": \"Text\",\n  \"bulletpoints\": [\n    \"Text\",\n    \"Text\"\n  ]\n}"
      },
      "typeVersion": 1.2
    },
    {
      "id": "c55a3e9b-5637-4775-a0a6-ea11f1bd26a7",
      "name": "Calculator1",
      "type": "@n8n/n8n-nodes-langchain.toolCalculator",
      "disabled": true,
      "position": [
        2320,
        240
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "4d4f7b04-5431-47d2-b9b1-ee2c516e729c",
      "name": "OpenAI Chat Model1",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        2180,
        240
      ],
      "parameters": {
        "model": "gpt-4o",
        "options": {
          "temperature": 0,
          "responseFormat": "json_object"
        }
      },
      "credentials": {
        "openAiApi": {
          "id": "mrgqM64cM1L88xC6",
          "name": "octionicsolutions@gmail.com"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "ea081c31-2721-4e6c-820a-2f0da33495ac",
      "name": "Generate Actionable Task",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        2220,
        20
      ],
      "parameters": {
        "text": "={{ $('Gmail Trigger').item.json.text }}",
        "options": {
          "systemMessage": "Your task is to understand the Email content and extract one actionable task. If there is no obvious actionable task, then just create a title which implies to take a look at this Email by addressing the content summarized to 5 words. The title should be quite decided. This attribute is called title.\n\nCreate a proper description for the task. Be precise but detailed. Start with a short sentence and if it is worth adding more information, add bulletpoints after that containing additional information which help to understand the context of the task better, like links and other references, or just more detailed instructions. Add the description to the output as attribute output. Add the bulletpoints to the output as attribute output, but remember, bullet points are optional.\n\nReturn all attributes in a JSON format."
        },
        "promptType": "define",
        "hasOutputParser": true
      },
      "typeVersion": 1.6
    },
    {
      "id": "6fb2d964-dc0b-45d9-8307-6da16fba769e",
      "name": "Get Summary & Meta Data",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        2600,
        20
      ],
      "parameters": {
        "text": "={{ $('Gmail Trigger').item.json.text }}",
        "options": {
          "systemMessage": "Summarize the email (as much detail as possible) and add it to the output as the attribute summary.\n\nExtract the email sender, subject and date of receipt. If this is a forwarded email, then get this data from the original message, otherwise use the meta data of this Email. Format the Email Adress as follows, and add it to the JSON output as the attribute meta.sender: \"From: Full Name <mail@example.com\". Format the the subject as follows and add it to the output as attribute meta.subject: \"Subject: SubjectGoesHere\". Format the the date as follows and add it to the output as attribute meta.date: \"Date: DateStringGoesHere\" (Date format: RFC 2822).\n\nReturn all attributes in a JSON format."
        },
        "promptType": "define",
        "hasOutputParser": true
      },
      "typeVersion": 1.6
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "ee560597-bc46-4255-89b9-af8fe332b226",
  "connections": {
    "Globals": {
      "main": [
        [
          {
            "node": "Filter for unprocessed mails",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Calculator": {
      "ai_tool": [
        [
          {
            "node": "Get Summary & Meta Data",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Calculator1": {
      "ai_tool": [
        [
          {
            "node": "Generate Actionable Task",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Gmail Trigger": {
      "main": [
        [
          {
            "node": "Globals",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get all labels": {
      "main": [
        [
          {
            "node": "Required labels",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Route by ID": {
      "main": [
        [
          {
            "node": "Active Routes Only",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "No Operation, do nothing",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Deactivate Route": {
      "main": [
        [
          {
            "node": "Send notification about deactivated route",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract Route ID": {
      "main": [
        [
          {
            "node": "Get Route by ID",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Chat Model": {
      "ai_languageModel": [
        [
          {
            "node": "Get Summary & Meta Data",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Active Routes Only": {
      "main": [
        [
          {
            "node": "Generate Actionable Task",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Create Notion Page": {
      "main": [
        [
          {
            "node": "Add Label \"Processed\"",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Deactivate Route",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Chat Model1": {
      "ai_languageModel": [
        [
          {
            "node": "Generate Actionable Task",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Get Summary & Meta Data": {
      "main": [
        [
          {
            "node": "Format Notion Page Blocks",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Generate Actionable Task": {
      "main": [
        [
          {
            "node": "Get Summary & Meta Data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "No Operation, do nothing": {
      "main": [
        [
          {
            "node": "Send notification about missing route",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Structured Output Parser": {
      "ai_outputParser": [
        [
          {
            "node": "Get Summary & Meta Data",
            "type": "ai_outputParser",
            "index": 0
          }
        ]
      ]
    },
    "Format Notion Page Blocks": {
      "main": [
        [
          {
            "node": "Create Notion Page",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Structured Output Parser1": {
      "ai_outputParser": [
        [
          {
            "node": "Generate Actionable Task",
            "type": "ai_outputParser",
            "index": 0
          }
        ]
      ]
    },
    "Filter for unprocessed mails": {
      "main": [
        [
          {
            "node": "Extract Route ID",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "When clicking ‘Test workflow’": {
      "main": [
        [
          {
            "node": "Get all labels",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Send notification about missing route": {
      "main": [
        [
          {
            "node": "Add Label \"Error\"",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Send notification about deactivated route": {
      "main": [
        [
          {
            "node": "Add Label \"Error\"",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-910"></a>

## Template 910 - Resumo horário de mercado cripto (BTC/ETH/SOL)

- **Nome:** Resumo horário de mercado cripto (BTC/ETH/SOL)
- **Descrição:** Busca dados de 24h da Binance para pares USDC de BTC, ETH e SOL, calcula métricas relevantes e envia um resumo formatado em HTML para um chat do Telegram a cada hora.
- **Funcionalidade:** • Agendamento automático: Executa a cada hora no minuto 5.
• Coleta de dados: Consulta o endpoint público de 24h da Binance para obter informações de preço e volume.
• Retentativa de requisição: Re-tenta a chamada HTTP até 5 vezes com intervalo de 5s em caso de falha.
• Filtragem de pares USDC: Seleciona apenas pares que terminam com USDC e filtra BTCUSDC, ETHUSDC e SOLUSDC.
• Cálculo de métricas: Calcula variação percentual, volatilidade (high vs low), spread bid-ask, momentum (versus weighted average), estimativa de market cap e contagem de trades.
• Comparação com média de mercado: Compara a performance de cada ativo com a média do conjunto analisado.
• Ordenação e destaque: Identifica ganhadores, perdedores, mais volátil, mais líquido e top por volume.
• Formatação de mensagem HTML: Gera resumo enriquecido com emojis, valores formatados e escape de HTML para segurança.
• Controle de tamanho da mensagem: Divide o texto em blocos para respeitar o limite de caracteres do Telegram (chunks abaixo do limite).
• Envio para Telegram: Publica os blocos sequenciais no chat configurado com parse_mode HTML.
- **Ferramentas:** • Binance (API pública - endpoint /api/v3/ticker/24hr): Fornece dados de preço, volume e estatísticas 24h para pares de negociação.
• Telegram Bot API: Entrega as mensagens formatadas em HTML para um chat ou grupo usando um bot (chatId configurado e credenciais do bot).

## Fluxo visual

```mermaid
flowchart LR
    N1["Schedule Trigger"]
    N2["Binance 24h Price Change"]
    N3["Send Telegram Message"]
    N4["Analyze & Format Market Data"]
    N5["Sticky Note"]
    N6["Sticky Note1"]
    N7["Sticky Note2"]
    N8["Sticky Note3"]
    N9["Sticky Note4"]

    N1 --> N2
    N2 --> N4
    N4 --> N3
```

## Fluxo (.json) :

```json
{
  "meta": {
    "instanceId": "411a4eea57cf88d4a82c27728a11bad4fe2fdcbc1ab5eae589890a37e4b909ca",
    "templateId": "2043"
  },
  "nodes": [
    {
      "id": "9fd007e4-9d21-4fef-8a28-3be3e92af6f7",
      "name": "Schedule Trigger",
      "type": "n8n-nodes-base.scheduleTrigger",
      "position": [
        260,
        600
      ],
      "parameters": {
        "rule": {
          "interval": [
            {
              "field": "cronExpression",
              "expression": "5 * * * *"
            }
          ]
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "cd23c427-56f1-4924-8adf-4b38417ba652",
      "name": "Binance 24h Price Change",
      "type": "n8n-nodes-base.httpRequest",
      "notes": "Get data of changed price coins in last 24h",
      "maxTries": 5,
      "position": [
        600,
        600
      ],
      "parameters": {
        "url": "https://api.binance.com/api/v3/ticker/24hr",
        "options": {}
      },
      "notesInFlow": true,
      "retryOnFail": true,
      "typeVersion": 1,
      "waitBetweenTries": 5000
    },
    {
      "id": "40e4f7bd-ac47-4617-9177-5a84ada3a92f",
      "name": "Send Telegram Message",
      "type": "n8n-nodes-base.telegram",
      "position": [
        1560,
        600
      ],
      "webhookId": "75a4f97f-1a11-47fd-9f90-cbecd75ad2df",
      "parameters": {
        "text": "={{ $json.data }}\n\n",
        "chatId": "-4685771678",
        "additionalFields": {
          "parse_mode": "HTML"
        }
      },
      "credentials": {
        "telegramApi": {
          "id": "d6O4BUmt3I6XZJ1D",
          "name": "Telegram account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "424bbed3-f134-418c-9961-e966c8dc2592",
      "name": "Analyze & Format Market Data",
      "type": "n8n-nodes-base.function",
      "position": [
        900,
        600
      ],
      "parameters": {
        "functionCode": "function escapeHTML(text) {\n  return String(text)\n    .replace(/&/g, \"&amp;\")\n    .replace(/</g, \"&lt;\")\n    .replace(/>/g, \"&gt;\");\n}\n\nfunction formatVolume(volume) {\n  const vol = parseFloat(volume);\n  if (vol >= 1_000_000_000) return (vol / 1_000_000_000).toFixed(2) + 'B';\n  if (vol >= 1_000_000) return (vol / 1_000_000).toFixed(2) + 'M';\n  if (vol >= 1_000) return (vol / 1_000).toFixed(2) + 'K';\n  return vol.toString();\n}\n\nfunction formatMoney(amount) {\n  return parseFloat(amount).toLocaleString('en-US', {\n    minimumFractionDigits: 2,\n    maximumFractionDigits: 2\n  });\n}\n\nfunction calculateVolatility(coin) {\n  const high = parseFloat(coin.highPrice);\n  const low = parseFloat(coin.lowPrice);\n  const volatility = ((high - low) / low) * 100;\n  return volatility.toFixed(2);\n}\n\nfunction calculateSpread(coin) {\n  const ask = parseFloat(coin.askPrice);\n  const bid = parseFloat(coin.bidPrice);\n  const spread = ((ask - bid) / bid) * 100;\n  return spread.toFixed(4);\n}\n\nfunction calculateMarketComparison(coin, avgMarketChange) {\n  const coinChange = parseFloat(coin.priceChangePercent);\n  const comparison = coinChange - avgMarketChange;\n  return comparison.toFixed(2);\n}\n\nfunction formatActivity(count) {\n  return count.toLocaleString('en-US');\n}\n\nfunction calculateMomentum(coin) {\n  const current = parseFloat(coin.lastPrice);\n  const weighted = parseFloat(coin.weightedAvgPrice);\n  return ((current - weighted) / weighted * 100).toFixed(2);\n}\n\nfunction estimateMarketCap(coin) {\n  return parseFloat(coin.lastPrice) * parseFloat(coin.quoteVolume);\n}\n\nfunction formatCoinWithAnalytics(coin, avgMarketChange) {\n  const change = parseFloat(coin.priceChangePercent);\n  const arrow = change > 0 ? '🔺' : '🔻';\n  const volatility = calculateVolatility(coin);\n  const spread = calculateSpread(coin);\n  const marketComparison = calculateMarketComparison(coin, avgMarketChange);\n  const momentum = calculateMomentum(coin);\n  \n  const comparisonEmoji = marketComparison > 0 ? '⭐' : '⬇️';\n  const momentumEmoji = parseFloat(momentum) > 0 ? '🔼' : '🔽';\n  \n  const timeFrameHours = (coin.closeTime - coin.openTime) / (1000 * 60 * 60);\n  \n  return `<b>${escapeHTML(coin.symbol)}</b>\\n` +\n         `${arrow} Change: ${escapeHTML(change.toFixed(2))}% (${timeFrameHours.toFixed(0)}h)\\n` +\n         `💰 Current: $${formatMoney(coin.lastPrice)}\\n` +\n         `📊 Range: $${formatMoney(coin.lowPrice)} - $${formatMoney(coin.highPrice)}\\n` +\n         `📈 Volatility: ${volatility}%\\n` +\n         `🔄 Volume: ${escapeHTML(formatVolume(coin.volume))} | $${formatMoney(coin.quoteVolume)}\\n` +\n         `⚖️ Bid-Ask Spread: ${spread}%\\n` +\n         `${comparisonEmoji} vs Market Avg: ${marketComparison}%\\n` +\n         `${momentumEmoji} Momentum: ${momentum}%\\n` +\n         `🔢 Trades: ${formatActivity(coin.count)}\\n\\n`;\n}\n\nfunction calculateMarketStats(coins) {\n  const totalVolume = coins.reduce((sum, coin) => sum + parseFloat(coin.quoteVolume), 0);\n  const averageChange = coins.reduce((sum, coin) => sum + parseFloat(coin.priceChangePercent), 0) / coins.length;\n  const mostVolatile = [...coins].sort((a, b) => calculateVolatility(b) - calculateVolatility(a))[0];\n  const mostTraded = [...coins].sort((a, b) => parseFloat(b.quoteVolume) - parseFloat(a.quoteVolume))[0];\n  const leastSpread = [...coins].sort((a, b) => calculateSpread(a) - calculateSpread(b))[0];\n  \n  const topByVolume = [...coins]\n    .sort((a, b) => parseFloat(b.quoteVolume) - parseFloat(a.quoteVolume))\n    .slice(0, 3);\n  \n  return {\n    totalVolume,\n    averageChange,\n    mostVolatile,\n    mostTraded,\n    leastSpread,\n    topByVolume\n  };\n}\n\nconst now = new Date();\nconst dateString = now.toISOString().replace('T', ' ').split('.')[0] + ' UTC';\nconst rawData = items[0].json;\n\nconst binanceData = Array.isArray(rawData) ? rawData : [];\nconst usdcPairs = binanceData.filter(coin => coin.symbol.endsWith('USDC'));\n\n// Filter only for Solana, Bitcoin, Ethereum\nconst relevantSymbols = ['SOLUSDC', 'BTCUSDC', 'ETHUSDC'];\nconst filteredCoins = usdcPairs.filter(coin => relevantSymbols.includes(coin.symbol));\n\n// Calculate market cap for each coin\nfilteredCoins.forEach(coin => {\n  coin.estimatedMarketCap = estimateMarketCap(coin);\n});\n\nconst marketStats = calculateMarketStats(filteredCoins);\nconst avgMarketChange = marketStats.averageChange;\n\nconst gainers = filteredCoins\n  .filter(c => parseFloat(c.priceChangePercent) > 0)\n  .sort((a, b) => parseFloat(b.priceChangePercent) - parseFloat(a.priceChangePercent));\n\nconst losers = filteredCoins\n  .filter(c => parseFloat(c.priceChangePercent) < 0)\n  .sort((a, b) => parseFloat(a.priceChangePercent) - parseFloat(b.priceChangePercent));\n\n// Build message\nlet summary = `<b>📊 Crypto Market Summary — ${escapeHTML(dateString)}</b>\\n\\n`;\n\nsummary += `<b>🌐 Market Overview (BTC, ETH, SOL)</b>\\n` +\n           `Average Change: ${avgMarketChange.toFixed(2)}%\\n` +\n           `24h Volume: $${formatMoney(marketStats.totalVolume)}\\n` +\n           `Most Volatile: ${marketStats.mostVolatile.symbol} (${calculateVolatility(marketStats.mostVolatile)}%)\\n` +\n           `Most Liquid: ${marketStats.leastSpread.symbol} (${calculateSpread(marketStats.leastSpread)}% spread)\\n\\n`;\n\nsummary += `<b>💹 Top by Volume</b>\\n`;\nmarketStats.topByVolume.forEach(coin => {\n  summary += `${coin.symbol}: $${formatMoney(coin.quoteVolume)} | ${coin.priceChangePercent}%\\n`;\n});\nsummary += `\\n`;\n\nif (gainers.length) {\n  summary += `<b>📈 Gainers</b>\\n\\n`;\n  summary += gainers.map(coin => formatCoinWithAnalytics(coin, avgMarketChange)).join('');\n}\n\nif (losers.length) {\n  summary += `<b>📉 Losers</b>\\n\\n`;\n  summary += losers.map(coin => formatCoinWithAnalytics(coin, avgMarketChange)).join('');\n}\n\nconst chunks = [];\nlet current = \"\";\nsummary.split(/\\n/g).forEach(line => {\n  const lineWithBreak = line + \"\\n\";\n  if ((current + lineWithBreak).length > 4000) {\n    chunks.push({ json: { data: current.trim() } });\n    current = lineWithBreak;\n  } else {\n    current += lineWithBreak;\n  }\n});\n\nif (current.trim()) {\n  chunks.push({ json: { data: current.trim() } });\n}\n\nreturn chunks;"
      },
      "notesInFlow": true,
      "typeVersion": 1
    },
    {
      "id": "1c43afdc-b15a-4380-9c6f-2056e28a37f7",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        220,
        -100
      ],
      "parameters": {
        "color": 6,
        "width": 940,
        "height": 620,
        "content": "## 📌 Daily Crypto Market Summary Bot\n\n### 📈 What It Does\nFetches hourly 24h price data from Binance for **BTC**, **ETH**, and **SOL** (USDC pairs), analyzes key market trends, and sends a well-formatted HTML summary to a Telegram chat.\n\n---\n### 📊 Metrics Analyzed\n- 🔺 Gainers / 📉 Losers\n- 💰 Price change %\n- 📈 Volatility (High vs Low)\n- ⚖️ Bid-Ask Spread %\n- 🔼 Momentum (vs Weighted Avg)\n- ⭐ vs Market Average\n - 🔢 Number of Trades\n\n---\n### ⚠️ Notes\n- Message output is automatically **split into chunks** to stay under Telegram’s **4096 character limit**.\n- Output is sent in **rich HTML format** for better readability.\n\n---\n\n✅ This note is for internal guidance. Feel free to delete or update it after setup.\n"
      },
      "typeVersion": 1
    },
    {
      "id": "5bbd9227-2a52-4130-abf1-f6745327dbd4",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1540,
        780
      ],
      "parameters": {
        "width": 340,
        "height": 240,
        "content": "### 🛠️ Setup Instructions\n\n4. **Telegram**\n   - Create a bot via [@BotFather](https://t.me/BotFather)\n   - Add the bot to a Telegram group or use a personal chat\n   - In the **Send Telegram Message** node:\n     - Add your bot token under credentials\n     - Replace the default `chatId` with your group/user chat ID\n"
      },
      "typeVersion": 1
    },
    {
      "id": "ffa51aa0-181a-415b-933c-44fd01ca27da",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        560,
        800
      ],
      "parameters": {
        "height": 180,
        "content": "**Binance**\n   - No Binance API key required (uses public endpoint)\n   - Ensure internet access to call Binance API"
      },
      "typeVersion": 1
    },
    {
      "id": "ba902bcb-f24c-491a-bcaa-ab7bf16e5bb1",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        220,
        800
      ],
      "parameters": {
        "height": 180,
        "content": "\n### ⏱ Schedule\n- Runs **every hour**\n- Cron expression: `5 * * * *`  \n  _(At minute 5 of every hour)_"
      },
      "typeVersion": 1
    },
    {
      "id": "ae8b4d48-90ab-4b28-bbc7-07ed5d333815",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        900,
        820
      ],
      "parameters": {
        "width": 560,
        "content": "\n3. **Optional: Add More Coins**\n   - In the **Function node**, find the line:\n     ```js\n     const relevantSymbols = ['SOLUSDC', 'BTCUSDC', 'ETHUSDC'];\n     ```\n   - Add your preferred trading pairs (must end in `USDC`)"
      },
      "typeVersion": 1
    }
  ],
  "pinData": {},
  "connections": {
    "Schedule Trigger": {
      "main": [
        [
          {
            "node": "Binance 24h Price Change",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Binance 24h Price Change": {
      "main": [
        [
          {
            "node": "Analyze & Format Market Data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Analyze & Format Market Data": {
      "main": [
        [
          {
            "node": "Send Telegram Message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-911"></a>

## Template 911 - Alerta de bug urgente (Linear → Slack)

- **Nome:** Alerta de bug urgente (Linear → Slack)
- **Descrição:** Este fluxo observa eventos do Linear, filtra bugs com prioridade alta e envia uma mensagem formatada para um canal no Slack.
- **Funcionalidade:** • Detecção de novos eventos: Inicia a automação quando ocorre um novo evento no Linear (gatilho).
• Filtragem de dados para bugs urgentes: Mantém apenas itens com prioridade 3 ou superior e com a etiqueta 'bug'.
• Transformação de dados: Extrai o título e a URL do item, convertendo o título para Title Case.
• Envio de notificação: Envia uma mensagem formatada para o canal apropriado com o link e o título do item.
• Testes manuais: Permite testar o fluxo acionando manualmente o gatilho de execução para ver entrada e saída.
- **Ferramentas:** • Linear: Plataforma de gestão de projetos usada como gatilho para iniciar o fluxo.
• Slack: Plataforma de mensagens usada para enviar a notificação ao canal designado com o link e o título.

## Fluxo visual

```mermaid
flowchart LR
    N1["Sticky Note"]
    N2["Sticky Note1"]
    N3["Sticky Note2"]
    N4["Sticky Note5"]
    N5["Linear Trigger"]
    N6["When clicking 'Execute Workflow'"]
    N7["Code"]
    N8["Filter"]
    N9["Set"]
    N10["Slack"]

    N9 --> N10
    N7 --> N8
    N8 --> N9
    N5 --> N8
    N6 --> N7
```

## Fluxo (.json) :

```json
{
  "nodes": [
    {
      "id": "764c42ae-3761-4375-9de4-69ecdaf82b10",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -20,
        520
      ],
      "parameters": {
        "width": 377.1993316649719,
        "height": 590.2004455566864,
        "content": "## 👋 How to use this template\nThis template shows how you can take any event from any service, transform its data and send an alert to your desired app. Here's how to use it:\n\n1. Double click the `Slack` node and connect to your Slack account by creating a Credential.\n2. Change the channel name in the `Slack` node to a channel or user you have in Slack.\n2. Click the `Execute Workflow` button, then double click the nodes to see their input and output data\n\n### To customize this template to you needs:\n1. Enable or swap the `Linear trigger` with any service that fits your use case.\n2. Change the data transformation to fit your needs\n3. Adjust the Slack node or swap it with any node that fits your use case\n4. Disable or remove the `When clicking \"Execute Workflow\"` and `Code` node\n"
      },
      "typeVersion": 1
    },
    {
      "id": "b35b39f5-2937-437e-b4bb-bfd4fc06b2e2",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        423.0997586567955,
        520
      ],
      "parameters": {
        "width": 398.2006312053042,
        "height": 600.6569416091058,
        "content": "### 1. Trigger step listens for new events\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWe added a `Linear trigger` that starts the workflow every time we have an `Issue` event int the `Product & Design` team. \n\n**You can replace this node with any trigger you wish, like [Jira](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.jiratrigger/?utm_source=n8n_app&utm_medium=node_settings_modal-credential_link&utm_campaign=n8n-nodes-base.jiraTrigger), [Clickup](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.clickuptrigger/?utm_source=n8n_app&utm_medium=node_settings_modal-credential_link&utm_campaign=n8n-nodes-base.clickUpTrigger), [HubSpot](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.hubspottrigger/?utm_source=n8n_app&utm_medium=node_settings_modal-credential_link&utm_campaign=n8n-nodes-base.hubspotTrigger), [Google Sheets](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.googlesheetstrigger/?utm_source=n8n_app&utm_medium=node_settings_modal-credential_link&utm_campaign=n8n-nodes-base.googleSheetsTrigger) etc.**"
      },
      "typeVersion": 1
    },
    {
      "id": "466097b6-a830-43fb-9776-d3c7f676fc9a",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1400,
        620
      ],
      "parameters": {
        "width": 317.52886836027733,
        "height": 408.7361996915138,
        "content": "### 3. Notify the right channel\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nLast but not least we're sending a message to the `#important-bugs` channel in Slack.\n\n**You can replace this node with any service like [Teams](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftteams/?utm_source=n8n_app&utm_medium=node_settings_modal-credential_link&utm_campaign=n8n-nodes-base.microsoftTeams), [Telegram](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/?utm_source=n8n_app&utm_medium=node_settings_modal-credential_link&utm_campaign=n8n-nodes-base.telegram), [Email](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sendemail/?utm_source=n8n_app&utm_medium=node_settings_modal-credential_link&utm_campaign=n8n-nodes-base.emailSend) etc.**"
      },
      "typeVersion": 1
    },
    {
      "id": "99b3eadc-f3ff-4f73-91c2-909ab17ea8ff",
      "name": "Sticky Note5",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        880,
        620
      ],
      "parameters": {
        "width": 462,
        "height": 407,
        "content": "### 2. Filter and transform your data\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWe only want to notify the team, if the event is fired on creating an urgent bug.\n\nTo edit the nodes, simply drag and drop input data into the fields or change the values directly. **Besides filters, n8n does have other powerful transformation nodes like [Set](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.set/?utm_source=n8n_app&utm_medium=node_settings_modal-credential_link&utm_campaign=n8n-nodes-base.set), [ItemList](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.itemlists/?utm_source=n8n_app&utm_medium=node_settings_modal-credential_link&utm_campaign=n8n-nodes-base.itemLists), [Code](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.code/?utm_source=n8n_app&utm_medium=node_settings_modal-credential_link&utm_campaign=n8n-nodes-base.code) and many more.**"
      },
      "typeVersion": 1
    },
    {
      "id": "90e3e605-f497-4aaa-b0be-cb064e9b9ac9",
      "name": "Linear Trigger",
      "type": "n8n-nodes-base.linearTrigger",
      "disabled": true,
      "position": [
        500,
        600
      ],
      "webhookId": "b705f01f-3262-46d4-90f2-fc9f962e6766",
      "parameters": {
        "teamId": "583b87b7-a8f8-436b-872c-61373503d61d",
        "resources": [
          "issue"
        ]
      },
      "credentials": {
        "linearApi": {
          "id": "15",
          "name": "Linear account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "f956bf3b-b119-4006-b964-6fdb089ff877",
      "name": "When clicking \"Execute Workflow\"",
      "type": "n8n-nodes-base.manualTrigger",
      "notes": "For testing the workflow",
      "position": [
        500,
        800
      ],
      "parameters": {},
      "notesInFlow": true,
      "typeVersion": 1
    },
    {
      "id": "2b347886-f7a8-44eb-b26a-57c436eda594",
      "name": "Code",
      "type": "n8n-nodes-base.code",
      "notes": "Mock Data",
      "position": [
        680,
        800
      ],
      "parameters": {
        "jsCode": "return [\n  {\n    \"action\": \"create\",\n    \"createdAt\": \"2023-06-27T13:15:14.118Z\",\n    \"data\": {\n      \"id\": \"204224f8-3084-49b0-981f-3ad7f9060316\",\n      \"createdAt\": \"2023-06-27T13:15:14.118Z\",\n      \"updatedAt\": \"2023-06-27T13:15:14.118Z\",\n      \"number\": 647,\n      \"title\": \"Test event\",\n      \"priority\": 3,\n      \"boardOrder\": 0,\n      \"sortOrder\": -48454,\n      \"teamId\": \"583b87b7-a8f8-436b-872c-61373503d61d\",\n      \"previousIdentifiers\": [],\n      \"creatorId\": \"49ae7598-ae5d-42e6-8a03-9f6038a0d37a\",\n      \"stateId\": \"49c4401a-3d9e-40f6-a904-2a5eb95e0237\",\n      \"priorityLabel\": \"No priority\",\n      \"subscriberIds\": [\n        \"49ae7598-ae5d-42e6-8a03-9f6038a0d37a\"\n      ],\n      \"labelIds\": [\n        \"23381844-cdf1-4547-8d42-3b369af5b4ef\"\n      ],\n      \"state\": {\n        \"id\": \"49c4401a-3d9e-40f6-a904-2a5eb95e0237\",\n        \"color\": \"#bec2c8\",\n        \"name\": \"Backlog\",\n        \"type\": \"backlog\"\n      },\n      \"team\": {\n        \"id\": \"583b87b7-a8f8-436b-872c-61373503d61d\",\n        \"key\": \"PD\",\n        \"name\": \"Product & Design\"\n      },\n      \"labels\": [\n        {\n          \"id\": \"23381844-cdf1-4547-8d42-3b369af5b4ef\",\n          \"color\": \"#4CB782\",\n          \"name\": \"bug\"\n        }\n      ]\n    },\n    \"url\": \"https://linear.app/n8n/issue/PD-647/test-event\",\n    \"type\": \"Issue\",\n    \"organizationId\": \"1c35bbc6-9cd4-427e-8bc5-e5d370a9869f\",\n    \"webhookTimestamp\": 1687871714230\n  }\n]"
      },
      "notesInFlow": true,
      "typeVersion": 1
    },
    {
      "id": "750acf22-5fc7-40b6-8989-aa8ba1cb207b",
      "name": "Filter",
      "type": "n8n-nodes-base.filter",
      "notes": "Keep urgent bugs only",
      "position": [
        960,
        700
      ],
      "parameters": {
        "conditions": {
          "number": [
            {
              "value1": "={{ $json.data.priority }}",
              "value2": 3,
              "operation": "largerEqual"
            }
          ],
          "string": [
            {
              "value1": "={{ $json.data.labels[0].name }}",
              "value2": "bug"
            }
          ]
        }
      },
      "notesInFlow": true,
      "typeVersion": 1
    },
    {
      "id": "8ce7bb41-30f6-4d28-a5c7-ae5cb856ecc2",
      "name": "Set",
      "type": "n8n-nodes-base.set",
      "notes": "Transform title",
      "position": [
        1180,
        700
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "title",
              "value": "={{ $json.data.title.toTitleCase() }}"
            },
            {
              "name": "url",
              "value": "={{ $json.url }}"
            }
          ]
        },
        "options": {},
        "keepOnlySet": true
      },
      "notesInFlow": true,
      "typeVersion": 2
    },
    {
      "id": "b9c6f60a-5b69-4bf5-9514-9c9dc9813595",
      "name": "Slack",
      "type": "n8n-nodes-base.slack",
      "position": [
        1500,
        700
      ],
      "parameters": {
        "text": "=<!channel> New urgent bug *<{{ $json.url }}|{{ $json.title }}>*",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "mode": "name",
          "value": "#important bugs"
        },
        "otherOptions": {}
      },
      "credentials": {
        "slackApi": {
          "id": "6",
          "name": "Idea Bot"
        }
      },
      "typeVersion": 2
    }
  ],
  "connections": {
    "Set": {
      "main": [
        [
          {
            "node": "Slack",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Code": {
      "main": [
        [
          {
            "node": "Filter",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Filter": {
      "main": [
        [
          {
            "node": "Set",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Linear Trigger": {
      "main": [
        [
          {
            "node": "Filter",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "When clicking \"Execute Workflow\"": {
      "main": [
        [
          {
            "node": "Code",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-912"></a>

## Template 912 - Verificação por chamadas TTS e email

- **Nome:** Verificação por chamadas TTS e email
- **Descrição:** Este fluxo automatiza o envio de chamadas de voz com TTS para verificação de código e, em seguida, envia uma verificação por email com código, validando ambos os canais.
- **Funcionalidade:** • Início pelo envio de formulário: o fluxo é acionado quando o usuário submete o formulário de verificação.
• Definição do código de voz: o código a ser falado na chamada de verificação é criado e salvo.
• Geração do código de voz com formatação: o código é formatado para ser falado (com espaçamento entre dígitos).
• Envio da chamada de voz: o serviço externo efetua a chamada com o código via TTS.
• Verificação do código de voz: o usuário insere o código recebido para validação.
• Definição do código de email: o código de email é criado para a verificação por email.
• Envio do email de verificação: o código de email é enviado ao destinatário informado.
• Verificação do código de email: o usuário insere o código recebido por email para validação.
• Sucesso: quando ambos códigos forem corretos, o fluxo mostra confirmação de verificação concluída.
• Falhas: falhas de código de voz ou de email resultam em mensagens de erro correspondentes.
- **Ferramentas:** • ClickSend: Serviço de envio de chamadas de voz via API para verificação de código por voz.
• SMTP: Serviço de envio de emails utilizado para entregar códigos de verificação por email.

## Fluxo visual

```mermaid
flowchart LR
    N1["Sticky Note"]
    N2["Sticky Note1"]
    N3["Send Voice"]
    N4["On form submission"]
    N5["Sticky Note2"]
    N6["Send Email"]
    N7["Code for voice"]
    N8["Set voice code"]
    N9["Verify voice code"]
    N10["Fail voice code"]
    N11["Set email code"]
    N12["Verify email code"]
    N13["Is email code correct?"]
    N14["Is voice code correct?"]
    N15["Success"]
    N16["Fail email code"]
    N17["Sticky Note3"]
    N18["Sticky Note4"]
    N19["Sticky Note5"]

    N6 --> N12
    N3 --> N9
    N7 --> N3
    N11 --> N6
    N8 --> N7
    N12 --> N13
    N9 --> N14
    N4 --> N8
    N13 --> N15
    N13 --> N16
    N14 --> N11
    N14 --> N10
```

## Fluxo (.json) :

```json
{
  "id": "1g8EAij2RwhNN70t",
  "meta": {
    "instanceId": "a4bfc93e975ca233ac45ed7c9227d84cf5a2329310525917adaf3312e10d5462",
    "templateCredsSetupCompleted": true
  },
  "name": "xSend and check TTS (Text-to-speech) voice calls end email verification",
  "tags": [],
  "nodes": [
    {
      "id": "56842e20-266b-4770-b4cd-3106418caefa",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -480,
        -740
      ],
      "parameters": {
        "width": 440,
        "height": 180,
        "content": "## STEP 1\n[Register here to ClickSend](https://clicksend.com/?u=586989) and obtain your API Key and 2 € of free credits\n\nIn the node \"Send Voice\" create a \"Basic Auth\" with the username you registered and the API Key provided as your password"
      },
      "typeVersion": 1
    },
    {
      "id": "9dfff5ae-fc04-4957-a7b6-6866e8ab0854",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -480,
        -320
      ],
      "parameters": {
        "width": 440,
        "content": "## STEP 3\n\nSubmit the form and you will receive a call to the phone number you entered where the selected voice will tell you the content of the text you wrote."
      },
      "typeVersion": 1
    },
    {
      "id": "914666e8-1dc3-4d71-abf7-408b66a4508c",
      "name": "Send Voice",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        260,
        0
      ],
      "parameters": {
        "url": "https://rest.clicksend.com/v3/voice/send",
        "method": "POST",
        "options": {},
        "jsonBody": "={\n  \"messages\": [\n    {\n      \"source\": \"n8n\",\n      \"body\": \"Your verification number is {{ $json.Code }}\",\n      \"to\": \"{{ $('On form submission').item.json.To }}\",\n      \"voice\": \"{{ $('On form submission').item.json.Voice }}\",\n      \"lang\": \"{{ $('On form submission').item.json.Lang }}\",\n      \"machine_detection\": 1\n    }\n  ]\n}",
        "sendBody": true,
        "sendHeaders": true,
        "specifyBody": "json",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpBasicAuth",
        "headerParameters": {
          "parameters": [
            {
              "name": "Content-Type",
              "value": " application/json"
            },
            {}
          ]
        }
      },
      "credentials": {
        "httpBasicAuth": {
          "id": "UwsDe2JxT39eWIvY",
          "name": "ClickSend API"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "838266ee-33aa-4380-9335-5290cad30504",
      "name": "On form submission",
      "type": "n8n-nodes-base.formTrigger",
      "position": [
        -440,
        0
      ],
      "webhookId": "194f453a-1d86-4222-bd4d-117f03005560",
      "parameters": {
        "options": {},
        "formTitle": "Send Voice Message",
        "formFields": {
          "values": [
            {
              "fieldLabel": "To",
              "placeholder": "+39xxxx",
              "requiredField": true
            },
            {
              "fieldType": "dropdown",
              "fieldLabel": "Voice",
              "fieldOptions": {
                "values": [
                  {
                    "option": "male"
                  },
                  {
                    "option": "female"
                  }
                ]
              },
              "requiredField": true
            },
            {
              "fieldType": "dropdown",
              "fieldLabel": "Lang",
              "fieldOptions": {
                "values": [
                  {
                    "option": "en-us \t"
                  },
                  {
                    "option": "it-it"
                  },
                  {
                    "option": "en-au"
                  },
                  {
                    "option": "en-gb"
                  },
                  {
                    "option": "de-de"
                  },
                  {
                    "option": "es-es"
                  },
                  {
                    "option": "fr-fr"
                  },
                  {
                    "option": "is-is"
                  },
                  {
                    "option": "da-dk"
                  },
                  {
                    "option": "nl-nl"
                  },
                  {
                    "option": "pl-pl"
                  },
                  {
                    "option": "pt-br"
                  },
                  {
                    "option": "ru-ru"
                  }
                ]
              },
              "requiredField": true
            },
            {
              "fieldType": "email",
              "fieldLabel": "Email",
              "placeholder": "Email",
              "requiredField": true
            },
            {
              "fieldLabel": "Nome ",
              "placeholder": "Nome",
              "requiredField": true
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "aab0e353-0af0-4867-9178-4195c6ed045b",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -480,
        -1020
      ],
      "parameters": {
        "color": 3,
        "width": 440,
        "height": 240,
        "content": "## Send and Check TTS (Text-to-Speech) Voice Calls with Email Verification\n\nThis workflow automates the process of sending voice calls for verification purposes and combines it with email verification. It uses the ClickSend API for voice calls and integrates with SMTP for email verification. \n"
      },
      "typeVersion": 1
    },
    {
      "id": "f4c3e305-be7e-43e7-a874-2767a0411624",
      "name": "Send Email",
      "type": "n8n-nodes-base.emailSend",
      "position": [
        1180,
        -100
      ],
      "webhookId": "92aa0a80-8bea-47b7-86ef-bebc90435526",
      "parameters": {
        "html": "=Hi {{ $('On form submission').item.json['Nome '] }},<br>\nThe email verification code is <b>{{ $json['Code Email'] }}</b>",
        "options": {},
        "subject": "Verify your code",
        "toEmail": "={{ $('On form submission').item.json['Email'] }}",
        "fromEmail": "EMAIL"
      },
      "credentials": {
        "smtp": {
          "id": "hRjP3XbDiIQqvi7x",
          "name": "SMTP info@n3witalia.com"
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "5a3ff941-6d25-4479-bedc-c3cfa7c75e36",
      "name": "Code for voice",
      "type": "n8n-nodes-base.code",
      "position": [
        40,
        0
      ],
      "parameters": {
        "jsCode": "// Loop over input items and modify the 'Code' field to add spaces between characters\nfor (const item of $input.all()) {\n  const code = item.json.Code;\n\n  const spacedCode = code.split('').join(' ');\n\n  item.json.Code = spacedCode;\n}\n\nreturn $input.all();"
      },
      "typeVersion": 2
    },
    {
      "id": "14ccfe99-8fbd-4cde-9ca3-c73e541086b3",
      "name": "Set voice code",
      "type": "n8n-nodes-base.set",
      "position": [
        -220,
        0
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "89fb63af-790e-4388-9495-5f1e517ee486",
              "name": "Code",
              "type": "string",
              "value": "12345"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "b01e3604-5ca9-45cb-8a59-4f86f33d169b",
      "name": "Verify voice code",
      "type": "n8n-nodes-base.form",
      "position": [
        480,
        0
      ],
      "webhookId": "b4356cb9-4185-4c65-b7c4-1f1e00a50ce0",
      "parameters": {
        "options": {},
        "formFields": {
          "values": [
            {
              "fieldLabel": "Verify",
              "placeholder": "Verify",
              "requiredField": true
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "id": "9c013995-ce9d-4c65-9c19-2f1a410ada38",
      "name": "Fail voice code",
      "type": "n8n-nodes-base.form",
      "position": [
        940,
        100
      ],
      "webhookId": "330b8918-7890-485c-a4fb-b0a917c14edb",
      "parameters": {
        "options": {},
        "operation": "completion",
        "completionTitle": "Oh no!",
        "completionMessage": "Sorry, the code entered is invalid. Verification has not been completed"
      },
      "typeVersion": 1
    },
    {
      "id": "3abbb31d-2ad0-4c2e-8891-e65e484e2ae4",
      "name": "Set email code",
      "type": "n8n-nodes-base.set",
      "position": [
        940,
        -100
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "33438b85-27f4-4264-ab88-e1d3ec8b1ae8",
              "name": "Code Email",
              "type": "string",
              "value": "56789"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "3e453956-0056-4532-a096-a0a6de9702ae",
      "name": "Verify email code",
      "type": "n8n-nodes-base.form",
      "position": [
        1440,
        -100
      ],
      "webhookId": "db9965d4-7660-4775-a5c6-772de7927e85",
      "parameters": {
        "options": {},
        "formFields": {
          "values": [
            {
              "fieldLabel": "Verify email",
              "placeholder": "Verify email code",
              "requiredField": true
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "id": "964528b3-f25f-4591-b5fe-6b405aaed0d2",
      "name": "Is email code correct?",
      "type": "n8n-nodes-base.if",
      "position": [
        1680,
        -100
      ],
      "parameters": {
        "options": {},
        "conditions": {
          "options": {
            "version": 2,
            "leftValue": "",
            "caseSensitive": true,
            "typeValidation": "strict"
          },
          "combinator": "and",
          "conditions": [
            {
              "id": "14ee5cfc-2a21-413d-9099-e63ce12da323",
              "operator": {
                "name": "filter.operator.equals",
                "type": "string",
                "operation": "equals"
              },
              "leftValue": "={{ $('Set email code').item.json['Code Email'] }}",
              "rightValue": "={{ $json['Verify email'] }}"
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "df8f62cc-8f45-462e-84bf-0121cbf650c7",
      "name": "Is voice code correct?",
      "type": "n8n-nodes-base.if",
      "position": [
        700,
        0
      ],
      "parameters": {
        "options": {},
        "conditions": {
          "options": {
            "version": 2,
            "leftValue": "",
            "caseSensitive": true,
            "typeValidation": "strict"
          },
          "combinator": "and",
          "conditions": [
            {
              "id": "5aaaf956-3693-4930-b63e-dceb51857716",
              "operator": {
                "name": "filter.operator.equals",
                "type": "string",
                "operation": "equals"
              },
              "leftValue": "={{$('Set voice code').item.json.Code}}",
              "rightValue": "={{ $json.Verify }}"
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "1f7ff94c-9b29-481b-99cf-cef63714995c",
      "name": "Success",
      "type": "n8n-nodes-base.form",
      "position": [
        1920,
        -200
      ],
      "webhookId": "3dfd4429-927f-4695-9b64-87f53b52c3f6",
      "parameters": {
        "options": {},
        "operation": "completion",
        "completionTitle": "Great!",
        "completionMessage": "Your mobile number and email address have been verified successfully. Thank you!"
      },
      "typeVersion": 1
    },
    {
      "id": "2c6fbd06-30f9-47b8-afa0-042439ff92c6",
      "name": "Fail email code",
      "type": "n8n-nodes-base.form",
      "position": [
        1920,
        0
      ],
      "webhookId": "a26fc536-f976-4719-bb11-43111f7ec330",
      "parameters": {
        "options": {},
        "operation": "completion",
        "completionTitle": "Oh no!",
        "completionMessage": "Sorry, the code entered is invalid. Verification has not been completed"
      },
      "typeVersion": 1
    },
    {
      "id": "632e4253-f4d1-4255-93d8-b7c3b8571e36",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -260,
        -80
      ],
      "parameters": {
        "width": 180,
        "height": 240,
        "content": "Set the code that will be spoken in the verification phone call"
      },
      "typeVersion": 1
    },
    {
      "id": "37f3d155-cbb8-4c03-b8ae-43df4eec06d1",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        900,
        -180
      ],
      "parameters": {
        "width": 180,
        "height": 240,
        "content": "Set the code that will be sent in the verification email"
      },
      "typeVersion": 1
    },
    {
      "id": "4c3a01a0-927f-499f-8bf2-e402b77050c4",
      "name": "Sticky Note5",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -480,
        -520
      ],
      "parameters": {
        "width": 440,
        "content": "## STEP 2\n\nSet the verification code for this explanatory flow that will be set in the voice call and verification email.\n\nIn the node \"Send Email\" set the sender."
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "3e26e024-4da6-4449-bc3f-8604c837396a",
  "connections": {
    "Send Email": {
      "main": [
        [
          {
            "node": "Verify email code",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Send Voice": {
      "main": [
        [
          {
            "node": "Verify voice code",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Code for voice": {
      "main": [
        [
          {
            "node": "Send Voice",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set email code": {
      "main": [
        [
          {
            "node": "Send Email",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set voice code": {
      "main": [
        [
          {
            "node": "Code for voice",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Verify email code": {
      "main": [
        [
          {
            "node": "Is email code correct?",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Verify voice code": {
      "main": [
        [
          {
            "node": "Is voice code correct?",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "On form submission": {
      "main": [
        [
          {
            "node": "Set voice code",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Is email code correct?": {
      "main": [
        [
          {
            "node": "Success",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Fail email code",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Is voice code correct?": {
      "main": [
        [
          {
            "node": "Set email code",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Fail voice code",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-913"></a>

## Template 913 - Exportar pedidos Squarespace para Google Sheets

- **Nome:** Exportar pedidos Squarespace para Google Sheets
- **Descrição:** Recupera pedidos da loja Squarespace e os grava (append/atualiza) em uma planilha do Google Sheets, permitindo filtros e paginação para obter todos os registros.
- **Funcionalidade:** • Gatilhos de execução: Permite iniciar a automação manualmente ou em uma agenda.
• Variáveis globais configuráveis: Define versão da API, filtros de data (modifiedAfter/modifiedBefore), cursor de paginação, status de cumprimento e limite de páginas.
• Consulta à API de pedidos: Faz requisições ao endpoint de pedidos do Squarespace com autenticação por cabeçalho.
• Paginação automática: Itera usando cursor e opção de máximo de páginas (inclui opção para buscar todas as páginas).
• Filtragem de resultados: Suporta filtros por datas e por fulfillmentStatus para limitar os pedidos retornados.
• Processamento de cada pedido individualmente: Separa os pedidos retornados para inserir um por linha na planilha.
• Inserção/atualização na planilha: Faz append ou update dos registros no Google Sheets usando correspondência pelo ID do pedido.
• Mapeamento de campos: Mapeia campos do pedido (email, totais, endereços, método de envio, status, etc.) para colunas definidas na planilha.
- **Ferramentas:** • Squarespace Commerce API: Fonte dos dados de pedidos da loja; suporta filtros, paginação por cursor e autenticação por chave/API.
• Google Sheets: Planilha usada para armazenar e manter os registros de pedidos, com suporte a append e atualização por coluna de correspondência (Order ID).

## Fluxo visual

```mermaid
flowchart LR
    N1["On clicking 'execute'"]
    N2["Query Orders"]
    N3["Split Out Order"]
    N4["Squarespace Orders Spreadsheet"]
    N5["Globals"]
    N6["Sticky Note3"]
    N7["Schedule Trigger"]
    N8["Sticky Note"]

    N5 --> N2
    N7 --> N5
    N1 --> N5
```

## Fluxo (.json) :

```json
{
  "id": "cRprVEUCjjvozkfb",
  "meta": {
    "instanceId": "e634e668fe1fc93a75c4f2a7fc0dad807ca318b79654157eadb9578496acbc76",
    "templateId": "548",
    "templateCredsSetupCompleted": true
  },
  "name": "Get all orders in Squarespace to Google Sheets",
  "tags": [
    {
      "id": "oIxDbURnjwrJFwau",
      "name": "Squarespace",
      "createdAt": "2025-03-06T05:49:51.612Z",
      "updatedAt": "2025-03-06T05:49:51.612Z"
    }
  ],
  "nodes": [
    {
      "id": "cafda066-7a13-4e0d-8e3d-288196b8297a",
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        340,
        100
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "a1dcafad-6e82-4569-ba33-560d3286b08e",
      "name": "Query Orders",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        800,
        180
      ],
      "parameters": {
        "url": "=https://api.squarespace.com/{{ $json[\"api-version\"] }}/commerce/orders",
        "options": {
          "pagination": {
            "pagination": {
              "parameters": {
                "parameters": [
                  {
                    "name": "cursor",
                    "value": "={{ $response.body.pagination.nextPageCursor }}"
                  }
                ]
              },
              "maxRequests": "={{ $json.maxPage === -1 ? Infinity : $json.maxPage }}",
              "limitPagesFetched": true,
              "completeExpression": "={{ !$response.body.pagination.nextPageCursor }}",
              "paginationCompleteWhen": "other"
            }
          }
        },
        "sendQuery": true,
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "queryParameters": {
          "parameters": [
            {
              "name": "modifiedAfter",
              "value": "={{ $json.modifiedAfter }}"
            },
            {
              "name": "=modifiedBefore",
              "value": "={{ $json.modifiedBefore }}"
            },
            {
              "name": "cursor",
              "value": "={{ $json.cursor }}"
            },
            {
              "name": "=fulfillmentStatus",
              "value": "={{ $json.fulfillmentStatus }}"
            }
          ]
        }
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "iiLmD473RYjGLbCA",
          "name": "Squarespace API key - Apps script"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "a2c82b9f-cc73-4f0c-bec7-ebacdeb5787d",
      "name": "Split Out Order ",
      "type": "n8n-nodes-base.splitOut",
      "position": [
        1020,
        180
      ],
      "parameters": {
        "options": {},
        "fieldToSplitOut": "result"
      },
      "typeVersion": 1
    },
    {
      "id": "e910c791-d8be-4a4a-8d91-b9ef78c7c287",
      "name": "Squarespace Orders Spreadsheet",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        1260,
        180
      ],
      "parameters": {
        "columns": {
          "value": {
            "Email": "={{ $json.customerEmail }}",
            "Total": "={{ $json.grandTotal.value }}",
            "Currency": "={{ $json.subtotal.currency }}",
            "Order ID": "={{ $json.orderNumber }}",
            "Subtotal": "={{ $json.subtotal.value }}",
            "Billing Zip": "={{ $json.billingAddress.postalCode }}",
            "Billing City": "={{ $json.billingAddress.city }}",
            "Billing Name": "={{ $json.billingAddress.firstName }} {{ $json.billingAddress.lastName }}",
            "Channel Name": "={{ $json.channel }}",
            "Shipping Zip": "={{ $json.shippingAddress.postalCode }}",
            "Billing Phone": "={{ $json.billingAddress.phone }}",
            "Shipping City": "={{ $json.shippingAddress.city }}",
            "Shipping Name": "={{ $json.shippingAddress.firstName }} {{ $json.shippingAddress.lastName }}",
            "Shipping Phone": "={{ $json.shippingAddress.phone }}",
            "Billing Country": "={{ $json.billingAddress.countryCode }}",
            "Shipping Method": "={{ $json.shippingLines[0].method }}",
            "Billing Address1": "={{ $json.billingAddress.address1 }}",
            "Billing Address2": "={{ $json.billingAddress.address2 }}",
            "Billing Province": "={{ $json.billingAddress.state }}",
            "Financial Status": "=",
            "Shipping Country": "={{ $json.shippingAddress.countryCode }}",
            "Shipping Address1": "={{ $json.shippingAddress.address1 }}",
            "Shipping Address2": "={{ $json.shippingAddress.address2 }}",
            "Shipping Province": "={{ $json.shippingAddress.state }}",
            "Fulfillment Status": "={{ $json.fulfillmentStatus }}"
          },
          "schema": [
            {
              "id": "Order ID",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "Order ID",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Email",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Email",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Financial Status",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Financial Status",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Paid at",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Paid at",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Fulfillment Status",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Fulfillment Status",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Fulfilled at",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Fulfilled at",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Currency",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Currency",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Subtotal",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Subtotal",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Shipping",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Shipping",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Taxes",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Taxes",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Amount Refunded",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Amount Refunded",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Total",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Total",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Discount Code",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Discount Code",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Discount Amount",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Discount Amount",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Shipping Method",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Shipping Method",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Created at",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Created at",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Lineitem quantity",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Lineitem quantity",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Lineitem name",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Lineitem name",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Lineitem price",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Lineitem price",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Lineitem sku",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Lineitem sku",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Lineitem variant",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Lineitem variant",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Lineitem requires shipping",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Lineitem requires shipping",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Lineitem taxable",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Lineitem taxable",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Lineitem fulfillment status",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Lineitem fulfillment status",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Billing Name",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Billing Name",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Billing Address1",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Billing Address1",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Billing Address2",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Billing Address2",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Billing City",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Billing City",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Billing Zip",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Billing Zip",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Billing Province",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Billing Province",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Billing Country",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Billing Country",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Billing Phone",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Billing Phone",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Shipping Name",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Shipping Name",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Shipping Address1",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Shipping Address1",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Shipping Address2",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Shipping Address2",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Shipping City",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Shipping City",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Shipping Zip",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Shipping Zip",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Shipping Province",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Shipping Province",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Shipping Country",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Shipping Country",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Shipping Phone",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Shipping Phone",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Cancelled at",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Cancelled at",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Private Notes",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Private Notes",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Channel Type",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Channel Type",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Channel Name",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Channel Name",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Channel Order Number",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Channel Order Number",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Payment Method",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Payment Method",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Payment Reference",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Payment Reference",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            }
          ],
          "mappingMode": "defineBelow",
          "matchingColumns": [
            "Order ID"
          ],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {},
        "operation": "appendOrUpdate",
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": 2043293467,
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1yf_RYZGFHpMyOvD3RKGSvIFY2vumvI4474Qm_1t4-jM/edit#gid=2043293467",
          "cachedResultName": "squarespace_orders"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "1yf_RYZGFHpMyOvD3RKGSvIFY2vumvI4474Qm_1t4-jM",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1yf_RYZGFHpMyOvD3RKGSvIFY2vumvI4474Qm_1t4-jM/edit?usp=drivesdk",
          "cachedResultName": "Squarespace automation"
        }
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "JgI9maibw5DnBXRP",
          "name": "Google Sheets account"
        }
      },
      "typeVersion": 4.5
    },
    {
      "id": "83b65c0e-c7f2-460d-b9cc-cc0dbab62737",
      "name": "Globals",
      "type": "n8n-nodes-base.set",
      "position": [
        580,
        180
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "7411b768-9861-414c-aeaa-2743b3d61a3b",
              "name": "api-version",
              "type": "string",
              "value": "1.0"
            },
            {
              "id": "6cf546c5-5737-4dbd-851b-17d68e0a3780",
              "name": "modifiedAfter",
              "type": "string",
              "value": ""
            },
            {
              "id": "452efa28-2dc6-4ea3-a7a2-c35d100d0382",
              "name": "modifiedBefore",
              "type": "string",
              "value": ""
            },
            {
              "id": "81c4dc54-86bf-4432-a23f-22c7ea831e74",
              "name": "cursor",
              "type": "string",
              "value": ""
            },
            {
              "id": "fa31a552-0d2d-4eb3-8476-44024e1fdc81",
              "name": "fulfillmentStatus",
              "type": "string",
              "value": ""
            },
            {
              "id": "489ff3e6-7bc3-4940-9312-e4ace8e1db9f",
              "name": "maxPage",
              "type": "number",
              "value": -1
            }
          ]
        }
      },
      "notesInFlow": true,
      "typeVersion": 3.4
    },
    {
      "id": "1626670d-6616-4d5a-84b7-d4d3948f4a99",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        520,
        60
      ],
      "parameters": {
        "color": 4,
        "width": 150,
        "height": 80,
        "content": "## Edit this node 👇"
      },
      "typeVersion": 1
    },
    {
      "id": "398082af-1188-46c9-8f71-a5029b3ff9d0",
      "name": "Schedule Trigger",
      "type": "n8n-nodes-base.scheduleTrigger",
      "position": [
        340,
        320
      ],
      "parameters": {
        "rule": {
          "interval": [
            {}
          ]
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "2eedf012-59dc-42ca-a073-374faaac4cf9",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -20,
        -20
      ],
      "parameters": {
        "width": 320,
        "height": 660,
        "content": "## Get all Squarespace Orders\nRetrieves all Squarespace Orders and saves them into a Google Sheets spreadsheet using the Squarespace Commerce API\n\n### Setup\nOpen `Globals` node and update the values below 👇\n\n- **api-version** (string, required) – The current API version (see Squarespace Orders API documentation).\n- **modifiedAfter**={a-datetime} (string, conditional) – Fetch orders modified after a specific date (ISO 8601 format).\n- **modifiedBefore**={b-datetime} (string, conditional) – Fetch orders modified before a specific date (ISO 8601 format).\n- **cursor**={c} (string, conditional) – Used for pagination, cannot be combined with other filters.\n- **fulfillmentStatus**: PENDING, FULFILLED, or CANCELED.\n- **maxPage** – Set -1 to enables infinite pagination to fetch all available orders.\n\n"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "fd8ca9c3-787d-40da-aa22-594a3e900f0d",
  "connections": {
    "Globals": {
      "main": [
        [
          {
            "node": "Query Orders",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Query Orders": {
      "main": [
        [
          {
            "node": "Split Out Order ",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Schedule Trigger": {
      "main": [
        [
          {
            "node": "Globals",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Split Out Order ": {
      "main": [
        [
          {
            "node": "Squarespace Orders Spreadsheet",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "Globals",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Squarespace Orders Spreadsheet": {
      "main": [
        []
      ]
    }
  }
}
```

<a id="template-914"></a>

## Template 914 - Análise de posts do Reddit para oportunidades de negócio

- **Nome:** Análise de posts do Reddit para oportunidades de negócio
- **Descrição:** Coleta posts de subreddits, filtra e analisa conteúdo com modelos de IA para gerar resumos, avaliar sentimento e sugerir ideias de negócio; resultados são organizados e salvos em planilha e rascunhos de e-mail.
- **Funcionalidade:** • Coleta de posts do Reddit: Pesquisa posts em um subreddit específico por palavra-chave e ordena por popularidade.
• Filtragem por métricas e recência: Filtra posts por número mínimo de upvotes, texto não vazio e publicação dentro de um período determinado (ex.: 180 dias).
• Seleção de campos chave: Extrai e padroniza campos essenciais (upvotes, subscritores do subreddit, conteúdo do post, URL, data).
• Classificação do conteúdo por relevância de negócio: Modelo de IA decide se o post descreve um problema ou necessidade empresarial (sim/não).
• Sumarização do post: Gera um resumo conciso do conteúdo do post usando um modelo de linguagem.
• Análise de sentimento: Avalia o sentimento do conteúdo para categorizar como positivo, neutro ou negativo.
• Geração de soluções/ideias de negócio: Produz uma proposta curta de serviço ou ideia de negócio para resolver o problema descrito no post.
• Geração de rascunhos de e-mail: Cria rascunhos no Gmail classificados por sentimento (positivo, neutro, negativo) com o conteúdo do post.
• Consolidação e saída: Combina resumos, soluções e metadados e grava linhas com colunas definidas em uma planilha do Google Sheets.
- **Ferramentas:** • Reddit: Fonte de posts públicos; usada para buscar e recuperar conteúdo de comunidades específicas com filtros de palavra-chave e ordenação.
• OpenAI (modelos de linguagem): Usado para classificar relevância de negócio, resumir posts, analisar sentimento e sugerir ideias/soluções comerciais.
• Gmail: Cria rascunhos de e-mail para posterior revisão ou envio, categorizados conforme o sentimento do post.
• Google Sheets: Armazena os resultados consolidados (upvotes, URL, data, resumo, solução proposta, tamanho do subreddit) para acompanhamento e análise.

## Fluxo visual

```mermaid
flowchart LR
    N1["When clicking ‘Test workflow’"]
    N2["OpenAI Chat Model"]
    N3["OpenAI Chat Model1"]
    N4["OpenAI Chat Model2"]
    N5["Post Sentiment Analysis"]
    N6["Positive Posts Draft"]
    N7["Neutral  Posts Draft"]
    N8["Negative  Posts Draft"]
    N9["Find Proper Solutions"]
    N10["Post Summarization"]
    N11["Merge Input"]
    N12["Output The Results"]
    N13["Merge 3 Inputs"]
    N14["Filter Posts By Features"]
    N15["Filter Posts By Content"]
    N16["Select Key Fields"]
    N17["Analysis Content  By AI"]
    N18["Get Posts"]
    N19["Sticky Note"]
    N20["Sticky Note1"]
    N21["Sticky Note2"]
    N22["Sticky Note3"]

    N18 --> N14
    N11 --> N15
    N13 --> N12
    N16 --> N11
    N16 --> N17
    N10 --> N13
    N9 --> N13
    N17 --> N11
    N15 --> N10
    N15 --> N9
    N15 --> N13
    N15 --> N5
    N5 --> N6
    N5 --> N7
    N5 --> N8
    N14 --> N16
    N1 --> N18
```

## Fluxo (.json) :

```json
{
  "id": "Xx4zOjRFLI8W9PiC",
  "meta": {
    "instanceId": "481a48d2941aac0cf9462ce6b93b63097e0c030779c473519ff7c167c8bed8f7",
    "templateCredsSetupCompleted": true
  },
  "name": "Analyze Reddit Posts with AI to Identify Business Opportunities",
  "tags": [],
  "nodes": [
    {
      "id": "52bdf7eb-ee1a-43c5-a0ad-199283003892",
      "name": "When clicking ‘Test workflow’",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        -1400,
        -640
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "e9a000b6-2f35-4928-a8d8-aa2d8cc27513",
      "name": "OpenAI Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        -360,
        -760
      ],
      "parameters": {
        "model": {
          "__rl": true,
          "mode": "list",
          "value": "gpt-4o-mini",
          "cachedResultName": "gpt-4o-mini"
        },
        "options": {}
      },
      "credentials": {
        "openAiApi": {
          "id": "SOgg2BJ10kvhpBbS",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "cd38a8b6-1369-4209-a80e-9e9949df49c0",
      "name": "OpenAI Chat Model1",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        680,
        -1080
      ],
      "parameters": {
        "model": {
          "__rl": true,
          "mode": "list",
          "value": "gpt-4o-mini"
        },
        "options": {}
      },
      "credentials": {
        "openAiApi": {
          "id": "SOgg2BJ10kvhpBbS",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "4749ca62-6061-4dc0-8f1a-b0e995bb3d0f",
      "name": "OpenAI Chat Model2",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        640,
        -220
      ],
      "parameters": {
        "model": {
          "__rl": true,
          "mode": "list",
          "value": "gpt-4o-mini"
        },
        "options": {}
      },
      "credentials": {
        "openAiApi": {
          "id": "SOgg2BJ10kvhpBbS",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "ed68c267-9716-4930-b210-d1f1ae89d8c8",
      "name": "Post Sentiment Analysis",
      "type": "@n8n/n8n-nodes-langchain.sentimentAnalysis",
      "position": [
        740,
        -400
      ],
      "parameters": {
        "options": {},
        "inputText": "={{ $json.postcontent }}"
      },
      "typeVersion": 1
    },
    {
      "id": "2e651e62-00dd-4f0d-a8bc-ce4d8b9fa1d7",
      "name": "Positive Posts Draft",
      "type": "n8n-nodes-base.gmail",
      "position": [
        1260,
        -560
      ],
      "webhookId": "f9dabe4c-9c74-4486-932a-606ea4bb830f",
      "parameters": {
        "message": "={{ $json.postcontent }}",
        "options": {},
        "subject": "Positive Post",
        "resource": "draft"
      },
      "credentials": {
        "gmailOAuth2": {
          "id": "jUQtZvR5i5glEufn",
          "name": "Gmail account"
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "29d478d2-43d4-467a-89c2-8c97ea6e245c",
      "name": "Neutral  Posts Draft",
      "type": "n8n-nodes-base.gmail",
      "position": [
        1280,
        -380
      ],
      "webhookId": "f9dabe4c-9c74-4486-932a-606ea4bb830f",
      "parameters": {
        "message": "={{ $json.postcontent }}",
        "options": {},
        "subject": "Neutral Post",
        "resource": "draft"
      },
      "credentials": {
        "gmailOAuth2": {
          "id": "jUQtZvR5i5glEufn",
          "name": "Gmail account"
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "c289805f-5246-4f3a-9052-48c426da8ce0",
      "name": "Negative  Posts Draft",
      "type": "n8n-nodes-base.gmail",
      "position": [
        1280,
        -160
      ],
      "webhookId": "f9dabe4c-9c74-4486-932a-606ea4bb830f",
      "parameters": {
        "message": "={{ $json.postcontent }}",
        "options": {},
        "subject": "Negative Post",
        "resource": "draft"
      },
      "credentials": {
        "gmailOAuth2": {
          "id": "jUQtZvR5i5glEufn",
          "name": "Gmail account"
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "00d17970-3195-4290-bb02-9956f31ecc8f",
      "name": "Find Proper Solutions",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "position": [
        840,
        -1040
      ],
      "parameters": {
        "modelId": {
          "__rl": true,
          "mode": "list",
          "value": "gpt-4o-mini",
          "cachedResultName": "GPT-4O-MINI"
        },
        "options": {},
        "messages": {
          "values": [
            {
              "content": "=Based on the following Reddit post, suggest a business idea or service that I could create to help this problem for this business and other with similar needs.\n\nReddit post:  \"{{ $json.postcontent }}\"\n\nProvide a concise description of a business idea or service that would adress this issue effectively for mutiple businesses facing similar challenges.\n"
            }
          ]
        }
      },
      "credentials": {
        "openAiApi": {
          "id": "SOgg2BJ10kvhpBbS",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1.8
    },
    {
      "id": "9bcbd874-5eed-47ce-9714-1aec71537fe2",
      "name": "Post Summarization",
      "type": "@n8n/n8n-nodes-langchain.chainSummarization",
      "position": [
        760,
        -1280
      ],
      "parameters": {
        "options": {}
      },
      "typeVersion": 2
    },
    {
      "id": "60991de9-ad29-484c-9233-966cc1980a03",
      "name": "Merge Input",
      "type": "n8n-nodes-base.merge",
      "position": [
        -80,
        -700
      ],
      "parameters": {
        "mode": "combine",
        "options": {},
        "combineBy": "combineByPosition"
      },
      "typeVersion": 3
    },
    {
      "id": "f78fbea9-5f7f-4a88-bde1-7c3f01613892",
      "name": "Output The Results",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        1520,
        -1260
      ],
      "parameters": {
        "columns": {
          "value": {
            "Upvotes": "={{ $json.upvotes }}",
            "Post_url": "={{ $json.url }}",
            "Post_date": "={{ $json.date }}",
            "Post_summary": "={{ $json.response.text }}",
            "Post_solution": "={{ $json.message.content }}",
            "Subreddit_size": "={{ $json.subreddit_subscribers }}"
          },
          "schema": [
            {
              "id": "Subreddit",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "Subreddit",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Subreddit_size",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "Subreddit_size",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Post_date",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "Post_date",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Upvotes",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "Upvotes",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Post_url",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "Post_url",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Post_summary",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "Post_summary",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Post_solution",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "Post_solution",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            }
          ],
          "mappingMode": "defineBelow",
          "matchingColumns": [
            "test"
          ],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {},
        "operation": "append",
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": "gid=0",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1C8grVByPo3osYiV5X1pWhEUR9NhBXJGXBE75wC5o6rE/edit#gid=0",
          "cachedResultName": "sheet1"
        },
        "documentId": {
          "__rl": true,
          "mode": "id",
          "value": "1C8grVByPo3osYiV5X1pWhEUR9NhBXJGXBE75wC5o6rE"
        }
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "WMi7PlGTPumH5bHV",
          "name": "Google Sheets account"
        }
      },
      "typeVersion": 4.5
    },
    {
      "id": "a0259ed2-0615-4e92-9e7e-cbff8c5bc0ce",
      "name": "Merge 3 Inputs",
      "type": "n8n-nodes-base.merge",
      "position": [
        1340,
        -1040
      ],
      "parameters": {
        "mode": "combine",
        "options": {},
        "combineBy": "combineByPosition",
        "numberInputs": 3
      },
      "typeVersion": 3
    },
    {
      "id": "b7326fd0-5379-42ac-b355-ef6c3c1790f9",
      "name": "Filter Posts By Features",
      "type": "n8n-nodes-base.if",
      "position": [
        -980,
        -640
      ],
      "parameters": {
        "options": {},
        "conditions": {
          "options": {
            "version": 2,
            "leftValue": "",
            "caseSensitive": true,
            "typeValidation": "strict"
          },
          "combinator": "and",
          "conditions": [
            {
              "id": "0823d10a-ad54-4d82-bcea-9dd236e97857",
              "operator": {
                "type": "number",
                "operation": "gt"
              },
              "leftValue": "={{ $json.ups }}",
              "rightValue": 2
            },
            {
              "id": "bb8187aa-f0f1-4999-8d4b-bdc9abba0618",
              "operator": {
                "type": "string",
                "operation": "notEmpty",
                "singleValue": true
              },
              "leftValue": "={{ $json.selftext }}",
              "rightValue": ""
            },
            {
              "id": "539f0f5c-025a-4f82-9b3a-2ef1ad3a2d96",
              "operator": {
                "type": "dateTime",
                "operation": "after"
              },
              "leftValue": "={{ DateTime.fromSeconds($json.created).toISO() }}",
              "rightValue": "={{ $today.minus(180,'days').toISO() }}"
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "11c45f28-97c0-4087-975c-651f27438956",
      "name": "Filter Posts By Content",
      "type": "n8n-nodes-base.if",
      "position": [
        180,
        -680
      ],
      "parameters": {
        "options": {},
        "conditions": {
          "options": {
            "version": 2,
            "leftValue": "",
            "caseSensitive": true,
            "typeValidation": "strict"
          },
          "combinator": "and",
          "conditions": [
            {
              "id": "d5d38c01-3a88-4767-b488-d9c04145bb8f",
              "operator": {
                "name": "filter.operator.equals",
                "type": "string",
                "operation": "equals"
              },
              "leftValue": "={{ $json.output }}",
              "rightValue": "yes"
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "efede239-eff5-4e38-b40d-3cefea040644",
      "name": "Select Key Fields",
      "type": "n8n-nodes-base.set",
      "position": [
        -740,
        -660
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "e5082ecc-3add-474e-bdb5-b8ad64729930",
              "name": "upvotes",
              "type": "string",
              "value": "={{ $json.ups }}"
            },
            {
              "id": "a92b5859-fbcc-40c2-95e0-452b12530d98",
              "name": "subreddit_subscribers",
              "type": "number",
              "value": "={{ $json.subreddit_subscribers }}"
            },
            {
              "id": "a846e21c-6cff-4521-9e0c-a32fa1305376",
              "name": "postcontent",
              "type": "string",
              "value": "={{ $json.selftext }}"
            },
            {
              "id": "b8045389-684d-4872-9e32-9a6b5511eb2b",
              "name": "url",
              "type": "string",
              "value": "={{ $json.url }}"
            },
            {
              "id": "f182fedc-1b09-40fe-aeb5-2473263da442",
              "name": "date",
              "type": "string",
              "value": "={{ DateTime.fromSeconds($json.created).toISO() }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "1a99fdaa-6857-4210-a695-71ce531c1fa0",
      "name": "Analysis Content  By AI",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        -460,
        -940
      ],
      "parameters": {
        "text": "Decide whether this reddit post is describing a business-related problem or a need for a solution. The post  should mention a specific challenge \n or requirement that a business is trying to address.\nReddit post:  {{ $json.postcontent }}\nIs this post about a business problem or need for a solution ? Output only yes or no",
        "agent": "conversationalAgent",
        "options": {},
        "promptType": "define"
      },
      "typeVersion": 1.7
    },
    {
      "id": "72b30080-e1f2-48b4-b816-ff43542cc6f1",
      "name": "Get Posts",
      "type": "n8n-nodes-base.reddit",
      "position": [
        -1180,
        -640
      ],
      "parameters": {
        "limit": 20,
        "keyword": "looking for a solution",
        "operation": "search",
        "subreddit": "=smallbusiness",
        "additionalFields": {
          "sort": "hot"
        }
      },
      "credentials": {
        "redditOAuth2Api": {
          "id": "iX4P4iMPDji7tHjP",
          "name": "Reddit account "
        }
      },
      "typeVersion": 1
    },
    {
      "id": "c4ecb9ec-4895-4b41-ba7e-185e3769ce41",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -1500,
        -880
      ],
      "parameters": {
        "width": 880,
        "height": 440,
        "content": "# Data Collection\n## Retrieves recent popular posts from specified Reddit communities\n## Filters content by engagement metrics and keywords"
      },
      "typeVersion": 1
    },
    {
      "id": "49735ff9-7f15-4050-9c46-6c13666479bd",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        560,
        -620
      ],
      "parameters": {
        "width": 1020,
        "height": 660,
        "content": "# Post Sentiment Analysis\n## "
      },
      "typeVersion": 1
    },
    {
      "id": "17048a9e-6080-406e-a4e7-5d57406576e1",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -500,
        -1160
      ],
      "parameters": {
        "color": 4,
        "width": 820,
        "height": 680,
        "content": "# Analysis Content\n## Emerging market needs\n## Underserved customer demands"
      },
      "typeVersion": 1
    },
    {
      "id": "5a412abc-3866-44ba-9ab0-8cc0a3e012f2",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        520,
        -1480
      ],
      "parameters": {
        "color": 6,
        "width": 1220,
        "height": 640,
        "content": "# Insight Generation And Output \n## Generates executive summaries of key opportunities\n## Consolidates findings in Google Sheets"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {
    "Merge Input": [
      {
        "json": {
          "url": "https://www.reddit.com/r/smallbusiness/comments/1iqletb/need_help_and_advice_for_a_business_name_idea/",
          "date": "2025-02-16T13:42:12.000+08:00",
          "output": "yes",
          "upvotes": "4",
          "postcontent": "Hello guys,\n\nMy partner and I are planning to open an accounting business that will focus on tax services such as filling taxes and tax advisor and we have plan for future to add wealth management and capital advising. Initially, we were thinking of using the name \"Global Solutions,\" but we found out that another company already has it, so we can’t use it.\n\nWe’re looking for a professional name that’s easy to pronounce and somewhat similar to \"Global Solutions.\" Also, unique enough that we won’t want to change it in the future. Any ideas or suggestions would be greatly appreciated! We would love to list all name suggestions to share with my partner so we can pick the best one.\n\nThanks in advance for your help! Appreciate it! ",
          "subreddit_subscribers": 1944498
        }
      },
      {
        "json": {
          "url": "https://www.reddit.com/r/smallbusiness/comments/1iob5ez/business_acquisition_loan_what_are_my_odds_what/",
          "date": "2025-02-13T12:34:29.000+08:00",
          "output": "yes",
          "upvotes": "3",
          "postcontent": "Hello!  \nLongtime friends have offered to sell my their local biz.    \n12 years running, last year did 950k gross, 325K SDE.  \nYOY growth has been good.  \n650k price.  \nThey have offered to seller finance up to 61.5% of the purchase price so far.  \nThey might go even higher on the seller financing if I ask.\n\n**The good (about me):**  \n  \n\\- I have good credit, probably 720+.  \n\\- I do have \\~200k equity in my home, I'm willing to collateralize.  \n  \n**The ugly (about me):**  \n  \n\\- I have only 5% down possible for equity injection, but would prefer 0%  \nI read that with a SBA 7(a) loan the seller can do 5% of my equity injection with a standby note (deferred payment until SBA loan is paid off).  I'm not sure if that could be done in tandem with another (much larger) note that would be payable (in payments) at closing.  \n  \n\\- I've had no / negative income the last couple of years.  I took some time off from my 20+ year profession, lived off of savings and some credit while I explored other career paths because I needed a change.  I did learn a couple of high value trades, and did incur some expenses in that process.\n\n\\- No direct industry experience.  I do have much professional experience I bring to the table, but not in this industry.  I have managed people on my team... but not employees.  \n\n**The rest:**  \n  \nThey are willing to hire me as store manager now, if that helps.    \nThey will be providing complete training and ongoing support.  \nIt is a simple business, really.  \nThey obviously believe in their business, given the willingness to seller finance so much of it.  \n  \nWhat are the odds I could get a SBA 7(a) loan with 5% down?  \nAre there any loans with 0% down?  \n  \nI would like to get an extra 50k or so for startup costs - it is an acquisition however I'm going to have startup expenses like first and last months lease payments, jurisdictional inspections, electricity deposit, liability insurance / workman's comp, that sort of stuff.\n\nI realize the scenario is not ideal, however it seems to me there should be SOME option out there given that all I have to do is not mess up the business!  It's a great business, well loved in the community.  \nThere is good room in the revenue for me to make accelerated loan repayments, establish business savings, grow the business, and even pay myself enough to cover my living expenses.  That is one heck of a deal, I have to find some way to pull this off!\n\nI'm willing to look at less fantastic loan offers with higher rates.    \nIt really seems to me that some entity would be willing to lend based on the cashflow / success / stability of the existing business.\n\nOne idea I had - if sellers would be willing to carry 100% for 12-24 months, would I then likely have an easier time qualifying for a SBA 7(a) loan to pay off their note, or part of it (depending on what they want)?\n\nAnother idea - store manager -&gt; partner -&gt; partner buyout  \nI do need to find out their maximum timeline for getting out.  \n  \nHad I known a couple of years ago this was going to come up, I would have made different decisions!  \nI really don't want to sell my house and rent something in order to do this, but I'm considering that as a last resort.  \nIf these weren't my longtime friends whom I trust with my life, I wouldn't consider this.  I'd be too chicken.  This is like winning the lottery to me, frankly... I'm not the perfect buyer on paper but they really want me to have it.  They know it will be my baby, as it has been theirs.\n\nGrateful for any solutions / ideas, thank you in advance!  =D\n\n",
          "subreddit_subscribers": 1944498
        }
      },
      {
        "json": {
          "url": "https://www.reddit.com/r/smallbusiness/comments/1ikcdi5/seeking_a_reliable_alternative_to_stripe_for/",
          "date": "2025-02-08T10:09:44.000+08:00",
          "output": "yes",
          "upvotes": "3",
          "postcontent": "Hi everyone,\n\nI'm looking for advice on the **best alternative to Stripe** for my service-based business. Here’s the situation:\n\n* I handle **monthly recurring payments** from customers who prefer paying by **credit card**.\n* My customers provide me with their credit card information, and I need a solution to **send invoices** or **auto-charge their cards monthly** without issues.\n\n# Problems I’ve Faced:\n\n1. **Stripe**: I’ve lost countless disputes despite providing proof of service, and I’m fed up with their **chargeback process**.\n2. **Square**: I processed just **two paid invoices totaling $180**, and they **deactivated my account**, holding my money for **90 days**!\n\nI’m desperate to find a platform that:\n\n* Allows **invoicing** and **recurring auto-charges**.\n* Has **minimal chargebacks or disputes**, or at least a fair dispute resolution process. or **BEST: no disputes at all**\n* Doesn’t hold funds unnecessarily or shut down accounts without notice.\n\nI’m open to hearing about **any reliable options**, whether they are traditional payment processors, blockchain-based platforms, or other innovative solutions.\n\n**Please help!** Any advice would mean the world to me right now.\n\nThank you in advance for your suggestions!",
          "subreddit_subscribers": 1944498
        }
      },
      {
        "json": {
          "url": "https://www.reddit.com/r/smallbusiness/comments/1ibkmzd/business_number_being_used_to_spam_call_people/",
          "date": "2025-01-28T05:28:30.000+08:00",
          "output": "yes",
          "upvotes": "7",
          "postcontent": "So I just got off the phone with the umpteenth person who has gotten a spam call from someone spoofing with our business number, and I’m just waiting for the day that we start getting negative reviews based on this.\n\nWe’ve gotten angry calls from people for a number of scams, and apparently it’s repeated calls to them.\n\nI feel bad, cos those calls make me mad too, but I get tired of getting cussed out several times a week, and having to explain what spam calls are. I haven’t found any solutions online that look like they’d actually solve the problem.\n\nDoes anyone else get this with their business numbers?",
          "subreddit_subscribers": 1944498
        }
      },
      {
        "json": {
          "url": "https://www.reddit.com/r/smallbusiness/comments/1i43orw/im_a_small_business_owner_which_software_should_i/",
          "date": "2025-01-18T17:06:49.000+08:00",
          "output": "yes",
          "upvotes": "38",
          "postcontent": "I generate about $100k in annual revenue and don’t have payroll. What software would you recommend, and why? Currently, I create invoices using Excel, but I’m looking for a more efficient solution to send invoices and receive payments seamlessly.\n\nAlso, is there a fee every time I receive a payment? For example, if I receive $20k, $10k, $30k, or $40k?",
          "subreddit_subscribers": 1944498
        }
      },
      {
        "json": {
          "url": "https://www.reddit.com/r/smallbusiness/comments/1i1euah/small_business_automation_can_someone_help_me/",
          "date": "2025-01-15T03:54:19.000+08:00",
          "output": "yes",
          "upvotes": "3",
          "postcontent": "So I am looking for ways to bring some automations to my business by leveraging the technology available and I started with programing a smart chat bot for my website that literally is an agent who knows everything about my company which is nice when I am not around.  Then I took it further and thought that I could make automated virtual receptionist for my company which I did which makes life better because when I am on a job I miss probably a few calls a day and then when I try to reach them back, they usually have already started to talk to other competitors and then it gets challenging from there.  So this has been my solution and now I never miss a call and started building automations to even sell for me on my products and services that I offer and now even can send a booking link to them by text and email and this has allowed me to convert better and not miss an opportunity that comes my way.  I say all this because I created another on that is used strictly to role play with and I need testers to help me refine and debug it.  Essentially I just need other business owners to role play with my agent and provide any feedback that would make it better or enhance it.  \n\nIf you're willing to help me test it just call 1-855-449-7005.  Thanks in advance to anyone who tries it out!            ",
          "subreddit_subscribers": 1944498
        }
      },
      {
        "json": {
          "url": "https://www.reddit.com/r/smallbusiness/comments/1hzlhcg/customer_emailcommunication_tracker/",
          "date": "2025-01-12T20:17:33.000+08:00",
          "output": "yes",
          "upvotes": "3",
          "postcontent": "What system do you use for customer communication?\n\nLooking for recommendations on CSR communication. I have a retail store with one full time retail manager and a handful of seasonal and part time associates. \n\nWebsite inquiries for retail are routed to a generic email of which all associates can respond. The goal was that with a generic email (accessed from one terminal plus an iPad) customers would get responded to quickly but Mozilla Thunderbird’s interface is clunky and associates never remember to “file” completed conversations. \n\nI am frugal (hence one email address) but am willing to invest in a solution that can better track inquiries (only a handful a week) to provide a better experience. Just curious what you might use that works well. ",
          "subreddit_subscribers": 1944498
        }
      },
      {
        "json": {
          "url": "https://www.reddit.com/r/smallbusiness/comments/1hyzgts/had_a_customer_fire_themselves_and_it_felt_good/",
          "date": "2025-01-12T00:24:35.000+08:00",
          "output": "yes",
          "upvotes": "57",
          "postcontent": "My work had a newer customer that we were happy to have because we knew they were working with our competition. We did some work for them and they would blame us for their problems. We would offer solutions and never hear back and to top it off they paid late. I also met the owner at a trade show and he treated me like I wasn't even there when I went to say thank you. He just looked at me blankly and ignored me. So we stopped calling.\n\nThen a half year later they send some work in. I quoted it extremely high. They asked for a price discount so they could get the job for their customer. I went down 10% knowing it was still high. Then the owner emailed back about his 25 year relationship with our competitor and how they would do it at half the price. \n\nI felt happy wasting their time and money. Also, if our competitor is so great, why did they start sending us work? \n\nI'm glad we won't hear from them. I have many other customers that are fantastic to work with and pay on time. ",
          "subreddit_subscribers": 1944498
        }
      },
      {
        "json": {
          "url": "https://www.reddit.com/r/smallbusiness/comments/1hnqv0q/attention_business_owners_using_benchco/",
          "date": "2024-12-28T06:31:18.000+08:00",
          "output": "yes",
          "upvotes": "8",
          "postcontent": "You may have seen in your email that [Bench.co](http://Bench.co) is closing its doors for bookkeeping services. They are giving business owners until **March 7th, 2025**, at **5 PM** ET to download their financial data.\n\nDon't wait until the last minute! This is absolutely critical - your financial data is too important to risk losing. The timing couldn't be worse in the middle of the holidays and so close to year-end... and the lack of advance warning is frustrating.\n\nI know this situation will leave many business owners scrambling for a new bookkeeping solution. But don’t stress—there are excellent alternatives out there that can serve you even better!\n\nI primarily wanted to make this post to alert people of the closure (in case you missed the email) and encourage everyone to secure their data ASAP. If you're looking for a reliable path forward, I'd recommend exploring smaller firms or individual remote bookkeepers. Many offer highly personalized services at a wide range of prices - with services often far better quality than Bench.\n\nI'm not here to promote my business, but if you're feeling overwhelmed or don't know where to start, I'm happy to chat and share advice based on my experience running a remote bookkeeping and accounting firm. At the end of the day, I hope all Bench clients find a bookkeeping service that's a better fit: personalized, reliable, and capable of supporting your business long-term.\n\n  \nTo add a question and make sure I'm following the sub rules: \n\nWhat are you currently doing for your bookkeeping and accounting? How did you find that solution and what do you wish was different about it?",
          "subreddit_subscribers": 1944498
        }
      }
    ],
    "Merge 3 Inputs": [
      {
        "json": {
          "url": "https://www.reddit.com/r/smallbusiness/comments/1iqletb/need_help_and_advice_for_a_business_name_idea/",
          "date": "2025-02-16T13:42:12.000+08:00",
          "index": 0,
          "output": "yes",
          "message": {
            "role": "assistant",
            "content": "**Business Idea: Name Generation and Branding Consulting Service**\n\n**Description:**\n\nCreate a consulting service specializing in business name generation and branding strategies for startups and small businesses, particularly in regulated industries like accounting, finance, and legal services. The service would utilize a combination of creative brainstorming sessions, market research, and trademark checks to ensure potential business names are not only unique and relevant but also resonate with target audiences.\n\nThe service can offer tiered packages, including:\n\n1. **Name Generation**: A dedicated session where clients brainstorm multiple name ideas, with a focus on industry relevance and ease of pronunciation.\n   \n2. **Market Research**: Analyze competitors and market trends to help clients select names that stand out.\n\n3. **Trademark and Domain Availability Check**: A comprehensive report on the availability of suggested names for trademarks and associated domain names to ensure legal compliance and digital presence.\n\n4. **Brand Strategy Development**: Optional services where you assist clients in developing a full branding strategy, including logo design, color palettes, and marketing messaging based on their selected name.\n\nBy offering this service, you can address the common challenge of finding a suitable and unique business name, while also providing valuable insights into branding that will grow as the client's business evolves, ensuring they don't face the same issue in the future.",
            "refusal": null
          },
          "upvotes": "4",
          "logprobs": null,
          "response": {
            "text": "A couple is starting an accounting business focused on tax services and plans to expand into wealth management and capital advising. They initially considered the name \"Global Solutions,\" but it's already taken. They seek unique, professional, and easy-to-pronounce name suggestions that are similar to \"Global Solutions\" to avoid future name changes. They appreciate any help and plan to discuss the suggestions together."
          },
          "postcontent": "Hello guys,\n\nMy partner and I are planning to open an accounting business that will focus on tax services such as filling taxes and tax advisor and we have plan for future to add wealth management and capital advising. Initially, we were thinking of using the name \"Global Solutions,\" but we found out that another company already has it, so we can’t use it.\n\nWe’re looking for a professional name that’s easy to pronounce and somewhat similar to \"Global Solutions.\" Also, unique enough that we won’t want to change it in the future. Any ideas or suggestions would be greatly appreciated! We would love to list all name suggestions to share with my partner so we can pick the best one.\n\nThanks in advance for your help! Appreciate it! ",
          "finish_reason": "stop",
          "subreddit_subscribers": 1944498
        }
      },
      {
        "json": {
          "url": "https://www.reddit.com/r/smallbusiness/comments/1iob5ez/business_acquisition_loan_what_are_my_odds_what/",
          "date": "2025-02-13T12:34:29.000+08:00",
          "index": 0,
          "output": "yes",
          "message": {
            "role": "assistant",
            "content": "**Business Idea: Financial Advisory and Structuring Service for Business Acquisitions**\n\n**Description:**\n\nCreate a financial advisory firm specializing in helping aspiring entrepreneurs and prospective buyers navigate the complexities of purchasing existing businesses, particularly those with seller financing options. This service would focus on individuals who may not have traditional funding routes available due to factors like low equity or limited industry experience.\n\n**Key Offerings:**\n\n1. **Loan Application Assistance:**\n   - Guide clients through the SBA 7(a) loan application process, including the nuances of seller financing and the potential for using standby notes.\n   - Help develop customized financing strategies tailored to each client’s unique situation.\n\n2. **Financial Structuring:**\n   - Assist in structuring financing deals that maximize seller financing and minimize upfront equity injections.\n   - Provide creative solutions for negotiating terms with sellers to facilitate smoother transactions.\n\n3. **Business Valuation and Due Diligence Support:**\n   - Offer expertise in conducting business valuations to ensure clients understand the worth of the business they are purchasing.\n   - Help perform due diligence to uncover any potential risks or hidden costs in the acquisition.\n\n4. **Training and Support for Transitioning Owners:**\n   - Provide training resources and integration plans for new owners into the business to ensure smooth day-to-day operations post-acquisition.\n   - Connect clients with mentorship programs or industry networks for ongoing support.\n\n5. **Additional Funding Solutions:**\n   - Explore non-traditional funding sources, including microloans, community funding initiatives, or partnership arrangements that suit clients' needs for startup costs.\n\n6. **Community and Networking Events:**\n   - Organize workshops and networking events that connect buyers, sellers, and financing institutions to foster community support and share experiences.\n\nBy addressing these specific needs, your service could significantly reduce the barriers to business acquisition for aspiring entrepreneurs, allowing more people to realize their dreams of ownership, as well as helping existing business owners find trustworthy successors. This not only benefits the buyers but also strengthens local economies by ensuring businesses remain operational and thriving.",
            "refusal": null
          },
          "upvotes": "3",
          "logprobs": null,
          "response": {
            "text": "A long-time friend is offering to sell their local business, which has been profitable for 12 years (grossing $950k last year with a $325k Seller's Discretionary Earnings). The business is priced at $650k, and the seller is open to financing up to 61.5% of the purchase price. The buyer has good credit and equity in their home but limited cash for a down payment (only 5% available, preferring 0%). They lack direct industry experience but have management experience and training will be provided by the seller. They are exploring loan options, including the potential for an SBA 7(a) loan and the possibility of seller financing for a portion of the purchase. The buyer is open to various financing solutions due to their trust in the sellers and the appealing nature of the business opportunity."
          },
          "postcontent": "Hello!  \nLongtime friends have offered to sell my their local biz.    \n12 years running, last year did 950k gross, 325K SDE.  \nYOY growth has been good.  \n650k price.  \nThey have offered to seller finance up to 61.5% of the purchase price so far.  \nThey might go even higher on the seller financing if I ask.\n\n**The good (about me):**  \n  \n\\- I have good credit, probably 720+.  \n\\- I do have \\~200k equity in my home, I'm willing to collateralize.  \n  \n**The ugly (about me):**  \n  \n\\- I have only 5% down possible for equity injection, but would prefer 0%  \nI read that with a SBA 7(a) loan the seller can do 5% of my equity injection with a standby note (deferred payment until SBA loan is paid off).  I'm not sure if that could be done in tandem with another (much larger) note that would be payable (in payments) at closing.  \n  \n\\- I've had no / negative income the last couple of years.  I took some time off from my 20+ year profession, lived off of savings and some credit while I explored other career paths because I needed a change.  I did learn a couple of high value trades, and did incur some expenses in that process.\n\n\\- No direct industry experience.  I do have much professional experience I bring to the table, but not in this industry.  I have managed people on my team... but not employees.  \n\n**The rest:**  \n  \nThey are willing to hire me as store manager now, if that helps.    \nThey will be providing complete training and ongoing support.  \nIt is a simple business, really.  \nThey obviously believe in their business, given the willingness to seller finance so much of it.  \n  \nWhat are the odds I could get a SBA 7(a) loan with 5% down?  \nAre there any loans with 0% down?  \n  \nI would like to get an extra 50k or so for startup costs - it is an acquisition however I'm going to have startup expenses like first and last months lease payments, jurisdictional inspections, electricity deposit, liability insurance / workman's comp, that sort of stuff.\n\nI realize the scenario is not ideal, however it seems to me there should be SOME option out there given that all I have to do is not mess up the business!  It's a great business, well loved in the community.  \nThere is good room in the revenue for me to make accelerated loan repayments, establish business savings, grow the business, and even pay myself enough to cover my living expenses.  That is one heck of a deal, I have to find some way to pull this off!\n\nI'm willing to look at less fantastic loan offers with higher rates.    \nIt really seems to me that some entity would be willing to lend based on the cashflow / success / stability of the existing business.\n\nOne idea I had - if sellers would be willing to carry 100% for 12-24 months, would I then likely have an easier time qualifying for a SBA 7(a) loan to pay off their note, or part of it (depending on what they want)?\n\nAnother idea - store manager -&gt; partner -&gt; partner buyout  \nI do need to find out their maximum timeline for getting out.  \n  \nHad I known a couple of years ago this was going to come up, I would have made different decisions!  \nI really don't want to sell my house and rent something in order to do this, but I'm considering that as a last resort.  \nIf these weren't my longtime friends whom I trust with my life, I wouldn't consider this.  I'd be too chicken.  This is like winning the lottery to me, frankly... I'm not the perfect buyer on paper but they really want me to have it.  They know it will be my baby, as it has been theirs.\n\nGrateful for any solutions / ideas, thank you in advance!  =D\n\n",
          "finish_reason": "stop",
          "subreddit_subscribers": 1944498
        }
      },
      {
        "json": {
          "url": "https://www.reddit.com/r/smallbusiness/comments/1ikcdi5/seeking_a_reliable_alternative_to_stripe_for/",
          "date": "2025-02-08T10:09:44.000+08:00",
          "index": 0,
          "output": "yes",
          "message": {
            "role": "assistant",
            "content": "**Business Idea: Payment Assurance & Dispute Resolution Service**\n\n**Description:**\n\nCreate a specialized payment processing platform designed specifically for service-based businesses that suffer from frequent disputes and account deactivations with traditional processors like Stripe and Square. The platform would focus on three key areas:\n\n1. **Dedicated Payment Processing**: Offer a secure and user-friendly interface for handling monthly recurring payments and invoicing. This could include features like automated invoicing, direct card entry, and easy integration with existing business systems.\n\n2. **Dispute Management Module**: Implement an innovative dispute resolution system that leverages AI and machine learning to analyze and document service delivery. This system would guide businesses in gathering comprehensive proof of service and recommend best practices to minimize chargebacks. Additionally, the platform could offer access to a team of dispute resolution specialists who can intervene on behalf of the businesses in case of disputes.\n\n3. **Client Risk Assessment and Education**: Incorporate a risk assessment feature that evaluates customer profiles for potential chargeback risks before onboarding them. This could involve verifying the legitimacy of the customer's payment method and prior transaction history. Moreover, provide educational resources on managing customer relationships, expectations, and payment disputes effectively.\n\nBy addressing the common pain points in payment processing and dispute resolution, this service would not only provide a reliable payment alternative but also empower service-based businesses to manage their payments and disputes with confidence, ultimately improving their cash flow and reducing anxiety related to chargebacks and fund holds.",
            "refusal": null
          },
          "upvotes": "3",
          "logprobs": null,
          "response": {
            "text": "A service-based business owner is seeking reliable alternatives to Stripe for handling monthly recurring credit card payments. They've faced issues with Stripe's chargeback process and had their Square account deactivated after processing only two invoices. The ideal solution should allow for invoicing and auto-charges, minimize disputes, and avoid unnecessary fund holds or account shutdowns. They are open to various payment processing options, including traditional and innovative solutions."
          },
          "postcontent": "Hi everyone,\n\nI'm looking for advice on the **best alternative to Stripe** for my service-based business. Here’s the situation:\n\n* I handle **monthly recurring payments** from customers who prefer paying by **credit card**.\n* My customers provide me with their credit card information, and I need a solution to **send invoices** or **auto-charge their cards monthly** without issues.\n\n# Problems I’ve Faced:\n\n1. **Stripe**: I’ve lost countless disputes despite providing proof of service, and I’m fed up with their **chargeback process**.\n2. **Square**: I processed just **two paid invoices totaling $180**, and they **deactivated my account**, holding my money for **90 days**!\n\nI’m desperate to find a platform that:\n\n* Allows **invoicing** and **recurring auto-charges**.\n* Has **minimal chargebacks or disputes**, or at least a fair dispute resolution process. or **BEST: no disputes at all**\n* Doesn’t hold funds unnecessarily or shut down accounts without notice.\n\nI’m open to hearing about **any reliable options**, whether they are traditional payment processors, blockchain-based platforms, or other innovative solutions.\n\n**Please help!** Any advice would mean the world to me right now.\n\nThank you in advance for your suggestions!",
          "finish_reason": "stop",
          "subreddit_subscribers": 1944498
        }
      },
      {
        "json": {
          "url": "https://www.reddit.com/r/smallbusiness/comments/1ibkmzd/business_number_being_used_to_spam_call_people/",
          "date": "2025-01-28T05:28:30.000+08:00",
          "index": 0,
          "output": "yes",
          "message": {
            "role": "assistant",
            "content": "**Business Idea: Caller ID Protection and Reputation Management Service**\n\n**Description:** Create a comprehensive service that helps businesses protect their caller ID and manage their reputation against spoofing and spam calls. This service would offer the following features:\n\n1. **Caller ID Verification Tool:** Implement a system that allows businesses to register their numbers with a trusted network, improving their chances of being recognized as legitimate by consumers' phone carriers and reducing the chance of spoofing.\n\n2. **Monitoring and Alerts:** Offer real-time monitoring of calls made from the business’s number. Whenever a spoofed call is detected, the business is notified immediately, allowing them to take preventive action (like notifying clients or issuing public statements).\n\n3. **Reputation Management:** Provide a platform that allows businesses to respond to negative reviews or comments regarding spam calls. This can include automated responses to FAQs about spam calls, educating callers on what to do if they receive a call from a spoofed number.\n\n4. **Customer Education Campaigns:** Develop educational materials and campaigns that businesses can share with their customers. This includes tips on identifying spoofed calls and reassurances that their actual business numbers are legitimate and safe to call.\n\n5. **Legal Support:** Offer guidance or access to legal support for businesses that are facing significant issues due to spoofing, helping them take action against malicious actors.\n\nThis service would not only alleviate the stress faced by businesses dealing with spoofing but also help improve their brand reputation and customer trust.",
            "refusal": null
          },
          "upvotes": "7",
          "logprobs": null,
          "response": {
            "text": "The author expresses frustration over receiving multiple angry calls from people who are being spammed by scammers using their business phone number. They worry about potential negative reviews and have not found effective solutions to the issue. The author seeks input from others who may experience similar problems with their business numbers."
          },
          "postcontent": "So I just got off the phone with the umpteenth person who has gotten a spam call from someone spoofing with our business number, and I’m just waiting for the day that we start getting negative reviews based on this.\n\nWe’ve gotten angry calls from people for a number of scams, and apparently it’s repeated calls to them.\n\nI feel bad, cos those calls make me mad too, but I get tired of getting cussed out several times a week, and having to explain what spam calls are. I haven’t found any solutions online that look like they’d actually solve the problem.\n\nDoes anyone else get this with their business numbers?",
          "finish_reason": "stop",
          "subreddit_subscribers": 1944498
        }
      },
      {
        "json": {
          "url": "https://www.reddit.com/r/smallbusiness/comments/1i43orw/im_a_small_business_owner_which_software_should_i/",
          "date": "2025-01-18T17:06:49.000+08:00",
          "index": 0,
          "output": "yes",
          "message": {
            "role": "assistant",
            "content": "**Business Idea: Simplified Invoicing and Payment Management SaaS**\n\n**Description**: Develop a cloud-based invoicing and payment management software tailored for small businesses generating modest annual revenues (e.g., under $500k). The platform would enable users to create, send, and manage invoices seamlessly, integrating payment processing to facilitate immediate payments. Key features would include:\n\n1. **Template-Based Invoicing**: User-friendly templates to create professional invoices without the complexity of spreadsheets.\n  \n2. **Integrated Payment Solutions**: Collaboration with payment processing providers to offer various payment methods (credit/debit cards, bank transfers) with transparent fee structures, ensuring users understand costs per transaction.\n\n3. **Automated Reminders**: Send automatic reminders for overdue invoices, reducing the need for follow-up communication.\n\n4. **Reporting Dashboard**: Real-time analytics to track income, outstanding invoices, and payment histories, helping users manage cash flow effectively.\n\n5. **Affordable Pricing Model**: A tiered subscription model with a low monthly fee, avoiding a pay-per-transaction fee structure, which would make managing costs easier for users.\n\nBy focusing on small businesses that currently rely on Excel or less efficient methods for invoicing, this service would cater to their need for efficiency, clarity in payment processing, and ultimately help improve their cash flow management.",
            "refusal": null
          },
          "upvotes": "38",
          "logprobs": null,
          "response": {
            "text": "The user generates approximately $100,000 in annual revenue without payroll and currently uses Excel for invoicing. They seek recommendations for more efficient invoicing and payment solutions and inquire about potential fees associated with receiving payments of varying amounts."
          },
          "postcontent": "I generate about $100k in annual revenue and don’t have payroll. What software would you recommend, and why? Currently, I create invoices using Excel, but I’m looking for a more efficient solution to send invoices and receive payments seamlessly.\n\nAlso, is there a fee every time I receive a payment? For example, if I receive $20k, $10k, $30k, or $40k?",
          "finish_reason": "stop",
          "subreddit_subscribers": 1944498
        }
      },
      {
        "json": {
          "url": "https://www.reddit.com/r/smallbusiness/comments/1i1euah/small_business_automation_can_someone_help_me/",
          "date": "2025-01-15T03:54:19.000+08:00",
          "index": 0,
          "output": "yes",
          "message": {
            "role": "assistant",
            "content": "**Business Idea: Comprehensive Virtual Receptionist and Automation Service**\n\n**Description:**\n\nCreate a subscription-based service that offers businesses a fully customizable virtual receptionist and automations platform tailored to their specific needs. This service would integrate an intelligent chatbot capable of handling customer inquiries, booking appointments, and providing information about products and services. \n\n**Key Features:**\n\n1. **Custom Chatbots:** Develop AI-driven chatbots that can be tailored to individual business needs, trained on specific FAQs, and able to engage with clients when human agents are unavailable.\n\n2. **Call Handling Automation:** Implement an automated call routing system that ensures every incoming call is answered or redirected efficiently, minimizing missed opportunities.\n\n3. **Booking and Scheduling Integration:** Provide integrated booking calendars that allow customers to book appointments directly through chat or voice interactions, synchronizing with the business owner's calendar to prevent double bookings.\n\n4. **Lead Capture and Follow-Up:** Automate lead capture through various channels and set up follow-up sequences, ensuring that potential customers are nurtured and converting effectively.\n\n5. **Testing and Feedback Loop:** Offer a beta version for a limited number of businesses to test the service and provide feedback, continuously refining and enhancing the platform based on user experiences.\n\n6. **Analytics Dashboard:** Provide users with insights into customer interactions, response rates, and booking conversions to help them optimize their communication strategies.\n\nThis service would not only help businesses avoid missed opportunities but also streamline their operations, allowing owners to focus on delivering services rather than managing communication.",
            "refusal": null
          },
          "upvotes": "3",
          "logprobs": null,
          "response": {
            "text": "The author is seeking to enhance their business through automation by developing a smart chatbot and a virtual receptionist for their website, which helps manage missed calls and improve customer conversion. They mention that these tools allow for better communication and efficiency while they are busy. Additionally, they are looking for business owners to test and provide feedback on a new role-playing chatbot designed to further refine its capabilities. Interested testers can reach out at the provided phone number."
          },
          "postcontent": "So I am looking for ways to bring some automations to my business by leveraging the technology available and I started with programing a smart chat bot for my website that literally is an agent who knows everything about my company which is nice when I am not around.  Then I took it further and thought that I could make automated virtual receptionist for my company which I did which makes life better because when I am on a job I miss probably a few calls a day and then when I try to reach them back, they usually have already started to talk to other competitors and then it gets challenging from there.  So this has been my solution and now I never miss a call and started building automations to even sell for me on my products and services that I offer and now even can send a booking link to them by text and email and this has allowed me to convert better and not miss an opportunity that comes my way.  I say all this because I created another on that is used strictly to role play with and I need testers to help me refine and debug it.  Essentially I just need other business owners to role play with my agent and provide any feedback that would make it better or enhance it.  \n\nIf you're willing to help me test it just call 1-855-449-7005.  Thanks in advance to anyone who tries it out!            ",
          "finish_reason": "stop",
          "subreddit_subscribers": 1944498
        }
      },
      {
        "json": {
          "url": "https://www.reddit.com/r/smallbusiness/comments/1hzlhcg/customer_emailcommunication_tracker/",
          "date": "2025-01-12T20:17:33.000+08:00",
          "index": 0,
          "output": "yes",
          "message": {
            "role": "assistant",
            "content": "**Business Idea: Unified Customer Communication Dashboard**\n\n**Description:**\nCreate a cloud-based customer communication platform specifically designed for small to medium retail businesses. The Unified Customer Communication Dashboard would streamline all inquiries from various channels (email, social media, website chat, etc.) into a single, user-friendly interface. Key features would include:\n\n1. **Centralized Inboxes**: Consolidate all customer messages into one inbox for associates to manage, reducing the need for a generic email.\n\n2. **Conversation Tracking**: Automatically log all customer interactions and categorize them based on status (new, in-progress, completed) to ensure no inquiry goes unanswered.\n\n3. **Task Management**: Include a simple task assignment feature where messages can be assigned to specific associates, allowing for better accountability and follow-up.\n\n4. **Response Templates**: Provide customizable templates for common inquiries, making response times faster while ensuring consistency in communication.\n\n5. **Analytics Dashboard**: Offer insights and reporting tools on response times, common inquiries, and associate performance to help businesses improve their customer service strategies.\n\n6. **Affordable Subscription Model**: Implement a tiered subscription pricing model to suit different budgets, allowing businesses to pay only for what they need.\n\nThis service would not only address the current issues faced by the Reddit user but also attract other similar businesses looking for a more efficient way to manage customer communications.",
            "refusal": null
          },
          "upvotes": "3",
          "logprobs": null,
          "response": {
            "text": "A retail store owner seeks recommendations for a more effective customer communication system, currently using a generic email for inquiries. The existing method via Mozilla Thunderbird is inefficient, with associates struggling to organize completed conversations. Although the owner is frugal, they are open to investing in a solution to better track inquiries and enhance customer experience."
          },
          "postcontent": "What system do you use for customer communication?\n\nLooking for recommendations on CSR communication. I have a retail store with one full time retail manager and a handful of seasonal and part time associates. \n\nWebsite inquiries for retail are routed to a generic email of which all associates can respond. The goal was that with a generic email (accessed from one terminal plus an iPad) customers would get responded to quickly but Mozilla Thunderbird’s interface is clunky and associates never remember to “file” completed conversations. \n\nI am frugal (hence one email address) but am willing to invest in a solution that can better track inquiries (only a handful a week) to provide a better experience. Just curious what you might use that works well. ",
          "finish_reason": "stop",
          "subreddit_subscribers": 1944498
        }
      },
      {
        "json": {
          "url": "https://www.reddit.com/r/smallbusiness/comments/1hyzgts/had_a_customer_fire_themselves_and_it_felt_good/",
          "date": "2025-01-12T00:24:35.000+08:00",
          "index": 0,
          "output": "yes",
          "message": {
            "role": "assistant",
            "content": "**Business Idea: Client Relationship Management Consultancy**\n\n**Description:** Launch a consultancy that specializes in helping businesses improve their client relationship management and communication strategies. The focus would be on educating companies about the importance of establishing clear expectations, setting boundaries, and understanding when it's time to disengage from unproductive client relationships.\n\n**Services Offered:**\n\n1. **Workshops and Training:** Conduct workshops on effective communication, negotiation skills, and identifying red flags in client relationships. Provide role-playing scenarios to help businesses practice handling difficult situations.\n\n2. **Client Assessment Tools:** Develop a proprietary assessment tool that helps companies evaluate potential clients before entering into contracts. This tool would analyze factors like payment history, communication style, and past reviews.\n\n3. **Consulting Services:** Offer one-on-one consulting to help businesses create client engagement strategies tailored to their specific needs. This would include establishing protocols for responding to problematic clients and deciding when to walk away.\n\n4. **Client Relationship Coaching:** Provide coaching sessions for business owners and their teams to build their confidence in managing difficult clients and to share strategies for fostering better client relationships.\n\n5. **Networking Systems:** Create a network for businesses to share experiences and insights about their clients, enabling collective intelligence on which clients may pose challenges.\n\nThis service would empower businesses to recognize the value of their time and resources and encourage them to focus on building relationships with clients that respect and appreciate their work.",
            "refusal": null
          },
          "upvotes": "57",
          "logprobs": null,
          "response": {
            "text": "The author had a negative experience with a new customer who previously worked with a competitor. Despite providing solutions, the customer blamed the author for their problems and consistently paid late. After a lackluster interaction at a trade show, the author stopped pursuing the customer. Later, the customer sought a price discount for new work but cited their long-term relationship with the competitor, who offered lower prices. The author felt satisfaction in the customer's frustration and is content to focus on better-paying clients."
          },
          "postcontent": "My work had a newer customer that we were happy to have because we knew they were working with our competition. We did some work for them and they would blame us for their problems. We would offer solutions and never hear back and to top it off they paid late. I also met the owner at a trade show and he treated me like I wasn't even there when I went to say thank you. He just looked at me blankly and ignored me. So we stopped calling.\n\nThen a half year later they send some work in. I quoted it extremely high. They asked for a price discount so they could get the job for their customer. I went down 10% knowing it was still high. Then the owner emailed back about his 25 year relationship with our competitor and how they would do it at half the price. \n\nI felt happy wasting their time and money. Also, if our competitor is so great, why did they start sending us work? \n\nI'm glad we won't hear from them. I have many other customers that are fantastic to work with and pay on time. ",
          "finish_reason": "stop",
          "subreddit_subscribers": 1944498
        }
      },
      {
        "json": {
          "url": "https://www.reddit.com/r/smallbusiness/comments/1hnqv0q/attention_business_owners_using_benchco/",
          "date": "2024-12-28T06:31:18.000+08:00",
          "index": 0,
          "output": "yes",
          "message": {
            "role": "assistant",
            "content": "**Business Idea: \"BookKeeper Connect\" - A Personalized Bookkeeping Transition Service**\n\n**Description:**\n\nBookKeeper Connect is a service designed to assist businesses, particularly those affected by the closure of Bench.co, in seamlessly transitioning to new bookkeeping services. This platform would serve as a one-stop-shop for businesses in need of alternative bookkeeping solutions while addressing their specific needs.\n\n**Key Features:**\n\n1. **Transition Consultation**: Personalized consultations to assess client needs, preferences, and pain points. This will help businesses understand what they should look for in a new bookkeeping service.\n\n2. **Curated Provider Directory**: A vetted list of smaller firms and individual remote bookkeepers that offer personalized services. Businesses can browse profiles, rates, and client reviews to find the best fit for them.\n\n3. **Data Migration Support**: Assistance with securely exporting and migrating financial data from Bench.co to the new provider, ensuring that no vital information is lost in the transition.\n\n4. **Training and Onboarding**: Educational resources and onboarding support for business owners and new bookkeepers, helping them to establish effective workflows and communication channels.\n\n5. **Ongoing Support**: A subscription service for ongoing support, where businesses can get expert advice or a second opinion on their new bookkeeping practices.\n\n6. **Sustainability Focus**: Promote smaller bookkeeping firms that prioritize eco-friendly practices, catering to businesses interested in sustainability.\n\n**Target Market:**\n\n- Small to medium-sized businesses, startups, and freelancers looking for reliable and personalized bookkeeping solutions after the Bench.co closure.\n\nBy addressing the immediate pain points of transitioning to new bookkeeping services, BookKeeper Connect would not only solve the frustration and uncertainty faced by these businesses but also foster long-term relationships with quality bookkeeping providers.",
            "refusal": null
          },
          "upvotes": "8",
          "logprobs": null,
          "response": {
            "text": "Bench.co is closing its bookkeeping services, giving clients until March 7, 2025, to download their financial data. Business owners are encouraged to act quickly to secure their data and explore alternative bookkeeping solutions, such as smaller firms or individual remote bookkeepers that may offer more personalized services. The author is willing to provide advice to those feeling overwhelmed by the transition. Additionally, a discussion is prompted about current bookkeeping solutions and desired improvements."
          },
          "postcontent": "You may have seen in your email that [Bench.co](http://Bench.co) is closing its doors for bookkeeping services. They are giving business owners until **March 7th, 2025**, at **5 PM** ET to download their financial data.\n\nDon't wait until the last minute! This is absolutely critical - your financial data is too important to risk losing. The timing couldn't be worse in the middle of the holidays and so close to year-end... and the lack of advance warning is frustrating.\n\nI know this situation will leave many business owners scrambling for a new bookkeeping solution. But don’t stress—there are excellent alternatives out there that can serve you even better!\n\nI primarily wanted to make this post to alert people of the closure (in case you missed the email) and encourage everyone to secure their data ASAP. If you're looking for a reliable path forward, I'd recommend exploring smaller firms or individual remote bookkeepers. Many offer highly personalized services at a wide range of prices - with services often far better quality than Bench.\n\nI'm not here to promote my business, but if you're feeling overwhelmed or don't know where to start, I'm happy to chat and share advice based on my experience running a remote bookkeeping and accounting firm. At the end of the day, I hope all Bench clients find a bookkeeping service that's a better fit: personalized, reliable, and capable of supporting your business long-term.\n\n  \nTo add a question and make sure I'm following the sub rules: \n\nWhat are you currently doing for your bookkeeping and accounting? How did you find that solution and what do you wish was different about it?",
          "finish_reason": "stop",
          "subreddit_subscribers": 1944498
        }
      }
    ]
  },
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "c78fd7b7-d3e4-48f2-9f82-81ff71ef49a7",
  "connections": {
    "Get Posts": {
      "main": [
        [
          {
            "node": "Filter Posts By Features",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Merge Input": {
      "main": [
        [
          {
            "node": "Filter Posts By Content",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Merge 3 Inputs": {
      "main": [
        [
          {
            "node": "Output The Results",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Chat Model": {
      "ai_languageModel": [
        [
          {
            "node": "Analysis Content  By AI",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Select Key Fields": {
      "main": [
        [
          {
            "node": "Merge Input",
            "type": "main",
            "index": 1
          },
          {
            "node": "Analysis Content  By AI",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Chat Model1": {
      "ai_languageModel": [
        [
          {
            "node": "Post Summarization",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Chat Model2": {
      "ai_languageModel": [
        [
          {
            "node": "Post Sentiment Analysis",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Output The Results": {
      "main": [
        []
      ]
    },
    "Post Summarization": {
      "main": [
        [
          {
            "node": "Merge 3 Inputs",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Find Proper Solutions": {
      "main": [
        [
          {
            "node": "Merge 3 Inputs",
            "type": "main",
            "index": 1
          }
        ]
      ]
    },
    "Analysis Content  By AI": {
      "main": [
        [
          {
            "node": "Merge Input",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Filter Posts By Content": {
      "main": [
        [
          {
            "node": "Post Summarization",
            "type": "main",
            "index": 0
          },
          {
            "node": "Find Proper Solutions",
            "type": "main",
            "index": 0
          },
          {
            "node": "Merge 3 Inputs",
            "type": "main",
            "index": 2
          },
          {
            "node": "Post Sentiment Analysis",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Post Sentiment Analysis": {
      "main": [
        [
          {
            "node": "Positive Posts Draft",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Neutral  Posts Draft",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Negative  Posts Draft",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Filter Posts By Features": {
      "main": [
        [
          {
            "node": "Select Key Fields",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "When clicking ‘Test workflow’": {
      "main": [
        [
          {
            "node": "Get Posts",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-915"></a>

## Template 915 - Servidor MCP para pesquisa e transcrição do YouTube

- **Nome:** Servidor MCP para pesquisa e transcrição do YouTube
- **Descrição:** Servidor MCP que permite pesquisar vídeos no YouTube, obter metadados e baixar transcrições usando serviços de scraping externos, além de consultar métricas de uso da conta.
- **Funcionalidade:** • Recepção de requisições MCP: Expõe um endpoint MCP que recebe operações de clientes compatíveis.
• Pesquisa no YouTube via scraping: Executa buscas por termos fornecidos e retorna vídeos relevantes com metadados (canal, título, URL, descrição resumida, views, likes).
• Download de transcrições: Baixa legendas em texto para uma ou mais URLs fornecidas e retorna o conteúdo principal da transcrição.
• Relatório de uso da conta: Recupera métricas mensais e limites da conta do serviço de scraping para monitoramento de custos e consumo.
• Simplificação e agregação de resultados: Extrai e formata campos relevantes dos retornos das APIs e agrega itens em uma resposta consolidada.
• Tolerância a falhas e re-tentativas: Re-tenta chamadas de transcrição quando necessário e trata respostas com número limitado de resultados.
- **Ferramentas:** • Apify: Plataforma de scraping e execução de atores usada para buscar vídeos do YouTube e baixar legendas.
• Apify API: API REST usada para executar os scrapers/atores, recuperar datasets de resultados e consultar métricas e limites da conta.
• Cliente MCP (ex.: Claude Desktop): Cliente compatível com o protocolo MCP utilizado para conectar ao servidor, enviar queries e consumir as ferramentas expostas.

## Fluxo visual

```mermaid
flowchart LR
    N1["When Executed by Another Workflow"]
    N2["Operation"]
    N3["Sticky Note"]
    N4["Sticky Note1"]
    N5["Sticky Note3"]
    N6["Youtube Transcripts"]
    N7["Youtube Search"]
    N8["Apify Youtube Search"]
    N9["Simplify Search Results"]
    N10["Apify Youtube Transcripts"]
    N11["Simplify Transcript Results"]
    N12["Aggregate Search Results"]
    N13["Aggregate Transcript Results"]
    N14["Simplify Usage Metrics"]
    N15["Get Usage Limits"]
    N16["Usage Report"]
    N17["Get Usage Metrics"]
    N18["Apify Youtube MCP Server"]
    N19["Sticky Note2"]
    N20["Sticky Note4"]

    N2 --> N8
    N2 --> N10
    N2 --> N17
    N15 --> N14
    N17 --> N15
    N8 --> N9
    N9 --> N12
    N10 --> N11
    N11 --> N13
    N1 --> N2
```

## Fluxo (.json) :

```json
{
  "meta": {
    "instanceId": "408f9fb9940c3cb18ffdef0e0150fe342d6e655c3a9fac21f0f644e8bedabcd9",
    "templateCredsSetupCompleted": true
  },
  "nodes": [
    {
      "id": "aef123fd-3481-4708-ae85-684529e4f05f",
      "name": "When Executed by Another Workflow",
      "type": "n8n-nodes-base.executeWorkflowTrigger",
      "position": [
        340,
        300
      ],
      "parameters": {
        "workflowInputs": {
          "values": [
            {
              "name": "operation"
            },
            {
              "name": "query"
            },
            {
              "name": "urls"
            }
          ]
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "d77e695b-8340-4715-9862-b6428d7d12e4",
      "name": "Operation",
      "type": "n8n-nodes-base.switch",
      "position": [
        580,
        300
      ],
      "parameters": {
        "rules": {
          "values": [
            {
              "outputKey": "Youtube Search",
              "conditions": {
                "options": {
                  "version": 2,
                  "leftValue": "",
                  "caseSensitive": true,
                  "typeValidation": "strict"
                },
                "combinator": "and",
                "conditions": [
                  {
                    "id": "81b134bc-d671-4493-b3ad-8df9be3f49a6",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $json.operation }}",
                    "rightValue": "youtube_search"
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "Youtube Transcripts",
              "conditions": {
                "options": {
                  "version": 2,
                  "leftValue": "",
                  "caseSensitive": true,
                  "typeValidation": "strict"
                },
                "combinator": "and",
                "conditions": [
                  {
                    "id": "8d57914f-6587-4fb3-88e0-aa1de6ba56c1",
                    "operator": {
                      "name": "filter.operator.equals",
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $json.operation }}",
                    "rightValue": "youtube_transcripts"
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "Usage Metrics",
              "conditions": {
                "options": {
                  "version": 2,
                  "leftValue": "",
                  "caseSensitive": true,
                  "typeValidation": "strict"
                },
                "combinator": "and",
                "conditions": [
                  {
                    "id": "7c38f238-213a-46ec-aefe-22e0bcb8dffc",
                    "operator": {
                      "name": "filter.operator.equals",
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $json.operation }}",
                    "rightValue": "usage_metrics"
                  }
                ]
              },
              "renameOutput": true
            }
          ]
        },
        "options": {}
      },
      "typeVersion": 3.2
    },
    {
      "id": "b2d3e630-9664-481e-b250-9d5a3ff065ee",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -440,
        -100
      ],
      "parameters": {
        "color": 7,
        "width": 680,
        "height": 660,
        "content": "## 1. Set up an MCP Server Trigger\n[Read more about the MCP Server Trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger)"
      },
      "typeVersion": 1
    },
    {
      "id": "6facfbdf-bc66-4652-8ae6-a1513962fe2e",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        260,
        -100
      ],
      "parameters": {
        "color": 7,
        "width": 1240,
        "height": 820,
        "content": "## 2. [APIFY.com](https://www.apify.com?fpr=414q6) for Easy Youtube Search and Transcripts\n[Sign up for Apify.com using 20JIMLEUK for 20% discount](https://www.apify.com?fpr=414q6)\n\nI've used Apify's Youtube scrapers a couple of times already and I find them quite fast and dependable for production use-cases.\nI particularly like that my workflows don't break when I inevitably hit the official Youtube rate limits which are quite low.\nFor this MCP server, I'm using the following youtube scraper for search and downloading transcripts: [https://apify.com/streamers/youtube-scraper](https://apify.com/streamers/youtube-scraper?fpr=414q6)"
      },
      "typeVersion": 1
    },
    {
      "id": "3473a800-6bdc-412d-82f2-aa5befd2dfe4",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -440,
        -220
      ],
      "parameters": {
        "color": 5,
        "width": 380,
        "height": 100,
        "content": "### Always Authenticate Your Server!\nBefore going to production, it's always advised to enable authentication on your MCP server trigger."
      },
      "typeVersion": 1
    },
    {
      "id": "adddb2c3-5823-426e-bd10-4ae2f3ed0f8c",
      "name": "Youtube Transcripts",
      "type": "@n8n/n8n-nodes-langchain.toolWorkflow",
      "position": [
        0,
        280
      ],
      "parameters": {
        "name": "youtube_transcripts",
        "workflowId": {
          "__rl": true,
          "mode": "id",
          "value": "={{ $workflow.id }}"
        },
        "description": "Fetch the transcript from a youtube video using the youtube video url.",
        "workflowInputs": {
          "value": {
            "urls": "={{ /*n8n-auto-generated-fromAI-override*/ $fromAI('urls', ``, 'string') }}",
            "query": "null",
            "operation": "youtube_transcripts"
          },
          "schema": [
            {
              "id": "operation",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "operation",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "query",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "query",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "urls",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "urls",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            }
          ],
          "mappingMode": "defineBelow",
          "matchingColumns": [],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "bce90f0f-a0d8-4e43-98f2-70426b28759d",
      "name": "Youtube Search",
      "type": "@n8n/n8n-nodes-langchain.toolWorkflow",
      "position": [
        -280,
        280
      ],
      "parameters": {
        "name": "websearch_contents",
        "workflowId": {
          "__rl": true,
          "mode": "id",
          "value": "={{ $workflow.id }}"
        },
        "description": "Performs a youtube search and retrieves relevant videos with metadata only.",
        "workflowInputs": {
          "value": {
            "urls": "null",
            "query": "={{ /*n8n-auto-generated-fromAI-override*/ $fromAI('query', ``, 'string') }}",
            "operation": "youtube_search"
          },
          "schema": [
            {
              "id": "operation",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "operation",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "query",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "query",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "urls",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "urls",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            }
          ],
          "mappingMode": "defineBelow",
          "matchingColumns": [],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "42cb7bd5-bdb4-40d4-9f69-d49fe066aaa2",
      "name": "Apify Youtube Search",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        860,
        100
      ],
      "parameters": {
        "url": "https://api.apify.com/v2/acts/streamers~youtube-scraper/run-sync-get-dataset-items",
        "options": {},
        "jsonBody": "={{\n{\n  \"searchQueries\": [$json.query],\n  \"maxResultStreams\": 0,\n  \"maxResults\": 5\n}\n}}",
        "sendBody": true,
        "specifyBody": "json",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth"
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "SV9BDKc1cRbZBeoL",
          "name": "Apify.com (personal token)"
        }
      },
      "executeOnce": true,
      "typeVersion": 4.2
    },
    {
      "id": "ea57908b-f927-466c-86ff-2265a5ee001a",
      "name": "Simplify Search Results",
      "type": "n8n-nodes-base.set",
      "position": [
        1060,
        100
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "9d1db837-e256-4124-80d1-8b103dbbefbb",
              "name": "channelName",
              "type": "string",
              "value": "={{ $json.channelName }}"
            },
            {
              "id": "94cebccb-b499-4fab-a1ff-187179dcd5ce",
              "name": "title",
              "type": "string",
              "value": "={{ $json.title }}"
            },
            {
              "id": "cc68698a-221a-49b8-a349-d16ad4fa746c",
              "name": "url",
              "type": "string",
              "value": "={{ $json.url }}"
            },
            {
              "id": "de8ae3e0-685d-4e40-839f-13c798d4e5e2",
              "name": "description",
              "type": "string",
              "value": "={{ $json.text.substr(0,2_000) }}"
            },
            {
              "id": "e933cbca-486c-45c9-8ed0-89a3d1efe003",
              "name": "viewCount",
              "type": "number",
              "value": "={{ $json.viewCount }}"
            },
            {
              "id": "417846bb-5e8c-42af-b1dc-8b1de9fa426c",
              "name": "likes",
              "type": "number",
              "value": "={{ $json.likes }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "aed4a7c8-f41e-4e14-90c9-4e298465e7f4",
      "name": "Apify Youtube Transcripts",
      "type": "n8n-nodes-base.httpRequest",
      "maxTries": 2,
      "position": [
        860,
        300
      ],
      "parameters": {
        "url": "https://api.apify.com/v2/acts/streamers~youtube-scraper/run-sync-get-dataset-items",
        "options": {},
        "jsonBody": "={{\n{\n  \"downloadSubtitles\": true,\n  \"hasCC\": false,\n  \"hasLocation\": false,\n  \"hasSubtitles\": false,\n  \"is360\": false,\n  \"is3D\": false,\n  \"is4K\": false,\n  \"isBought\": false,\n  \"isHD\": false,\n  \"isHDR\": false,\n  \"isLive\": false,\n  \"isVR180\": false,\n  \"maxResultStreams\": 0,\n  \"maxResults\": 1,\n  \"maxResultsShorts\": 0,\n  \"preferAutoGeneratedSubtitles\": false,\n  \"saveSubsToKVS\": false,\n  \"startUrls\": $json.urls.split(',').map(url => ({\n    \"url\": url,\n    \"method\": \"GET\"\n  })),\n  \"subtitlesFormat\": \"plaintext\",\n  \"subtitlesLanguage\": \"en\"\n}\n}}",
        "sendBody": true,
        "specifyBody": "json",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth"
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "SV9BDKc1cRbZBeoL",
          "name": "Apify.com (personal token)"
        }
      },
      "retryOnFail": true,
      "typeVersion": 4.2,
      "waitBetweenTries": 5000
    },
    {
      "id": "a73c672c-c36a-4ac0-bb0f-a87ed4dd9329",
      "name": "Simplify Transcript Results",
      "type": "n8n-nodes-base.set",
      "position": [
        1060,
        300
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "94cebccb-b499-4fab-a1ff-187179dcd5ce",
              "name": "title",
              "type": "string",
              "value": "={{ $json.title }}"
            },
            {
              "id": "cc68698a-221a-49b8-a349-d16ad4fa746c",
              "name": "url",
              "type": "string",
              "value": "={{ $json.url }}"
            },
            {
              "id": "7501fe60-f43d-42fe-9087-6f70a1cf12af",
              "name": "transcript",
              "type": "string",
              "value": "={{ $json.subtitles[0].plaintext }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "c62ef6f9-6a81-4f00-aa68-433e3378e6ff",
      "name": "Aggregate Search Results",
      "type": "n8n-nodes-base.aggregate",
      "position": [
        1260,
        100
      ],
      "parameters": {
        "options": {},
        "aggregate": "aggregateAllItemData",
        "destinationFieldName": "response"
      },
      "typeVersion": 1
    },
    {
      "id": "53f6c967-bca1-4322-9939-7e0078ef99ed",
      "name": "Aggregate Transcript Results",
      "type": "n8n-nodes-base.aggregate",
      "position": [
        1260,
        300
      ],
      "parameters": {
        "options": {},
        "aggregate": "aggregateAllItemData",
        "destinationFieldName": "response"
      },
      "typeVersion": 1
    },
    {
      "id": "04590cf0-38e5-4113-abb8-14c141524b1c",
      "name": "Simplify Usage Metrics",
      "type": "n8n-nodes-base.set",
      "position": [
        1260,
        500
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "ff43aa98-4e32-478d-9e43-619b7b808948",
              "name": "monthlyUsageCycle_startAt",
              "type": "string",
              "value": "={{ $json.data.monthlyUsageCycle.startAt }}"
            },
            {
              "id": "145eefd3-5248-40e9-a988-9e0e578d930a",
              "name": "monthlyUsageCycle_endAt",
              "type": "string",
              "value": "={{ $json.data.monthlyUsageCycle.endAt }}"
            },
            {
              "id": "020d1e4f-d7ec-4d69-b9be-b6c4ba5971eb",
              "name": "monthlyUsageUsd",
              "type": "string",
              "value": "={{ $json.data.current.monthlyUsageUsd.toFixed(2) }} of {{ $json.data.limits.maxMonthlyUsageUsd.toFixed(2) }}"
            },
            {
              "id": "112fb245-b35b-45ce-ad29-e05d0f352010",
              "name": "ACTOR_COMPUTE_UNITS",
              "type": "number",
              "value": "={{ $('Get Usage Metrics').item.json.data.monthlyServiceUsage.ACTOR_COMPUTE_UNITS.amountAfterVolumeDiscountUsd }}"
            },
            {
              "id": "4b451afb-eba7-49c6-8c3c-7279fb315ec6",
              "name": "DATASET_READS",
              "type": "number",
              "value": "={{ $('Get Usage Metrics').item.json.data.monthlyServiceUsage.DATASET_READS.amountAfterVolumeDiscountUsd }}"
            },
            {
              "id": "c002234c-955e-41f4-a27f-7f031ae6111e",
              "name": "DATASET_TIMED_STORAGE_GBYTE_HOURS",
              "type": "number",
              "value": "={{ $('Get Usage Metrics').item.json.data.monthlyServiceUsage.DATASET_TIMED_STORAGE_GBYTE_HOURS.amountAfterVolumeDiscountUsd }}"
            },
            {
              "id": "0108085d-1bb4-44c5-bc3b-845a7206abfe",
              "name": "DATASET_WRITES",
              "type": "number",
              "value": "={{ $('Get Usage Metrics').item.json.data.monthlyServiceUsage.DATASET_WRITES.amountAfterVolumeDiscountUsd }}"
            },
            {
              "id": "df993499-7410-450c-b5b1-50052e6d061e",
              "name": "DATA_TRANSFER_EXTERNAL_GBYTES",
              "type": "number",
              "value": "={{ $('Get Usage Metrics').item.json.data.monthlyServiceUsage.DATA_TRANSFER_EXTERNAL_GBYTES.amountAfterVolumeDiscountUsd }}"
            },
            {
              "id": "1627a2dd-15a6-4b69-b480-4e1b792c403d",
              "name": "DATA_TRANSFER_INTERNAL_GBYTES",
              "type": "number",
              "value": "={{ $('Get Usage Metrics').item.json.data.monthlyServiceUsage.DATA_TRANSFER_INTERNAL_GBYTES.amountAfterVolumeDiscountUsd }}"
            },
            {
              "id": "73037e97-e43d-4ecd-bb7e-6c5ce4740e4d",
              "name": "KEY_VALUE_STORE_READS",
              "type": "number",
              "value": "={{ $('Get Usage Metrics').item.json.data.monthlyServiceUsage.KEY_VALUE_STORE_READS.amountAfterVolumeDiscountUsd }}"
            },
            {
              "id": "5de9ba3b-bf62-4525-9cd9-5008bafe73c5",
              "name": "KEY_VALUE_STORE_TIMED_STORAGE_GBYTE_HOURS",
              "type": "number",
              "value": "={{ $('Get Usage Metrics').item.json.data.monthlyServiceUsage.KEY_VALUE_STORE_TIMED_STORAGE_GBYTE_HOURS.amountAfterVolumeDiscountUsd }}"
            },
            {
              "id": "6d1997f2-46c0-468b-b50f-fc37512417d2",
              "name": "KEY_VALUE_STORE_WRITES",
              "type": "number",
              "value": "={{ $('Get Usage Metrics').item.json.data.monthlyServiceUsage.KEY_VALUE_STORE_WRITES.amountAfterVolumeDiscountUsd }}"
            },
            {
              "id": "b579cb9e-d18f-4877-b808-a177195a364a",
              "name": "PAID_ACTORS_PER_DATASET_ITEM",
              "type": "number",
              "value": "={{ $('Get Usage Metrics').item.json.data.monthlyServiceUsage.PAID_ACTORS_PER_DATASET_ITEM.amountAfterVolumeDiscountUsd }}"
            },
            {
              "id": "5c69831c-3c62-421d-afff-bd8cfb68fb29",
              "name": "REQUEST_QUEUE_READS",
              "type": "number",
              "value": "={{ $('Get Usage Metrics').item.json.data.monthlyServiceUsage.REQUEST_QUEUE_READS.amountAfterVolumeDiscountUsd }}"
            },
            {
              "id": "21d54d4d-515b-4fa7-b099-c8b193fc4436",
              "name": "=REQUEST_QUEUE_TIMED_STORAGE_GBYTE_HOURS",
              "type": "number",
              "value": "={{ $('Get Usage Metrics').item.json.data.monthlyServiceUsage.REQUEST_QUEUE_TIMED_STORAGE_GBYTE_HOURS.amountAfterVolumeDiscountUsd }}"
            },
            {
              "id": "68168fc6-0052-4fa6-b631-942d972af340",
              "name": "REQUEST_QUEUE_WRITES",
              "type": "number",
              "value": "={{ $('Get Usage Metrics').item.json.data.monthlyServiceUsage.REQUEST_QUEUE_WRITES.amountAfterVolumeDiscountUsd }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "dee72606-aeea-41bf-97e3-037afbd03efc",
      "name": "Get Usage Limits",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1060,
        500
      ],
      "parameters": {
        "url": "https://api.apify.com/v2/users/me/limits",
        "options": {},
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth"
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "SV9BDKc1cRbZBeoL",
          "name": "Apify.com (personal token)"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "49715bf8-56a9-41ee-a756-eb05ea4f1e7d",
      "name": "Usage Report",
      "type": "@n8n/n8n-nodes-langchain.toolWorkflow",
      "position": [
        -140,
        400
      ],
      "parameters": {
        "name": "Apfiy_Usage_Metrics",
        "workflowId": {
          "__rl": true,
          "mode": "id",
          "value": "={{ $workflow.id }}"
        },
        "description": "Returns current month's usage metrics.",
        "workflowInputs": {
          "value": {
            "urls": "null",
            "query": "null",
            "operation": "=usage_report"
          },
          "schema": [
            {
              "id": "operation",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "operation",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "query",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "query",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "urls",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "urls",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            }
          ],
          "mappingMode": "defineBelow",
          "matchingColumns": [],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "737eca46-cb1f-443f-8243-33d429f0bfe3",
      "name": "Get Usage Metrics",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        860,
        500
      ],
      "parameters": {
        "url": "https://api.apify.com/v2/users/me/usage/monthly",
        "options": {},
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth"
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "SV9BDKc1cRbZBeoL",
          "name": "Apify.com (personal token)"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "90da2c29-a1fc-4772-a271-602cdd14b679",
      "name": "Apify Youtube MCP Server",
      "type": "@n8n/n8n-nodes-langchain.mcpTrigger",
      "position": [
        -300,
        60
      ],
      "webhookId": "b975bb25-be7c-49fb-8cd2-8e135d91ed4e",
      "parameters": {
        "path": "b975bb25-be7c-49fb-8cd2-8e135d91ed4e"
      },
      "typeVersion": 1
    },
    {
      "id": "b427a01f-099d-43f8-8b8d-04186a5d330e",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -960,
        -460
      ],
      "parameters": {
        "width": 480,
        "height": 1020,
        "content": "## Try It Out!\n### This n8n demonstrates how to build a simple Youtube Search MCP server to look up videos on Youtube and download their transcripts for research purposes.\n\n### How it works\n* A MCP server trigger is used and connected to 3 custom workflow tools: Youtube Search, Youtube Transcripts and Usage Reports.\n* Both Youtube tools use an external scraping service called [APIFY.com](https://www.apify.com?fpr=414q6). This is my preference as it's a much simpler interface and there are no rate limits.  \n* The Youtube Search fetches 10 results based on the user's query.\n* The Youtube Transcripts downloads the subtitles from one or more given urls.\n* The usage reports pulls in your monthly [APIFY.com](https://www.apify.com?fpr=414q6) monthly spending and limits as a way to check your account.\n\n### How to use\n* This Apify Youtube MCP server allows any compatible MCP client to research youtube videos for any desired topic. An Apify account is required however to connect and use the service.\n* Connect your MCP client by following the n8n guidelines here - https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger/#integrating-with-claude-desktop\n* Alternatively, connect any n8n AI agent with the MCP client tool.\n* Try the following queries in your MCP client:\n  * \"what is MCP?\"\n  * \"How can I use MCP in n8n?\"\n  * \"How can I use Apify's official MCP server?\"\n\n### Requirements\n* [APIFY.com](https://www.apify.com?fpr=414q6) for Youtube Scraping. This is a paid service but there is a $5 free tier which is ample for this template.\n* MCP Client or Agent for usage such as Claude Desktop - https://claude.ai/download\n\n### Customising this workflow\n* Add as many [APIFY.com](https://www.apify.com?fpr=414q6) actors as required for your use-case or users. Consider using Apify's official MCP server for 4000+ available tools.\n* Remember to set the MCP server to require credentials before going to production and sharing this MCP server with others!"
      },
      "typeVersion": 1
    },
    {
      "id": "e11a8af0-0a53-4b9b-a499-4bbd956858f8",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        260,
        -360
      ],
      "parameters": {
        "width": 280,
        "height": 240,
        "content": "[![](https://d2gdx5nv84sdx2.cloudfront.net/uploads/35gj8m4w/marketing_asset/banner/13734/Large_rectangle_336x280_Light__1_.png)](https://www.apify.com?fpr=414q6)"
      },
      "typeVersion": 1
    }
  ],
  "pinData": {},
  "connections": {
    "Operation": {
      "main": [
        [
          {
            "node": "Apify Youtube Search",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Apify Youtube Transcripts",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Get Usage Metrics",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Usage Report": {
      "ai_tool": [
        [
          {
            "node": "Apify Youtube MCP Server",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Youtube Search": {
      "ai_tool": [
        [
          {
            "node": "Apify Youtube MCP Server",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Get Usage Limits": {
      "main": [
        [
          {
            "node": "Simplify Usage Metrics",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Usage Metrics": {
      "main": [
        [
          {
            "node": "Get Usage Limits",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Youtube Transcripts": {
      "ai_tool": [
        [
          {
            "node": "Apify Youtube MCP Server",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Apify Youtube Search": {
      "main": [
        [
          {
            "node": "Simplify Search Results",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Simplify Search Results": {
      "main": [
        [
          {
            "node": "Aggregate Search Results",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Apify Youtube Transcripts": {
      "main": [
        [
          {
            "node": "Simplify Transcript Results",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Simplify Transcript Results": {
      "main": [
        [
          {
            "node": "Aggregate Transcript Results",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "When Executed by Another Workflow": {
      "main": [
        [
          {
            "node": "Operation",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-916"></a>

## Template 916 - Busca de emails com Icypeas a partir de planilha

- **Nome:** Busca de emails com Icypeas a partir de planilha
- **Descrição:** Este fluxo lê dados de uma planilha com nomes e empresas, autentica-se no Icypeas e realiza buscas em lote de e-mails via API.
- **Funcionalidade:** • Leitura de dados da planilha: lê lastname, firstname e company de uma Google Sheet.
• Autenticação com Icypeas: conecta-se à conta usando API key, API secret e User ID.
• Busca em lote de e-mails: envia os dados para a API de bulk-search para localizar contatos.
• Geração de assinatura/segurança de API: prepara timestamp e assinatura para autenticação nas requisições.
• Disponibilização de resultados: os resultados ficam acessíveis na plataforma Icypeas e por e-mail.
- **Ferramentas:** • Google Sheets: Leitura de dados da planilha.
• Icypeas API: Serviço de busca de e-mails em lote via endpoint bulk-search.

## Fluxo visual

```mermaid
flowchart LR
    N1["When clicking 'Execute Workflow'"]
    N2["Sticky Note"]
    N3["Authenticates to your Icypeas account"]
    N4["Sticky Note1"]
    N5["Sticky Note3"]
    N6["Sticky Note4"]
    N7["Reads lastname,firstname and company from your sheet"]
    N8["Run bulk search (email-search)"]

    N1 --> N7
    N3 --> N8
    N7 --> N3
```

## Fluxo (.json) :

```json
{
  "meta": {
    "instanceId": "257476b1ef58bf3cb6a46e65fac7ee34a53a5e1a8492d5c6e4da5f87c9b82833"
  },
  "nodes": [
    {
      "id": "f5c16b6d-b7b0-4b36-9e74-795a4f486604",
      "name": "When clicking \"Execute Workflow\"",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        360,
        1700
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "0cc486d8-397f-44b1-a23b-04d0c142a48d",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        220,
        1420
      ],
      "parameters": {
        "height": 259,
        "content": "## Email search with Icypeas (bulk search)\n\n\nThis workflow demonstrates how to perform email searches (bulk search) using Icypeas. Visit https://icypeas.com to create your account."
      },
      "typeVersion": 1
    },
    {
      "id": "b932d050-4934-4f2f-a620-79f08b97c428",
      "name": "Authenticates to your Icypeas account",
      "type": "n8n-nodes-base.code",
      "position": [
        860,
        1700
      ],
      "parameters": {
        "jsCode": "const API_BASE_URL = \"https://app.icypeas.com/api\";\nconst API_PATH = \"/bulk-search\";\nconst METHOD = \"POST\";\n\n// Change here\nconst API_KEY = \"PUT_API_KEY_HERE\";\nconst API_SECRET = \"PUT_API_SECRET_HERE\";\nconst USER_ID = \"PUT_USER_ID_HERE\";\n////////////////\n\nconst genSignature = (\n    url,\n    method,\n    secret,\n    timestamp = new Date().toISOString()\n) => {\n    const Crypto = require('crypto');\n    const payload = `${method}${url}${timestamp}`.toLowerCase();\n    const sign = Crypto.createHmac(\"sha1\", secret).update(payload).digest(\"hex\");\n\n    return sign;\n};\n\nconst apiUrl = `${API_BASE_URL}${API_PATH}`;\n\nconst data = $input.all().map((x) => [x.json.firstname, x.json.lastname, x.json.company]);\n$input.first().json.data = data;\n$input.first().json.api = {\n  timestamp: new Date().toISOString(),\n  secret: API_SECRET,\n  key: API_KEY,\n  userId: USER_ID,\n  url: apiUrl,\n};\n\n$input.first().json.api.signature = genSignature(apiUrl, METHOD, API_SECRET, $input.first().json.api.timestamp);\nreturn $input.first();"
      },
      "typeVersion": 1
    },
    {
      "id": "35325df4-1d77-4200-9aca-a7f311f3857e",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        500,
        1560
      ],
      "parameters": {
        "height": 606.4963141641612,
        "content": "## Read your Google Sheet file\n\nThis node reads a Google Sheet. You need to create a sheet with :\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n**The first column** :\nHeader : lastname\n\n**The first column** :\nHeader : firstname\n\n**The first column** :\nHeader : company\n\n\nDon't forget to specify the path of your file in the node and your credentials."
      },
      "typeVersion": 1
    },
    {
      "id": "ca04cf0b-59b6-4836-902f-2e93b6cbc3f5",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        741.0092314499475,
        1458.51011235955
      ],
      "parameters": {
        "width": 392.0593078758952,
        "height": 1203.3290499048028,
        "content": "## Authenticates to your Icypeas account\n\nThis code node utilizes your API key, API secret, and User ID to establish a connection with your Icypeas account.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nOpen this node and insert your API Key, API secret, and User ID within the quotation marks. You can locate these credentials on your Icypeas profile at https://app.icypeas.com/bo/profile. Here is the extract of what you have to change :\n\nconst API_KEY = \"**PUT_API_KEY_HERE**\";\nconst API_SECRET = \"**PUT_API_SECRET_HERE**\";\nconst USER_ID = \"**PUT_USER_ID_HERE**\";\n\nDo not change any other line of the code.\n\nIf you are a self-hosted user, follow these steps to activate the crypto module :\n\n1.Access your n8n instance:\nLog in to your n8n instance using your web browser by navigating to the URL of your instance, for example: http://your-n8n-instance.com.\n\n2.Go to Settings:\nIn the top-right corner, click on your username, then select \"Settings.\"\n\n3.Select General Settings:\nIn the left menu, click on \"General.\"\n\n4.Enable the Crypto module:\nScroll down to the \"Additional Node Packages\" section. You will see an option called \"crypto\" with a checkbox next to it. Check this box to enable the Crypto module.\n\n5.Save the changes:\nAt the bottom of the page, click \"Save\" to apply the changes.\n\nOnce you've followed these steps, the Crypto module should be activated for your self-hosted n8n instance. Make sure to save your changes and optionally restart your n8n instance for the changes to take effect.\n\n\n\n\n\n"
      },
      "typeVersion": 1
    },
    {
      "id": "69e3246b-f490-43e7-94ae-566eb4faf6b9",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1133,
        1460
      ],
      "parameters": {
        "width": 328.8456933308303,
        "height": 869.114109302513,
        "content": "## Performs email searches (bulk).\n\n\nThis node executes an HTTP request (POST) to search for the email addresses.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n### You need to create credentials in the HTTP Request node :\n\n➔ In the Credential for Header Auth, click on - Create new Credential -.\n➔ In the Name section, write “Authorization”\n➔ In the Value section, select expression (located just above the field on the right when you hover on top of it) and write {{ $json.api.key + ':' + $json.api.signature }} .\n➔ Then click on “Save” to save the changes.\n\n### To retrieve the results :\n\nAfter some time, the results, which are downloadable, will be available in the Icypeas application  in this section : https://app.icypeas.com/bo/bulksearch?task=email-search, and you will receive the search results via email from no-reply@icypeas.com, providing you with the results of your search.\n\n\n\n\n"
      },
      "typeVersion": 1
    },
    {
      "id": "56abf128-57b3-4038-a262-38b09b3e3faf",
      "name": "Reads lastname,firstname and company from your sheet",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        580,
        1700
      ],
      "parameters": {
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": ""
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": ""
        }
      },
      "typeVersion": 4.1
    },
    {
      "id": "f256a8e7-c8c6-4177-810e-f7af4961db05",
      "name": "Run bulk search (email-search)",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1200,
        1700
      ],
      "parameters": {
        "url": "={{ $json.api.url }}",
        "method": "POST",
        "options": {},
        "sendBody": true,
        "sendHeaders": true,
        "authentication": "genericCredentialType",
        "bodyParameters": {
          "parameters": [
            {
              "name": "task",
              "value": "=email-search"
            },
            {
              "name": "name",
              "value": "Test"
            },
            {
              "name": "user",
              "value": "={{ $json.api.userId }}"
            },
            {
              "name": "data",
              "value": "={{ $json.data }}"
            }
          ]
        },
        "genericAuthType": "httpHeaderAuth",
        "headerParameters": {
          "parameters": [
            {
              "name": "X-ROCK-TIMESTAMP",
              "value": "={{ $json.api.timestamp }}"
            }
          ]
        }
      },
      "typeVersion": 4.1
    }
  ],
  "pinData": {},
  "connections": {
    "When clicking \"Execute Workflow\"": {
      "main": [
        [
          {
            "node": "Reads lastname,firstname and company from your sheet",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Authenticates to your Icypeas account": {
      "main": [
        [
          {
            "node": "Run bulk search (email-search)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Reads lastname,firstname and company from your sheet": {
      "main": [
        [
          {
            "node": "Authenticates to your Icypeas account",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-917"></a>

## Template 917 - Criação automática de rascunhos de resposta Fastmail

- **Nome:** Criação automática de rascunhos de resposta Fastmail
- **Descrição:** Gera rascunhos de respostas para e-mails recebidos usando IA e salva-os na conta Fastmail.
- **Funcionalidade:** • Monitoramento de e-mails: Verifica continuamente uma conta IMAP em busca de novas mensagens não lidas.
• Extração de campos do e-mail: Captura remetente, assunto, corpo e metadados relevantes do e-mail recebido.
• Geração de resposta por IA: Envia o conteúdo do e-mail para o modelo GPT-4 para redigir uma resposta apropriada e com nível de formalidade correspondente.
• Obtenção de sessão e IDs de pastas: Consulta a API do Fastmail para obter sessão e identificadores das caixas de correio.
• Identificação da pasta Rascunhos: Filtra a lista de pastas para localizar a pasta de rascunhos do usuário.
• Preparação do rascunho: Compõe o rascunho com destinatário, assunto (prefixado com "Re:"), referências e corpo gerado pela IA.
• Upload do rascunho: Envia o rascunho montado para a pasta de Rascunhos na conta Fastmail, marcando-o como rascunho.
- **Ferramentas:** • Servidor IMAP: Fonte dos e-mails recebidos que aciona o fluxo.
• OpenAI (GPT-4): Gera o texto da resposta com base no conteúdo do e-mail.
• Fastmail JMAP API: Fornece sessão, identificadores de pastas e permite criar/upload de rascunhos na conta do usuário.



## Fluxo visual

```mermaid
flowchart LR
    N1["Session"]
    N2["Get Mailbox IDs"]
    N3["Split Out"]
    N4["Email Trigger (IMAP)"]
    N5["Get fields from source email"]
    N6["OpenAI"]
    N7["Filter for drafts folder"]
    N8["upload draft email"]
    N9["gather data for draft email"]
    N10["Sticky Note"]
    N11["Sticky Note1"]

    N6 --> N1
    N1 --> N2
    N3 --> N7
    N2 --> N3
    N4 --> N5
    N7 --> N9
    N9 --> N8
    N5 --> N6
```

## Fluxo (.json) :

```json
{
  "meta": {
    "instanceId": "04ab549d8bbb435ec33b81e4e29965c46cf6f0f9e7afe631018b5e34c8eead58"
  },
  "nodes": [
    {
      "id": "082d1828-72b1-48c0-8426-c8051c29f0db",
      "name": "Session",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        -20,
        -20
      ],
      "parameters": {
        "url": "https://api.fastmail.com/jmap/session",
        "options": {},
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth"
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "3IRsYkeB2ofrwQjv",
          "name": "Fastmail"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "d7dc4c50-c8fc-4999-918d-5d357567ed14",
      "name": "Get Mailbox IDs",
      "type": "n8n-nodes-base.httpRequest",
      "notes": "https://api.fastmail.com/.well-known/jmap\n\nhttps://api.fastmail.com/jmap/session",
      "position": [
        200,
        -20
      ],
      "parameters": {
        "url": "https://api.fastmail.com/jmap/api/",
        "method": "POST",
        "options": {},
        "jsonBody": "={\n \"using\": [\"urn:ietf:params:jmap:core\", \"urn:ietf:params:jmap:mail\"],\n \"methodCalls\": [\n [\n \"Mailbox/get\",\n {\n \"accountId\": \"{{ $('Session').item.json.primaryAccounts['urn:ietf:params:jmap:mail'] }}\"\n },\n \"c0\"\n ]\n ]\n }",
        "sendBody": true,
        "sendHeaders": true,
        "specifyBody": "json",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "headerParameters": {
          "parameters": [
            {
              "name": "Content-Type",
              "value": "application/json"
            },
            {
              "name": "Accept",
              "value": "application/json"
            }
          ]
        }
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "3IRsYkeB2ofrwQjv",
          "name": "Fastmail"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "31be3c1c-f4c5-4309-92b3-2fd0a3fcecc6",
      "name": "Split Out",
      "type": "n8n-nodes-base.splitOut",
      "position": [
        400,
        -20
      ],
      "parameters": {
        "options": {},
        "fieldToSplitOut": "methodResponses[0][1].list"
      },
      "typeVersion": 1
    },
    {
      "id": "93de4dad-70d6-4e16-b351-7c540c3a4bfa",
      "name": "Email Trigger (IMAP)",
      "type": "n8n-nodes-base.emailReadImap",
      "position": [
        -20,
        -240
      ],
      "parameters": {
        "options": {
          "customEmailConfig": "[\"UNSEEN\"]"
        },
        "postProcessAction": "nothing",
        "downloadAttachments": true
      },
      "credentials": {
        "imap": {
          "id": "vFzz9hU9rTHVHs3I",
          "name": "IMAP"
        }
      },
      "typeVersion": 2
    },
    {
      "id": "41e77a60-622f-426c-a50c-e0df03c53208",
      "name": "Get fields from source email",
      "type": "n8n-nodes-base.set",
      "position": [
        200,
        -240
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "a9d425bd-e576-4e38-a251-b462240d3e2d",
              "name": "textPlain",
              "type": "string",
              "value": "={{ $json.textPlain }}"
            },
            {
              "id": "7071a252-fcad-4aa1-953f-205c3e403497",
              "name": "from",
              "type": "string",
              "value": "={{ $json.from }}"
            },
            {
              "id": "c4b0ed1b-590c-4d7f-b494-a0f34304cc1a",
              "name": "subject",
              "type": "string",
              "value": "={{ $json.subject }}"
            },
            {
              "id": "7e0badd1-02be-4149-b9ff-286f0943f051",
              "name": "metadata['message-id']",
              "type": "string",
              "value": "={{ $json.metadata['message-id'] }}"
            },
            {
              "id": "f87c7c15-c1d3-4696-bcd4-6677e5ddb240",
              "name": "metadata['reply-to']",
              "type": "string",
              "value": "={{ $json.metadata['reply-to'] }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "f9d1a529-1377-456b-8357-d37fb3fe74f9",
      "name": "OpenAI",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "position": [
        400,
        -240
      ],
      "parameters": {
        "modelId": {
          "__rl": true,
          "mode": "list",
          "value": "gpt-4o",
          "cachedResultName": "GPT-4O"
        },
        "options": {},
        "messages": {
          "values": [
            {
              "content": "=Please analyze the following personal email and draft a casual response based solely on its content. Return only the response text without any additional introductions or formatting. The response should include appropriate greetings (e.g., \"Hi\", \"Hallo\", \"Moin\" in German or \"Hi\", \"Hello\" in English) and sign-offs (e.g., \"Gruß\", \"Lieben Gruß\" in German or \"Regards\" in English). Add a thanks if appropriate. Use \"Du\" only if appropriate; if the email contains \"Sie\", maintain the same formality.\n\nSubject: {{ $json.subject }}\nEmail Content: {{ $json.textPlain }}"
            }
          ]
        }
      },
      "credentials": {
        "openAiApi": {
          "id": "iW0ItIt1ZxCQrBqk",
          "name": "OpenAI"
        }
      },
      "typeVersion": 1.5
    },
    {
      "id": "c421ddc9-b230-499c-a11d-a20a68d30c5b",
      "name": "Filter for drafts folder",
      "type": "n8n-nodes-base.filter",
      "position": [
        560,
        -20
      ],
      "parameters": {
        "options": {},
        "conditions": {
          "options": {
            "version": 2,
            "leftValue": "",
            "caseSensitive": true,
            "typeValidation": "strict"
          },
          "combinator": "and",
          "conditions": [
            {
              "id": "4e4c63d1-40fe-4314-bfe7-4fee62c78b88",
              "operator": {
                "name": "filter.operator.equals",
                "type": "string",
                "operation": "equals"
              },
              "leftValue": "={{ $json.role }}",
              "rightValue": "drafts"
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "ef19fde4-cf8c-4e19-912e-822611c18056",
      "name": "upload draft email",
      "type": "n8n-nodes-base.httpRequest",
      "notes": "https://api.fastmail.com/.well-known/jmap\n\nhttps://api.fastmail.com/jmap/session",
      "position": [
        1000,
        -120
      ],
      "parameters": {
        "url": "https://api.fastmail.com/jmap/api/",
        "method": "POST",
        "options": {},
        "jsonBody": "={\n \"using\": [\"urn:ietf:params:jmap:core\", \"urn:ietf:params:jmap:mail\"],\n \"methodCalls\": [\n [\n \"Email/set\",\n {\n \"accountId\": \"{{ $('Session').item.json.primaryAccounts['urn:ietf:params:jmap:mail'] }}\",\n \"create\": {\n \"newDraft\": {\n \"mailboxIds\": {\n \"{{ $json.draftsId }}\": true\n },\n \"keywords\": {\n \"$draft\": true\n },\n \"inReplyTo\": [\"{{ $json.metadata['message-id'] }}\"],\n \"references\": [\"{{ $json.metadata['message-id'] }}\"],\n \"from\": [{\n \"name\": \"\",\n \"email\": \"{{ $('Session').item.json.username }}\"\n }],\n \"to\": [{\n \"name\": \"{{ $json['to-friendly'] }}\",\n \"email\": \"{{ $json.to }}\"\n }],\n \"subject\": \"{{ $json.subject }}\",\n \"bodyValues\": {\n \"textBody\": {\n \"value\": \"{{ $json.message.content.replace(/\\n/g, '\\\\n') }}\"\n }\n },\n \"bodyStructure\": {\n \"partId\": \"textBody\"\n }\n }\n }\n },\n \"c1\"\n ]\n ]\n}",
        "sendBody": true,
        "sendHeaders": true,
        "specifyBody": "json",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "headerParameters": {
          "parameters": [
            {
              "name": "Content-Type",
              "value": "application/json"
            },
            {
              "name": "Accept",
              "value": "application/json"
            }
          ]
        }
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "3IRsYkeB2ofrwQjv",
          "name": "Fastmail"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "f4ecb64a-c978-4aa3-943e-c4a7f0592b91",
      "name": "gather data for draft email",
      "type": "n8n-nodes-base.set",
      "position": [
        800,
        -120
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "78885ad0-fa62-407e-82de-f297190265be",
              "name": "draftsId",
              "type": "string",
              "value": "={{ $json.id }}"
            },
            {
              "id": "fcb31dde-0881-4b98-8bc2-e3e215148a5c",
              "name": "to-friendly",
              "type": "string",
              "value": "={{ $('Get fields from source email').item.json.from.match(/[^<]+/)[0].trim().replaceAll(/\\\"/g, \"\") }}"
            },
            {
              "id": "84c80af6-68dd-44bd-97ba-fde78a42e88a",
              "name": "subject",
              "type": "string",
              "value": "=Re: {{ $('Get fields from source email').item.json.subject }}"
            },
            {
              "id": "590e9856-9c6f-4d23-af42-8a0a1384ac00",
              "name": "message.content",
              "type": "string",
              "value": "={{ $('OpenAI').item.json.message.content }}"
            },
            {
              "id": "4f24e071-24e3-4101-a423-ad5bbcca9fc7",
              "name": "metadata['message-id']",
              "type": "string",
              "value": "={{ $('Get fields from source email').item.json.metadata['message-id'] }}"
            },
            {
              "id": "80c92734-0296-4299-9f98-15cc62e93d44",
              "name": "to",
              "type": "string",
              "value": "={{ $('Get fields from source email').item.json.metadata['reply-to'].match(/<([^>]+)>/)[1] ?? $('Get fields from source email').item.json.from.match(/<([^>]+)>/)[1] }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "ca868672-85bd-4e2e-b2c6-6c6c69b78b24",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -580,
        -560
      ],
      "parameters": {
        "width": 493.9330818092735,
        "height": 695.2489786026621,
        "content": "## Workflow Description:\nThis n8n workflow automates the drafting of email replies for Fastmail using OpenAI's GPT-4 model. Here’s the overall process:\n\n1. **Email Monitoring**: The workflow continuously monitors a specified IMAP inbox for new, unread emails.\n2. **Email Data Extraction**: When a new email is detected, it extracts relevant details such as the sender, subject, email body, and metadata.\n3. **AI Response Generation**: The extracted email content is sent to OpenAI's GPT-4, which generates a personalized draft response.\n4. **Get Fastmail Session and Mailbox IDs**: Connects to the Fastmail API to retrieve necessary session details and mailbox IDs.\n5. **Draft Identification**: Identifies the \"Drafts\" folder in the mailbox.\n6. **Draft Preparation**: Compiles all the necessary information to create the draft, including the generated response, original email details, and specified recipient.\n7. **Draft Uploading**: Uploads the prepared draft email to the \"Drafts\" folder in the Fastmail mailbox."
      },
      "typeVersion": 1
    },
    {
      "id": "c4273cc2-1ac2-43f4-bcd1-7f42d3109373",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -40,
        -560
      ],
      "parameters": {
        "color": 3,
        "width": 722.928660826031,
        "height": 285.5319148936168,
        "content": "## Prerequisites:\n1. **IMAP Email Account**: You need to configure an IMAP email account in n8n to monitor incoming emails.\n2. **Fastmail API Credentials**: A Fastmail account with JMAP API enabled. You should set up HTTP Header authentication in n8n with your Fastmail API credentials.\n3. **OpenAI API Key**: An API key from OpenAI to access GPT-4. Make sure to configure the OpenAI credentials in n8n."
      },
      "typeVersion": 1
    }
  ],
  "pinData": {},
  "connections": {
    "OpenAI": {
      "main": [
        [
          {
            "node": "Session",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Session": {
      "main": [
        [
          {
            "node": "Get Mailbox IDs",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Split Out": {
      "main": [
        [
          {
            "node": "Filter for drafts folder",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Mailbox IDs": {
      "main": [
        [
          {
            "node": "Split Out",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Email Trigger (IMAP)": {
      "main": [
        [
          {
            "node": "Get fields from source email",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Filter for drafts folder": {
      "main": [
        [
          {
            "node": "gather data for draft email",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "gather data for draft email": {
      "main": [
        [
          {
            "node": "upload draft email",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get fields from source email": {
      "main": [
        [
          {
            "node": "OpenAI",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-918"></a>

## Template 918 - Varredura de domínios com Icypeas (bulk search)

- **Nome:** Varredura de domínios com Icypeas (bulk search)
- **Descrição:** Este fluxo lê dados de uma planilha Google (lastname, firstname e company), autentica na Icypeas e executa buscas em bulk de domínios enviando os dados para a API, com resultados disponibilizados no painel e por e‑mail.
- **Funcionalidade:** • Gatilho manual: inicia a automação quando o usuário aciona a opção Executar Fluxo.
• Leitura de dados: extrai lastname, firstname e company de uma planilha do Google Sheets.
• Autenticação na Icypeas: utiliza API key, API secret e User ID para autenticar e gerar a assinatura da requisição.
• Preparação de payload: organiza os dados da planilha no formato esperado pela API para bulk search.
• Execução de bulk search: envia uma requisição POST com tarefa domain-search, nome e dados para a API.
• Recuperação de resultados: os resultados ficam disponíveis no painel da Icypeas e via e-mail.
- **Ferramentas:** • Icypeas: Serviço de bulk domain search que requer autenticação por API key, secret e user ID.
• Google Sheets: Planilha usada para armazenar e ler os dados (lastname, firstname e company).



## Fluxo visual

```mermaid
flowchart LR
    N1["When clicking 'Execute Workflow'"]
    N2["Sticky Note"]
    N3["Authenticates to your Icypeas account"]
    N4["Sticky Note1"]
    N5["Sticky Note3"]
    N6["Sticky Note4"]
    N7["Reads lastname,firstname and company from your sheet"]
    N8["Run bulk search (domain-search)"]

    N1 --> N7
    N3 --> N8
    N7 --> N3
```

## Fluxo (.json) :

```json
{
  "meta": {
    "instanceId": "257476b1ef58bf3cb6a46e65fac7ee34a53a5e1a8492d5c6e4da5f87c9b82833"
  },
  "nodes": [
    {
      "id": "bfbd4299-0c8d-4368-b156-c76602ca068c",
      "name": "When clicking \"Execute Workflow\"",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        640,
        1700
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "40cf87be-d9fc-434b-9099-0151968d2a0b",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        500,
        1420
      ],
      "parameters": {
        "height": 259,
        "content": "## Domain scan with Icypeas (bulk search)\n\n\nThis workflow demonstrates how to perform domain scans (bulk search) using Icypeas. Visit https://icypeas.com to create your account."
      },
      "typeVersion": 1
    },
    {
      "id": "c646dddb-bcd4-4ac8-b08f-e61ec16c99c5",
      "name": "Authenticates to your Icypeas account",
      "type": "n8n-nodes-base.code",
      "position": [
        1140,
        1700
      ],
      "parameters": {
        "jsCode": "const API_BASE_URL = \"https://app.icypeas.com/api\";\nconst API_PATH = \"/bulk-search\";\nconst METHOD = \"POST\";\n\n// Change here\nconst API_KEY = \"PUT_API_KEY_HERE\";\nconst API_SECRET = \"PUT_API_SECRET_HERE\";\nconst USER_ID = \"PUT_USER_ID_HERE\";\n////////////////\n\nconst genSignature = (\n    url,\n    method,\n    secret,\n    timestamp = new Date().toISOString()\n) => {\n    const Crypto = require('crypto');\n    const payload = `${method}${url}${timestamp}`.toLowerCase();\n    const sign = Crypto.createHmac(\"sha1\", secret).update(payload).digest(\"hex\");\n\n    return sign;\n};\n\nconst apiUrl = `${API_BASE_URL}${API_PATH}`;\n\nconst data = $input.all().map((x) => [ x.json.company]);\n$input.first().json.data = data;\n$input.first().json.api = {\n  timestamp: new Date().toISOString(),\n  secret: API_SECRET,\n  key: API_KEY,\n  userId: USER_ID,\n  url: apiUrl,\n};\n\n$input.first().json.api.signature = genSignature(apiUrl, METHOD, API_SECRET, $input.first().json.api.timestamp);\nreturn $input.first();"
      },
      "typeVersion": 1
    },
    {
      "id": "f0fcf039-2508-429e-8b9a-4ec1ab929d97",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        780,
        1548.9314213779933
      ],
      "parameters": {
        "height": 523.2083276562503,
        "content": "## Read your Google sheet file\n\nThis node reads a Google Sheet. You need to create a sheet with :\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n**The first column** :\nHeader : company\n\n\n\n\nDon't forget to specify the path of your file in the node and your credentials."
      },
      "typeVersion": 1
    },
    {
      "id": "1d0d1805-f664-44d3-83be-9ea26d43526c",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1021.0092314499475,
        1458.51011235955
      ],
      "parameters": {
        "width": 392.0593078758952,
        "height": 1203.3290499048028,
        "content": "## Authenticates to your Icypeas account\n\nThis code node utilizes your API key, API secret, and User ID to establish a connection with your Icypeas account.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nOpen this node and insert your API Key, API secret, and User ID within the quotation marks. You can locate these credentials on your Icypeas profile at https://app.icypeas.com/bo/profile. Here is the extract of what you have to change :\n\nconst API_KEY = \"**PUT_API_KEY_HERE**\";\nconst API_SECRET = \"**PUT_API_SECRET_HERE**\";\nconst USER_ID = \"**PUT_USER_ID_HERE**\";\n\nDo not change any other line of the code.\n\nIf you are a self-hosted user, follow these steps to activate the crypto module :\n\n1.Access your n8n instance:\nLog in to your n8n instance using your web browser by navigating to the URL of your instance, for example: http://your-n8n-instance.com.\n\n2.Go to Settings:\nIn the top-right corner, click on your username, then select \"Settings.\"\n\n3.Select General Settings:\nIn the left menu, click on \"General.\"\n\n4.Enable the Crypto module:\nScroll down to the \"Additional Node Packages\" section. You will see an option called \"crypto\" with a checkbox next to it. Check this box to enable the Crypto module.\n\n5.Save the changes:\nAt the bottom of the page, click \"Save\" to apply the changes.\n\nOnce you've followed these steps, the Crypto module should be activated for your self-hosted n8n instance. Make sure to save your changes and optionally restart your n8n instance for the changes to take effect.\n\n\n\n\n\n"
      },
      "typeVersion": 1
    },
    {
      "id": "999fda2a-50ba-4641-8842-7d62587e0ad5",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1413,
        1460
      ],
      "parameters": {
        "width": 328.8456933308303,
        "height": 869.114109302513,
        "content": "## Performs domain scans (bulk).\n\n\nThis node executes an HTTP request (POST) to scan the domains/companies.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n### You need to create credentials in the HTTP Request node :\n\n➔ In the Credential for Header Auth, click on - Create new Credential -.\n➔ In the Name section, write “Authorization”\n➔ In the Value section, select expression (located just above the field on the right when you hover on top of it) and write {{ $json.api.key + ':' + $json.api.signature }} .\n➔ Then click on “Save” to save the changes.\n\n### To retrieve the results :\n\nAfter some time, the results, which are downloadable, will be available in the Icypeas application  in this section : https://app.icypeas.com/bo/bulksearch?task=domain-search, and you will receive the scan results via email from no-reply@icypeas.com, providing you with the results of your scans.\n\n\n\n\n"
      },
      "typeVersion": 1
    },
    {
      "id": "0f5382ae-cd84-47a7-9818-ad252c9d62c3",
      "name": "Reads lastname,firstname and company from your sheet",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        840,
        1700
      ],
      "parameters": {
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": ""
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": ""
        }
      },
      "typeVersion": 4.1
    },
    {
      "id": "ce00b713-6ddc-4625-a9cc-e9badc2022d4",
      "name": "Run bulk search (domain-search)",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1480,
        1700
      ],
      "parameters": {
        "url": "={{ $json.api.url }}",
        "method": "POST",
        "options": {},
        "sendBody": true,
        "sendHeaders": true,
        "authentication": "genericCredentialType",
        "bodyParameters": {
          "parameters": [
            {
              "name": "task",
              "value": "=domain-search"
            },
            {
              "name": "name",
              "value": "dernierT"
            },
            {
              "name": "user",
              "value": "={{ $json.api.userId }}"
            },
            {
              "name": "data",
              "value": "={{ $json.data }}"
            }
          ]
        },
        "genericAuthType": "httpHeaderAuth",
        "headerParameters": {
          "parameters": [
            {
              "name": "X-ROCK-TIMESTAMP",
              "value": "={{ $json.api.timestamp }}"
            }
          ]
        }
      },
      "typeVersion": 4.1
    }
  ],
  "pinData": {},
  "connections": {
    "When clicking \"Execute Workflow\"": {
      "main": [
        [
          {
            "node": "Reads lastname,firstname and company from your sheet",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Authenticates to your Icypeas account": {
      "main": [
        [
          {
            "node": "Run bulk search (domain-search)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Reads lastname,firstname and company from your sheet": {
      "main": [
        [
          {
            "node": "Authenticates to your Icypeas account",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-919"></a>

## Template 919 - Auto-categorizar posts WordPress

- **Nome:** Auto-categorizar posts WordPress
- **Descrição:** Fluxo que lê posts do WordPress, usa um modelo de IA para determinar uma única categoria para cada post com base no título e atualiza o post com o ID da categoria selecionada.
- **Funcionalidade:** • Início manual: permite executar o processo sob demanda.
• Recuperação de posts: obtém todos os posts existentes do site WordPress.
• Classificação por IA: analisa o título de cada post e retorna um único ID de categoria a partir de uma lista fixa.
• Atualização automática: aplica o ID de categoria retornado ao post no WordPress.
• Configuração personalizável: o prompt de categorização e a lista de categorias/IDs podem ser editados para ajustar a taxonomia.
- **Ferramentas:** • WordPress: repositório de posts e categorias acessível via API para leitura e atualização de conteúdo.
• OpenAI (modelo de linguagem): realiza a análise do título e fornece a decisão de categoria com base no prompt e na lista de IDs.



## Fluxo visual

```mermaid
flowchart LR
    N1["When clicking ‘Test workflow’"]
    N2["Wordpress"]
    N3["Sticky Note1"]
    N4["Sticky Note"]
    N5["Sticky Note2"]
    N6["Sticky Note3"]
    N7["Get All Wordpress Posts"]
    N8["OpenAI Chat Model"]
    N9["AI Agent"]

    N9 --> N2
    N7 --> N9
    N1 --> N7
```

## Fluxo (.json) :

```json
{
  "id": "caaf1WFANPKAikiH",
  "meta": {
    "instanceId": "558d88703fb65b2d0e44613bc35916258b0f0bf983c5d4730c00c424b77ca36a",
    "templateCredsSetupCompleted": true
  },
  "name": "Auto categorize wordpress template",
  "tags": [],
  "nodes": [
    {
      "id": "2017403c-7496-48f8-a487-8a017c7adfe3",
      "name": "When clicking ‘Test workflow’",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        680,
        320
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "82ff288f-4234-4192-9046-33e5ffee5264",
      "name": "Wordpress",
      "type": "n8n-nodes-base.wordpress",
      "position": [
        1500,
        320
      ],
      "parameters": {
        "postId": "={{ $('Get All Wordpress Posts').item.json.id }}",
        "operation": "update",
        "updateFields": {
          "categories": "={{ $json.output }}"
        }
      },
      "credentials": {
        "wordpressApi": {
          "id": "lGWPwxTdfPDDbFjj",
          "name": "Rumjahn.com wordpress"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "521deb22-62dd-4b5f-8b9a-aab9777821da",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        620,
        -100
      ],
      "parameters": {
        "width": 504.88636363636317,
        "content": "## How to Auto-Categorize 82 Blog Posts in 2 Minutes using A.I. (No Coding Required)\n\n💡 Read the [case study here](https://rumjahn.com/how-to-use-a-i-to-categorize-wordpress-posts-and-streamline-your-content-organization-process/).\n\n📺 Watch the [youtube tutorial here](https://www.youtube.com/watch?v=IvQioioVqhw)\n\n"
      },
      "typeVersion": 1
    },
    {
      "id": "4090d827-f8cd-47ef-ad4f-654ee58216f6",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        860,
        180
      ],
      "parameters": {
        "color": 3,
        "width": 188.14814814814804,
        "height": 327.3400673400663,
        "content": "### Get wordpress posts\n\nTurn off return all if you're running into issues.\n"
      },
      "typeVersion": 1
    },
    {
      "id": "71585d54-fdcc-42a5-8a0e-0fac3adc1809",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1080,
        80
      ],
      "parameters": {
        "color": 4,
        "width": 315.1464152082392,
        "height": 416.90235690235625,
        "content": "### A.I. Categorization\n\n1. you need to set up the categories first in wordpress\n\n2. Edit the message prompt and change the categories and category numbers"
      },
      "typeVersion": 1
    },
    {
      "id": "29354054-8600-4e45-99d0-6f30f779a505",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1480,
        240
      ],
      "parameters": {
        "color": 5,
        "width": 171.64983164983155,
        "height": 269.59595959595947,
        "content": "### Update category"
      },
      "typeVersion": 1
    },
    {
      "id": "d9fe6289-6b97-4830-80aa-754ac4d4b3e0",
      "name": "Get All Wordpress Posts",
      "type": "n8n-nodes-base.wordpress",
      "position": [
        900,
        320
      ],
      "parameters": {
        "options": {},
        "operation": "getAll",
        "returnAll": true
      },
      "credentials": {
        "wordpressApi": {
          "id": "lGWPwxTdfPDDbFjj",
          "name": "Rumjahn.com wordpress"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "ed40bf13-8294-4b4e-a8b6-5749989d3420",
      "name": "OpenAI Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        1080,
        540
      ],
      "parameters": {
        "options": {}
      },
      "credentials": {
        "openAiApi": {
          "id": "XO3iT1iYT5Vod56X",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "dafeb935-532e-4067-9dfb-7e9a6bbc4e5a",
      "name": "AI Agent",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        1100,
        320
      ],
      "parameters": {
        "text": "=You are an expert content strategist and taxonomy specialist with extensive experience in blog categorization and content organization.\n\nI will provide you with a blog post's title. Your task is to assign ONE primary category ID from this fixed list:\n\n13 = Content Creation\n14 = Digital Marketing\n15 = AI Tools\n17 = Automation & Integration\n18 = Productivity Tools\n19 = Analytics & Strategy\n\nAnalyze the title and return only the single most relevant category ID number that best represents the main focus of the post. While a post might touch on multiple topics, select the dominant theme that would be most useful for navigation purposes.\n\n{{ $json.title.rendered }}\n\nOutput only the category number",
        "options": {},
        "promptType": "define"
      },
      "typeVersion": 1.7
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "2a753171-425f-4b5a-bd1b-8591ad2d142c",
  "connections": {
    "AI Agent": {
      "main": [
        [
          {
            "node": "Wordpress",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Chat Model": {
      "ai_languageModel": [
        [
          {
            "node": "AI Agent",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Get All Wordpress Posts": {
      "main": [
        [
          {
            "node": "AI Agent",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "When clicking ‘Test workflow’": {
      "main": [
        [
          {
            "node": "Get All Wordpress Posts",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-920"></a>

## Template 920 - Automação de captação e follow-up de leads

- **Nome:** Automação de captação e follow-up de leads
- **Descrição:** Fluxo que recebe leads de um formulário, registra em backup, cria/atualiza contato no CRM, envia email de boas-vindas e faz contato inicial via WhatsApp, com atualização de tags de CRM.
- **Funcionalidade:** • Captura de leads via endpoint HTTP: Recebe dados de formulário enviados pelo site para iniciar a automação.
• Backup em planilha: Registra os dados do lead em uma planilha do Google Sheets para histórico e auditoria.
• Criação de contato no CRM: Envia os dados do lead para o CRM (FluentCRM) e aplica uma tag inicial "New Lead".
• Envio de email de aquecimento: Dispara um email de boas-vindas personalizado para o endereço do lead.
• Envio de mensagem via WhatsApp: Envia uma mensagem inicial personalizada usando o provedor Whinta para contato rápido.
• Atualização de tag no CRM: Após o envio da mensagem WhatsApp, atualiza a tag do contato no CRM para "Customer" para refletir o avanço no funil.
- **Ferramentas:** • Formulário do site / Endpoint HTTP: Origem dos leads que aciona o fluxo.
• Google Sheets: Planilha usada para backup e registro dos leads.
• FluentCRM (WordPress): CRM usado para criar contatos e gerenciar tags via API.
• Servidor SMTP: Serviço para envio do email de boas-vindas.
• Whinta API: Provedor externo utilizado para envio de mensagens WhatsApp.

## Fluxo visual

```mermaid
flowchart LR
    N1["Webhook - Lead Capture"]
    N2["Google Sheets - Backup Log"]
    N3["FluentCRM - Add Contact"]
    N4["Send Warmup Email"]
    N5["Send WhatsApp via Whinta"]
    N6["Update CRM Tag to Customer"]

    N4 --> N5
    N1 --> N2
    N1 --> N3
    N5 --> N6
    N2 --> N4
```

## Fluxo (.json) :

```json
{
  "name": "AccountCraft WhatsApp Automation - Infridet",
  "nodes": [
    {
      "id": "1",
      "name": "Webhook - Lead Capture",
      "type": "n8n-nodes-base.webhook",
      "position": [
        250,
        300
      ],
      "parameters": {
        "path": "lead-capture",
        "responseMode": "onReceived"
      },
      "typeVersion": 1
    },
    {
      "id": "2",
      "name": "Google Sheets - Backup Log",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        500,
        200
      ],
      "parameters": {
        "range": "Leads!A1",
        "options": {},
        "sheetId": "your_google_sheet_id_here",
        "valueInputMode": "USER_ENTERED"
      },
      "credentials": {
        "googleApi": "Google Account"
      },
      "typeVersion": 1
    },
    {
      "id": "3",
      "name": "FluentCRM - Add Contact",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        500,
        400
      ],
      "parameters": {
        "url": "https://your-crm-domain.com/wp-json/fluent-crm/v2/contacts",
        "method": "POST",
        "options": {},
        "jsonParameters": true,
        "bodyParametersJson": "{\n  \"email\": \"{{$json[\"email\"]}}\",\n  \"first_name\": \"{{$json[\"name\"]}}\",\n  \"tags\": [\"New Lead\"]\n}"
      },
      "credentials": {
        "httpBasicAuth": {
          "user": "your_crm_api_user",
          "password": "your_crm_api_key"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "4",
      "name": "Send Warmup Email",
      "type": "n8n-nodes-base.emailSend",
      "position": [
        750,
        200
      ],
      "parameters": {
        "text": "Hey {{$json[\"name\"]}},\n\nThanks for joining Account Craft! We’ll help you build your YouTube channel and earn like a pro. Stay tuned. 🔥\n\nCheers,\nGyan",
        "subject": "Welcome to Account Craft 🚀",
        "toEmail": "={{$json[\"email\"]}}",
        "fromEmail": "your@email.com"
      },
      "credentials": {
        "smtp": "SMTP Account"
      },
      "typeVersion": 1
    },
    {
      "id": "5",
      "name": "Send WhatsApp via Whinta",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1000,
        200
      ],
      "parameters": {
        "url": "https://api.whinta.com/send",
        "method": "POST",
        "options": {},
        "jsonParameters": true,
        "bodyParametersJson": "{\n  \"phone\": \"{{$json[\"phone\"]}}\",\n  \"message\": \"Hey {{$json[\"name\"]}}, Gyan here from Account Craft 👋 Just saw your form – want help starting your YouTube channel?\"\n}"
      },
      "typeVersion": 1
    },
    {
      "id": "6",
      "name": "Update CRM Tag to Customer",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1250,
        200
      ],
      "parameters": {
        "url": "https://your-crm-domain.com/wp-json/fluent-crm/v2/contacts/update",
        "method": "POST",
        "options": {},
        "jsonParameters": true,
        "bodyParametersJson": "{\n  \"email\": \"{{$json[\"email\"]}}\",\n  \"tags\": [\"Customer\"]\n}"
      },
      "credentials": {
        "httpBasicAuth": {
          "user": "your_crm_api_user",
          "password": "your_crm_api_key"
        }
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "versionId": "1",
  "connections": {
    "Send Warmup Email": {
      "main": [
        [
          {
            "node": "Send WhatsApp via Whinta",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Webhook - Lead Capture": {
      "main": [
        [
          {
            "node": "Google Sheets - Backup Log",
            "type": "main",
            "index": 0
          },
          {
            "node": "FluentCRM - Add Contact",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Send WhatsApp via Whinta": {
      "main": [
        [
          {
            "node": "Update CRM Tag to Customer",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Sheets - Backup Log": {
      "main": [
        [
          {
            "node": "Send Warmup Email",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-921"></a>

## Template 921 - Batch processing of email verifications with Icypeas

- **Nome:** Batch processing of email verifications with Icypeas
- **Descrição:** Este fluxo lê dados de uma planilha, autentica na Icypeas e envia verificação de emails em lote, retornando os resultados para o usuário.
- **Funcionalidade:** • Leitura de dados da planilha: extrai emails, nomes (lastname, firstname) e empresa para uso na verificação.
• Autenticação e assinatura da requisição: prepara timestamp, api key/secret e gera assinatura para chamada de API.
• Envio de verificação em lote: envia os dados para bulk-search da Icypeas para verificação de emails.
• Recuperação de resultados e notificações: disponibiliza resultados na aplicação Icypeas e envia confirmação por email.
- **Ferramentas:** • Google Sheets: fonte de dados com emails, nomes e empresa.
• Icypeas: serviço de verificação de emails em lote via endpoint bulk-search.



## Fluxo visual

```mermaid
flowchart LR
    N1["When clicking 'Execute Workflow'"]
    N2["Sticky Note"]
    N3["Authenticates to your Icypeas account"]
    N4["Sticky Note1"]
    N5["Sticky Note3"]
    N6["Sticky Note4"]
    N7["Reads lastname,firstname and company from your sheet"]
    N8["Run bulk search (email-verif)"]

    N1 --> N7
    N3 --> N8
    N7 --> N3
```

## Fluxo (.json) :

```json
{
  "meta": {
    "instanceId": "257476b1ef58bf3cb6a46e65fac7ee34a53a5e1a8492d5c6e4da5f87c9b82833"
  },
  "nodes": [
    {
      "id": "8e31498a-d004-4d55-8952-b07e4e49f75f",
      "name": "When clicking \"Execute Workflow\"",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        800,
        1320
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "56e1351c-804d-41d4-9651-d2ca2020c4ce",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        660,
        1020
      ],
      "parameters": {
        "height": 292.0581548177272,
        "content": "## Perform Batch Processing of Email verifications with Icypeas \n\n\nThis workflow demonstrates how to perform email verifications (bulk search) using Icypeas. Visit https://icypeas.com to create your account."
      },
      "typeVersion": 1
    },
    {
      "id": "0bd19032-2894-4e0e-b66f-00718bd389a7",
      "name": "Authenticates to your Icypeas account",
      "type": "n8n-nodes-base.code",
      "position": [
        1300,
        1320
      ],
      "parameters": {
        "jsCode": "const API_BASE_URL = \"https://app.icypeas.com/api\";\nconst API_PATH = \"/bulk-search\";\nconst METHOD = \"POST\";\n\n// Change here\nconst API_KEY = \"PUT_API_KEY_HERE\";\nconst API_SECRET = \"PUT_API_SECRET_HERE\";\nconst USER_ID = \"PUT_USER_ID_HERE\";\n////////////////\n\nconst genSignature = (\n    url,\n    method,\n    secret,\n    timestamp = new Date().toISOString()\n) => {\n    const Crypto = require('crypto');\n    const payload = `${method}${url}${timestamp}`.toLowerCase();\n    const sign = Crypto.createHmac(\"sha1\", secret).update(payload).digest(\"hex\");\n\n    return sign;\n};\n\nconst apiUrl = `${API_BASE_URL}${API_PATH}`;\n\nconst data = $input.all().map((x) => [ x.json.email]);\n$input.first().json.data = data;\n$input.first().json.api = {\n  timestamp: new Date().toISOString(),\n  secret: API_SECRET,\n  key: API_KEY,\n  userId: USER_ID,\n  url: apiUrl,\n};\n\n$input.first().json.api.signature = genSignature(apiUrl, METHOD, API_SECRET, $input.first().json.api.timestamp);\nreturn $input.first();"
      },
      "typeVersion": 1
    },
    {
      "id": "df9bc762-c680-447f-a4f3-eba1ba13cb3d",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        940,
        1168.9314213779933
      ],
      "parameters": {
        "height": 523.2083276562503,
        "content": "## Read your Google sheet file\n\nThis node reads a Google Sheet. You need to create a sheet with :\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n**The first column** :\nHeader : email\n\n\n\n\nDon't forget to specify the path of your file in the node and your credentials."
      },
      "typeVersion": 1
    },
    {
      "id": "c542f720-7c21-4161-a643-4e67983ad090",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1181.009231449947,
        1078.51011235955
      ],
      "parameters": {
        "width": 392.0593078758952,
        "height": 1203.3290499048028,
        "content": "## Authenticates to your Icypeas account\n\nThis code node utilizes your API key, API secret, and User ID to establish a connection with your Icypeas account.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nOpen this node and insert your API Key, API secret, and User ID within the quotation marks. You can locate these credentials on your Icypeas profile at https://app.icypeas.com/bo/profile. Here is the extract of what you have to change :\n\nconst API_KEY = \"**PUT_API_KEY_HERE**\";\nconst API_SECRET = \"**PUT_API_SECRET_HERE**\";\nconst USER_ID = \"**PUT_USER_ID_HERE**\";\n\nDo not change any other line of the code.\n\nIf you are a self-hosted user, follow these steps to activate the crypto module :\n\n1.Access your n8n instance:\nLog in to your n8n instance using your web browser by navigating to the URL of your instance, for example: http://your-n8n-instance.com.\n\n2.Go to Settings:\nIn the top-right corner, click on your username, then select \"Settings.\"\n\n3.Select General Settings:\nIn the left menu, click on \"General.\"\n\n4.Enable the Crypto module:\nScroll down to the \"Additional Node Packages\" section. You will see an option called \"crypto\" with a checkbox next to it. Check this box to enable the Crypto module.\n\n5.Save the changes:\nAt the bottom of the page, click \"Save\" to apply the changes.\n\nOnce you've followed these steps, the Crypto module should be activated for your self-hosted n8n instance. Make sure to save your changes and optionally restart your n8n instance for the changes to take effect.\n\n\n\n\n\n"
      },
      "typeVersion": 1
    },
    {
      "id": "26602f88-789e-4f9e-8df0-2f7f498f242c",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1573,
        1080
      ],
      "parameters": {
        "width": 328.8456933308303,
        "height": 869.114109302513,
        "content": "## Performs email verifications (bulk).\n\n\nThis node executes an HTTP request (POST) to verify the emails.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n### You need to create credentials in the HTTP Request node :\n\n➔ In the Credential for Header Auth, click on - Create new Credential -.\n➔ In the Name section, write “Authorization”\n➔ In the Value section, select expression (located just above the field on the right when you hover on top of it) and write {{ $json.api.key + ':' + $json.api.signature }} .\n➔ Then click on “Save” to save the changes.\n\n### To retrieve the results :\n\nAfter some time, the results, which are downloadable, will be available in the Icypeas application  in this section : https://app.icypeas.com/bo/bulksearch?task=email-verification, and you will receive the verification results via email from no-reply@icypeas.com, providing you with the results of your email verifications.\n\n\n\n\n"
      },
      "typeVersion": 1
    },
    {
      "id": "96128999-d7e1-44cd-b9d3-7550e4333414",
      "name": "Reads lastname,firstname and company from your sheet",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        1000,
        1320
      ],
      "parameters": {
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": ""
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": ""
        }
      },
      "typeVersion": 4.1
    },
    {
      "id": "bc548060-6e09-493b-9e74-fc7ef6a9b88f",
      "name": "Run bulk search (email-verif)",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1640,
        1320
      ],
      "parameters": {
        "url": "={{ $json.api.url }}",
        "method": "POST",
        "options": {},
        "sendBody": true,
        "sendHeaders": true,
        "authentication": "genericCredentialType",
        "bodyParameters": {
          "parameters": [
            {
              "name": "task",
              "value": "=email-verification"
            },
            {
              "name": "name",
              "value": "dernierTsfg"
            },
            {
              "name": "user",
              "value": "={{ $json.api.userId }}"
            },
            {
              "name": "data",
              "value": "={{ $json.data }}"
            }
          ]
        },
        "genericAuthType": "httpHeaderAuth",
        "headerParameters": {
          "parameters": [
            {
              "name": "X-ROCK-TIMESTAMP",
              "value": "={{ $json.api.timestamp }}"
            }
          ]
        }
      },
      "typeVersion": 4.1
    }
  ],
  "pinData": {},
  "connections": {
    "When clicking \"Execute Workflow\"": {
      "main": [
        [
          {
            "node": "Reads lastname,firstname and company from your sheet",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Authenticates to your Icypeas account": {
      "main": [
        [
          {
            "node": "Run bulk search (email-verif)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Reads lastname,firstname and company from your sheet": {
      "main": [
        [
          {
            "node": "Authenticates to your Icypeas account",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
