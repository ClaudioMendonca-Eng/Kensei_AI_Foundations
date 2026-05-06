# PACK 1999 TEMPLATES PARTE 08 - Bloco 7

Templates neste bloco: 20

## Sumário

- [Template 1706 - Salvar novos vídeos do YouTube no Raindrop](#template-1706)
- [Template 1708 - Follow up de leads com IA, Lemlist e HubSpot](#template-1708)
- [Template 1710 - Sincronização periódica de planilhas](#template-1710)
- [Template 1712 - Agente DEXScan CoinMarketCap](#template-1712)
- [Template 1714 - Arquivar duplicatas em banco de dados Notion](#template-1714)
- [Template 1716 - Assistente de previsão do tempo com Open-Meteo e IA](#template-1716)
- [Template 1718 - Comparação semanal de métricas GA4 com A.I. e salvamento](#template-1718)
- [Template 1721 - Criar contato HubSpot e follow-up por email](#template-1721)
- [Template 1723 - Atribuição automática de issues no GitHub](#template-1723)
- [Template 1725 - Assistente pessoal com integração a calendário, email e CRM](#template-1725)
- [Template 1727 - Gerador de workflow AI para base Notion](#template-1727)
- [Template 1730 - Criação/Atualização de contato Mautic com Calendly](#template-1730)
- [Template 1731 - Reengajamento pós-reunião com sugestões de disponibilidade](#template-1731)
- [Template 1733 - Converter artigo WordPress em áudio](#template-1733)
- [Template 1735 - Transcrição de arquivo MP4 para texto](#template-1735)
- [Template 1737 - Criar cliente e adicioná‑lo a um segmento (Customer.io)](#template-1737)
- [Template 1739 - Criar tarefa ClickUp via Slack e retornar ID](#template-1739)
- [Template 1741 - Geração automática de artigos para base de conhecimento](#template-1741)
- [Template 1742 - API REST multi-métodos para clientes (Airtable)](#template-1742)
- [Template 1745 - Registro automático de participantes](#template-1745)

---

<a id="template-1706"></a>

## Template 1706 - Salvar novos vídeos do YouTube no Raindrop

- **Nome:** Salvar novos vídeos do YouTube no Raindrop
- **Descrição:** Verifica uma playlist do YouTube e salva novos vídeos como bookmarks no Raindrop automaticamente.
- **Funcionalidade:** • Verificação agendada e manual: executa a cada 30 minutos e permite acionamento manual para checagens imediatas.
• Coleta de itens da playlist: busca todos os vídeos de uma playlist configurada.
• Normalização dos dados: extrai e utiliza o bloco de dados relevante (snippet) para facilitar processamento.
• Filtragem de novos vídeos: compara IDs de vídeos com um armazenamento estático para identificar apenas itens não processados.
• Criação de favoritos no Raindrop: adiciona um bookmark com link do vídeo, título formatado (canal | título) e tag "youtube".
• Atualização do histórico: registra os IDs processados para evitar duplicatas futuras.
- **Ferramentas:** • YouTube: API do YouTube usada para obter os itens de uma playlist (requer credenciais OAuth).
• Raindrop: serviço de bookmarks usado para criar favoritos com link, título e tags (requer credenciais OAuth).

## Fluxo visual

```mermaid
flowchart LR
    N1["On clicking 'execute'"]
    N2["YouTube"]
    N3["Filter new items"]
    N4["Flatten JSON"]
    N5["Raindrop Bookmark"]
    N6["Every 30 mins"]

    N2 --> N4
    N4 --> N3
    N6 --> N2
    N3 --> N5
    N1 --> N2
```

## Fluxo (.json) :

```json
{
  "id": 7,
  "name": "YouTube to Raindrop",
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        -610,
        160
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "YouTube",
      "type": "n8n-nodes-base.youTube",
      "position": [
        -440,
        240
      ],
      "parameters": {
        "part": [
          "snippet"
        ],
        "options": {},
        "resource": "playlistItem",
        "operation": "getAll",
        "playlistId": "CHANGE_ME"
      },
      "credentials": {
        "youTubeOAuth2Api": "Google n8n"
      },
      "typeVersion": 1
    },
    {
      "name": "Filter new items",
      "type": "n8n-nodes-base.function",
      "position": [
        -120,
        240
      ],
      "parameters": {
        "functionCode": "const staticData = getWorkflowStaticData('global');\nconst newIds = items.map(item => item.json[\"resourceId\"][\"videoId\"]);\nconst oldIds = staticData.oldIds; \n\nif (!oldIds) {\n  staticData.oldIds = newIds;\n  return items;\n}\n\n\nconst actualNewIds = newIds.filter((id) => !oldIds.includes(id));\nconst actualNew = items.filter((data) => actualNewIds.includes(data.json[\"resourceId\"][\"videoId\"]));\nstaticData.oldIds = [...actualNewIds, ...oldIds];\n\nreturn actualNew;\n"
      },
      "typeVersion": 1
    },
    {
      "name": "Flatten JSON",
      "type": "n8n-nodes-base.functionItem",
      "position": [
        -280,
        240
      ],
      "parameters": {
        "functionCode": "item = item[\"snippet\"]\n\nreturn item;"
      },
      "typeVersion": 1
    },
    {
      "name": "Raindrop Bookmark",
      "type": "n8n-nodes-base.raindrop",
      "position": [
        40,
        240
      ],
      "parameters": {
        "link": "=https://www.youtube.com/watch?v={{$json[\"resourceId\"][\"videoId\"]}}",
        "resource": "bookmark",
        "operation": "create",
        "collectionId": 0,
        "additionalFields": {
          "tags": "youtube",
          "title": "={{$json[\"videoOwnerChannelTitle\"]}} | {{$json[\"title\"]}}"
        }
      },
      "credentials": {
        "raindropOAuth2Api": "Raindrop"
      },
      "typeVersion": 1
    },
    {
      "name": "Every 30 mins",
      "type": "n8n-nodes-base.cron",
      "position": [
        -610,
        320
      ],
      "parameters": {
        "triggerTimes": {
          "item": [
            {
              "mode": "everyX",
              "unit": "minutes",
              "value": 30
            }
          ]
        }
      },
      "typeVersion": 1
    }
  ],
  "active": true,
  "settings": {},
  "connections": {
    "YouTube": {
      "main": [
        [
          {
            "node": "Flatten JSON",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Flatten JSON": {
      "main": [
        [
          {
            "node": "Filter new items",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Every 30 mins": {
      "main": [
        [
          {
            "node": "YouTube",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Filter new items": {
      "main": [
        [
          {
            "node": "Raindrop Bookmark",
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
            "node": "YouTube",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-1708"></a>

## Template 1708 - Follow up de leads com IA, Lemlist e HubSpot

- **Nome:** Follow up de leads com IA, Lemlist e HubSpot
- **Descrição:** Automatiza o tratamento de respostas de leads em campanhas de e-mail, classificando a intenção da resposta com IA, gerando conteúdo de follow-up, atualizando o status no Lemlist e criando/atualizando negócios no HubSpot.
- **Funcionalidade:** • Classificação da resposta do lead: usa IA para categorizar a mensagem em categorias como interested, Out of Office, unsubscribe ou other.
• Geração de texto de follow-up: cria o corpo do e-mail com informações da campanha e dados do lead.
• Atualização do status no Lemlist: marca o lead como 'interested' na campanha correspondente via API.
• Criação de deal no HubSpot: cria um novo negócio com o nome personalizado e associa ao contato/lead.
• Recuperação do ID de contato no HubSpot: obtém o VID/ID do contato para vincular dados.
• Criação de tarefa de follow-up: gera uma tarefa para a equipe acompanhar o lead.
• Envio de follow-up: utiliza o assunto personalizado e o conteúdo gerado, incluindo link para relatórios da campanha.
• Integração de serviços: coordena Lemlist, HubSpot e OpenAI para automatizar o fluxo.
- **Ferramentas:** • Lemlist: API para gerenciar leads, campanhas e mensagens de follow-up.
• HubSpot: CRM para criação de deals, gestão de contatos e associação de leads a oportunidades.
• OpenAI: Serviço de IA para classificação de mensagens e geração de conteúdo de e-mail.



## Fluxo (.json) :

```json
{
  "\"id\"": "\"67\",",
  "\"url\"": "\"=https://api.lemlist.com/api/campaigns/YOUR_CAMPAIGN_ID/leads/{{$json[\\\"leadEmail\\\"]}}/interested\",",
  "\"main\"": "[",
  "\"meta\"": "{",
  "\"mode\"": "\"combine\",",
  "\"name\"": "\"Lucas Open AI\"",
  "\"node\"": "\"follow up task\",",
  "\"text\"": "\"=Hello a lead replied to your emails. \\n\\nMore info in lemlist here: \\nhttps://app.lemlist.com/teams/{{$json[\\\"teamId\\\"]}}/reports/campaigns/{{$json[\\\"campaignId\\\"]}}\",",
  "\"topP\"": "1,",
  "\"type\"": "\"main\",",
  "\"Merge\"": "{",
  "\"email\"": "\"={{ $json[\\\"leadEmail\\\"] }}\",",
  "\"event\"": "\"emailsReplied\",",
  "\"index\"": "0",
  "\"nodes\"": "[",
  "\"rules\"": "[",
  "\"stage\"": "\"79009480\",",
  "\"OpenAI\"": "{",
  "\"Switch\"": "{",
  "\"output\"": "2,",
  "\"prompt\"": "\"=The following is a list of emails and the categories they fall into:\\nCategories=[\\\"interested\\\", \\\"Out of office\\\", \\\"unsubscribe\\\", \\\"other\\\"]\\n\\nInterested is when the reply is positive.\\\"\\n\\n{{$json[\\\"text\\\"].replaceAll(/^\\\\s+|\\\\s+$/g, '').replace(/(\\\\r\\\\n|\\\\n|\\\\r)/gm, \\\"\\\")}}\\\\\\\"\\nCategory:\",",
  "\"value1\"": "\"={{ $json[\\\"text\\\"].trim() }}\",",
  "\"value2\"": "\"Out of Office\"",
  "\"values\"": "{",
  "\"channel\"": "\"Your channel name\",",
  "\"isFirst\"": "true",
  "\"options\"": "{",
  "\"subject\"": "\"=OOO - Follow up with {{ $json[\\\"properties\\\"][\\\"firstname\\\"][\\\"value\\\"] }} {{ $json[\\\"properties\\\"][\\\"lastname\\\"][\\\"value\\\"] }}\"",
  "\"dataType\"": "\"string\",",
  "\"dealName\"": "\"=New Deal with {{ $json[\\\"identity-profiles\\\"][0][\\\"identities\\\"][0][\\\"value\\\"] }}\",",
  "\"lastName\"": "\"={{ $json[\\\"leadLastName\\\"] }}\",",
  "\"metadata\"": "{",
  "\"position\"": "[",
  "\"resource\"": "\"contact\",",
  "\"firstName\"": "\"={{ $json[\\\"leadFirstName\\\"] }}\"",
  "\"maxTokens\"": "6,",
  "\"openAiApi\"": "{",
  "\"operation\"": "\"unsubscribe\",",
  "\"webhookId\"": "\"c8f49f36-7ab6-4607-bc5a-41c9555ebd09\",",
  "\"campaignId\"": "\"={{$json[\\\"campaignId\\\"]}}\"",
  "\"contactIds\"": "\"={{ $json[\\\"vid\\\"] }}\"",
  "\"instanceId\"": "\"f0a68da631efd4ed052a324b63ff90f7a844426af0398a68338f44245d1dd9e5\"",
  "\"lemlistApi\"": "{",
  "\"parameters\"": "{",
  "\"attachments\"": "[],",
  "\"connections\"": "{",
  "\"credentials\"": "{",
  "\"temperature\"": "0",
  "\"typeVersion\"": "1",
  "\"associations\"": "{",
  "\"otherOptions\"": "{},",
  "\"resolveClash\"": "\"preferInput1\"",
  "\"clashHandling\"": "{",
  "\"requestMethod\"": "\"POST\",",
  "\"associatedVids\"": "\"={{$json[\\\"canonical-vid\\\"]}}\"",
  "\"authentication\"": "\"oAuth2\"",
  "\"fallbackOutput\"": "3",
  "\"combinationMode\"": "\"mergeByPosition\"",
  "\"additionalFields\"": "{",
  "\"hubspotOAuth2Api\"": "{",
  "}slemlist <> GPT-3": "Supercharge your sales workflows",
  "\"nodeCredentialType\"": "\"lemlistApi\"",
  "\"HubSpot - Create Deal\"": "{",
  "\"Lemlist - Lead Replied\"": "{",
  "\"HubSpot - Get contact ID\"": "{",
  "\"HubSpot - Get contact ID1\"": "{"
}
```

<a id="template-1710"></a>

## Template 1710 - Sincronização periódica de planilhas

- **Nome:** Sincronização periódica de planilhas
- **Descrição:** Lê o intervalo Data!A:G periodicamente e atualiza dois destinos com os mesmos dados.
- **Funcionalidade:** • Agendamento periódico: Executa o fluxo a cada 2 minutos usando expressão cron.
• Leitura de intervalo: Lê o intervalo Data!A:G com dados em formato bruto.
• Atualização de destinos: Atualiza dois destinos distintos com os dados lidos.
• Reutilização de configuração: Usa dinamicamente o mesmo intervalo lido para as operações de atualização.
• Operação de atualização: Realiza operação de update para sobrescrever as células no intervalo especificado.
- **Ferramentas:** • Google Sheets: Serviço de planilhas online utilizado para ler e atualizar intervalos de células.



## Fluxo visual

```mermaid
flowchart LR
    N1["Read Sheet"]
    N2["Cron"]
    N3["Write Sheet 2"]
    N4["Write Sheet 1"]

    N2 --> N1
    N1 --> N3
    N1 --> N4
```

## Fluxo (.json) :

```json
{
  "nodes": [
    {
      "name": "Read Sheet",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        700,
        300
      ],
      "parameters": {
        "range": "Data!A:G",
        "rawData": true
      },
      "typeVersion": 1
    },
    {
      "name": "Cron",
      "type": "n8n-nodes-base.cron",
      "position": [
        500,
        300
      ],
      "parameters": {
        "triggerTimes": {
          "item": [
            {
              "mode": "custom",
              "cronExpression": "0 */2 * * * *"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Write Sheet 2",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        900,
        400
      ],
      "parameters": {
        "range": "={{$node[\"Read Sheet\"].parameter[\"range\"]}}",
        "rawData": true,
        "operation": "update"
      },
      "typeVersion": 1
    },
    {
      "name": "Write Sheet 1",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        900,
        200
      ],
      "parameters": {
        "range": "={{$node[\"Read Sheet\"].parameter[\"range\"]}}",
        "rawData": true,
        "operation": "update"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Cron": {
      "main": [
        [
          {
            "node": "Read Sheet",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Read Sheet": {
      "main": [
        [
          {
            "node": "Write Sheet 2",
            "type": "main",
            "index": 0
          },
          {
            "node": "Write Sheet 1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-1712"></a>

## Template 1712 - Agente DEXScan CoinMarketCap

- **Nome:** Agente DEXScan CoinMarketCap
- **Descrição:** Agente AI que consulta a API DEXScan da CoinMarketCap para obter dados em tempo real e históricos sobre exchanges descentralizadas, pares, liquidez e trades, encaminhando e resumindo respostas para aplicações externas.
- **Funcionalidade:** • Consulta de metadata de DEXs: Recupera informações estáticas como nome, logo, URLs, descrição e data de lançamento.
• Listagem de redes: Obtém todas as blockchains associadas ao ecossistema DEX com metadados e paginação.
• Rankings e cotações de DEXs: Retorna listagens com dados de volume, market share e métricas de mercado.
• Cotações de pares (latest): Fornece cotações mais recentes por contrato ou rede, com dados de liquidez e taxas.
• OHLCV histórico e atual: Recupera séries temporais OHLCV para análise técnica e snapshots em tempo real.
• Últimas trades: Lista operações mais recentes (até 100) para pares específicos.
• Busca de pares spot com filtros avançados: Filtra e ordena pares por rede, volume, liquidez, variação e outros critérios.
• Validação de parâmetros e prevenção de erros: Aplica regras e orientações para evitar requisições inválidas (400) e mistura indevida de parâmetros.
• Memória de sessão e roteamento inteligente: Mantém contexto de conversas e decide qual endpoint usar com base na solicitação do usuário.
• Documentação e exemplos integrados: Inclui instruções de uso, exemplos de chamadas e mensagens de erro para facilitar integração.
- **Ferramentas:** • CoinMarketCap DEXScan API: Serviço principal de dados on-chain que fornece endpoints para metadata, redes, listagens, cotações de pares, OHLCV e trades.
• OpenAI (modelo GPT-4o Mini): Modelo de linguagem usado como 'brain' do agente para interpretar pedidos, validar parâmetros, roteear chamadas e resumir respostas.



## Fluxo visual

```mermaid
flowchart LR
    N1["When Executed by Another Workflow"]
    N2["CoinMarketCap DEXScan Agent"]
    N3["DEXScan Agent Brain"]
    N4["DEXScan Agent Memory"]
    N5["DEX Metadata"]
    N6["DEX Networks List"]
    N7["DEX Listings Quotes"]
    N8["DEX Pair Quotes Latest"]
    N9["DEX OHLCV Historical"]
    N10["DEX OHLCV Latest"]
    N11["DEX Trades Latest"]
    N12["DEX Spot Pairs Latest"]
    N13["DEXScan Agent Guide"]
    N14["DEX Usage + Examples"]
    N15["DEX Errors + IP Notice"]

    N1 --> N2
```

## Fluxo (.json) :

```json
{
  "id": "ImiznkEUWCkKbg1w",
  "meta": {
    "instanceId": "a5283507e1917a33cc3ae615b2e7d5ad2c1e50955e6f831272ddd5ab816f3fb6",
    "templateCredsSetupCompleted": true
  },
  "name": "CoinMarketCap_DEXScan_Agent_Tool",
  "tags": [],
  "nodes": [
    {
      "id": "c055762a-8fe7-4141-a639-df2372f30060",
      "name": "When Executed by Another Workflow",
      "type": "n8n-nodes-base.executeWorkflowTrigger",
      "position": [
        -60,
        320
      ],
      "parameters": {
        "workflowInputs": {
          "values": [
            {
              "name": "sessionId"
            },
            {
              "name": "message"
            }
          ]
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "427c5700-f6d4-4e98-b2ef-c8eac986a754",
      "name": "CoinMarketCap DEXScan Agent",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        360,
        320
      ],
      "parameters": {
        "text": "={{ $json.message }}",
        "options": {
          "systemMessage": "You are an AI agent connected to CoinMarketCap's DEXScan API via a suite of HTTP tools. You can retrieve detailed, real-time, and historical data about decentralized exchanges, spot pairs, liquidity pools, trading activity, and more.\n\nEach tool includes parameter validation and usage guidance to prevent 400 Bad Request errors.\n\n🔧 Available Tools & Descriptions\n1. 📜 DEX Metadata\nPurpose: Retrieve static information (name, logo, URLs, launch date, etc.) for one or more DEXs.\nEndpoint: /v4/dex/listings/info\nRequired: id (one or more CMC DEX IDs)\nOptional: aux → urls, logo, description, date_launched, notice\n\n2. 🌐 DEX Networks List\nPurpose: Get all blockchain networks associated with DEX trading, including metadata.\nEndpoint: /v4/dex/networks/list\nOptional Query Parameters:\n\nstart, limit (pagination)\n\nsort: id, name\n\nsort_dir: asc, desc\n\naux: alternativeName, cryptocurrencyId, cryptocurrencySlug, wrappedTokenId, etc.\n\n3. 📊 DEX Listings Quotes\nPurpose: List all decentralized exchanges with live trading data.\nEndpoint: /v4/dex/listings/quotes\nOptional:\n\nstart, limit, sort, sort_dir, type, aux, convert_id\nSort options: volume_24h, market_share, name, num_markets\n\n4. 🔁 DEX Pair Quotes Latest\nPurpose: Return latest market quotes for one or more spot pairs.\nEndpoint: /v4/dex/pairs/quotes/latest\nRequired: contract_address or network_id or network_slug\nOptional: aux, convert_id, skip_invalid, reverse_order\n\n5. 📈 DEX OHLCV Historical\nPurpose: Retrieve historical OHLCV (Open, High, Low, Close, Volume) data for spot pairs.\nEndpoint: /v4/dex/pairs/ohlcv/historical\nRequired: contract_address or use network+asset identifiers\nOptional:\n\ntime_period: daily, hourly, 1m, 5m, etc.\n\ntime_start, time_end, count, interval\n\naux, convert_id, skip_invalid, reverse_order\n\n6. 🕒 DEX OHLCV Latest\nPurpose: Returns current-day OHLCV data for spot pairs (real-time snapshot).\nEndpoint: /v4/dex/pairs/ohlcv/latest\nRequired: contract_address or network_id or network_slug\nOptional: aux, convert_id, skip_invalid, reverse_order\n\n7. 🧾 DEX Trades Latest\nPurpose: View the latest trades (up to 100) for one or more spot pairs.\nEndpoint: /v4/dex/pairs/trade/latest\nRequired: contract_address or network_id or network_slug\nOptional: aux, convert_id, skip_invalid, reverse_order\n\n8. 🪙 DEX Spot Pairs Latest\nPurpose: List all active spot trading pairs with latest market data.\nEndpoint: /v4/dex/spot-pairs/latest\nRequired (any of):\n\nnetwork_id, network_slug\n\ndex_id, dex_slug\n\nbase_asset_id, base_asset_symbol, base_asset_contract_address\n\nquote_asset_id, quote_asset_symbol, quote_asset_contract_address\nOptional:\n\nlimit, scroll_id\n\nliquidity_min/max, volume_24h_min/max, percent_change_24h_min/max\n\nsort: name, price, volume_24h, etc.\n\nsort_dir: asc, desc\n\naux, convert_id, reverse_order\n\n⚠️ General Rules to Avoid 400 Errors\nAlways include at least one required identifier per endpoint.\n\nUse proper casing and valid slugs (e.g., ethereum, polygon).\n\nAvoid mixing convert and convert_id.\n\nUse comma-separated values when multiple inputs are allowed.\n\nOnly use documented values in aux, sort, and interval fields.\n\nDo not leave required parameters blank or use unsupported types."
        },
        "promptType": "define"
      },
      "typeVersion": 1.8
    },
    {
      "id": "3101c7f4-cf73-4150-8a17-e11366c07c80",
      "name": "DEXScan Agent Brain",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        -400,
        620
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
          "id": "yUizd8t0sD5wMYVG",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "a596e26a-61eb-4fe1-8a07-3a93694beca0",
      "name": "DEXScan Agent Memory",
      "type": "@n8n/n8n-nodes-langchain.memoryBufferWindow",
      "position": [
        -220,
        620
      ],
      "parameters": {},
      "typeVersion": 1.3
    },
    {
      "id": "49bb58dc-d68b-4091-86f1-12e1071b1fbc",
      "name": "DEX Metadata",
      "type": "@n8n/n8n-nodes-langchain.toolHttpRequest",
      "position": [
        -40,
        620
      ],
      "parameters": {
        "url": "https://pro-api.coinmarketcap.com/v4/dex/listings/info",
        "sendQuery": true,
        "sendHeaders": true,
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "parametersQuery": {
          "values": [
            {
              "name": "id"
            },
            {
              "name": "aux",
              "valueProvider": "modelOptional"
            }
          ]
        },
        "toolDescription": "Returns static metadata for one or more decentralized exchanges, including launch date, description, URLs, and logos.\n\nHere is a precise and complete **tool description** for the `GET /v4/dex/listings/info` endpoint, formatted for use in your n8n agent system or documentation:\n\n---\n\n### 🧭 **DEX Metadata Tool**\n\n**Purpose:**  \nRetrieve static metadata for one or more decentralized exchanges (DEXs) listed on CoinMarketCap. This includes key profile information such as name, status, description, launch date, logos, official URLs, and important notices.\n\n**Endpoint:**  \n`https://pro-api.coinmarketcap.com/v4/dex/listings/info`\n\n---\n\n**Query Parameters:**\n\n- `id` *(string, required)* – One or more comma-separated CoinMarketCap DEX IDs to fetch metadata for.\n- `aux` *(string, optional)* – A comma-separated list of supplemental fields to include in the response.  \n  Valid values:\n  - `\"urls\"` – Official website, social media, and documentation links\n  - `\"logo\"` – Hosted logo (default 64x64, customizable size via URL)\n  - `\"description\"` – Platform description\n  - `\"date_launched\"` – ISO 8601 launch date timestamp\n  - `\"notice\"` – Markdown-formatted warning about operational issues or status alerts\n\n---\n\n**Returns (200 OK):**\n\nFor each exchange:\n- `id`: Unique CoinMarketCap ID\n- `name`: Exchange name\n- `slug`: URL-friendly name\n- `status`: `\"active\"` or `\"inactive\"`\n- `description`: (if requested via `aux`)\n- `date_launched`: (if requested via `aux`)\n- `logo`: (if requested via `aux`)\n- `urls`: (if requested via `aux`)\n- `notice`: Operational message, if applicable\n\n---\n\n**Error Handling:**\n\n- **400 Bad Request**: Triggered if the `id` is missing or invalid.\n- **⚠️ Large Response Alert:** If multiple IDs return too much metadata and exceed the GPT model’s context window, notify with:  \n  > **\"⚠️ The returned metadata exceeds processing limits. Please reduce the number of IDs or narrow the `aux` parameters.\"**\n\n",
        "parametersHeaders": {
          "values": [
            {
              "name": "Accept",
              "value": "application/json",
              "valueProvider": "fieldValue"
            }
          ]
        }
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "OKXROn8aWkgAOvvV",
          "name": "CoinMarketCap Standard"
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "f87838f8-0840-4a78-9d4b-96c79a137d48",
      "name": "DEX Networks List",
      "type": "@n8n/n8n-nodes-langchain.toolHttpRequest",
      "position": [
        140,
        620
      ],
      "parameters": {
        "url": "https://pro-api.coinmarketcap.com/v4/dex/networks/list",
        "sendQuery": true,
        "sendHeaders": true,
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "parametersQuery": {
          "values": [
            {
              "name": "start",
              "valueProvider": "modelOptional"
            },
            {
              "name": "limit",
              "valueProvider": "modelOptional"
            },
            {
              "name": "sort",
              "valueProvider": "modelOptional"
            },
            {
              "name": "sort_dir",
              "valueProvider": "modelOptional"
            },
            {
              "name": "aux",
              "valueProvider": "modelOptional"
            }
          ]
        },
        "toolDescription": "Returns a list of all decentralized exchange (DEX) blockchain networks along with their CoinMarketCap IDs and associated metadata.\n\nOptional query parameters (to avoid errors):\n\nstart (string) – Offset for pagination (1-based index)\n\nlimit (string) – Number of results to return (e.g. \"100\")\n\nsort (string) – Sort field. Valid values: \"id\", \"name\"\n\nsort_dir (string) – Sort order. Valid values: \"asc\", \"desc\"\n\naux (string) – Comma-separated list of extra fields. Valid values:\n\"alternativeName\", \"cryptocurrencyId\", \"cryptocurrenySlug\",\n\"wrappedTokenId\", \"wrappedTokenSlug\", \"tokenExplorerUrl\",\n\"poolExplorerUrl\", \"transactionHashUrl\"\n\nMake sure input values for sort, sort_dir, and aux are spelled exactly as shown to prevent a 400 error response.",
        "parametersHeaders": {
          "values": [
            {
              "name": "Accept",
              "value": "application/json",
              "valueProvider": "fieldValue"
            }
          ]
        }
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "OKXROn8aWkgAOvvV",
          "name": "CoinMarketCap Standard"
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "3f356c20-4efc-479b-b0fa-ab346c7340d8",
      "name": "DEX Listings Quotes",
      "type": "@n8n/n8n-nodes-langchain.toolHttpRequest",
      "position": [
        360,
        620
      ],
      "parameters": {
        "url": "https://pro-api.coinmarketcap.com/v4/dex/listings/quotes",
        "sendQuery": true,
        "sendHeaders": true,
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "parametersQuery": {
          "values": [
            {
              "name": "start",
              "valueProvider": "modelOptional"
            },
            {
              "name": "limit",
              "valueProvider": "modelOptional"
            },
            {
              "name": "sort",
              "valueProvider": "modelOptional"
            },
            {
              "name": "sort_dir",
              "valueProvider": "modelOptional"
            },
            {
              "name": "type",
              "valueProvider": "modelOptional"
            },
            {
              "name": "aux",
              "valueProvider": "modelOptional"
            },
            {
              "name": "convert_id",
              "valueProvider": "modelOptional"
            }
          ]
        },
        "toolDescription": "Returns a paginated list of all decentralized exchanges (DEXs) with their latest market data, including market share, quote volume, trading pairs, and multi-currency conversions.\n\n🛠️ Acceptable Query Inputs:\nstart – Offset pagination start (e.g., \"1\")\n\nlimit – Max results to return\n\nsort – Valid: \"name\", \"volume_24h\", \"market_share\", \"num_markets\"\n\nsort_dir – \"asc\" or \"desc\"\n\ntype – \"all\", \"orderbook\", \"swap\", \"aggregator\"\n\naux – Optional extras, e.g., \"date_launched\"\n\nconvert_id – Currency IDs to convert quote values (up to 30)",
        "parametersHeaders": {
          "values": [
            {
              "name": "Accept",
              "value": "application/json",
              "valueProvider": "fieldValue"
            }
          ]
        }
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "OKXROn8aWkgAOvvV",
          "name": "CoinMarketCap Standard"
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "3fceb769-621f-4e7f-9351-4052d72b3346",
      "name": "DEX Pair Quotes Latest",
      "type": "@n8n/n8n-nodes-langchain.toolHttpRequest",
      "position": [
        560,
        620
      ],
      "parameters": {
        "url": "https://pro-api.coinmarketcap.com/v4/dex/pairs/quotes/latest",
        "sendQuery": true,
        "sendHeaders": true,
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "parametersQuery": {
          "values": [
            {
              "name": "contract_address",
              "valueProvider": "modelOptional"
            },
            {
              "name": "network_id",
              "valueProvider": "modelOptional"
            },
            {
              "name": "aux",
              "valueProvider": "modelOptional"
            },
            {
              "name": "convert_id",
              "valueProvider": "modelOptional"
            },
            {
              "name": "skip_invalid",
              "valueProvider": "modelOptional"
            },
            {
              "name": "reverse_order",
              "valueProvider": "modelOptional"
            },
            {
              "name": "network_slug",
              "valueProvider": "modelOptional"
            }
          ]
        },
        "toolDescription": "Returns the latest market quote for one or more DEX spot trading pairs, including metrics like:\n\nLiquidity\n\n24h buy/sell volume\n\nSecurity scans\n\nBuy/sell tax\n\nPercent pooled\n\nPool creation and supply stats\n\n🛠️ Query Parameters Supported:\n\ncontract_address – (Comma-separated smart contract addresses)\n\nnetwork_id – CMC network IDs\n\nnetwork_slug – Slug-formatted network names (e.g., ethereum, polygon)\n\naux – Comma-separated fields:\npool_created, percent_pooled_base_asset, num_transactions_24h,\npool_base_asset, pool_quote_asset, 24h_volume_quote_asset,\ntotal_supply_quote_asset, total_supply_base_asset, holders,\nbuy_tax, sell_tax, security_scan, 24h_no_of_buys, 24h_no_of_sells,\n24h_buy_volume, 24h_sell_volume\n\nconvert_id – Comma-separated CMC currency IDs for conversion\n\nskip_invalid – Pass \"true\" to ignore invalid results\n\nreverse_order – Pass \"true\" to invert base/quote pair display",
        "parametersHeaders": {
          "values": [
            {
              "name": "Accept",
              "value": "application/json",
              "valueProvider": "fieldValue"
            }
          ]
        }
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "OKXROn8aWkgAOvvV",
          "name": "CoinMarketCap Standard"
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "134d7fc5-15cf-4897-92bb-97b18a121e41",
      "name": "DEX OHLCV Historical",
      "type": "@n8n/n8n-nodes-langchain.toolHttpRequest",
      "position": [
        740,
        620
      ],
      "parameters": {
        "url": "https://pro-api.coinmarketcap.com/v4/dex/pairs/ohlcv/historical",
        "sendQuery": true,
        "sendHeaders": true,
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "parametersQuery": {
          "values": [
            {
              "name": "contract_address",
              "valueProvider": "modelOptional"
            },
            {
              "name": "network_id",
              "valueProvider": "modelOptional"
            },
            {
              "name": "network_slug",
              "valueProvider": "modelOptional"
            },
            {
              "name": "time_period",
              "valueProvider": "modelOptional"
            },
            {
              "name": "time_start",
              "valueProvider": "modelOptional"
            },
            {
              "name": "time_end",
              "valueProvider": "modelOptional"
            },
            {
              "name": "count",
              "valueProvider": "modelOptional"
            },
            {
              "name": "interval",
              "valueProvider": "modelOptional"
            },
            {
              "name": "aux",
              "valueProvider": "modelOptional"
            },
            {
              "name": "convert_id",
              "valueProvider": "modelOptional"
            },
            {
              "name": "skip_invalid",
              "valueProvider": "modelOptional"
            },
            {
              "name": "reverse_order",
              "valueProvider": "modelOptional"
            }
          ]
        },
        "toolDescription": "This tool retrieves historical OHLCV (Open, High, Low, Close, Volume) data for DEX spot trading pairs. It includes optional data on security risks, transaction activity, supply, and tax information. Supports flexible time range and sampling intervals for charting or backtesting.\n\n✅ Valid Query Parameters:\n\ncontract_address (string) – A single DEX spot pair’s smart contract address (required unless using network + asset options).\n\nnetwork_id (string) – One or more CMC network IDs.\n\nnetwork_slug (string) – Friendly name slug of the network (e.g., \"ethereum\").\n\ntime_period (string) – Time unit for OHLCV data.\nAllowed: \"daily\", \"hourly\", \"1m\", \"5m\", \"15m\", \"30m\", \"4h\", \"8h\", \"12h\", \"weekly\", \"monthly\"\n(Default: \"daily\")\n\ntime_start (string) – ISO or Unix timestamp for start (e.g., \"2024-01-01\").\n\ntime_end (string) – ISO or Unix timestamp for end (e.g., \"2024-03-01\"). Optional.\n\ncount (string) – Number of time intervals to return (default is 10, max is 500).\n\ninterval (string) – How frequently to sample the time_period. Same options as time_period.\n\naux (string) – Optional comma-separated extra fields to return: pool_created, percent_pooled_base_asset, num_transactions_24h,\npool_base_asset, pool_quote_asset, 24h_volume_quote_asset,\ntotal_supply_quote_asset, total_supply_base_asset, holders,\nbuy_tax, sell_tax, security_scan, 24h_no_of_buys, 24h_no_of_sells,\n24h_buy_volume, 24h_sell_volume\n\nconvert_id (string) – Comma-separated CMC currency IDs for market conversion (e.g., \"1,2781\").\n\nskip_invalid (string) – Pass \"true\" to skip failed lookups in bulk queries.\n\nreverse_order (string) – Pass \"true\" to reverse base/quote asset display order.",
        "parametersHeaders": {
          "values": [
            {
              "name": "Accept",
              "value": "application/json",
              "valueProvider": "fieldValue"
            }
          ]
        }
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "OKXROn8aWkgAOvvV",
          "name": "CoinMarketCap Standard"
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "bee1d41a-af4c-442d-b0c6-7be0e17c31a5",
      "name": "DEX OHLCV Latest",
      "type": "@n8n/n8n-nodes-langchain.toolHttpRequest",
      "position": [
        940,
        640
      ],
      "parameters": {
        "url": "https://pro-api.coinmarketcap.com/v4/dex/pairs/ohlcv/latest",
        "sendQuery": true,
        "sendHeaders": true,
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "parametersQuery": {
          "values": [
            {
              "name": "contract_address",
              "valueProvider": "modelOptional"
            },
            {
              "name": "network_id",
              "valueProvider": "modelOptional"
            },
            {
              "name": "network_slug",
              "valueProvider": "modelOptional"
            },
            {
              "name": "aux",
              "valueProvider": "modelOptional"
            },
            {
              "name": "convert_id",
              "valueProvider": "modelOptional"
            },
            {
              "name": "skip_invalid",
              "valueProvider": "modelOptional"
            },
            {
              "name": "reverse_order",
              "valueProvider": "modelOptional"
            }
          ]
        },
        "toolDescription": "This tool retrieves the most recent OHLCV (Open, High, Low, Close, Volume) data for one or more spot trading pairs on decentralized exchanges. It reflects market activity during the current UTC day and is continuously updated. Suitable for real-time monitoring of decentralized market performance, this tool supports advanced filtering via network identifiers or contract addresses.\n\nRequired Input (at least one of the following):\ncontract_address (string)\nOne or more comma-separated smart contract addresses for the trading pair(s).\n\nExample: \"0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640\"\n\nnetwork_id (string)\nOne or more CoinMarketCap internal network IDs.\n\nExample: \"1\" (Ethereum)\n\nnetwork_slug (string)\nThe lowercase, hyphenated identifier of a blockchain network.\n\nExample: \"ethereum\", \"binance-smart-chain\"\n\n🧩 Optional Query Parameters:\naux (string)\nComma-separated list of additional fields to enrich the returned data:\nValid values: pool_created, percent_pooled_base_asset, num_transactions_24h,\npool_base_asset, pool_quote_asset, 24h_volume_quote_asset,\ntotal_supply_quote_asset, total_supply_base_asset, holders,\nbuy_tax, sell_tax, security_scan, 24h_no_of_buys, 24h_no_of_sells,\n24h_buy_volume, 24h_sell_volume\n\nExample: \"security_scan,holders,pool_created\"\n\nconvert_id (string)\nCalculate quote values in one or more fiat/crypto currencies using CoinMarketCap IDs.\n\nExample: \"1\" (USD), \"2781\" (BTC)\n\nNote: Cannot be used with the convert symbol-based parameter.\n\nskip_invalid (string)\nAccepts \"true\" or \"false\" (default).\nIf set to \"true\", skips spot pairs with invalid or missing data instead of returning a 400 error.\n\nExample: \"true\"\n\nreverse_order (string)\nAccepts \"true\" or \"false\" (default).\nFlips the order of the token pair if the token contract uses reverse naming convention.\n\nExample: \"true\"\n\n⚠️ Tips to Avoid 400 Errors:\nEnsure at least one of contract_address, network_id, or network_slug is included.\n\nUse correct spelling and case for slugs (e.g., \"ethereum\" not \"Ethereum\").\n\nOnly include valid aux values in a comma-separated list.\n\nDo not use both convert and convert_id at the same time.\n\nAvoid empty strings for required parameters or unsupported values in optional fields.",
        "parametersHeaders": {
          "values": [
            {
              "name": "Accept",
              "value": "application/json",
              "valueProvider": "fieldValue"
            }
          ]
        }
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "OKXROn8aWkgAOvvV",
          "name": "CoinMarketCap Standard"
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "742a6f07-d85d-4b6c-9ba6-90940e2b365c",
      "name": "DEX Trades Latest",
      "type": "@n8n/n8n-nodes-langchain.toolHttpRequest",
      "position": [
        1140,
        640
      ],
      "parameters": {
        "url": "https://pro-api.coinmarketcap.com/v4/dex/pairs/trade/latest",
        "sendQuery": true,
        "sendHeaders": true,
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "parametersQuery": {
          "values": [
            {
              "name": "contract_address",
              "valueProvider": "modelOptional"
            },
            {
              "name": "network_id",
              "valueProvider": "modelOptional"
            },
            {
              "name": "network_slug",
              "valueProvider": "modelOptional"
            },
            {
              "name": "aux",
              "valueProvider": "modelOptional"
            },
            {
              "name": "convert_id",
              "valueProvider": "modelOptional"
            },
            {
              "name": "skip_invalid",
              "valueProvider": "modelOptional"
            },
            {
              "name": "reverse_order",
              "valueProvider": "modelOptional"
            }
          ]
        },
        "toolDescription": "Returns up to the latest 100 trades for one or more DEX spot pairs using CoinMarketCap.\nQuery Parameters Accepted:\n\ncontract_address: (Required*) One or more comma-separated contract addresses.\n\nnetwork_id: CoinMarketCap network ID (alternative to contract_address).\n\nnetwork_slug: URL-friendly network name (alternative to network_id).\n\naux: Optional fields to include: \"transaction_hash\", \"blockchain_explorer_link\".\n\nconvert_id: One or more fiat/crypto IDs to return converted market values.\n\nskip_invalid: \"true\" to skip invalid pairs instead of erroring.\n\nreverse_order: \"true\" to reverse trading pair (e.g., A/B → B/A).\n\nUse at least one of contract_address, network_id, or network_slug to avoid a 400 error.",
        "parametersHeaders": {
          "values": [
            {
              "name": "Accept",
              "value": "application/json",
              "valueProvider": "fieldValue"
            }
          ]
        }
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "OKXROn8aWkgAOvvV",
          "name": "CoinMarketCap Standard"
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "3ddf229c-16b2-4610-982e-d5e3c07b0cb0",
      "name": "DEX Spot Pairs Latest",
      "type": "@n8n/n8n-nodes-langchain.toolHttpRequest",
      "position": [
        1340,
        640
      ],
      "parameters": {
        "url": "https://pro-api.coinmarketcap.com/v4/dex/spot-pairs/latest",
        "sendQuery": true,
        "sendHeaders": true,
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "parametersQuery": {
          "values": [
            {
              "name": "network_id",
              "valueProvider": "modelOptional"
            },
            {
              "name": "network_slug",
              "valueProvider": "modelOptional"
            },
            {
              "name": "dex_id",
              "valueProvider": "modelOptional"
            },
            {
              "name": "dex_slug",
              "valueProvider": "modelOptional"
            },
            {
              "name": "base_asset_id",
              "valueProvider": "modelOptional"
            },
            {
              "name": "base_asset_symbol",
              "valueProvider": "modelOptional"
            },
            {
              "name": "base_asset_contract_address",
              "valueProvider": "modelOptional"
            },
            {
              "name": "base_asset_ucid",
              "valueProvider": "modelOptional"
            },
            {
              "name": "quote_asset_id",
              "valueProvider": "modelOptional"
            },
            {
              "name": "quote_asset_symbol",
              "valueProvider": "modelOptional"
            },
            {
              "name": "quote_asset_contract_address",
              "valueProvider": "modelOptional"
            },
            {
              "name": "quote_asset_ucid",
              "valueProvider": "modelOptional"
            },
            {
              "name": "scroll_id",
              "valueProvider": "modelOptional"
            },
            {
              "name": "limit",
              "valueProvider": "modelOptional"
            },
            {
              "name": "liquidity_min",
              "valueProvider": "modelOptional"
            },
            {
              "name": "liquidity_max",
              "valueProvider": "modelOptional"
            },
            {
              "name": "volume_24h_min",
              "valueProvider": "modelOptional"
            },
            {
              "name": "volume_24h_max",
              "valueProvider": "modelOptional"
            },
            {
              "name": "no_of_transactions_24h_min",
              "valueProvider": "modelOptional"
            },
            {
              "name": "no_of_transactions_24h_max",
              "valueProvider": "modelOptional"
            },
            {
              "name": "percent_change_24h_min",
              "valueProvider": "modelOptional"
            },
            {
              "name": "percent_change_24h_max",
              "valueProvider": "modelOptional"
            },
            {
              "name": "sort",
              "valueProvider": "modelOptional"
            },
            {
              "name": "sort_dir",
              "valueProvider": "modelOptional"
            },
            {
              "name": "aux",
              "valueProvider": "modelOptional"
            },
            {
              "name": "reverse_order",
              "valueProvider": "modelOptional"
            },
            {
              "name": "convert_id",
              "valueProvider": "modelOptional"
            }
          ]
        },
        "toolDescription": "This tool calls the /v4/dex/spot-pairs/latest endpoint to retrieve a paginated list of all active decentralized exchange (DEX) spot pairs with the latest market data. This includes price, liquidity, trading volume, and more. You can filter, sort, and enrich the results using query parameters.\n\n⚠️ To avoid a 400 Bad Request error, you must include at least one of the following identifiers in your request:\n\nnetwork_id OR network_slug\n\ndex_id OR dex_slug\n\nbase_asset_id, base_asset_symbol, or base_asset_contract_address\n\nquote_asset_id, quote_asset_symbol, or quote_asset_contract_address\n\n✅ Supported Query Parameters\nCore Identifiers (At least one required):\nnetwork_id: One or more comma-separated CoinMarketCap network IDs.\n\nnetwork_slug: One or more comma-separated URL-friendly network slugs.\n\ndex_id: One or more CoinMarketCap DEX exchange IDs.\n\ndex_slug: One or more URL-friendly DEX slugs.\n\nbase_asset_id, base_asset_symbol, base_asset_contract_address: Identify the base asset of the pair.\n\nquote_asset_id, quote_asset_symbol, quote_asset_contract_address: Identify the quote asset of the pair.\n\nbase_asset_ucid / quote_asset_ucid: Optional unique CoinMarketCap identifiers.\n\nPagination:\nscroll_id: For continuous pagination. Use the scroll_id from the previous response to get the next set.\n\nlimit: Maximum number of results to return.\n\nFiltering:\nliquidity_min, liquidity_max: Minimum/maximum liquidity thresholds.\n\nvolume_24h_min, volume_24h_max: Minimum/maximum 24h volume thresholds.\n\nno_of_transactions_24h_min, no_of_transactions_24h_max: Filter by transaction count.\n\npercent_change_24h_min, percent_change_24h_max: 24-hour price change filters.\n\nSorting:\nsort: Sort the results by:\n\nname, date_added, price, volume_24h, percent_change_1h, percent_change_24h, liquidity, fully_diluted_value, no_of_transactions_24h\n\nsort_dir: Direction of sort (asc or desc, default: desc)\n\nAdditional Metadata (Optional):\nUse the aux parameter to enrich the response with supplemental fields:\n\npool_created, percent_pooled_base_asset, num_transactions_24h, pool_base_asset, pool_quote_asset, 24h_volume_quote_asset, total_supply_quote_asset, total_supply_base_asset, holders, buy_tax, sell_tax, security_scan, 24h_no_of_buys, 24h_no_of_sells, 24h_buy_volume, 24h_sell_volume\n\nQuote Conversion:\nconvert_id: Convert pricing to specific fiat or crypto by CMC ID (e.g. convert_id=1,2781 for BTC, USD).\n\n⚠️ Cannot be used with convert (symbol-based conversion).\n\nOther Options:\nreverse_order: Flip the base/quote asset order if needed.",
        "parametersHeaders": {
          "values": [
            {
              "name": "Accept",
              "value": "application/json",
              "valueProvider": "fieldValue"
            }
          ]
        }
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "OKXROn8aWkgAOvvV",
          "name": "CoinMarketCap Standard"
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "3dab3ebc-14c5-49a8-bb11-aa82564785a5",
      "name": "DEXScan Agent Guide",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -1580,
        -760
      ],
      "parameters": {
        "width": 1080,
        "height": 1420,
        "content": "# 📊 CoinMarketCap DEXScan AI Agent Tool (n8n Workflow)\n\n## 🧠 Multi-Agent System: DEXScan Agent\nThis workflow powers **DEX intelligence capabilities** in the CoinMarketCap AI Analyst ecosystem. It enables deep insights into **liquidity**, **volume**, **spot pairs**, and **trading activity** across decentralized exchanges.\n\n---\n\n### 🔧 Connected DEX Tools:\n1. **DEX Metadata** – `/v4/dex/listings/info`\n2. **DEX Networks List** – `/v4/dex/networks/list`\n3. **DEX Listings Quotes** – `/v4/dex/listings/quotes`\n4. **DEX Pair Quotes Latest** – `/v4/dex/pairs/quotes/latest`\n5. **DEX OHLCV Historical** – `/v4/dex/pairs/ohlcv/historical`\n6. **DEX OHLCV Latest** – `/v4/dex/pairs/ohlcv/latest`\n7. **DEX Trades Latest** – `/v4/dex/pairs/trade/latest`\n8. **DEX Spot Pairs Latest** – `/v4/dex/spot-pairs/latest`\n\n---\n\n## ✅ Key Capabilities:\n- View real-time DEX liquidity and 24h trading volume\n- Retrieve metadata (logos, URLs, launch info) for decentralized exchanges\n- Track market pair quotes, liquidity, and spot pair data\n- Monitor historical OHLCV data for technical analysis\n- Identify recent trades and pair-specific activity\n\n---\n\n## 🧠 Agent Structure\n### **1️⃣ DEXScan Brain**\n- **Type**: GPT-4o Mini\n- **Function**: Understands queries, routes tools, summarizes results\n\n### **2️⃣ Session Memory**\n- Maintains contextual state via memory buffer\n\n### **3️⃣ Tool Triggers**\n- **HTTP Tools:** Each CMC endpoint is mapped to one of 8 tool nodes with rich parameter control\n\n---\n\n## ⚠️ Notes:\n- Use **`contract_address`**, **`network_slug`**, or **`network_id`** in nearly all endpoints\n- Avoid using both `convert` and `convert_id` in the same query\n- Be cautious of high-volume requests which may exceed token limits (e.g., when requesting OHLCV for many intervals)\n\n---\n\n📎 API responses are designed for fine-tuned filtering. You can retrieve:\n- Top trading pairs on Polygon\n- Volume-based DEX rankings\n- Historical trade data for a Uniswap pair\n- Real-time liquidity on Solana spot pairs"
      },
      "typeVersion": 1
    },
    {
      "id": "af395be6-3683-478e-bffd-087ffa8dc8c9",
      "name": "DEX Usage + Examples",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -100,
        -760
      ],
      "parameters": {
        "color": 5,
        "width": 960,
        "height": 1000,
        "content": "## 📌 How to Use the Workflow\n\n### ✅ Step 1: Provide Inputs\nUse `contract_address`, `network_slug`, `dex_slug`, or `convert_id` as needed\n\n### ✅ Step 2: Trigger From Supervisor Agent\nParent agent forwards user message and sessionId to DEXScan\n\n### ✅ Step 3: DEX Data is Returned\nData can be streamed to Telegram, dashboards, or HTTP response\n\n---\n\n## 🔍 Example API Calls\n\n### 1️⃣ Get Top DEXs by 24h Volume\n```plaintext\nGET /v4/dex/listings/quotes?sort=volume_24h&limit=5\n```\n\n### 2️⃣ Query Historical OHLCV for SOL-USDT\n```plaintext\nGET /v4/dex/pairs/ohlcv/historical?network=solana&pair=SOL-USDT&interval=1d\n```\n\n### 3️⃣ Latest Trades on a Uniswap Pair\n```plaintext\nGET /v4/dex/pairs/trade/latest?contract_address=0x...&network_slug=ethereum\n```\n\n### 4️⃣ Spot Pairs on Polygon\n```plaintext\nGET /v4/dex/spot-pairs/latest?network_slug=polygon&sort=volume_24h\n```\n\n### 5️⃣ DEX Metadata for PancakeSwap\n```plaintext\nGET /v4/dex/listings/info?id=123&aux=logo,description,date_launched\n```"
      },
      "typeVersion": 1
    },
    {
      "id": "0fcffddb-d343-4739-917a-878925673295",
      "name": "DEX Errors + IP Notice",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1220,
        -760
      ],
      "parameters": {
        "color": 3,
        "width": 740,
        "height": 600,
        "content": "## ⚠️ DEXScan Error Codes & Fixes\n\n| Code | Message |\n|------|---------|\n| `200` | Success |\n| `400` | Bad Request – missing/invalid query |\n| `401` | Unauthorized – invalid API key |\n| `429` | Rate limit exceeded |\n| `500` | Server error |\n\n### 🔍 Fixes:\n- Always use at least 1 required param: `contract_address`, `network_slug`, etc.\n- Double-check slugs and convert ID formats\n- Don’t mix `convert` and `convert_id`\n- Avoid oversized `aux` and `interval` combinations\n\n---\n\n## 🚀 Support & Licensing\n\n🔗 **Don Jayamaha – LinkedIn**  \n[http://linkedin.com/in/donjayamahajr](http://linkedin.com/in/donjayamahajr)\n\n© 2025 Treasurium Capital Limited Company. All rights reserved.\nThis AI workflow architecture, including logic, design, and prompt structures, is the intellectual property of Treasurium Capital Limited Company. Unauthorized reproduction, redistribution, or resale is prohibited under U.S. copyright law. Licensed use only."
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "2507ec1c-d0e3-45ef-aca6-f16c81f9cf17",
  "connections": {
    "DEX Metadata": {
      "ai_tool": [
        [
          {
            "node": "CoinMarketCap DEXScan Agent",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "DEX OHLCV Latest": {
      "ai_tool": [
        [
          {
            "node": "CoinMarketCap DEXScan Agent",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "DEX Networks List": {
      "ai_tool": [
        [
          {
            "node": "CoinMarketCap DEXScan Agent",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "DEX Trades Latest": {
      "ai_tool": [
        [
          {
            "node": "CoinMarketCap DEXScan Agent",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "DEX Listings Quotes": {
      "ai_tool": [
        [
          {
            "node": "CoinMarketCap DEXScan Agent",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "DEXScan Agent Brain": {
      "ai_languageModel": [
        [
          {
            "node": "CoinMarketCap DEXScan Agent",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "DEX OHLCV Historical": {
      "ai_tool": [
        [
          {
            "node": "CoinMarketCap DEXScan Agent",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "DEXScan Agent Memory": {
      "ai_memory": [
        [
          {
            "node": "CoinMarketCap DEXScan Agent",
            "type": "ai_memory",
            "index": 0
          }
        ]
      ]
    },
    "DEX Spot Pairs Latest": {
      "ai_tool": [
        [
          {
            "node": "CoinMarketCap DEXScan Agent",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "DEX Pair Quotes Latest": {
      "ai_tool": [
        [
          {
            "node": "CoinMarketCap DEXScan Agent",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "When Executed by Another Workflow": {
      "main": [
        [
          {
            "node": "CoinMarketCap DEXScan Agent",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-1714"></a>

## Template 1714 - Arquivar duplicatas em banco de dados Notion

- **Nome:** Arquivar duplicatas em banco de dados Notion
- **Descrição:** Este fluxo identifica itens duplicados em um banco de dados e arquiva (exclui) as cópias, mantendo apenas uma opção por valor de propriedade.
- **Funcionalidade:** • Detecção de duplicatas: identifica itens duplicados com base no valor de uma propriedade específica.
• Coleta de dados: busca todas as páginas do banco de dados.
• Preparação dos itens: formata cada item com campos necessários, incluindo o id e a propriedade a checar.
• Agrupamento de dados: agrega as informações para facilitar a verificação de duplicatas.
• Filtragem de duplicatas: seleciona apenas as entradas duplicadas com o mesmo valor de propriedade.
• Arquivamento de duplicatas: arquiva as páginas duplicadas, mantendo apenas uma cópia.
• Gatilhos de execução: executa automaticamente ao adicionar novas páginas ou em intervalos diários.
- **Ferramentas:** • Notion API: API utilizada para ler e arquivar páginas no banco de dados.



## Fluxo visual

```mermaid
flowchart LR
    N1["Every day"]
    N2["Get pages from database"]
    N3["Aggregate all items"]
    N4["Format items properly"]
    N5["Filter duplicates"]
    N6["Archive pages"]
    N7["When a page is added to the database"]
    N8["Sticky Note"]
    N9["Sticky Note1"]
    N10["Sticky Note2"]
    N11["Sticky Note3"]

    N1 --> N2
    N5 --> N6
    N3 --> N5
    N4 --> N3
    N2 --> N4
    N7 --> N2
```

## Fluxo (.json) :

```json
{
  "id": "As8TxF3PjyXygc0o",
  "meta": {
    "instanceId": "a059b3dfdab56aa587cc6a2c8635f6f2700cf0c7064dbfb5981c26f7ad9eab88"
  },
  "name": "🧹 Archive (delete) duplicate items from a Notion database",
  "tags": [],
  "nodes": [
    {
      "id": "b758ce01-7f5e-4bdc-a4c3-6c00d6bc022a",
      "name": "Every day",
      "type": "n8n-nodes-base.scheduleTrigger",
      "position": [
        -180,
        660
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
      "id": "1ca45ba5-4635-4710-9807-26f22d535059",
      "name": "Get pages from database",
      "type": "n8n-nodes-base.notion",
      "position": [
        60,
        560
      ],
      "parameters": {
        "options": {},
        "resource": "databasePage",
        "operation": "getAll",
        "returnAll": true,
        "databaseId": {
          "__rl": true,
          "mode": "list",
          "value": ""
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "ef8c8cfa-12fb-4fb9-8552-09f69f1f358d",
      "name": "Aggregate all items",
      "type": "n8n-nodes-base.aggregate",
      "position": [
        500,
        560
      ],
      "parameters": {
        "options": {},
        "aggregate": "aggregateAllItemData",
        "destinationFieldName": "pages"
      },
      "typeVersion": 1
    },
    {
      "id": "f1c3c0ad-f904-4d63-a131-0b045a21ce04",
      "name": "Format items properly",
      "type": "n8n-nodes-base.set",
      "position": [
        280,
        560
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "309a1e9b-f3e9-41a0-aadb-aa74bc993fe9",
              "name": "id",
              "type": "string",
              "value": "={{ $json.id }}"
            },
            {
              "id": "ad6e8fa9-9872-456d-971f-3cef940b7d8a",
              "name": "property_to_check",
              "type": "string",
              "value": "=\"SET YOUR PROPERTY HERE\""
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "5d39d3b7-604d-4aca-bf9a-3bb09bddad66",
      "name": "Filter duplicates",
      "type": "n8n-nodes-base.code",
      "position": [
        720,
        560
      ],
      "parameters": {
        "jsCode": "const inputData = $input.first().json.pages;\n\nconst seen = new Set();\nconst duplicates = new Map();\n\ninputData.forEach(item => {\n  const propertyValue = item.property_to_check;\n  if (seen.has(propertyValue)) {\n    duplicates.set(propertyValue, item);\n  } else {\n    seen.add(propertyValue);\n  }\n});\n\nconst output = Array.from(duplicates.values()).map(item => ({ json: item }));\n\nreturn output;"
      },
      "typeVersion": 2
    },
    {
      "id": "55a8f0eb-702b-4056-a28c-96a7ade7c2cd",
      "name": "Archive pages",
      "type": "n8n-nodes-base.notion",
      "position": [
        920,
        560
      ],
      "parameters": {
        "pageId": {
          "__rl": true,
          "mode": "id",
          "value": "={{ $json.id }}"
        },
        "operation": "archive"
      },
      "typeVersion": 2.2
    },
    {
      "id": "2c9655ea-401c-410b-a4b1-b001ae6dbe4b",
      "name": "When a page is added to the database",
      "type": "n8n-nodes-base.notionTrigger",
      "position": [
        -180,
        460
      ],
      "parameters": {
        "pollTimes": {
          "item": [
            {
              "mode": "everyMinute"
            }
          ]
        },
        "databaseId": {
          "__rl": true,
          "mode": "list",
          "value": ""
        }
      },
      "typeVersion": 1
    },
    {
      "id": "672b647c-d009-45c3-b69e-6dfe85992e15",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        0,
        0
      ],
      "parameters": {
        "width": 860,
        "height": 460,
        "content": "## 🧹 Archive (delete) extra duplicate items from Notion database\n### ABOUT THIS WORKFLOW\nThis n8n workflow automatically gets duplicate database pages based on a property and \"archives\" them (equivalent to deleting them), leaving just one copy.\n\n### SETUP\n1. Create a Notion credential.\n2. Add it to the Notion nodes, selecting the appropriate database.\n3. In the \"Set\" node (\"Format items properly\"), specify a reference to the property you want to check for duplicates and assign it to the field \"property_to_check\". I recommend using the n8n property drag-and-drop feature.\n4. Enjoy!\n\n### ABOUT THE TRIGGERS\nThis workflow offers two possible triggers by default:\n- Run every time a page is added to the database.\n- Run every day.\n\n\nYou can enable, disable, or modify these triggers as you like."
      },
      "typeVersion": 1
    },
    {
      "id": "83881bd3-60e3-40be-a469-0b7acb21d2be",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -240,
        400
      ],
      "parameters": {
        "color": 5,
        "width": 220,
        "height": 420,
        "content": "## TRIGGERS"
      },
      "typeVersion": 1
    },
    {
      "id": "cd4b8717-19ae-42d6-ac87-bbdd071dd774",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        0,
        480
      ],
      "parameters": {
        "color": 6,
        "width": 860,
        "height": 340,
        "content": "## GET DUPLICATE PAGES"
      },
      "typeVersion": 1
    },
    {
      "id": "087fb844-2241-4ed9-976d-9bdc7ccd8aa5",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        880,
        400
      ],
      "parameters": {
        "color": 3,
        "width": 180,
        "height": 420,
        "content": "## ARCHIVE (DELETE)"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "fdd2e5ad-4ff5-4432-a5f9-ebbeb1a1a6cb",
  "connections": {
    "Every day": {
      "main": [
        [
          {
            "node": "Get pages from database",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Filter duplicates": {
      "main": [
        [
          {
            "node": "Archive pages",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Aggregate all items": {
      "main": [
        [
          {
            "node": "Filter duplicates",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Format items properly": {
      "main": [
        [
          {
            "node": "Aggregate all items",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get pages from database": {
      "main": [
        [
          {
            "node": "Format items properly",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "When a page is added to the database": {
      "main": [
        [
          {
            "node": "Get pages from database",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-1716"></a>

## Template 1716 - Assistente de previsão do tempo com Open-Meteo e IA

- **Nome:** Assistente de previsão do tempo com Open-Meteo e IA
- **Descrição:** Recebe pedidos via chat, usa um modelo de linguagem para obter coordenadas de uma cidade e consultar a previsão do tempo, retornando um resumo ao usuário.
- **Funcionalidade:** • Receber e processar mensagens de chat: aceita mensagens de usuário através de um endpoint de chat.
• Manter contexto de conversa: armazena e reutiliza histórico de interação para respostas mais coerentes.
• Agente de IA para orquestração: determina quais ferramentas chamar e em que ordem, com base na intenção do usuário.
• Consulta de geolocalização: obtém latitude e longitude de um nome de cidade usando um serviço de geocodificação.
• Obtenção de previsão meteorológica: consulta a previsão diária (ex.: temperatura máxima e precipitação) passando coordenadas e número de dias.
• Resposta formatada ao usuário: gera e devolve um resumo compreensível da previsão, incluindo parâmetros solicitados como dias de previsão e fuso horário.
- **Ferramentas:** • Open-Meteo Geocoding API: serviço que converte o nome de uma cidade em coordenadas geográficas (latitude/longitude).
• Open-Meteo Forecast API: serviço que fornece previsões meteorológicas diárias, incluindo temperatura e precipitação.
• OpenAI (modelo de linguagem): modelo de IA usado para interpretar a solicitação do usuário, escolher quais chamadas de API realizar e formatar a resposta final.

## Fluxo visual

```mermaid
flowchart LR
    N1["When chat message received"]
    N2["OpenAI Chat Model"]
    N3["Sticky Note"]
    N4["Sticky Note1"]
    N5["Generic AI Tool Agent"]
    N6["Chat Memory Buffer"]
    N7["Sticky Note2"]
    N8["Sticky Note5"]
    N9["A tool to get the weather forecast based on geolocation"]
    N10["Sticky Note6"]
    N11["A tool for inputting the city and obtaining geolocation"]
    N12["Sticky Note4"]

    N1 --> N5
```

## Fluxo (.json) :

```json
{
  "id": "Nfh274NHoDy7pB4M",
  "meta": {
    "instanceId": "00493e38fecfc163cb182114bc2fab90114038eb9aad665a7a752d076920d3d5",
    "templateCredsSetupCompleted": true
  },
  "name": "Integrating AI with Open-Meteo API for Enhanced Weather Forecasting",
  "tags": [],
  "nodes": [
    {
      "id": "80debfe0-c591-4ba1-aca1-068adac62aa9",
      "name": "When chat message received",
      "type": "@n8n/n8n-nodes-langchain.chatTrigger",
      "position": [
        100,
        -300
      ],
      "webhookId": "4a44e974-db62-4727-9913-12a22bc88e01",
      "parameters": {
        "public": true,
        "options": {
          "title": "N8N 👋",
          "subtitle": "Weather Assistant: Example of Tools Using ChatGPT",
          "allowFileUploads": false,
          "loadPreviousSession": "memory"
        },
        "initialMessages": "Type like this: Weather Forecast for the Next 7 Days in São Paulo"
      },
      "typeVersion": 1.1
    },
    {
      "id": "ec375027-1c0d-438b-9fca-7bc4fbef2479",
      "name": "OpenAI Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        420,
        -60
      ],
      "parameters": {
        "options": {}
      },
      "credentials": {
        "openAiApi": {
          "id": "bhRvwBXztNmJVObo",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "bd2f5967-8188-4b1f-9255-8008870aaf7b",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -540,
        -640
      ],
      "parameters": {
        "color": 5,
        "width": 500,
        "height": 720,
        "content": "## Integrating AI with Open-Meteo API for Enhanced Weather Forecasting\n\n## Use case\n\n### Workshop\n\nWe are using this workflow in our workshops to teach how to use Tools a.k.a functions with artificial intelligence. In this specific case, we will use a generic \"AI Agent\" node to illustrate that it could use other models from different data providers.\n\n### Enhanced Weather Forecasting\n\nIn this small example, it's easy to demonstrate how to obtain weather forecast results from the Open-Meteo site to accurately display the upcoming days.\n\nThis can be used to plan travel decisions, for example.\n\n## What this workflow does\n\n1. We will make an HTTP request to find out the geographic coordinates of a city.\n2. Then, we will make other HTTP requests to discover the weather for the upcoming days.\n\nIn this workshop, we demonstrate that the AI will be able to determine which tool to call first—it will first call the geolocation tool and then the weather forecast tool. All of this within a single client conversation call.\n\n\n## Setup\n\nInsert an OpenAI Key and activate the workflow.\n\nby Davi Saranszky Mesquita\nhttps://www.linkedin.com/in/mesquitadavi/"
      },
      "typeVersion": 1
    },
    {
      "id": "3cfeea52-a310-4101-8377-0f393bf54c8d",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        60,
        -440
      ],
      "parameters": {
        "width": 340,
        "height": 220,
        "content": "## Create an Hosted Web Chat\n\n### And setup the trigger!\n\nExample: https://website/webhook/4a4..../chat"
      },
      "typeVersion": 1
    },
    {
      "id": "55713ffc-da61-4594-99f4-ca6b448cbee2",
      "name": "Generic AI Tool Agent",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        440,
        -300
      ],
      "parameters": {
        "options": {}
      },
      "typeVersion": 1.7
    },
    {
      "id": "7f608ddc-87bb-4e54-84a8-4db6b7f95011",
      "name": "Chat Memory Buffer",
      "type": "@n8n/n8n-nodes-langchain.memoryBufferWindow",
      "position": [
        200,
        -60
      ],
      "parameters": {},
      "typeVersion": 1.3
    },
    {
      "id": "77f82443-1efe-47d3-92ec-aa193853c8a5",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        320,
        0
      ],
      "parameters": {
        "width": 260,
        "content": "-\n\n\n## Setup OpenAI Key"
      },
      "typeVersion": 1
    },
    {
      "id": "ed37ea94-3cff-47cb-bf45-bce620b0f056",
      "name": "Sticky Note5",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        780,
        60
      ],
      "parameters": {
        "color": 4,
        "width": 280,
        "height": 360,
        "content": "### Open Meteo SPEC - City Geolocation\n\nThis tool will go to the URL https://geocoding-api.open-meteo.com/v1/search to fetch the geolocation data of the city, and I only need to get the name of the city.\n\nSo, I will ask the user to input the name of the city and pass some pre-existing information, such as returning only the first city and returning in JSON format.\n\n- name (By Model) - And placeholder - The parameter that the AI will need to fill in as required.\n\n- count - 1 by default because I want only the first city.\n\n- format - Putting JSON for no specific reason, but OpenAI could figure out how to process that information."
      },
      "typeVersion": 1
    },
    {
      "id": "f9b0e65d-a85e-4511-bdd2-adf54b1c039d",
      "name": "A tool to get the weather forecast based on geolocation",
      "type": "@n8n/n8n-nodes-langchain.toolHttpRequest",
      "position": [
        1100,
        -160
      ],
      "parameters": {
        "url": "https://api.open-meteo.com/v1/forecast",
        "sendQuery": true,
        "parametersQuery": {
          "values": [
            {
              "name": "latitude"
            },
            {
              "name": "longitude"
            },
            {
              "name": "daily",
              "value": "temperature_2m_max,precipitation_sum",
              "valueProvider": "fieldValue"
            },
            {
              "name": "timezone",
              "value": "GMT",
              "valueProvider": "fieldValue"
            },
            {
              "name": "forecast_days"
            }
          ]
        },
        "toolDescription": "To get forecast of next [forecast_days] input the geolocation of an City",
        "placeholderDefinitions": {
          "values": [
            {
              "name": "longitude",
              "type": "number",
              "description": "longitude"
            },
            {
              "name": "latitude",
              "type": "number",
              "description": "latitude"
            },
            {
              "name": "forecast_days",
              "type": "number",
              "description": "forecast_days number of days ahead"
            }
          ]
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "76382491-dd75-4b51-a2d8-cb9782246af8",
      "name": "Sticky Note6",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1240,
        -220
      ],
      "parameters": {
        "color": 4,
        "width": 280,
        "height": 320,
        "content": "### Open Meteo SPEC - Weather Forecast\n\nThis tool will go to the Open Meteo site with the geolocation information at https://api.open-meteo.com/v1/forecast\n\nIt will pass the information on latitude, longitude, and the number of days for which it will bring data.\n\nThere are many default pieces of information within, but the focus is not to explain the Open Meteo API.\n\nVariables like latitude, longitude, and forecast_days are self-explanatory for OpenAI, making it the easiest tool to configure.\n\n- latitude (By Model) and Placeholder\n- longitude (By Model) and Placeholder\n- forecast_days (By Model) and Placeholder\n"
      },
      "typeVersion": 1
    },
    {
      "id": "1c8087ce-6800-4ece-8234-23914e21a692",
      "name": "A tool for inputting the city and obtaining geolocation",
      "type": "@n8n/n8n-nodes-langchain.toolHttpRequest",
      "position": [
        820,
        -100
      ],
      "parameters": {
        "url": "=https://geocoding-api.open-meteo.com/v1/search",
        "sendQuery": true,
        "parametersQuery": {
          "values": [
            {
              "name": "name"
            },
            {
              "name": "count",
              "value": "1",
              "valueProvider": "fieldValue"
            },
            {
              "name": "format",
              "value": "json",
              "valueProvider": "fieldValue"
            }
          ]
        },
        "toolDescription": "Input the City and get geolocation, geocode or coordinates from Requested City",
        "placeholderDefinitions": {
          "values": [
            {
              "name": "name",
              "type": "string",
              "description": "Requested City"
            }
          ]
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "15ae7421-eff9-4677-b8cf-b7bbb5d2385e",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -100,
        340
      ],
      "parameters": {
        "color": 3,
        "width": 840,
        "height": 80,
        "content": "## Within N8N, there will be a chat button to test, or you can use the external chat link from the trigger."
      },
      "typeVersion": 1
    }
  ],
  "active": true,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "778e2544-db78-4836-8bd1-771f333a621c",
  "connections": {
    "OpenAI Chat Model": {
      "ai_languageModel": [
        [
          {
            "node": "Generic AI Tool Agent",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Chat Memory Buffer": {
      "ai_memory": [
        [
          {
            "node": "When chat message received",
            "type": "ai_memory",
            "index": 0
          },
          {
            "node": "Generic AI Tool Agent",
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
            "node": "Generic AI Tool Agent",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "A tool for inputting the city and obtaining geolocation": {
      "ai_tool": [
        [
          {
            "node": "Generic AI Tool Agent",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "A tool to get the weather forecast based on geolocation": {
      "ai_tool": [
        [
          {
            "node": "Generic AI Tool Agent",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-1718"></a>

## Template 1718 - Comparação semanal de métricas GA4 com A.I. e salvamento

- **Nome:** Comparação semanal de métricas GA4 com A.I. e salvamento
- **Descrição:** Coleta métricas de engajamento de página, resultados de busca orgânica e visualizações por país para as duas últimas semanas, compara os períodos com um modelo de A.I. e salva as recomendações em uma base remota.
- **Funcionalidade:** • Coleta agendada e manual de dados: permite execução semanal automática ou disparo manual para iniciar o fluxo.
• Recuperação de métricas de página: obtém screenPageViews, activeUsers, screenPageViewsPerUser e eventCount por página para o período atual e o anterior.
• Recuperação de resultados de busca orgânica: captura métricas como posição média, CTR, cliques e impressões por landing page+query para ambos os períodos.
• Recuperação de visualizações por país: coleta activeUsers, newUsers, engagementRate, engagedSessions, eventCount e sessions por país para comparação semanal.
• Parsing e transformação: normaliza as linhas retornadas em objetos simplificados e codifica os dados para envio ao serviço de A.I.
• Envio para A.I.: envia os dados das duas semanas com um prompt instruindo o modelo a comparar, gerar uma tabela em markdown e sugerir melhorias de SEO.
• Armazenamento do output: salva as respostas geradas pelo A.I. em uma tabela remota com campos para título, relatórios e timestamp.
- **Ferramentas:** • Google Analytics (GA4): fonte das métricas de engajamento, tráfego orgânico e dados por país.
• OpenRouter AI (modelo meta-llama/llama-3.1-70b-instruct): serviço de A.I. usado para comparar dados, gerar tabelas em markdown e fornecer sugestões de SEO.
• Baserow: base de dados online usada para armazenar os outputs e recomendações geradas pelo modelo de A.I.

## Fluxo visual

```mermaid
flowchart LR
    N1["Schedule Trigger"]
    N2["When clicking ‘Test workflow’"]
    N3["Sticky Note"]
    N4["Sticky Note1"]
    N5["Get Page Engagement Stats for this week"]
    N6["Get Page Engagement Stats for prior week"]
    N7["Parse data from Google Analytics"]
    N8["Parse GA data"]
    N9["Get Google Search Results for this week"]
    N10["Get Google Search Results for last week"]
    N11["Parse Google Analytics Data"]
    N12["Parse Google Analytics Data1"]
    N13["Get Country views data for this week"]
    N14["Get Country views data for last week"]
    N15["Parse Google analytics data"]
    N16["Parse Google analytics data1"]
    N17["Send page data to A.I."]
    N18["Send page Search data to A.I."]
    N19["Send country view data to A.I."]
    N20["Save A.I. output to Baserow"]
    N21["Sticky Note2"]
    N22["Sticky Note3"]

    N8 --> N9
    N1 --> N5
    N17 --> N18
    N11 --> N10
    N15 --> N14
    N12 --> N13
    N16 --> N17
    N18 --> N19
    N19 --> N20
    N7 --> N6
    N2 --> N5
    N14 --> N16
    N13 --> N15
    N10 --> N12
    N9 --> N11
    N5 --> N7
    N6 --> N8
```

## Fluxo (.json) :

```json
{
  "id": "K3uf8aY8wipScEay",
  "meta": {
    "instanceId": "558d88703fb65b2d0e44613bc35916258b0f0bf983c5d4730c00c424b77ca36a",
    "templateCredsSetupCompleted": true
  },
  "name": "Google analytics template",
  "tags": [],
  "nodes": [
    {
      "id": "6a9fc442-d0a3-48be-8dff-94f8d9cd5cf1",
      "name": "Schedule Trigger",
      "type": "n8n-nodes-base.scheduleTrigger",
      "position": [
        460,
        460
      ],
      "parameters": {
        "rule": {
          "interval": [
            {
              "field": "weeks"
            }
          ]
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "484cbc41-f57d-4c3d-a458-e439d480d290",
      "name": "When clicking ‘Test workflow’",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        460,
        640
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "b1b66e9b-5fea-407b-9c1e-39bd2a9d4a90",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        460,
        100
      ],
      "parameters": {
        "width": 714.172987012987,
        "content": "## Send Google analytics to A.I. and save results to baserow\n\nThis workflow will check for country views, page engagement and google search console results. It will take this week's data and compare it to last week's data.\n\n[You can read more about this workflow here](https://rumjahn.com/how-i-used-a-i-to-be-an-seo-expert-and-analyzed-my-google-analytics-data-in-n8n-and-make-com/)"
      },
      "typeVersion": 1
    },
    {
      "id": "adde29fc-ddb5-4b50-aa78-313ac9ede879",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        633.6540259740264,
        320
      ],
      "parameters": {
        "color": 4,
        "width": 2097.92831168831,
        "height": 342.6576623376624,
        "content": "## Property ID\n\n1. Create your [Google Analytics Credentials](https://docs.n8n.io/integrations/builtin/credentials/google/oauth-single-service/?utm_source=n8n_app&utm_medium=credential_settings&utm_campaign=create_new_credentials_modal)\n2. Enter your [property ID](https://developers.google.com/analytics/devguides/reporting/data/v1/property-id)."
      },
      "typeVersion": 1
    },
    {
      "id": "f2fb8535-e81e-4ca1-80df-ee68edba6386",
      "name": "Get Page Engagement Stats for this week",
      "type": "n8n-nodes-base.googleAnalytics",
      "position": [
        700,
        460
      ],
      "parameters": {
        "simple": false,
        "returnAll": true,
        "metricsGA4": {
          "metricValues": [
            {
              "name": "screenPageViews",
              "listName": "other"
            },
            {
              "name": "activeUsers",
              "listName": "other"
            },
            {
              "name": "screenPageViewsPerUser",
              "listName": "other"
            },
            {
              "name": "eventCount",
              "listName": "other"
            }
          ]
        },
        "propertyId": {
          "__rl": true,
          "mode": "id",
          "value": "460520224"
        },
        "dimensionsGA4": {
          "dimensionValues": [
            {
              "name": "unifiedScreenName",
              "listName": "other"
            }
          ]
        },
        "additionalFields": {}
      },
      "credentials": {
        "googleAnalyticsOAuth2": {
          "id": "b1GX8VBMKCUNweV1",
          "name": "Google Analytics account"
        }
      },
      "typeVersion": 2
    },
    {
      "id": "1d761425-cebf-4787-b286-b723a0851485",
      "name": "Get Page Engagement Stats for prior week",
      "type": "n8n-nodes-base.googleAnalytics",
      "position": [
        1060,
        460
      ],
      "parameters": {
        "simple": false,
        "endDate": "2024-10-23T00:00:00",
        "dateRange": "custom",
        "returnAll": true,
        "startDate": "={{$today.minus({days: 14})}}",
        "metricsGA4": {
          "metricValues": [
            {
              "name": "screenPageViews",
              "listName": "other"
            },
            {
              "name": "activeUsers",
              "listName": "other"
            },
            {
              "name": "screenPageViewsPerUser",
              "listName": "other"
            },
            {
              "name": "eventCount",
              "listName": "other"
            }
          ]
        },
        "propertyId": {
          "__rl": true,
          "mode": "id",
          "value": "460520224"
        },
        "dimensionsGA4": {
          "dimensionValues": [
            {
              "name": "unifiedScreenName",
              "listName": "other"
            }
          ]
        },
        "additionalFields": {}
      },
      "typeVersion": 2
    },
    {
      "id": "f8dac36b-9e8a-407f-b923-b4cea368f1bc",
      "name": "Parse data from Google Analytics",
      "type": "n8n-nodes-base.code",
      "position": [
        880,
        460
      ],
      "parameters": {
        "jsCode": "function transformToUrlString(items) {\n    // Debug logging\n    console.log('Input items:', JSON.stringify(items, null, 2));\n    \n    // Check if items is an array and has content\n    if (!Array.isArray(items) || items.length === 0) {\n        console.log('Items is not an array or is empty');\n        throw new Error('Invalid data structure');\n    }\n\n    // Check if first item exists and has json property\n    if (!items[0] || !items[0].json) {\n        console.log('First item is missing or has no json property');\n        throw new Error('Invalid data structure');\n    }\n\n    // Get the analytics data\n    const analyticsData = items[0].json;\n    \n    // Check if analyticsData has rows\n    if (!analyticsData || !Array.isArray(analyticsData.rows)) {\n        console.log('Analytics data is missing or has no rows array');\n        throw new Error('Invalid data structure');\n    }\n    \n    // Map each row to a simplified object\n    const simplified = analyticsData.rows.map(row => {\n        if (!row.dimensionValues?.[0]?.value || !row.metricValues?.length) {\n            console.log('Invalid row structure:', row);\n            throw new Error('Invalid row structure');\n        }\n        \n        return {\n            page: row.dimensionValues[0].value,\n            pageViews: parseInt(row.metricValues[0].value) || 0,\n            activeUsers: parseInt(row.metricValues[1].value) || 0,\n            viewsPerUser: parseFloat(row.metricValues[2].value) || 0,\n            eventCount: parseInt(row.metricValues[3].value) || 0\n        };\n    });\n    \n    // Convert to JSON string and encode for URL\n    return encodeURIComponent(JSON.stringify(simplified));\n}\n\n// Get input data and transform it\nconst urlString = transformToUrlString($input.all());\n\n// Return the result\nreturn { json: { urlString } };"
      },
      "typeVersion": 2
    },
    {
      "id": "ed880442-c92e-4347-b277-e8794aea6fbc",
      "name": "Parse GA data",
      "type": "n8n-nodes-base.code",
      "position": [
        1240,
        460
      ],
      "parameters": {
        "jsCode": "function transformToUrlString(items) {\n    // Debug logging\n    console.log('Input items:', JSON.stringify(items, null, 2));\n    \n    // Check if items is an array and has content\n    if (!Array.isArray(items) || items.length === 0) {\n        console.log('Items is not an array or is empty');\n        throw new Error('Invalid data structure');\n    }\n\n    // Check if first item exists and has json property\n    if (!items[0] || !items[0].json) {\n        console.log('First item is missing or has no json property');\n        throw new Error('Invalid data structure');\n    }\n\n    // Get the analytics data\n    const analyticsData = items[0].json;\n    \n    // Check if analyticsData has rows\n    if (!analyticsData || !Array.isArray(analyticsData.rows)) {\n        console.log('Analytics data is missing or has no rows array');\n        throw new Error('Invalid data structure');\n    }\n    \n    // Map each row to a simplified object\n    const simplified = analyticsData.rows.map(row => {\n        if (!row.dimensionValues?.[0]?.value || !row.metricValues?.length) {\n            console.log('Invalid row structure:', row);\n            throw new Error('Invalid row structure');\n        }\n        \n        return {\n            page: row.dimensionValues[0].value,\n            pageViews: parseInt(row.metricValues[0].value) || 0,\n            activeUsers: parseInt(row.metricValues[1].value) || 0,\n            viewsPerUser: parseFloat(row.metricValues[2].value) || 0,\n            eventCount: parseInt(row.metricValues[3].value) || 0\n        };\n    });\n    \n    // Convert to JSON string and encode for URL\n    return encodeURIComponent(JSON.stringify(simplified));\n}\n\n// Get input data and transform it\nconst urlString = transformToUrlString($input.all());\n\n// Return the result\nreturn { json: { urlString } };"
      },
      "typeVersion": 2
    },
    {
      "id": "46e092cc-af94-4e64-aa92-931c56345eff",
      "name": "Get Google Search Results for this week",
      "type": "n8n-nodes-base.googleAnalytics",
      "position": [
        1420,
        460
      ],
      "parameters": {
        "simple": false,
        "returnAll": true,
        "metricsGA4": {
          "metricValues": [
            {
              "name": "activeUsers",
              "listName": "other"
            },
            {
              "name": "engagedSessions",
              "listName": "other"
            },
            {
              "name": "engagementRate",
              "listName": "other"
            },
            {
              "name": "eventCount",
              "listName": "other"
            },
            {
              "name": "organicGoogleSearchAveragePosition",
              "listName": "other"
            },
            {
              "name": "organicGoogleSearchClickThroughRate",
              "listName": "other"
            },
            {
              "name": "organicGoogleSearchClicks",
              "listName": "other"
            },
            {
              "name": "organicGoogleSearchImpressions",
              "listName": "other"
            }
          ]
        },
        "propertyId": {
          "__rl": true,
          "mode": "id",
          "value": "460520224"
        },
        "dimensionsGA4": {
          "dimensionValues": [
            {
              "name": "landingPagePlusQueryString",
              "listName": "other"
            }
          ]
        },
        "additionalFields": {}
      },
      "credentials": {
        "googleAnalyticsOAuth2": {
          "id": "b1GX8VBMKCUNweV1",
          "name": "Google Analytics account"
        }
      },
      "typeVersion": 2
    },
    {
      "id": "709d0aaf-bd3d-4d83-9e66-b7df495855bd",
      "name": "Get Google Search Results for last week",
      "type": "n8n-nodes-base.googleAnalytics",
      "position": [
        1780,
        460
      ],
      "parameters": {
        "simple": false,
        "endDate": "={{$today.minus({days: 7})}}",
        "dateRange": "custom",
        "returnAll": true,
        "startDate": "={{$today.minus({days: 14})}}",
        "metricsGA4": {
          "metricValues": [
            {
              "name": "activeUsers",
              "listName": "other"
            },
            {
              "name": "engagedSessions",
              "listName": "other"
            },
            {
              "name": "engagementRate",
              "listName": "other"
            },
            {
              "name": "eventCount",
              "listName": "other"
            },
            {
              "name": "organicGoogleSearchAveragePosition",
              "listName": "other"
            },
            {
              "name": "organicGoogleSearchClickThroughRate",
              "listName": "other"
            },
            {
              "name": "organicGoogleSearchClicks",
              "listName": "other"
            },
            {
              "name": "organicGoogleSearchImpressions",
              "listName": "other"
            }
          ]
        },
        "propertyId": {
          "__rl": true,
          "mode": "id",
          "value": "460520224"
        },
        "dimensionsGA4": {
          "dimensionValues": [
            {
              "name": "landingPagePlusQueryString",
              "listName": "other"
            }
          ]
        },
        "additionalFields": {}
      },
      "credentials": {
        "googleAnalyticsOAuth2": {
          "id": "b1GX8VBMKCUNweV1",
          "name": "Google Analytics account"
        }
      },
      "typeVersion": 2
    },
    {
      "id": "7d3835d6-d1f5-4159-8e34-871871e63989",
      "name": "Parse Google Analytics Data",
      "type": "n8n-nodes-base.code",
      "position": [
        1600,
        460
      ],
      "parameters": {
        "jsCode": "function transformToUrlString(items) {\n    // In n8n, we need to check if items is an array and get the json property\n    const data = items[0].json;\n    \n    if (!data || !data.rows) {\n        console.log('No valid data found');\n        return encodeURIComponent(JSON.stringify([]));\n    }\n    \n    try {\n        // Process each row\n        const simplified = data.rows.map(row => ({\n            page: row.dimensionValues[0].value,\n            activeUsers: parseInt(row.metricValues[0].value) || 0,\n            engagedSessions: parseInt(row.metricValues[1].value) || 0,\n            engagementRate: parseFloat(row.metricValues[2].value) || 0,\n            eventCount: parseInt(row.metricValues[3].value) || 0,\n            avgPosition: parseFloat(row.metricValues[4].value) || 0,\n            ctr: parseFloat(row.metricValues[5].value) || 0,\n            clicks: parseInt(row.metricValues[6].value) || 0,\n            impressions: parseInt(row.metricValues[7].value) || 0\n        }));\n        \n        return encodeURIComponent(JSON.stringify(simplified));\n    } catch (error) {\n        console.log('Error processing data:', error);\n        throw new Error('Invalid data structure');\n    }\n}\n\n// Get the input data\nconst items = $input.all();\n\n// Process the data\nconst result = transformToUrlString(items);\n\n// Return the result\nreturn { json: { urlString: result } };"
      },
      "typeVersion": 2
    },
    {
      "id": "c018fda4-a2e6-48f4-aabb-039c66374dc7",
      "name": "Parse Google Analytics Data1",
      "type": "n8n-nodes-base.code",
      "position": [
        1940,
        460
      ],
      "parameters": {
        "jsCode": "function transformToUrlString(items) {\n    // In n8n, we need to check if items is an array and get the json property\n    const data = items[0].json;\n    \n    if (!data || !data.rows) {\n        console.log('No valid data found');\n        return encodeURIComponent(JSON.stringify([]));\n    }\n    \n    try {\n        // Process each row\n        const simplified = data.rows.map(row => ({\n            page: row.dimensionValues[0].value,\n            activeUsers: parseInt(row.metricValues[0].value) || 0,\n            engagedSessions: parseInt(row.metricValues[1].value) || 0,\n            engagementRate: parseFloat(row.metricValues[2].value) || 0,\n            eventCount: parseInt(row.metricValues[3].value) || 0,\n            avgPosition: parseFloat(row.metricValues[4].value) || 0,\n            ctr: parseFloat(row.metricValues[5].value) || 0,\n            clicks: parseInt(row.metricValues[6].value) || 0,\n            impressions: parseInt(row.metricValues[7].value) || 0\n        }));\n        \n        return encodeURIComponent(JSON.stringify(simplified));\n    } catch (error) {\n        console.log('Error processing data:', error);\n        throw new Error('Invalid data structure');\n    }\n}\n\n// Get the input data\nconst items = $input.all();\n\n// Process the data\nconst result = transformToUrlString(items);\n\n// Return the result\nreturn { json: { urlString: result } };"
      },
      "typeVersion": 2
    },
    {
      "id": "d8f775cd-daf9-42de-a527-d932be46d945",
      "name": "Get Country views data for this week",
      "type": "n8n-nodes-base.googleAnalytics",
      "position": [
        2120,
        460
      ],
      "parameters": {
        "simple": false,
        "returnAll": true,
        "metricsGA4": {
          "metricValues": [
            {
              "name": "activeUsers",
              "listName": "other"
            },
            {
              "name": "newUsers",
              "listName": "other"
            },
            {
              "name": "engagementRate",
              "listName": "other"
            },
            {
              "name": "engagedSessions",
              "listName": "other"
            },
            {
              "name": "eventCount",
              "listName": "other"
            },
            {
              "listName": "other"
            },
            {
              "name": "sessions",
              "listName": "other"
            }
          ]
        },
        "propertyId": {
          "__rl": true,
          "mode": "id",
          "value": "460520224"
        },
        "dimensionsGA4": {
          "dimensionValues": [
            {
              "name": "country",
              "listName": "other"
            }
          ]
        },
        "additionalFields": {}
      },
      "credentials": {
        "googleAnalyticsOAuth2": {
          "id": "b1GX8VBMKCUNweV1",
          "name": "Google Analytics account"
        }
      },
      "typeVersion": 2
    },
    {
      "id": "7119e57c-cbf4-49a9-b0c9-1f3da1fd2af3",
      "name": "Get Country views data for last week",
      "type": "n8n-nodes-base.googleAnalytics",
      "position": [
        2440,
        460
      ],
      "parameters": {
        "simple": false,
        "endDate": "={{$today.minus({days: 7})}}",
        "dateRange": "custom",
        "returnAll": true,
        "startDate": "={{$today.minus({days: 14})}}",
        "metricsGA4": {
          "metricValues": [
            {
              "name": "activeUsers",
              "listName": "other"
            },
            {
              "name": "newUsers",
              "listName": "other"
            },
            {
              "name": "engagementRate",
              "listName": "other"
            },
            {
              "name": "engagedSessions",
              "listName": "other"
            },
            {
              "name": "eventCount",
              "listName": "other"
            },
            {
              "listName": "other"
            },
            {
              "name": "sessions",
              "listName": "other"
            }
          ]
        },
        "propertyId": {
          "__rl": true,
          "mode": "id",
          "value": "460520224"
        },
        "dimensionsGA4": {
          "dimensionValues": [
            {
              "name": "country",
              "listName": "other"
            }
          ]
        },
        "additionalFields": {}
      },
      "typeVersion": 2
    },
    {
      "id": "546d6cd2-6db6-4276-be35-abbe5a7e9b6a",
      "name": "Parse Google analytics data",
      "type": "n8n-nodes-base.code",
      "position": [
        2280,
        460
      ],
      "parameters": {
        "jsCode": "function transformToUrlString(items) {\n    // In n8n, we need to check if items is an array and get the json property\n    const data = items[0].json;\n    \n    if (!data || !data.rows) {\n        console.log('No valid data found');\n        return encodeURIComponent(JSON.stringify([]));\n    }\n    \n    try {\n        // Process each row\n        const simplified = data.rows.map(row => ({\n            country: row.dimensionValues[0].value,\n            activeUsers: parseInt(row.metricValues[0].value) || 0,\n            newUsers: parseInt(row.metricValues[1].value) || 0,\n            engagementRate: parseFloat(row.metricValues[2].value) || 0,\n            engagedSessions: parseInt(row.metricValues[3].value) || 0,\n            eventCount: parseInt(row.metricValues[4].value) || 0,\n            totalUsers: parseInt(row.metricValues[5].value) || 0,\n            sessions: parseInt(row.metricValues[6].value) || 0\n        }));\n        \n        return encodeURIComponent(JSON.stringify(simplified));\n    } catch (error) {\n        console.log('Error processing data:', error);\n        throw new Error('Invalid data structure');\n    }\n}\n\n// Get the input data\nconst items = $input.all();\n\n// Process the data\nconst result = transformToUrlString(items);\n\n// Return the result\nreturn { json: { urlString: result } };"
      },
      "typeVersion": 2
    },
    {
      "id": "87cb137c-686d-49a5-8657-06ed0c5f5c27",
      "name": "Parse Google analytics data1",
      "type": "n8n-nodes-base.code",
      "position": [
        2600,
        460
      ],
      "parameters": {
        "jsCode": "function transformToUrlString(items) {\n    // In n8n, we need to check if items is an array and get the json property\n    const data = items[0].json;\n    \n    if (!data || !data.rows) {\n        console.log('No valid data found');\n        return encodeURIComponent(JSON.stringify([]));\n    }\n    \n    try {\n        // Process each row\n        const simplified = data.rows.map(row => ({\n            country: row.dimensionValues[0].value,\n            activeUsers: parseInt(row.metricValues[0].value) || 0,\n            newUsers: parseInt(row.metricValues[1].value) || 0,\n            engagementRate: parseFloat(row.metricValues[2].value) || 0,\n            engagedSessions: parseInt(row.metricValues[3].value) || 0,\n            eventCount: parseInt(row.metricValues[4].value) || 0,\n            totalUsers: parseInt(row.metricValues[5].value) || 0,\n            sessions: parseInt(row.metricValues[6].value) || 0\n        }));\n        \n        return encodeURIComponent(JSON.stringify(simplified));\n    } catch (error) {\n        console.log('Error processing data:', error);\n        throw new Error('Invalid data structure');\n    }\n}\n\n// Get the input data\nconst items = $input.all();\n\n// Process the data\nconst result = transformToUrlString(items);\n\n// Return the result\nreturn { json: { urlString: result } };"
      },
      "typeVersion": 2
    },
    {
      "id": "06c4478d-a13a-4587-9f1f-451a68798a9f",
      "name": "Send page data to A.I.",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        2760,
        460
      ],
      "parameters": {
        "url": "https://openrouter.ai/api/v1/chat/completions",
        "method": "POST",
        "options": {},
        "jsonBody": "={\n  \"model\": \"meta-llama/llama-3.1-70b-instruct:free\",\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": \"You are an SEO expert. Compare the data from past 2 weeks, give me a table in markdown. Then give me 5 suggestions to improve my SEO. Output the data so that it works with markdown editors. Data from 2 weeks ago:{{ $json.urlString }} Data from last week: {{ $('Parse data from Google Analytics').item.json.urlString }}\"\n    }\n  ]\n}",
        "sendBody": true,
        "specifyBody": "json",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth"
      },
      "typeVersion": 4.2,
      "alwaysOutputData": false
    },
    {
      "id": "4ad522b0-afe4-4eff-aa16-b86cc892ead8",
      "name": "Send page Search data to A.I.",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        2920,
        460
      ],
      "parameters": {
        "url": "https://openrouter.ai/api/v1/chat/completions",
        "method": "POST",
        "options": {},
        "jsonBody": "={\n  \"model\": \"meta-llama/llama-3.1-70b-instruct:free\",\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": \"You are an SEO expert. Compare the data from past 2 weeks, give me a table in markdown. Then give me 5 suggestions to improve my SEO. Output the data so that it works with markdown editors. Data from 2 weeks ago:{{ $('Parse Google Analytics Data1').item.json.urlString }} Data from last week:{{ $('Parse Google Analytics Data').item.json.urlString }}\"\n    }\n  ]\n}",
        "sendBody": true,
        "specifyBody": "json",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth"
      },
      "typeVersion": 4.2,
      "alwaysOutputData": false
    },
    {
      "id": "07e1eebf-f16a-44c0-83b5-76bf65a3d3fc",
      "name": "Send country view data to A.I.",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        3080,
        460
      ],
      "parameters": {
        "url": "https://openrouter.ai/api/v1/chat/completions",
        "method": "POST",
        "options": {},
        "jsonBody": "={\n  \"model\": \"meta-llama/llama-3.1-70b-instruct:free\",\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": \"You are an SEO expert. Compare the data from past 2 weeks, give me a table in markdown. Then give me 5 suggestions to improve my SEO. Output the data so that it works with markdown editors. Data from 2 weeks ago:{{ $('Parse Google analytics data1').item.json.urlString }} Data from last week:{{ $('Parse Google analytics data').item.json.urlString }}\"\n    }\n  ]\n}",
        "sendBody": true,
        "specifyBody": "json",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth"
      },
      "typeVersion": 4.2,
      "alwaysOutputData": false
    },
    {
      "id": "c4648ad8-2377-42a0-a431-931b53631c9d",
      "name": "Save A.I. output to Baserow",
      "type": "n8n-nodes-base.baserow",
      "position": [
        3240,
        460
      ],
      "parameters": {
        "tableId": 601,
        "fieldsUi": {
          "fieldValues": [
            {
              "fieldId": 5833,
              "fieldValue": "Name of your blog"
            },
            {
              "fieldId": 5831,
              "fieldValue": "={{ $('Send page data to A.I.').item.json.choices[0].message.content }}"
            },
            {
              "fieldId": 5830,
              "fieldValue": "={{ $('Send page Search data to A.I.').item.json.choices[0].message.content }}"
            },
            {
              "fieldId": 5832,
              "fieldValue": "={{ $json.choices[0].message.content }}"
            },
            {
              "fieldId": 5829,
              "fieldValue": "={{ DateTime.now() }}"
            }
          ]
        },
        "operation": "create",
        "databaseId": 121
      },
      "typeVersion": 1
    },
    {
      "id": "e185c836-c12f-4452-92bd-0daaf33b653a",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2760,
        180
      ],
      "parameters": {
        "color": 5,
        "width": 441.7412987012988,
        "height": 508.95792207792226,
        "content": "## Send data to A.I.\n\nFill in your Openrouter A.I. credentials. Use Header Auth.\n- Username: Authorization\n- Password: Bearer {insert your API key}\n\nRemember to add a space after bearer. Also, feel free to modify the prompt to A.1."
      },
      "typeVersion": 1
    },
    {
      "id": "a1de2d16-d09e-4c74-8be1-f6bab8c34246",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        3220,
        180
      ],
      "parameters": {
        "color": 6,
        "width": 331.32883116883124,
        "height": 474.88,
        "content": "## Send data to Baserow\n\nCreate a table first with the following columns:\n- Name\n- Country Views\n- Page Views\n- Search Report\n- Blog \n\nEnter the name of your website under \"Blog\" field."
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "ac4b5eac-1c84-49ce-9ff7-794f857265b4",
  "connections": {
    "Parse GA data": {
      "main": [
        [
          {
            "node": "Get Google Search Results for this week",
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
            "node": "Get Page Engagement Stats for this week",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Send page data to A.I.": {
      "main": [
        [
          {
            "node": "Send page Search data to A.I.",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Parse Google Analytics Data": {
      "main": [
        [
          {
            "node": "Get Google Search Results for last week",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Parse Google analytics data": {
      "main": [
        [
          {
            "node": "Get Country views data for last week",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Parse Google Analytics Data1": {
      "main": [
        [
          {
            "node": "Get Country views data for this week",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Parse Google analytics data1": {
      "main": [
        [
          {
            "node": "Send page data to A.I.",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Send page Search data to A.I.": {
      "main": [
        [
          {
            "node": "Send country view data to A.I.",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Send country view data to A.I.": {
      "main": [
        [
          {
            "node": "Save A.I. output to Baserow",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Parse data from Google Analytics": {
      "main": [
        [
          {
            "node": "Get Page Engagement Stats for prior week",
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
            "node": "Get Page Engagement Stats for this week",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Country views data for last week": {
      "main": [
        [
          {
            "node": "Parse Google analytics data1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Country views data for this week": {
      "main": [
        [
          {
            "node": "Parse Google analytics data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Google Search Results for last week": {
      "main": [
        [
          {
            "node": "Parse Google Analytics Data1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Google Search Results for this week": {
      "main": [
        [
          {
            "node": "Parse Google Analytics Data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Page Engagement Stats for this week": {
      "main": [
        [
          {
            "node": "Parse data from Google Analytics",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Page Engagement Stats for prior week": {
      "main": [
        [
          {
            "node": "Parse GA data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-1721"></a>

## Template 1721 - Criar contato HubSpot e follow-up por email

- **Nome:** Criar contato HubSpot e follow-up por email
- **Descrição:** Automatiza a criação de contatos a partir de respostas do Typeform, atualiza o estágio do lead conforme interesse e envia um email de seguimento para leads interessados.
- **Funcionalidade:** • Detecção de submissão do Typeform via webhook: inicia o fluxo ao receber uma resposta do formulário.
• Mapeamento de respostas para variáveis internas: extrai nome, sobrenome, departamento, empresa, email e interesse a partir das perguntas do formulário.
• Criação de novo contato no HubSpot: usa o email e campos adicionais (nome, sobrenome, empresa, indústria) para criar o contato.
• Verificação do interesse do lead: avalia se o respondente manifestou interesse em escalar conteúdo visual.
• Atualização do estágio do lead: define o lifecycle stage como 'opportunity' para leads interessados.
• Envio de email de seguimento personalizado: envia um email via Gmail com convite para agendar e materiais adicionais para leads interessados.
• Ramificação para não interessados: fluxo segue por um nó vazio (NoOp) quando não há interesse, sem ações adicionais.
- **Ferramentas:** • Typeform: captura respostas de formulários online e aciona a automação via webhook.
• HubSpot: CRM utilizado para criar e atualizar contatos e gerenciar o estágio do lead.
• Gmail: serviço de email utilizado para enviar mensagens de seguimento personalizadas aos leads interessados.

## Fluxo visual

```mermaid
flowchart LR
    N1["create new contact"]
    N2["update lead stage"]
    N3["NoOp"]
    N4["Set values"]
    N5["Typeform Trigger"]
    N6["lead interested"]
    N7["send information"]

    N4 --> N1
    N6 --> N2
    N6 --> N3
    N5 --> N4
    N2 --> N7
    N1 --> N6
```

## Fluxo (.json) :

```json
{
  "nodes": [
    {
      "name": "create new contact",
      "type": "n8n-nodes-base.hubspot",
      "position": [
        -300,
        1200
      ],
      "parameters": {
        "email": "={{$json[\"form_email\"]}}",
        "resource": "contact",
        "additionalFields": {
          "industry": "={{$json[\"form_department\"]}}",
          "lastName": "={{$json[\"form_lastname\"]}}",
          "firstName": "={{$json[\"form_firstname\"]}}",
          "companyName": "={{$json[\"form_companyname\"]}}"
        }
      },
      "credentials": {
        "hubspotApi": "hubspot_nodeqa"
      },
      "typeVersion": 1
    },
    {
      "name": "update lead stage",
      "type": "n8n-nodes-base.hubspot",
      "position": [
        100,
        1100
      ],
      "parameters": {
        "email": "={{$node[\"create new contact\"].json[\"properties\"][\"email\"][\"value\"]}}",
        "resource": "contact",
        "additionalFields": {
          "lifeCycleStage": "opportunity"
        }
      },
      "credentials": {
        "hubspotApi": "hubspot_nodeqa"
      },
      "typeVersion": 1
    },
    {
      "name": "NoOp",
      "type": "n8n-nodes-base.noOp",
      "position": [
        100,
        1300
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Set values",
      "type": "n8n-nodes-base.set",
      "position": [
        -500,
        1200
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "form_firstname",
              "value": "={{$json[\"First up, what's your name?\"]}}"
            },
            {
              "name": "form_lastname",
              "value": "={{$json[\"And your surname, [field:fda1954c-f7a3-4fd3-a8dc-dcad5160bab5]?\"]}}"
            },
            {
              "name": "form_department",
              "value": "={{$json[\"And in which department do you work, [field:fda1954c-f7a3-4fd3-a8dc-dcad5160bab5]?\"]}}"
            },
            {
              "name": "form_companyname",
              "value": "={{$json[\"Great! Now what company are you from?\"]}}"
            },
            {
              "name": "form_email",
              "value": "={{$json[\"Just a couple more questions left! What's your email address?\"]}}"
            }
          ],
          "boolean": [
            {
              "name": "form_interest",
              "value": "={{$json[\"And are you currently looking to scale your visual content?\"]}}"
            }
          ]
        },
        "options": {},
        "keepOnlySet": true
      },
      "typeVersion": 1
    },
    {
      "name": "Typeform Trigger",
      "type": "n8n-nodes-base.typeformTrigger",
      "position": [
        -700,
        1200
      ],
      "webhookId": "97eb74c8-156c-4329-8679-37b69533f709",
      "parameters": {
        "formId": "RPueloJC"
      },
      "credentials": {
        "typeformApi": "typeform"
      },
      "typeVersion": 1
    },
    {
      "name": "lead interested",
      "type": "n8n-nodes-base.if",
      "position": [
        -100,
        1200
      ],
      "parameters": {
        "conditions": {
          "boolean": [
            {
              "value1": "={{$node[\"Set values\"].json[\"form_interest\"]}}",
              "value2": true
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "send information",
      "type": "n8n-nodes-base.gmail",
      "position": [
        300,
        1100
      ],
      "parameters": {
        "toList": [
          "={{$json[\"properties\"][\"email\"][\"value\"]}}"
        ],
        "message": "=Hello {{$json[\"properties\"][\"firstname\"][\"value\"]}},\n\nI'm glad to hear you're interested in our services. You can schedule a call with me here: [calendly_link].\nUntil then, check out this presentation about how we can help your business: [presentation_link].\nLooking forward to talking to you!\n\nBest,\nTeam",
        "subject": "So you're interested in growing your business",
        "resource": "message",
        "additionalFields": {}
      },
      "credentials": {
        "gmailOAuth2": "gmail"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Set values": {
      "main": [
        [
          {
            "node": "create new contact",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "lead interested": {
      "main": [
        [
          {
            "node": "update lead stage",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "NoOp",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Typeform Trigger": {
      "main": [
        [
          {
            "node": "Set values",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "update lead stage": {
      "main": [
        [
          {
            "node": "send information",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "create new contact": {
      "main": [
        [
          {
            "node": "lead interested",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-1723"></a>

## Template 1723 - Atribuição automática de issues no GitHub

- **Nome:** Atribuição automática de issues no GitHub
- **Descrição:** Fluxo que detecta eventos de issues e comentários no GitHub e atribui automaticamente responsáveis quando solicitados, além de adicionar rótulo de atribuído ou avisar quando já há um responsável.
- **Funcionalidade:** • Monitoramento de eventos do repositório: Inicia ao receber eventos de criação/abertura de issues e comentários.
• Detecção de pedido de atribuição: Verifica o texto da issue ou do comentário por padrões como "assign me" usando regex.
• Atribuição ao criador da issue: Se a issue for criada/aberta sem responsáveis e contiver o pedido, atribui o autor da issue e adiciona um rótulo "assigned".
• Atribuição ao comentarista: Se um comentário solicitar atribuição e a issue estiver sem responsáveis, atribui o autor do comentário e adiciona o rótulo.
• Notificação quando já houver responsável: Se alguém pedir para ser atribuído mas a issue já tiver um responsável, publica um comentário informando quem já está atribuído.
- **Ferramentas:** • GitHub: Plataforma para monitoramento de eventos (issues e comentários), edição de issues (atribuir usuários e adicionar rótulos) e criação de comentários.

## Fluxo visual

```mermaid
flowchart LR
    N1["Switch"]
    N2["IF no assignee?"]
    N3["NoOp"]
    N4["IF wants to work?"]
    N5["IF not assigned?"]
    N6["Assign Issue Creator"]
    N7["Add Comment"]
    N8["NoOp1"]
    N9["Assign Commenter"]
    N10["Github Trigger1"]

    N1 --> N2
    N1 --> N4
    N10 --> N1
    N2 --> N6
    N2 --> N3
    N5 --> N9
    N5 --> N7
    N4 --> N5
    N4 --> N8
```

## Fluxo (.json) :

```json
{
  "id": 122,
  "name": "Automate assigning GitHub issues",
  "nodes": [
    {
      "name": "Switch",
      "type": "n8n-nodes-base.switch",
      "position": [
        720,
        360
      ],
      "parameters": {
        "rules": {
          "rules": [
            {
              "value2": "opened"
            },
            {
              "output": 1,
              "value2": "created"
            }
          ]
        },
        "value1": "={{$json[\"body\"][\"action\"]}}",
        "dataType": "string"
      },
      "typeVersion": 1
    },
    {
      "name": "IF no assignee?",
      "type": "n8n-nodes-base.if",
      "position": [
        1120,
        220
      ],
      "parameters": {
        "conditions": {
          "number": [
            {
              "value1": "={{$json[\"body\"][\"issue\"][\"assignees\"].length}}",
              "operation": "equal"
            }
          ],
          "string": [
            {
              "value1": "={{$json[\"body\"][\"issue\"][\"body\"]}}",
              "value2": "/[a,A]ssign[\\w*\\s*]*me/gm",
              "operation": "regex"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "NoOp",
      "type": "n8n-nodes-base.noOp",
      "position": [
        1320,
        320
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "IF wants to work?",
      "type": "n8n-nodes-base.if",
      "position": [
        920,
        560
      ],
      "parameters": {
        "conditions": {
          "number": [],
          "string": [
            {
              "value1": "={{$json[\"body\"][\"comment\"][\"body\"]}}",
              "value2": "/[a,A]ssign[\\w*\\s*]*me/gm",
              "operation": "regex"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "IF not assigned?",
      "type": "n8n-nodes-base.if",
      "position": [
        1120,
        520
      ],
      "parameters": {
        "conditions": {
          "number": [
            {
              "value1": "={{$json[\"body\"][\"issue\"][\"assignees\"].length}}",
              "operation": "equal"
            }
          ],
          "string": []
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Assign Issue Creator",
      "type": "n8n-nodes-base.github",
      "position": [
        1320,
        120
      ],
      "parameters": {
        "owner": "={{$node[\"Switch\"].json[\"body\"][\"repository\"][\"owner\"][\"login\"]}}",
        "operation": "edit",
        "editFields": {
          "labels": [
            {
              "label": "assigned"
            }
          ],
          "assignees": [
            {
              "assignee": "={{$json.body.issue[\"user\"][\"login\"]}}"
            }
          ]
        },
        "repository": "={{$node[\"Switch\"].json[\"body\"][\"repository\"][\"name\"]}}",
        "issueNumber": "={{ $json[\"body\"][\"issue\"][\"number\"] }}",
        "authentication": "oAuth2"
      },
      "credentials": {
        "githubOAuth2Api": {
          "id": null,
          "name": "GitHub@Harshil"
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Add Comment",
      "type": "n8n-nodes-base.github",
      "position": [
        1420,
        660
      ],
      "parameters": {
        "body": "=Hey @{{$json[\"body\"][\"comment\"][\"user\"][\"login\"]}},\n\nThis issue is already assigned to {{$json[\"body\"][\"issue\"][\"assignee\"][\"login\"]}} 🙂",
        "owner": "={{$json[\"body\"][\"repository\"][\"owner\"][\"login\"]}}",
        "operation": "createComment",
        "repository": "={{$json[\"body\"][\"repository\"][\"name\"]}}",
        "issueNumber": "={{$json[\"body\"][\"issue\"][\"number\"]}}",
        "authentication": "oAuth2"
      },
      "credentials": {
        "githubOAuth2Api": {
          "id": null,
          "name": "GitHub@Harshil"
        }
      },
      "typeVersion": 1
    },
    {
      "name": "NoOp1",
      "type": "n8n-nodes-base.noOp",
      "position": [
        1120,
        720
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Assign Commenter",
      "type": "n8n-nodes-base.github",
      "position": [
        1420,
        460
      ],
      "parameters": {
        "owner": "={{$json[\"body\"][\"repository\"][\"owner\"][\"login\"]}}",
        "operation": "edit",
        "editFields": {
          "labels": [
            {
              "label": "assigned"
            }
          ],
          "assignees": [
            {
              "assignee": "={{$json[\"body\"][\"comment\"][\"user\"][\"login\"]}}"
            }
          ]
        },
        "repository": "={{$json[\"body\"][\"repository\"][\"name\"]}}",
        "issueNumber": "={{$json[\"body\"][\"issue\"][\"number\"]}}",
        "authentication": "oAuth2"
      },
      "credentials": {
        "githubOAuth2Api": {
          "id": null,
          "name": "GitHub@Harshil"
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Github Trigger1",
      "type": "n8n-nodes-base.githubTrigger",
      "position": [
        520,
        360
      ],
      "webhookId": "52c5fe44-23ef-4903-b6ae-731edd36127e",
      "parameters": {
        "owner": "harshil1712",
        "events": [
          "issue_comment",
          "issues"
        ],
        "repository": "build-discord-bot",
        "authentication": "oAuth2"
      },
      "credentials": {
        "githubOAuth2Api": {
          "id": null,
          "name": "GitHub Personal Credentials"
        }
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "Switch": {
      "main": [
        [
          {
            "node": "IF no assignee?",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "IF wants to work?",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Github Trigger1": {
      "main": [
        [
          {
            "node": "Switch",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "IF no assignee?": {
      "main": [
        [
          {
            "node": "Assign Issue Creator",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "NoOp",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "IF not assigned?": {
      "main": [
        [
          {
            "node": "Assign Commenter",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Add Comment",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "IF wants to work?": {
      "main": [
        [
          {
            "node": "IF not assigned?",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "NoOp1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-1725"></a>

## Template 1725 - Assistente pessoal com integração a calendário, email e CRM

- **Nome:** Assistente pessoal com integração a calendário, email e CRM
- **Descrição:** Fluxo que recebe mensagens de chat e atua como um assistente pessoal que pode consultar memória, interagir com um modelo de linguagem e executar ações em calendário, email e planilha de contatos, notificando o cliente via canal MCP.
- **Funcionalidade:** • Recepção de mensagens de chat: Inicia o assistente a partir de mensagens recebidas por chat.
• Agente conversacional com LLM: Utiliza um modelo de linguagem para interpretar instruções e gerar respostas.
• Memória simples: Mantém um buffer de memória para contexto de conversas recentes.
• Comunicação MCP Server/Client: Expõe um endpoint para receber comandos e usa um cliente SSE para enviar notificações de conclusão ao cliente.
• Criação e atualização de eventos no calendário: Permite criar novos eventos, atualizar eventos existentes e recuperar eventos (único ou múltiplos).
• Gestão de emails: Pesquisa emails e cria rascunhos para revisão/envio posterior, com campos preenchidos pelo agente.
• Operações em planilha de contatos (CRM): Adiciona novas linhas, encontra linhas existentes e atualiza linhas em uma planilha de contatos.
• Saída de status/notificações: Notifica clientes sobre o término das tarefas e fornece resumos/ações em formato preparado para revisão humana.
- **Ferramentas:** • Google Gemini (PaLM): modelo de linguagem usado para processamento de linguagem natural e geração de respostas do assistente.
• Gmail: serviço de email usado para pesquisar mensagens e criar rascunhos.
• Google Calendar: serviço de calendário usado para criar, atualizar e recuperar eventos.
• Google Sheets: planilha usada como CRM para adicionar, buscar e atualizar contatos.
• Canal MCP (Server/Client SSE): mecanismo de comunicação em tempo real para receber comandos do cliente e enviar notificações de conclusão.

## Fluxo visual

```mermaid
flowchart LR
    N1["When chat message received"]
    N2["Google Gemini Chat Model"]
    N3["Simple Memory"]
    N4["MCP Server Trigger"]
    N5["MCP Client"]
    N6["Create event"]
    N7["Update event"]
    N8["Draft email"]
    N9["Personal Assistant"]
    N10["Sticky Note"]
    N11["Sticky Note1"]
    N12["Sticky Note2"]
    N13["Sticky Note3"]
    N14["Sticky Note4"]
    N15["Add new row"]
    N16["Find row"]
    N17["Update row"]
    N18["Find emails"]
    N19["Find single event"]
    N20["Find multiple events"]

    N1 --> N9
```

## Fluxo (.json) :

```json
{
  "id": "KhUd3rHKtZAImiXZ",
  "meta": {
    "instanceId": "9219ebc7795bea866f70aa3d977d54417fdf06c41944be95e20cfb60f992db19",
    "templateCredsSetupCompleted": true
  },
  "name": "Personal Assistant MCP server",
  "tags": [],
  "nodes": [
    {
      "id": "f27f3d00-8019-401f-a1c4-5c9754ca5d7e",
      "name": "When chat message received",
      "type": "@n8n/n8n-nodes-langchain.chatTrigger",
      "position": [
        -220,
        -60
      ],
      "webhookId": "989c3a79-5a0c-4ca1-a542-55e060816121",
      "parameters": {
        "options": {}
      },
      "typeVersion": 1.1
    },
    {
      "id": "49e4bd69-141f-47ae-bb97-f03a92e56131",
      "name": "Google Gemini Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatGoogleGemini",
      "position": [
        -80,
        140
      ],
      "parameters": {
        "options": {},
        "modelName": "models/gemini-2.5-pro-preview-05-06"
      },
      "credentials": {
        "googlePalmApi": {
          "id": "MF12DwQJWL1egyiN",
          "name": "Google Gemini(PaLM) Api account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "aaa58803-52ad-439b-8876-05a84fc63eaf",
      "name": "Simple Memory",
      "type": "@n8n/n8n-nodes-langchain.memoryBufferWindow",
      "position": [
        120,
        140
      ],
      "parameters": {},
      "typeVersion": 1.3
    },
    {
      "id": "5c49309e-054c-4097-b8c3-1bf0b10539ec",
      "name": "MCP Server Trigger",
      "type": "@n8n/n8n-nodes-langchain.mcpTrigger",
      "position": [
        20,
        340
      ],
      "webhookId": "b37ab045-0b99-4d57-af44-6ae1e9ac6381",
      "parameters": {
        "path": "b37ab045-0b99-4d57-af44-6ae1e9ac6381"
      },
      "typeVersion": 1
    },
    {
      "id": "24e5ee35-c53c-4e82-9d79-d48d9220d7ac",
      "name": "MCP Client",
      "type": "@n8n/n8n-nodes-langchain.mcpClientTool",
      "position": [
        480,
        140
      ],
      "parameters": {
        "sseEndpoint": "<set-your-url-here>"
      },
      "typeVersion": 1
    },
    {
      "id": "24d7de59-9db2-43e8-ad2a-923bbfc9877b",
      "name": "Create event",
      "type": "n8n-nodes-base.googleCalendarTool",
      "position": [
        820,
        380
      ],
      "parameters": {
        "calendar": {
          "__rl": true,
          "mode": "list",
          "value": "hello@1node.ai",
          "cachedResultName": "hello@1node.ai"
        },
        "additionalFields": {}
      },
      "credentials": {
        "googleCalendarOAuth2Api": {
          "id": "UfvyikkM1kt4EcMl",
          "name": "Google Calendar account"
        }
      },
      "typeVersion": 1.3
    },
    {
      "id": "54a2e041-8c5c-40bb-ae6b-1494b8a5a198",
      "name": "Update event",
      "type": "n8n-nodes-base.googleCalendarTool",
      "position": [
        580,
        720
      ],
      "parameters": {
        "eventId": "={{ /*n8n-auto-generated-fromAI-override*/ $fromAI('Event_ID', ``, 'string') }}",
        "calendar": {
          "__rl": true,
          "mode": "list",
          "value": "hello@1node.ai",
          "cachedResultName": "hello@1node.ai"
        },
        "operation": "update",
        "updateFields": {}
      },
      "credentials": {
        "googleCalendarOAuth2Api": {
          "id": "UfvyikkM1kt4EcMl",
          "name": "Google Calendar account"
        }
      },
      "typeVersion": 1.3
    },
    {
      "id": "7bebda2e-711f-478b-8ba3-36306b1ffb49",
      "name": "Draft email",
      "type": "n8n-nodes-base.gmailTool",
      "position": [
        260,
        780
      ],
      "webhookId": "4e76cb3d-4239-4030-a23a-544029535f70",
      "parameters": {
        "message": "={{ /*n8n-auto-generated-fromAI-override*/ $fromAI('Message', `Sign off as \"Your name, company name\"`, 'string') }}",
        "options": {},
        "subject": "={{ /*n8n-auto-generated-fromAI-override*/ $fromAI('Subject', ``, 'string') }}",
        "resource": "draft"
      },
      "credentials": {
        "gmailOAuth2": {
          "id": "q3P6IybvNdDiPZ52",
          "name": "Gmail account"
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "26538db2-f3af-47a8-b97e-2afa7d9ea05d",
      "name": "Personal Assistant",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        40,
        -60
      ],
      "parameters": {
        "options": {}
      },
      "typeVersion": 1.9
    },
    {
      "id": "04c5d14f-a80d-4113-b3ff-a6ee1ab3917e",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        920,
        280
      ],
      "parameters": {
        "color": 5,
        "width": 560,
        "height": 620,
        "content": "# Calendar nodes\n\nYou could order your agent to create a new event in your Google Calendar, find a specific event, get multiple events or update an event's details. \n\n**The true power of these nodes regarding Email, CRM and Calendar remains in combining multiple into one set of instructions**.\n\n## Examples:\n\n- Find the contact for Jhon for A. Corp and send him an email asking saying that you have scheduled the meeting for next Wednesday at 9AM. Draft an email to remind him of the details and the topic of discussion being the weekly update call and the main company bottlenecks.\n- Update the contact details for Jhon since he changed his email and company to B corp and john[at]bcorpfakeemail[dot]com and please update me about my upcoming meetings with him next month.\n- Send me a summary for all my meetings today. Draft one email for each different person that I'll meet with today, reminding them about today's meeting\n"
      },
      "typeVersion": 1
    },
    {
      "id": "0de610d2-20bf-4fd4-b93e-60b082d22e56",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        0,
        700
      ],
      "parameters": {
        "color": 3,
        "width": 460,
        "height": 500,
        "content": "# Email nodes\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYour AI Agent will be able to search through your email inbox to find specific email content for you. Based on this records you can fetch information quickly and order to draft responses to review later.\n\n## Examples:\n\n- hey what were the last 5 emails sent to Jon from X corp? \n- Draft an email with these details to Jon sharing I can't make it today and propose a new time for 9AM tomorrow. "
      },
      "typeVersion": 1
    },
    {
      "id": "e084e23e-473b-4798-a39c-00529ef9e827",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -720,
        360
      ],
      "parameters": {
        "color": 4,
        "width": 660,
        "height": 480,
        "content": "# CRM nodes\n\nWith these node operations your \nAI agent will be able to do the following:\n\n- Add a new row with contact data\n- Find a row and its details in the table\n- Update a value or group of values\n\n\n## Examples:\n\n- Add a new contact data with Rick as first name\n his cell is +1 XXX XXX XXXX. \nI will tell you the email later on.\n- Can you tell me the details and email for Jon Doe?\n I want to send him an email reminder.\n- Update Rick's email to rick[at]someemail[dot]com from X corp. please."
      },
      "typeVersion": 1
    },
    {
      "id": "dc9dcee5-35ec-4ea3-8c67-21c277705dec",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        360,
        -220
      ],
      "parameters": {
        "width": 480,
        "height": 480,
        "content": "## MCP Client\n\nPaste your MCP client URL from the MCP server trigger node.\n\nCustomize your output node to receive the workflow completion notifications (eg. Telegram, Gmail) from your personal assistant"
      },
      "typeVersion": 1
    },
    {
      "id": "1764e9cd-7fc1-46e7-bc97-33d4b81d5141",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        520,
        280
      ],
      "parameters": {
        "color": 5,
        "width": 400,
        "height": 620,
        "content": ""
      },
      "typeVersion": 1
    },
    {
      "id": "b4dda81f-fa22-43ec-a841-7b924b8884e8",
      "name": "Add new row",
      "type": "n8n-nodes-base.googleSheetsTool",
      "position": [
        -340,
        440
      ],
      "parameters": {
        "columns": {
          "value": {},
          "schema": [],
          "mappingMode": "autoMapInputData",
          "matchingColumns": [],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {},
        "operation": "append",
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": "gid=0",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1JDoEkNqk1c_TrIht2n1XF-jmIWpk48DP3NUaNbhcFV8/edit#gid=0",
          "cachedResultName": "Sheet1"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "1JDoEkNqk1c_TrIht2n1XF-jmIWpk48DP3NUaNbhcFV8",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1JDoEkNqk1c_TrIht2n1XF-jmIWpk48DP3NUaNbhcFV8/edit?usp=drivesdk",
          "cachedResultName": "Contacts"
        }
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "twZdLFsI3kTnqtpG",
          "name": "Google Sheets account"
        }
      },
      "typeVersion": 4.5
    },
    {
      "id": "e3bc61e0-1d95-4554-b7ba-f76c3f105339",
      "name": "Find row",
      "type": "n8n-nodes-base.googleSheetsTool",
      "position": [
        -280,
        580
      ],
      "parameters": {
        "options": {},
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": "gid=0",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1JDoEkNqk1c_TrIht2n1XF-jmIWpk48DP3NUaNbhcFV8/edit#gid=0",
          "cachedResultName": "Sheet1"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "1JDoEkNqk1c_TrIht2n1XF-jmIWpk48DP3NUaNbhcFV8",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1JDoEkNqk1c_TrIht2n1XF-jmIWpk48DP3NUaNbhcFV8/edit?usp=drivesdk",
          "cachedResultName": "Contacts"
        }
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "twZdLFsI3kTnqtpG",
          "name": "Google Sheets account"
        }
      },
      "typeVersion": 4.5
    },
    {
      "id": "461469da-c47a-486f-98c2-71fcc9abc235",
      "name": "Update row",
      "type": "n8n-nodes-base.googleSheetsTool",
      "position": [
        -180,
        680
      ],
      "parameters": {
        "columns": {
          "value": {},
          "schema": [
            {
              "id": "row_number",
              "type": "string",
              "display": true,
              "removed": false,
              "readOnly": true,
              "required": false,
              "displayName": "row_number",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            }
          ],
          "mappingMode": "autoMapInputData",
          "matchingColumns": [
            "row_number"
          ],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {},
        "operation": "update",
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": "gid=0",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1JDoEkNqk1c_TrIht2n1XF-jmIWpk48DP3NUaNbhcFV8/edit#gid=0",
          "cachedResultName": "Sheet1"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "1JDoEkNqk1c_TrIht2n1XF-jmIWpk48DP3NUaNbhcFV8",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1JDoEkNqk1c_TrIht2n1XF-jmIWpk48DP3NUaNbhcFV8/edit?usp=drivesdk",
          "cachedResultName": "Contacts"
        }
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "twZdLFsI3kTnqtpG",
          "name": "Google Sheets account"
        }
      },
      "typeVersion": 4.5
    },
    {
      "id": "01c0ba70-c1b1-454f-9b4e-0727c8280ace",
      "name": "Find emails",
      "type": "n8n-nodes-base.gmailTool",
      "position": [
        120,
        780
      ],
      "webhookId": "b36e3112-52b1-4e03-a2d3-74d5d4705891",
      "parameters": {
        "filters": {},
        "operation": "getAll",
        "returnAll": "={{ /*n8n-auto-generated-fromAI-override*/ $fromAI('Return_All', ``, 'boolean') }}"
      },
      "credentials": {
        "gmailOAuth2": {
          "id": "q3P6IybvNdDiPZ52",
          "name": "Gmail account"
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "40efd312-032f-496b-8485-a6a49001aa75",
      "name": "Find single event",
      "type": "n8n-nodes-base.googleCalendarTool",
      "position": [
        760,
        520
      ],
      "parameters": {
        "eventId": "={{ /*n8n-auto-generated-fromAI-override*/ $fromAI('Event_ID', ``, 'string') }}",
        "options": {},
        "calendar": {
          "__rl": true,
          "mode": "list",
          "value": "hello@1node.ai",
          "cachedResultName": "hello@1node.ai"
        },
        "operation": "get"
      },
      "credentials": {
        "googleCalendarOAuth2Api": {
          "id": "UfvyikkM1kt4EcMl",
          "name": "Google Calendar account"
        }
      },
      "typeVersion": 1.3
    },
    {
      "id": "8ac5c33e-f4fb-4627-98d5-b66838db3037",
      "name": "Find multiple events",
      "type": "n8n-nodes-base.googleCalendarTool",
      "position": [
        680,
        620
      ],
      "parameters": {
        "limit": 10,
        "options": {},
        "calendar": {
          "__rl": true,
          "mode": "list",
          "value": "hello@1node.ai",
          "cachedResultName": "hello@1node.ai"
        },
        "operation": "getAll"
      },
      "credentials": {
        "googleCalendarOAuth2Api": {
          "id": "UfvyikkM1kt4EcMl",
          "name": "Google Calendar account"
        }
      },
      "typeVersion": 1.3
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "99536a4c-8e1b-4b7e-9a2a-8baa404499fe",
  "connections": {
    "Find row": {
      "ai_tool": [
        [
          {
            "node": "MCP Server Trigger",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "MCP Client": {
      "ai_tool": [
        [
          {
            "node": "Personal Assistant",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Update row": {
      "ai_tool": [
        [
          {
            "node": "MCP Server Trigger",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Add new row": {
      "ai_tool": [
        [
          {
            "node": "MCP Server Trigger",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Draft email": {
      "ai_tool": [
        [
          {
            "node": "MCP Server Trigger",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Find emails": {
      "ai_tool": [
        [
          {
            "node": "MCP Server Trigger",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Create event": {
      "ai_tool": [
        [
          {
            "node": "MCP Server Trigger",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Update event": {
      "ai_tool": [
        [
          {
            "node": "MCP Server Trigger",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Simple Memory": {
      "ai_memory": [
        [
          {
            "node": "Personal Assistant",
            "type": "ai_memory",
            "index": 0
          }
        ]
      ]
    },
    "Find single event": {
      "ai_tool": [
        [
          {
            "node": "MCP Server Trigger",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Find multiple events": {
      "ai_tool": [
        [
          {
            "node": "MCP Server Trigger",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Google Gemini Chat Model": {
      "ai_languageModel": [
        [
          {
            "node": "Personal Assistant",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "When chat message received": {
      "main": [
        [
          {
            "node": "Personal Assistant",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-1727"></a>

## Template 1727 - Gerador de workflow AI para base Notion

- **Nome:** Gerador de workflow AI para base Notion
- **Descrição:** Gera automaticamente um workflow de assistente AI adaptado ao esquema de uma base de dados do Notion a partir de uma URL fornecida pelo usuário, validando e ajustando o JSON resultante antes de retornar.
- **Funcionalidade:** • Receber URL do usuário: aceita um link de base do Notion via chat e extrai a URL válida.
• Recuperar esquema do banco: consulta a API do Notion para obter detalhes do banco de dados (título, id, propriedades, opções) e dados públicos.
• Padronizar e simplificar esquema: transforma a resposta da API em um formato padronizado e simplificado para economizar tokens e facilitar a utilização pelo modelo.
• Gerar workflow adaptado: usa um template de workflow como referência e um modelo de linguagem para produzir uma versão modificada que funcione com o esquema da base fornecida.
• Validar JSON do workflow: verifica se a saída é um JSON de workflow válido e classifica como válido ou inválido.
• Auto-correção e retry: quando detecta erros comuns (como placeholders ou objetos mal formatados), insere feedback e reexecuta a geração para corrigir a saída.
• Mensagem de sucesso ou erro ao chat: retorna ao usuário o JSON final pronto para colar no canvas ou uma mensagem de erro clara se a URL for inválida.
• Preparar ferramentas no workflow gerado: inclui definições de endpoints e ferramentas no workflow resultante para buscar e ler páginas e conteúdo dentro da base do Notion.
- **Ferramentas:** • Notion: API usada para recuperar detalhes do banco de dados, propriedades e conteúdo das páginas.
• OpenAI: modelo de linguagem (ex.: gpt-4o presente no template) utilizado para geração de texto e construção do workflow adaptado.
• Anthropic: modelos de chat e classificadores empregados para geração auxiliar, validação e auto-correção das saídas.
• YouTube: vídeo tutorial externo fornecido como apoio para configuração e uso.

## Fluxo visual

```mermaid
flowchart LR
    N1["Sticky Note"]
    N2["Notion"]
    N3["Return success to chat"]
    N4["Auto-fixing Output Parser"]
    N5["Anthropic Chat Model"]
    N6["Set schema for eval"]
    N7["Return error to chat"]
    N8["Anthropic Chat Model1"]
    N9["standardize schema"]
    N10["Simplify properties object"]
    N11["Structured Output Parser"]
    N12["Set input data"]
    N13["Set schem for rerun"]
    N14["Sticky Note1"]
    N15["Sticky Note2"]
    N16["Sticky Note3"]
    N17["Add feedback prompt"]
    N18["Check for WF JSON errors"]
    N19["Sticky Note4"]
    N20["Generate Workflow Agent"]
    N21["Anthropic Chat Model2"]
    N22["When chat message received"]
    N23["Valid n8n workflow JSON?"]
    N24["Sticky Note5"]

    N2 --> N9
    N2 --> N7
    N12 --> N20
    N9 --> N10
    N17 --> N13
    N13 --> N12
    N6 --> N18
    N20 --> N6
    N18 --> N17
    N18 --> N23
    N23 --> N13
    N23 --> N3
    N10 --> N12
    N22 --> N2
```

## Fluxo (.json) :

```json
{
  "nodes": [
    {
      "id": "9052b5b2-1e2d-425c-92e5-1ed51323e71c",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        380,
        240
      ],
      "parameters": {
        "color": 7,
        "width": 616.7964812508943,
        "height": 231.27721611949534,
        "content": "# Generate new workflow version for specific notion db schema\nInput a Notion database URL and get an AI Assistant chatbot workflow for it based on this template: https://n8n.io/workflows/2413-notion-knowledge-base-ai-assistant/\n\nProject in notion: https://www.notion.so/n8n/Chat-with-notion-database-84eec91b74dd4e36ba97edda17c2c306"
      },
      "typeVersion": 1
    },
    {
      "id": "b4a83f76-2bad-4bbe-9b7f-1df684166035",
      "name": "Notion",
      "type": "n8n-nodes-base.notion",
      "onError": "continueErrorOutput",
      "position": [
        1280,
        480
      ],
      "parameters": {
        "simple": false,
        "resource": "database",
        "databaseId": {
          "__rl": true,
          "mode": "url",
          "value": "={{ $json.chatInput.match(/https?://[^\\s/$.?#].[^\\s]*/g)[0] }}"
        }
      },
      "credentials": {
        "notionApi": {
          "id": "aDS2eHXMOtsMrQnJ",
          "name": "Nathan's notion account"
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "39537c95-5ca0-47a9-b2bf-2c0134d3f236",
      "name": "Return success to chat",
      "type": "n8n-nodes-base.set",
      "position": [
        3540,
        740
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "bebcb43c-461d-40d7-af83-436d94733622",
              "name": "output",
              "type": "string",
              "value": "=Created workflow:\n```\n{{ $json.generatedWorkflow }}\n```\n\n☝️ Copy and paste JSON above into an n8n workflow canvas (on v 1.52.0+)"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "5ae0fcfb-c3e2-443d-9a0c-25e7b17dc189",
      "name": "Auto-fixing Output Parser",
      "type": "@n8n/n8n-nodes-langchain.outputParserAutofixing",
      "position": [
        2340,
        640
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "4cd182ff-040a-4c0f-819f-a0648c67ab66",
      "name": "Anthropic Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatAnthropic",
      "position": [
        2100,
        640
      ],
      "parameters": {
        "options": {
          "temperature": 0.7,
          "maxTokensToSample": 8192
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "dc751c1f-4cd6-4d04-8152-402eb5e24574",
      "name": "Set schema for eval",
      "type": "n8n-nodes-base.set",
      "position": [
        2720,
        440
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "f82e26dd-f5c5-43b5-b97d-ee63c3ef124e",
              "name": "searchNotionDBJsonBody",
              "type": "string",
              "value": "={{ $json.output.output.workflowJson.parseJson().nodes.find(node => node.name === \"Search notion database\").parameters.jsonBody }}"
            },
            {
              "id": "a804139b-8bf0-43dc-aa8c-9c0dcb387392",
              "name": "generatedWorkflow",
              "type": "string",
              "value": "={{ $json.output.output.workflowJson }}"
            },
            {
              "id": "1e24fdfe-c31f-43e3-bca2-7124352fd62e",
              "name": "inputDatabase",
              "type": "object",
              "value": "={{ $('Set input data').first().json.inputDatabase }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "8f8c9d29-c901-4c3c-83a6-23bfe51809bd",
      "name": "Return error to chat",
      "type": "n8n-nodes-base.set",
      "position": [
        1500,
        660
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "b561b640-7fcb-4613-8b66-068dbd115b4e",
              "name": "sessionId",
              "type": "string",
              "value": "={{ $('When chat message received').item.json.sessionId }}"
            },
            {
              "id": "74d91d28-b73a-4341-a037-693468120d2d",
              "name": "output",
              "type": "string",
              "value": "Sorry that doesn't look like a valid notion database url. Try again."
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "518d2e58-6f2e-4497-9f74-7dbfeff4fd6f",
      "name": "Anthropic Chat Model1",
      "type": "@n8n/n8n-nodes-langchain.lmChatAnthropic",
      "position": [
        2300,
        800
      ],
      "parameters": {
        "options": {
          "maxTokensToSample": 8192
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "0e7a4d05-db00-4915-9df4-d3cb79bf5789",
      "name": "standardize schema",
      "type": "n8n-nodes-base.set",
      "position": [
        1500,
        440
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "8fc7df86-4a47-43ec-baea-f9ee87a899a8",
              "name": "inputDatabase.id",
              "type": "string",
              "value": "={{ $json.id }}"
            },
            {
              "id": "fdeb5b1b-0bf3-46d6-a266-7f85e212a427",
              "name": "inputDatabase.url",
              "type": "string",
              "value": "={{ $json.url }}"
            },
            {
              "id": "b2b06176-b4df-41bd-9422-9c89726fa3fd",
              "name": "inputDatabase.public_url",
              "type": "string",
              "value": "={{ $json.public_url }}"
            },
            {
              "id": "c7b65a70-8af6-4808-aae9-898df9b10340",
              "name": "inputDatabase.name",
              "type": "string",
              "value": "={{ $json.title[0].text.content }}"
            },
            {
              "id": "87c1be85-e180-487b-9c82-61c87c7c460b",
              "name": "inputDatabase.properties",
              "type": "object",
              "value": "={{ $json.properties }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "8244fb04-75ec-4b41-93cf-e9c5755fabfd",
      "name": "Simplify properties object",
      "type": "n8n-nodes-base.code",
      "position": [
        1720,
        440
      ],
      "parameters": {
        "jsCode": "// Loop through each incoming item\nreturn items.map(item => {\n const inputDatabase = item.json[\"inputDatabase\"];\n\n const simplifiedProperties = Object.fromEntries(Object.entries(inputDatabase.properties).map(([key, value]) => {\n const simplifiedValue = {\n id: value.id,\n name: value.name,\n type: value.type\n };\n\n // Simplify based on type\n if (value.type === 'multi_select' || value.type === 'select') {\n simplifiedValue.options = value.multi_select?.options?.map(option => option.name) || [];\n }\n \n return [key, simplifiedValue];\n }));\n\n // Overwrite the properties object with simplifiedProperties\n item.json.inputDatabase.properties = simplifiedProperties;\n\n return item; // Return the modified item\n});\n"
      },
      "typeVersion": 2
    },
    {
      "id": "41b615cc-de7d-4c3f-b608-2d1856e0541a",
      "name": "Structured Output Parser",
      "type": "@n8n/n8n-nodes-langchain.outputParserStructured",
      "position": [
        2500,
        800
      ],
      "parameters": {
        "jsonSchemaExample": "{\n\t\"workflowJson\": \"json of workflow\"\n}"
      },
      "typeVersion": 1.2
    },
    {
      "id": "8016baac-9242-44e6-b487-111bb560019d",
      "name": "Set input data",
      "type": "n8n-nodes-base.code",
      "notes": "This allows different routes to input into our agent (e.g. the retry branch). In the AI Agent, we can use a relative $json reference for data, since it's always the same input schema going in. ",
      "position": [
        1980,
        440
      ],
      "parameters": {
        "jsCode": "\nreturn [{\n json: {\n inputDatabase: $input.first().json.inputDatabase,\n feedbackPrompt: (typeof yourVariable !== 'undefined' && yourVariable) ? yourVariable : \" \",\n workflowTemplate: {\n \"nodes\": [\n {\n \"parameters\": {\n \"model\": \"gpt-4o\",\n \"options\": {\n \"temperature\": 0.7,\n \"timeout\": 25000\n }\n },\n \"id\": \"f262c0b4-d627-4fd4-ad78-0aa2f57d963f\",\n \"name\": \"OpenAI Chat Model\",\n \"type\": \"@n8n/n8n-nodes-langchain.lmChatOpenAi\",\n \"typeVersion\": 1,\n \"position\": [\n 1320,\n 640\n ],\n \"credentials\": {\n \"openAiApi\": {\n \"id\": \"AzPPV759YPBxJj3o\",\n \"name\": \"Max's DevRel OpenAI account\"\n }\n }\n },\n {\n \"parameters\": {\n \"assignments\": {\n \"assignments\": [\n {\n \"id\": \"055e8a80-4aff-4466-aaa5-ac58bb90f2d0\",\n \"name\": \"databaseName\",\n \"value\": \"={{ $json.name }}\",\n \"type\": \"string\"\n },\n {\n \"id\": \"2a61e473-72e7-46f6-98b0-817508d701c7\",\n \"name\": \"databaseId\",\n \"value\": \"={{ $json.id }}\",\n \"type\": \"string\"\n }\n ]\n },\n \"options\": {}\n },\n \"id\": \"fb74819f-660e-479c-9519-73cfc41c7ee0\",\n \"name\": \"workflow vars\",\n \"type\": \"n8n-nodes-base.set\",\n \"typeVersion\": 3.4,\n \"position\": [\n 940,\n 460\n ]\n },\n {\n \"parameters\": {\n \"assignments\": {\n \"assignments\": [\n {\n \"id\": \"a8e58791-ba51-46a2-8645-386dd1a0ff6e\",\n \"name\": \"sessionId\",\n \"value\": \"={{ $('When chat message received').item.json.sessionId }}\",\n \"type\": \"string\"\n },\n {\n \"id\": \"434209de-39d5-43d8-a964-0fcb7396306c\",\n \"name\": \"action\",\n \"value\": \"={{ $('When chat message received').item.json.action }}\",\n \"type\": \"string\"\n },\n {\n \"id\": \"cad4c972-51a9-4e16-a627-b00eea77eb30\",\n \"name\": \"chatInput\",\n \"value\": \"={{ $('When chat message received').item.json.chatInput }}\",\n \"type\": \"string\"\n }\n ]\n },\n \"options\": {}\n },\n \"id\": \"832ec8ce-0f7c-4380-9a24-633f490a60a9\",\n \"name\": \"format input for agent\",\n \"type\": \"n8n-nodes-base.set\",\n \"typeVersion\": 3.4,\n \"position\": [\n 1160,\n 460\n ]\n },\n {\n \"parameters\": {\n \"toolDescription\": \"=Use this tool to search the \\\"{{ $('workflow vars').item.json.databaseName }}\\\" Notion app database.\\n\\nIt is structured with question and answer format. \\nYou can filter query result by:\\n- By keyword\\n- filter by tag.\\n\\nKeyword and Tag have an OR relationship not AND.\\n\\n\",\n \"method\": \"POST\",\n \"url\": \"https://api.notion.com/v1/databases/7ea9697d-4875-441e-b262-1105337d232e/query\",\n \"authentication\": \"predefinedCredentialType\",\n \"nodeCredentialType\": \"notionApi\",\n \"sendBody\": true,\n \"specifyBody\": \"json\",\n \"jsonBody\": \"{\\n \\\"filter\\\": {\\n \\\"or\\\": [\\n {\\n \\\"property\\\": \\\"question\\\",\\n \\\"rich_text\\\": {\\n \\\"contains\\\": \\\"{keyword}\\\"\\n }\\n },\\n {\\n \\\"property\\\": \\\"tags\\\",\\n \\\"multi_select\\\": {\\n \\\"contains\\\": \\\"{tag}\\\"\\n }\\n }\\n ]\\n },\\n \\\"sorts\\\": [\\n {\\n \\\"property\\\": \\\"updated_at\\\",\\n \\\"direction\\\": \\\"ascending\\\"\\n }\\n ]\\n}\",\n \"placeholderDefinitions\": {\n \"values\": [\n {\n \"name\": \"keyword\",\n \"description\": \"Searches question of the record. Use one keyword at a time.\"\n },\n {\n \"name\": \"tag\",\n \"description\": \"Options: PTO, HR Policy, Health Benefits, Direct Deposit, Payroll, Sick Leave, 1:1 Meetings, Scheduling, Internal Jobs, Performance Review, Diversity, Inclusion, Training, Harassment, Discrimination, Product Roadmap, Development, Feature Request, Product Management, Support, Ticket Submission, Password Reset, Email, Slack, GitHub, Team Collaboration, Development Setup, DevOps, GitHub Profile Analyzer, Security Breach, Incident Report, New Software, Software Request, IT, Hardware, Procurement, Software Licenses, JetBrains, Adobe, Data Backup, IT Policy, Security, MFA, Okta, Device Policy, Support Ticket, Phishing, Office Supplies, Operations, Meeting Room, Berlin Office, Travel Expenses, Reimbursement, Facilities, Maintenance, Equipment, Expense Reimbursement, Mobile Phones, SIM Cards, Parking, OKRs, Dashboard, Catering, Office Events\"\n }\n ]\n }\n },\n \"id\": \"f16acb7e-f27d-4a95-845c-c990fc334795\",\n \"name\": \"Search notion database\",\n \"type\": \"@n8n/n8n-nodes-langchain.toolHttpRequest\",\n \"typeVersion\": 1.1,\n \"position\": [\n 1620,\n 640\n ],\n \"credentials\": {\n \"notionApi\": {\n \"id\": \"gfNp6Jup8rsmFLRr\",\n \"name\": \"max-bot\"\n }\n }\n },\n {\n \"parameters\": {\n \"public\": true,\n \"initialMessages\": \"=Happy {{ $today.weekdayLong }}!\\nKnowledge source assistant at your service. How can I help?\",\n \"options\": {\n \"subtitle\": \"\",\n \"title\": \"Notion Knowledge Base\"\n }\n },\n \"id\": \"9fc1ae38-d115-44d0-a088-7cec7036be6f\",\n \"name\": \"When chat message received\",\n \"type\": \"@n8n/n8n-nodes-langchain.chatTrigger\",\n \"typeVersion\": 1.1,\n \"position\": [\n 560,\n 460\n ],\n \"webhookId\": \"b76d02c0-b406-4d21-b6bf-8ad2c623def3\"\n },\n {\n \"parameters\": {\n \"resource\": \"database\",\n \"databaseId\": {\n \"__rl\": true,\n \"value\": \"7ea9697d-4875-441e-b262-1105337d232e\",\n \"mode\": \"list\",\n \"cachedResultName\": \"StarLens Company Knowledge Base\",\n \"cachedResultUrl\": \"https://www.notion.so/7ea9697d4875441eb2621105337d232e\"\n }\n },\n \"id\": \"9325e0fe-549f-423b-af48-85e802429a7f\",\n \"name\": \"Get database details\",\n \"type\": \"n8n-nodes-base.notion\",\n \"typeVersion\": 2.2,\n \"position\": [\n 760,\n 460\n ],\n \"credentials\": {\n \"notionApi\": {\n \"id\": \"gfNp6Jup8rsmFLRr\",\n \"name\": \"max-bot\"\n }\n }\n },\n {\n \"parameters\": {\n \"contextWindowLength\": 4\n },\n \"id\": \"637f5731-4442-42be-9151-30ee29ad97c6\",\n \"name\": \"Window Buffer Memory\",\n \"type\": \"@n8n/n8n-nodes-langchain.memoryBufferWindow\",\n \"typeVersion\": 1.2,\n \"position\": [\n 1460,\n 640\n ]\n },\n {\n \"parameters\": {\n \"toolDescription\": \"=Use this tool to retrieve Notion page content using the page ID. \\n\\nIt is structured with question and answer format. \\nYou can filter query result by:\\n- By keyword\\n- filter by tag.\\n\\nKeyword and Tag have an OR relationship not AND.\\n\\n\",\n \"url\": \"https://api.notion.com/v1/blocks/{page_id}/children\",\n \"authentication\": \"predefinedCredentialType\",\n \"nodeCredentialType\": \"notionApi\",\n \"placeholderDefinitions\": {\n \"values\": [\n {\n \"name\": \"page_id\",\n \"description\": \"Notion page id from 'Search notion database' tool results\"\n }\n ]\n },\n \"optimizeResponse\": true,\n \"dataField\": \"results\",\n \"fieldsToInclude\": \"selected\",\n \"fields\": \"id, type, paragraph.text, heading_1.text, heading_2.text, heading_3.text, bulleted_list_item.text, numbered_list_item.text, to_do.text, children\"\n },\n \"id\": \"6b87ae47-fac9-4ef5-aa9a-f1a1ae1adc5f\",\n \"name\": \"Search inside database record\",\n \"type\": \"@n8n/n8n-nodes-langchain.toolHttpRequest\",\n \"typeVersion\": 1.1,\n \"position\": [\n 1800,\n 640\n ],\n \"credentials\": {\n \"notionApi\": {\n \"id\": \"gfNp6Jup8rsmFLRr\",\n \"name\": \"max-bot\"\n }\n }\n },\n {\n \"parameters\": {\n \"promptType\": \"define\",\n \"text\": \"={{ $json.chatInput }}\",\n \"options\": {\n \"systemMessage\": \"=# Role:\\nYou are a helpful agent. Query the \\\"{{ $('workflow vars').item.json.databaseName }}\\\" Notion database to find relevant records or provide insights based on multiple records.\\n\\n# Behavior:\\n\\nBe clear, very concise, efficient, and accurate in responses. Do not hallucinate.\\nIf the request is ambiguous, ask for clarification. Do not embellish, only use facts from the Notion records. Never offer general advice.\\n\\n# Error Handling:\\n\\nIf no matching records are found, try alternative search criteria. Example: Laptop, then Computer, then Equipment. \\nClearly explain any issues with queries (e.g., missing fields or unsupported filters).\\n\\n# Output:\\n\\nReturn concise, user-friendly results or summaries.\\nFor large sets, show top results by default and offer more if needed. Output URLs in markdown format. \\n\\nWhen a record has the answer to user question, always output the URL to that page. Always list links to records separately at the end of the message like this:\\n\\\"Relevant pages: \\n(links in markdown format)\\\"\\nDo not output links twice, only in Relevant pages section\\n\"\n }\n },\n \"id\": \"17f2c426-c48e-48e0-9c5e-e35bdafe5109\",\n \"name\": \"AI Agent\",\n \"type\": \"@n8n/n8n-nodes-langchain.agent\",\n \"typeVersion\": 1.6,\n \"position\": [\n 1380,\n 460\n ]\n }\n ],\n \"connections\": {\n \"OpenAI Chat Model\": {\n \"ai_languageModel\": [\n [\n {\n \"node\": \"AI Agent\",\n \"type\": \"ai_languageModel\",\n \"index\": 0\n }\n ]\n ]\n },\n \"workflow vars\": {\n \"main\": [\n [\n {\n \"node\": \"format input for agent\",\n \"type\": \"main\",\n \"index\": 0\n }\n ]\n ]\n },\n \"format input for agent\": {\n \"main\": [\n [\n {\n \"node\": \"AI Agent\",\n \"type\": \"main\",\n \"index\": 0\n }\n ]\n ]\n },\n \"Search notion database\": {\n \"ai_tool\": [\n [\n {\n \"node\": \"AI Agent\",\n \"type\": \"ai_tool\",\n \"index\": 0\n }\n ]\n ]\n },\n \"When chat message received\": {\n \"main\": [\n [\n {\n \"node\": \"Get database details\",\n \"type\": \"main\",\n \"index\": 0\n }\n ]\n ]\n },\n \"Get database details\": {\n \"main\": [\n [\n {\n \"node\": \"workflow vars\",\n \"type\": \"main\",\n \"index\": 0\n }\n ]\n ]\n },\n \"Window Buffer Memory\": {\n \"ai_memory\": [\n [\n {\n \"node\": \"AI Agent\",\n \"type\": \"ai_memory\",\n \"index\": 0\n }\n ]\n ]\n },\n \"Search inside database record\": {\n \"ai_tool\": [\n [\n {\n \"node\": \"AI Agent\",\n \"type\": \"ai_tool\",\n \"index\": 0\n }\n ]\n ]\n }\n },\n \"pinData\": {}\n}\n }\n}];"
      },
      "typeVersion": 2
    },
    {
      "id": "dc15a250-074e-4aed-8eec-5c60c91cc42d",
      "name": "Set schem for rerun",
      "type": "n8n-nodes-base.set",
      "position": [
        3540,
        240
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "b4669a2c-7780-4c54-aef6-89a56ddf1d06",
              "name": "inputDatabase",
              "type": "object",
              "value": "={{ $json.inputDatabase }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "224f4963-caac-4438-a61b-90e2c0858f24",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1060,
        240
      ],
      "parameters": {
        "color": 7,
        "width": 747.234277816171,
        "height": 110.78786136085805,
        "content": "## #1 Serve chat, get URL from user, pull new notion DB schema\nUses n8n Chat trigger. Notion node will fail if an invalid URL is used, or if n8n doesn't have access to it. Also attempts to strip non URL text input. Simplifies notion DB outputs for more efficient token usage in AI Agent."
      },
      "typeVersion": 1
    },
    {
      "id": "7e18ca8d-3181-446f-96f5-0e4b1000d855",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1939,
        240
      ],
      "parameters": {
        "color": 7,
        "width": 638.6509136143742,
        "height": 114.20873484539783,
        "content": "## #2 GenAI step\nTakes 2 inputs: [original workflow template](https://n8n.io/workflows/2413-notion-knowledge-base-ai-assistant/) and new Notion database details from #1"
      },
      "typeVersion": 1
    },
    {
      "id": "b54b8c03-eb66-4ec7-bc7f-f62ddc566bbe",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2660,
        240
      ],
      "parameters": {
        "color": 7,
        "width": 727.8599253628195,
        "height": 111.9281525223713,
        "content": "## #3 Does the new workflow look right?\nChecks for previously identified cases (e.g. LLM outputs placeholder for certain values) then does general LLM check on whether it looks like valid n8n workflow JSON."
      },
      "typeVersion": 1
    },
    {
      "id": "a5cc97a7-33e3-45fe-9e13-45ebafd469d7",
      "name": "Add feedback prompt",
      "type": "n8n-nodes-base.set",
      "position": [
        3220,
        440
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "1243a328-8420-4be0-8932-4e153472a638",
              "name": "feedbackPrompt",
              "type": "string",
              "value": "=You attempted the below task and outputted incorrect JSON. Below is your incorrect attempt and original task prompt. Try again.\n\n# Incorrect task prompt\n"
            }
          ]
        },
        "includeOtherFields": true
      },
      "typeVersion": 3.4
    },
    {
      "id": "b066fa2d-77ba-4466-ae3b-9ab2405bae3c",
      "name": "Check for WF JSON errors",
      "type": "n8n-nodes-base.switch",
      "notes": "Placeholder jsonBody in tool - this means the 'Search notion database' tool got [object Object] as it's value (happening ~25% of the time)",
      "position": [
        2920,
        440
      ],
      "parameters": {
        "rules": {
          "values": [
            {
              "outputKey": "Placeholder jsonBody in tool",
              "conditions": {
                "options": {
                  "leftValue": "",
                  "caseSensitive": true,
                  "typeValidation": "strict"
                },
                "combinator": "and",
                "conditions": [
                  {
                    "operator": {
                      "type": "string",
                      "operation": "contains"
                    },
                    "leftValue": "={{ $json.searchNotionDBJsonBody }}",
                    "rightValue": "object Object"
                  }
                ]
              },
              "renameOutput": true
            }
          ]
        },
        "options": {
          "fallbackOutput": "extra",
          "allMatchingOutputs": false
        }
      },
      "typeVersion": 3.1
    },
    {
      "id": "e4b38c13-255d-4136-9c7b-90678cbe523b",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        3540,
        60
      ],
      "parameters": {
        "color": 7,
        "width": 343.3887397891673,
        "height": 132.30907857627597,
        "content": "## #4 Respond to Chat trigger\nEach response to the chat trigger is one run. Data of the last node that runs in the workflow is sent to chat trigger, like `Return success to chat`"
      },
      "typeVersion": 1
    },
    {
      "id": "3ecfadc2-2499-4e0f-94c4-1e68770beefb",
      "name": "Generate Workflow Agent",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "onError": "continueRegularOutput",
      "position": [
        2220,
        440
      ],
      "parameters": {
        "text": "=Your task is to output a modified version of a n8n workflow template so it works with the provided new notion database schema. \n\n\n# new notion database details\n{{ $json.inputDatabase.toJsonString() }}\n\n# n8n workflow template to use as reference\n{{ $json.workflowTemplate.toJsonString() }}\n\nJSON Output:\n- Ensure valid JSON with properly quoted keys and values, no trailing commas, and correctly nested braces `{}` and brackets `[]`. If unable to format, return an error or a valid example.\n- Output linebreaks so user can copy working JSON",
        "agent": "reActAgent",
        "options": {
          "prefix": "You are an n8n expert and understand n8n's workflow JSON Structure. You take n8n workflows and make changes to them based on the user request. \n\nDon't hallucinate. Only output n8n workflow json. \n\n",
          "returnIntermediateSteps": false
        },
        "promptType": "define",
        "hasOutputParser": true
      },
      "typeVersion": 1.6
    },
    {
      "id": "3ac37a66-30d5-404a-8c22-1402874e4f37",
      "name": "Anthropic Chat Model2",
      "type": "@n8n/n8n-nodes-langchain.lmChatAnthropic",
      "position": [
        3120,
        860
      ],
      "parameters": {
        "options": {
          "maxTokensToSample": 8192
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "f71ddd6e-7d41-405c-8cd8-bb21fc0654ae",
      "name": "When chat message received",
      "type": "@n8n/n8n-nodes-langchain.chatTrigger",
      "position": [
        1100,
        480
      ],
      "webhookId": "49dfdc22-b4c8-4ed3-baef-6751ec52f278",
      "parameters": {
        "public": true,
        "options": {
          "title": "🤖 Notion database assistant generator",
          "subtitle": "Generates an n8n workflow-based AI Agent that can query any arbitrary Notion database. ",
          "inputPlaceholder": "e.g. https://www.notion.so/n8n/34f67a14195344fda645691c63dc3901",
          "loadPreviousSession": "manually"
        },
        "initialMessages": "Hi there, I can help you make an AI Agent assistant that can query a Notion database.\n\nGenerating the workflow may take a few minutes as I check whether it works and try again if I oopsie.\n\nEnter a notion database URL and I'll output the workflow in JSON that you can paste in to the n8n canvas. \n"
      },
      "typeVersion": 1.1
    },
    {
      "id": "5a549080-0ad0-4f94-87b1-8b735d7b95a3",
      "name": "Valid n8n workflow JSON?",
      "type": "@n8n/n8n-nodes-langchain.textClassifier",
      "position": [
        3140,
        700
      ],
      "parameters": {
        "options": {
          "systemPromptTemplate": "You are an expert in n8n workflow automation tool. You know whether the json representation of an n8n workflow is valid. \n\nPlease classify the text provided by the user into one of the following categories: {categories}, and use the provided formatting instructions below. Don't explain, and only output the json."
        },
        "inputText": "={{ $json.generatedWorkflow }}",
        "categories": {
          "categories": [
            {
              "category": "invalidJSON",
              "description": "Any other workflow JSON"
            },
            {
              "category": "validJSON",
              "description": "A valid n8n workflow JSON"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "id": "02bf6e06-6671-4d18-ba30-117459e9d58a",
      "name": "Sticky Note5",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        380,
        500
      ],
      "parameters": {
        "color": 7,
        "width": 614.8565246662145,
        "height": 416.2640726760381,
        "content": "## Watch a quick set up video 👇\n[![Notion AI Assistant Generator](https://uploads.n8n.io/devrel/notion-db-assistant-thumb#full-width)](https://youtu.be/iK87ppcaNgM)\n"
      },
      "typeVersion": 1
    }
  ],
  "pinData": {},
  "connections": {
    "Notion": {
      "main": [
        [
          {
            "node": "standardize schema",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Return error to chat",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set input data": {
      "main": [
        [
          {
            "node": "Generate Workflow Agent",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "standardize schema": {
      "main": [
        [
          {
            "node": "Simplify properties object",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Add feedback prompt": {
      "main": [
        [
          {
            "node": "Set schem for rerun",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set schem for rerun": {
      "main": [
        [
          {
            "node": "Set input data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set schema for eval": {
      "main": [
        [
          {
            "node": "Check for WF JSON errors",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Anthropic Chat Model": {
      "ai_languageModel": [
        [
          {
            "node": "Generate Workflow Agent",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Anthropic Chat Model1": {
      "ai_languageModel": [
        [
          {
            "node": "Auto-fixing Output Parser",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Anthropic Chat Model2": {
      "ai_languageModel": [
        [
          {
            "node": "Valid n8n workflow JSON?",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Generate Workflow Agent": {
      "main": [
        [
          {
            "node": "Set schema for eval",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Check for WF JSON errors": {
      "main": [
        [
          {
            "node": "Add feedback prompt",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Valid n8n workflow JSON?",
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
            "node": "Auto-fixing Output Parser",
            "type": "ai_outputParser",
            "index": 0
          }
        ]
      ]
    },
    "Valid n8n workflow JSON?": {
      "main": [
        [
          {
            "node": "Set schem for rerun",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Return success to chat",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Auto-fixing Output Parser": {
      "ai_outputParser": [
        [
          {
            "node": "Generate Workflow Agent",
            "type": "ai_outputParser",
            "index": 0
          }
        ]
      ]
    },
    "Simplify properties object": {
      "main": [
        [
          {
            "node": "Set input data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "When chat message received": {
      "main": [
        [
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

<a id="template-1730"></a>

## Template 1730 - Criação/Atualização de contato Mautic com Calendly

- **Nome:** Criação/Atualização de contato Mautic com Calendly
- **Descrição:** Este fluxo cria ou atualiza contatos no Mautic sempre que um novo evento é criado no Calendly, usando o email como identificador e atualizando o primeiro nome.
- **Funcionalidade:** • Detecção de novos eventos do Calendly: disparo do fluxo quando um convite é criado.
• Criação/atualização de contato no Mautic: cria ou atualiza o contato com base no email, definindo o primeiro nome. Se o email já existir, o primeiro nome é atualizado.
• Registro de contexto explicativo: mantém uma nota com o objetivo do fluxo para referência.
- **Ferramentas:** • Calendly: Serviço de agendamento utilizado para disparar o fluxo quando um novo convidado é criado.
• Mautic: Plataforma de automação de marketing para gerenciar contatos e dados.

## Fluxo visual

```mermaid
flowchart LR
    N1["On new event"]
    N2["Create/update contact"]
    N3["Note"]

    N1 --> N2
```

## Fluxo (.json) :

```json
{
  "meta": {
    "instanceId": "237600ca44303ce91fa31ee72babcdc8493f55ee2c0e8aa2b78b3b4ce6f70bd9"
  },
  "nodes": [
    {
      "id": "40216649-af2c-44df-83c6-75afe75dcdaf",
      "name": "On new event",
      "type": "n8n-nodes-base.calendlyTrigger",
      "position": [
        400,
        240
      ],
      "webhookId": "28087fc9-e623-48fe-949e-e002cbc7a817",
      "parameters": {
        "events": [
          "invitee.created"
        ]
      },
      "credentials": {
        "calendlyApi": {
          "id": "38",
          "name": "[UPDATE ME]"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "46914a34-984e-4736-b2a3-6e97555b73c7",
      "name": "Create/update contact",
      "type": "n8n-nodes-base.mautic",
      "position": [
        620,
        240
      ],
      "parameters": {
        "email": "={{$node[\"On new event\"].json[\"payload\"][\"email\"]}}",
        "options": {},
        "firstName": "={{$json[\"payload\"][\"name\"]}}",
        "additionalFields": {}
      },
      "credentials": {
        "mauticApi": {
          "id": "34",
          "name": "[UPDATE ME]"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "df809a8d-7b05-4ecc-a022-7bb12842b4bc",
      "name": "Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -20,
        180
      ],
      "parameters": {
        "width": 313,
        "height": 229,
        "content": "### Create/update Mautic contact on a new Calendly event\n1. `On new event` triggers on new Calendly events.\n2. `Create/update contact` will create a contact in Mautic or update the contact's first name. If the contact's email is already in Mautic, then the first name will be overwritten to the new first name."
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "On new event": {
      "main": [
        [
          {
            "node": "Create/update contact",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-1731"></a>

## Template 1731 - Reengajamento pós-reunião com sugestões de disponibilidade

- **Nome:** Reengajamento pós-reunião com sugestões de disponibilidade
- **Descrição:** Verifica reuniões recentes, identifica contatos sem seguimento e sugere novas opções de horário usando IA; envia proposta para aprovação humana e agenda a reunião se confirmada.
- **Funcionalidade:** • Agendamento periódico: Executa checagens automáticas diariamente para analisar reuniões recentes.
• Coleta de eventos passados: Recupera reuniões ocorridas entre 2 e 4 dias atrás para avaliação.
• Remoção de duplicados: Evita processar o mesmo evento mais de uma vez entre execuções.
• Verificação de comunicação: Busca mensagens entre o usuário e o participante desde o fim da reunião para detectar follow-ups.
• Marcação para follow-up: Identifica reuniões sem contato subsequente e as sinaliza para ação.
• Sugestão de disponibilidade por IA: Analisa detalhes da reunião anterior (dia, hora, duração) e gera opções de horários semelhantes futuros.
• Formatação de mensagem: Compõe um e-mail com as opções de vagas sugeridas para envio ao usuário responsável.
• Aprovação humana: Envia a proposta ao usuário e aguarda resposta livre para confirmar ação.
• Agendamento automático: Se o usuário confirmar, agenda a nova reunião com os dados fornecidos.
- **Ferramentas:** • Google Calendar: Fonte de eventos e API para verificar disponibilidade e criar novos compromissos.
• Gmail: Envio de mensagens ao usuário e busca de comunicações com os participantes para detectar follow-ups.
• OpenAI (modelos de linguagem): Geração e análise de sugestões de disponibilidade e compreensão da resposta humana para decidir agendamento.

## Fluxo visual

```mermaid
flowchart LR
    N1["Schedule Trigger"]
    N2["Get Past Events"]
    N3["Loop Over Items"]
    N4["Flag to Follow Up"]
    N5["Only Follow Ups"]
    N6["Get Emails Since"]
    N7["Output"]
    N8["Availability"]
    N9["Model"]
    N10["Meeting Availability Agent"]
    N11["Generate Message"]
    N12["Meetings"]
    N13["Model1"]
    N14["Meeting Booking Agent"]
    N15["Mark as Seen"]
    N16["Sticky Note"]
    N17["Sticky Note1"]
    N18["Sticky Note2"]
    N19["Sticky Note3"]
    N20["Sticky Note4"]
    N21["Sticky Note5"]
    N22["Send for Human Approval"]

    N15 --> N3
    N2 --> N15
    N3 --> N5
    N3 --> N6
    N5 --> N10
    N11 --> N22
    N6 --> N4
    N1 --> N2
    N4 --> N3
    N22 --> N14
    N10 --> N11
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
      "id": "cbc2ee05-3bb9-4064-ac26-fed7241e673f",
      "name": "Schedule Trigger",
      "type": "n8n-nodes-base.scheduleTrigger",
      "position": [
        -460,
        0
      ],
      "parameters": {
        "rule": {
          "interval": [
            {
              "triggerAtHour": 6
            }
          ]
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "4a18dea4-9eda-4b8e-9d0c-fff9793802c5",
      "name": "Get Past Events",
      "type": "n8n-nodes-base.googleCalendar",
      "position": [
        -280,
        0
      ],
      "parameters": {
        "options": {},
        "timeMax": "={{ $now.minus({ day: 2 }) }}",
        "timeMin": "={{ $now.minus({ day: 4 }) }}",
        "calendar": {
          "__rl": true,
          "mode": "id",
          "value": "<your-calendar>"
        },
        "operation": "getAll"
      },
      "credentials": {
        "googleCalendarOAuth2Api": {
          "id": "kWMxmDbMDDJoYFVK",
          "name": "Google Calendar account"
        }
      },
      "typeVersion": 1.3
    },
    {
      "id": "df2ef6d0-5fcb-43c5-8ba9-2d094dffb4e1",
      "name": "Loop Over Items",
      "type": "n8n-nodes-base.splitInBatches",
      "position": [
        200,
        40
      ],
      "parameters": {
        "options": {}
      },
      "typeVersion": 3
    },
    {
      "id": "bedc77ad-f0c9-47ae-9609-48ceda47a224",
      "name": "Flag to Follow Up",
      "type": "n8n-nodes-base.set",
      "position": [
        580,
        200
      ],
      "parameters": {
        "mode": "raw",
        "options": {},
        "jsonOutput": "={{\n{\n  ...$('Loop Over Items').first().json,\n  followUp: $json.isEmpty()\n}\n}}",
        "includeOtherFields": true
      },
      "typeVersion": 3.4
    },
    {
      "id": "b332ca5d-45d5-4a79-a028-baa1728aea78",
      "name": "Only Follow Ups",
      "type": "n8n-nodes-base.filter",
      "position": [
        400,
        40
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
              "id": "73f38d1b-75c6-4372-8e81-a2db61b045a8",
              "operator": {
                "name": "filter.operator.equals",
                "type": "string",
                "operation": "equals"
              },
              "leftValue": "",
              "rightValue": ""
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "1b8a6510-f1c5-4969-a68d-143874b5737d",
      "name": "Get Emails Since",
      "type": "n8n-nodes-base.gmail",
      "position": [
        400,
        200
      ],
      "webhookId": "08fbccff-cce6-461a-b040-f5a74920c803",
      "parameters": {
        "limit": 1,
        "filters": {
          "q": "=(from:{{ $json.attendees.find(attendee => !attendee.self)?.email }} OR to:{{ $json.attendees.find(attendee => !attendee.self)?.email }})",
          "receivedAfter": "={{ $json.end.dateTime }}"
        },
        "resource": "thread"
      },
      "credentials": {
        "gmailOAuth2": {
          "id": "Sf5Gfl9NiFTNXFWb",
          "name": "Gmail account"
        }
      },
      "typeVersion": 2.1,
      "alwaysOutputData": true
    },
    {
      "id": "4ce7ac3f-bad8-4822-b166-fd164d733734",
      "name": "Output",
      "type": "@n8n/n8n-nodes-langchain.outputParserStructured",
      "position": [
        1140,
        220
      ],
      "parameters": {
        "schemaType": "manual",
        "inputSchema": "{\n  \"type\": \"object\",\n  \"properties\": {\n    \"slots\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"start\": { \"type\": \"string\" },\n          \"end\": { \"type\": \"string\" }\n        }\n      }\n    }\n  }\n}"
      },
      "typeVersion": 1.2
    },
    {
      "id": "a22c5b78-d213-4e37-b2c6-f3d1dac96858",
      "name": "Availability",
      "type": "n8n-nodes-base.googleCalendarTool",
      "position": [
        1020,
        220
      ],
      "parameters": {
        "options": {
          "timezone": {
            "__rl": true,
            "mode": "id",
            "value": "={{ /*n8n-auto-generated-fromAI-override*/ $fromAI('Timezone', ``, 'string') }}",
            "__regex": "([-+/_a-zA-Z0-9]*)"
          }
        },
        "timeMax": "={{ /*n8n-auto-generated-fromAI-override*/ $fromAI('End_Time', ``, 'string') }}",
        "timeMin": "={{ /*n8n-auto-generated-fromAI-override*/ $fromAI('Start_Time', ``, 'string') }}",
        "calendar": {
          "__rl": true,
          "mode": "id",
          "value": "<your-calendar>"
        },
        "resource": "calendar"
      },
      "credentials": {
        "googleCalendarOAuth2Api": {
          "id": "kWMxmDbMDDJoYFVK",
          "name": "Google Calendar account"
        }
      },
      "typeVersion": 1.3
    },
    {
      "id": "690c79d3-cf0e-4d15-9419-dafb7d86025b",
      "name": "Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        900,
        220
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
          "id": "8gccIjcuf3gvaoEr",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "4e9d23c0-f9a0-4e71-b1b8-1011313942ba",
      "name": "Meeting Availability Agent",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        920,
        40
      ],
      "parameters": {
        "text": "=### Details of the previous call as following\ntitle: {{ $json.summary }}\ndate: {{ $json.start.dateTime }} {{ $json.start.timeZone }}\nduration: {{ DateTime.fromISO($json.end.dateTime).diffTo(DateTime.fromISO($json.start.dateTime), 'minutes') }} minutes",
        "options": {
          "systemMessage": "=You are a calendar availability assistant. Analyse the previous meeting and help me find a similar available slot for the next meeting.\n* take into consideration the day, time of day and duration of the previous meeting and try to set the same or similar for the next\n* next meeting should be in the future.\n* return a list of available slots so that I can forward them to the user.\n\nToday's date is {{ $now }}."
        },
        "promptType": "define",
        "hasOutputParser": true
      },
      "typeVersion": 1.7
    },
    {
      "id": "851728bf-7f94-4434-9dc6-23569544cdb7",
      "name": "Generate Message",
      "type": "n8n-nodes-base.set",
      "position": [
        1260,
        40
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "cf09c95c-f25e-4fd7-bade-a0feaeaffb3b",
              "name": "message",
              "type": "string",
              "value": "=Hey, just noticed there wasn't a follow-up email to {{ $('Only Follow Ups').item.json.attendees.find(x => !x.self).email }} after your last call a few days ago.\n\nHere's are a few available slots to book the next call.\n{{\n$json.output.slots\n  .filter(slot => !DateTime.fromISO(slot.start).isWeekend())\n  .map(slot => `* ${DateTime.fromISO(slot.start).format('cccc, DDD @ hh:mm')} - ${DateTime.fromISO(slot.end).format('hh:mm')}`)\n.join('\\n')\n}}\n\nLet me know which I should book or let me know if it's okay to dismiss."
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "7e45eddc-8c34-402a-86a2-ed89ff463095",
      "name": "Meetings",
      "type": "n8n-nodes-base.googleCalendarTool",
      "position": [
        2360,
        240
      ],
      "parameters": {
        "end": "={{ /*n8n-auto-generated-fromAI-override*/ $fromAI('End', ``, 'string') }}",
        "start": "={{ /*n8n-auto-generated-fromAI-override*/ $fromAI('Start', ``, 'string') }}",
        "calendar": {
          "__rl": true,
          "mode": "id",
          "value": "<your-calendar>"
        },
        "additionalFields": {
          "summary": "={{ /*n8n-auto-generated-fromAI-override*/ $fromAI('Summary', ``, 'string') }}",
          "description": "={{ /*n8n-auto-generated-fromAI-override*/ $fromAI('Description', ``, 'string') }}"
        }
      },
      "credentials": {
        "googleCalendarOAuth2Api": {
          "id": "kWMxmDbMDDJoYFVK",
          "name": "Google Calendar account"
        }
      },
      "typeVersion": 1.3
    },
    {
      "id": "74618cf0-1fe5-4abb-ba38-6818162ce826",
      "name": "Model1",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        2180,
        240
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
          "id": "8gccIjcuf3gvaoEr",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "790cc7ee-fe1b-434f-8736-38952bffbb85",
      "name": "Meeting Booking Agent",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        2180,
        60
      ],
      "parameters": {
        "text": "={{ $json.data.text }}",
        "options": {
          "systemMessage": "=You are a meeting booking agent. Your task is to book the meeting requested if confirmed by the user or otherwise do nothing if the user wants to disregard. No need to ask for further approval.\n\nAI: {{ $('Generate Message').first().json.message }}"
        },
        "promptType": "define"
      },
      "typeVersion": 1.7
    },
    {
      "id": "7ed171b2-08ee-49b0-9f9b-b4943549b2f6",
      "name": "Mark as Seen",
      "type": "n8n-nodes-base.removeDuplicates",
      "position": [
        -100,
        0
      ],
      "parameters": {
        "options": {},
        "operation": "removeItemsSeenInPreviousExecutions",
        "dedupeValue": "={{ $json.id }}"
      },
      "typeVersion": 2
    },
    {
      "id": "c8198538-4e02-429d-9fef-4cc2cb0bb7d0",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -540,
        -200
      ],
      "parameters": {
        "color": 7,
        "width": 620,
        "height": 420,
        "content": "## 1. Get Recent Meetings\n[Learn more about the GCalendar node](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar)\n\nFor this template, a scheduled trigger is set to fire every morning to pull in past meetings from 2-3 days ago. A \"Remove Duplicates\" node ensures we don't double process events more than once between runs."
      },
      "typeVersion": 1
    },
    {
      "id": "ef4888e2-249f-4501-a731-4dc8886dfa1a",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        100,
        -160
      ],
      "parameters": {
        "color": 7,
        "width": 680,
        "height": 600,
        "content": "## 2. Check If Any Messages Since\n[Read more about the Gmail node](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail)\n\nNext, we want to check if there has been any messages/contact between the lead and the user since the meeting ended. Where there is not, it could be a good opportunity to remind the user to reengage the lead as to not lose them."
      },
      "typeVersion": 1
    },
    {
      "id": "d9ccc4d5-2ccb-4f85-ada1-6a6fc5374ff2",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        800,
        -160
      ],
      "parameters": {
        "color": 7,
        "width": 620,
        "height": 580,
        "content": "## 3. Suggest Availability For Next Call\n[Read more about AI Agents](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/)\n\nOnce filtered for applicable leads, we can use an AI Agent to suggest another meeting slot for them. An AI Agent can analyse the previous meeting details and use that information to suggest a similar date and time."
      },
      "typeVersion": 1
    },
    {
      "id": "851b15f6-ea6a-4d30-a45b-f9ed087a37fa",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1440,
        -200
      ],
      "parameters": {
        "color": 7,
        "width": 540,
        "height": 520,
        "content": "## 4. Get Human Approval\n[Learn more about n8n's Human-in-the-loop features](https://docs.n8n.io/advanced-ai/examples/human-fallback/)\n\nOf course, we don't want the AI to actually book the meeting unless the user confirms it is something he/she wants to do and the best way to confirm is just to ask the user directly! Thanks for n8n's Human-in-the-loop feature, we can achieve this with a number of messaging protocols.\n\nHere, we're using the Gmail node's **Send-and-wait-for-approval** mode. This will send an email to the user and give them a textbox to tell our agent what they want to do next."
      },
      "typeVersion": 1
    },
    {
      "id": "725b187f-d59b-4a7d-bf11-6265a4c995ed",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2000,
        -160
      ],
      "parameters": {
        "color": 7,
        "width": 640,
        "height": 560,
        "content": "## 5. Book the meeting If Accepted\n[Learn more about the AI Agent node](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/)\n\nFinally, the response from the user combined with the suggested availability slots are given to another AI agent which can book meetings. If the user accepted and confirmed a date, this agent will book the meeting on behalf of the user. If the user declined, then the agent takes no action."
      },
      "typeVersion": 1
    },
    {
      "id": "ae59a45a-01e9-42be-99da-f75ed90f881b",
      "name": "Sticky Note5",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -1000,
        -700
      ],
      "parameters": {
        "width": 420,
        "height": 980,
        "content": "## Try it out!\n### This n8n template extends the idea of sales leads follow-up reminders by having an AI agent suggest and book the next call or message to reengage the prospect.\n\nWhat makes this template practical for use is that it uses the Human-in-the-loop approach to wait for a user's approval before actually making the booking. Without, this could be annoying for both the user and the recipient!\n\n### How it works\n* A scheduled trigger checks your google calendar for sales meetings which happened a few days ago.\n* For each event, gmail search is used to figure out if a follow-up message has been sent or received from the other party since the meeting. If none, we want to remind ourselves to reengage the lead.\n* For leads applicable for follow-up, we first get an AI Agent to find available meeting slots in the calendar.\n* These slots and reminder are sent to the user via send-and-approval mode of the gmail node. The user replies in natural language either picking a slot, suggesting an entirely new slot or declines the request.\n* When accepted, another AI Agent books the meeting in the calendar with the proposed dates and lead.\n\n### How to use\n* Update all calendar nodes (+subnodes) to point to the right calendar. If this is a shared-purpose calendar, you may need to either filter or create a new calendar.\n* Update the gmail nodes to point to the right accounts.\n\n### Customising the template\n* Not using Google? Swap out for Microsoft or otherwise.\n* Try swapping out or adding in additional send-for-approval methods such as telegram or whatsapp.\n\n### Need Help?\nJoin the [Discord](https://discord.com/invite/XPKeKXeB7d) or ask in the [Forum](https://community.n8n.io/)!"
      },
      "typeVersion": 1
    },
    {
      "id": "46ef7220-49ea-4dfc-8e4c-ce7da5119daf",
      "name": "Send for Human Approval",
      "type": "n8n-nodes-base.gmail",
      "position": [
        1660,
        80
      ],
      "webhookId": "76b88312-1c54-482e-abdd-e699159577f0",
      "parameters": {
        "sendTo": "=<your-email-here>",
        "message": "={{ $json.message }}",
        "options": {},
        "subject": "=Book a follow-up meeting with {{ $('Only Follow Ups').item.json.attendees.find(x => !x.self).email }}?",
        "operation": "sendAndWait",
        "responseType": "freeText"
      },
      "credentials": {
        "gmailOAuth2": {
          "id": "Sf5Gfl9NiFTNXFWb",
          "name": "Gmail account"
        }
      },
      "typeVersion": 2.1
    }
  ],
  "pinData": {},
  "connections": {
    "Model": {
      "ai_languageModel": [
        [
          {
            "node": "Meeting Availability Agent",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Model1": {
      "ai_languageModel": [
        [
          {
            "node": "Meeting Booking Agent",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Output": {
      "ai_outputParser": [
        [
          {
            "node": "Meeting Availability Agent",
            "type": "ai_outputParser",
            "index": 0
          }
        ]
      ]
    },
    "Meetings": {
      "ai_tool": [
        [
          {
            "node": "Meeting Booking Agent",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Availability": {
      "ai_tool": [
        [
          {
            "node": "Meeting Availability Agent",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Mark as Seen": {
      "main": [
        [
          {
            "node": "Loop Over Items",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Past Events": {
      "main": [
        [
          {
            "node": "Mark as Seen",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Loop Over Items": {
      "main": [
        [
          {
            "node": "Only Follow Ups",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Get Emails Since",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Only Follow Ups": {
      "main": [
        [
          {
            "node": "Meeting Availability Agent",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Generate Message": {
      "main": [
        [
          {
            "node": "Send for Human Approval",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Emails Since": {
      "main": [
        [
          {
            "node": "Flag to Follow Up",
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
            "node": "Get Past Events",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Flag to Follow Up": {
      "main": [
        [
          {
            "node": "Loop Over Items",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Send for Human Approval": {
      "main": [
        [
          {
            "node": "Meeting Booking Agent",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Meeting Availability Agent": {
      "main": [
        [
          {
            "node": "Generate Message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-1733"></a>

## Template 1733 - Converter artigo WordPress em áudio

- **Nome:** Converter artigo WordPress em áudio
- **Descrição:** Este fluxo extrai um artigo do site, gera um resumo ou transcrição com um modelo de linguagem, converte o texto em áudio e publica o MP3 no próprio post do site.
- **Funcionalidade:** • Recuperar artigo do WordPress por ID: busca o conteúdo do post para processamento.
• Gerar resumo ou transcrição: utiliza um modelo de linguagem para resumir ou transcrever o texto do artigo conforme a configuração do fluxo.
• Permitir personalização do prompt: possibilita ajustar ou limpar o texto gerado antes da conversão para fala.
• Converter texto em fala via API: envia o texto ao serviço de TTS e obtém um arquivo de áudio (MP3) com formato configurável.
• Fazer upload do arquivo MP3 ao WordPress: publica o áudio na biblioteca de mídia do site com nome baseado no slug do post.
• Atualizar post com bloco de áudio: insere um bloco de áudio no conteúdo do post apontando para o arquivo enviado, mantendo o conteúdo original.
• Uso de configurações de site: utiliza uma variável de URL do site para compor endpoints de upload e atualização.
• Retentativa em falhas de upload: tenta reenviar o arquivo em caso de falhas temporárias para aumentar a resiliência.
- **Ferramentas:** • WordPress: CMS usado para recuperar artigos, armazenar mídia e atualizar o conteúdo do post.
• Eleven Labs: serviço de Text-to-Speech responsável por gerar o áudio a partir do texto.
• OpenAI: modelo de linguagem usado para gerar resumos, transcrições e para permitir a personalização do texto antes do TTS.

## Fluxo visual

```mermaid
flowchart LR
    N1["When clicking ‘Test workflow’"]
    N2["Retrieve WordPress Article"]
    N3["Generate Summary or Transcription"]
    N4["Generate Speech"]
    N5["Upload MP3"]
    N6["Update WordPress Post"]
    N7["Sticky Note1"]
    N8["Sticky Note"]
    N9["OpenAI Chat Model"]
    N10["settings"]

    N10 --> N2
    N5 --> N6
    N4 --> N5
    N2 --> N3
    N3 --> N4
    N1 --> N10
```

## Fluxo (.json) :

```json
{
  "meta": {
    "instanceId": "c911aed9995230b93fd0d9bc41c258d697c2fe97a3bab8c02baf85963eeda618",
    "templateCredsSetupCompleted": true
  },
  "nodes": [
    {
      "id": "468084ed-ce7d-45c5-bf27-ea9c91d5898a",
      "name": "When clicking ‘Test workflow’",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        0,
        0
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "fbde6cfe-9fac-46d2-958a-f42c9ef383a3",
      "name": "Retrieve WordPress Article",
      "type": "n8n-nodes-base.wordpress",
      "position": [
        440,
        0
      ],
      "parameters": {
        "postId": "1032",
        "options": {},
        "operation": "get"
      },
      "credentials": {
        "wordpressApi": {
          "id": "T0ygUN7hNFQVztP2",
          "name": "Wordpress account 2"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "54241e39-7a5f-45f4-9dab-72b5424f4061",
      "name": "Generate Summary or Transcription",
      "type": "@n8n/n8n-nodes-langchain.chainLlm",
      "position": [
        680,
        0
      ],
      "parameters": {
        "text": "={{ $json.content }}",
        "messages": {
          "messageValues": [
            {
              "message": "Summarize or transcribe this article, depending on the workflow setting."
            }
          ]
        },
        "promptType": "define",
        "hasOutputParser": true
      },
      "typeVersion": 1.5
    },
    {
      "id": "49cfaab6-a0c1-4319-904d-c1e0a2c6aa91",
      "name": "Generate Speech",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1120,
        0
      ],
      "parameters": {
        "url": "https://api.elevenlabs.io/v1/text-to-speech/voice_id",
        "method": "POST",
        "options": {},
        "sendBody": true,
        "authentication": "genericCredentialType",
        "bodyParameters": {
          "parameters": [
            {
              "name": "text",
              "value": "={{ $json.text }}"
            },
            {
              "name": "model_id",
              "value": "eleven_multilingual_v2"
            },
            {
              "name": "output_format",
              "value": "mp3_44100_128"
            }
          ]
        },
        "genericAuthType": "httpCustomAuth"
      },
      "credentials": {
        "httpCustomAuth": {
          "id": "wUJksQ68RUH0XuTO",
          "name": "Custom Auth account"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "899abf3f-4ab6-48bd-90ba-0502cb23348e",
      "name": "Upload MP3",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        2060,
        0
      ],
      "parameters": {
        "url": "={{ $('settings').item.json['site_url'] }}wp-json/wp/v2/media",
        "method": "POST",
        "options": {},
        "sendBody": true,
        "contentType": "binaryData",
        "sendHeaders": true,
        "authentication": "predefinedCredentialType",
        "headerParameters": {
          "parameters": [
            {
              "name": "Content-Disposition",
              "value": "=attachment; filename=\"{{ $('Retrieve WordPress Article').item.json.slug }}.mp3\""
            }
          ]
        },
        "inputDataFieldName": "data",
        "nodeCredentialType": "wordpressApi"
      },
      "credentials": {
        "wordpressApi": {
          "id": "T0ygUN7hNFQVztP2",
          "name": "Wordpress account 2"
        }
      },
      "retryOnFail": true,
      "typeVersion": 4.2
    },
    {
      "id": "590297c9-1f66-4071-8b47-230b08c379d4",
      "name": "Update WordPress Post",
      "type": "n8n-nodes-base.wordpress",
      "position": [
        2300,
        0
      ],
      "parameters": {
        "postId": "={{ $('Retrieve WordPress Article').item.json.id }}",
        "operation": "update",
        "updateFields": {
          "content": "=<!-- wp:audio {\"id\":{{ $json.id }}} -->\n<figure class=\"wp-block-audio\"><audio controls src=\"{{ $json.guid.rendered }}\"></audio><figcaption class=\"wp-element-caption\">🗣️ Listen to the summary or transcription. 👆</figcaption></figure>\n<!-- /wp:audio --><br>{{ $('Retrieve WordPress Article').item.json.content.rendered }}"
        }
      },
      "credentials": {
        "wordpressApi": {
          "id": "T0ygUN7hNFQVztP2",
          "name": "Wordpress account 2"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "5297d517-5dd9-4d4d-b201-0822af030c95",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1320,
        -340
      ],
      "parameters": {
        "color": 6,
        "width": 660,
        "height": 1000,
        "content": "## 🎙️ Generate Text-to-Speech Using Eleven Labs via API\n\nSince there is no predefined node for Eleven Labs in n8n, we will use the **HTTP Request** module.\n\n### 🛠️ Prerequisites:\n1. **Get an API Key**: Visit [Eleven Labs](https://try.elevenlabs.io/text-audio) to obtain your API key.\n2. **Choose a Suitable Voice**: Test different voices on [this demo page](https://try.elevenlabs.io/text-audio) to find the best fit for your use case.\n3. **Select the Right Model**: For multilingual usage, use:  \n   ~~~json\n   \"model_id\": \"eleven_multilingual_v2\"\n   ~~~\n4. **Set Output Format**: You can adjust the quality by modifying `output_format`, for example:  \n   ~~~json\n   \"output_format\": \"mp3_44100_128\"\n   ~~~\n\n📖 Refer to the full API documentation: [API Reference - Eleven Labs](https://try.elevenlabs.io/api-reference-text-to-speech)\n\n---\n## 🚀 Step 1: Configure API Credentials in n8n\n\nAdd a custom authentication entry in n8n with the following structure: \n\n(Replace `\"your-elevenlabs-api-key\"` with your **actual API key**)\n\n~~~json\n{\n  \"headers\": {\n    \"xi-api-key\": \"your-elevenlabs-api-key\"\n  }\n}\n~~~\n---\n\n## 📩 Step 2: Send a POST Request to the API\n\nMake an HTTP POST request to the **webhook** of your workflow with the following parameters:\n\n- **`voice_id`**: The ID of the selected voice.\n- **`text`**: The text to convert into speech.\n\n---"
      },
      "typeVersion": 1
    },
    {
      "id": "8fecbb98-8120-4d94-82ce-15efa063394b",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        640,
        -340
      ],
      "parameters": {
        "width": 460,
        "height": 280,
        "content": "# Modify This Prompt\n\nHere you can modify this prompt. It is interesting because the neutral node might return HTML, and using a ChatGPT node allows you to clean or customize the output before sending it to text-to-speech.\n\nIn the example provided, I requested a summary. However, you could ask for the benefits or product advantages when using it for e-commerce or affiliate marketing. You could also request the full transcription of the article."
      },
      "typeVersion": 1
    },
    {
      "id": "06e66119-2b95-416b-8167-41dccbbd8612",
      "name": "OpenAI Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        640,
        220
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
          "id": "yekgKa01FVKc8Etr",
          "name": "OpenAi account 2"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "47821853-b8f5-45f3-8e37-66365ba62422",
      "name": "settings",
      "type": "n8n-nodes-base.set",
      "position": [
        220,
        0
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "10c07d50-1310-4dd7-a143-b0c0e5cf1b70",
              "name": "site_url",
              "type": "string",
              "value": "https://mydomain.com/"
            }
          ]
        }
      },
      "typeVersion": 3.4
    }
  ],
  "pinData": {},
  "connections": {
    "settings": {
      "main": [
        [
          {
            "node": "Retrieve WordPress Article",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Upload MP3": {
      "main": [
        [
          {
            "node": "Update WordPress Post",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Generate Speech": {
      "main": [
        [
          {
            "node": "Upload MP3",
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
            "node": "Generate Summary or Transcription",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Retrieve WordPress Article": {
      "main": [
        [
          {
            "node": "Generate Summary or Transcription",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Generate Summary or Transcription": {
      "main": [
        [
          {
            "node": "Generate Speech",
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
            "node": "settings",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-1735"></a>

## Template 1735 - Transcrição de arquivo MP4 para texto

- **Nome:** Transcrição de arquivo MP4 para texto
- **Descrição:** Fluxo que lê um arquivo local de áudio/vídeo e envia para a API de transcrição da Eleven Labs para gerar texto.
- **Funcionalidade:** • Início manual: inicia o processo ao clicar em 'Test workflow'.
• Leitura de arquivo local: acessa o arquivo localizado em /files/tmp/tst1.mp4.
• Envio para transcrição: envia o arquivo como multipart/form-data para o endpoint de speech-to-text.
• Seleção de modelo: especifica model_id como scribe_v1 para realizar a transcrição.
• Autenticação: utiliza credenciais de API configuradas para autorizar a requisição.
• Cabeçalhos personalizados: define o cabeçalho Content-Type como multipart/form-data na requisição.
- **Ferramentas:** • Eleven Labs: serviço de transcrição (speech-to-text) usado para converter o áudio em texto via API.
• Sistema de arquivos local: armazena e fornece o arquivo de entrada (/files/tmp/tst1.mp4) que será transcrito.

## Fluxo visual

```mermaid
flowchart LR
    N1["When clicking ‘Test workflow’"]
    N2["Create Transcript1"]
    N3["Read/Write Files from Disk"]

    N3 --> N2
    N1 --> N3
```

## Fluxo (.json) :

```json
{
  "meta": {
    "instanceId": "c911aed9995230b93fd0d9bc41c258d697c2fe97a3bab8c02baf85963eeda618"
  },
  "nodes": [
    {
      "id": "fe599878-c955-4354-bbd0-a24fc1e3e933",
      "name": "When clicking ‘Test workflow’",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        -340,
        -40
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "e03c7cef-4897-4234-b285-7be69e3c970d",
      "name": "Create Transcript1",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        100,
        -40
      ],
      "parameters": {
        "url": "https://api.elevenlabs.io/v1/speech-to-text",
        "method": "POST",
        "options": {},
        "sendBody": true,
        "contentType": "multipart-form-data",
        "sendHeaders": true,
        "authentication": "genericCredentialType",
        "bodyParameters": {
          "parameters": [
            {
              "name": "file",
              "parameterType": "formBinaryData",
              "inputDataFieldName": "data"
            },
            {
              "name": "model_id",
              "value": "scribe_v1"
            }
          ]
        },
        "genericAuthType": "httpCustomAuth",
        "headerParameters": {
          "parameters": [
            {
              "name": "Content-Type",
              "value": "multipart/form-data"
            }
          ]
        }
      },
      "credentials": {
        "httpCustomAuth": {
          "id": "rDkSKjIA0mjmEv5k",
          "name": "Eleven Labs"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "ea48aabf-1d93-41b4-84a0-53115aba53b4",
      "name": "Read/Write Files from Disk",
      "type": "n8n-nodes-base.readWriteFile",
      "position": [
        -120,
        -40
      ],
      "parameters": {
        "options": {},
        "fileSelector": "/files/tmp/tst1.mp4"
      },
      "typeVersion": 1
    }
  ],
  "pinData": {},
  "connections": {
    "Read/Write Files from Disk": {
      "main": [
        [
          {
            "node": "Create Transcript1",
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
            "node": "Read/Write Files from Disk",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-1737"></a>

## Template 1737 - Criar cliente e adicioná‑lo a um segmento (Customer.io)

- **Nome:** Criar cliente e adicioná‑lo a um segmento (Customer.io)
- **Descrição:** Cria ou atualiza um cliente na plataforma Customer.io e o adiciona a um segmento específico.
- **Funcionalidade:** • Gatilho manual: inicia o fluxo ao clicar em executar.
• Criação/atualização de cliente: cria ou atualiza um cliente com ID fixo e adiciona propriedades personalizadas (ex.: Name = "n8n").
• Adição a segmento: obtém o ID do cliente criado/atualizado e o adiciona a um segmento na plataforma.
• Autenticação: utiliza credenciais configuradas para conectar-se à plataforma e executar as ações.
- **Ferramentas:** • Customer.io: Plataforma de automação de marketing e gerenciamento de clientes, usada para criar/atualizar clientes e gerenciar segmentação.

## Fluxo visual

```mermaid
flowchart LR
    N1["On clicking 'execute'"]
    N2["CustomerIo"]
    N3["CustomerIo1"]

    N2 --> N3
    N1 --> N2
```

## Fluxo (.json) :

```json
{
  "id": "32",
  "name": "Create a customer and add them to a segment in Customer.io",
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        440,
        260
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "CustomerIo",
      "type": "n8n-nodes-base.customerIo",
      "position": [
        650,
        260
      ],
      "parameters": {
        "id": "2",
        "additionalFields": {
          "customProperties": {
            "customProperty": [
              {
                "key": "Name",
                "value": "n8n"
              }
            ]
          }
        }
      },
      "credentials": {
        "customerIoApi": "cust"
      },
      "typeVersion": 1
    },
    {
      "name": "CustomerIo1",
      "type": "n8n-nodes-base.customerIo",
      "position": [
        840,
        260
      ],
      "parameters": {
        "resource": "segment",
        "customerIds": "={{$node[\"CustomerIo\"].json[\"id\"]}}"
      },
      "credentials": {
        "customerIoApi": "cust"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "CustomerIo": {
      "main": [
        [
          {
            "node": "CustomerIo1",
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
            "node": "CustomerIo",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-1739"></a>

## Template 1739 - Criar tarefa ClickUp via Slack e retornar ID

- **Nome:** Criar tarefa ClickUp via Slack e retornar ID
- **Descrição:** Este fluxo recebe comandos do Slack, cria uma nova tarefa no ClickUp com o conteúdo do Slack e responde com o ID da tarefa criada.
- **Funcionalidade:** • Recepção de comandos do Slack via webhook: o fluxo inicia ao receber o slash command e extrai informações como canal, usuário e texto.
• Criação de tarefa no ClickUp: utiliza as informações do Slack para criar uma nova tarefa com título e conteúdo.
• Resposta com o ID da tarefa: após a criação, responde com o ID da tarefa gerada.
- **Ferramentas:** • Slack: Plataforma de mensagens utilizada para receber o comando e acionar o fluxo.
• ClickUp: Ferramenta de gerenciamento de tarefas onde é criada a nova tarefa.

## Fluxo visual

```mermaid
flowchart LR
    N1["Respond to Webhook"]
    N2["Sticky Note"]
    N3["Receives slack command"]
    N4["Set your nodes"]
    N5["Create new clickup task"]
    N6["Sticky Note2"]

    N4 --> N5
    N3 --> N4
    N5 --> N1
```

## Fluxo (.json) :

```json
{
  "meta": {
    "instanceId": "1e5c69f0bf3f7484ac715feadbdb5d46fa5fa304d6cf822da9bd609721d1fee8"
  },
  "nodes": [
    {
      "id": "c39381ac-4795-4408-9383-7bae62755569",
      "name": "Respond to Webhook",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        1580,
        640
      ],
      "parameters": {
        "options": {},
        "respondWith": "text",
        "responseBody": "=Task Created: ID  {{ $json.id }}"
      },
      "typeVersion": 1
    },
    {
      "id": "ff72f0cb-1ea2-41e5-8f9f-7aa7ce994632",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        900,
        500
      ],
      "parameters": {
        "color": 4,
        "width": 874,
        "height": 359,
        "content": "## Create new tasks to airtable from a slack command"
      },
      "typeVersion": 1
    },
    {
      "id": "263f6c3b-5225-4d3f-a8ce-5052946b4251",
      "name": "Receives slack command",
      "type": "n8n-nodes-base.webhook",
      "position": [
        960,
        640
      ],
      "webhookId": "09d30853-66a3-4494-ba4b-115d28402811",
      "parameters": {
        "path": "09d30853-66a3-4494-ba4b-115d28402811/slackcommand",
        "options": {},
        "httpMethod": "POST",
        "responseMode": "responseNode"
      },
      "typeVersion": 1.1
    },
    {
      "id": "bbb46ec6-0b43-4a15-b12a-5e5d4b8d6c3d",
      "name": "Set your nodes",
      "type": "n8n-nodes-base.set",
      "position": [
        1160,
        640
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "8f6664ce-a3ad-42fb-84f7-58608d3c0ce8",
              "name": "channel_name",
              "type": "string",
              "value": "={{ $json.body.channel_name }}"
            },
            {
              "id": "54bf76f5-f00a-4f8e-bfcb-addd8af75a1a",
              "name": "command",
              "type": "string",
              "value": "={{ $json.body.command }}"
            },
            {
              "id": "37e273c0-2775-420b-9eb2-baeab3d1fdb6",
              "name": "user_name",
              "type": "string",
              "value": "={{ $json.body.user_name }}"
            },
            {
              "id": "6926bdae-e5eb-429d-a17d-7775b87184b1",
              "name": "text",
              "type": "string",
              "value": "={{ $json.body.text }}"
            }
          ]
        }
      },
      "typeVersion": 3.3
    },
    {
      "id": "f8b66cdb-3c56-4ec6-b2a2-f3fab8ba392c",
      "name": "Create new clickup task",
      "type": "n8n-nodes-base.clickUp",
      "position": [
        1340,
        640
      ],
      "parameters": {
        "list": "900900727522",
        "name": "={{ $json.text }}",
        "team": "9009074051",
        "space": "90090146907",
        "folderless": true,
        "authentication": "oAuth2",
        "additionalFields": {
          "content": "={{ $json.text }}",
          "assignees": []
        }
      },
      "credentials": {
        "clickUpOAuth2Api": {
          "id": "Cs34tMBCqaT1yt1w",
          "name": "ClickUp account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "47aa82ae-8a9c-40fa-be79-2bd602ffa045",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        400,
        300
      ],
      "parameters": {
        "width": 467,
        "height": 861.9451537637377,
        "content": "## Create new Clickup Tasks from Slack commands\nThis workflow aims to make it easy to create new tasks on Clickup from normal Slack messages using simple slack command. \n\nFor example We can have a slack command as \n\n/newTask Set task to update new contacts on CRM and assign them to the sales team\nThis will have an new task on Clickup with the same title and description on Clickup \n\nFor most teams, getting tasks from Slack to Clickup involves manually entering the new tasks into Clickup. What if we could do this with a simple slash command?\n\n## Step 1\nThe first step is to Create an endpoint URL for your slack command by creating an events API from the link [below] https://api.slack.com/apps/)\n\n## STEP 2 \nNext step is defining the endpoint for your URL\nCreate a new webhook endpoint from your n8n with a POST and paste the endpoint URL to your event API. This will send all slash commands associated with the Slash to the desired endpoint\n\n\nOnce you have tested the webhook slash command is working with the webhook, create a new Clickup API that can be used to create new tasks in ClickUp\n\nThis workflow creates a new task with the start dates on Clikup that can be assigned to the respective team members\n\nMore details about the document setup can be found on this document [below](https://docs.google.com/document/d/1jw_UP6sXmGsIMktW0Z-b-yQB1leDLatUY2393bA4z8s/edit?usp=sharing)\n\n   ####  Happy Productivity\n"
      },
      "typeVersion": 1
    }
  ],
  "pinData": {},
  "connections": {
    "Set your nodes": {
      "main": [
        [
          {
            "node": "Create new clickup task",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Receives slack command": {
      "main": [
        [
          {
            "node": "Set your nodes",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Create new clickup task": {
      "main": [
        [
          {
            "node": "Respond to Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-1741"></a>

## Template 1741 - Geração automática de artigos para base de conhecimento

- **Nome:** Geração automática de artigos para base de conhecimento
- **Descrição:** Fluxo que gera, edita e publica artigos de base de conhecimento combinando pesquisa profunda, geração de conteúdo e revisão editorial, com publicação automatizada no CMS.
- **Funcionalidade:** • Detecção de interesse via chat para iniciar a geração de artigo.
• Geração de estrutura completa do artigo (título, slug, categoria, descrição, palavras‑chave, conteúdo, meta titles, reading time e dificuldade).
• Pesquisa aprofundada do tema com fontes e citações.
• Combinação de saídas de diferentes agentes de IA para enriquecer o conteúdo final.
• Revisão editorial automática com sugestões de melhorias e decisão de publicação.
• Publicação automatizada no CMS (Contentful) após aprovação.
• Controle de iterações para evitar loops e excesso de revisões.
• Inclusão de fontes e contatos como referências no texto.
- **Ferramentas:** • Perplexity: Plataforma de pesquisa e geração de conteúdo que fornece conteúdo detalhado e citações.
• OpenAI: API de modelos de linguagem usados para criar, revisar e aperfeiçoar artigos.
• Contentful: CMS onde o artigo final é publicado e gerenciado.

## Fluxo visual

```mermaid
flowchart LR
    N1["Create Perplexity Content"]
    N2["AI Writer Agent"]
    N3["AI Editor Agent"]
    N4["OpenAI Chat Model"]
    N5["OpenAI Chat Model1"]
    N6["Accept and Publish"]
    N7["When chat message received"]
    N8["JSON.parse1"]
    N9["Merge"]
    N10["Format"]
    N11["JSON.parse"]
    N12["Format Perplexity Output & Add Citations"]
    N13["Initialize Count"]
    N14["Increment Count"]
    N15["Check Limit"]
    N16["Stop Here"]
    N17["Execute Workflow"]
    N18["JSON.parse3"]
    N19["should submit"]
    N20["Sticky Note"]
    N21["Sticky Note1"]
    N22["Sticky Note2"]
    N23["Sticky Note3"]

    N9 --> N10
    N10 --> N3
    N16 --> N18
    N11 --> N2
    N11 --> N14
    N15 --> N16
    N15 --> N19
    N8 --> N9
    N18 --> N17
    N19 --> N18
    N19 --> N11
    N3 --> N15
    N2 --> N1
    N2 --> N8
    N14 --> N9
    N13 --> N2
    N13 --> N14
    N1 --> N12
    N7 --> N13
    N12 --> N9
```

## Fluxo (.json) :

```json
{
  "id": "WwEFqNK4YP6UJcg2",
  "meta": {
    "instanceId": "6bcff5ef8a06e8086902526a05c2a4c7bf5da8101f89e582301ed78094606f40",
    "templateCredsSetupCompleted": true
  },
  "name": "Auto Knowledge Base Article Generator",
  "tags": [],
  "nodes": [
    {
      "id": "17900021-8da3-4bd9-9d79-5d20d879ddc7",
      "name": "Create Perplexity Content",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1220,
        380
      ],
      "parameters": {
        "url": "https://api.perplexity.ai/chat/completions",
        "method": "POST",
        "options": {},
        "jsonBody": "={\n  \"model\": \"sonar-deep-research\",\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": \"Conduct an in-depth research on '{{ $json.output.parseJson().title }}', covering essential topics, recommended resources, and best practices. Additionally, please address these improvements: '{{ $json.output.parseJson().improvements }}'. The returned data should be at least 1000 words and use a combination of headers, tables, bold, and italics\"\n    }\n  ],\n  \"max_tokens\": 60000,\n  \"temperature\": 0.7,\n  \"top_p\": 0.9,\n  \"top_k\": 50,\n  \"stream\": false,\n  \"presence_penalty\": 0,\n  \"frequency_penalty\": 0\n}",
        "sendBody": true,
        "jsonHeaders": "{\n  \"Authorization\": \"Bearer PERPLEXITY_KEY_REMOVIDA\",\n  \"Content-Type\": \"application/json\"\n}",
        "sendHeaders": true,
        "specifyBody": "json",
        "specifyHeaders": "json"
      },
      "typeVersion": 4.2
    },
    {
      "id": "0cb3f3a7-92bd-4ff3-8a89-b6fc29513e65",
      "name": "AI Writer Agent",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        720,
        380
      ],
      "parameters": {
        "text": "=Please create or revise an article about \"{{ $json.chatInput }}\".\n\nOr an article is already written because title: {{ $json.title }} is defined. Reference it to rewrite the {{ $json.content }} field\n\nDo not change the title, either the chatinput or the input article title. This is the title, do not change it.\n\nIf an article is NOT given, pick new categories in:\n- getting-started\n- learning-paths\n- certifications\n- programming\n- applications\n- career\n\nDo not make up a category, it should be the same in the exact case as above\n\nIf an article is given, only make ammendments to the content based on these specific improvements to include: \"{{ $json.improvements }}\".\n\nInclude the improvements key only if it is an input, and in that case don't change it\n\nRemember to return valid JSON with the fields:\n{\n  \"title\": \"...\",\n  \"slug\": \"...\",\n  \"category\": {\n    \"id\": \"...\"\n  },\n  \"description\": \"...\",\n  \"keywords\": [...],\n  \"content\": \"...\",\n  \"metaTitle\": \"...\",\n  \"metaDescription\": \"...\",\n  \"readingTime\": \"...\",\n  \"difficulty\": \"...\"\n  \"content\": \"...\"\n}",
        "options": {
          "systemMessage": "You are a writing assistant. You will receive instructions to create or update an article in JSON format with the following structure:\n\n{\n  \"title\": \"<string>\",\n  \"slug\": \"<string>\",\n  \"category\": {\n    \"id\": \"<string>\" // e.g., \"getting-started\", \"learning-paths\", etc.\n  },\n  \"description\": \"<string>\",\n  \"keywords\": [\"<string>\", \"<string>\", ...],\n  \"content\": \"<string>\",\n  \"metaTitle\": \"<string>\",\n  \"metaDescription\": \"<string>\",\n  \"readingTime\": \"<number or string>\",\n  \"difficulty\": \"<string>\"\n}\n\nYour task:\n1. Produce a complete article in the above format, or revise the existing article if provided.\n2. Make sure the text is clear, specific, and helpful to the reader.\n3. Return valid JSON only – do not include extra commentary or fields beyond the above structure.\n4. If any information is missing from the user instructions, make reasonable assumptions.\n"
        },
        "promptType": "define"
      },
      "typeVersion": 1.7
    },
    {
      "id": "bc62facb-c5cb-465d-89b1-a65a893c3ce1",
      "name": "AI Editor Agent",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        2280,
        380
      ],
      "parameters": {
        "text": "={{ $json }}",
        "options": {
          "maxIterations": 5,
          "systemMessage": "=You are an editorial AI assistant. Your role is to review and evaluate a draft article represented as a JSON object.\n\nCategory IDs:\n- \"getting-started\"\n- \"learning-paths\"\n- \"certifications\"\n- \"programming\"\n- \"applications\"\n- \"career\"\n\nInput Format:\n\n{\n  \"title\": \"<string>\",\n  \"slug\": \"<string>\",\n  \"category\": { \"id\": \"<string>\" },\n  \"description\": \"<string>\",\n  \"keywords\": [\"<string>\", \"...\"],\n  \"content\": \"<string>\",\n  \"metaTitle\": \"<string>\",\n  \"metaDescription\": \"<string>\",\n  \"readingTime\": \"<string | number>\",\n  \"difficulty\": \"<string>\"\n}\n\nYour Tasks:\n\n1. Evaluate the quality of the article — especially the title, description, content, and metadata.\n2. Comment on clarity, specificity, usefulness, and overall quality.\n3. If improvements are needed, add an \"improvements\" field describing exactly what to fix.\n4. Set the \"action\" field:\n- \"rewrite\" if improvements are needed.\n- \"submit\" if the article is high quality.\n5. Include all fields from the original input in your output.\n6. If \"action\" is \"submit\", set \"improvements\" to null.\n7. Avoid repeating feedback across iterations.\n8. After 2 iterations, automatically call the accept-and-publish tool and set the \"action\" to \"submit\".\n9. VERY IMPORTANT: Do NOT modify any of the input fields\n10. VERY IMPORTANT: Do NOT truncate the sources or modify the content field in any way\n\n✅ Output Format:\n\n{\n  \"title\": \"...\",\n  \"action\": \"rewrite | submit\",\n  \"improvements\": \"... | null\",\n  \"slug\": \"...\",\n  \"category\": {\n    \"id\": \"...\"\n  },\n  \"description\": \"...\",\n  \"keywords\": [\"...\"],\n  \"content\": \"...\",\n  \"metaTitle\": \"...\",\n  \"metaDescription\": \"...\",\n  \"readingTime\": \"...\",\n  \"difficulty\": \"...\"\n}\n\nTone: Be concise, direct, and constructive. Focus on maximizing clarity, usefulness, and readability for the end reader."
        },
        "promptType": "define",
        "hasOutputParser": true
      },
      "retryOnFail": true,
      "typeVersion": 1.7
    },
    {
      "id": "8c08d67a-b916-4cfd-89cd-16b34250bcb2",
      "name": "OpenAI Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        680,
        640
      ],
      "parameters": {
        "model": {
          "__rl": true,
          "mode": "list",
          "value": "gpt-3.5-turbo",
          "cachedResultName": "gpt-3.5-turbo"
        },
        "options": {}
      },
      "credentials": {
        "openAiApi": {
          "id": "KLN8ZfDzv8mW6pyu",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "97bb1374-f502-4152-a5a3-bc5d46a18171",
      "name": "OpenAI Chat Model1",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        2200,
        660
      ],
      "parameters": {
        "model": {
          "__rl": true,
          "mode": "list",
          "value": "gpt-4.5-preview",
          "cachedResultName": "gpt-4.5-preview"
        },
        "options": {}
      },
      "credentials": {
        "openAiApi": {
          "id": "KLN8ZfDzv8mW6pyu",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "1c422e76-5b1a-4615-b379-ab39d4bd13b4",
      "name": "Accept and Publish",
      "type": "@n8n/n8n-nodes-langchain.toolWorkflow",
      "position": [
        2500,
        680
      ],
      "parameters": {
        "name": "submit",
        "workflowId": {
          "__rl": true,
          "mode": "list",
          "value": "uIREtTV8TRuF3lru",
          "cachedResultName": "Publish to Contentful"
        },
        "description": "Call this tool when the article quality is above the threshold we need",
        "workflowInputs": {
          "value": {
            "slug": "=  {{ $json.slug }}",
            "title": "={{ $('Format').item.json.title }}",
            "content": "={{ $json.content }}",
            "category": "={{ $json.category }}",
            "keywords": "={{ $json.keywords }}",
            "metaTitle": "={{ $json.metaTitle }}",
            "difficulty": "={{ $json.difficulty }}",
            "description": "={{ $json.description }}",
            "readingTime": "={{ $json.readingTime }}",
            "metaDescription": "={{ $json.metaDescription }}"
          },
          "schema": [
            {
              "id": "title",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "title",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "action",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "action",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "improvements",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "improvements",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "slug",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "slug",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "category",
              "type": "object",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "category",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "description",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "description",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "keywords",
              "type": "array",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "keywords",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "content",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "content",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "metaTitle",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "metaTitle",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "metaDescription",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "metaDescription",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "readingTime",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "readingTime",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "difficulty",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "difficulty",
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
      "typeVersion": 2
    },
    {
      "id": "b6807e84-900a-48fc-a869-862824c62ba1",
      "name": "When chat message received",
      "type": "@n8n/n8n-nodes-langchain.chatTrigger",
      "position": [
        -60,
        660
      ],
      "webhookId": "7ed20abc-d8bc-4426-95f1-b9778c075ddf",
      "parameters": {
        "public": true,
        "options": {},
        "initialMessages": "What topics should I write about?"
      },
      "typeVersion": 1.1
    },
    {
      "id": "e3021ac4-9444-4689-af0c-a4bbd4729c35",
      "name": "JSON.parse1",
      "type": "n8n-nodes-base.code",
      "position": [
        1320,
        120
      ],
      "parameters": {
        "mode": "runOnceForEachItem",
        "jsCode": "const outputText = $json.output;\n\n// Parse JSON from ChatGPT response\nconst parsedOutput = JSON.parse(outputText);\n\n// Return parsed object for next nodes\nreturn parsedOutput;"
      },
      "typeVersion": 2
    },
    {
      "id": "d6a5eccd-c8e3-4ee0-beb0-7b8fc8428b91",
      "name": "Merge",
      "type": "n8n-nodes-base.merge",
      "position": [
        1840,
        380
      ],
      "parameters": {
        "numberInputs": 3
      },
      "typeVersion": 3
    },
    {
      "id": "8461a1a0-a984-4ec1-bc93-3a1a312caf55",
      "name": "Format",
      "type": "n8n-nodes-base.code",
      "position": [
        2060,
        380
      ],
      "parameters": {
        "jsCode": "// Get all items passed into this node as an array\nconst items = $input.all();\n\n// If you always have at least two items:\nconst firstItem = items[0].json;\nconst secondItem = items[1].json;\nconst thirdItem = items[2].json;\n\n// Overwrite the first item’s “content” with the second item’s “content”\nfirstItem.content = secondItem.content;\nfirstItem.iterationCount = thirdItem.iterationCount\n\n// Return a single new item containing the merged result\nreturn [\n  {\n    json: firstItem\n  }\n];"
      },
      "typeVersion": 2
    },
    {
      "id": "9b9a82fb-990c-4be0-aee9-ed80f0631c28",
      "name": "JSON.parse",
      "type": "n8n-nodes-base.code",
      "position": [
        3300,
        840
      ],
      "parameters": {
        "mode": "runOnceForEachItem",
        "jsCode": "const outputText = $json.output;\n\n// Parse JSON from ChatGPT response\nconst parsedOutput = JSON.parse(outputText);\n\n// Return parsed object for next nodes\nreturn parsedOutput;"
      },
      "typeVersion": 2
    },
    {
      "id": "066dfd10-e97a-44a8-89e0-5b2b5c4a6244",
      "name": "Format Perplexity Output & Add Citations",
      "type": "n8n-nodes-base.code",
      "position": [
        1480,
        380
      ],
      "parameters": {
        "mode": "runOnceForEachItem",
        "jsCode": "const data = { ...$json };\n\n// Clean out <think> block if present\ndata.content = $json.choices[0].message.content.replace(/<think>[\\s\\S]*?</think>/g, '').trim();\n\n// Convert citations array to markdown link list\nconst citations = $json.citations\n  .map((url, i) => `- [${i + 1}](${url})`)\n  .join('\\n');\n\ndata.content += `\\n\\n---\\n\\n### Sources\\n${citations}`;\n\nreturn data;"
      },
      "typeVersion": 2
    },
    {
      "id": "fc9d9e93-568a-41af-a295-8736617b157e",
      "name": "Initialize Count",
      "type": "n8n-nodes-base.set",
      "position": [
        340,
        660
      ],
      "parameters": {
        "values": {
          "number": [
            {
              "name": "iterationCount"
            }
          ]
        },
        "options": {}
      },
      "typeVersion": 1
    },
    {
      "id": "b0e636dd-f572-4ee2-832f-4bb4167b011b",
      "name": "Increment Count",
      "type": "n8n-nodes-base.function",
      "position": [
        1400,
        740
      ],
      "parameters": {
        "functionCode": "const current = $json.iterationCount || 0;\n\nreturn [{ iterationCount: current + 1 }];"
      },
      "typeVersion": 1
    },
    {
      "id": "86689f0e-9607-4eda-bcd6-36241d0cbe63",
      "name": "Check Limit",
      "type": "n8n-nodes-base.if",
      "position": [
        2660,
        380
      ],
      "parameters": {
        "conditions": {
          "number": [
            {
              "value1": "={{ $json.iterationCount }}",
              "value2": 3,
              "operation": "largerEqual"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "id": "0f42b0f3-0b96-40df-9c06-2a6d31e142d9",
      "name": "Stop Here",
      "type": "n8n-nodes-base.noOp",
      "position": [
        2980,
        300
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "1e61b3ba-e9bd-43c7-8217-d4a22f707318",
      "name": "Execute Workflow",
      "type": "n8n-nodes-base.executeWorkflow",
      "position": [
        3740,
        300
      ],
      "parameters": {
        "options": {},
        "workflowId": {
          "__rl": true,
          "mode": "list",
          "value": "uIREtTV8TRuF3lru",
          "cachedResultName": "Publish to Contentful"
        },
        "workflowInputs": {
          "value": {
            "slug": "={{ $json.slug }}",
            "title": "={{ $json.title }}",
            "content": "={{ $json.content }}",
            "category": "={{ $json.category }}",
            "keywords": "={{ $json.keywords }}",
            "metaTitle": "={{ $json.metaTitle }}",
            "difficulty": "={{ $json.difficulty }}",
            "description": "={{ $json.description }}",
            "readingTime": "={{ $json.readingTime }}",
            "metaDescription": "={{ $json.metaDescription }}"
          },
          "schema": [
            {
              "id": "title",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "title",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "slug",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "slug",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "category",
              "type": "object",
              "display": true,
              "required": false,
              "displayName": "category",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "description",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "description",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "keywords",
              "type": "array",
              "display": true,
              "required": false,
              "displayName": "keywords",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "content",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "content",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "metaTitle",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "metaTitle",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "metaDescription",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "metaDescription",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "readingTime",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "readingTime",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "difficulty",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "difficulty",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            }
          ],
          "mappingMode": "defineBelow",
          "matchingColumns": [],
          "attemptToConvertTypes": false,
          "convertFieldsToString": true
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "04526224-e48c-4032-9c92-475c6bf9cd0a",
      "name": "JSON.parse3",
      "type": "n8n-nodes-base.code",
      "position": [
        3280,
        300
      ],
      "parameters": {
        "mode": "runOnceForEachItem",
        "jsCode": "const outputText = $json.output;\n\n// Parse JSON from ChatGPT response\nconst parsedOutput = JSON.parse(outputText);\n\n// Return parsed object for next nodes\nreturn parsedOutput;"
      },
      "typeVersion": 2
    },
    {
      "id": "0303ab91-b788-4074-a15d-239565528dec",
      "name": "should submit",
      "type": "n8n-nodes-base.if",
      "position": [
        2980,
        680
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
              "id": "3c1f6cb2-a556-4c74-885e-05e4f757997b",
              "operator": {
                "name": "filter.operator.equals",
                "type": "string",
                "operation": "equals"
              },
              "leftValue": "submit",
              "rightValue": "={{ $json.output.parseJson().action }}"
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "4f68e1ad-0b7c-41ca-a9cc-d220017cc1bd",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        540,
        80
      ],
      "parameters": {
        "color": 6,
        "width": 940,
        "height": 680,
        "content": "## Writer Agent\n\n- Focuses on writing for all the fields in contentful\n- Has a specified format for input and output\n- Handles implementing feedback from editor agent"
      },
      "typeVersion": 1
    },
    {
      "id": "f5e9968a-0681-4b72-9bb3-98750f55565e",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2620,
        120
      ],
      "parameters": {
        "color": 3,
        "width": 860,
        "height": 880,
        "content": "## Count Incrementer\n\n- Tracks a variable count to ensure the flow hits a max number of feedback iterations.\n- This is critical for feedback to avoid hitting an infinite loop."
      },
      "typeVersion": 1
    },
    {
      "id": "462e6c9a-162a-4f66-b846-14b29517454c",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2140,
        160
      ],
      "parameters": {
        "width": 460,
        "height": 640,
        "content": "## Editor Agent\n\n- Sole purpose is to look at the quality of output for the previous combo of perplexity & openAI Agent.\n- Determines if it is publishable or not."
      },
      "typeVersion": 1
    },
    {
      "id": "27149a0a-ab95-4f73-a20c-34167ac56d2a",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        3580,
        60
      ],
      "parameters": {
        "color": 4,
        "width": 460,
        "height": 480,
        "content": "## Publish To Contentful\n\n- Publishes to Contentful by converting the fields to the appropriate fields for the contentful POST create content API.\n- Converts the article to Rich Text formatting specifically for Contentful by using another AI formatter trained on it's specs.\n\nemail us if you want that flow too: christian@varritech.com"
      },
      "typeVersion": 1
    }
  ],
  "active": true,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "69ce37b2-0909-4d9e-af89-992e22888bd8",
  "connections": {
    "Merge": {
      "main": [
        [
          {
            "node": "Format",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Format": {
      "main": [
        [
          {
            "node": "AI Editor Agent",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Stop Here": {
      "main": [
        [
          {
            "node": "JSON.parse3",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "JSON.parse": {
      "main": [
        [
          {
            "node": "AI Writer Agent",
            "type": "main",
            "index": 0
          },
          {
            "node": "Increment Count",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Check Limit": {
      "main": [
        [
          {
            "node": "Stop Here",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "should submit",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "JSON.parse1": {
      "main": [
        [
          {
            "node": "Merge",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "JSON.parse3": {
      "main": [
        [
          {
            "node": "Execute Workflow",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "should submit": {
      "main": [
        [
          {
            "node": "JSON.parse3",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "JSON.parse",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "AI Editor Agent": {
      "main": [
        [
          {
            "node": "Check Limit",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "AI Writer Agent": {
      "main": [
        [
          {
            "node": "Create Perplexity Content",
            "type": "main",
            "index": 0
          },
          {
            "node": "JSON.parse1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Increment Count": {
      "main": [
        [
          {
            "node": "Merge",
            "type": "main",
            "index": 2
          }
        ]
      ]
    },
    "Initialize Count": {
      "main": [
        [
          {
            "node": "AI Writer Agent",
            "type": "main",
            "index": 0
          },
          {
            "node": "Increment Count",
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
            "node": "AI Writer Agent",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Accept and Publish": {
      "ai_tool": [
        [
          {
            "node": "AI Editor Agent",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Chat Model1": {
      "ai_languageModel": [
        [
          {
            "node": "AI Editor Agent",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Create Perplexity Content": {
      "main": [
        [
          {
            "node": "Format Perplexity Output & Add Citations",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "When chat message received": {
      "main": [
        [
          {
            "node": "Initialize Count",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Format Perplexity Output & Add Citations": {
      "main": [
        [
          {
            "node": "Merge",
            "type": "main",
            "index": 1
          }
        ]
      ]
    }
  }
}
```

<a id="template-1742"></a>

## Template 1742 - API REST multi-métodos para clientes (Airtable)

- **Nome:** API REST multi-métodos para clientes (Airtable)
- **Descrição:** Expõe endpoints HTTP para criar, listar, obter, atualizar e deletar registros de clientes armazenados em uma base do Airtable.
- **Funcionalidade:** • Listar clientes: Retorna todos os registros de clientes.
• Criar cliente: Cria um novo registro usando campos (customer_id, first_name, last_name, email, phone, address).
• Obter cliente por ID: Recupera um único registro filtrando pelo campo customer_id recebido como parâmetro de URL.
• Atualizar cliente: Atualiza campos de um cliente existente identificando-o pelo customer_id.
• Deletar cliente: Localiza o registro pelo customer_id e remove o registro correspondente na base.
• Respostas HTTP: Retorna códigos HTTP apropriados (por exemplo, 201 para criação e 200 para sucesso nas demais operações).
- **Ferramentas:** • Airtable: Base de dados online usada para armazenar e manipular registros de clientes (CRUD) via API.
• Endpoints HTTP / Webhooks: Ponto de entrada público que recebe requisições REST (GET, POST, PUT, DELETE) para as rotas /customers e /customers/:id.

## Fluxo visual

```mermaid
flowchart LR
    N1["Respond to Webhook"]
    N2["Respond to Webhook1"]
    N3["Respond to Webhook2"]
    N4["Respond to Webhook4"]
    N5["Sticky Note"]
    N6["Create"]
    N7["Get All"]
    N8["Sticky Note1"]
    N9["Sticky Note2"]
    N10["Get Single"]
    N11["Sticky Note3"]
    N12["Airtable"]
    N13["Respond to Webhook5"]
    N14["Sticky Note4"]
    N15["Airtable1"]
    N16["Get Single1"]
    N17["Webhook"]
    N18["Webhook (with ID)"]

    N6 --> N2
    N7 --> N4
    N17 --> N7
    N17 --> N6
    N12 --> N3
    N15 --> N13
    N10 --> N1
    N16 --> N15
    N18 --> N10
    N18 --> N16
    N18 --> N12
```

## Fluxo (.json) :

```json
{
  "id": "GWXjIqENWvx6OqvX",
  "meta": {
    "instanceId": "94467bfa3af1aedd621d1940913d2d1a79e58bb9e7bbb0aa858d7f4a635296a5",
    "templateCredsSetupCompleted": true
  },
  "name": "TEMPLATE - Multi Methods API Endpoint",
  "tags": [],
  "nodes": [
    {
      "id": "d5b5010f-97fb-4f80-871b-e9f04b3977a9",
      "name": "Respond to Webhook",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        1220,
        -180
      ],
      "parameters": {
        "options": {},
        "respondWith": "allIncomingItems"
      },
      "typeVersion": 1.1
    },
    {
      "id": "46711e2f-6cd1-4947-9452-7a1484ae562f",
      "name": "Respond to Webhook1",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        1220,
        860
      ],
      "parameters": {
        "options": {
          "responseCode": 201
        },
        "respondWith": "allIncomingItems"
      },
      "typeVersion": 1.1
    },
    {
      "id": "20489a88-39a5-4cf7-8c08-826e4e9a7f34",
      "name": "Respond to Webhook2",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        1220,
        340
      ],
      "parameters": {
        "options": {
          "responseCode": 200
        },
        "respondWith": "allIncomingItems"
      },
      "typeVersion": 1.1
    },
    {
      "id": "04320a5f-29fe-42b0-9e01-31035f23b9dc",
      "name": "Respond to Webhook4",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        1220,
        600
      ],
      "parameters": {
        "options": {},
        "respondWith": "allIncomingItems"
      },
      "typeVersion": 1.1
    },
    {
      "id": "45ef8f08-f765-440d-be85-12096b6b4105",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        940,
        765.3897477624087
      ],
      "parameters": {
        "color": 4,
        "width": 514,
        "height": 255.253864930838,
        "content": "#### Creation\nCreates a new record"
      },
      "typeVersion": 1
    },
    {
      "id": "2e820357-250c-41a7-9daa-4eb77e7eded6",
      "name": "Create",
      "type": "n8n-nodes-base.airtable",
      "position": [
        1000,
        860
      ],
      "parameters": {
        "base": {
          "__rl": true,
          "mode": "list",
          "value": "app662qLY5J8ys4fU",
          "cachedResultUrl": "https://airtable.com/app662qLY5J8ys4fU",
          "cachedResultName": "customers"
        },
        "table": {
          "__rl": true,
          "mode": "list",
          "value": "tblwvA7Wrmvmv37rq",
          "cachedResultUrl": "https://airtable.com/app662qLY5J8ys4fU/tblwvA7Wrmvmv37rq",
          "cachedResultName": "Table 1"
        },
        "columns": {
          "value": {
            "email": "={{ $json.query.email }}",
            "phone": "={{ $json.query.phone }}",
            "address": "={{ $json.query.address }}",
            "last_name": "={{ $json.query.last_name }}",
            "first_name": "={{ $json.query.first_name }}",
            "customer_id": "={{ $json.query.customer_id }}"
          },
          "schema": [
            {
              "id": "customer_id",
              "type": "number",
              "display": true,
              "removed": false,
              "readOnly": false,
              "required": false,
              "displayName": "customer_id",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "first_name",
              "type": "string",
              "display": true,
              "removed": false,
              "readOnly": false,
              "required": false,
              "displayName": "first_name",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "last_name",
              "type": "string",
              "display": true,
              "removed": false,
              "readOnly": false,
              "required": false,
              "displayName": "last_name",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "email",
              "type": "string",
              "display": true,
              "removed": false,
              "readOnly": false,
              "required": false,
              "displayName": "email",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "phone",
              "type": "string",
              "display": true,
              "removed": false,
              "readOnly": false,
              "required": false,
              "displayName": "phone",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "address",
              "type": "string",
              "display": true,
              "removed": false,
              "readOnly": false,
              "required": false,
              "displayName": "address",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            }
          ],
          "mappingMode": "defineBelow",
          "matchingColumns": []
        },
        "options": {},
        "operation": "create"
      },
      "credentials": {
        "airtableTokenApi": {
          "id": "yX3WnQ0zNClN0JoN",
          "name": "Airtable giulio@n8n"
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "dceb7ad3-3c29-4cb9-b097-00c5ae1d2732",
      "name": "Get All",
      "type": "n8n-nodes-base.airtable",
      "position": [
        1000,
        600
      ],
      "parameters": {
        "base": {
          "__rl": true,
          "mode": "list",
          "value": "app662qLY5J8ys4fU",
          "cachedResultUrl": "https://airtable.com/app662qLY5J8ys4fU",
          "cachedResultName": "customers"
        },
        "table": {
          "__rl": true,
          "mode": "list",
          "value": "tblwvA7Wrmvmv37rq",
          "cachedResultUrl": "https://airtable.com/app662qLY5J8ys4fU/tblwvA7Wrmvmv37rq",
          "cachedResultName": "Table 1"
        },
        "options": {},
        "operation": "search"
      },
      "credentials": {
        "airtableTokenApi": {
          "id": "yX3WnQ0zNClN0JoN",
          "name": "Airtable giulio@n8n"
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "15a418ac-9de1-4c1d-ada7-057c280373df",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        940,
        522.9617575264442
      ],
      "parameters": {
        "color": 4,
        "width": 514,
        "height": 228.69080553295362,
        "content": "#### Get All\nRetrieves all records"
      },
      "typeVersion": 1
    },
    {
      "id": "9736394d-3298-485c-b907-19804bbd48fb",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        940,
        -260
      ],
      "parameters": {
        "color": 4,
        "width": 514,
        "height": 228,
        "content": "#### Get\nRetrieves a single record"
      },
      "typeVersion": 1
    },
    {
      "id": "b5544fc2-10cf-47dd-815c-51e8044e073d",
      "name": "Get Single",
      "type": "n8n-nodes-base.airtable",
      "position": [
        1000,
        -180
      ],
      "parameters": {
        "base": {
          "__rl": true,
          "mode": "list",
          "value": "app662qLY5J8ys4fU",
          "cachedResultUrl": "https://airtable.com/app662qLY5J8ys4fU",
          "cachedResultName": "customers"
        },
        "limit": 1,
        "table": {
          "__rl": true,
          "mode": "list",
          "value": "tblwvA7Wrmvmv37rq",
          "cachedResultUrl": "https://airtable.com/app662qLY5J8ys4fU/tblwvA7Wrmvmv37rq",
          "cachedResultName": "Table 1"
        },
        "options": {},
        "operation": "search",
        "returnAll": false,
        "filterByFormula": "=({customer_id} = {{ $json.params.id }})"
      },
      "credentials": {
        "airtableTokenApi": {
          "id": "yX3WnQ0zNClN0JoN",
          "name": "Airtable giulio@n8n"
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "0f08fcee-b892-47ec-b13c-639f7e5b4b91",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        940,
        260
      ],
      "parameters": {
        "color": 4,
        "width": 508.29454841334433,
        "height": 248.84784377542707,
        "content": "#### Update\nUpdates of an existing record"
      },
      "typeVersion": 1
    },
    {
      "id": "56ff1769-15fe-475d-96aa-9c0f1a9edf05",
      "name": "Airtable",
      "type": "n8n-nodes-base.airtable",
      "position": [
        1000,
        340
      ],
      "parameters": {
        "base": {
          "__rl": true,
          "mode": "list",
          "value": "app662qLY5J8ys4fU",
          "cachedResultUrl": "https://airtable.com/app662qLY5J8ys4fU",
          "cachedResultName": "customers"
        },
        "table": {
          "__rl": true,
          "mode": "list",
          "value": "tblwvA7Wrmvmv37rq",
          "cachedResultUrl": "https://airtable.com/app662qLY5J8ys4fU/tblwvA7Wrmvmv37rq",
          "cachedResultName": "Table 1"
        },
        "columns": {
          "value": {
            "email": "={{ $json.query.email }}",
            "phone": "={{ $json.query.phone }}",
            "address": "={{ $json.query.address }}",
            "last_name": "={{ $json.query.last_name }}",
            "first_name": "={{ $json.query.first_name }}",
            "customer_id": "={{ $json.query.customer_id }}"
          },
          "schema": [
            {
              "id": "id",
              "type": "string",
              "display": true,
              "removed": true,
              "readOnly": true,
              "required": false,
              "displayName": "id",
              "defaultMatch": true
            },
            {
              "id": "customer_id",
              "type": "number",
              "display": true,
              "removed": false,
              "readOnly": false,
              "required": false,
              "displayName": "customer_id",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "first_name",
              "type": "string",
              "display": true,
              "removed": false,
              "readOnly": false,
              "required": false,
              "displayName": "first_name",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "last_name",
              "type": "string",
              "display": true,
              "removed": false,
              "readOnly": false,
              "required": false,
              "displayName": "last_name",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "email",
              "type": "string",
              "display": true,
              "removed": false,
              "readOnly": false,
              "required": false,
              "displayName": "email",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "phone",
              "type": "string",
              "display": true,
              "removed": false,
              "readOnly": false,
              "required": false,
              "displayName": "phone",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "address",
              "type": "string",
              "display": true,
              "removed": false,
              "readOnly": false,
              "required": false,
              "displayName": "address",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            }
          ],
          "mappingMode": "defineBelow",
          "matchingColumns": [
            "customer_id"
          ]
        },
        "options": {},
        "operation": "update"
      },
      "credentials": {
        "airtableTokenApi": {
          "id": "yX3WnQ0zNClN0JoN",
          "name": "Airtable giulio@n8n"
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "e20c0448-9688-47ae-873b-7cc5ac6e826a",
      "name": "Respond to Webhook5",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        1420,
        80
      ],
      "parameters": {
        "options": {
          "responseCode": 200
        },
        "respondWith": "allIncomingItems"
      },
      "typeVersion": 1.1
    },
    {
      "id": "f13eb006-b576-4e65-9c04-7a8516dccb35",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        940,
        -20
      ],
      "parameters": {
        "color": 4,
        "width": 737.8307567127741,
        "height": 267.43205858421476,
        "content": "#### Delete\nDeletes a record"
      },
      "typeVersion": 1
    },
    {
      "id": "0f434e52-2fda-41c0-9f40-38bf1977b8a6",
      "name": "Airtable1",
      "type": "n8n-nodes-base.airtable",
      "position": [
        1200,
        80
      ],
      "parameters": {
        "id": "={{ $json.id }}",
        "base": {
          "__rl": true,
          "mode": "list",
          "value": "app662qLY5J8ys4fU",
          "cachedResultUrl": "https://airtable.com/app662qLY5J8ys4fU",
          "cachedResultName": "customers"
        },
        "table": {
          "__rl": true,
          "mode": "list",
          "value": "tblwvA7Wrmvmv37rq",
          "cachedResultUrl": "https://airtable.com/app662qLY5J8ys4fU/tblwvA7Wrmvmv37rq",
          "cachedResultName": "Table 1"
        },
        "operation": "deleteRecord"
      },
      "credentials": {
        "airtableTokenApi": {
          "id": "yX3WnQ0zNClN0JoN",
          "name": "Airtable giulio@n8n"
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "c58724ab-354b-43af-8a60-495837f8a4a2",
      "name": "Get Single1",
      "type": "n8n-nodes-base.airtable",
      "position": [
        1000,
        80
      ],
      "parameters": {
        "base": {
          "__rl": true,
          "mode": "list",
          "value": "app662qLY5J8ys4fU",
          "cachedResultUrl": "https://airtable.com/app662qLY5J8ys4fU",
          "cachedResultName": "customers"
        },
        "limit": 1,
        "table": {
          "__rl": true,
          "mode": "list",
          "value": "tblwvA7Wrmvmv37rq",
          "cachedResultUrl": "https://airtable.com/app662qLY5J8ys4fU/tblwvA7Wrmvmv37rq",
          "cachedResultName": "Table 1"
        },
        "options": {},
        "operation": "search",
        "returnAll": false,
        "filterByFormula": "=({customer_id} = {{ $json.params.id }})"
      },
      "credentials": {
        "airtableTokenApi": {
          "id": "yX3WnQ0zNClN0JoN",
          "name": "Airtable giulio@n8n"
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "1b8fc8af-4892-4804-85d0-8e84904a3cf0",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "position": [
        500,
        720
      ],
      "webhookId": "580ccc56-f308-4b64-961d-38323501a170",
      "parameters": {
        "path": "customers",
        "options": {},
        "responseMode": "responseNode",
        "multipleMethods": true
      },
      "typeVersion": 2
    },
    {
      "id": "7a8a9006-c2ea-4a87-8a94-fb925ed91abd",
      "name": "Webhook (with ID)",
      "type": "n8n-nodes-base.webhook",
      "position": [
        500,
        80
      ],
      "webhookId": "580ccc56-f308-4b64-961d-38323501a170",
      "parameters": {
        "path": "customers/:id",
        "options": {},
        "httpMethod": [
          "GET",
          "DELETE",
          "PUT"
        ],
        "responseMode": "responseNode",
        "multipleMethods": true
      },
      "typeVersion": 2
    }
  ],
  "active": true,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "b9009017-c9f6-4f8c-9592-350825e54476",
  "connections": {
    "Create": {
      "main": [
        [
          {
            "node": "Respond to Webhook1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get All": {
      "main": [
        [
          {
            "node": "Respond to Webhook4",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Webhook": {
      "main": [
        [
          {
            "node": "Get All",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Create",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Airtable": {
      "main": [
        [
          {
            "node": "Respond to Webhook2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Airtable1": {
      "main": [
        [
          {
            "node": "Respond to Webhook5",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Single": {
      "main": [
        [
          {
            "node": "Respond to Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Single1": {
      "main": [
        [
          {
            "node": "Airtable1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Webhook (with ID)": {
      "main": [
        [
          {
            "node": "Get Single",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Get Single1",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Airtable",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-1745"></a>

## Template 1745 - Registro automático de participantes

- **Nome:** Registro automático de participantes
- **Descrição:** Automatiza o processamento de inscrições: recebe respostas de formulário, registra em planilha, cria conta no chat, adiciona a equipes e canais, atualiza eventos de calendário e envia e-mail de boas-vindas.
- **Funcionalidade:** • Detecção de inscrições via formulário: inicia o fluxo ao receber uma nova submissão de inscrição.
• Registro dos dados em planilha: anexa os dados do participante na aba de Attendees de uma planilha.
• Criação de conta no chat: gera e cria uma conta de usuário com username e senha baseados nos dados fornecidos.
• Convite para a equipe do chat: convida o e-mail do participante para a equipe específica.
• Mapeamento de sessões selecionadas: converte a lista de sessões escolhidas em linhas individuais e busca detalhes das sessões.
• Adição a canais de sessão: adiciona o usuário aos canais correspondentes a cada sessão selecionada.
• Atualização de eventos do calendário: adiciona o participante como convidado aos eventos do Google Calendar relacionados às sessões.
• Envio de e-mail de boas-vindas: envia um e-mail contendo lista de sessões, credenciais de acesso ao chat e instruções úteis.
- **Ferramentas:** • Typeform: coleta as respostas do formulário de inscrição.
• Google Sheets: armazena os registros de participantes e os detalhes das sessões.
• Mattermost: plataforma de chat onde são criadas contas, enviadas convites e adicionados usuários a canais.
• Google Calendar: gerencia eventos das sessões e recebe a atualização de participantes.
• Gmail: envia o e-mail de confirmação e boas-vindas para o participante.

## Fluxo visual

```mermaid
flowchart LR
    N1["Attendee Registrations"]
    N2["Add to Sheets"]
    N3["Create Account"]
    N4["Add to team"]
    N5["Array to Rows"]
    N6["Get Session Details"]
    N7["Merge Data"]
    N8["Add to channels"]
    N9["Add to Event"]
    N10["Welcome Email"]

    N7 --> N8
    N4 --> N5
    N9 --> N10
    N2 --> N3
    N5 --> N7
    N3 --> N4
    N8 --> N9
    N6 --> N7
    N1 --> N2
```

## Fluxo (.json) :

```json
{
  "nodes": [
    {
      "name": "Attendee Registrations",
      "type": "n8n-nodes-base.typeformTrigger",
      "position": [
        400,
        300
      ],
      "webhookId": "6314f4db-12ca-4c5e-a6c5-062bb0437734",
      "parameters": {
        "formId": "RknoIFsl"
      },
      "credentials": {
        "typeformApi": "Typeform Burner Account"
      },
      "typeVersion": 1
    },
    {
      "name": "Add to Sheets",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        600,
        300
      ],
      "parameters": {
        "range": "Attendees!A:F",
        "options": {},
        "sheetId": "1nlnsTQKGgQZN-Rtd07K9bn0ROm0aFBC2O4kzM2YaTBI",
        "operation": "append",
        "authentication": "oAuth2"
      },
      "credentials": {
        "googleSheetsOAuth2Api": "google-sheets"
      },
      "typeVersion": 1
    },
    {
      "name": "Create Account",
      "type": "n8n-nodes-base.mattermost",
      "position": [
        800,
        300
      ],
      "parameters": {
        "email": "={{$json[\"And what's your email address?\"]}}",
        "password": "=P!_{{$json[\"And what's your email address?\"].split(\" \").join(\"\")}}-{{new Date().getHours()}}{{new Date().getDate()}}",
        "resource": "user",
        "username": "={{$json[\"Great, can we get your full name?\"].split(\" \").join(\"\")}}-{{new Date().getHours()}}",
        "operation": "create",
        "authService": "email",
        "additionalFields": {
          "first_name": "={{$json[\"Great, can we get your full name?\"]}}"
        }
      },
      "credentials": {
        "mattermostApi": "Mattermost Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Add to team",
      "type": "n8n-nodes-base.mattermost",
      "position": [
        1000,
        300
      ],
      "parameters": {
        "emails": "={{$node[\"Attendee Registrations\"].json[\"And what's your email address?\"]}}",
        "teamId": "ee3ddsn98i8d3xizkcttras5nw",
        "resource": "user",
        "operation": "invite"
      },
      "credentials": {
        "mattermostApi": "Mattermost Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Array to Rows",
      "type": "n8n-nodes-base.function",
      "position": [
        1200,
        300
      ],
      "parameters": {
        "functionCode": "const newItems = [];\nfor (let i=0;i<$node[\"Attendee Registrations\"].json[\"Which sessions would you like to attend?\"].length;i++) {\n\tnewItems.push({\n    \tjson: {\n        \tSession: $node[\"Attendee Registrations\"].json[\"Which sessions would you like to attend?\"][i]\n        }\n     });\n}\n\nreturn newItems;"
      },
      "typeVersion": 1
    },
    {
      "name": "Get Session Details",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        1200,
        500
      ],
      "parameters": {
        "range": "Sessions!A:F",
        "options": {},
        "sheetId": "1nlnsTQKGgQZN-Rtd07K9bn0ROm0aFBC2O4kzM2YaTBI",
        "authentication": "oAuth2"
      },
      "credentials": {
        "googleSheetsOAuth2Api": "google-sheets"
      },
      "typeVersion": 1
    },
    {
      "name": "Merge Data",
      "type": "n8n-nodes-base.merge",
      "position": [
        1376,
        422
      ],
      "parameters": {
        "mode": "mergeByKey",
        "propertyName1": "Session",
        "propertyName2": "Session"
      },
      "typeVersion": 1
    },
    {
      "name": "Add to channels",
      "type": "n8n-nodes-base.mattermost",
      "position": [
        1576,
        422
      ],
      "parameters": {
        "userId": "={{$node[\"Create Account\"].json[\"id\"]}}",
        "resource": "channel",
        "channelId": "={{$json[\"Mattermost Channel ID\"]}}",
        "operation": "addUser"
      },
      "credentials": {
        "mattermostApi": "Mattermost Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Add to Event",
      "type": "n8n-nodes-base.googleCalendar",
      "position": [
        1776,
        422
      ],
      "parameters": {
        "eventId": "={{$node[\"Merge Data\"].json[\"Google Calendar Event ID\"]}}",
        "calendar": "3ne32v2nlrrd2l3624v5qpg6qk@group.calendar.google.com",
        "operation": "update",
        "updateFields": {
          "attendees": [
            "={{$node[\"Attendee Registrations\"].json[\"And what's your email address?\"]}}"
          ]
        }
      },
      "credentials": {
        "googleCalendarOAuth2Api": "Google Calendar Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Welcome Email",
      "type": "n8n-nodes-base.gmail",
      "position": [
        1976,
        422
      ],
      "parameters": {
        "toList": [
          "={{$node[\"Attendee Registrations\"].json[\"And what's your email address?\"]}}"
        ],
        "message": "=Dear {{$node[\"Attendee Registrations\"].json[\"Great, can we get your full name?\"]}},\n\nWelcome to n8nConf, the world's largest no-code automation conference!\n\nThis email is to confirm your registration to the following sessions:\n- {{$node[\"Attendee Registrations\"].json[\"Which sessions would you like to attend?\"].join('\\n- ')}}\n\nYou should receive Google Calendar invites to these events on your email. Please consult those for the Google Meet joining information.\n\nYou can also interact with the rest of the community via our Mattermost chat. We created an account just for you!\nLook for the channel corresponding to your session to join the discussion!\n\nLogin URL: https://mm.failedmachine.com/\nUsername: {{$node[\"Create Account\"].json[\"username\"]}}\nPassword: {{$node[\"Create Account\"].parameter[\"password\"]}}\n\nRemember to change your password immediately after your first login!\n\nIf you have any troubles with joining the event, or using the chat rooms; please feel free to let us know on support@n8nconf.com\n\nWe look forward to your participation!\n\nBest,\nTeam n8n",
        "subject": "Welcome to n8nConf",
        "resource": "message",
        "additionalFields": {}
      },
      "credentials": {
        "gmailOAuth2": "gmail"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Merge Data": {
      "main": [
        [
          {
            "node": "Add to channels",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Add to team": {
      "main": [
        [
          {
            "node": "Array to Rows",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Add to Event": {
      "main": [
        [
          {
            "node": "Welcome Email",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Add to Sheets": {
      "main": [
        [
          {
            "node": "Create Account",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Array to Rows": {
      "main": [
        [
          {
            "node": "Merge Data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Create Account": {
      "main": [
        [
          {
            "node": "Add to team",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Add to channels": {
      "main": [
        [
          {
            "node": "Add to Event",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Session Details": {
      "main": [
        [
          {
            "node": "Merge Data",
            "type": "main",
            "index": 1
          }
        ]
      ]
    },
    "Attendee Registrations": {
      "main": [
        [
          {
            "node": "Add to Sheets",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
