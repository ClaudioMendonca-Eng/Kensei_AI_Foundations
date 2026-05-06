# PACK 1999 TEMPLATES PARTE 10 - Bloco 5

Templates neste bloco: 20

## Sumário

- [Template 2425 - Enviar posição da ISS a cada minuto para ActiveMQ](#template-2425)
- [Template 2427 - Publicação periódica da posição da ISS](#template-2427)
- [Template 2430 - Salvar link no Notion e responder no Discord](#template-2430)
- [Template 2433 - Rastreamento e confirmação de entregas por Telegram](#template-2433)
- [Template 2435 - Timer Pomodoro no Telegram](#template-2435)
- [Template 2436 - Analisar imagem e salvar rótulos no Google Sheets](#template-2436)
- [Template 2438 - Download de PDF via GET](#template-2438)
- [Template 2441 - Registro automático de refeições](#template-2441)
- [Template 2443 - Criar cartão no Nextcloud Deck a partir de e-mail](#template-2443)
- [Template 2445 - Criar/atualizar chamados no Syncro a partir de chamadas Dialpad](#template-2445)
- [Template 2448 - Integração Cloudflare KV (CRUD e operações em lote)](#template-2448)
- [Template 2450 - Geração automática de keywords](#template-2450)
- [Template 2451 - Notificação por email de nova release do GitHub](#template-2451)
- [Template 2453 - Assistente Telegram para transcrição e gestão de tarefas](#template-2453)
- [Template 2454 - Triagem automática de e-mails com IA](#template-2454)
- [Template 2456 - Responder e criar tickets/itens a partir de mensagens do Telegram](#template-2456)
- [Template 2458 - Enviar feeds RSS para Telegram](#template-2458)
- [Template 2461 - Gerar post e imagem a partir de mensagem Telegram](#template-2461)
- [Template 2462 - Enviar logs para BetterStack](#template-2462)
- [Template 2465 - Pesquisa Brave via Telegram](#template-2465)

---

<a id="template-2425"></a>

## Template 2425 - Enviar posição da ISS a cada minuto para ActiveMQ

- **Nome:** Enviar posição da ISS a cada minuto para ActiveMQ
- **Descrição:** Este fluxo obtém a posição atual da Estação Espacial Internacional a cada minuto e envia os dados para um tópico no broker ActiveMQ.
- **Funcionalidade:** • Agendamento periódico: Dispara a operação automaticamente a cada minuto.
• Consulta de posição da ISS: Requere à API pública para obter latitude, longitude, timestamp e nome da estação no momento atual.
• Extração e formatação de dados: Seleciona e organiza os campos Latitude, Longitude, Timestamp e Name para envio.
• Publicação via AMQP: Envia a mensagem formatada para o destino (tópico/queue) denominado "iss-postition" no broker.
• Uso de timestamp dinâmico: Utiliza o timestamp atual para solicitar a posição correspondente.
- **Ferramentas:** • WhereTheISS API: Serviço público que fornece a posição em tempo real da Estação Espacial Internacional.
• ActiveMQ (via AMQP): Broker de mensagens utilizado como destino para publicar as posições da ISS.



## Fluxo visual

```mermaid
flowchart LR
    N1["Cron"]
    N2["HTTP Request"]
    N3["Set"]
    N4["AMQP Sender"]

    N3 --> N4
    N1 --> N2
    N2 --> N3
```

## Fluxo (.json) :

```json
{
  "id": "102",
  "name": "Send updates about the position of the ISS every minute to a topic in ActiveMQ",
  "nodes": [
    {
      "name": "Cron",
      "type": "n8n-nodes-base.cron",
      "position": [
        510,
        300
      ],
      "parameters": {
        "triggerTimes": {
          "item": [
            {
              "mode": "everyMinute"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "HTTP Request",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        710,
        300
      ],
      "parameters": {
        "url": "https://api.wheretheiss.at/v1/satellites/25544/positions",
        "options": {},
        "queryParametersUi": {
          "parameter": [
            {
              "name": "timestamps",
              "value": "={{Date.now();}}"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Set",
      "type": "n8n-nodes-base.set",
      "position": [
        910,
        300
      ],
      "parameters": {
        "values": {
          "number": [
            {
              "name": "Latitude",
              "value": "={{$node[\"HTTP Request\"].json[\"0\"][\"latitude\"]}}"
            },
            {
              "name": "Longitude",
              "value": "={{$node[\"HTTP Request\"].json[\"0\"][\"longitude\"]}}"
            },
            {
              "name": "Timestamp",
              "value": "={{$node[\"HTTP Request\"].json[\"0\"][\"timestamp\"]}}"
            }
          ],
          "string": [
            {
              "name": "Name",
              "value": "={{$node[\"HTTP Request\"].json[\"0\"][\"name\"]}}"
            }
          ]
        },
        "options": {},
        "keepOnlySet": true
      },
      "typeVersion": 1
    },
    {
      "name": "AMQP Sender",
      "type": "n8n-nodes-base.amqp",
      "position": [
        1110,
        300
      ],
      "parameters": {
        "sink": "iss-postition",
        "options": {}
      },
      "credentials": {
        "amqp": "ampq"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "Set": {
      "main": [
        [
          {
            "node": "AMQP Sender",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Cron": {
      "main": [
        [
          {
            "node": "HTTP Request",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "HTTP Request": {
      "main": [
        [
          {
            "node": "Set",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2427"></a>

## Template 2427 - Publicação periódica da posição da ISS

- **Nome:** Publicação periódica da posição da ISS
- **Descrição:** Coleta a posição atual da Estação Espacial Internacional e publica os dados em um broker MQTT a cada minuto.
- **Funcionalidade:** • Agendamento por minuto: inicia o fluxo uma vez a cada minuto.
• Consulta de posição da ISS: solicita a posição atual da Estação Espacial Internacional ao endpoint https://api.wheretheiss.at utilizando o timestamp atual.
• Extração de campos relevantes: formata e mantém somente nome, latitude, longitude e timestamp.
• Publicação via MQTT: envia a posição formatada para o tópico 'iss-position' no broker MQTT.
- **Ferramentas:** • WhereTheISS API: serviço público que fornece posições e dados da Estação Espacial Internacional.
• Broker MQTT: serviço de mensagens que recebe publicações no tópico 'iss-position' para distribuição a assinantes.



## Fluxo visual

```mermaid
flowchart LR
    N1["Cron"]
    N2["HTTP Request"]
    N3["Set"]
    N4["MQTT"]

    N3 --> N4
    N1 --> N2
    N2 --> N3
```

## Fluxo (.json) :

```json
{
  "nodes": [
    {
      "name": "Cron",
      "type": "n8n-nodes-base.cron",
      "position": [
        490,
        360
      ],
      "parameters": {
        "triggerTimes": {
          "item": [
            {
              "mode": "everyMinute"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "HTTP Request",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        690,
        360
      ],
      "parameters": {
        "url": "https://api.wheretheiss.at/v1/satellites/25544/positions",
        "options": {},
        "queryParametersUi": {
          "parameter": [
            {
              "name": "timestamps",
              "value": "={{Date.now()}}"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Set",
      "type": "n8n-nodes-base.set",
      "position": [
        890,
        360
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "Name",
              "value": "={{$json[\"0\"][\"name\"]}}"
            },
            {
              "name": "Latitude",
              "value": "={{$json[\"0\"][\"latitude\"]}}"
            },
            {
              "name": "Longitude",
              "value": "={{$json[\"0\"][\"longitude\"]}}"
            },
            {
              "name": "Timestamp",
              "value": "={{$json[\"0\"][\"timestamp\"]}}"
            }
          ]
        },
        "options": {},
        "keepOnlySet": true
      },
      "typeVersion": 1
    },
    {
      "name": "MQTT",
      "type": "n8n-nodes-base.mqtt",
      "position": [
        1090,
        360
      ],
      "parameters": {
        "topic": "iss-position",
        "options": {}
      },
      "credentials": {
        "mqtt": "mqtt"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Set": {
      "main": [
        [
          {
            "node": "MQTT",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Cron": {
      "main": [
        [
          {
            "node": "HTTP Request",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "HTTP Request": {
      "main": [
        [
          {
            "node": "Set",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2430"></a>

## Template 2430 - Salvar link no Notion e responder no Discord

- **Nome:** Salvar link no Notion e responder no Discord
- **Descrição:** Recebe um webhook do Discord, verifica o tipo de evento, e quando contém um link busca o título da página, cria uma entrada no Notion com título e URL e envia confirmação de volta ao Discord.
- **Funcionalidade:** • Receber eventos via webhook: Ouve requisições POST com o payload recebido do Discord.
• Verificar tipo de evento: Analisa o campo de tipo no payload para decidir o fluxo de processamento.
• Registrar URL/ping: Para eventos do tipo específico (type = 1) retorna/register uma resposta simples sem processar o link.
• Buscar conteúdo da URL: Faz uma requisição HTTP para obter o HTML da URL enviada no payload.
• Extrair título da página: Extrai a tag <title> do HTML para usar como nome da entrada.
• Criar página no Notion: Insere uma nova página em uma base do Notion com o título extraído e a URL original.
• Responder no Discord: Envia uma mensagem de confirmação informando que o link foi adicionado ao Notion.
- **Ferramentas:** • Discord: Origem dos eventos via webhook/interação e destino das respostas de confirmação.
• Notion: Armazena as páginas criadas com título e URL na base de dados.
• Requisições HTTP a websites: Recupera o conteúdo HTML das URLs fornecidas para extração do título.

## Fluxo visual

```mermaid
flowchart LR
    N1["Webhook"]
    N2["HTTP Request"]
    N3["Check type"]
    N4["Extract Title"]
    N5["Add Link to Notion"]
    N6["Reply on Discord"]
    N7["Register URL"]

    N1 --> N3
    N3 --> N2
    N3 --> N7
    N2 --> N4
    N4 --> N5
    N5 --> N6
```

## Fluxo (.json) :

```json
{
  "nodes": [
    {
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "position": [
        450,
        300
      ],
      "webhookId": "45e2593e-f25d-4be5-9b50-4a7c1e566a9e",
      "parameters": {
        "path": "45e2593e-f25d-4be5-9b50-4a7c1e566a9e",
        "options": {},
        "httpMethod": "POST",
        "responseMode": "lastNode"
      },
      "typeVersion": 1
    },
    {
      "name": "HTTP Request",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        850,
        200
      ],
      "parameters": {
        "url": "=https://{{$json[\"body\"][\"data\"][\"options\"][0][\"value\"]}}",
        "options": {},
        "responseFormat": "string"
      },
      "typeVersion": 1
    },
    {
      "name": "Check type",
      "type": "n8n-nodes-base.if",
      "position": [
        650,
        300
      ],
      "parameters": {
        "conditions": {
          "number": [
            {
              "value1": "={{$json[\"body\"][\"type\"]}}",
              "value2": 1,
              "operation": "notEqual"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Extract Title",
      "type": "n8n-nodes-base.htmlExtract",
      "position": [
        1050,
        200
      ],
      "parameters": {
        "options": {},
        "extractionValues": {
          "values": [
            {
              "key": "title",
              "cssSelector": "title"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Add Link to Notion",
      "type": "n8n-nodes-base.notion",
      "position": [
        1250,
        200
      ],
      "parameters": {
        "resource": "databasePage",
        "databaseId": "8a1638ce-da33-41b7-8fd9-37a4c272ba95",
        "propertiesUi": {
          "propertyValues": [
            {
              "key": "Name|title",
              "title": "={{$json[\"title\"]}}"
            },
            {
              "key": "Link|url",
              "urlValue": "={{$node[\"Check type\"].json[\"body\"][\"data\"][\"options\"][0][\"value\"]}}"
            }
          ]
        }
      },
      "credentials": {
        "notionApi": "Notion API Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Reply on Discord",
      "type": "n8n-nodes-base.set",
      "position": [
        1450,
        200
      ],
      "parameters": {
        "values": {
          "number": [
            {
              "name": "type",
              "value": 4
            }
          ],
          "string": [
            {
              "name": "data.content",
              "value": "Added Link to notion"
            }
          ]
        },
        "options": {},
        "keepOnlySet": true
      },
      "typeVersion": 1
    },
    {
      "name": "Register URL",
      "type": "n8n-nodes-base.set",
      "position": [
        850,
        410
      ],
      "parameters": {
        "values": {
          "number": [
            {
              "name": "type",
              "value": 1
            }
          ],
          "string": []
        },
        "options": {},
        "keepOnlySet": true
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Check type",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Check type": {
      "main": [
        [
          {
            "node": "HTTP Request",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Register URL",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "HTTP Request": {
      "main": [
        [
          {
            "node": "Extract Title",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract Title": {
      "main": [
        [
          {
            "node": "Add Link to Notion",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Add Link to Notion": {
      "main": [
        [
          {
            "node": "Reply on Discord",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2433"></a>

## Template 2433 - Rastreamento e confirmação de entregas por Telegram

- **Nome:** Rastreamento e confirmação de entregas por Telegram
- **Descrição:** Fluxo que guia entregadores via Telegram para registrar número de entrega, localização e foto, armazena os dados, gera link público da imagem e envia confirmação por email à equipe logística.
- **Funcionalidade:** • Recepção de mensagens via bot Telegram: Inicia o fluxo quando o entregador envia mensagens ou comandos.
• Roteamento por comando: Identifica comandos como /addShipment, /addGPS, /sendPhoto e /sendConfirmation para direcionar o processo.
• Coleta de número de entrega: Solicita e armazena o número do pedido informado pelo entregador.
• Coleta de localização GPS: Solicita o envio da localização e registra latitude/longitude.
• Solicitação e upload de foto do envio: Pede ao entregador que envie uma foto, baixa o arquivo e envia para armazenamento.
• Armazenamento do arquivo e criação de link público: Faz upload da imagem para armazenamento em nuvem e gera link público para visualização.
• Registro em planilha: Anexa os dados da entrega (número, GPS, link da imagem, horário) em uma planilha para histórico.
• Notificação ao entregador: Envia um resumo com detalhes da entrega e link da imagem no chat do entregador.
• Envio de confirmação por email à equipe de distribuição: Envia email com foto incorporada, horário e coordenadas para a equipe logística.
• Gerenciamento de estado por conversação: Mantém flags por chat para saber qual informação está sendo aguardada e limpa o estado ao finalizar.
- **Ferramentas:** • Telegram (Bot): Canal de interação com os entregadores para receber comandos, localização e fotos, e enviar mensagens de confirmação.
• Google Drive: Armazenamento das imagens enviadas e geração de link público para visualização das fotos.
• Google Sheets: Registro em planilha dos dados de entrega para histórico e acompanhamento.
• Gmail: Envio de email com confirmação de entrega e inclusão da foto para a equipe logística.

## Fluxo visual

```mermaid
flowchart LR
    N1["Sticky Note3"]
    N2["Telegram Trigger"]
    N3["Check State"]
    N4["Clear State"]
    N5["Sticky Note5"]
    N6["Sticky Note6"]
    N7["addGPS"]
    N8["Welcome Message"]
    N9["Command?"]
    N10["Store GPS Location"]
    N11["addGPS result"]
    N12["addShipmentNumber"]
    N13["Shipment Number"]
    N14["addShipmentNumber result"]
    N15["Store Shipment"]
    N16["Store GPS"]
    N17["Load Workspace Data"]
    N18["waitingShipmentNumber"]
    N19["waitingGPS"]
    N20["Instructions"]
    N21["waitingPhoto"]
    N22["Waiting Conditions"]
    N23["addPhoto result"]
    N24["sendPhoto"]
    N25["Upload Picture"]
    N26["Save Public Image Link"]
    N27["Confirmation Driver"]
    N28["Distribution Team Confirmation"]
    N29["Extract FileName"]
    N30["Store fileName"]
    N31["Get Picture"]
    N32["Share Picture"]
    N33["Initiate Workflow Data"]
    N34["Sticky Note"]
    N35["Switch Command"]
    N36["Sticky Note1"]
    N37["Load Delivery Information"]

    N9 --> N35
    N9 --> N22
    N19 --> N7
    N3 --> N13
    N3 --> N10
    N3 --> N31
    N3 --> N20
    N31 --> N25
    N31 --> N29
    N21 --> N24
    N32 --> N26
    N35 --> N18
    N35 --> N19
    N35 --> N21
    N35 --> N17
    N35 --> N8
    N25 --> N32
    N13 --> N14
    N13 --> N15
    N29 --> N30
    N2 --> N9
    N10 --> N11
    N10 --> N16
    N22 --> N3
    N17 --> N37
    N17 --> N27
    N17 --> N28
    N18 --> N12
    N26 --> N23
    N28 --> N4
```

## Fluxo (.json) :

```json
{
  "meta": {
    "instanceId": "6a5e68bcca67c4cdb3e0b698d01739aea084e1ec06e551db64aeff43d174cb23",
    "templateCredsSetupCompleted": true
  },
  "nodes": [
    {
      "id": "bc49829b-45f2-4910-9c37-907271982f14",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -3200,
        660
      ],
      "parameters": {
        "width": 780,
        "height": 540,
        "content": "### 5. Do you need more details?\nFind a step-by-step guide in this tutorial\n![Guide](https://www.samirsaci.com/content/images/2025/04/Telegram-Shipment-Tracking.png)\n[🎥 Watch My Tutorial](https://youtu.be/9NS4RYaOwJ8)"
      },
      "typeVersion": 1
    },
    {
      "id": "91269b35-1dbc-46bd-b8b4-85227d324e6d",
      "name": "Telegram Trigger",
      "type": "n8n-nodes-base.telegramTrigger",
      "position": [
        -3020,
        220
      ],
      "webhookId": "97a26e94-6de8-4d44-9cda-631ad869119d",
      "parameters": {
        "updates": [
          "message"
        ],
        "additionalFields": {}
      },
      "notesInFlow": true,
      "typeVersion": 1
    },
    {
      "id": "5752611d-97b5-4d5b-b40d-a0ae05d7bd71",
      "name": "Check State",
      "type": "n8n-nodes-base.switch",
      "position": [
        -2600,
        1480
      ],
      "parameters": {
        "rules": {
          "values": [
            {
              "outputKey": "1",
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
                    "id": "f5b2d141-7bd2-4656-b9c7-d2b562b2406e",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $json.state }}",
                    "rightValue": "waitingShipmentNumber"
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "2",
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
                    "id": "1a145782-de66-496c-aa5e-5fa5b93614f9",
                    "operator": {
                      "name": "filter.operator.equals",
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $json.state }}",
                    "rightValue": "waitingGPS"
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "3",
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
                    "id": "22f4f461-5973-4cba-9341-e077dd7b3fa1",
                    "operator": {
                      "name": "filter.operator.equals",
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $json.state }}",
                    "rightValue": "waitingPhoto"
                  }
                ]
              },
              "renameOutput": true
            }
          ]
        },
        "options": {
          "fallbackOutput": "extra"
        }
      },
      "notesInFlow": true,
      "typeVersion": 3.2
    },
    {
      "id": "7fa4e34e-562e-43de-b61e-d5827fcc51fb",
      "name": "Clear State",
      "type": "n8n-nodes-base.code",
      "position": [
        -1620,
        620
      ],
      "parameters": {
        "jsCode": "let workflowStaticData = $getWorkflowStaticData('global');\nif (workflowStaticData.telegramStates) {\n    delete workflowStaticData.telegramStates[$('Telegram Trigger').first().json.message.chat.id.toString()];\n}\n\nreturn $input.all();"
      },
      "typeVersion": 2
    },
    {
      "id": "46db0fda-bf2e-4c26-b1dc-305a4bb23ecc",
      "name": "Sticky Note5",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -2360,
        980
      ],
      "parameters": {
        "color": 7,
        "width": 1013,
        "height": 1189,
        "content": "\n### 3. Driver's Input Collection Block\nBased on the state flag value, the workflow process the input expected from the driver.\n\nThe **waiting conditions** code node is filtering the request based on the workplace state variable value\n- **If the value is waitingXXX**: the output from the driver is processed, a value is recorded in a code node and a confirmation message is sent to the driver (including the next command to follow)\n- **If the value does not start with waiting**: a message with instructions is sent to the driver\n\n#### How to setup?\n- **Telegram Message Nodes:** set up your telegram bot credentials\n[Learn more about the Telegram Message Node](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/)\n- **Google Drive Nodes**:\n   1. Add your Google Drive API credentials to access your drive\n   2. Select the folder using the list, an URL or an ID\n   3. Select the sheet in which the vocabulary list is stored\n  [Learn more about the Google Drive Node](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/?utm_source=n8n_app&utm_medium=node_settings_modal-credential_link&utm_campaign=n8n-nodes-base.googleDrive)"
      },
      "typeVersion": 1
    },
    {
      "id": "27cd5591-e014-4b35-9462-a297c12f9957",
      "name": "Sticky Note6",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -2360,
        -300
      ],
      "parameters": {
        "color": 7,
        "width": 993,
        "height": 1149,
        "content": "### 2. Driver's Input Command Block\nThe switch command tunnels the flow based on the command:\n  1. The code nodes named waitingXXX are storing a state flag to wait for the user input\n  2. Telegram Message Nodes are asking users for the expected input\n\nIf the command is **/sendConfirmation**:\n- A proof of delivery is sent to the logistics team by the Gmail Node\n- Shipment information are recorded in the Google Sheet\n- A confirmation is sent to the driver by the Telegram Node\n\n#### How to setup?\n- **Telegram Message Nodes:** set up your telegram bot credentials\n[Learn more about the Telegram Message Node](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/)\n- **Send Email with Gmail Node**: set up the node to send the confirmation to the delivery team\n[Learn more about the Gmail Email Node](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail)\n  1. Add the email of the recipient **To**\n  2. Add your Gmail API credentials\n  3. Change the **Send Name**\n\n"
      },
      "typeVersion": 1
    },
    {
      "id": "95db3b8c-6ca8-4a47-8c2b-8dd8e29a1ac6",
      "name": "addGPS",
      "type": "n8n-nodes-base.telegram",
      "position": [
        -2060,
        280
      ],
      "webhookId": "f50b0e4e-8a6b-4af8-bdb3-becec1f6ccaf",
      "parameters": {
        "text": "=📍 Please share your GPS location by clicking the 📎 attachment button.",
        "chatId": "={{ $json.message.chat.id }}",
        "forceReply": {
          "force_reply": true
        },
        "replyMarkup": "forceReply",
        "additionalFields": {
          "appendAttribution": false
        }
      },
      "notesInFlow": true,
      "typeVersion": 1.2
    },
    {
      "id": "8594469e-2456-45f3-be5c-db8d56fc1f58",
      "name": "Welcome Message",
      "type": "n8n-nodes-base.telegram",
      "position": [
        -2320,
        700
      ],
      "webhookId": "5c54b2fa-f6ef-44ea-90db-af1822586d0f",
      "parameters": {
        "text": "=Hello {{ $json.message.chat.first_name }}! 👋  \nI am **LogiGreenTrack**, your delivery tracking assistant. 🚛📦  \n\nYou can use the following commands:  \n\n🚚 /addShipment - Start a new shipment tracking process.\nℹ️ /help - Get more information about how to use LogiTrack.\n\nWhen you start a new shipment, I will guide you through these simple steps:  \n1️⃣ Provide the **delivery number**. \n2️⃣ Share your **GPS location**.   \n3️⃣ Upload a **picture** of the shipment.  \n\nYour data will be stored safely in our system for tracking. ✅  \n\nType a command to get started! 🚀",
        "chatId": "={{ $json.message.chat.id }}",
        "additionalFields": {
          "appendAttribution": false
        }
      },
      "notesInFlow": true,
      "typeVersion": 1.2
    },
    {
      "id": "1e18abec-0328-4556-b947-c91afc2a1425",
      "name": "Command?",
      "type": "n8n-nodes-base.if",
      "position": [
        -2820,
        220
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
              "id": "70ac1322-2ef4-46b4-9090-7c3c93bf546f",
              "operator": {
                "type": "object",
                "operation": "exists",
                "singleValue": true
              },
              "leftValue": "={{ $json.message.entities[0] }}",
              "rightValue": "/start"
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "8b7c62eb-cee6-46fb-8591-f2b8c66fe360",
      "name": "Store GPS Location",
      "type": "n8n-nodes-base.set",
      "position": [
        -2320,
        1660
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "03403259-8673-4a0b-b238-da2d4f311e59",
              "name": "latitude",
              "type": "string",
              "value": "={{ $('Telegram Trigger').item.json.message.location.latitude }}"
            },
            {
              "id": "762d4db4-f4d0-414e-9937-d4e7ea36fab7",
              "name": "longitude",
              "type": "string",
              "value": "={{ $('Telegram Trigger').item.json.message.location.longitude }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "994e6cda-3ae4-4190-9b28-4fdc48b64330",
      "name": "addGPS result",
      "type": "n8n-nodes-base.telegram",
      "position": [
        -1980,
        1660
      ],
      "webhookId": "2a31bd25-91a1-449f-b018-b88eabaa4daf",
      "parameters": {
        "text": "=Record GPS Coordinates: [{\"latitude\": {{ $json.latitude }}, \"longitude\": {{ $json.longitude }}}].  \nPlease continue with 📸 /sendPhoto to upload a picture of the shipment.",
        "chatId": "={{ $('Telegram Trigger').first().json.message.chat.id }}",
        "additionalFields": {
          "appendAttribution": false
        }
      },
      "notesInFlow": true,
      "typeVersion": 1
    },
    {
      "id": "fd8c2f32-205d-4f41-a5cf-fa7fb6cc6257",
      "name": "addShipmentNumber",
      "type": "n8n-nodes-base.telegram",
      "position": [
        -2060,
        140
      ],
      "webhookId": "fb230af6-f0e6-4e0b-bcf6-72a0b82e4322",
      "parameters": {
        "text": "📦 Please enter the delivery number for this shipment.",
        "chatId": "={{ $('Telegram Trigger').item.json.message.chat.id }}",
        "forceReply": {
          "force_reply": true
        },
        "replyMarkup": "forceReply",
        "additionalFields": {
          "appendAttribution": false
        }
      },
      "notesInFlow": true,
      "typeVersion": 1.2
    },
    {
      "id": "849b1cd3-2115-4f52-9705-dcf4c3ad0492",
      "name": "Shipment Number",
      "type": "n8n-nodes-base.set",
      "position": [
        -2340,
        1460
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "aa417d79-9da9-48e1-ab32-df034db44a1c",
              "name": "shipmentNumber",
              "type": "string",
              "value": "={{ $('Command?').item.json.message.text }}"
            }
          ]
        }
      },
      "notesInFlow": true,
      "typeVersion": 3.4
    },
    {
      "id": "ef960bb8-e6d8-47f6-9b20-7bcaed46dc13",
      "name": "addShipmentNumber result",
      "type": "n8n-nodes-base.telegram",
      "position": [
        -1980,
        1460
      ],
      "webhookId": "2f97d0e7-315e-4a65-ba9a-171f35d51e27",
      "parameters": {
        "text": "=Recorded Shipment Number: {{ $json.shipmentNumber }}. \nNext step:📍 /addGPS - Add your GPS location",
        "chatId": "={{ $('Telegram Trigger').first().json.message.chat.id }}",
        "additionalFields": {
          "appendAttribution": false
        }
      },
      "notesInFlow": true,
      "typeVersion": 1
    },
    {
      "id": "a6d95daf-a1e7-48e5-905c-5fe0c40cacc6",
      "name": "Store Shipment",
      "type": "n8n-nodes-base.code",
      "position": [
        -2160,
        1360
      ],
      "parameters": {
        "jsCode": "let workflowData = $getWorkflowStaticData('global');\nworkflowData.shipmentNumber = $input.first().json.shipmentNumber;\nreturn $json;"
      },
      "typeVersion": 2
    },
    {
      "id": "8da873e9-08e2-4d6c-a0ae-a7cdbd657dbc",
      "name": "Store GPS",
      "type": "n8n-nodes-base.code",
      "position": [
        -2160,
        1560
      ],
      "parameters": {
        "jsCode": "let workflowData = $getWorkflowStaticData('global');\nworkflowData.gpsLatitude = $input.first().json.latitude\nworkflowData.gpsLongitude = $input.first().json.longitude\nreturn $json;"
      },
      "typeVersion": 2
    },
    {
      "id": "f3e06841-9870-4179-a65b-22d3d94348fe",
      "name": "Load Workspace Data",
      "type": "n8n-nodes-base.code",
      "position": [
        -2320,
        560
      ],
      "parameters": {
        "jsCode": "let workflowData = $getWorkflowStaticData('global');\n\nreturn [\n    {\n        json: {\n            shipmentNumber: workflowData.shipmentNumber || \"Not available\",\n            gpsLatitude: workflowData.gpsLatitude || \"Not available\",\n            gpsLongitude: workflowData.gpsLongitude || \"Not available\",\n            publicImageLink: workflowData.publicImageLink || \"Not available\",\n            deliveryTime: workflowData.deliveryTime || \"Not available\",\n            fileName: workflowData.fileName || \"Not available\"\n        }\n    }\n];"
      },
      "typeVersion": 2
    },
    {
      "id": "d439fa72-1f6e-40c6-86cb-d083954d8c59",
      "name": "waitingShipmentNumber",
      "type": "n8n-nodes-base.code",
      "position": [
        -2320,
        140
      ],
      "parameters": {
        "jsCode": "let workflowStaticData = $getWorkflowStaticData('global');\nif (!workflowStaticData.telegramStates) {\n    workflowStaticData.telegramStates = {};\n}\nworkflowStaticData.telegramStates[$json.message.chat.id.toString()] = { waitingShipmentNumber: true };\nreturn $input.all();"
      },
      "typeVersion": 2
    },
    {
      "id": "378c50b5-eff8-4cb3-89d8-3ed823bf3b52",
      "name": "waitingGPS",
      "type": "n8n-nodes-base.code",
      "position": [
        -2320,
        280
      ],
      "parameters": {
        "jsCode": "let workflowStaticData = $getWorkflowStaticData('global');\nif (!workflowStaticData.telegramStates) {\n    workflowStaticData.telegramStates = {};\n}\nworkflowStaticData.telegramStates[$json.message.chat.id.toString()] = { waitingGPS: true };\nreturn $input.all();"
      },
      "typeVersion": 2
    },
    {
      "id": "8e3b46c6-6cb6-4d0d-b118-d777c2a8a728",
      "name": "Instructions",
      "type": "n8n-nodes-base.telegram",
      "position": [
        -2320,
        2000
      ],
      "webhookId": "53fbb69e-8271-4e59-bcbc-deccb79c47a8",
      "parameters": {
        "text": "=Hello {{ $json.message.chat.first_name }}! 👋  \nI am **LogiGreenTrack**, your delivery tracking assistant. 🚛📦  \n\nYou can use the following commands:  \n\n🚚 /addShipment - Start a new shipment tracking process.\nℹ️ /help - Get more information about how to use LogiTrack.\n\nWhen you start a new shipment, I will guide you through these simple steps:  \n1️⃣ Provide the **delivery number**. \n2️⃣ Share your **GPS location**.   \n3️⃣ Upload a **picture** of the shipment.  \n\nYour data will be stored safely in our system for tracking. ✅  \n\nType a command to get started! 🚀",
        "chatId": "={{ $('Telegram Trigger').first().json.message.chat.id }}",
        "additionalFields": {
          "appendAttribution": false
        }
      },
      "notesInFlow": true,
      "typeVersion": 1
    },
    {
      "id": "7e448986-d88e-413e-a174-6ef477f0de39",
      "name": "waitingPhoto",
      "type": "n8n-nodes-base.code",
      "position": [
        -2320,
        420
      ],
      "parameters": {
        "jsCode": "let workflowStaticData = $getWorkflowStaticData('global');\nif (!workflowStaticData.telegramStates) {\n    workflowStaticData.telegramStates = {};\n}\nworkflowStaticData.telegramStates[$json.message.chat.id.toString()] = { waitingPhoto: true };\nreturn $input.all();"
      },
      "typeVersion": 2
    },
    {
      "id": "112db445-fa9b-41ca-ae58-3cff7abc92d5",
      "name": "Waiting Conditions",
      "type": "n8n-nodes-base.code",
      "position": [
        -2800,
        1500
      ],
      "parameters": {
        "jsCode": "let globalData = $getWorkflowStaticData('global');\nlet state = \"none\"; // Default state\n\nif (globalData && globalData.telegramStates) {\n    let chatData = globalData.telegramStates[$json.message.chat.id.toString()];\n    if (chatData) {\n        if (chatData.waitingShipmentNumber === true) {\n            state = \"waitingShipmentNumber\";\n        } else if (chatData.waitingGPS === true) {\n            state = \"waitingGPS\";\n        } else if (chatData.waitingPhoto === true) {\n            state = \"waitingPhoto\";\n        }\n    }\n}\nreturn { state };"
      },
      "typeVersion": 2
    },
    {
      "id": "0176a1ee-414a-4df4-8859-3a3175549107",
      "name": "addPhoto result",
      "type": "n8n-nodes-base.telegram",
      "position": [
        -1600,
        1840
      ],
      "webhookId": "4f77a501-82b8-4046-8ac4-027c0874a7ae",
      "parameters": {
        "text": "=Photo saved in a file named using shipment number. \nPlease continue with 📩 /sendConfirmation to send a proof of delivery via email to the logistics team.\n",
        "chatId": "={{ $('Telegram Trigger').first().json.message.chat.id }}",
        "additionalFields": {
          "parse_mode": "HTML",
          "appendAttribution": false
        }
      },
      "notesInFlow": true,
      "typeVersion": 1
    },
    {
      "id": "7e1d37bc-a3ba-45fb-a8d1-59090f786036",
      "name": "sendPhoto",
      "type": "n8n-nodes-base.telegram",
      "position": [
        -2060,
        420
      ],
      "webhookId": "aef2449a-c6bf-4956-a986-dce76deae089",
      "parameters": {
        "text": "=Please take a **photo of the shipment** and upload it here by clicking the 📎 attachment button.",
        "chatId": "={{ $json.message.chat.id }}",
        "forceReply": {
          "force_reply": true
        },
        "replyMarkup": "forceReply",
        "additionalFields": {
          "appendAttribution": false
        }
      },
      "notesInFlow": true,
      "typeVersion": 1.2
    },
    {
      "id": "5dfae752-581a-4835-9815-521f371539a4",
      "name": "Upload Picture",
      "type": "n8n-nodes-base.googleDrive",
      "position": [
        -2140,
        1840
      ],
      "parameters": {
        "name": "=",
        "driveId": {
          "__rl": true,
          "mode": "list",
          "value": "My Drive",
          "cachedResultUrl": "https://drive.google.com/drive/my-drive",
          "cachedResultName": "My Drive"
        },
        "options": {},
        "folderId": {
          "__rl": true,
          "mode": "url",
          "value": "https://drive.google.com/drive/folders/<FILE_ID>"
        }
      },
      "typeVersion": 3
    },
    {
      "id": "887f2571-c80d-43ba-b838-32fea8f3315f",
      "name": "Save Public Image Link",
      "type": "n8n-nodes-base.code",
      "position": [
        -1780,
        1840
      ],
      "parameters": {
        "jsCode": "let workflowData = $getWorkflowStaticData('global');\n\n// Extract the file link from Google Drive node\nlet fileLink = $('Upload Picture').first().json.webContentLink || \"No link available\";\nlet fileId = $('Upload Picture').first().json.id || \"No ID available\";\n// Public Link\nlet publicImageLink = `https://drive.google.com/uc?export=view&id=${fileId}`;\nlet deliveryTime = $now\n\n// Store the link in static data\nworkflowData.fileLink = fileLink;\nworkflowData.publicImageLink = publicImageLink;\nworkflowData.deliveryTime = deliveryTime\nreturn {\n    fileLink: fileLink,\n    publicImageLink: publicImageLink,\n    deliveryTime: deliveryTime\n};"
      },
      "typeVersion": 2
    },
    {
      "id": "5b147f24-f2ed-45ad-a147-2490938232aa",
      "name": "Confirmation Driver",
      "type": "n8n-nodes-base.telegram",
      "position": [
        -2060,
        700
      ],
      "webhookId": "012fbfba-9133-4446-b4cd-bbce5b7064f5",
      "parameters": {
        "text": "=<b>📦 Shipment Details</b>\n\n<b>Shipment Number:</b> {{ $json.shipmentNumber }}\n\n<b>📍 Location:</b>  \nLat: <code>{{ $json.gpsLatitude }}</code>  \nLong: <code>{{ $json.gpsLongitude }}</code>  \n\n🖼️ <b>Shipment Photo:</b>  \n<a href=\"{{ $json.fileLink }}\">📷 View Image</a>",
        "chatId": "={{ $('Telegram Trigger').item.json.message.chat.id }}",
        "additionalFields": {
          "parse_mode": "HTML",
          "appendAttribution": false
        }
      },
      "notesInFlow": true,
      "typeVersion": 1.2
    },
    {
      "id": "d5adfbeb-cbdb-461f-9709-6458a29e8fb8",
      "name": "Distribution Team Confirmation",
      "type": "n8n-nodes-base.gmail",
      "position": [
        -1800,
        620
      ],
      "webhookId": "85e72ad7-effa-4445-911b-90e5f13efa41",
      "parameters": {
        "sendTo": "logigreenbot@logistics.com",
        "message": "=<h2>📦 Delivery Confirmation</h2>\n\n<p><b>Shipment Number:</b> {{ $json.shipmentNumber }}</p>\n\n<p>📍 <b>Delivery Location:</b><br>\nLat: <code>{{ $json.gpsLatitude }}</code><br>\nLong: <code>{{ $json.gpsLongitude }}</code>\n</p>\n\n<p>⏳ <b>Delivery Time:</b> {{ $json.deliveryTime }}</p>\n\n<p>🖼️ <b>Shipment Photo:</b><br>\n<img src=\"{{ $json.publicImageLink }}\" width=\"400\">\n</p>\n\n<p>✅ This shipment has been successfully delivered by {{ $('Switch Command').item.json.message.chat.first_name }} (Driver ID: {{ $('Switch Command').item.json.message.chat.username }}).</p>\n",
        "options": {
          "senderName": "LogiGreenTrack Solution",
          "appendAttribution": false
        },
        "subject": "=Delivery Confirmation: {{ $json.shipmentNumber }}"
      },
      "notesInFlow": true,
      "typeVersion": 2.1
    },
    {
      "id": "963417b3-7e35-43dc-b303-c7445333aa5b",
      "name": "Extract FileName",
      "type": "n8n-nodes-base.set",
      "position": [
        -2100,
        2020
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "ebee599b-f2d8-4b64-b8a5-eac8bdd698bb",
              "name": "fileName",
              "type": "string",
              "value": "={{ $binary.data.fileName }}"
            }
          ]
        }
      },
      "notesInFlow": true,
      "typeVersion": 3.4
    },
    {
      "id": "d85cf18b-825e-4ab8-a9b0-fef63cb66ad8",
      "name": "Store fileName",
      "type": "n8n-nodes-base.code",
      "position": [
        -1920,
        2020
      ],
      "parameters": {
        "jsCode": "let workflowData = $getWorkflowStaticData('global');\nworkflowData.fileName = $input.first().json.fileName\nreturn $json;\n"
      },
      "typeVersion": 2
    },
    {
      "id": "1ef71e46-4e1e-4707-99fc-41daa724a396",
      "name": "Get Picture",
      "type": "n8n-nodes-base.telegram",
      "position": [
        -2320,
        1840
      ],
      "webhookId": "09e9f612-0040-416a-8cbe-51d041d17436",
      "parameters": {
        "fileId": "={{ $('Telegram Trigger').item.json.message.photo[3].file_id }}",
        "resource": "file"
      },
      "typeVersion": 1.2
    },
    {
      "id": "9f0159ae-0236-470e-8935-d5991292ad63",
      "name": "Share Picture",
      "type": "n8n-nodes-base.googleDrive",
      "position": [
        -1960,
        1840
      ],
      "parameters": {
        "fileId": {
          "__rl": true,
          "mode": "id",
          "value": "={{ $json.id }}"
        },
        "options": {},
        "operation": "share",
        "permissionsUi": {
          "permissionsValues": {
            "role": "reader",
            "type": "anyone",
            "allowFileDiscovery": true
          }
        }
      },
      "typeVersion": 3
    },
    {
      "id": "66189707-157d-4f0d-b0b9-4b88d1fbc725",
      "name": "Initiate Workflow Data",
      "type": "n8n-nodes-base.code",
      "notes": "You only need to run the initialization step once per workflow, regardless of the number of Telegram chat IDs. The initialization creates the telegramStates object within the global static data of the workflow. Once that object exists, the workflow will use it to store the state for any chat ID.",
      "position": [
        -3500,
        -80
      ],
      "parameters": {
        "jsCode": "let workflowStaticData = $getWorkflowStaticData('global');\nif (!workflowStaticData.telegramStates) {\n    workflowStaticData.telegramStates = {}; \n}\nreturn workflowStaticData;"
      },
      "notesInFlow": false,
      "typeVersion": 2
    },
    {
      "id": "7db890fb-9fe2-4148-b01a-f01d3c4e5d89",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -3560,
        -300
      ],
      "parameters": {
        "width": 440,
        "height": 380,
        "content": "### 0. Initiate Workplace Static Data\nRun it **once** before activating the workflow to initialize workspace data that will be used to **store state flags** and **outputs from users**.\n\n#### How to setup?\n- **Code Node:** do not change anything, just run it\n  [Learn more about the code node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.code)\n"
      },
      "typeVersion": 1
    },
    {
      "id": "f01fb87a-1a24-4e0c-a769-9b5da7a402d2",
      "name": "Switch Command",
      "type": "n8n-nodes-base.switch",
      "position": [
        -2620,
        220
      ],
      "parameters": {
        "rules": {
          "values": [
            {
              "outputKey": "1",
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
                    "id": "f2c10700-113d-4062-8c00-af59ccbe3b6f",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $json.message.text }}",
                    "rightValue": "/addShipment"
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "2",
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
                    "id": "d09b6282-e9f8-4e43-b3db-9edae88cd634",
                    "operator": {
                      "name": "filter.operator.equals",
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $json.message.text }}",
                    "rightValue": "/addGPS"
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "3",
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
                    "id": "2637a054-0892-411c-b659-b878219a26ab",
                    "operator": {
                      "name": "filter.operator.equals",
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $json.message.text }}",
                    "rightValue": "/sendPhoto"
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "4",
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
                    "id": "5f3223e6-da0a-4056-8843-7778cf9de0a7",
                    "operator": {
                      "name": "filter.operator.equals",
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $json.message.text }}",
                    "rightValue": "/sendConfirmation"
                  }
                ]
              },
              "renameOutput": true
            }
          ]
        },
        "options": {
          "fallbackOutput": "extra"
        }
      },
      "notesInFlow": true,
      "typeVersion": 3.2
    },
    {
      "id": "2e121b11-0302-4be5-bc67-629ab6ea50b3",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -3060,
        -300
      ],
      "parameters": {
        "color": 7,
        "width": 620,
        "height": 740,
        "content": "### 1. Workflow Trigger with Telegram Message\nThe workflow is triggered by a user message. The second is checking if the message is a command (starting with \"/\") to route it to the proper block.\n\n#### How to setup?\n- **Telegram Trigger Node:** set up your telegram bot credentials\n[Learn more about the Telegram Trigger Node](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.telegramtrigger/)\n"
      },
      "typeVersion": 1
    },
    {
      "id": "3898ff6c-b127-4fdf-91b5-dd79c2906f05",
      "name": "Load Delivery Information",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        -2060,
        560
      ],
      "parameters": {
        "columns": {
          "value": {
            "recordTime": "={{ $now }}",
            "gpsLatitude": "={{ $json.gpsLatitude }}",
            "cargoPicture": "={{ $json.publicImageLink }}",
            "deliveryTime": "={{ $json.deliveryTime }}",
            "gpsLongitude": "={{ $json.gpsLongitude }}",
            "shipmentNumber": "={{ $json.shipmentNumber }}"
          },
          "schema": [
            {
              "id": "shipmentNumber",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "shipmentNumber",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "recordTime",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "recordTime",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "gpsLatitude",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "gpsLatitude",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "gpsLongitude",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "gpsLongitude",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "cargoPicture",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "cargoPicture",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "deliveryTime",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "deliveryTime",
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
        "operation": "append",
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": "gid=0",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/<FILE_ID>/edit#gid=0",
          "cachedResultName": "="
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "=",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/<FILE_ID>/edit?usp=drivesdk",
          "cachedResultName": "="
        }
      },
      "notesInFlow": true,
      "typeVersion": 4.5
    }
  ],
  "pinData": {},
  "connections": {
    "Command?": {
      "main": [
        [
          {
            "node": "Switch Command",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Waiting Conditions",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "waitingGPS": {
      "main": [
        [
          {
            "node": "addGPS",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Check State": {
      "main": [
        [
          {
            "node": "Shipment Number",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Store GPS Location",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Get Picture",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Instructions",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Picture": {
      "main": [
        [
          {
            "node": "Upload Picture",
            "type": "main",
            "index": 0
          },
          {
            "node": "Extract FileName",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "waitingPhoto": {
      "main": [
        [
          {
            "node": "sendPhoto",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Share Picture": {
      "main": [
        [
          {
            "node": "Save Public Image Link",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch Command": {
      "main": [
        [
          {
            "node": "waitingShipmentNumber",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "waitingGPS",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "waitingPhoto",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Load Workspace Data",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Welcome Message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Upload Picture": {
      "main": [
        [
          {
            "node": "Share Picture",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Shipment Number": {
      "main": [
        [
          {
            "node": "addShipmentNumber result",
            "type": "main",
            "index": 0
          },
          {
            "node": "Store Shipment",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract FileName": {
      "main": [
        [
          {
            "node": "Store fileName",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Telegram Trigger": {
      "main": [
        [
          {
            "node": "Command?",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Store GPS Location": {
      "main": [
        [
          {
            "node": "addGPS result",
            "type": "main",
            "index": 0
          },
          {
            "node": "Store GPS",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Waiting Conditions": {
      "main": [
        [
          {
            "node": "Check State",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Load Workspace Data": {
      "main": [
        [
          {
            "node": "Load Delivery Information",
            "type": "main",
            "index": 0
          },
          {
            "node": "Confirmation Driver",
            "type": "main",
            "index": 0
          },
          {
            "node": "Distribution Team Confirmation",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "waitingShipmentNumber": {
      "main": [
        [
          {
            "node": "addShipmentNumber",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Save Public Image Link": {
      "main": [
        [
          {
            "node": "addPhoto result",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Distribution Team Confirmation": {
      "main": [
        [
          {
            "node": "Clear State",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2435"></a>

## Template 2435 - Timer Pomodoro no Telegram

- **Nome:** Timer Pomodoro no Telegram
- **Descrição:** Fluxo que controla sessões Pomodoro iniciadas por comandos via Telegram, notifica o usuário durante o ciclo e registra sessões em uma planilha.
- **Funcionalidade:** • Detecção de mensagens via Telegram: O fluxo é disparado ao receber mensagens do usuário.
• Validação de comando: Verifica se a mensagem começa com "/" e encaminha para processamento de comando ou envia instruções quando não é um comando.
• Comando /start: Inicia uma sessão Pomodoro, envia notificação de início e passa por ciclos de foco (25 minutos) e pequeno intervalo.
• Contagem de ciclos: Mantém uma contagem por chat, incrementando a cada bloco de trabalho concluído e associando um sessionId e startTime ao usuário.
• Notificações ao usuário: Envia mensagens para iniciar foco, avisar fim de trabalho, iniciar retorno ao trabalho e avisar longo descanso quando aplicável.
• Registo de sessões: Cada bloco de trabalho e o longo intervalo final são gravados em uma planilha com data, hora, ID do usuário, tipo de bloco, contagem e sessionId.
• Long break após 4 ciclos: Ao atingir o quarto ciclo, envia notificação de longo descanso, registra o longo intervalo e limpa as variáveis do usuário.
• Comando /stop: Permite ao usuário encerrar a sessão antecipadamente, notifica o fim e limpa o estado associado ao chat.
• Armazenamento de estado por chat: Guarda localmente (por chat) os dados de sessão para controlar comportamento entre mensagens.
- **Ferramentas:** • Telegram Bot: Recebe comandos dos usuários e envia notificações e mensagens de instrução.
• Google Sheets: Armazena registros das sessões (data, hora, usuário, tipo de bloco, contagem, sessionId e durações).

## Fluxo visual

```mermaid
flowchart LR
    N1["Sticky Note3"]
    N2["Telegram Trigger"]
    N3["If"]
    N4["Deep Work"]
    N5["Break"]
    N6["Initiate Static Data"]
    N7["Increment Count"]
    N8["Record Deep Work"]
    N9["Record Long Break"]
    N10["Instructions Message"]
    N11["Sticky Note"]
    N12["Sticky Note1"]
    N13["start or stop?"]
    N14["Sticky Note2"]
    N15["Long Break Notification"]
    N16["Clear Variables1"]
    N17["Clear Variables2"]
    N18["< 4 Cycles"]
    N19["Short Break Notification"]
    N20["Back to Work Notification"]
    N21["Start Cycle Notification"]
    N22["End of Session Notification"]
    N23["Sticky Note4"]

    N3 --> N13
    N3 --> N10
    N5 --> N7
    N4 --> N19
    N18 --> N15
    N18 --> N21
    N13 --> N21
    N13 --> N22
    N7 --> N20
    N2 --> N3
    N15 --> N17
    N15 --> N9
    N19 --> N5
    N21 --> N4
    N20 --> N18
    N20 --> N8
    N22 --> N16
```

## Fluxo (.json) :

```json
{
  "meta": {
    "instanceId": "6a5e68bcca67c4cdb3e0b698d01739aea084e1ec06e551db64aeff43d174cb23",
    "templateCredsSetupCompleted": true
  },
  "nodes": [
    {
      "id": "bc49829b-45f2-4910-9c37-907271982f14",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        100,
        0
      ],
      "parameters": {
        "width": 780,
        "height": 540,
        "content": "### 4. Do you need more details?\nFind a step-by-step guide in this tutorial\n![Guide](https://www.samirsaci.com/content/images/2025/04/Pomodoro-Timer.png)\n[🎥 Watch My Tutorial](https://www.youtube.com/watch?v=ztMMrmbgGEo)"
      },
      "typeVersion": 1
    },
    {
      "id": "b5f24526-f1fc-43b0-82bf-887288838304",
      "name": "Telegram Trigger",
      "type": "n8n-nodes-base.telegramTrigger",
      "position": [
        -2560,
        540
      ],
      "webhookId": "09021985-57be-46c0-ac3d-c3a029ebf9e9",
      "parameters": {
        "updates": [
          "message"
        ],
        "additionalFields": {}
      },
      "typeVersion": 1.1
    },
    {
      "id": "8bb53ae0-515a-493d-9c1a-8a06362ada2e",
      "name": "If",
      "type": "n8n-nodes-base.if",
      "position": [
        -2340,
        540
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
              "id": "a0be860f-a9ae-4a49-b478-dac25bd550e2",
              "operator": {
                "type": "string",
                "operation": "startsWith"
              },
              "leftValue": "={{ $('Telegram Trigger').item.json.message.text }}",
              "rightValue": "/"
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "2bba3d64-03b7-4875-ac13-d4be13d2aa6d",
      "name": "Deep Work",
      "type": "n8n-nodes-base.wait",
      "position": [
        -1680,
        460
      ],
      "webhookId": "e4e8c51c-286e-47ff-809c-510069debd56",
      "parameters": {
        "unit": "minutes",
        "amount": 25
      },
      "typeVersion": 1.1
    },
    {
      "id": "bc3ea269-cbc5-4c7d-8ea1-74413883e425",
      "name": "Break",
      "type": "n8n-nodes-base.wait",
      "position": [
        -1340,
        460
      ],
      "webhookId": "3d3e199b-257c-4517-ab36-3e32242dabf8",
      "parameters": {
        "unit": "minutes"
      },
      "typeVersion": 1.1
    },
    {
      "id": "da225392-cd09-4afb-ba56-816484c742ae",
      "name": "Initiate Static Data",
      "type": "n8n-nodes-base.code",
      "notes": "You only need to run the initialization step once per workflow, regardless of the number of Telegram chat IDs. The initialization creates the telegramStates object within the global static data of the workflow. Once that object exists, the workflow will use it to store the state for any chat ID.",
      "position": [
        -2540,
        -160
      ],
      "parameters": {
        "jsCode": "let workflowStaticData = $getWorkflowStaticData('global');\nif (!workflowStaticData.telegramStates) {\n    workflowStaticData.telegramStates = {}; \n}\nreturn workflowStaticData;\n"
      },
      "notesInFlow": false,
      "typeVersion": 2
    },
    {
      "id": "b4f1ae18-ff8d-4b1d-8c26-8e3f87350d2d",
      "name": "Increment Count",
      "type": "n8n-nodes-base.code",
      "position": [
        -1180,
        460
      ],
      "parameters": {
        "jsCode": "let workflowStaticData = $getWorkflowStaticData('global');\n\nif (!workflowStaticData.telegramStates) {\n    workflowStaticData.telegramStates = {}; \n}\n\nlet userId = $('Telegram Trigger').first().json.message.chat.id.toString();\n\n// Ensure the user object exists\nif (!workflowStaticData.telegramStates[userId]) {\n    workflowStaticData.telegramStates[userId] = { count: 0, sessionId: \"\", startTime: \"\" };\n}\n\n// Check if sessionId is missing, then generate one\nif (!workflowStaticData.telegramStates[userId].sessionId) {\n    workflowStaticData.telegramStates[userId].sessionId = Date.now().toString(36) + Math.random().toString(36).substring(2, 8);\n    workflowStaticData.telegramStates[userId].startTime = new Date().toISOString();\n}\n\n// Increment the Pomodoro count\nworkflowStaticData.telegramStates[userId].count += 1;\n\n// Return the updated session details\nreturn [\n    {\n        json: {\n            count: workflowStaticData.telegramStates[userId].count,\n            sessionId: workflowStaticData.telegramStates[userId].sessionId,\n            startTime: workflowStaticData.telegramStates[userId].startTime\n        }\n    }\n];\n"
      },
      "typeVersion": 2
    },
    {
      "id": "5315d3fc-9c1e-4f3d-9e00-81f806d84e6a",
      "name": "Record Deep Work",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        -720,
        400
      ],
      "parameters": {
        "columns": {
          "value": {
            "Date": "={{ $now.format('dd-LL-yyyy') }}",
            "Time": "={{ $now.hour.toString().padStart(2, '0') }}:{{ $now.minute.toString().padStart(2, '0') }} ",
            "User ID": "={{ $json.result.chat.id }}",
            "Block Type": "Deep Work",
            "Pomodoro Count": "={{ $('Increment Count').item.json.count }}",
            "Working Session ID": "={{ $('Increment Count').item.json.sessionId }}",
            "Break Duration (min)": "5",
            "Focus Duration (min)": "25"
          },
          "schema": [
            {
              "id": "Date",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Date",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Time",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Time",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "User ID",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "User ID",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Working Session ID",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "Working Session ID",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Block Type",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "Block Type",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Pomodoro Count",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Pomodoro Count",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Focus Duration (min)",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Focus Duration (min)",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Break Duration (min)",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "Break Duration (min)",
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
        "operation": "append",
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": "gid=0",
          "cachedResultUrl": "=",
          "cachedResultName": "="
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "=",
          "cachedResultUrl": "=",
          "cachedResultName": "="
        }
      },
      "notesInFlow": true,
      "typeVersion": 4.5
    },
    {
      "id": "7328bccb-bb00-42bb-9659-6f66600894cc",
      "name": "Record Long Break",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        -120,
        460
      ],
      "parameters": {
        "columns": {
          "value": {
            "Date": "={{ $now.format('dd-LL-yyyy') }}",
            "Time": "={{ $now.hour.toString().padStart(2, '0') }}:{{ $now.minute.toString().padStart(2, '0') }} ",
            "User ID": "={{ $json.result.chat.id }}",
            "Block Type": "Long Break",
            "Pomodoro Count": "={{ $('Increment Count').item.json.count }}",
            "Working Session ID": "={{ $('Increment Count').item.json.sessionId }}",
            "Break Duration (min)": "15",
            "Focus Duration (min)": "0"
          },
          "schema": [
            {
              "id": "Date",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Date",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Time",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Time",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "User ID",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "User ID",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Working Session ID",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "Working Session ID",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Block Type",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "Block Type",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Pomodoro Count",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Pomodoro Count",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Focus Duration (min)",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Focus Duration (min)",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Break Duration (min)",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "Break Duration (min)",
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
        "operation": "append",
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": "gid=0",
          "cachedResultUrl": "=",
          "cachedResultName": "="
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "=",
          "cachedResultUrl": "=",
          "cachedResultName": "="
        }
      },
      "typeVersion": 4.5
    },
    {
      "id": "2d45a378-7188-4ac2-bb2e-c0ba745794d7",
      "name": "Instructions Message",
      "type": "n8n-nodes-base.telegram",
      "position": [
        -2160,
        660
      ],
      "webhookId": "a4c1043e-0520-4ef6-994c-6e733f90827b",
      "parameters": {
        "text": "=💡 Oops! That’s not a valid command.\n\nHere’s what you can do:\n✅ /start – Kick off a Pomodoro session and get in the zone.\n✅ /stop – Wrap up your session like a productivity pro.\n\nNow, let’s get some deep work done! 🔥💻",
        "chatId": "={{ $('Telegram Trigger').item.json.message.from.id }}",
        "additionalFields": {}
      },
      "notesInFlow": true,
      "typeVersion": 1.2
    },
    {
      "id": "14c90858-f22d-4495-bda0-c846209e6736",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -2580,
        -400
      ],
      "parameters": {
        "width": 440,
        "height": 380,
        "content": "### 0. Initiate Workplace Static Data\nRun it **once** before activating the workflow to initialize workspace data that will be used to **store state flags** and **outputs from users**.\n\n#### How to setup?\n- **Code Node:** do not change anything, just run it\n  [Learn more about the code node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.code)\n"
      },
      "typeVersion": 1
    },
    {
      "id": "26cdb973-26eb-41a6-b071-11b5b51faf70",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -2580,
        0
      ],
      "parameters": {
        "color": 7,
        "width": 620,
        "height": 940,
        "content": "### 1. Workflow Trigger with Telegram Message\n1. The workflow is triggered by a user message. \n2. The second is checking if the message is a command (starting with \"/\") to route it to the proper block. If the message is not a command, the bot sends an instruction message to the user.\n3. The third node checks if the message is a **/stop**. If yes, we stop the workflow the bot send a notice to the user and state variables are clears\n\n#### How to setup?\n- **Telegram Nodes:** set up your telegram bot credentials\n[Learn more about the Telegram Trigger Node](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.telegramtrigger/)\n"
      },
      "typeVersion": 1
    },
    {
      "id": "6d4f131c-076e-4d0a-9738-847692557468",
      "name": "start or stop?",
      "type": "n8n-nodes-base.if",
      "position": [
        -2160,
        460
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
              "id": "f169eadd-424b-42b0-8229-615608ecb23c",
              "operator": {
                "name": "filter.operator.equals",
                "type": "string",
                "operation": "equals"
              },
              "leftValue": "={{ $('Telegram Trigger').item.json.message.text }}",
              "rightValue": "/start"
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "aa50b802-83f1-47da-a9eb-cf2fc9576c28",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -1900,
        0
      ],
      "parameters": {
        "color": 7,
        "width": 1360,
        "height": 940,
        "content": "### 2. Deep Work Blocks of 25 minutes\n1. The bot notifies the user that the session started.\n2. After 25 minutes, it sends a notification to inform the user that [he/she] should take a break.\n3. The loop continues until we reached four working sessions.\n\n#### Why do we need Google Sheets?\nEach deep work session is recorded to help users keep track of their stats.\n\n#### How to setup?\n- **Deep Work & Break Mode**: fix the amount of time you want for the deep work session (Default: 25 min) and the short break (Default: 5 min)\n- **Telegram Nodes:** set up your telegram bot credentials\n[Learn more about the Telegram Trigger Node](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.telegramtrigger/)\n- **Record Deep Work in the Google Sheet Node**:\n   1. Add your Google Sheet API credentials to access the Google Sheet file\n   2. Select the file using the list, an URL or an ID\n   3. Select the sheet in which you want to record your working sessions\n   4. Map the fields\n  [Learn more about the Google Sheet Node](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets)\n"
      },
      "typeVersion": 1
    },
    {
      "id": "6a7b7b74-61b0-40de-8def-7bc602302d05",
      "name": "Long Break Notification",
      "type": "n8n-nodes-base.telegram",
      "position": [
        -440,
        520
      ],
      "webhookId": "251e850d-fcad-4fe8-a335-001ff1677415",
      "parameters": {
        "text": "🍴 Time for a long break. Great job!",
        "chatId": "={{ $('Telegram Trigger').item.json.message.from.id }}",
        "additionalFields": {
          "appendAttribution": false
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "fc63c241-53ee-4443-9a8c-a8f8a5da992b",
      "name": "Clear Variables1",
      "type": "n8n-nodes-base.code",
      "position": [
        -1680,
        760
      ],
      "parameters": {
        "jsCode": "let workflowStaticData = $getWorkflowStaticData('global');\nif (workflowStaticData.telegramStates) {\n    delete workflowStaticData.telegramStates[$('Telegram Trigger').first().json.message.chat.id.toString()];\n}\n\nreturn $input.all();"
      },
      "typeVersion": 2
    },
    {
      "id": "12297308-57ca-493f-8e65-49e396042893",
      "name": "Clear Variables2",
      "type": "n8n-nodes-base.code",
      "position": [
        -120,
        640
      ],
      "parameters": {
        "jsCode": "let workflowStaticData = $getWorkflowStaticData('global');\nif (workflowStaticData.telegramStates) {\n    delete workflowStaticData.telegramStates[$('Telegram Trigger').first().json.message.chat.id.toString()];\n}\n\nreturn $input.all();"
      },
      "typeVersion": 2
    },
    {
      "id": "46ab1b8b-c9be-4da9-a470-d1a4c9fcc219",
      "name": "< 4 Cycles",
      "type": "n8n-nodes-base.if",
      "position": [
        -720,
        540
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
              "id": "307c1ccf-9a10-49e6-a59d-d250edb1cae5",
              "operator": {
                "type": "number",
                "operation": "gt"
              },
              "leftValue": "={{ $('Increment Count').item.json.count }}",
              "rightValue": 4
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "22752905-50fc-48ee-9b4c-f80e6184c17f",
      "name": "Short Break Notification",
      "type": "n8n-nodes-base.telegram",
      "position": [
        -1520,
        460
      ],
      "webhookId": "b436cc4e-83d8-4bfa-9de9-e37cde83f9f9",
      "parameters": {
        "text": "🚰 Work session complete! Take a short break.",
        "chatId": "={{ $('Telegram Trigger').item.json.message.from.id }}",
        "additionalFields": {
          "appendAttribution": false
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "d43993be-ae96-4f83-8047-fffc956d2bac",
      "name": "Back to Work Notification",
      "type": "n8n-nodes-base.telegram",
      "position": [
        -1000,
        460
      ],
      "webhookId": "d13ad958-abf2-46a8-8785-da369933de24",
      "parameters": {
        "text": "=🏢 Break over! Back to work for the cycle: {{ $json.count }}",
        "chatId": "={{ $('Telegram Trigger').item.json.message.from.id }}",
        "additionalFields": {
          "appendAttribution": false
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "480f9003-3c1d-44a1-8552-8b59d9d074af",
      "name": "Start Cycle Notification",
      "type": "n8n-nodes-base.telegram",
      "position": [
        -1840,
        460
      ],
      "webhookId": "16fa6143-2d4e-44b5-b0d0-3d58bc6022a8",
      "parameters": {
        "text": "⏰ Time to focus! 25 minutes of deep work starts now.",
        "chatId": "={{ $('Telegram Trigger').item.json.message.from.id }}",
        "additionalFields": {
          "appendAttribution": false
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "b0ce8b4c-7e41-47f6-b505-46fdf606b84d",
      "name": "End of Session Notification",
      "type": "n8n-nodes-base.telegram",
      "position": [
        -1860,
        760
      ],
      "webhookId": "126e70c5-ea40-4bd5-81ee-5ca459db6a0d",
      "parameters": {
        "text": "=🛑 You decided to stop the session early.\n🚀 Use /start to relaunch a working session.",
        "chatId": "={{ $('Telegram Trigger').item.json.message.from.id }}",
        "additionalFields": {
          "appendAttribution": false
        }
      },
      "notesInFlow": true,
      "retryOnFail": false,
      "typeVersion": 1.2
    },
    {
      "id": "bd6b313b-2418-4b03-ad0e-7373b26b68c3",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -500,
        0
      ],
      "parameters": {
        "color": 7,
        "width": 560,
        "height": 940,
        "content": "### 3. End of the session for a long break\n1. The bot notifies the user that the session ended.\n2. The long break is recorded in the Google Sheets.\n3. Variables are cleared so the workflow is ready for a new session with this user.\n\n#### How to setup?\n- **Telegram Nodes:** set up your telegram bot credentials\n[Learn more about the Telegram Trigger Node](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.telegramtrigger/)\n- **Record Long Break in the Google Sheet Node**:\n   1. Add your Google Sheet API credentials to access the Google Sheet file\n   2. Select the file using the list, an URL or an ID\n   3. Select the sheet in which you want to record your working sessions\n   4. Map the fields\n  [Learn more about the Google Sheet Node](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets)\n"
      },
      "typeVersion": 1
    }
  ],
  "pinData": {
    "Telegram Trigger": [
      {
        "message": {
          "chat": {
            "id": 0,
            "type": "private",
            "username": "=",
            "first_name": "="
          },
          "date": 1742551547,
          "from": {
            "id": 0,
            "is_bot": false,
            "username": "=",
            "first_name": "=",
            "language_code": "en"
          },
          "text": "/stop",
          "entities": [
            {
              "type": "bot_command",
              "length": 6,
              "offset": 0
            }
          ],
          "message_id": 1846
        },
        "update_id": 567456699
      }
    ]
  },
  "connections": {
    "If": {
      "main": [
        [
          {
            "node": "start or stop?",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Instructions Message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Break": {
      "main": [
        [
          {
            "node": "Increment Count",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Deep Work": {
      "main": [
        [
          {
            "node": "Short Break Notification",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "< 4 Cycles": {
      "main": [
        [
          {
            "node": "Long Break Notification",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Start Cycle Notification",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "start or stop?": {
      "main": [
        [
          {
            "node": "Start Cycle Notification",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "End of Session Notification",
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
            "node": "Back to Work Notification",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Telegram Trigger": {
      "main": [
        [
          {
            "node": "If",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Long Break Notification": {
      "main": [
        [
          {
            "node": "Clear Variables2",
            "type": "main",
            "index": 0
          },
          {
            "node": "Record Long Break",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Short Break Notification": {
      "main": [
        [
          {
            "node": "Break",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Start Cycle Notification": {
      "main": [
        [
          {
            "node": "Deep Work",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Back to Work Notification": {
      "main": [
        [
          {
            "node": "< 4 Cycles",
            "type": "main",
            "index": 0
          },
          {
            "node": "Record Deep Work",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "End of Session Notification": {
      "main": [
        [
          {
            "node": "Clear Variables1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2436"></a>

## Template 2436 - Analisar imagem e salvar rótulos no Google Sheets

- **Nome:** Analisar imagem e salvar rótulos no Google Sheets
- **Descrição:** O fluxo busca uma imagem via API de busca, analisa seus rótulos usando reconhecimento de imagens e registra o nome, link e rótulos na planilha do Google Sheets.
- **Funcionalidade:** • Busca de imagem por termo: Realiza uma requisição à API de busca para obter resultados de imagem para um termo específico.
• Análise de conteúdo da imagem: Envia a imagem para um serviço de reconhecimento de imagens para detectar e extrair rótulos (labels).
• Extração e formatação de dados: Captura o título e link da imagem e compila os rótulos detectados em campos estruturados.
• Gravação em planilha: Adiciona uma nova linha na planilha do Google com o nome da imagem, link e os rótulos obtidos.
- **Ferramentas:** • Google Custom Search API: Serviço para pesquisar imagens na web e obter metadados como título e link.
• AWS Rekognition: Serviço de reconhecimento de imagens para detectar e retornar rótulos e informações sobre o conteúdo visual.
• Google Sheets: Plataforma para armazenar os resultados em uma planilha, permitindo futuras consultas e gerenciamento dos dados.



## Fluxo visual

```mermaid
flowchart LR
    N1["HTTP Request1"]
    N2["AWS Rekognition1"]
    N3["Google Sheets2"]
    N4["Set3"]

    N4 --> N3
    N1 --> N2
    N2 --> N4
```

## Fluxo (.json) :

```json
{
  "nodes": [
    {
      "name": "HTTP Request1",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        500,
        540
      ],
      "parameters": {
        "url": "https://www.googleapis.com/customsearch/v1?imgType=photo&key=AIzaSyBQry407hE5VwMaDedHogPuwJeIbAIidQU&cx=e51ced3f3563dfac9&q=street&searchType=image",
        "options": {}
      },
      "typeVersion": 1
    },
    {
      "name": "AWS Rekognition1",
      "type": "n8n-nodes-base.awsRekognition",
      "position": [
        680,
        540
      ],
      "parameters": {
        "type": "detectLabels",
        "binaryData": true,
        "additionalFields": {}
      },
      "credentials": {
        "aws": {
          "id": "9",
          "name": "aws"
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Google Sheets2",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        1040,
        540
      ],
      "parameters": {
        "options": {},
        "sheetId": "qwertz",
        "operation": "append",
        "authentication": "oAuth2"
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "2",
          "name": "google_sheets_oauth"
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Set3",
      "type": "n8n-nodes-base.set",
      "position": [
        860,
        540
      ],
      "parameters": {
        "values": {
          "number": [],
          "string": [
            {
              "name": "img_name",
              "value": "={{$node[\"HTTP Request1\"].json[\"items\"][0][\"title\"]}}"
            },
            {
              "name": "img_link",
              "value": "={{$node[\"HTTP Request1\"].json[\"items\"][0][\"link\"]}}"
            },
            {
              "name": "img_labels",
              "value": "={{$node[\"AWS Rekognition\"][\"Labels\"][\"Name\"]}}"
            }
          ]
        },
        "options": {},
        "keepOnlySet": true
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Set3": {
      "main": [
        [
          {
            "node": "Google Sheets2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "HTTP Request1": {
      "main": [
        [
          {
            "node": "AWS Rekognition1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "AWS Rekognition1": {
      "main": [
        [
          {
            "node": "Set3",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2438"></a>

## Template 2438 - Download de PDF via GET

- **Nome:** Download de PDF via GET
- **Descrição:** Este fluxo recebe uma requisição GET, baixa um arquivo PDF de uma URL externa e o retorna ao cliente como um anexo com nome contendo a data atual.
- **Funcionalidade:** • Disparo por requisição GET: Inicia o fluxo quando uma requisição GET é recebida no endpoint especificado.
• Download do PDF remoto: Faz uma requisição HTTP para baixar o arquivo PDF em formato binário.
• Resposta como anexo: Retorna o PDF ao solicitante configurando o cabeçalho Content-Disposition para forçar o download.
• Nomenclatura dinâmica do arquivo: Define o nome do arquivo retornado incluindo a data atual no formato yyyy-MM-dd.
- **Ferramentas:** • Servidor de arquivos HTTP (Deutsche Bahn): Fonte pública que hospeda e fornece o PDF acessado pela URL.



## Fluxo visual

```mermaid
flowchart LR
    N1["On GET request"]
    N2["Fetch binary file"]
    N3["Respond with attachment"]

    N1 --> N2
    N2 --> N3
```

## Fluxo (.json) :

```json
{
  "nodes": [
    {
      "id": "0357b17f-9fcf-4725-8311-28bd9c76c37c",
      "name": "On GET request",
      "type": "n8n-nodes-base.webhook",
      "position": [
        820,
        400
      ],
      "webhookId": "454eb4ea-e460-4196-b31c-284abf234fc3",
      "parameters": {
        "path": "download-pdf",
        "options": {},
        "responseMode": "responseNode"
      },
      "typeVersion": 1
    },
    {
      "id": "21d8c543-33c2-45eb-b392-2cb7139344c6",
      "name": "Fetch binary file",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1040,
        400
      ],
      "parameters": {
        "url": "https://www.deutschebahn.com/resource/blob/8813300/bdf106f07186f66e4448f95aca02bd4a/Faktenblatt-ICE-L_Mai23-data.pdf",
        "options": {
          "response": {
            "response": {
              "responseFormat": "file"
            }
          }
        }
      },
      "typeVersion": 4.1
    },
    {
      "id": "3ced3067-d82c-4bb4-b5fe-53a8d79c2177",
      "name": "Respond with attachment",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        1260,
        400
      ],
      "parameters": {
        "options": {
          "responseHeaders": {
            "entries": [
              {
                "name": "content-disposition",
                "value": "=attachment; filename=\"my_document_{{ $now.toFormat('yyyy-MM-dd') }}.pdf\""
              }
            ]
          }
        },
        "respondWith": "binary"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "On GET request": {
      "main": [
        [
          {
            "node": "Fetch binary file",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Fetch binary file": {
      "main": [
        [
          {
            "node": "Respond with attachment",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2441"></a>

## Template 2441 - Registro automático de refeições

- **Nome:** Registro automático de refeições
- **Descrição:** Recebe mensagens de texto ou voz pelo Telegram, interpreta a descrição das refeições, estima nutrientes principais e armazena os resultados em uma planilha do Google.
- **Funcionalidade:** • Recepção de mensagens do usuário: Detecta mensagens de texto ou mensagens de voz enviadas por um chat do Telegram.
• Transcrição de áudio: Converte mensagens de voz em texto para posterior processamento.
• Estimativa nutricional com IA: Usa um modelo de linguagem para aproximar kcal, proteínas, carboidratos, lipídeos e eletrólitos (sódio, potássio, magnésio, zinco e ferro) por item e em total.
• Saída estruturada em JSON: Gera a resposta como um JSON contendo nome do nutriente, quantidade, unidade e raciocínio (reasoning).
• Explosão e normalização dos itens: Separa a lista de nutrientes/itens retornada e normaliza cada entrada para armazenamento.
• Adição de data: Acrescenta uma data/formato compatível antes do salvamento para permitir filtros e somas posteriores.
• Armazenamento em planilha: Registra cada item (nome, quantidade, unidade, data) em uma Google Sheet para histórico e análise.
• Confirmação ao usuário: Envia uma mensagem de retorno no Telegram confirmando que a refeição foi salva.
• Controle de fluxo: Limita/organiza envios para evitar processamentos em excesso.
• Modo de teste/chat: Permite testar o fluxo via interface de chat para validar entradas e respostas.
- **Ferramentas:** • Telegram Bot API: Recebe mensagens de texto e áudio dos usuários e envia respostas de confirmação.
• OpenAI (modelos de linguagem e transcrição): Transcreve áudios e processa a descrição da refeição para estimativas nutricionais estruturadas em JSON.
• Google Sheets: Armazena os registros das refeições (nome do nutriente, quantidade, unidade, data) para histórico e análises futuras.

## Fluxo visual

```mermaid
flowchart LR
    N1["When chat message received"]
    N2["OpenAI Chat Model"]
    N3["Structured Output Parser"]
    N4["Get Audio File"]
    N5["Transcribe Recording"]
    N6["Limit"]
    N7["Receive Telegram message"]
    N8["If it's a voice message"]
    N9["Set chatInput from message"]
    N10["Set chatInput from voice"]
    N11["List of Ingredients and nutrients"]
    N12["Explode the list"]
    N13["Add date"]
    N14["Store in sheet"]
    N15["Sticky Note"]
    N16["Sticky Note1"]
    N17["Sticky Note2"]
    N18["Sticky Note3"]
    N19["Sticky Note4"]
    N20["Sticky Note5"]
    N21["Sticky Note6"]
    N22["Respond message"]
    N23["Sticky Note7"]

    N6 --> N22
    N13 --> N14
    N4 --> N5
    N14 --> N6
    N12 --> N13
    N5 --> N10
    N8 --> N4
    N8 --> N9
    N7 --> N8
    N10 --> N11
    N9 --> N11
    N1 --> N11
    N11 --> N12
```

## Fluxo (.json) :

```json
{
  "nodes": [
    {
      "id": "cab4467e-449e-4823-abe5-eb0368883e9c",
      "name": "When chat message received",
      "type": "@n8n/n8n-nodes-langchain.chatTrigger",
      "position": [
        740,
        180
      ],
      "webhookId": "231e8ee3-320f-47c7-8368-03965732d709",
      "parameters": {
        "options": {}
      },
      "typeVersion": 1.1
    },
    {
      "id": "a32a646b-80f2-46a4-81c2-7e3b5a4a192c",
      "name": "OpenAI Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        940,
        140
      ],
      "parameters": {
        "model": {
          "__rl": true,
          "mode": "list",
          "value": "gpt-4o-mini"
        },
        "options": {
          "temperature": 0
        }
      },
      "credentials": {
        "openAiApi": {
          "id": "1IOLtYX7aTspCAN8",
          "name": "OpenAI Pollup"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "3d934326-ad89-477f-9ab6-b97c04960597",
      "name": "Structured Output Parser",
      "type": "@n8n/n8n-nodes-langchain.outputParserStructured",
      "position": [
        1160,
        140
      ],
      "parameters": {
        "jsonSchemaExample": "\n[{\"name\": \"total Protein\",\n  \"quantity\": 86,\n  \"unit\": \"gr\"\n},\n  {\"name\": \"total lipids\",\n  \"quantity\": 86,\n  \"unit\": \"gr\"\n},\n  {\"name\": \"total carbohydrats\",\n  \"quantity\": 86,\n  \"unit\": \"gr\"\n},\n  {\"name\": \"total potassium\",\n  \"quantity\": 86,\n  \"unit\": \"gr\"\n},\n  {\"name\": \"total magnesium\",\n  \"quantity\": 86,\n  \"unit\": \"gr\"\n},\n  {\"name\": \"total sodium\",\n  \"quantity\": 86,\n  \"unit\": \"gr\"\n},\n  {\"name\": \"total kcal\",\n  \"quantity\": 248,\n  \"unit\": \"kcal\"\n},\n  {\n    \"reasoning\": \"this is my reasoning\"\n  }\n]"
      },
      "typeVersion": 1.2
    },
    {
      "id": "5a086fb6-6f12-40b6-aa82-64bb2d76b730",
      "name": "Get Audio File",
      "type": "n8n-nodes-base.telegram",
      "position": [
        300,
        -280
      ],
      "webhookId": "36dfe00d-6f05-419a-a80a-f6c7321e9a7d",
      "parameters": {
        "fileId": "={{ $json.message.voice.file_id }}",
        "resource": "file"
      },
      "credentials": {
        "telegramApi": {
          "id": "ynY4cqTMvfHfi0bc",
          "name": "Mes repas bot"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "f72d4182-26e2-4026-8097-7e4cef50bfed",
      "name": "Transcribe Recording",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "position": [
        520,
        -280
      ],
      "parameters": {
        "options": {},
        "resource": "audio",
        "operation": "transcribe",
        "binaryPropertyName": "=data"
      },
      "credentials": {
        "openAiApi": {
          "id": "1IOLtYX7aTspCAN8",
          "name": "OpenAI Pollup"
        }
      },
      "typeVersion": 1.6
    },
    {
      "id": "0f3b227f-b15a-410c-9333-a40c3e1b95ee",
      "name": "Limit",
      "type": "n8n-nodes-base.limit",
      "position": [
        1996,
        -80
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "fddaae3c-d7e6-4cb4-bb23-f734dcbefb85",
      "name": "Receive Telegram message",
      "type": "n8n-nodes-base.telegramTrigger",
      "position": [
        -140,
        -180
      ],
      "webhookId": "34756bf0-27bd-4384-9e46-549473c307a0",
      "parameters": {
        "updates": [
          "message",
          "channel_post"
        ],
        "additionalFields": {}
      },
      "credentials": {
        "telegramApi": {
          "id": "ynY4cqTMvfHfi0bc",
          "name": "Mes repas bot"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "9c6c00ca-e6f6-4f0b-b120-2249978379aa",
      "name": "If it's a voice message",
      "type": "n8n-nodes-base.if",
      "position": [
        80,
        -180
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
              "id": "fb7a6885-6149-4666-bd3a-5eebde28d601",
              "operator": {
                "type": "object",
                "operation": "exists",
                "singleValue": true
              },
              "leftValue": "={{ $json.message.voice }}",
              "rightValue": ""
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "97e56ec8-3a71-4e0d-a626-07a5113b09b7",
      "name": "Set chatInput from message",
      "type": "n8n-nodes-base.set",
      "position": [
        740,
        -80
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "3af0daa0-795f-45e8-ae10-fca10950b855",
              "name": "chatInput",
              "type": "string",
              "value": "={{ $json.message.text }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "e1609f06-f769-4dfe-98e4-a56e95217307",
      "name": "Set chatInput from voice",
      "type": "n8n-nodes-base.set",
      "position": [
        740,
        -280
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "3af0daa0-795f-45e8-ae10-fca10950b855",
              "name": "chatInput",
              "type": "string",
              "value": "={{ $json.text }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "42acb130-91f7-4d94-8b6b-c6b6b79f59f9",
      "name": "List of Ingredients and nutrients",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        960,
        -80
      ],
      "parameters": {
        "text": "=\n*\"Approximate the kcals, protein, carbohydrates, lipids (fats), and electrolyte (sodium, potassium, magnesium, Zinc and Iron) content in the following dietary intake statement:  \n\n{{ $json.chatInput }}\n\nProvide estimates for each component based on typical nutritional values. Break down the contributions from each food item (steak, salad, vinaigrette) and give a total number for each nutrient.  \n\nGive the total result as a json, with as name, the name of the nutrient, as quantity, the total summed value, and as unit the unit that been chosen (gr, mg).\nPut the reasoning in another variable called \"reasonning\"\n",
        "options": {
          "systemMessage": "You are a nutrition expert."
        },
        "promptType": "define",
        "hasOutputParser": true
      },
      "typeVersion": 1.8
    },
    {
      "id": "b27195f2-cb45-45d8-ab87-60e76828f7c4",
      "name": "Explode the list",
      "type": "n8n-nodes-base.splitOut",
      "position": [
        1336,
        -80
      ],
      "parameters": {
        "include": "={{ $json.output }}",
        "options": {},
        "fieldToSplitOut": "output"
      },
      "typeVersion": 1
    },
    {
      "id": "cf95c6a1-8ed4-45ee-90d0-fe87300c2968",
      "name": "Add date",
      "type": "n8n-nodes-base.code",
      "position": [
        1556,
        -80
      ],
      "parameters": {
        "mode": "runOnceForEachItem",
        "jsCode": "let entry = $input.item.json.output\nlet my_date = new Date()\n\nlet my_date_f = (my_date.getTime() / 86400000) + 25569;\nentry.my_date = my_date_f\nreturn {json: entry}"
      },
      "typeVersion": 2
    },
    {
      "id": "a0fd85ad-5cce-4419-af80-a6ff50a93631",
      "name": "Store in sheet",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        1776,
        -80
      ],
      "parameters": {
        "columns": {
          "value": {},
          "schema": [
            {
              "id": "name",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "name",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "quantity",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "quantity",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "unit",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "unit",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "my_date",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "my_date",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            }
          ],
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
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1HdL1iwHvIhN44yW_HzRbjC--ZxItCfyX-wObjWzZHAc/edit#gid=0",
          "cachedResultName": "Sheet1"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "1HdL1iwHvIhN44yW_HzRbjC--ZxItCfyX-wObjWzZHAc",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1HdL1iwHvIhN44yW_HzRbjC--ZxItCfyX-wObjWzZHAc/edit?usp=drivesdk",
          "cachedResultName": "Mes repas"
        }
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "gdLmm513ROUyH6oU",
          "name": "Google Sheets account"
        }
      },
      "typeVersion": 4.5
    },
    {
      "id": "06ee2513-0622-450b-b195-84cdef13cd27",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -200,
        -380
      ],
      "parameters": {
        "color": 4,
        "height": 340,
        "content": "## Send a Telegram message\n1. To your channel with the list of what you ate during your last meal. \nYour input can be a written or a voice message."
      },
      "typeVersion": 1
    },
    {
      "id": "fc4a2f5b-5565-4644-bd9f-74da73818698",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -680,
        -380
      ],
      "parameters": {
        "color": 5,
        "width": 460,
        "content": "## Setup\n1. Create a telegram Bot by following the instructions [here](https://docs.n8n.io/integrations/builtin/credentials/telegram/).\n2. Create an empty Google sheet and set it in \"Store in sheet\" along with your credentials\n3. Set your creadential for your OpenAI account\n"
      },
      "typeVersion": 1
    },
    {
      "id": "9e4e2ead-0c19-4799-8004-adaf30a5e0b1",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1700,
        -220
      ],
      "parameters": {
        "color": 4,
        "height": 320,
        "content": "## Check your data\n- to see if it seems correct \n- you can filter and sum your nutrients to check if you had enough! "
      },
      "typeVersion": 1
    },
    {
      "id": "e57b8eef-d72d-46b2-ae1b-5d61a2c22d01",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        260,
        -380
      ],
      "parameters": {
        "color": 4,
        "width": 640,
        "height": 260,
        "content": "## If it's an Audio file\nTRanscript it using openAI "
      },
      "typeVersion": 1
    },
    {
      "id": "9bd1447e-bcde-4b4c-92c9-76120c9a42d2",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        560,
        80
      ],
      "parameters": {
        "color": 4,
        "width": 340,
        "height": 260,
        "content": "## Testing\nYou can chat with the workflow by clicking on \"open chat\" to test your input and the response"
      },
      "typeVersion": 1
    },
    {
      "id": "ac3a7c88-782a-4943-a332-2509287df840",
      "name": "Sticky Note5",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        920,
        -220
      ],
      "parameters": {
        "color": 4,
        "width": 340,
        "height": 320,
        "content": "## Personalize the prompt!!\n- It's a very simple one, you can of course make it better!"
      },
      "typeVersion": 1
    },
    {
      "id": "58642d48-d97e-4a3d-84ea-a4de580e4c25",
      "name": "Sticky Note6",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2140,
        -220
      ],
      "parameters": {
        "color": 4,
        "height": 320,
        "content": "## Personalize the response message\nYou can send the response of the Agent\nOr just be more polite! "
      },
      "typeVersion": 1
    },
    {
      "id": "c6b8206c-bcb0-4034-8f99-9a4165770709",
      "name": "Respond message",
      "type": "n8n-nodes-base.telegram",
      "position": [
        2216,
        -80
      ],
      "webhookId": "8e646f8a-1f21-4719-b5f2-0cc5fad144df",
      "parameters": {
        "text": "Your meal has been saved",
        "chatId": "={{ $('If it's a voice message').item.json.message.chat.id }}",
        "additionalFields": {
          "appendAttribution": false
        }
      },
      "credentials": {
        "telegramApi": {
          "id": "ynY4cqTMvfHfi0bc",
          "name": "Mes repas bot"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "414d1da4-94e0-454d-acf9-a8344d1168b4",
      "name": "Sticky Note7",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -680,
        -200
      ],
      "parameters": {
        "width": 460,
        "height": 260,
        "content": "## Contact me\n- If you need any modification to this workflow\n- if you need some help with this workflow\n- Or if you need any workflow in n8n, Make, or Langchain / Langgraph\n\nWrite to me: [thomas@pollup.net](mailto:thomas@pollup.net)\n\nThis a light version of My Meals. I have a working \"Pro\" version with searches in the USDA database for each ingredients that return ALL the Nutrients.\n"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Limit": {
      "main": [
        [
          {
            "node": "Respond message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Add date": {
      "main": [
        [
          {
            "node": "Store in sheet",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Audio File": {
      "main": [
        [
          {
            "node": "Transcribe Recording",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Store in sheet": {
      "main": [
        [
          {
            "node": "Limit",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Explode the list": {
      "main": [
        [
          {
            "node": "Add date",
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
            "node": "List of Ingredients and nutrients",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Transcribe Recording": {
      "main": [
        [
          {
            "node": "Set chatInput from voice",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "If it's a voice message": {
      "main": [
        [
          {
            "node": "Get Audio File",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Set chatInput from message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Receive Telegram message": {
      "main": [
        [
          {
            "node": "If it's a voice message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set chatInput from voice": {
      "main": [
        [
          {
            "node": "List of Ingredients and nutrients",
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
            "node": "List of Ingredients and nutrients",
            "type": "ai_outputParser",
            "index": 0
          }
        ]
      ]
    },
    "Set chatInput from message": {
      "main": [
        [
          {
            "node": "List of Ingredients and nutrients",
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
            "node": "List of Ingredients and nutrients",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "List of Ingredients and nutrients": {
      "main": [
        [
          {
            "node": "Explode the list",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2443"></a>

## Template 2443 - Criar cartão no Nextcloud Deck a partir de e-mail

- **Nome:** Criar cartão no Nextcloud Deck a partir de e-mail
- **Descrição:** Cria automaticamente um cartão no Nextcloud Deck quando um e-mail é recebido, usando o assunto como título e o corpo como descrição.
- **Funcionalidade:** • Monitoramento de e-mail (IMAP): Verifica a chegada de novas mensagens em uma conta de e-mail configurada.
• Normalização do corpo do e-mail: Remove HTML e converte quebras de linha para texto simples, garantindo conteúdo limpo.
• Uso do assunto como título: Define o assunto do e-mail como título do cartão criado.
• Criação de cartão no Board/Stack: Envia uma requisição HTTP para criar um cartão em um board/stack específico do Nextcloud Deck.
• Configuração de autenticação e cabeçalhos: Utiliza autenticação básica e cabeçalhos necessários para a API do Nextcloud.
- **Ferramentas:** • Conta de e-mail (IMAP): Fonte dos e-mails que disparam a criação dos cartões.
• Nextcloud Deck (API HTTP): Plataforma onde os cartões são criados via chamadas HTTP à API do Nextcloud, usando board e stack configurados.

## Fluxo visual

```mermaid
flowchart LR
    N1["IMAP Email"]
    N2["Function"]
    N3["HTTP Request"]

    N2 --> N3
    N1 --> N2
```

## Fluxo (.json) :

```json
{
  "id": 1,
  "name": "Create Nextcloud Deck card from email",
  "nodes": [
    {
      "name": "IMAP Email",
      "type": "n8n-nodes-base.emailReadImap",
      "notes": "Check email",
      "position": [
        480,
        140
      ],
      "parameters": {
        "options": {}
      },
      "credentials": {
        "imap": {
          "id": "2",
          "name": "todo@yourdomain.com"
        }
      },
      "notesInFlow": true,
      "typeVersion": 1
    },
    {
      "name": "Function",
      "type": "n8n-nodes-base.function",
      "notes": "Strip HTML code",
      "position": [
        730,
        140
      ],
      "parameters": {
        "functionCode": "// Code here will run only once, no matter how many input items there are.\n// More info and help: https://docs.n8n.io/nodes/n8n-nodes-base.function\n\n// Loop over inputs and add a new field called 'myNewField' to the JSON of each one\nfor (item of items) {\n  if (item.json.textHtml) {\n    // Remove HTML, double quotations, line breaks, carriage returns\n    item.json.body = item.json.textHtml.replace(/<br(\\s*?/?)>/g, \"\\\\n\").replace(/(<([^>]+)>)/g, \"\").replace(/\\\"/g, \"\");\n    //item.json.body = item.json.textHtml.eplace(/(<([^>]+)>)/g, \"\").replace(/\\\"/g, \"\").replace(/\\n/g, \"\").replace(/\\r/g, \"\");\n  } else {\n    // Remove double quotations, line breaks, carriage returns\n    item.json.body = item.json.textPlain.replace(/\\\"/g, \"\").replace(/\\n/g, \"\\\\n\").replace(/\\r/g, \"\");\n  }\n}\n\n// You can write logs to the browser console\nconsole.log('Done!');\n\nreturn items;"
      },
      "notesInFlow": true,
      "typeVersion": 1
    },
    {
      "name": "HTTP Request",
      "type": "n8n-nodes-base.httpRequest",
      "notes": "Add card to Nextcloud Deck App. Configure board / stack id to your environment.",
      "position": [
        970,
        140
      ],
      "parameters": {
        "url": "https://your.nextcloud.com/index.php/apps/deck/api/v1.0/boards/YOUR-BOARD-ID/stacks/YOUR-STACK-ID/cards",
        "options": {},
        "requestMethod": "POST",
        "authentication": "basicAuth",
        "jsonParameters": true,
        "bodyParametersJson": "={\n\"title\": \"{{$json[\"subject\"]}}\",\n\"type\": \"plain\",\n\"order\": -1,\n\"description\": \"{{$json[\"body\"]}}\"\n}",
        "headerParametersJson": "{\n\"OCS-APIRequest\": \"true\",\n\"Content-Type\": \"application/json\"\n}"
      },
      "credentials": {
        "httpBasicAuth": {
          "id": "3",
          "name": "Nextcloud credential"
        }
      },
      "notesInFlow": true,
      "typeVersion": 1
    }
  ],
  "active": true,
  "settings": {},
  "connections": {
    "Function": {
      "main": [
        [
          {
            "node": "HTTP Request",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "IMAP Email": {
      "main": [
        [
          {
            "node": "Function",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2445"></a>

## Template 2445 - Criar/atualizar chamados no Syncro a partir de chamadas Dialpad

- **Nome:** Criar/atualizar chamados no Syncro a partir de chamadas Dialpad
- **Descrição:** Recebe webhooks de chamadas (inbound) do Dialpad, procura contatos/clientes no Syncro e cria ou atualiza chamados conforme regras, registrando o resultado em uma planilha.
- **Funcionalidade:** • Recepção de webhook de chamada: Aceita POSTs contendo dados da chamada e filtra apenas chamadas inbound.
• Normalização do número: Remove sinais como "+" e prefixos comuns antes da pesquisa.
• Busca de contato/cliente: Consulta a base do Syncro para localizar contatos e clientes pelo número de telefone.
• Extração de dados: Agrupa e formata os resultados da busca em listas de contatos e clientes utilizáveis.
• Verificação de chamados abertos: Para um contato encontrado, consulta chamados não fechados relacionados a esse contato.
• Atualização de chamado existente: Se houver exatamente um chamado não fechado, adiciona um comentário oculto e atualiza o assunto com informações da chamada.
• Criação de novo chamado: Se não houver chamado único, cria um novo chamado atrelado ao contato ou ao cliente, com status e usuário definidos.
• Registro em planilha: Registra o par (call_id, ticket_id) em uma planilha do Google Sheets para auditoria/controle.
• Uso de variáveis de ambiente: Utiliza URL base do Syncro e user_id configuráveis para requisições e atribuições.
- **Ferramentas:** • Dialpad: Fonte dos webhooks de chamadas e informações do contato/telefone.
• Syncro (Syncro MSP): Sistema de ticketing/CRM onde são buscados contatos/clientes, criados e atualizados chamados.
• Google Sheets: Planilha usada para registrar logs simples com identificador da chamada e do chamado.

## Fluxo visual

```mermaid
flowchart LR
    N1["GetCustomer"]
    N2["Webhook"]
    N3["CreateTicket"]
    N4["GetTicket"]
    N5["IFMoreThanOne"]
    N6["Google Sheets"]
    N7["ForGoogle"]
    N8["UpdateTicket"]
    N9["ForGoogle1"]
    N10["Google Sheets1"]
    N11["NoOp"]
    N12["Contacts"]
    N13["IFContacts"]
    N14["Customers"]
    N15["IFCustomers"]
    N16["NoOp1"]
    N17["CreateTicketForCustomer"]
    N18["ForGoogle2"]
    N19["Google Sheets2"]
    N20["EnvVariables"]
    N21["IF"]
    N22["NoOp2"]

    N21 --> N20
    N21 --> N22
    N2 --> N21
    N12 --> N13
    N14 --> N15
    N7 --> N6
    N4 --> N5
    N9 --> N10
    N18 --> N19
    N13 --> N4
    N13 --> N11
    N1 --> N12
    N1 --> N14
    N15 --> N17
    N15 --> N16
    N3 --> N9
    N20 --> N1
    N8 --> N7
    N5 --> N8
    N5 --> N3
    N17 --> N18
```

## Fluxo (.json) :

```json
{
  "id": "1",
  "name": "Dialpad to Syncro",
  "nodes": [
    {
      "name": "GetCustomer",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        350,
        180
      ],
      "parameters": {
        "url": "={{$node[\"EnvVariables\"].json[\"syncro_baseurl\"]}}/api/v1/search?query={{$json[\"body\"][\"external_number\"].replace(/\\+/g, '').replace(/^[01]/, '')}}",
        "options": {},
        "authentication": "headerAuth"
      },
      "credentials": {
        "httpHeaderAuth": "Syncro"
      },
      "typeVersion": 1
    },
    {
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "position": [
        -60,
        180
      ],
      "webhookId": "ec452bb5-58d9-4e0d-9cd2-c6df1c2cd957",
      "parameters": {
        "path": "moezdialpad",
        "options": {},
        "httpMethod": "POST",
        "responseData": "allEntries",
        "responseMode": "lastNode"
      },
      "typeVersion": 1
    },
    {
      "name": "CreateTicket",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1190,
        110
      ],
      "parameters": {
        "url": "={{$node[\"EnvVariables\"].json[\"syncro_baseurl\"]}}/api/v1/tickets",
        "options": {
          "bodyContentType": "json"
        },
        "requestMethod": "POST",
        "authentication": "headerAuth",
        "bodyParametersUi": {
          "parameter": [
            {
              "name": "customer_id",
              "value": "={{$node[\"Contacts\"].json[\"contacts\"][0][\"customer_id\"]}}"
            },
            {
              "name": "subject",
              "value": "=Phone call from {{$node[\"Function\"].json[\"contacts\"][0][\"firstname\"]}} {{$node[\"Function\"].json[\"contacts\"][0][\"lastname\"]}} ({{$node[\"Webhook\"].json[\"body\"][\"contact\"][\"phone\"]}})"
            },
            {
              "name": "status",
              "value": "In Progress"
            },
            {
              "name": "contact_id",
              "value": "={{$node[\"Contacts\"].json[\"contacts\"][0][\"id\"]}}"
            },
            {
              "name": "user_id",
              "value": "={{$node[\"EnvVariables\"].parameter[\"values\"][\"string\"][1][\"value\"]}}"
            }
          ]
        }
      },
      "credentials": {
        "httpHeaderAuth": "Syncro"
      },
      "typeVersion": 1
    },
    {
      "name": "GetTicket",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        860,
        40
      ],
      "parameters": {
        "url": "={{$node[\"EnvVariables\"].json[\"syncro_baseurl\"]}}/api/v1/tickets?contact_id={{$json[\"contacts\"][0][\"id\"]}}&status=Not%20Closed",
        "options": {},
        "authentication": "headerAuth"
      },
      "credentials": {
        "httpHeaderAuth": "Syncro"
      },
      "typeVersion": 1
    },
    {
      "name": "IFMoreThanOne",
      "type": "n8n-nodes-base.if",
      "position": [
        1000,
        40
      ],
      "parameters": {
        "conditions": {
          "number": [
            {
              "value1": "={{$node[\"GetTicket\"].json[\"tickets\"].length}}",
              "value2": 1,
              "operation": "equal"
            }
          ],
          "boolean": [
            {
              "value1": "={{$json[\"tickets\"]}}",
              "value2": true
            }
          ]
        },
        "combineOperation": "any"
      },
      "typeVersion": 1
    },
    {
      "name": "Google Sheets",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        1480,
        -40
      ],
      "parameters": {
        "range": "A:B",
        "options": {
          "valueInputMode": "USER_ENTERED"
        },
        "sheetId": "xxx",
        "operation": "append"
      },
      "credentials": {
        "googleApi": "Google"
      },
      "typeVersion": 1
    },
    {
      "name": "ForGoogle",
      "type": "n8n-nodes-base.set",
      "position": [
        1340,
        -40
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "Call",
              "value": "={{$node[\"Webhook\"].json[\"body\"][\"call_id\"]}}"
            },
            {
              "name": "Ticket",
              "value": "={{$node[\"GetTicket\"].json[\"tickets\"][0][\"id\"]}}"
            }
          ]
        },
        "options": {},
        "keepOnlySet": true
      },
      "typeVersion": 1
    },
    {
      "name": "UpdateTicket",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1190,
        -40
      ],
      "parameters": {
        "url": "={{$node[\"EnvVariables\"].json[\"syncro_baseurl\"]}}/api/v1/tickets/{{$json[\"tickets\"][0][\"id\"]}}/comment",
        "options": {},
        "requestMethod": "POST",
        "authentication": "headerAuth",
        "bodyParametersUi": {
          "parameter": [
            {
              "name": "subject",
              "value": "=Phone call from {{$node[\"GetCustomer\"].json[\"results\"][0][\"table\"][\"_source\"][\"table\"][\"firstname\"]}} {{$node[\"GetCustomer\"].json[\"results\"][0][\"table\"][\"_source\"][\"table\"][\"lastname\"]}} ({{$node[\"Webhook\"].json[\"body\"][\"contact\"][\"phone\"]}})"
            },
            {
              "name": "body",
              "value": "={{$node[\"GetCustomer\"].json[\"results\"][0][\"table\"][\"_source\"][\"table\"][\"firstname\"]}} {{$node[\"GetCustomer\"].json[\"results\"][0][\"table\"][\"_source\"][\"table\"][\"lastname\"]}} called."
            },
            {
              "name": "hidden",
              "value": "true"
            },
            {
              "name": "user_id",
              "value": "={{$node[\"EnvVariables\"].parameter[\"values\"][\"string\"][1][\"value\"]}}"
            }
          ]
        }
      },
      "credentials": {
        "httpHeaderAuth": "Syncro"
      },
      "typeVersion": 1
    },
    {
      "name": "ForGoogle1",
      "type": "n8n-nodes-base.set",
      "position": [
        1340,
        110
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "Call",
              "value": "={{$node[\"Webhook\"].json[\"body\"][\"call_id\"]}}"
            },
            {
              "name": "Ticket",
              "value": "={{$node[\"CreateTicket\"].json[\"ticket\"][\"id\"]}}"
            }
          ]
        },
        "options": {},
        "keepOnlySet": true
      },
      "typeVersion": 1
    },
    {
      "name": "Google Sheets1",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        1480,
        110
      ],
      "parameters": {
        "range": "A:B",
        "options": {
          "valueInputMode": "USER_ENTERED"
        },
        "sheetId": "xxx",
        "operation": "append"
      },
      "credentials": {
        "googleApi": "Google"
      },
      "typeVersion": 1
    },
    {
      "name": "NoOp",
      "type": "n8n-nodes-base.noOp",
      "position": [
        830,
        220
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Contacts",
      "type": "n8n-nodes-base.function",
      "position": [
        510,
        180
      ],
      "parameters": {
        "functionCode": "const { json: { results } } = items[0];\n\nconst getData = (results, type) => results.filter(r => r.table._index === type).map(x => ({\n   id: x.table._id,\n   firstname: x.table._source.table.firstname,\n   lastname: x.table._source.table.lastname,\n   customer_id: x.table._source.table.customer_id,\n   email: x.table._source.table.email,\n   business_name: x.table._source.table.business_name,\n   phones: x.table._source.table.phones\n }));\n \nreturn [ { json: { contacts: getData(results, 'contacts') } } ];\n"
      },
      "typeVersion": 1,
      "alwaysOutputData": false
    },
    {
      "name": "IFContacts",
      "type": "n8n-nodes-base.if",
      "position": [
        670,
        180
      ],
      "parameters": {
        "conditions": {
          "number": [
            {
              "value1": "={{$node[\"Contacts\"].json[\"contacts\"].length}}",
              "value2": 1,
              "operation": "equal"
            }
          ],
          "string": [],
          "boolean": []
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Customers",
      "type": "n8n-nodes-base.function",
      "position": [
        510,
        370
      ],
      "parameters": {
        "functionCode": "const { json: { results } } = items[0];\n\nconst getData = (results, type) => results.filter(r => r.table._index === type).map(x => ({\n   id: x.table._id,\n   firstname: x.table._source.table.firstname,\n   lastname: x.table._source.table.lastname,\n   customer_id: x.table._source.table.customer_id,\n   email: x.table._source.table.email,\n   business_name: x.table._source.table.business_name,\n   phones: x.table._source.table.phones\n }));\n \nreturn [ { json: { customers: getData(results, 'customers') } } ];\n"
      },
      "typeVersion": 1
    },
    {
      "name": "IFCustomers",
      "type": "n8n-nodes-base.if",
      "position": [
        670,
        370
      ],
      "parameters": {
        "conditions": {
          "number": [
            {
              "value1": "={{$node[\"Customers\"].json[\"customers\"].length}}",
              "value2": 1,
              "operation": "equal"
            }
          ],
          "string": [],
          "boolean": []
        }
      },
      "typeVersion": 1
    },
    {
      "name": "NoOp1",
      "type": "n8n-nodes-base.noOp",
      "position": [
        810,
        520
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "CreateTicketForCustomer",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        860,
        360
      ],
      "parameters": {
        "url": "={{$node[\"EnvVariables\"].json[\"syncro_baseurl\"]}}/api/v1/tickets",
        "options": {
          "bodyContentType": "json"
        },
        "requestMethod": "POST",
        "authentication": "headerAuth",
        "bodyParametersUi": {
          "parameter": [
            {
              "name": "customer_id",
              "value": "={{$node[\"Customers\"].json[\"customers\"][0][\"id\"]}}"
            },
            {
              "name": "subject",
              "value": "=Phone call from {{$node[\"Customers\"].json[\"customers\"][0][\"business_name\"]}} ({{$node[\"Webhook\"].json[\"body\"][\"contact\"][\"phone\"]}})"
            },
            {
              "name": "status",
              "value": "In Progress"
            },
            {
              "name": "user_id",
              "value": "={{$node[\"EnvVariables\"].parameter[\"values\"][\"string\"][1][\"value\"]}}"
            }
          ]
        }
      },
      "credentials": {
        "httpHeaderAuth": "Syncro"
      },
      "typeVersion": 1
    },
    {
      "name": "ForGoogle2",
      "type": "n8n-nodes-base.set",
      "position": [
        1040,
        360
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "Call",
              "value": "={{$node[\"Webhook\"].json[\"body\"][\"call_id\"]}}"
            },
            {
              "name": "Ticket",
              "value": "={{$node[\"CreateTicketForCustomer\"].json[\"ticket\"][\"id\"]}}"
            }
          ]
        },
        "options": {},
        "keepOnlySet": true
      },
      "typeVersion": 1
    },
    {
      "name": "Google Sheets2",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        1210,
        360
      ],
      "parameters": {
        "range": "A:B",
        "options": {
          "valueInputMode": "USER_ENTERED"
        },
        "sheetId": "xxx",
        "operation": "append"
      },
      "credentials": {
        "googleApi": "Google"
      },
      "typeVersion": 1
    },
    {
      "name": "EnvVariables",
      "type": "n8n-nodes-base.set",
      "position": [
        210,
        180
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "syncro_baseurl",
              "value": "https://subdomain.syncromsp.com"
            },
            {
              "name": "user_id",
              "value": "1234"
            }
          ]
        },
        "options": {}
      },
      "typeVersion": 1
    },
    {
      "name": "IF",
      "type": "n8n-nodes-base.if",
      "position": [
        70,
        180
      ],
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$node[\"Webhook\"].json[\"body\"][\"direction\"]}}",
              "value2": "inbound"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "NoOp2",
      "type": "n8n-nodes-base.noOp",
      "position": [
        70,
        370
      ],
      "parameters": {},
      "typeVersion": 1
    }
  ],
  "active": true,
  "settings": {},
  "connections": {
    "IF": {
      "main": [
        [
          {
            "node": "EnvVariables",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "NoOp2",
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
            "node": "IF",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Contacts": {
      "main": [
        [
          {
            "node": "IFContacts",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Customers": {
      "main": [
        [
          {
            "node": "IFCustomers",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "ForGoogle": {
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
    "GetTicket": {
      "main": [
        [
          {
            "node": "IFMoreThanOne",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "ForGoogle1": {
      "main": [
        [
          {
            "node": "Google Sheets1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "ForGoogle2": {
      "main": [
        [
          {
            "node": "Google Sheets2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "IFContacts": {
      "main": [
        [
          {
            "node": "GetTicket",
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
    "GetCustomer": {
      "main": [
        [
          {
            "node": "Contacts",
            "type": "main",
            "index": 0
          },
          {
            "node": "Customers",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "IFCustomers": {
      "main": [
        [
          {
            "node": "CreateTicketForCustomer",
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
    },
    "CreateTicket": {
      "main": [
        [
          {
            "node": "ForGoogle1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "EnvVariables": {
      "main": [
        [
          {
            "node": "GetCustomer",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "UpdateTicket": {
      "main": [
        [
          {
            "node": "ForGoogle",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "IFMoreThanOne": {
      "main": [
        [
          {
            "node": "UpdateTicket",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "CreateTicket",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "CreateTicketForCustomer": {
      "main": [
        [
          {
            "node": "ForGoogle2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2448"></a>

## Template 2448 - Integração Cloudflare KV (CRUD e operações em lote)

- **Nome:** Integração Cloudflare KV (CRUD e operações em lote)
- **Descrição:** Fluxo que expõe operações para gerenciar Namespaces e pares chave-valor no Cloudflare Workers KV utilizando a API do Cloudflare.
- **Funcionalidade:** • Criar Namespace: Permite criar um novo namespace (KV Namespace) na conta especificada.
• Listar Namespaces: Recupera a lista de namespaces disponíveis na conta.
• Excluir Namespace por nome: Localiza um namespace pelo título e o remove.
• Renomear Namespace: Busca um namespace pelo título e altera seu título (rename).
• Escrever valor com metadados: Grava um valor em uma chave específica incluindo metadados (multipart/form-data PUT).
• Ler valor de chave: Recupera o conteúdo (valor) de uma chave específica dentro de um namespace.
• Ler metadados de chave: Obtém somente os metadados associados a uma chave específica.
• Excluir chave específica: Remove um par chave-valor dentro de um namespace.
• Gravar múltiplos pares (bulk write): Envia vários pares chave-valor em uma única requisição bulk (PUT /bulk).
• Excluir múltiplos pares (bulk delete): Remove múltiplas chaves de um namespace em uma única requisição bulk (DELETE /bulk).
• Listar chaves de um namespace: Recupera a lista de chaves existentes dentro de um namespace.
• Configuração de conta/identificador: Utiliza um identificador de conta (account_identifier) configurável para direcionar as chamadas à conta correta.
- **Ferramentas:** • Cloudflare Workers KV: Serviço de armazenamento key-value distribuído usado para salvar chaves, valores e metadados.
• Cloudflare API (Client v4): API REST utilizada para criar, listar, renomear e excluir namespaces, bem como para operações sobre chaves e bulk operations.
• Autenticação com Account Identifier e Token/API Key: Credenciais da conta (account_identifier e token) necessárias para autorizar chamadas à API do Cloudflare.



## Fluxo visual

```mermaid
flowchart LR
    N1["Sticky Note"]
    N2["Sticky Note1"]
    N3["Sticky Note2"]
    N4["Delete KV"]
    N5["Sticky Note3"]
    N6["Delete KV1"]
    N7["KV to Rename"]
    N8["Account Path"]
    N9["Sticky Note4"]
    N10["Sticky Note5"]
    N11["Delete KVs inside NM"]
    N12["Sticky Note6"]
    N13["Create KV-NM"]
    N14["Write KVs inside NM"]
    N15["Sticky Note7"]
    N16["-Get Keys inside NM"]
    N17["Sticky Note8"]
    N18["Sticky Note9"]
    N19["Sticky Note10"]
    N20["Delete KV inside NM"]
    N21["Sticky Note11"]
    N22["Read Value Of KV In NM"]
    N23["Sticky Note12"]
    N24["Sticky Note13"]
    N25["Sticky Note14"]
    N26["Sticky Note15"]
    N27["Manual Trigger"]
    N28["List KV-NMs (1)"]
    N29["Set KV-NM Name (2)"]
    N30["Set KV-NM Name (1)"]
    N31["Set KV-NM Name (3)"]
    N32["List KV-NMs (2)"]
    N33["List KV-NMs (3)"]
    N34["Set KV-NM Name (4)"]
    N35["Write V & MD of KV In NM"]
    N36["Set KV-NM Name (5)"]
    N37["Set KV-NM Name (6)"]
    N38["List KV-NMs (4)"]
    N39["List KV-NMs (5)"]
    N40["List KV-NMs (6)"]
    N41["List KV-NMs (7)"]
    N42["List KV-NMs (8)"]
    N43["List KV-NMs (9)"]
    N44["List KV-NMs (10)"]
    N45["Set KV-NM Name (7)"]
    N46["Set KV-NM Name (8)"]
    N47["Read MD from Key"]

    N8 --> N30
    N8 --> N13
    N8 --> N37
    N8 --> N29
    N8 --> N7
    N8 --> N45
    N8 --> N31
    N8 --> N36
    N8 --> N46
    N7 --> N39
    N27 --> N8
    N28 --> N20
    N32 --> N4
    N33 --> N11
    N38 --> N35
    N39 --> N6
    N40 --> N14
    N41 --> N22
    N42 --> N47
    N43 --> N16
    N30 --> N28
    N29 --> N32
    N31 --> N33
    N34 --> N38
    N36 --> N40
    N37 --> N41
    N45 --> N42
    N46 --> N43
```

## Fluxo (.json) :

```json
{
  "meta": {
    "instanceId": "dbd43d88d26a9e30d8aadc002c9e77f1400c683dd34efe3778d43d27250dde50"
  },
  "nodes": [
    {
      "id": "14a494bf-acda-4758-ab79-bae07b7bbd10",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2800,
        1744
      ],
      "parameters": {
        "color": 6,
        "width": 305,
        "height": 254.26094733974475,
        "content": "## List NMs\nto change parameters read [Docs](https://developers.cloudflare.com/api/operations/workers-kv-namespace-list-namespaces)"
      },
      "typeVersion": 1
    },
    {
      "id": "a97a332f-e8f2-4011-9158-66cff1f0773f",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        476,
        1460
      ],
      "parameters": {
        "color": 4,
        "width": 289.22425544359976,
        "height": 259,
        "content": "## Create NM\nto change parameters read [Docs](https://developers.cloudflare.com/api/operations/workers-kv-namespace-create-a-namespace)"
      },
      "typeVersion": 1
    },
    {
      "id": "b7575223-8467-4723-9b4d-38941382aea8",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1399,
        1180
      ],
      "parameters": {
        "color": 3,
        "width": 767.2997851806018,
        "height": 260.5583291593211,
        "content": "## Delete NM of KV (By Name Serach)\nto change anything read [Docs](https://developers.cloudflare.com/api/operations/workers-kv-namespace-remove-a-namespace)"
      },
      "typeVersion": 1
    },
    {
      "id": "259848b4-5472-436e-9ef7-dbba14f21348",
      "name": "Delete KV",
      "type": "n8n-nodes-base.httpRequest",
      "notes": "Delete Selected KV",
      "position": [
        2000,
        1280
      ],
      "parameters": {
        "url": "=https://api.cloudflare.com/client/v4/accounts/{{ $('Account Path').params[\"fields\"][\"values\"][0][\"stringValue\"] }}/storage/kv/namespaces/{{ $node[\"List KV-NMs (2)\"].json[\"result\"].find(kv => kv.title === $node[\"Set KV-NM Name (2)\"].json[\"NameSpace\"]).id }}",
        "method": "DELETE",
        "options": {},
        "authentication": "predefinedCredentialType",
        "nodeCredentialType": "cloudflareApi"
      },
      "notesInFlow": true,
      "typeVersion": 4.1
    },
    {
      "id": "509c3878-e7b0-4a04-84a0-86b4c81db3b3",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1401,
        1460
      ],
      "parameters": {
        "color": 4,
        "width": 762.4679767633019,
        "height": 259,
        "content": "## Rename NM of KV (By Serach)\nto change parameters read [Docs](https://developers.cloudflare.com/api/operations/workers-kv-namespace-rename-a-namespace)"
      },
      "typeVersion": 1
    },
    {
      "id": "2f6a6158-f755-4ad5-a874-c08f2182e2bd",
      "name": "Delete KV1",
      "type": "n8n-nodes-base.httpRequest",
      "notes": "/storage/kv/namespaces/",
      "position": [
        2000,
        1540
      ],
      "parameters": {
        "url": "=https://api.cloudflare.com/client/v4/accounts/{{ $('Account Path').params[\"fields\"][\"values\"][0][\"stringValue\"] }}/storage/kv/namespaces/{{ $node[\"List KV-NMs (5)\"].json[\"result\"].find(kv => kv.title === $node[\"KV to Rename\"].json[\"Previous KV Name\"]).id }}",
        "method": "PUT",
        "options": {},
        "sendBody": true,
        "authentication": "predefinedCredentialType",
        "bodyParameters": {
          "parameters": [
            {
              "name": "title",
              "value": "={{ $('KV to Rename').item.json[\"New KV Name\"] }}"
            }
          ]
        },
        "nodeCredentialType": "cloudflareApi"
      },
      "notesInFlow": true,
      "typeVersion": 4.1
    },
    {
      "id": "466b9ec4-1ee6-46c9-ac52-65a9c9c942ba",
      "name": "KV to Rename",
      "type": "n8n-nodes-base.set",
      "position": [
        1440,
        1540
      ],
      "parameters": {
        "fields": {
          "values": [
            {
              "name": "Previous KV Name",
              "stringValue": "<Enter your previous Namespace name>"
            },
            {
              "name": "New KV Name",
              "stringValue": "<Enter your new Namespace name>"
            }
          ]
        },
        "options": {}
      },
      "typeVersion": 3.2
    },
    {
      "id": "f74468c5-235b-43f1-aa9a-544b5b8a6d3c",
      "name": "Account Path",
      "type": "n8n-nodes-base.set",
      "notes": "Required for all nodes",
      "position": [
        3000,
        920
      ],
      "parameters": {
        "fields": {
          "values": [
            {
              "name": "Account Path (account_identifier)",
              "stringValue": "65889d72a808df2e380018d87fffca5f"
            }
          ]
        },
        "options": {}
      },
      "notesInFlow": true,
      "typeVersion": 3.2
    },
    {
      "id": "32ffd694-52a3-4da5-b6f4-b4f7a17365cb",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2260,
        1184
      ],
      "parameters": {
        "color": 3,
        "width": 838.4149493375248,
        "height": 259,
        "content": "## Delete multiple KV pairs\nto change anything read [Docs](https://developers.cloudflare.com/api/operations/workers-kv-namespace-delete-multiple-key-value-pairs)"
      },
      "typeVersion": 1
    },
    {
      "id": "e90de48a-8d2b-4924-accc-6ef1a1448a95",
      "name": "Sticky Note5",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        460,
        460
      ],
      "parameters": {
        "color": 7,
        "width": 1264.141937886304,
        "height": 607,
        "content": "#  ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ **`Cloudflare Key-Value Full API integration Workflow`**\n[![Hetzner Cloud](https://developers.cloudflare.com/assets/kv-write-fdb5578b.svg)](https://www.hetzner.com/cloud)\n##  ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ _Integrate your N8N with CF KV Free instead of selfhosting Redis or any RAM based Storages!!_"
      },
      "typeVersion": 1
    },
    {
      "id": "5ca2dfda-2662-44ad-a4f5-3a036533eaac",
      "name": "Delete KVs inside NM",
      "type": "n8n-nodes-base.httpRequest",
      "notes": "Delete bulk Keys-Values inside select Namespace",
      "position": [
        2920,
        1284
      ],
      "parameters": {
        "url": "=https://api.cloudflare.com/client/v4/accounts/{{ $('Account Path').params[\"fields\"][\"values\"][0][\"stringValue\"] }}/storage/kv/namespaces/{{ $node[\"List KV-NMs (3)\"].json[\"result\"].find(kv => kv.title === $node[\"Set KV-NM Name (3)\"].json[\"NameSpace\"]).id }}/bulk",
        "method": "DELETE",
        "options": {},
        "jsonBody": "[   \"key1\",   \"key2\",   \"key3\" ]",
        "sendBody": true,
        "specifyBody": "json",
        "authentication": "predefinedCredentialType",
        "nodeCredentialType": "cloudflareApi"
      },
      "notesInFlow": true,
      "typeVersion": 4.1
    },
    {
      "id": "63d0419c-a031-41df-ab0b-89de6fe3459e",
      "name": "Sticky Note6",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2260,
        1464
      ],
      "parameters": {
        "color": 4,
        "width": 839.99463355761,
        "height": 257.7516694510983,
        "content": "## Write multiple KV pairs\nto change anything read [Docs](https://developers.cloudflare.com/api/operations/workers-kv-namespace-write-multiple-key-value-pairs)"
      },
      "typeVersion": 1
    },
    {
      "id": "689575b2-8dcf-4a6b-bedb-2aa1e1de48f7",
      "name": "Create KV-NM",
      "type": "n8n-nodes-base.httpRequest",
      "notes": "Create New Key-Value Namespace",
      "position": [
        560,
        1540
      ],
      "parameters": {
        "url": "=https://api.cloudflare.com/client/v4/accounts/{{ $('Account Path').params[\"fields\"][\"values\"][0][\"stringValue\"] }}/storage/kv/namespaces",
        "method": "POST",
        "options": {},
        "sendBody": true,
        "authentication": "predefinedCredentialType",
        "bodyParameters": {
          "parameters": [
            {
              "name": "title",
              "value": "<Enter Your Key-Value Namespace Here>"
            }
          ]
        },
        "nodeCredentialType": "cloudflareApi"
      },
      "notesInFlow": true,
      "typeVersion": 4.1
    },
    {
      "id": "e78616dc-bf3d-4913-a463-427d4b62c07b",
      "name": "Write KVs inside NM",
      "type": "n8n-nodes-base.httpRequest",
      "notes": "/storage/kv/namespaces/",
      "position": [
        2920,
        1560
      ],
      "parameters": {
        "url": "=https://api.cloudflare.com/client/v4/accounts/{{ $('Account Path').params[\"fields\"][\"values\"][0][\"stringValue\"] }}/storage/kv/namespaces/{{ $node[\"List KV-NMs (6)\"].json[\"result\"].find(kv => kv.title === $node[\"Set KV-NM Name (5)\"].json[\"NameSpace\"]).id }}/bulk",
        "method": "PUT",
        "options": {},
        "jsonBody": "=[{\n        \"key\": \"key1\",\n        \"value\": \"Value1\",\n        \"base64\": false,\n        \"expiration\": 1578435000,\n        \"expiration_ttl\": 300\n      },\n      {\n        \"key\": \"key2\",\n        \"value\": \"Value2\",\n        \"base64\": false,\n        \"expiration\": 1578435000,\n        \"expiration_ttl\": 300\n      },\n      {\n        \"key\": \"key3\",\n        \"value\": \"Value3\",\n        \"base64\": false,\n        \"expiration\": 1578435000,\n        \"expiration_ttl\": 300\n      }]",
        "sendBody": true,
        "sendHeaders": true,
        "specifyBody": "json",
        "authentication": "predefinedCredentialType",
        "headerParameters": {
          "parameters": [
            {
              "name": "Authorization",
              "value": "Bearer undefined"
            }
          ]
        },
        "nodeCredentialType": "cloudflareApi"
      },
      "notesInFlow": true,
      "typeVersion": 4.1
    },
    {
      "id": "d6843312-6186-475c-9a30-e8d913cb9b17",
      "name": "Sticky Note7",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2260,
        1747
      ],
      "parameters": {
        "color": 6,
        "width": 513,
        "height": 254.59230101092814,
        "content": "## List NM-Keys\nto change anything read [Docs](https://developers.cloudflare.com/api/operations/workers-kv-namespace-list-a-namespace'-s-keys)"
      },
      "typeVersion": 1
    },
    {
      "id": "1e444f44-4561-493d-b295-812f71e14385",
      "name": "-Get Keys inside NM",
      "type": "n8n-nodes-base.httpRequest",
      "notes": "Get Available Keys",
      "position": [
        2620,
        1840
      ],
      "parameters": {
        "url": "=https://api.cloudflare.com/client/v4/accounts/{{ $('Account Path').params[\"fields\"][\"values\"][0][\"stringValue\"] }}/storage/kv/namespaces/{{ $node[\"List KV-NMs (9)\"].json[\"result\"].find(kv => kv.title === $node[\"Set KV-NM Name (8)\"].json[\"NameSpace\"]).id }}/keys",
        "options": {},
        "jsonBody": "=[{\n        \"key\": \"key1\",\n        \"value\": \"Value1\",\n        \"base64\": false,\n        \"expiration\": 1578435000,\n        \"expiration_ttl\": 300\n      },\n      {\n        \"key\": \"key2\",\n        \"value\": \"Value2\",\n        \"base64\": false,\n        \"expiration\": 1578435000,\n        \"expiration_ttl\": 300\n      },\n      {\n        \"key\": \"key3\",\n        \"value\": \"Value3\",\n        \"base64\": false,\n        \"expiration\": 1578435000,\n        \"expiration_ttl\": 300\n      }]",
        "sendBody": true,
        "sendHeaders": true,
        "specifyBody": "json",
        "authentication": "predefinedCredentialType",
        "headerParameters": {
          "parameters": [
            {
              "name": "Authorization",
              "value": "Bearer undefined"
            }
          ]
        },
        "nodeCredentialType": "cloudflareApi"
      },
      "notesInFlow": true,
      "typeVersion": 4.1
    },
    {
      "id": "623e3bb7-8bb4-4da0-8434-c9472efee11a",
      "name": "Sticky Note8",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2240,
        1120
      ],
      "parameters": {
        "color": 7,
        "width": 878.0751770171937,
        "height": 920.8960116234484,
        "content": "##     ‌ ‌‌‌‌ ‌ ‌ ‌ ‌‌‌‌ ‌   Bulk Actions"
      },
      "typeVersion": 1
    },
    {
      "id": "dba1cfb6-207b-4938-ae95-7f9aaef1e85c",
      "name": "Sticky Note9",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1405,
        1740
      ],
      "parameters": {
        "color": 6,
        "width": 755.5520725546517,
        "height": 257.7516694510983,
        "content": "## Read MD in spesific key\nto change anything read [Docs](https://developers.cloudflare.com/api/operations/workers-kv-namespace-read-the-metadata-for-a-key)"
      },
      "typeVersion": 1
    },
    {
      "id": "0d02ba91-eebd-4dfd-8711-8060bfbbb0f5",
      "name": "Sticky Note10",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        480,
        1180
      ],
      "parameters": {
        "color": 3,
        "width": 828.445488674341,
        "height": 259,
        "content": "## Delete KV\nto change anything read [Docs](https://developers.cloudflare.com/api/operations/workers-kv-namespace-delete-key-value-pair)"
      },
      "typeVersion": 1
    },
    {
      "id": "89cde428-54c7-4f8f-b16c-5803ede6e015",
      "name": "Delete KV inside NM",
      "type": "n8n-nodes-base.httpRequest",
      "notes": "Delete selected KV in NM",
      "position": [
        1120,
        1280
      ],
      "parameters": {
        "url": "=https://api.cloudflare.com/client/v4/accounts/{{ $('Account Path').params[\"fields\"][\"values\"][0][\"stringValue\"] }}/storage/kv/namespaces/{{ $node[\"List KV-NMs (1)\"].json[\"result\"].find(kv => kv.title === $node[\"Set KV-NM Name (1)\"].json[\"NameSpace\"]).id }}/values/{{ $('Set KV-NM Name (1)').item.json['Key Name'] }}",
        "method": "DELETE",
        "options": {},
        "authentication": "predefinedCredentialType",
        "nodeCredentialType": "cloudflareApi"
      },
      "notesInFlow": true,
      "typeVersion": 4.1
    },
    {
      "id": "0a03189d-9a69-4c57-bac3-f5d92b6724e3",
      "name": "Sticky Note11",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        474,
        1740
      ],
      "parameters": {
        "color": 6,
        "width": 834.9104620941396,
        "height": 259,
        "content": "## Read KV\nto change anything read [Docs](https://developers.cloudflare.com/api/operations/workers-kv-namespace-read-key-value-pair)"
      },
      "typeVersion": 1
    },
    {
      "id": "71e7e9e3-57e6-43da-a90a-64aa79197769",
      "name": "Read Value Of KV In NM",
      "type": "n8n-nodes-base.httpRequest",
      "notes": "/storage/kv/namespaces/",
      "position": [
        1140,
        1840
      ],
      "parameters": {
        "url": "=https://api.cloudflare.com/client/v4/accounts/{{ $('Account Path').params[\"fields\"][\"values\"][0][\"stringValue\"] }}/storage/kv/namespaces/{{ $node[\"List KV-NMs (7)\"].json[\"result\"].find(kv => kv.title === $node[\"Set KV-NM Name (6)\"].json[\"NameSpace\"]).id }}/values/{{ $('Set KV-NM Name (6)').item.json['Key Name'] }}",
        "options": {
          "response": {
            "response": {
              "responseFormat": "text",
              "outputPropertyName": "={{ $('Set KV-NM Name (6)').item.json['Key Name'] }}"
            }
          }
        },
        "authentication": "predefinedCredentialType",
        "nodeCredentialType": "cloudflareApi"
      },
      "notesInFlow": true,
      "typeVersion": 4.1
    },
    {
      "id": "c0442be4-8a66-46d4-a158-f5d452270374",
      "name": "Sticky Note12",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        780,
        1460
      ],
      "parameters": {
        "color": 4,
        "width": 531.3495902609195,
        "height": 263.788476053995,
        "content": "## Write KV\nto change anything read [Docs](https://developers.cloudflare.com/api/operations/workers-kv-namespace-write-key-value-pair-with-metadata)"
      },
      "typeVersion": 1
    },
    {
      "id": "229dda34-b608-4dab-af3a-e81aaed1b8a5",
      "name": "Sticky Note13",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1375,
        1120
      ],
      "parameters": {
        "color": 7,
        "width": 817.7528311355856,
        "height": 917.7366431832784,
        "content": "##     ‌ ‌‌‌‌ ‌ ‌ ‌ Specific Actions"
      },
      "typeVersion": 1
    },
    {
      "id": "0b677885-bc87-4573-8d0b-02bfaaaf164e",
      "name": "Sticky Note14",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        461,
        1124
      ],
      "parameters": {
        "color": 7,
        "width": 876.5452405896403,
        "height": 913.7927070441785,
        "content": "##     ‌ ‌‌‌‌ ‌ ‌ ‌  ‌‌‌‌ ‌ ‌‌‌‌ ‌ ‌ ‌  ‌ ‌ Single Actions"
      },
      "typeVersion": 1
    },
    {
      "id": "500121cd-3ec5-4e3d-b3ad-de38f3733fc6",
      "name": "Sticky Note15",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1720,
        460
      ],
      "parameters": {
        "color": 7,
        "width": 1389.3461161034518,
        "height": 607,
        "content": "## This n8n template provides a seamless and efficient way to manage Key-Value (KV) pairs in Cloudflare's KV storage. all you need just take the part of action you want then use it with your workflow, keep in mind that the **_`Account Path`_** node is required for all actions as it's used to set the path of account, other authentication values is automatically set by n8n pre configured cloudflare api.\n ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌  ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌  ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌  ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌  ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌   ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌  ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌  ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌  ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌  ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌   ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌  ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌  ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌  ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌  ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌  ![Cloudflare Logo](https://cf-assets.www.cloudflare.com/slt3lc6tev37/7bIgGp4hk4SFO0o3SBbOKJ/546b2df59d9ef1ac226d70c40b17d019/Cloudflare-logo-transparent-v-rgb_thumbnail.png)\n\n\n# shortcuts:\n- ## **`NM`** or **`NMs`** =  _**`NameSpace/s`**_\n- ## **`KV`** or **`KVs`** = _**`Key/s - Value/s`**_\n- ## **`MD`** = _**`MetaData`**_"
      },
      "typeVersion": 1
    },
    {
      "id": "b65a6aab-08de-4217-b580-fd3afae16b47",
      "name": "Manual Trigger",
      "type": "n8n-nodes-base.manualTrigger",
      "notes": "Replace Me",
      "position": [
        2460,
        920
      ],
      "parameters": {},
      "notesInFlow": true,
      "typeVersion": 1
    },
    {
      "id": "197ca562-fc20-4cd6-8990-cd3e9e3d3b0d",
      "name": "List KV-NMs (1)",
      "type": "n8n-nodes-base.httpRequest",
      "notes": "Get Available Namespaces",
      "position": [
        820,
        1280
      ],
      "parameters": {
        "url": "=https://api.cloudflare.com/client/v4/accounts/{{ $json[\"Account Path (account_identifier)\"] }}/storage/kv/namespaces",
        "options": {},
        "sendQuery": true,
        "authentication": "predefinedCredentialType",
        "queryParameters": {
          "parameters": [
            {
              "name": "direction",
              "value": "asc"
            },
            {
              "name": "order",
              "value": "id"
            },
            {
              "name": "page",
              "value": "1"
            },
            {
              "name": "per_page",
              "value": "20"
            }
          ]
        },
        "nodeCredentialType": "cloudflareApi"
      },
      "notesInFlow": true,
      "typeVersion": 4.1
    },
    {
      "id": "64e26fad-eeab-4d04-b8ff-c42bb581a409",
      "name": "Set KV-NM Name (2)",
      "type": "n8n-nodes-base.set",
      "notes": "Set Key-Value Namespace for deleting",
      "position": [
        1440,
        1280
      ],
      "parameters": {
        "fields": {
          "values": [
            {
              "name": "NameSpace",
              "stringValue": "<Enter Your Key-Value Namespace Here>"
            }
          ]
        },
        "options": {}
      },
      "notesInFlow": true,
      "typeVersion": 3.2
    },
    {
      "id": "4a12fa4c-59df-4a27-bf94-59c5ccd05d40",
      "name": "Set KV-NM Name (1)",
      "type": "n8n-nodes-base.set",
      "notes": "Set Key-Value Namespace for deleting",
      "position": [
        560,
        1280
      ],
      "parameters": {
        "fields": {
          "values": [
            {
              "name": "NameSpace",
              "stringValue": "<Enter Your Key-Value Namespace Here>"
            },
            {
              "name": "Key Name",
              "stringValue": "<Enter Your Key Name Here>"
            }
          ]
        },
        "options": {}
      },
      "notesInFlow": true,
      "typeVersion": 3.2
    },
    {
      "id": "6f33a389-0b2e-4c9c-9cf5-38bfbf482f3b",
      "name": "Set KV-NM Name (3)",
      "type": "n8n-nodes-base.set",
      "notes": "Set Key-Value Namespace for Deleting",
      "position": [
        2320,
        1284
      ],
      "parameters": {
        "fields": {
          "values": [
            {
              "name": "NameSpace",
              "stringValue": "Set Key-Value Namespace for "
            }
          ]
        },
        "options": {}
      },
      "notesInFlow": true,
      "typeVersion": 3.2
    },
    {
      "id": "a9692d7c-f0bc-45c3-b99c-3c7a36d98f5c",
      "name": "List KV-NMs (2)",
      "type": "n8n-nodes-base.httpRequest",
      "notes": "Get Available Namespaces",
      "position": [
        1720,
        1280
      ],
      "parameters": {
        "url": "=https://api.cloudflare.com/client/v4/accounts/{{ $json[\"Account Path (account_identifier)\"] }}/storage/kv/namespaces",
        "options": {},
        "sendQuery": true,
        "authentication": "predefinedCredentialType",
        "queryParameters": {
          "parameters": [
            {
              "name": "direction",
              "value": "asc"
            },
            {
              "name": "order",
              "value": "id"
            },
            {
              "name": "page",
              "value": "1"
            },
            {
              "name": "per_page",
              "value": "20"
            }
          ]
        },
        "nodeCredentialType": "cloudflareApi"
      },
      "notesInFlow": true,
      "typeVersion": 4.1
    },
    {
      "id": "1c655d60-bcf8-42ee-a993-57b151789d44",
      "name": "List KV-NMs (3)",
      "type": "n8n-nodes-base.httpRequest",
      "notes": "Get Available Namespaces",
      "position": [
        2640,
        1284
      ],
      "parameters": {
        "url": "=https://api.cloudflare.com/client/v4/accounts/{{ $json[\"Account Path (account_identifier)\"] }}/storage/kv/namespaces",
        "options": {},
        "sendQuery": true,
        "authentication": "predefinedCredentialType",
        "queryParameters": {
          "parameters": [
            {
              "name": "direction",
              "value": "asc"
            },
            {
              "name": "order",
              "value": "id"
            },
            {
              "name": "page",
              "value": "1"
            },
            {
              "name": "per_page",
              "value": "20"
            }
          ]
        },
        "nodeCredentialType": "cloudflareApi"
      },
      "notesInFlow": true,
      "typeVersion": 4.1
    },
    {
      "id": "fdbbc7bc-9825-4882-a7ea-c30c2e1fb909",
      "name": "Set KV-NM Name (4)",
      "type": "n8n-nodes-base.set",
      "notes": "Set Key-Value Namespace for kv",
      "position": [
        840,
        1540
      ],
      "parameters": {
        "fields": {
          "values": [
            {
              "name": "NameSpace",
              "stringValue": "<Enter Your Key-Value Namespace Here>"
            },
            {
              "name": "Key Name",
              "stringValue": "<Enter Your Key-Value Name Here>"
            }
          ]
        },
        "options": {}
      },
      "notesInFlow": true,
      "typeVersion": 3.2
    },
    {
      "id": "b72a4e3e-60d6-4c31-9299-3d09c934d1c7",
      "name": "Write V & MD of KV In NM",
      "type": "n8n-nodes-base.httpRequest",
      "notes": "Put value with Metadata to NM key",
      "position": [
        1160,
        1540
      ],
      "parameters": {
        "url": "=https://api.cloudflare.com/client/v4/accounts/{{ $('Account Path').params[\"fields\"][\"values\"][0][\"stringValue\"] }}/storage/kv/namespaces/{{ $node[\"List KV-NMs (4)\"].json[\"result\"].find(kv => kv.title === $node[\"Set KV-NM Name (4)\"].json[\"NameSpace\"]).id }}/values/{{ $('Set KV-NM Name (4)').item.json['Key Name'] }}",
        "method": "PUT",
        "options": {},
        "sendBody": true,
        "contentType": "multipart-form-data",
        "authentication": "predefinedCredentialType",
        "bodyParameters": {
          "parameters": [
            {
              "name": "value",
              "value": "Some Value"
            },
            {
              "name": "metadata",
              "value": "{\"someMetadataKey\": \"someMetadataValue\"}"
            }
          ]
        },
        "nodeCredentialType": "cloudflareApi"
      },
      "notesInFlow": true,
      "typeVersion": 4.1
    },
    {
      "id": "143d7590-608c-4742-844d-0033b0066aab",
      "name": "Set KV-NM Name (5)",
      "type": "n8n-nodes-base.set",
      "position": [
        2320,
        1560
      ],
      "parameters": {
        "fields": {
          "values": [
            {
              "name": "NameSpace",
              "stringValue": "<Enter Your Key-Value Namespace Here>"
            }
          ]
        },
        "options": {}
      },
      "notesInFlow": false,
      "typeVersion": 3.2
    },
    {
      "id": "e6eb4b67-75e7-4264-a312-c66d21db947b",
      "name": "Set KV-NM Name (6)",
      "type": "n8n-nodes-base.set",
      "notes": "Set Key-Value Namespace",
      "position": [
        560,
        1840
      ],
      "parameters": {
        "fields": {
          "values": [
            {
              "name": "NameSpace",
              "stringValue": "<Enter Your Key-Value Namespace Here>"
            },
            {
              "name": "Key Name",
              "stringValue": "<Enter Your Key-Value Name Here>"
            }
          ]
        },
        "options": {}
      },
      "notesInFlow": true,
      "typeVersion": 3.2
    },
    {
      "id": "c2635c89-51a0-4a84-aa63-775f318fdc7a",
      "name": "List KV-NMs (4)",
      "type": "n8n-nodes-base.httpRequest",
      "notes": "Get Available Namespaces",
      "position": [
        1000,
        1540
      ],
      "parameters": {
        "url": "=https://api.cloudflare.com/client/v4/accounts/{{ $json[\"Account Path (account_identifier)\"] }}/storage/kv/namespaces",
        "options": {},
        "sendQuery": true,
        "authentication": "predefinedCredentialType",
        "queryParameters": {
          "parameters": [
            {
              "name": "direction",
              "value": "asc"
            },
            {
              "name": "order",
              "value": "id"
            },
            {
              "name": "page",
              "value": "1"
            },
            {
              "name": "per_page",
              "value": "20"
            }
          ]
        },
        "nodeCredentialType": "cloudflareApi"
      },
      "notesInFlow": true,
      "typeVersion": 4.1
    },
    {
      "id": "b0bcd87c-f19f-4e8f-8899-37676e66aa95",
      "name": "List KV-NMs (5)",
      "type": "n8n-nodes-base.httpRequest",
      "notes": "Get Available Namespaces",
      "position": [
        1720,
        1540
      ],
      "parameters": {
        "url": "=https://api.cloudflare.com/client/v4/accounts/{{ $json[\"Account Path (account_identifier)\"] }}/storage/kv/namespaces",
        "options": {},
        "sendQuery": true,
        "authentication": "predefinedCredentialType",
        "queryParameters": {
          "parameters": [
            {
              "name": "direction",
              "value": "asc"
            },
            {
              "name": "order",
              "value": "id"
            },
            {
              "name": "page",
              "value": "1"
            },
            {
              "name": "per_page",
              "value": "20"
            }
          ]
        },
        "nodeCredentialType": "cloudflareApi"
      },
      "notesInFlow": true,
      "typeVersion": 4.1
    },
    {
      "id": "50f41db8-62ba-4bb2-abc0-cecbce4bcd12",
      "name": "List KV-NMs (6)",
      "type": "n8n-nodes-base.httpRequest",
      "notes": "Get Available Namespaces",
      "position": [
        2640,
        1560
      ],
      "parameters": {
        "url": "=https://api.cloudflare.com/client/v4/accounts/{{ $json[\"Account Path (account_identifier)\"] }}/storage/kv/namespaces",
        "options": {},
        "sendQuery": true,
        "authentication": "predefinedCredentialType",
        "queryParameters": {
          "parameters": [
            {
              "name": "direction",
              "value": "asc"
            },
            {
              "name": "order",
              "value": "id"
            },
            {
              "name": "page",
              "value": "1"
            },
            {
              "name": "per_page",
              "value": "20"
            }
          ]
        },
        "nodeCredentialType": "cloudflareApi"
      },
      "notesInFlow": true,
      "typeVersion": 4.1
    },
    {
      "id": "00315620-0ed0-47df-bbd1-98a8a089a018",
      "name": "List KV-NMs (7)",
      "type": "n8n-nodes-base.httpRequest",
      "notes": "Get Available Namespaces",
      "position": [
        820,
        1840
      ],
      "parameters": {
        "url": "=https://api.cloudflare.com/client/v4/accounts/{{ $json[\"Account Path (account_identifier)\"] }}/storage/kv/namespaces",
        "options": {},
        "sendQuery": true,
        "authentication": "predefinedCredentialType",
        "queryParameters": {
          "parameters": [
            {
              "name": "direction",
              "value": "asc"
            },
            {
              "name": "order",
              "value": "id"
            },
            {
              "name": "page",
              "value": "1"
            },
            {
              "name": "per_page",
              "value": "20"
            }
          ]
        },
        "nodeCredentialType": "cloudflareApi"
      },
      "notesInFlow": true,
      "typeVersion": 4.1
    },
    {
      "id": "ecce1146-2562-4beb-8c88-b30158251999",
      "name": "List KV-NMs (8)",
      "type": "n8n-nodes-base.httpRequest",
      "notes": "Get Available Namespaces",
      "position": [
        1720,
        1840
      ],
      "parameters": {
        "url": "=https://api.cloudflare.com/client/v4/accounts/{{ $json[\"Account Path (account_identifier)\"] }}/storage/kv/namespaces",
        "options": {},
        "sendQuery": true,
        "authentication": "predefinedCredentialType",
        "queryParameters": {
          "parameters": [
            {
              "name": "direction",
              "value": "asc"
            },
            {
              "name": "order",
              "value": "id"
            },
            {
              "name": "page",
              "value": "1"
            },
            {
              "name": "per_page",
              "value": "20"
            }
          ]
        },
        "nodeCredentialType": "cloudflareApi"
      },
      "notesInFlow": true,
      "typeVersion": 4.1
    },
    {
      "id": "bcad9996-5d32-4367-8b81-618a3af70879",
      "name": "List KV-NMs (9)",
      "type": "n8n-nodes-base.httpRequest",
      "notes": "Get Available Namespaces",
      "position": [
        2460,
        1840
      ],
      "parameters": {
        "url": "=https://api.cloudflare.com/client/v4/accounts/{{ $json[\"Account Path (account_identifier)\"] }}/storage/kv/namespaces",
        "options": {},
        "sendQuery": true,
        "authentication": "predefinedCredentialType",
        "queryParameters": {
          "parameters": [
            {
              "name": "direction",
              "value": "asc"
            },
            {
              "name": "order",
              "value": "id"
            },
            {
              "name": "page",
              "value": "1"
            },
            {
              "name": "per_page",
              "value": "20"
            }
          ]
        },
        "nodeCredentialType": "cloudflareApi"
      },
      "notesInFlow": true,
      "typeVersion": 4.1
    },
    {
      "id": "64253d04-7ce4-4045-a41f-45faae2b6fd7",
      "name": "List KV-NMs (10)",
      "type": "n8n-nodes-base.httpRequest",
      "notes": "Get Available Namespaces",
      "position": [
        2900,
        1835
      ],
      "parameters": {
        "url": "=https://api.cloudflare.com/client/v4/accounts/{{ $json[\"Account Path (account_identifier)\"] }}/storage/kv/namespaces",
        "options": {},
        "sendQuery": true,
        "authentication": "predefinedCredentialType",
        "queryParameters": {
          "parameters": [
            {
              "name": "direction",
              "value": "asc"
            },
            {
              "name": "order",
              "value": "id"
            },
            {
              "name": "page",
              "value": "1"
            },
            {
              "name": "per_page",
              "value": "20"
            }
          ]
        },
        "nodeCredentialType": "cloudflareApi"
      },
      "notesInFlow": true,
      "typeVersion": 4.1
    },
    {
      "id": "66372c83-f593-4262-a0af-7902afa2d819",
      "name": "Set KV-NM Name (7)",
      "type": "n8n-nodes-base.set",
      "position": [
        1440,
        1840
      ],
      "parameters": {
        "fields": {
          "values": [
            {
              "name": "NameSpace",
              "stringValue": "<Enter Your Key-Value Namespace Here>"
            },
            {
              "name": "Key Name",
              "stringValue": "<Enter Your Key-Value Name Here>"
            }
          ]
        },
        "options": {}
      },
      "notesInFlow": false,
      "typeVersion": 3.2
    },
    {
      "id": "18f0e8c6-c1bb-4632-9333-7ca296333966",
      "name": "Set KV-NM Name (8)",
      "type": "n8n-nodes-base.set",
      "notes": "Set Key-Value Namespace",
      "position": [
        2300,
        1840
      ],
      "parameters": {
        "fields": {
          "values": [
            {
              "name": "NameSpace",
              "stringValue": "<Enter Your Key-Value Namespace Here>"
            }
          ]
        },
        "options": {}
      },
      "notesInFlow": true,
      "typeVersion": 3.2
    },
    {
      "id": "16f84be9-30b3-4664-9f9e-69b2ac961034",
      "name": "Read MD from Key",
      "type": "n8n-nodes-base.httpRequest",
      "notes": "/storage/kv/namespaces/",
      "position": [
        2000,
        1840
      ],
      "parameters": {
        "url": "=https://api.cloudflare.com/client/v4/accounts/{{ $('Account Path').params[\"fields\"][\"values\"][0][\"stringValue\"] }}/storage/kv/namespaces/{{ $node[\"List KV-NMs (8)\"].json[\"result\"].find(kv => kv.title === $node[\"Set KV-NM Name (7)\"].json[\"NameSpace\"]).id }}/metadata/{{ $('Set KV-NM Name (7)').item.json['Key Name'] }}",
        "options": {},
        "sendHeaders": true,
        "authentication": "predefinedCredentialType",
        "headerParameters": {
          "parameters": [
            {
              "name": "Authorization",
              "value": "Bearer undefined"
            }
          ]
        },
        "nodeCredentialType": "cloudflareApi"
      },
      "notesInFlow": true,
      "typeVersion": 4.1
    }
  ],
  "pinData": {},
  "connections": {
    "Account Path": {
      "main": [
        [
          {
            "node": "Set KV-NM Name (1)",
            "type": "main",
            "index": 0
          },
          {
            "node": "Create KV-NM",
            "type": "main",
            "index": 0
          },
          {
            "node": "Set KV-NM Name (6)",
            "type": "main",
            "index": 0
          },
          {
            "node": "Set KV-NM Name (2)",
            "type": "main",
            "index": 0
          },
          {
            "node": "KV to Rename",
            "type": "main",
            "index": 0
          },
          {
            "node": "Set KV-NM Name (7)",
            "type": "main",
            "index": 0
          },
          {
            "node": "Set KV-NM Name (3)",
            "type": "main",
            "index": 0
          },
          {
            "node": "Set KV-NM Name (5)",
            "type": "main",
            "index": 0
          },
          {
            "node": "Set KV-NM Name (8)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "KV to Rename": {
      "main": [
        [
          {
            "node": "List KV-NMs (5)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Manual Trigger": {
      "main": [
        [
          {
            "node": "Account Path",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "List KV-NMs (1)": {
      "main": [
        [
          {
            "node": "Delete KV inside NM",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "List KV-NMs (2)": {
      "main": [
        [
          {
            "node": "Delete KV",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "List KV-NMs (3)": {
      "main": [
        [
          {
            "node": "Delete KVs inside NM",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "List KV-NMs (4)": {
      "main": [
        [
          {
            "node": "Write V & MD of KV In NM",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "List KV-NMs (5)": {
      "main": [
        [
          {
            "node": "Delete KV1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "List KV-NMs (6)": {
      "main": [
        [
          {
            "node": "Write KVs inside NM",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "List KV-NMs (7)": {
      "main": [
        [
          {
            "node": "Read Value Of KV In NM",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "List KV-NMs (8)": {
      "main": [
        [
          {
            "node": "Read MD from Key",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "List KV-NMs (9)": {
      "main": [
        [
          {
            "node": "-Get Keys inside NM",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set KV-NM Name (1)": {
      "main": [
        [
          {
            "node": "List KV-NMs (1)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set KV-NM Name (2)": {
      "main": [
        [
          {
            "node": "List KV-NMs (2)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set KV-NM Name (3)": {
      "main": [
        [
          {
            "node": "List KV-NMs (3)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set KV-NM Name (4)": {
      "main": [
        [
          {
            "node": "List KV-NMs (4)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set KV-NM Name (5)": {
      "main": [
        [
          {
            "node": "List KV-NMs (6)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set KV-NM Name (6)": {
      "main": [
        [
          {
            "node": "List KV-NMs (7)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set KV-NM Name (7)": {
      "main": [
        [
          {
            "node": "List KV-NMs (8)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set KV-NM Name (8)": {
      "main": [
        [
          {
            "node": "List KV-NMs (9)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2450"></a>

## Template 2450 - Geração automática de keywords

- **Nome:** Geração automática de keywords
- **Descrição:** Recebe uma consulta via webhook, obtém sugestões de palavras-chave do Google, formata e limpa as sugestões, e retorna uma lista consolidada de keywords.
- **Funcionalidade:** • Recepção de consulta via webhook: Recebe o parâmetro de busca (q) enviado pelo cliente.
• Consulta ao serviço de sugestões: Envia a query ao serviço de autocomplete do Google para obter sugestões relacionadas.
• Conversão de resposta XML: Converte a resposta em XML para um formato estruturado legível.
• Separação de sugestões: Extrai cada sugestão individual da resposta estruturada.
• Limpeza e formatação: Normaliza os itens extraídos e organiza-os como um array de keywords.
• Agregação de resultados: Agrupa todas as keywords em uma única lista de saída.
• Resposta HTTP com keywords: Retorna todas as keywords coletadas ao solicitante na resposta do webhook.
• Instruções de uso embutidas: Nota com exemplo de URL local para testar o webhook (ex.: http://localhost:5678/webhook/76a63718-b3cb-4141-bc55-efa614d13f1d?q=keyword%20research).
- **Ferramentas:** • Google Autocomplete: Serviço de sugestões de pesquisa do Google usado para obter ideias de keywords com base na query fornecida.
• Endpoint HTTP/Webhook local: Ponto de entrada HTTP para receber a consulta do usuário e devolver os resultados (pode ser acessado via URL local para testes).



## Fluxo visual

```mermaid
flowchart LR
    N1["Split Out"]
    N2["Aggregate"]
    N3["Sticky Note"]
    N4["Receive Keyword"]
    N5["Autogenerate Keywords"]
    N6["Format Keywords"]
    N7["Clean Keywords"]
    N8["return Keywords"]
    N9["Sticky Note1"]

    N2 --> N8
    N1 --> N7
    N7 --> N2
    N6 --> N1
    N4 --> N5
    N5 --> N6
```

## Fluxo (.json) :

```json
{
  "meta": {
    "instanceId": "8eadf351d49a11e77d3a57adf374670f06c5294af8b1b7c86a1123340397e728"
  },
  "nodes": [
    {
      "id": "551a3a1f-07ad-48aa-bc9a-18f39c883929",
      "name": "Split Out",
      "type": "n8n-nodes-base.splitOut",
      "position": [
        940,
        180
      ],
      "parameters": {
        "options": {},
        "fieldToSplitOut": "toplevel.CompleteSuggestion"
      },
      "typeVersion": 1
    },
    {
      "id": "f451dc0d-a78d-4ba6-adcf-c1180502a904",
      "name": "Aggregate",
      "type": "n8n-nodes-base.aggregate",
      "position": [
        1260,
        180
      ],
      "parameters": {
        "options": {},
        "fieldsToAggregate": {
          "fieldToAggregate": [
            {
              "fieldToAggregate": "Keywords"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "id": "ccad69b0-7f88-490e-bfbd-50ef702f48ce",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        350.13991769547397,
        134.716049382716
      ],
      "parameters": {
        "color": 4,
        "width": 1323.884773662551,
        "height": 224.79012345679018,
        "content": "* Generating keywords for your SEO"
      },
      "typeVersion": 1
    },
    {
      "id": "9ed26e36-e05a-416e-a517-3f5d07718256",
      "name": "Receive Keyword",
      "type": "n8n-nodes-base.webhook",
      "position": [
        400,
        180
      ],
      "webhookId": "76a63718-b3cb-4141-bc55-efa614d13f1d",
      "parameters": {
        "path": "76a63718-b3cb-4141-bc55-efa614d13f1d",
        "options": {},
        "responseMode": "lastNode"
      },
      "typeVersion": 1.1
    },
    {
      "id": "51aa0811-7f31-4476-9460-4eacad81e469",
      "name": "Autogenerate Keywords",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        600,
        180
      ],
      "parameters": {
        "url": "=https://google.com/complete/search?output=toolbar&gl=US&q={{ $json.query.q }}",
        "options": {}
      },
      "typeVersion": 4.1
    },
    {
      "id": "f3bd360c-bf72-4e5f-92ec-ca08c8e4daed",
      "name": "Format Keywords",
      "type": "n8n-nodes-base.xml",
      "position": [
        760,
        180
      ],
      "parameters": {
        "options": {}
      },
      "typeVersion": 1
    },
    {
      "id": "17bef508-47e1-482b-8dc1-aeb1f6faca63",
      "name": "Clean Keywords",
      "type": "n8n-nodes-base.set",
      "position": [
        1100,
        180
      ],
      "parameters": {
        "options": {
          "ignoreConversionErrors": true
        },
        "assignments": {
          "assignments": [
            {
              "id": "fb95058f-0c20-4249-8a45-7b935fde1874",
              "name": "Keywords",
              "type": "array",
              "value": "={{ $json.suggestion.data }}"
            }
          ]
        }
      },
      "typeVersion": 3.3
    },
    {
      "id": "81e3ced0-d3b7-4019-a6a7-5e940ad33df1",
      "name": "return Keywords",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        1440,
        180
      ],
      "parameters": {
        "options": {},
        "respondWith": "allIncomingItems"
      },
      "typeVersion": 1
    },
    {
      "id": "fafc57a6-64e1-4463-bbf0-c9dccd880345",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        360,
        380
      ],
      "parameters": {
        "width": 767.7695473251028,
        "content": "* If you are using this one, just copy the this webhook url http://localhost:5678/webhook/76a63718-b3cb-4141-bc55-efa614d13f1d?q=keyword%20research\n* All you need is to change the keyword to e your desired keyword and you will be good to go\n\n* You can use the keyword with a space and the results will be the same"
      },
      "typeVersion": 1
    }
  ],
  "pinData": {},
  "connections": {
    "Aggregate": {
      "main": [
        [
          {
            "node": "return Keywords",
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
            "node": "Clean Keywords",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Clean Keywords": {
      "main": [
        [
          {
            "node": "Aggregate",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Format Keywords": {
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
    "Receive Keyword": {
      "main": [
        [
          {
            "node": "Autogenerate Keywords",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Autogenerate Keywords": {
      "main": [
        [
          {
            "node": "Format Keywords",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2451"></a>

## Template 2451 - Notificação por email de nova release do GitHub

- **Nome:** Notificação por email de nova release do GitHub
- **Descrição:** Busca diariamente a última release de um repositório no GitHub, converte o texto da release de Markdown para HTML e envia esse conteúdo por email.
- **Funcionalidade:** • Agendamento diário: inicia a execução do fluxo automaticamente em uma base diária.
• Requisição à API do repositório: obtém a release mais recente do repositório configurado no endpoint de releases.
• Extração do conteúdo da release: isola o campo de descrição (body) da release retornada.
• Conversão de Markdown para HTML: transforma o texto em Markdown da release para HTML pronto para email.
• Envio de email com conteúdo HTML: envia a versão HTML da release para o endereço configurado, com assunto predefinido e opção de atribuição no envio.
- **Ferramentas:** • GitHub API: fornece os dados da release mais recente do repositório através do endpoint de releases.
• Gmail: serviço de email utilizado para enviar a notificação com o conteúdo HTML.

## Fluxo visual

```mermaid
flowchart LR
    N1["Send Gmail"]
    N2["Fetch Github Repo Releases"]
    N3["Split Out Content"]
    N4["Convert Markdown to HTML"]
    N5["Daily Trigger"]
    N6["Sticky Note"]
    N7["Sticky Note1"]

    N5 --> N2
    N3 --> N4
    N4 --> N1
    N2 --> N3
```

## Fluxo (.json) :

```json
{
  "meta": {
    "instanceId": "84ba6d895254e080ac2b4916d987aa66b000f88d4d919a6b9c76848f9b8a7616",
    "templateId": "2278",
    "templateCredsSetupCompleted": true
  },
  "nodes": [
    {
      "id": "4074dda0-993b-4b63-8502-3db09a920e42",
      "name": "Send Gmail",
      "type": "n8n-nodes-base.gmail",
      "position": [
        1520,
        260
      ],
      "parameters": {
        "sendTo": "nico@n8n.io",
        "message": "={{ $json.html }}",
        "options": {
          "appendAttribution": true
        },
        "subject": "new stable version of n8n released"
      },
      "credentials": {
        "gmailOAuth2": {
          "id": "nx3IJyQ7TuVxI0y2",
          "name": "Gmail account"
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "01364110-5482-416f-abab-32ddbb9c3123",
      "name": "Fetch Github Repo Releases",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        840,
        260
      ],
      "parameters": {
        "url": "https://api.github.com/repos/n8n-io/n8n/releases/latest",
        "options": {}
      },
      "typeVersion": 4.2
    },
    {
      "id": "fb96efc1-e615-4378-80c5-1ddafff3a4e8",
      "name": "Split Out Content",
      "type": "n8n-nodes-base.splitOut",
      "position": [
        1080,
        260
      ],
      "parameters": {
        "options": {},
        "fieldToSplitOut": "body"
      },
      "typeVersion": 1
    },
    {
      "id": "ca540fee-a2dc-4780-95d1-6a0a5b8dc6fa",
      "name": "Convert Markdown to HTML",
      "type": "n8n-nodes-base.markdown",
      "position": [
        1260,
        260
      ],
      "parameters": {
        "mode": "markdownToHtml",
        "options": {},
        "markdown": "={{ $json.body }}",
        "destinationKey": "html"
      },
      "typeVersion": 1
    },
    {
      "id": "e0e74830-bb7b-4b1f-9a1e-e7eb01a5cecb",
      "name": "Daily Trigger",
      "type": "n8n-nodes-base.scheduleTrigger",
      "position": [
        580,
        260
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
      "id": "d90f0d15-de3b-4997-9a36-f6ee08d5aea2",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        740,
        160
      ],
      "parameters": {
        "width": 288,
        "height": 300,
        "content": "Change **url** for Github Repo here"
      },
      "typeVersion": 1
    },
    {
      "id": "f3b1af79-9946-4588-bae9-839f712a7d12",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1440,
        160
      ],
      "parameters": {
        "width": 288,
        "height": 300,
        "content": "Change **to Email** here"
      },
      "typeVersion": 1
    }
  ],
  "pinData": {},
  "connections": {
    "Daily Trigger": {
      "main": [
        [
          {
            "node": "Fetch Github Repo Releases",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Split Out Content": {
      "main": [
        [
          {
            "node": "Convert Markdown to HTML",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Convert Markdown to HTML": {
      "main": [
        [
          {
            "node": "Send Gmail",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Fetch Github Repo Releases": {
      "main": [
        [
          {
            "node": "Split Out Content",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2453"></a>

## Template 2453 - Assistente Telegram para transcrição e gestão de tarefas

- **Nome:** Assistente Telegram para transcrição e gestão de tarefas
- **Descrição:** Recebe mensagens e notas de voz do Telegram, transcreve áudio, processa com um agente de IA que pode criar/atualizar tarefas e responde ao usuário no Telegram.
- **Funcionalidade:** • Recepção de mensagens Telegram: monitora e inicia o fluxo ao receber mensagens privadas (texto ou voz).
• Detecção de notas de voz: identifica mensagens de voz e as separa do fluxo de texto.
• Download de áudio: baixa o arquivo de voz a partir do identificador enviado pelo Telegram.
• Transcrição de áudio: converte áudio para texto usando o serviço de transcrição.
• Preparação da entrada para IA: formata e envia o texto transcrito ou texto original como entrada para o agente de IA, incluindo identificação do usuário.
• Agente de IA com contexto e memória: utiliza um modelo de conversa com janela de memória por sessão para manter contexto e instruções sistêmicas.
• Chamadas a ferramentas remotas via MCP: permite que o agente solicite ações (criar, listar, atualizar tarefas) a um servidor de ferramentas através de um cliente MCP.
• Gerenciamento de tarefas: cria tarefas em listas designadas (hoje e próximas), obtém listas de tarefas e marca tarefas como concluídas usando IDs apropriados.
• Envio de resposta ao usuário: formata a saída do agente e envia a mensagem de volta ao chat do Telegram.
- **Ferramentas:** • Telegram: plataforma de mensagens usada para receber textos e notas de voz e para enviar respostas ao usuário.
• OpenAI: fornece o modelo de linguagem para conversação (gpt-4o-mini) e o serviço de transcrição de áudio.
• Google Tasks: serviço de gerenciamento de tarefas usado para criar, listar e atualizar tarefas do usuário.
• Serviço MCP (ai.gatuservices.info): endpoint SSE/cliente para executar ferramentas remotas solicitadas pelo agente de IA (orquestração de operações sobre tarefas).

## Fluxo visual

```mermaid
flowchart LR
    N1["Incoming Message"]
    N2["MCP Server Trigger"]
    N3["AI Agent"]
    N4["MCP Client"]
    N5["OpenAI Chat Model"]
    N6["Simple Memory"]
    N7["chatInput"]
    N8["create_todays_task"]
    N9["chatOutput"]
    N10["sendMessage"]
    N11["create_upcoming_task"]
    N12["complete_task"]
    N13["get_todays_tasks"]
    N14["get_upcoming_tasks"]
    N15["Switch"]
    N16["audio_id"]
    N17["download_audio"]
    N18["transcribeAudio"]
    N19["audioInput"]
    N20["Sticky Note"]
    N21["Sticky Note1"]

    N15 --> N16
    N15 --> N7
    N3 --> N9
    N16 --> N17
    N7 --> N3
    N19 --> N3
    N9 --> N10
    N17 --> N18
    N18 --> N19
    N1 --> N15
```

## Fluxo (.json) :

```json
{
  "meta": {
    "instanceId": "be27b2af86ae3a5dc19ef2a1947644c0aec45fd8c88f29daa7dea6f0ce537691",
    "templateCredsSetupCompleted": true
  },
  "nodes": [
    {
      "id": "ca8b122d-1739-4377-ac99-e20dd2341342",
      "name": "Incoming Message",
      "type": "n8n-nodes-base.telegramTrigger",
      "position": [
        -1020,
        -320
      ],
      "webhookId": "75921955-c8ed-4ff6-8de2-e436c6bbe69d",
      "parameters": {
        "updates": [
          "message"
        ],
        "additionalFields": {}
      },
      "credentials": {
        "telegramApi": {
          "id": "ayMpCvQ69GjrbPdP",
          "name": "gatu_pa_bot"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "68f7568b-e677-454b-a1e8-6c07a05e7570",
      "name": "MCP Server Trigger",
      "type": "@n8n/n8n-nodes-langchain.mcpTrigger",
      "position": [
        -860,
        240
      ],
      "webhookId": "562ffc95-cf8e-4d4d-8f5b-29b3ff22d5ee",
      "parameters": {
        "path": "562ffc95-cf8e-4d4d-8f5b-29b3ff22d5ee"
      },
      "typeVersion": 1
    },
    {
      "id": "635b8ecc-0f50-477d-8e19-631f868e30f6",
      "name": "AI Agent",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        340,
        -320
      ],
      "parameters": {
        "options": {
          "systemMessage": "=You are a helpful assistant. Whenever askes to update a task, call the get_tasks tools first to retrieve the appropriate task ids then use that to update the tasks.\n\nToday's date: {{ $now }}\n"
        }
      },
      "typeVersion": 1.8
    },
    {
      "id": "ab7740dc-bac2-4044-8317-40d90252d992",
      "name": "MCP Client",
      "type": "@n8n/n8n-nodes-langchain.mcpClientTool",
      "position": [
        540,
        -100
      ],
      "parameters": {
        "sseEndpoint": "https://ai.gatuservices.info/mcp/562ffc95-cf8e-4d4d-8f5b-29b3ff22d5ee/sse"
      },
      "typeVersion": 1
    },
    {
      "id": "5298eee0-747a-496a-a3a2-e395f7c1caa1",
      "name": "OpenAI Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        300,
        -100
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
          "id": "lcpI0YZU9bebg3uW",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "c5b7e10d-2d7c-403c-bcb5-a10033252f97",
      "name": "Simple Memory",
      "type": "@n8n/n8n-nodes-langchain.memoryBufferWindow",
      "position": [
        420,
        -100
      ],
      "parameters": {
        "sessionKey": "={{ $('Incoming Message').item.json.message.from.id }}",
        "sessionIdType": "customKey",
        "contextWindowLength": 20
      },
      "typeVersion": 1.3
    },
    {
      "id": "06d2e8c8-3912-45cd-a074-4eea27c2e5eb",
      "name": "chatInput",
      "type": "n8n-nodes-base.set",
      "position": [
        80,
        -220
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "ab70dc2d-35d0-4742-988f-ed7077633467",
              "name": "chatInput",
              "type": "string",
              "value": "={{ $json.message.text }}"
            },
            {
              "id": "6439fc2c-dc2d-41fc-b8a3-b33ef80d2878",
              "name": "id",
              "type": "number",
              "value": "={{ $json.message.from.id }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "a9309816-8c1d-435c-ad49-2e45053718c1",
      "name": "create_todays_task",
      "type": "n8n-nodes-base.googleTasksTool",
      "position": [
        -1020,
        460
      ],
      "parameters": {
        "task": "MDg2MzM1OTA5NzI0NzUzNjUwNjc6MDow",
        "title": "={{ /*n8n-auto-generated-fromAI-override*/ $fromAI('Title', `Title summary of the task to be done`, 'string') }}",
        "additionalFields": {
          "notes": "={{ /*n8n-auto-generated-fromAI-override*/ $fromAI('Notes', `Detailed description of the task`, 'string') }}",
          "dueDate": "={{ /*n8n-auto-generated-fromAI-override*/ $fromAI('Due_Date', `Date the task should be completed`, 'string') }}",
          "completed": "={{ /*n8n-auto-generated-fromAI-override*/ $fromAI('Completion_Date', `Date the task was completed`, 'string') }}"
        }
      },
      "credentials": {
        "googleTasksOAuth2Api": {
          "id": "8sBGA2BWJuF6SObU",
          "name": "Connected Account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "ad6cfc1a-7094-434a-98d1-a6f030067091",
      "name": "chatOutput",
      "type": "n8n-nodes-base.set",
      "position": [
        740,
        -320
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "df6bd510-e63f-41b1-b5b4-d2c612d5b8d0",
              "name": "chatOutput",
              "type": "string",
              "value": "={{ $json.output }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "e342066f-3cf8-4926-94df-798e831226be",
      "name": "sendMessage",
      "type": "n8n-nodes-base.telegram",
      "position": [
        960,
        -320
      ],
      "webhookId": "c5eb133f-338f-4918-8e49-83ac339d841b",
      "parameters": {
        "text": "={{ $json.chatOutput }}",
        "chatId": "={{ $('Incoming Message').item.json.message.chat.id }}",
        "additionalFields": {
          "appendAttribution": false,
          "disable_notification": false
        }
      },
      "credentials": {
        "telegramApi": {
          "id": "ayMpCvQ69GjrbPdP",
          "name": "gatu_pa_bot"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "e4a1bc16-549f-46a2-92a8-a06e6023089c",
      "name": "create_upcoming_task",
      "type": "n8n-nodes-base.googleTasksTool",
      "position": [
        -900,
        460
      ],
      "parameters": {
        "task": "OFVvNlh6ZmhScHVvNll4dw",
        "title": "={{ /*n8n-auto-generated-fromAI-override*/ $fromAI('Title', `Title summary of the task to be done`, 'string') }}",
        "additionalFields": {
          "notes": "={{ /*n8n-auto-generated-fromAI-override*/ $fromAI('Notes', `Detailed description of the task`, 'string') }}",
          "dueDate": "={{ /*n8n-auto-generated-fromAI-override*/ $fromAI('Due_Date', `Date the task should be completed`, 'string') }}",
          "completed": "={{ /*n8n-auto-generated-fromAI-override*/ $fromAI('Completion_Date', `Date the task was completed`, 'string') }}"
        }
      },
      "credentials": {
        "googleTasksOAuth2Api": {
          "id": "8sBGA2BWJuF6SObU",
          "name": "Connected Account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "df71bb02-016d-4d56-b80d-404a60c0e7cf",
      "name": "complete_task",
      "type": "n8n-nodes-base.googleTasksTool",
      "position": [
        -780,
        460
      ],
      "parameters": {
        "task": "RS1rbkNCS2JsdVFnVl80cg",
        "taskId": "={{ /*n8n-auto-generated-fromAI-override*/ $fromAI('Task_ID', `The task id tom be marked as completed. Get it from the get tasks tool`, 'string') }}",
        "operation": "update",
        "updateFields": {}
      },
      "credentials": {
        "googleTasksOAuth2Api": {
          "id": "8sBGA2BWJuF6SObU",
          "name": "Connected Account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "a33812bd-986e-4762-87a0-199ff8a7c9aa",
      "name": "get_todays_tasks",
      "type": "n8n-nodes-base.googleTasksTool",
      "position": [
        -660,
        460
      ],
      "parameters": {
        "task": "MDg2MzM1OTA5NzI0NzUzNjUwNjc6MDow",
        "operation": "getAll",
        "returnAll": true,
        "additionalFields": {}
      },
      "credentials": {
        "googleTasksOAuth2Api": {
          "id": "8sBGA2BWJuF6SObU",
          "name": "Connected Account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "dcb3a6c9-5d7c-4fe6-8b52-f07cf74cfa0c",
      "name": "get_upcoming_tasks",
      "type": "n8n-nodes-base.googleTasksTool",
      "position": [
        -540,
        460
      ],
      "parameters": {
        "task": "OFVvNlh6ZmhScHVvNll4dw",
        "operation": "getAll",
        "returnAll": true,
        "additionalFields": {}
      },
      "credentials": {
        "googleTasksOAuth2Api": {
          "id": "8sBGA2BWJuF6SObU",
          "name": "Connected Account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "ce63c24a-ce2f-4e06-8ae5-7de75540d438",
      "name": "Switch",
      "type": "n8n-nodes-base.switch",
      "position": [
        -800,
        -320
      ],
      "parameters": {
        "rules": {
          "values": [
            {
              "outputKey": "Voice Note",
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
                    "id": "8415cc8d-65a2-448e-a106-1ceb54634dfd",
                    "operator": {
                      "type": "object",
                      "operation": "exists",
                      "singleValue": true
                    },
                    "leftValue": "={{ $json.message.voice }}",
                    "rightValue": ""
                  }
                ]
              },
              "renameOutput": true
            }
          ]
        },
        "options": {
          "fallbackOutput": "extra"
        }
      },
      "typeVersion": 3.2
    },
    {
      "id": "a58488c3-38b8-4492-9f13-a900c7697812",
      "name": "audio_id",
      "type": "n8n-nodes-base.set",
      "position": [
        -580,
        -420
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "eb7f5d62-e4f3-4b4e-9f1b-6c329feafb3e",
              "name": "file_id",
              "type": "string",
              "value": "={{ $json.message.voice.file_id }}"
            },
            {
              "id": "803031b8-6b21-47fa-b339-ad674ccbbb1e",
              "name": "file_unique_id",
              "type": "string",
              "value": "={{ $json.message.voice.file_unique_id }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "83c2ecae-b601-4669-b820-b5c35d3f936e",
      "name": "download_audio",
      "type": "n8n-nodes-base.telegram",
      "position": [
        -360,
        -420
      ],
      "webhookId": "c2dbc0eb-0f3a-4f11-9525-804bd5bef4b1",
      "parameters": {
        "fileId": "={{ $json.file_id }}",
        "resource": "file"
      },
      "credentials": {
        "telegramApi": {
          "id": "ayMpCvQ69GjrbPdP",
          "name": "gatu_pa_bot"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "4a496e3a-2e3a-4ce0-9344-192847de1760",
      "name": "transcribeAudio",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "position": [
        -140,
        -420
      ],
      "parameters": {
        "options": {},
        "resource": "audio",
        "operation": "transcribe"
      },
      "credentials": {
        "openAiApi": {
          "id": "lcpI0YZU9bebg3uW",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1.8
    },
    {
      "id": "38b6aa37-d279-4b1b-be42-7f7cc1bbe688",
      "name": "audioInput",
      "type": "n8n-nodes-base.set",
      "position": [
        80,
        -420
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "d57b4fc2-10f7-46cd-a89c-0021a92f41d1",
              "name": "chatInput",
              "type": "string",
              "value": "={{ $json.text }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "e524f12f-205f-4fc8-b2f0-b308ec4066b7",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -1060,
        -500
      ],
      "parameters": {
        "color": 4,
        "width": 2180,
        "height": 540,
        "content": "## Main Function to Receive and Send Telegram Messages\n"
      },
      "typeVersion": 1
    },
    {
      "id": "709b252a-b5e8-4c7e-8bcd-a7092d588070",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -1060,
        140
      ],
      "parameters": {
        "color": 3,
        "width": 640,
        "height": 480,
        "content": "## MCP Server to Carry Out Actions"
      },
      "typeVersion": 1
    }
  ],
  "pinData": {
    "Incoming Message": [
      {
        "message": {
          "chat": {
            "id": 6043747866,
            "type": "private",
            "first_name": "Gatu"
          },
          "date": 1745294191,
          "from": {
            "id": 6043747866,
            "is_bot": false,
            "first_name": "Gatu",
            "language_code": "en"
          },
          "voice": {
            "file_id": "AwACAgQAAxkBAAMYaAcTb6Sm3bpJ_8Cc2q1q4vC7MLYAAg8ZAAJAOjlQQhWQOxUBqfU2BA",
            "duration": 2,
            "file_size": 9854,
            "mime_type": "audio/ogg",
            "file_unique_id": "AgADDxkAAkA6OVA"
          },
          "message_id": 24
        },
        "update_id": 656804764
      }
    ]
  },
  "connections": {
    "Switch": {
      "main": [
        [
          {
            "node": "audio_id",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "chatInput",
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
            "node": "chatOutput",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "audio_id": {
      "main": [
        [
          {
            "node": "download_audio",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "chatInput": {
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
    "MCP Client": {
      "ai_tool": [
        [
          {
            "node": "AI Agent",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "audioInput": {
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
    "chatOutput": {
      "main": [
        [
          {
            "node": "sendMessage",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Simple Memory": {
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
    "complete_task": {
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
    "download_audio": {
      "main": [
        [
          {
            "node": "transcribeAudio",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "transcribeAudio": {
      "main": [
        [
          {
            "node": "audioInput",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Incoming Message": {
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
    "get_todays_tasks": {
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
    "create_todays_task": {
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
    "get_upcoming_tasks": {
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
    "create_upcoming_task": {
      "ai_tool": [
        [
          {
            "node": "MCP Server Trigger",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2454"></a>

## Template 2454 - Triagem automática de e-mails com IA

- **Nome:** Triagem automática de e-mails com IA
- **Descrição:** Automatiza a triagem de mensagens da caixa de entrada, arquivando e rotulando e-mails com base em decisões tomadas por um agente de IA e reportando o resultado via Telegram.
- **Funcionalidade:** • Gatilho por Telegram: Inicia a execução do fluxo ao receber um comando ou mensagem via Telegram.
• Recuperação de e-mails: Busca todas as mensagens presentes na caixa de entrada do Gmail.
• Filtragem de processados: Ignora e-mails que já receberam rótulos de processamento para evitar reprocessamento.
• Classificação por IA: Para cada e-mail, um agente de IA decide se deve ser arquivado ou receber um rótulo específico com base em regras definidas.
• Ações no Gmail: Executa operações no Gmail para remover o rótulo INBOX (arquivar) ou adicionar rótulos conforme a decisão da IA.
• Agregação de resultados: Consolida os resultados do processamento de múltiplos e-mails.
• Relatório para usuário: Envia um resumo do processamento ao usuário via Telegram.
- **Ferramentas:** • Gmail: Armazenamento e gestão de e-mails; usado para recuperar mensagens e aplicar/remover rótulos (arquivar).
• Telegram: Interface de acionamento e entrega de relatórios ao usuário.
• OpenRouter (modelo GPT-4.1-nano): Serviço de modelo de linguagem usado para categorizar e-mails e gerar o relatório de resumo.

## Fluxo visual

```mermaid
flowchart LR
    N1["When clicking ‘Test workflow’"]
    N2["OpenRouter Chat Model"]
    N3["Telegram Trigger"]
    N4["Sticky Note"]
    N5["Sticky Note1"]
    N6["Sticky Note2"]
    N7["Sticky Note3"]
    N8["Sticky Note4"]
    N9["mail_label_setter"]
    N10["mail_archiver"]
    N11["Aggregate"]
    N12["Telegram"]
    N13["OpenRouter Chat Model1"]
    N14["Reporter"]
    N15["Get mails in INBOX"]
    N16["Filter processed"]
    N17["Categoriser"]

    N14 --> N12
    N11 --> N14
    N17 --> N11
    N16 --> N17
    N3 --> N15
    N15 --> N16
    N1 --> N15
```

## Fluxo (.json) :

```json
{
  "meta": {
    "instanceId": "6af2f94153ea0551e6264b16187490bd4c4739c7f5f3d7adab90c5cf186e22a1",
    "templateCredsSetupCompleted": true
  },
  "nodes": [
    {
      "id": "43e68fe1-7f48-4bc9-b19a-66d39bee5bbd",
      "name": "When clicking ‘Test workflow’",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        -520,
        20
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "32aa401a-60c3-4436-94d5-5ba09d3be6ae",
      "name": "OpenRouter Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenRouter",
      "position": [
        80,
        0
      ],
      "parameters": {
        "model": "openai/gpt-4.1-nano",
        "options": {}
      },
      "credentials": {
        "openRouterApi": {
          "id": "eQmkAlMDYm8oEtBL",
          "name": "OpenRouter account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "f6d325b4-ff87-4bba-9f27-b68590c8a533",
      "name": "Telegram Trigger",
      "type": "n8n-nodes-base.telegramTrigger",
      "position": [
        -520,
        -220
      ],
      "webhookId": "e61d3286-920e-406c-b787-d330cf897ef4",
      "parameters": {
        "updates": [
          "message"
        ],
        "additionalFields": {}
      },
      "credentials": {
        "telegramApi": {
          "id": "ZOl2ZojetuN1uFiX",
          "name": "My Mail Agent Bot via Telegram"
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "8e10c622-9bf8-414b-8364-185c5c4808a0",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -600,
        -480
      ],
      "parameters": {
        "width": 1660,
        "height": 680,
        "content": "## Mail Agent\nFor emails in the inbox, archive those that are completely unnecessary, and label the rest based on their relevance.\n\n"
      },
      "typeVersion": 1
    },
    {
      "id": "2e664cd4-37af-4b8f-84a5-ff07911b8aaa",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -560,
        -380
      ],
      "parameters": {
        "color": 5,
        "width": 180,
        "height": 360,
        "content": "### Trigger\nRun by communicating with Telegram"
      },
      "typeVersion": 1
    },
    {
      "id": "966af8d0-bfca-40fa-b97c-ec1bb7de82d2",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -360,
        -380
      ],
      "parameters": {
        "color": 4,
        "width": 180,
        "height": 360,
        "content": "### Get Mail via Gmail\nRetrieve all emails in the Gmail inbox.\n(Inbox = Label: INBOX)"
      },
      "typeVersion": 1
    },
    {
      "id": "07dabeda-a075-4e45-9ecf-9a0e6d0df0b2",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -160,
        -380
      ],
      "parameters": {
        "color": 4,
        "width": 180,
        "height": 360,
        "content": "### Filter\nFilter out emails that have already been processed to avoid unnecessary work for the AI.\n\n"
      },
      "typeVersion": 1
    },
    {
      "id": "b9a96646-283e-4328-8c79-57befa97bb69",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        40,
        -380
      ],
      "parameters": {
        "color": 3,
        "width": 980,
        "height": 540,
        "content": "### AI Agent\nCheck each email one by one, categorize them as necessary or unnecessary according to the provided prompt, and instruct Gmail to apply the appropriate labels."
      },
      "typeVersion": 1
    },
    {
      "id": "32c73c57-61b5-430b-a011-f0b44fa2b226",
      "name": "mail_label_setter",
      "type": "n8n-nodes-base.gmailTool",
      "position": [
        360,
        0
      ],
      "webhookId": "37bb94d2-6aeb-4038-afc7-e25a330e7860",
      "parameters": {
        "labelIds": "={{ /*n8n-auto-generated-fromAI-override*/ $fromAI('Label_Names_or_IDs', ``, 'string') }}",
        "messageId": "={{ /*n8n-auto-generated-fromAI-override*/ $fromAI('Message_ID', ``, 'string') }}",
        "operation": "addLabels"
      },
      "credentials": {
        "gmailOAuth2": {
          "id": "5GhcPqZ48DrfujWd",
          "name": "Gmail account"
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "7cf38850-939c-4c8e-af62-1f730d5b7e34",
      "name": "mail_archiver",
      "type": "n8n-nodes-base.gmailTool",
      "position": [
        220,
        0
      ],
      "webhookId": "81956225-38dd-4acf-b97a-8e68f332f56a",
      "parameters": {
        "labelIds": [
          "INBOX"
        ],
        "messageId": "={{ /*n8n-auto-generated-fromAI-override*/ $fromAI('Message_ID', ``, 'string') }}",
        "operation": "removeLabels"
      },
      "credentials": {
        "gmailOAuth2": {
          "id": "5GhcPqZ48DrfujWd",
          "name": "Gmail account"
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "5fab497e-a632-4565-8048-7ae9b209728d",
      "name": "Aggregate",
      "type": "n8n-nodes-base.aggregate",
      "position": [
        380,
        -220
      ],
      "parameters": {
        "options": {},
        "aggregate": "aggregateAllItemData"
      },
      "typeVersion": 1
    },
    {
      "id": "f7144884-6ba6-4e97-be35-f5f8b27d56ad",
      "name": "Telegram",
      "type": "n8n-nodes-base.telegram",
      "position": [
        820,
        -220
      ],
      "webhookId": "6324ebbf-b2c3-42c3-b4ee-849184380b4f",
      "parameters": {
        "text": "={{ $json.output }}",
        "chatId": "={{ $('Telegram Trigger').item.json.message.chat.id }}",
        "additionalFields": {}
      },
      "credentials": {
        "telegramApi": {
          "id": "ZOl2ZojetuN1uFiX",
          "name": "My Mail Agent Bot via Telegram"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "9236fbc1-ffad-4bf0-b3a1-5d389e5b422c",
      "name": "OpenRouter Chat Model1",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenRouter",
      "position": [
        520,
        0
      ],
      "parameters": {
        "model": "openai/gpt-4.1-nano",
        "options": {}
      },
      "credentials": {
        "openRouterApi": {
          "id": "eQmkAlMDYm8oEtBL",
          "name": "OpenRouter account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "e0ec10ca-ad72-4784-891e-5bd5bcff7082",
      "name": "Reporter",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        520,
        -220
      ],
      "parameters": {
        "text": "=Summarize data\n```\n{{ $json.data.map(item => item.output + '\\n\\n') }}\n```\n",
        "options": {
          "systemMessage": "=# persona\n* You are a helpful assistant.\n"
        },
        "promptType": "define"
      },
      "typeVersion": 1.8
    },
    {
      "id": "9b4f8e14-7b9c-45b3-97cb-32f2fe756440",
      "name": "Get mails in INBOX",
      "type": "n8n-nodes-base.gmail",
      "position": [
        -320,
        -220
      ],
      "webhookId": "f4c95906-916d-4c94-8e35-cb37c9472043",
      "parameters": {
        "filters": {
          "labelIds": [
            "INBOX"
          ]
        },
        "operation": "getAll",
        "returnAll": true
      },
      "credentials": {
        "gmailOAuth2": {
          "id": "5GhcPqZ48DrfujWd",
          "name": "Gmail account"
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "13088de9-6f96-463e-bcb6-92f97d7144d9",
      "name": "Filter processed",
      "type": "n8n-nodes-base.filter",
      "position": [
        -120,
        -220
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
              "id": "1091eba0-3d75-47b6-92c5-404f93e263ae",
              "operator": {
                "type": "array",
                "operation": "notContains",
                "rightType": "any"
              },
              "leftValue": "={{ $json.labels.map(item => item.name)}}",
              "rightValue": "NotNeed"
            },
            {
              "id": "31160689-98ce-43ac-8c7b-116cd7da5ebc",
              "operator": {
                "type": "array",
                "operation": "notContains",
                "rightType": "any"
              },
              "leftValue": "={{ $json.labels.map(item => item.name)}}",
              "rightValue": "MustRead"
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "317ea413-e8fd-4148-8115-8b4d2b9a7fe4",
      "name": "Categoriser",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        80,
        -220
      ],
      "parameters": {
        "text": "=<task>\nProcess mail\n</task>\n<mail>\n<id>{{ $json.id }}</id>\n<from>{{ $json.From }}</from>\n<subject>{{ $json.Subject }}</subject>\n<body>{{ $json.snippet }}</body>\n</mail>",
        "options": {
          "systemMessage": "=<persona>\nYou are an email processing assistant.\n</persona>\n<task>\nLook at the content of the email and decide whether to apply a label or archive it, processing it only once. First, archive those that are absolutely unnecessary using the mail_archiver tool. This judgment is the top priority. After that, if it does not fall into that category, determine whether it should be read based on the following criteria and use the mail_label_setter tool to apply the label.\n<case>Absolutely unnecessary: Archive using the mail_archiver tool</case>\n<case>Needs to be read: Apply \"Label_[label_id]\" using the mail_label_setter tool</case>\n<case>Other: Apply \"Label_[label_id]\" using the mail_label_setter tool</case>\nReport the processing results carefully.\n</task>\n<rules>\n<Archive>\nEmails that are absolutely unnecessary and will be archived\n<item>[list up your rule1]</item>\n<item>[list up your rule2]</item>\n</Archive><MustRead>\nEmails that need to be read\n<item>[list up your rule1]</item>\n<item>[list up your rule2]</item>\n</MustRead>\n<Other>\nEmails that are not necessary to read but will not be archived\n<item>[list up your rule1]</item>\n<item>[list up your rule2]</item>\n</Other>\n</rules>"
        },
        "promptType": "define"
      },
      "typeVersion": 1.7
    }
  ],
  "pinData": {},
  "connections": {
    "Reporter": {
      "main": [
        [
          {
            "node": "Telegram",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Aggregate": {
      "main": [
        [
          {
            "node": "Reporter",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Categoriser": {
      "main": [
        [
          {
            "node": "Aggregate",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "mail_archiver": {
      "ai_tool": [
        [
          {
            "node": "Categoriser",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Filter processed": {
      "main": [
        [
          {
            "node": "Categoriser",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Telegram Trigger": {
      "main": [
        [
          {
            "node": "Get mails in INBOX",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "mail_label_setter": {
      "ai_tool": [
        [
          {
            "node": "Categoriser",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Get mails in INBOX": {
      "main": [
        [
          {
            "node": "Filter processed",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenRouter Chat Model": {
      "ai_languageModel": [
        [
          {
            "node": "Categoriser",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "OpenRouter Chat Model1": {
      "ai_languageModel": [
        [
          {
            "node": "Reporter",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "When clicking ‘Test workflow’": {
      "main": [
        [
          {
            "node": "Get mails in INBOX",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2456"></a>

## Template 2456 - Responder e criar tickets/itens a partir de mensagens do Telegram

- **Nome:** Responder e criar tickets/itens a partir de mensagens do Telegram
- **Descrição:** Ao receber uma mensagem no Telegram, o fluxo verifica se contém a palavra 'refund', cria um ticket no Freshdesk com a tag adequada, envia uma resposta automática ao usuário e registra um item no Monday.com.
- **Funcionalidade:** • Recepção de mensagens via Telegram: inicia o fluxo quando chega uma mensagem de usuário.
• Detecção de palavra-chave 'refund': classifica a mensagem em duas trilhas (reembolso ou reclamação) conforme o conteúdo.
• Criação de ticket no Freshdesk: gera um ticket usando o texto da mensagem como assunto e adiciona a tag 'refund' ou 'complaint' conforme o caso.
• Resposta automática ao remetente: envia mensagens pré-definidas confirmando recebimento do pedido de reembolso ou da reclamação.
• Registro em Monday.com: cria um item no board especificado; para reembolsos o item usa o assunto do ticket, para demais mensagens usa o texto original e insere em grupos distintos (new_group ou topics).
- **Ferramentas:** • Telegram: plataforma de mensagens usada para receber as mensagens dos usuários e enviar respostas automáticas.
• Freshdesk: sistema de suporte ao cliente utilizado para criar tickets com tags e assuntos baseados nas mensagens.
• Monday.com: ferramenta de gestão de trabalho usada para criar itens em um board específico e organizá-los em grupos.

## Fluxo visual

```mermaid
flowchart LR
    N1["Telegram Trigger"]
    N2["Monday.com"]
    N3["Monday.com1"]
    N4["Telegram"]
    N5["IF1"]
    N6["Freshdesk"]
    N7["Freshdesk1"]
    N8["Telegram1"]

    N5 --> N6
    N5 --> N7
    N4 --> N2
    N6 --> N4
    N8 --> N3
    N7 --> N8
    N1 --> N5
```

## Fluxo (.json) :

```json
{
  "nodes": [
    {
      "name": "Telegram Trigger",
      "type": "n8n-nodes-base.telegramTrigger",
      "position": [
        0,
        250
      ],
      "parameters": {
        "updates": [
          "message"
        ]
      },
      "credentials": {
        "telegramApi": "Telegram"
      },
      "typeVersion": 1
    },
    {
      "name": "Monday.com",
      "type": "n8n-nodes-base.mondayCom",
      "position": [
        650,
        150
      ],
      "parameters": {
        "name": "={{$node[\"Freshdesk\"].json[\"subject\"]}}",
        "boardId": "565971708",
        "groupId": "new_group",
        "resource": "boardItem",
        "additionalFields": {}
      },
      "credentials": {
        "mondayComApi": "Monday"
      },
      "typeVersion": 1
    },
    {
      "name": "Monday.com1",
      "type": "n8n-nodes-base.mondayCom",
      "position": [
        650,
        350
      ],
      "parameters": {
        "name": "={{$node[\"Telegram Trigger\"].json[\"message\"][\"text\"]}}",
        "boardId": "565971708",
        "groupId": "topics",
        "resource": "boardItem",
        "additionalFields": {}
      },
      "credentials": {
        "mondayComApi": "Monday"
      },
      "typeVersion": 1
    },
    {
      "name": "Telegram",
      "type": "n8n-nodes-base.telegram",
      "position": [
        500,
        150
      ],
      "parameters": {
        "text": "Hi, thanks for sending this. We will review your request for refund as soon as possible 💶 💵 💷",
        "chatId": "={{$node[\"Telegram Trigger\"].json[\"message\"][\"chat\"][\"id\"]}}",
        "additionalFields": {}
      },
      "credentials": {
        "telegramApi": "Telegram"
      },
      "typeVersion": 1
    },
    {
      "name": "IF1",
      "type": "n8n-nodes-base.if",
      "position": [
        180,
        250
      ],
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$node[\"Telegram Trigger\"].json[\"message\"][\"text\"]}}",
              "value2": "refund",
              "operation": "contains"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Freshdesk",
      "type": "n8n-nodes-base.freshdesk",
      "position": [
        350,
        150
      ],
      "parameters": {
        "options": {
          "tags": "refund",
          "subject": "={{$node[\"IF1\"].json[\"message\"][\"text\"]}}"
        },
        "requester": "email",
        "requesterIdentificationValue": ""
      },
      "credentials": {
        "freshdeskApi": "Freshdesk"
      },
      "typeVersion": 1
    },
    {
      "name": "Freshdesk1",
      "type": "n8n-nodes-base.freshdesk",
      "position": [
        350,
        350
      ],
      "parameters": {
        "options": {
          "tags": "complaint",
          "subject": "={{$node[\"IF1\"].json[\"message\"][\"text\"]}}"
        },
        "requester": "email",
        "requesterIdentificationValue": ""
      },
      "credentials": {
        "freshdeskApi": "Freshdesk"
      },
      "typeVersion": 1
    },
    {
      "name": "Telegram1",
      "type": "n8n-nodes-base.telegram",
      "position": [
        500,
        350
      ],
      "parameters": {
        "text": "Hi, thanks for sending this. We will review your complaint as soon as possible 📬 ☀️ ✅",
        "chatId": "={{$node[\"Telegram Trigger\"].json[\"message\"][\"chat\"][\"id\"]}}",
        "additionalFields": {}
      },
      "credentials": {
        "telegramApi": "Telegram"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "IF1": {
      "main": [
        [
          {
            "node": "Freshdesk",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Freshdesk1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Telegram": {
      "main": [
        [
          {
            "node": "Monday.com",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Freshdesk": {
      "main": [
        [
          {
            "node": "Telegram",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Telegram1": {
      "main": [
        [
          {
            "node": "Monday.com1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Freshdesk1": {
      "main": [
        [
          {
            "node": "Telegram1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Telegram Trigger": {
      "main": [
        [
          {
            "node": "IF1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2458"></a>

## Template 2458 - Enviar feeds RSS para Telegram

- **Nome:** Enviar feeds RSS para Telegram
- **Descrição:** Verifica periodicamente feeds RSS do Weibo e Instagram, detecta novos itens e envia o conteúdo apropriado para chats do Telegram, tratando imagens e evitando duplicados.
- **Funcionalidade:** • Verificação periódica: checa os feeds RSS a cada minuto.
• Leitura de feeds: obtém itens dos feeds do Weibo e Instagram a partir de um serviço RSS.
• Processamento por lotes: processa itens um por vez para controlar o fluxo de envio.
• Detecção de duplicados: armazena o último link processado por feed e impede repostagens do mesmo item.
• Extração de imagens: analisa o conteúdo HTML do item, extrai URLs de imagens e conta quantas existem.
• Envio condicional para Telegram: se houver exatamente uma imagem envia como foto com legenda; caso contrário envia uma mensagem de texto com link e sem pré-visualização.
• Suporte a múltiplos canais: envia conteúdos para chats/grupos diferentes conforme a origem (Weibo / Instagram).
• Uso de legenda: utiliza o contentSnippet do item como legenda ou corpo da mensagem.
- **Ferramentas:** • RSSHub (instância hospedada no Heroku): fornece as versões RSS dos perfis de Instagram e Weibo usados como fonte.
• Telegram Bot API: realiza o envio de fotos e mensagens para os chats/grupos especificados.

## Fluxo visual

```mermaid
flowchart LR
    N1["SplitInBatches"]
    N2["Function"]
    N3["Cron1"]
    N4["是否重复"]
    N5["写入图片的属性"]
    N6["图片数量判断"]
    N7["一张图片"]
    N8["其他状况"]
    N9["NaN"]
    N10["SplitInBatches1"]
    N11["Function1"]
    N12["IF"]
    N13["IF1"]
    N14["send"]
    N15["instagram rss"]
    N16["weibo rss"]
    N17["Telegram"]
    N18["test"]

    N12 --> N9
    N13 --> N14
    N13 --> N17
    N9 --> N13
    N18 --> N15
    N18 --> N16
    N3 --> N16
    N3 --> N15
    N2 --> N4
    N11 --> N12
    N16 --> N1
    N4 --> N5
    N15 --> N10
    N1 --> N2
    N10 --> N11
    N6 --> N7
    N6 --> N8
    N5 --> N6
```

## Fluxo (.json) :

```json
{
  "id": "3",
  "name": "rss-telegram",
  "nodes": [
    {
      "name": "SplitInBatches",
      "type": "n8n-nodes-base.splitInBatches",
      "position": [
        480,
        220
      ],
      "parameters": {
        "batchSize": 1
      },
      "typeVersion": 1
    },
    {
      "name": "Function",
      "type": "n8n-nodes-base.function",
      "position": [
        610,
        220
      ],
      "parameters": {
        "functionCode": "const staticData = getWorkflowStaticData('global');\n\n// Access its data\nconst oldlink = staticData.oldlink;\n\nitems[0].json.oldlink = oldlink || \"\";\n\n// Update its data\nstaticData.oldlink = items[0].json.link;\n\nreturn items;"
      },
      "typeVersion": 1
    },
    {
      "name": "Cron1",
      "type": "n8n-nodes-base.cron",
      "position": [
        180,
        290
      ],
      "parameters": {
        "triggerTimes": {
          "item": [
            {
              "mode": "everyMinute"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "是否重复",
      "type": "n8n-nodes-base.if",
      "notes": "判断链接是否相同",
      "position": [
        750,
        220
      ],
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$node[\"Function\"].data[\"oldlink\"]}}",
              "value2": "={{$node[\"Function\"].data[\"link\"]}}"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "写入图片的属性",
      "type": "n8n-nodes-base.function",
      "position": [
        910,
        220
      ],
      "parameters": {
        "functionCode": "function imgList(items) {\n  let imgReg = /<img.*?(?:>|/>)/gi //匹配图片中的img标签\n  let srcReg = /src=[\\'\\\"]?([^\\'\\\"]*)[\\'\\\"]?/i // 匹配图片中的src\n  let str = items[0].json.content\n  let arr = str.match(imgReg)  //筛选出所有的img\n  let srcArr = []\n  if(arr !== null){\n     for (let i = 0; i < arr.length; i++) {\n          let src = arr[i].match(srcReg)\n          // 获取图片地址\n          srcArr.push(src[1])\n      }\n        items[0].json.arrlength = arr.length;\n        items[0].json.imgList = srcArr;\n   } else {\n        items[0].json.arrlength = 0;\n   }\n   \n }\nimgList(items)\nreturn items;"
      },
      "typeVersion": 1
    },
    {
      "name": "图片数量判断",
      "type": "n8n-nodes-base.if",
      "position": [
        1060,
        220
      ],
      "parameters": {
        "conditions": {
          "number": [
            {
              "value1": "={{$node[\"写入图片的属性\"].data[\"arrlength\"]}}",
              "value2": 1,
              "operation": "equal"
            }
          ],
          "string": [],
          "boolean": []
        }
      },
      "typeVersion": 1
    },
    {
      "name": "一张图片",
      "type": "n8n-nodes-base.telegram",
      "position": [
        1270,
        80
      ],
      "parameters": {
        "file": "={{$node[\"图片数量判断\"].data[\"imgList\"][0]}}",
        "chatId": "-1001314058276",
        "operation": "sendPhoto",
        "additionalFields": {
          "caption": "={{$node[\"图片数量判断\"].data[\"contentSnippet\"]}}"
        }
      },
      "credentials": {
        "telegramApi": "lataimei"
      },
      "typeVersion": 1
    },
    {
      "name": "其他状况",
      "type": "n8n-nodes-base.telegram",
      "notes": "无图片",
      "position": [
        1270,
        230
      ],
      "parameters": {
        "text": "={{$node[\"图片数量判断\"].data[\"contentSnippet\"]}} {{$node[\"图片数量判断\"].data[\"link\"]}}",
        "chatId": "-1001314058276",
        "additionalFields": {
          "parse_mode": "HTML",
          "disable_web_page_preview": true
        }
      },
      "credentials": {
        "telegramApi": "lataimei"
      },
      "typeVersion": 1
    },
    {
      "name": "NaN",
      "type": "n8n-nodes-base.function",
      "position": [
        910,
        370
      ],
      "parameters": {
        "functionCode": "function imgList(items) {\n  let imgReg = /<img.*?(?:>|/>)/gi //匹配图片中的img标签\n  let srcReg = /src=[\\'\\\"]?([^\\'\\\"]*)[\\'\\\"]?/i // 匹配图片中的src\n  let str = items[0].json.content\n  let arr = str.match(imgReg)  //筛选出所有的img\n  let srcArr = []\n  if(arr !== null){\n     for (let i = 0; i < arr.length; i++) {\n          let src = arr[i].match(srcReg)\n          // 获取图片地址\n          srcArr.push(src[1])\n      }\n        items[0].json.arrlength = arr.length;\n        items[0].json.imgList = srcArr;\n   } else {\n        items[0].json.arrlength = 0;\n   }\n   \n }\nimgList(items)\nreturn items;"
      },
      "typeVersion": 1
    },
    {
      "name": "SplitInBatches1",
      "type": "n8n-nodes-base.splitInBatches",
      "position": [
        480,
        370
      ],
      "parameters": {
        "batchSize": 1
      },
      "typeVersion": 1
    },
    {
      "name": "Function1",
      "type": "n8n-nodes-base.function",
      "position": [
        610,
        370
      ],
      "parameters": {
        "functionCode": "const staticData = getWorkflowStaticData('global');\n\n// Access its data\nconst tsaioldlink = staticData.tsaioldlink;\n\nitems[0].json.tsaioldlink = tsaioldlink || \"\";\n\n// Update its data\nstaticData.tsaioldlink = items[0].json.link;\n\nreturn items;"
      },
      "typeVersion": 1
    },
    {
      "name": "IF",
      "type": "n8n-nodes-base.if",
      "position": [
        750,
        370
      ],
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$node[\"Function1\"].data[\"tsaioldlink\"]}}",
              "value2": "={{$node[\"Function1\"].data[\"link\"]}}"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "IF1",
      "type": "n8n-nodes-base.if",
      "position": [
        1060,
        370
      ],
      "parameters": {
        "conditions": {
          "number": [
            {
              "value1": 1,
              "value2": "=0",
              "operation": "equal"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "send",
      "type": "n8n-nodes-base.telegram",
      "notes": "无图片",
      "position": [
        1270,
        380
      ],
      "parameters": {
        "file": "={{$node[\"IF1\"].data[\"imgList\"][0]}}",
        "chatId": "-1001499587010",
        "operation": "sendPhoto",
        "additionalFields": {
          "caption": "={{$node[\"IF1\"].data[\"contentSnippet\"]}}"
        }
      },
      "credentials": {
        "telegramApi": "lataimei"
      },
      "typeVersion": 1
    },
    {
      "name": "instagram rss",
      "type": "n8n-nodes-base.rssFeedRead",
      "position": [
        360,
        370
      ],
      "parameters": {
        "url": "=https://rsshub985.herokuapp.com/instagram/user/tsai_ingwen/"
      },
      "typeVersion": 1
    },
    {
      "name": "weibo rss",
      "type": "n8n-nodes-base.rssFeedRead",
      "position": [
        360,
        220
      ],
      "parameters": {
        "url": "=https://rsshub985.herokuapp.com/weibo/user/5721376081"
      },
      "typeVersion": 1
    },
    {
      "name": "Telegram",
      "type": "n8n-nodes-base.telegram",
      "position": [
        1270,
        530
      ],
      "parameters": {
        "file": "={{$node[\"IF1\"].data[\"imgList\"][0]}}",
        "chatId": "-1001499587010",
        "operation": "sendPhoto",
        "additionalFields": {
          "caption": "={{$node[\"IF1\"].data[\"contentSnippet\"]}} {{$node[\"IF1\"].data[\"link\"]}}"
        }
      },
      "credentials": {
        "telegramApi": "lataimei"
      },
      "typeVersion": 1
    },
    {
      "name": "test",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        180,
        130
      ],
      "parameters": {},
      "typeVersion": 1
    }
  ],
  "active": true,
  "settings": {},
  "connections": {
    "IF": {
      "main": [
        [],
        [
          {
            "node": "NaN",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "IF1": {
      "main": [
        [
          {
            "node": "send",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Telegram",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "NaN": {
      "main": [
        [
          {
            "node": "IF1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "test": {
      "main": [
        [
          {
            "node": "instagram rss",
            "type": "main",
            "index": 0
          },
          {
            "node": "weibo rss",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Cron1": {
      "main": [
        [
          {
            "node": "weibo rss",
            "type": "main",
            "index": 0
          },
          {
            "node": "instagram rss",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Function": {
      "main": [
        [
          {
            "node": "是否重复",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Function1": {
      "main": [
        [
          {
            "node": "IF",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "weibo rss": {
      "main": [
        [
          {
            "node": "SplitInBatches",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "是否重复": {
      "main": [
        [],
        [
          {
            "node": "写入图片的属性",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "instagram rss": {
      "main": [
        [
          {
            "node": "SplitInBatches1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "SplitInBatches": {
      "main": [
        [
          {
            "node": "Function",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "SplitInBatches1": {
      "main": [
        [
          {
            "node": "Function1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "图片数量判断": {
      "main": [
        [
          {
            "node": "一张图片",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "其他状况",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "写入图片的属性": {
      "main": [
        [
          {
            "node": "图片数量判断",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2461"></a>

## Template 2461 - Gerar post e imagem a partir de mensagem Telegram

- **Nome:** Gerar post e imagem a partir de mensagem Telegram
- **Descrição:** Escuta mensagens do Telegram (voz ou texto), transcreve áudios quando necessário, pesquisa o tema, gera conteúdo otimizado para redes sociais e cria uma imagem baseada num prompt detalhado.
- **Funcionalidade:** • Receber mensagens do Telegram: Inicia o fluxo ao detectar mensagens de usuários.
• Identificar tipo de mensagem: Diferencia automaticamente entre mensagens de voz e texto.
• Fazer download de mensagens de voz: Busca o arquivo de áudio enviado pelo usuário.
• Transcrever áudio para texto: Converte mensagens de voz em texto usando serviço de transcrição.
• Preparar entrada para IA: Formata o texto transcrito ou recebido para processamento posterior.
• Pesquisa web automatizada: Realiza pesquisa do tema usando um serviço de busca para obter dados e contexto.
• Gerar conteúdo social otimizado: Cria um post engajador, claro e otimizado para SEO com tamanho definido.
• Criar prompt de imagem detalhado: Gera um prompt fotorealista e específico para ferramentas de geração de imagem.
• Gerar imagem a partir do prompt: Envia o prompt a um serviço de geração de imagem e recebe o resultado.
• Montar saída final: Empacota o conteúdo criado e a imagem gerada para envio ou uso posterior.
- **Ferramentas:** • Telegram: Plataforma de mensagens usada para receber textos e áudios dos usuários.
• OpenAI: Serviço utilizado para transcrição de áudio e para geração de texto/diálogo com modelos de linguagem.
• SerpAPI: Ferramenta de pesquisa na web usada para obter informações e contexto sobre o tema.
• Hugging Face / Stable Diffusion (inference): Serviço de inferência para gerar imagens fotorealistas a partir do prompt produzido.



## Fluxo visual

```mermaid
flowchart LR
    N1["Receive Telegram Messages"]
    N2["Voice or Text?"]
    N3["Fetch Voice Message"]
    N4["Transcribe Voice to Text"]
    N5["Prepare for LLM"]
    N6["Sticky Note2"]
    N7["Sticky Note3"]
    N8["AI Agent"]
    N9["OpenAI Chat Model"]
    N10["SerpAPI"]
    N11["Structured Output Parser"]
    N12["Extract from File"]
    N13["Sticky Note"]
    N14["Prepare Final Output"]
    N15["Generate Image"]
    N16["Sticky Note1"]

    N8 --> N15
    N15 --> N12
    N2 --> N3
    N2 --> N5
    N5 --> N8
    N12 --> N14
    N3 --> N4
    N4 --> N8
    N1 --> N2
```

## Fluxo (.json) :

```json
{
  "meta": {
    "instanceId": "b41148c809c7896d124743d940fc0964703e540af66564ef95e25a4ceea61c77",
    "templateCredsSetupCompleted": true
  },
  "nodes": [
    {
      "id": "070fd7b4-58ca-4372-a347-6f60f590e20b",
      "name": "Receive Telegram Messages",
      "type": "n8n-nodes-base.telegramTrigger",
      "position": [
        40,
        140
      ],
      "webhookId": "4e2cd560-ae4e-4ed7-a8ea-984518404e51",
      "parameters": {
        "updates": [
          "message"
        ],
        "additionalFields": {}
      },
      "credentials": {
        "telegramApi": {
          "id": "lff3pLERRdQmkmeV",
          "name": "Telegram account"
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "0e0f3a32-fbde-42a9-aa7f-70fda7b05357",
      "name": "Voice or Text?",
      "type": "n8n-nodes-base.switch",
      "position": [
        400,
        220
      ],
      "parameters": {
        "rules": {
          "values": [
            {
              "outputKey": "Audio",
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
                    "id": "af30c479-4542-405f-b315-37c50c4e2bef",
                    "operator": {
                      "type": "string",
                      "operation": "exists",
                      "singleValue": true
                    },
                    "leftValue": "={{ $json.message.voice.file_id }}",
                    "rightValue": ""
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "Text",
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
                    "id": "a3ca8cd4-fbb2-40b5-829a-24724f2fbc85",
                    "operator": {
                      "type": "string",
                      "operation": "exists",
                      "singleValue": true
                    },
                    "leftValue": "={{ $json.message.text || \"\" }}",
                    "rightValue": ""
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "Error",
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
                    "id": "9bcfdee0-2f09-4037-a7b9-689ef392371d",
                    "operator": {
                      "type": "string",
                      "operation": "exists",
                      "singleValue": true
                    },
                    "leftValue": "error",
                    "rightValue": ""
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
      "id": "b01dde88-bede-4500-974f-b2dc203ff841",
      "name": "Fetch Voice Message",
      "type": "n8n-nodes-base.telegram",
      "position": [
        760,
        120
      ],
      "webhookId": "23645237-4943-4c32-b18c-97c410cc3409",
      "parameters": {
        "fileId": "={{ $json.message.voice.file_id }}",
        "resource": "file"
      },
      "credentials": {
        "telegramApi": {
          "id": "lff3pLERRdQmkmeV",
          "name": "Telegram account"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "fe91414e-3b10-482e-b8dd-d55266828dd7",
      "name": "Transcribe Voice to Text",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "position": [
        980,
        120
      ],
      "parameters": {
        "options": {},
        "resource": "audio",
        "operation": "translate"
      },
      "credentials": {
        "openAiApi": {
          "id": "uFPD9I4pWJ4xUVf7",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1.8
    },
    {
      "id": "74549458-fd4d-4824-a561-944f2f536b9b",
      "name": "Prepare for LLM",
      "type": "n8n-nodes-base.set",
      "position": [
        880,
        340
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "b324a329-3c49-4f7f-b683-74331b7fe7f8",
              "name": "=text",
              "type": "string",
              "value": "={{$json.message.text}}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "886246ad-7127-462a-a2b2-b4281f369d8b",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -40,
        0
      ],
      "parameters": {
        "width": 260,
        "height": 320,
        "content": " \n**This workflow listens for incoming voice or text messages from Telegram users.** "
      },
      "typeVersion": 1
    },
    {
      "id": "d052bd49-dc23-4ec5-b153-a9eb305f0641",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        700,
        20
      ],
      "parameters": {
        "width": 460,
        "height": 260,
        "content": " **Voice messages are fetched from Telegram and transcribed into text using OpenAI's Whisper API.**  "
      },
      "typeVersion": 1
    },
    {
      "id": "156580f1-adf5-43ba-b54d-89b84ca87818",
      "name": "AI Agent",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        1460,
        320
      ],
      "parameters": {
        "text": "={{$json.text}}",
        "options": {
          "systemMessage": " \n**1. AI Agent Goal Prompt (Overall Task)**\n\n*   **Purpose:** To define the agent's overall objective, removing the image creation step.\n\n```\nYou are an AI social media content creator. Your task is to research a given topic using SerpAPI, create engaging and SEO-optimized social media content (800-1000 characters), and generate a detailed image prompt. The content must be factually accurate and engaging. Prioritize factual accuracy and engaging storytelling in your content. The generated image prompt should be detailed and specific enough to be used with an image generation tool like DALL-E or Stable Diffusion.\n```\n\n**2. SerpAPI Tool Prompt (Research Phase)**\n\n*   **Purpose:** To instruct the agent on how to use SerpAPI to effectively gather information. (No change from previous version)\n\n```\nUse the SerpAPI tool to research the following topic: [TOPIC]. Focus on identifying key facts, trends, and interesting angles relevant for social media. Extract information from the top search results. Return a summary of the information you found focusing on key data and facts.\n```\n\n*   **Explanation:**\n    *   `[TOPIC]` is a variable that will be replaced with the specific topic.\n    *   Focuses the agent on extracting key facts and trends rather than just providing a list of results.\n    *   Limits the scope to the top search results to maintain efficiency.\n\n**3. Social Media Content Creation Prompt**\n\n*   **Purpose:** To guide the agent in creating engaging and SEO-friendly content based on the research. (No change from previous version)\n\n```\nBased on the following research summary: [RESEARCH_SUMMARY], create a social media post that is:\n\n*   Engaging and attention-grabbing\n*   Factually accurate\n*   Optimized for SEO (include relevant keywords naturally)\n*   Within 800-1000 characters\n*   Clearly and concisely written.\n*   Avoid jargon and technical terms.\n*    Include a call to action.\n\nThe tone should be informative but also enthusiastic and easily understandable.\n```\n\n*   **Explanation:**\n    *   `[RESEARCH_SUMMARY]` will be replaced with the output from the SerpAPI tool.\n    *   Specific instructions on tone, length, and SEO optimization.\n    *   Explicitly asks for clear and concise writing, avoiding jargon.\n    *   Added \"Include a call to action\" to make the content more actionable\n\n**4. Image Generation Prompt (for hypothetical image generation tool)**\n\n*   **Purpose:** To create a prompt that generates a detailed and descriptive image prompt for an image generation tool.  This prompt should now be the *final output* related to the image.\n\n```\nBased on the following topic: [TOPIC] and social media content: [SOCIAL_MEDIA_CONTENT], generate a detailed image prompt for a photorealistic image that visually represents the topic and complements the content. The image should be:\n\n*   Photorealistic and high-quality.\n*   Visually appealing and attention-grabbing.\n*   Relevant to the topic and content.\n*   Appropriate for social media.\n\nThe prompt should be exceptionally detailed and specific, providing precise instructions for an image generation tool like DALL-E or Stable Diffusion. Include details about the subject, setting, style, lighting, camera angles, and any other relevant visual elements.  Aim for a prompt that leaves no room for misinterpretation by the image generation AI.  Mention specific artists or photographic styles to emulate if appropriate.\n```\n\n*   **Explanation:**\n    *   `[TOPIC]` and `[SOCIAL_MEDIA_CONTENT]` are variables that will be replaced with the topic and the created social media content, respectively.\n    *   Focuses on *photorealism*, relevance, and visual appeal.\n    *   Emphasizes the need for an *exceptionally detailed and specific* prompt for the image generation tool.\n    *  Explicitly mentions DALL-E and Stable Diffusion as target tools.\n    *   Advises the inclusion of artist styles or photographic techniques to guide the image generation.\n\n**5. JSON Output Instruction**\n\n*   **Purpose:** To ensure the AI agent provides the output in the correct format.  The `image_url` field is replaced with `image_prompt`.\n\n```\nAfter generating the social media content and the image prompt, output the results in the following JSON format:\n\n```json\n{\n\"content\": \"[SOCIAL_MEDIA_CONTENT]\",\n\"image_prompt\": \"[IMAGE_PROMPT]\"\n}\n```\n\n`[SOCIAL_MEDIA_CONTENT]` is the social media content you created.\n`[IMAGE_PROMPT]` is the detailed image prompt you generated.\n```\n\n**Example Usage:**\n\nLet's say the topic is still \"The Benefits of Regular Exercise.\"\n\n1.  **SerpAPI Tool:** The agent uses SerpAPI to find information about the benefits of exercise.\n2.  **Social Media Content:** The agent generates content like: \"Boost your mood & health! 💪 Regular exercise reduces stress, improves sleep, and lowers disease risk. Get moving today! #exercise #healthylifestyle #fitness\"\n3.  **Image Prompt:** The agent generates an image prompt like: \"A photorealistic image of a diverse group of people happily participating in various forms of exercise in a vibrant outdoor setting. Some are jogging in a park with lush green trees, others are doing yoga poses on a grassy field, and a few are cycling on a paved path. The lighting is warm and golden, as if it's early morning or late afternoon. The style should be reminiscent of a National Geographic photograph, emphasizing the natural beauty of the scene and the healthy glow of the people. Use a shallow depth of field to blur the background slightly, drawing focus to the subjects. Camera angle: slightly low, capturing the energy and movement of the scene. Consider influences from the photographic style of Steve McCurry.\"\n4.  **JSON Output:**\n\n```json\n{\n\"content\": \"Boost your mood & health! 💪 Regular exercise reduces stress, improves sleep, and lowers disease risk. Get moving today! #exercise #healthylifestyle #fitness\",\n\"image_prompt\": \"A photorealistic image of a diverse group of people happily participating in various forms of exercise in a vibrant outdoor setting. Some are jogging in a park with lush green trees, others are doing yoga poses on a grassy field, and a few are cycling on a paved path. The lighting is warm and golden, as if it's early morning or late afternoon. The style should be reminiscent of a National Geographic photograph, emphasizing the natural beauty of the scene and the healthy glow of the people. Use a shallow depth of field to blur the background slightly, drawing focus to the subjects. Camera angle: slightly low, capturing the energy and movement of the scene. Consider influences from the photographic style of Steve McCurry.\"\n}\n```\n\n**Key Improvements and Techniques Used (Beyond the Previous Version):**\n\n*   **Focus on Photorealism:**  The image prompt now explicitly aims for photorealistic results.\n*   **Detailed Image Prompting:** The prompt emphasizes extreme detail and specificity in the image prompt.\n*   **Tool Agnostic:** The prompt mentions DALL-E and Stable Diffusion as example tools, but is designed to be usable with other image generation AIs.\n*   **Artist Style Guidance:** The prompt encourages the inclusion of artist or photographic style references.\n\n \n"
        },
        "promptType": "define",
        "hasOutputParser": true
      },
      "typeVersion": 1.7
    },
    {
      "id": "74f99543-d7e6-4d9b-8af1-9d86e0566ddc",
      "name": "OpenAI Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        1460,
        560
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
          "id": "uFPD9I4pWJ4xUVf7",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "62b9bb5f-0c87-4df4-ac1c-70b96a0a5cc4",
      "name": "SerpAPI",
      "type": "@n8n/n8n-nodes-langchain.toolSerpApi",
      "position": [
        1580,
        560
      ],
      "parameters": {
        "options": {}
      },
      "credentials": {
        "serpApi": {
          "id": "AuYW6wcagKBXR214",
          "name": "SerpAPI account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "3782a100-3210-4c87-9e6a-5808cd488601",
      "name": "Structured Output Parser",
      "type": "@n8n/n8n-nodes-langchain.outputParserStructured",
      "position": [
        1700,
        560
      ],
      "parameters": {
        "jsonSchemaExample": "{\n\"content\": \"[SOCIAL_MEDIA_CONTENT]\",\n\"image_prompt\": \"[IMAGE_PROMPT]\"\n}"
      },
      "typeVersion": 1.2
    },
    {
      "id": "87bf4b00-4f75-4098-993b-b4bd168339c2",
      "name": "Extract from File",
      "type": "n8n-nodes-base.extractFromFile",
      "position": [
        2380,
        320
      ],
      "parameters": {
        "options": {},
        "operation": "binaryToPropery"
      },
      "typeVersion": 1
    },
    {
      "id": "9a273f0b-bcb0-4ed8-93f5-6161d192e3ef",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1460,
        160
      ],
      "parameters": {
        "width": 280,
        "height": 140,
        "content": " **The AI agent uses the OpenAI Chat Model and SerpAPI tool to conduct research and generate social media content and an image prompt based on the user request.**"
      },
      "typeVersion": 1
    },
    {
      "id": "c907aa15-1ccf-475e-94da-3a81e54b3746",
      "name": "Prepare Final Output",
      "type": "n8n-nodes-base.set",
      "position": [
        2740,
        320
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "df5eb034-ef40-44a3-a620-48981efd1a69",
              "name": "content",
              "type": "string",
              "value": "={{ $('AI Agent').item.json.output.content }}"
            },
            {
              "id": "9ed8afc9-a957-4aea-8554-8c67017ef0e6",
              "name": "image",
              "type": "string",
              "value": "={{ $json.data }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "0893eac1-e72b-4a95-8c3c-4803aaaed9b9",
      "name": "Generate Image",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        2020,
        320
      ],
      "parameters": {
        "url": "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-3.5-large",
        "method": "POST",
        "options": {},
        "sendBody": true,
        "authentication": "predefinedCredentialType",
        "bodyParameters": {
          "parameters": [
            {
              "name": "inputs",
              "value": "={{ $json.output.image_prompt }}"
            }
          ]
        },
        "nodeCredentialType": "huggingFaceApi"
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "ERi7DgDYlifAQg7i",
          "name": "Header Auth account"
        },
        "huggingFaceApi": {
          "id": "2koOz09ZdzCYUNif",
          "name": "HuggingFaceApi account"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "b99a090f-73de-4703-b569-8992df36132f",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1960,
        240
      ],
      "parameters": {
        "width": 220,
        "height": 240,
        "content": " **An image is generated using the image prompt**  "
      },
      "typeVersion": 1
    }
  ],
  "pinData": {},
  "connections": {
    "SerpAPI": {
      "ai_tool": [
        [
          {
            "node": "AI Agent",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "AI Agent": {
      "main": [
        [
          {
            "node": "Generate Image",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Generate Image": {
      "main": [
        [
          {
            "node": "Extract from File",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Voice or Text?": {
      "main": [
        [
          {
            "node": "Fetch Voice Message",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Prepare for LLM",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Prepare for LLM": {
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
    "Extract from File": {
      "main": [
        [
          {
            "node": "Prepare Final Output",
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
    "Fetch Voice Message": {
      "main": [
        [
          {
            "node": "Transcribe Voice to Text",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Prepare Final Output": {
      "main": [
        []
      ]
    },
    "Structured Output Parser": {
      "ai_outputParser": [
        [
          {
            "node": "AI Agent",
            "type": "ai_outputParser",
            "index": 0
          }
        ]
      ]
    },
    "Transcribe Voice to Text": {
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
    "Receive Telegram Messages": {
      "main": [
        [
          {
            "node": "Voice or Text?",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2462"></a>

## Template 2462 - Enviar logs para BetterStack

- **Nome:** Enviar logs para BetterStack
- **Descrição:** Fluxo que recebe mensagens de log e as encaminha para o serviço BetterStack Logs via requisição HTTP.
- **Funcionalidade:** • Recebe mensagens de log de outros fluxos: aceita os campos 'level' e 'message' como entrada.
• Envia logs para BetterStack Logs: realiza uma requisição POST com corpo JSON contendo 'message' e 'level'.
• Suporta autenticação por cabeçalho: utiliza um token Bearer no cabeçalho Authorization para autorizar a requisição.
• Permite testes manuais: inclui um gatilho manual para enviar logs de teste.
• Exemplo de uso integrado: contém um fluxo de teste que chama este fluxo e envia uma mensagem de exemplo (level: error, message: "This is a test log message").
- **Ferramentas:** • BetterStack Logs: serviço de coleta e armazenamento de logs acessível via endpoint HTTP; aceita entradas em JSON e normalmente exige autenticação por token Bearer no cabeçalho Authorization.



## Fluxo visual

```mermaid
flowchart LR
    N1["Send Log to BetterStack"]
    N2["Recieve log message"]
    N3["Test workflow"]
    N4["Send test log message"]
    N5["Sticky Note"]
    N6["Sticky Note1"]
    N7["Sticky Note2"]
    N8["Sticky Note3"]

    N3 --> N4
    N2 --> N1
```

## Fluxo (.json) :

```json
{
  "meta": {
    "instanceId": "568298fde06d3db80a2eea77fe5bf45f0c7bb898dea20b769944e9ac7c6c5a80"
  },
  "nodes": [
    {
      "id": "72babb83-0530-4809-9f6f-d9afaf91fd59",
      "name": "Send Log to BetterStack",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        80,
        140
      ],
      "parameters": {
        "method": "POST",
        "options": {},
        "jsonBody": "={\n  \"message\":\"{{ $json.message }}\",\n  \"level\": \"{{ $json.level }}\"\n} ",
        "sendBody": true,
        "specifyBody": "json",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth"
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "NAa1bu8yteVhXxxV",
          "name": "Header Auth BetterStack"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "863b184b-05c0-47b7-82c1-166bdf25a32a",
      "name": "Recieve log message",
      "type": "n8n-nodes-base.executeWorkflowTrigger",
      "notes": "from another workflow",
      "position": [
        -140,
        140
      ],
      "parameters": {
        "workflowInputs": {
          "values": [
            {
              "name": "level"
            },
            {
              "name": "message"
            }
          ]
        }
      },
      "notesInFlow": true,
      "typeVersion": 1.1
    },
    {
      "id": "e696b65e-5249-43b2-9a33-4e59fc616f21",
      "name": "Test workflow",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        -260,
        -120
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "f7b51eae-4016-4072-9539-b66ea8646508",
      "name": "Send test log message",
      "type": "n8n-nodes-base.executeWorkflow",
      "notes": "using workflow",
      "position": [
        -40,
        -120
      ],
      "parameters": {
        "options": {},
        "workflowId": {
          "__rl": true,
          "mode": "id",
          "value": "={{$workflow.id}}"
        },
        "workflowInputs": {
          "value": {
            "level": "error",
            "message": "This is a test log message"
          },
          "schema": [
            {
              "id": "level",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "level",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "message",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "message",
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
      "notesInFlow": true,
      "typeVersion": 1.2
    },
    {
      "id": "72457cde-ea6f-406a-8d5e-70878114dd3e",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -440,
        60
      ],
      "parameters": {
        "width": 860,
        "height": 280,
        "content": "## Send log entries to BetterStack\nThis workflow can be used in two ways:\n1. Save it as a separate workflow to\nuse if from multiple worflows.\n2. Embed it into one workflow to just\nuse it from one."
      },
      "typeVersion": 1
    },
    {
      "id": "442976e5-1306-4c9b-a3e6-5693ae6d132c",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -440,
        -240
      ],
      "parameters": {
        "color": 7,
        "width": 660,
        "height": 280,
        "content": "## Demo\nThis is just a demo of how to call the workflow.\nKeep it here, replace it with your own workflow or delete it."
      },
      "typeVersion": 1
    },
    {
      "id": "4175c168-1f59-4213-8bc4-a71dd62c3bd9",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        20,
        100
      ],
      "parameters": {
        "color": 3,
        "height": 200,
        "content": "### Edit me"
      },
      "typeVersion": 1
    },
    {
      "id": "c69c7c62-f4b5-4b14-b6be-8e9f3b8a38cd",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -780,
        -240
      ],
      "parameters": {
        "color": 6,
        "width": 300,
        "height": 580,
        "content": "### 🧾 Log to BetterStack\n\n**👋 Hello! I'm Audun / xqus** \n🔗 My work: [xqus.com](https://xqus.com)\n💸 n8n shop: [xqus.gumroad.com](https://xqus.gumroad.com)\n\n\nThis workflow sends log messages to [BetterStack Logs](https://betterstack.com/logs) using a POST request.\n\n#### ✅ Usage:\n1. **From other workflows**  \n   → Use the **Execute Workflow** node and pass in `level` and `message`.\n\n2. **As standalone**  \n   → Manually trigger for testing, or embed it into a single workflow.\n\n#### 🔧 Setup:\n1. Set your **BetterStack Logs endpoint URL** in the HTTP Request node.  \n2. Add your **Header Auth** credentials: `Authorization: Bearer YOUR_TOKEN`\n"
      },
      "typeVersion": 1
    }
  ],
  "pinData": {},
  "connections": {
    "Test workflow": {
      "main": [
        [
          {
            "node": "Send test log message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Recieve log message": {
      "main": [
        [
          {
            "node": "Send Log to BetterStack",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2465"></a>

## Template 2465 - Pesquisa Brave via Telegram

- **Nome:** Pesquisa Brave via Telegram
- **Descrição:** Workflow que permite realizar buscas no Brave a partir de comandos enviados por Telegram e retornar os resultados diretamente ao usuário.
- **Funcionalidade:** • Detecção de mensagens do Telegram: inicia o fluxo ao receber uma mensagem do usuário.
• Filtragem por comando /brave: o processamento continua apenas se a mensagem começar com "/brave ".
• Extração e limpeza da consulta: remove o comando "/brave" e prepara o texto da busca.
• Listagem de ferramentas Brave disponíveis: consulta as ferramentas Brave configuradas para determinar qual usar.
• Execução da busca no Brave: envia a consulta para a ferramenta de busca Brave configurada e obtém os resultados.
• Envio de resultados ao usuário no Telegram: responde ao remetente com o texto retornado pela busca, usando formatação HTML quando aplicável.
- **Ferramentas:** • Brave Search API: serviço de busca que processa consultas e retorna resultados; requer chave de API.
• Telegram: plataforma de mensagens usada para receber comandos dos usuários e enviar as respostas.

## Fluxo visual

```mermaid
flowchart LR
    N1["List Brave Tools"]
    N2["Exec Brave tool"]
    N3["Clean query"]
    N4["Send message"]
    N5["Get Message"]
    N6["Search with Brave?"]
    N7["Sticky Note"]
    N8["Sticky Note1"]
    N9["Sticky Note2"]
    N10["Sticky Note3"]
    N11["Sticky Note4"]
    N12["Sticky Note5"]
    N13["Sticky Note6"]
    N14["Get Text"]

    N14 --> N3
    N3 --> N1
    N5 --> N6
    N2 --> N4
    N1 --> N2
    N6 --> N14
```

## Fluxo (.json) :

```json
{
  "id": "52pBJt8swWgtdY54",
  "meta": {
    "instanceId": "a4bfc93e975ca233ac45ed7c9227d84cf5a2329310525917adaf3312e10d5462",
    "templateCredsSetupCompleted": true
  },
  "name": "MCP Client with Brave and Telegram",
  "tags": [],
  "nodes": [
    {
      "id": "af9b297d-0f8f-408f-a4d6-7545a94e8a38",
      "name": "List Brave Tools",
      "type": "n8n-nodes-mcp.mcpClient",
      "position": [
        560,
        -40
      ],
      "parameters": {},
      "credentials": {
        "mcpClientApi": {
          "id": "YEgJcPwvAlBOCEDA",
          "name": "MCP Client (STDIO) Brave"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "c3265586-a376-4d02-8f33-828bbba6d221",
      "name": "Exec Brave tool",
      "type": "n8n-nodes-mcp.mcpClient",
      "position": [
        800,
        -40
      ],
      "parameters": {
        "toolName": "={{ $json.tools[0].name }}",
        "operation": "executeTool",
        "toolParameters": "={\n  \"query\":\"{{ $('Clean query').item.json.query }}\"\n}"
      },
      "credentials": {
        "mcpClientApi": {
          "id": "YEgJcPwvAlBOCEDA",
          "name": "MCP Client (STDIO) Brave"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "adbfe84e-ab4a-4640-bb52-fcb06f9d1450",
      "name": "Clean query",
      "type": "n8n-nodes-base.code",
      "position": [
        300,
        -40
      ],
      "parameters": {
        "jsCode": "for (const item of $input.all()) {\n  const originalText = item.json.text;\n\n  const query = originalText.replace(\"/brave \", \"\");\n\n  item.json.query = query;\n}\n\nreturn $input.all();\n"
      },
      "typeVersion": 2
    },
    {
      "id": "9905cad4-e847-44be-8cc4-69fd427ce8a1",
      "name": "Send message",
      "type": "n8n-nodes-base.telegram",
      "position": [
        1040,
        -40
      ],
      "webhookId": "b48bb09b-e019-46a2-994b-8058f65e6442",
      "parameters": {
        "text": "={{ $json.result.content[0].text }}",
        "chatId": "={{ $('Get Message').item.json.message.from.id }}",
        "additionalFields": {
          "parse_mode": "HTML"
        }
      },
      "credentials": {
        "telegramApi": {
          "id": "rQ5q95W7uKesMDx4",
          "name": "Telegram account Fastewb"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "bf0e7c48-bbc8-4efd-9083-2fa965902453",
      "name": "Get Message",
      "type": "n8n-nodes-base.telegramTrigger",
      "position": [
        -440,
        -20
      ],
      "webhookId": "07c09a64-758b-40ea-8c24-d999048781c3",
      "parameters": {
        "updates": [
          "message"
        ],
        "additionalFields": {}
      },
      "credentials": {
        "telegramApi": {
          "id": "rQ5q95W7uKesMDx4",
          "name": "Telegram account Fastewb"
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "b37c6f84-bceb-476c-9a7c-5682a4e69f8d",
      "name": "Search with Brave?",
      "type": "n8n-nodes-base.if",
      "position": [
        -180,
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
              "id": "9c5ea127-cbbb-4304-8a93-b47b5c09b837",
              "operator": {
                "type": "string",
                "operation": "startsWith"
              },
              "leftValue": "={{ $json.message.text }}",
              "rightValue": "/brave "
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "e879ea50-83f9-4a87-856c-a06a628ae31c",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -440,
        -860
      ],
      "parameters": {
        "color": 6,
        "width": 480,
        "content": "## PRELIMINARY STEPS\n- Access to an n8n self-hosted instance and install the Community node \"n8n-nodes-mcp\". Please see this [easy guide](https://github.com/nerding-io/n8n-nodes-mcp)\n- Get your Brave Search API Key: https://brave.com/search/api/\n- Telegram Bot Access Token\n\n\n"
      },
      "typeVersion": 1
    },
    {
      "id": "754e62d1-efdb-460d-bdb1-2369d633a804",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -440,
        -660
      ],
      "parameters": {
        "color": 6,
        "width": 480,
        "height": 420,
        "content": "## SET MCP BRAVE TOOL\nIn \"List Brave Tools\" create new credential as shown in  this image\n![image](https://github.com/nerding-io/n8n-nodes-mcp/raw/main/assets/credentials-envs.png)\n\nIn Environment field set this value:\nBRAVE_API_KEY=your-api-key"
      },
      "typeVersion": 1
    },
    {
      "id": "073eb8d2-9026-4031-af01-850342a5c5ca",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -240,
        -120
      ],
      "parameters": {
        "height": 260,
        "content": "the search only occurs when the command \"/brave\" is present in the message"
      },
      "typeVersion": 1
    },
    {
      "id": "eb76fbed-0ba0-4a56-a1fe-65e4bfb38ea8",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        240,
        -120
      ],
      "parameters": {
        "width": 220,
        "height": 260,
        "content": "I clean the message by removing the \"/brave\" command"
      },
      "typeVersion": 1
    },
    {
      "id": "980bf4e1-15cf-4276-b746-343850ec4b6f",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        520,
        -120
      ],
      "parameters": {
        "width": 180,
        "height": 260,
        "content": "Get all available Brave search tools"
      },
      "typeVersion": 1
    },
    {
      "id": "2c712ec4-2184-4136-bd21-f17e19fb029e",
      "name": "Sticky Note5",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        760,
        -120
      ],
      "parameters": {
        "width": 180,
        "height": 260,
        "content": "I get the search results"
      },
      "typeVersion": 1
    },
    {
      "id": "226a396a-e152-422d-b4e2-670a39117f57",
      "name": "Sticky Note6",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -440,
        -1180
      ],
      "parameters": {
        "color": 3,
        "width": 480,
        "height": 280,
        "content": "## MCP-based Brave Search Engine on Telegram \n\nThis workflow is a powerful tool for automating interactions with Brave tools through Telegram, providing users with quick and easy access to information directly in their chat.\n\nThis n8n workflow enables users to perform web searches directly from Telegram using the Brave search engine. By simply sending the command /brave followed by a query, the workflow retrieves search results from Brave and returns them as a Telegram message."
      },
      "typeVersion": 1
    },
    {
      "id": "7c526a9e-f3a2-433c-aeb1-ced2e5af6a12",
      "name": "Get Text",
      "type": "n8n-nodes-base.set",
      "position": [
        80,
        -40
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "029f4e7e-b367-4aa9-863e-e372694940fb",
              "name": "text",
              "type": "string",
              "value": "={{ $json.message.text }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "4566dd53-d373-43da-91c5-213ca5f335c6",
  "connections": {
    "Get Text": {
      "main": [
        [
          {
            "node": "Clean query",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Clean query": {
      "main": [
        [
          {
            "node": "List Brave Tools",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Message": {
      "main": [
        [
          {
            "node": "Search with Brave?",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Exec Brave tool": {
      "main": [
        [
          {
            "node": "Send message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "List Brave Tools": {
      "main": [
        [
          {
            "node": "Exec Brave tool",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Search with Brave?": {
      "main": [
        [
          {
            "node": "Get Text",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
