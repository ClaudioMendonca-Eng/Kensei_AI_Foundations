# PACK 1999 TEMPLATES PARTE 02 - Bloco 8

Templates neste bloco: 20

## Sumário

- [Template 342 - Restaurar emails por correspondência de itens](#template-342)
- [Template 343 - Geração TTS por script Python e reprodução](#template-343)
- [Template 344 - Renovação automática de tokens Pipedrive](#template-344)
- [Template 345 - Gerador de gráfico e upload para Google Drive](#template-345)
- [Template 346 - Obter data e hora local](#template-346)
- [Template 347 - Triagem automática de CV com IA](#template-347)
- [Template 348 - Upload de foto para SharePoint](#template-348)
- [Template 349 - Backend AI para extensão Chrome](#template-349)
- [Template 350 - Servidor MCP para GitHub (ver e comentar issues)](#template-350)
- [Template 351 - Agente de IA acionado por Siri](#template-351)
- [Template 352 - Indexação e busca de ensaios com Milvus](#template-352)
- [Template 353 - Resumo de vídeos YouTube e chat via Telegram](#template-353)
- [Template 354 - Encontrar e resumir oportunidades no Reddit](#template-354)
- [Template 355 - Conversão e compressão de PDFs](#template-355)
- [Template 356 - Rastreamento de horários e pausas](#template-356)
- [Template 357 - Iniciar workflows com tag 'Auto start'](#template-357)
- [Template 358 - Adicionar/Atualizar contato no ActiveCampaign](#template-358)
- [Template 359 - Assistente de documentos por Telegram](#template-359)
- [Template 360 - Automatizar marcação de fulfillment em pedidos Shopify](#template-360)
- [Template 361 - Extrair e consolidar listas de pessoas](#template-361)

---

<a id="template-342"></a>

## Template 342 - Restaurar emails por correspondência de itens

- **Nome:** Restaurar emails por correspondência de itens
- **Descrição:** Fluxo de exemplo que obtém registros de clientes, reduz os campos mantendo apenas o nome e depois restaura o email correspondente usando a correspondência por índice entre os itens.
- **Funcionalidade:** • Obtenção de registros: busca todos os registros de um datastore de clientes para uso no fluxo.
• Redução de dados: remove campos desnecessários mantendo apenas o nome em cada item.
• Restauração de campos vinculados: para cada item reduzido, recupera o email correspondente do conjunto original usando o índice do item e adiciona como campo restoreEmail.
• Execução manual: permite iniciar o fluxo manualmente para testes e demonstração.
- **Ferramentas:** • Datastore de clientes de exemplo: fonte de dados contendo registros de pessoas (nome e email) usada para gerar os dados do fluxo.
• Python (script): linguagem usada para executar a lógica de correspondência de itens e restaurar o campo de email.



## Fluxo visual

```mermaid
flowchart LR
    N1["When clicking 'Execute Workflow'"]
    N2["Customer Datastore (n8n training)"]
    N3["Code"]
    N4["Edit Fields"]
    N5["Sticky Note"]
    N6["Sticky Note1"]
    N7["Sticky Note2"]
    N8["Sticky Note3"]

    N4 --> N3
    N1 --> N2
    N2 --> N4
```

## Fluxo (.json) :

```json
{
  "id": "gkOayLvJnwcTiHbk",
  "meta": {
    "instanceId": "bd0e051174def82b88b5cd547222662900558d74b239c4048ea0f6b7ed61c642"
  },
  "name": "itemMatching() example",
  "tags": [],
  "nodes": [
    {
      "id": "ba0e23f6-aec6-4c22-8e7c-ab4fc65c7767",
      "name": "When clicking \"Execute Workflow\"",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        640,
        500
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "8434c3b4-5b80-48e5-803b-b84eb750b2c5",
      "name": "Customer Datastore (n8n training)",
      "type": "n8n-nodes-base.n8nTrainingCustomerDatastore",
      "position": [
        880,
        500
      ],
      "parameters": {
        "operation": "getAllPeople",
        "returnAll": true
      },
      "typeVersion": 1
    },
    {
      "id": "4750754a-92a6-44d2-a353-22fbb51a4d00",
      "name": "Code",
      "type": "n8n-nodes-base.code",
      "position": [
        1440,
        500
      ],
      "parameters": {
        "language": "python",
        "pythonCode": "for i,item in enumerate(_input.all()):\n  _input.all()[i].json.restoreEmail = _('Customer Datastore (n8n training)').itemMatching(i).json.email\n\nreturn _input.all();"
      },
      "typeVersion": 2
    },
    {
      "id": "9ac437bd-0d0d-4d92-845a-a1c9a7976d4d",
      "name": "Edit Fields",
      "type": "n8n-nodes-base.set",
      "position": [
        1180,
        500
      ],
      "parameters": {
        "fields": {
          "values": [
            {
              "name": "name",
              "stringValue": "={{ $json.name }}"
            }
          ]
        },
        "include": "none",
        "options": {}
      },
      "typeVersion": 3.2
    },
    {
      "id": "d59c512c-2dca-4960-b287-b4908713b0a3",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        820,
        400
      ],
      "parameters": {
        "height": 304,
        "content": "## Generate example data"
      },
      "typeVersion": 1
    },
    {
      "id": "fad37032-13cc-461e-b48e-a2f470d07823",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1100,
        398
      ],
      "parameters": {
        "height": 303,
        "content": "## Reduce the data\n\nRemove all data except the names"
      },
      "typeVersion": 1
    },
    {
      "id": "d0751fce-d9f0-40bf-aeb2-9dbc5d0e9bdb",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1380,
        400
      ],
      "parameters": {
        "height": 304,
        "content": "## Restore\n\nRestore the email address data"
      },
      "typeVersion": 1
    },
    {
      "id": "2b1a67e9-60d6-411e-8ae7-94b02da6be34",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        430,
        220
      ],
      "parameters": {
        "width": 352,
        "height": 264,
        "content": "## About this workflow\n\nThis workflow provides a simple example of how to use `itemMatching(itemIndex: Number)` in the Code node to retrieve linked items from earlier in the workflow.\n\nThis example uses JavaScript. Refer to [Retrieve linked items from earlier in the workflow](https://docs.n8n.io/code/cookbook/builtin/itemmatching/) for the Python code.\n"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "02e18c8e-1bec-4170-a2d0-72ec6e063273",
  "connections": {
    "Edit Fields": {
      "main": [
        [
          {
            "node": "Code",
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
            "node": "Customer Datastore (n8n training)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Customer Datastore (n8n training)": {
      "main": [
        [
          {
            "node": "Edit Fields",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-343"></a>

## Template 343 - Geração TTS por script Python e reprodução

- **Nome:** Geração TTS por script Python e reprodução
- **Descrição:** Gera um arquivo de áudio a partir de texto usando um script Python e em seguida carrega o arquivo MP3 para reprodução.
- **Funcionalidade:** • Início manual: permite acionar o processo manualmente.
• Definição de variáveis: define parâmetros de entrada, como texto e voz a serem usados.
• Execução de script Python: chama o script local voicegen.py com os parâmetros para converter texto em áudio.
• Leitura do arquivo de saída: carrega o arquivo MP3 gerado (output.mp3) para reprodução ou uso posterior.
- **Ferramentas:** • Python (voicegen.py): script local que converte texto em áudio usando um parâmetro de voz e gera um arquivo MP3 de saída.
• Sistema de arquivos local: armazena e disponibiliza o arquivo de áudio gerado (por exemplo, D:/output.mp3) para leitura e reprodução.



## Fluxo visual

```mermaid
flowchart LR
    N1["Run python script"]
    N2["Passing variables"]
    N3["Start"]
    N4["Play sound"]

    N3 --> N2
    N2 --> N1
    N1 --> N4
```

## Fluxo (.json) :

```json
{
  "meta": {
    "instanceId": "a6d5191e58fd6be87222f47435e6f9df8f98ec0d945d3e7b7f6373c59a6c3f37",
    "templateCredsSetupCompleted": true
  },
  "nodes": [
    {
      "id": "fcf1064e-557f-4514-9109-bb10ac837f8b",
      "name": "Run python script",
      "type": "n8n-nodes-base.executeCommand",
      "position": [
        -100,
        20
      ],
      "parameters": {
        "command": "=python C:\\KOKORO\\voicegen.py \"{{ $json.text }}\" \"{{ $json.voice }}\" 1\n"
      },
      "typeVersion": 1
    },
    {
      "id": "199a3212-69c0-4314-92c8-783573f165d7",
      "name": "Passing variables",
      "type": "n8n-nodes-base.set",
      "position": [
        -320,
        20
      ],
      "parameters": {
        "mode": "raw",
        "options": {},
        "jsonOutput": "{\n  \"voice\": \"af_sarah\",\n  \"text\": \"Hello world!\"\n}\n"
      },
      "typeVersion": 3.4
    },
    {
      "id": "deb008d0-53ae-4348-a555-9e54b6e0efd4",
      "name": "Start",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        -540,
        20
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "ffa1b2bf-abc3-45d8-8b7b-de4c0780a609",
      "name": "Play sound",
      "type": "n8n-nodes-base.readBinaryFiles",
      "position": [
        120,
        20
      ],
      "parameters": {
        "fileSelector": "D:/output.mp3"
      },
      "typeVersion": 1,
      "alwaysOutputData": false
    }
  ],
  "pinData": {},
  "connections": {
    "Start": {
      "main": [
        [
          {
            "node": "Passing variables",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Passing variables": {
      "main": [
        [
          {
            "node": "Run python script",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Run python script": {
      "main": [
        [
          {
            "node": "Play sound",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-344"></a>

## Template 344 - Renovação automática de tokens Pipedrive

- **Nome:** Renovação automática de tokens Pipedrive
- **Descrição:** Fluxo que gerencia tokens OAuth do Pipedrive: recebe requisições, usa tokens armazenados para chamar a API, detecta token inválido e renova o access token atualizando o banco.
- **Funcionalidade:** • Recepção de requisições via webhook: Aceita chamadas externas que iniciam a busca por uma pessoa (email) no Pipedrive.
• Recuperação de tokens do banco: Consulta registro no banco para obter access_token e refresh_token associados ao app.
• Chamada à API do Pipedrive: Executa uma busca de pessoa usando o access_token armazenado.
• Detecção de token inválido: Verifica a resposta da API e detecta quando o access_token é inválido.
• Fluxo de refresh automático: Quando o token é inválido, aciona um webhook interno que obtém um novo access_token usando o refresh_token.
• Atualização do registro de tokens: Salva o novo access_token e refresh_token no banco de dados.
• Geração inicial de tokens via authorization code: Captura o authorization_code (callback) e troca por access/refresh tokens, inserindo ou atualizando o registro no banco.
• Conversão de client_id: Constrói o header de Authorization em Basic (client_id:client_secret em base64) para chamadas ao endpoint de token.
• Loop para reexecução: Após refresh, o fluxo retorna para buscar o token atualizado e repetir a chamada original quando necessário.
- **Ferramentas:** • Pipedrive: API e endpoint OAuth para autenticação e operações sobre pessoas.
• Supabase: Banco de dados para armazenar e atualizar access_token e refresh_token por aplicação.
• Aplicação cliente (webhook): Serviço externo que envia requisições para este fluxo para realizar buscas e acionar o processo de refresh.



## Fluxo visual

```mermaid
flowchart LR
    N1["Stop and Error"]
    N2["Sticky Note"]
    N3["Sticky Note1"]
    N4["Sticky Note2"]
    N5["Sticky Note3"]
    N6["Insert"]
    N7["Sticky Note4"]
    N8["Sticky Note5"]
    N9["Get Pipedrive Token"]
    N10["Get contact from Pipedrive"]
    N11["Access Token Invalid"]
    N12["Success"]
    N13["Refresh Access Token"]
    N14["Sticky Note6"]
    N15["Sticky Note7"]
    N16["Sticky Note8"]
    N17["convert clientId and secret to base64"]
    N18["Generate Refresh Token from authcode"]
    N19["Look for the related record in Supabase"]
    N20["IF rec not found"]
    N21["Update tokns in the record"]
    N22["Supabase- look for the record"]
    N23["combine client id and secret"]
    N24["Get Pipedrive acess token"]
    N25["IF success"]
    N26["Update thr row with new access token"]
    N27["Webhook"]
    N28["Receive request"]
    N29["catch Auth code"]

    N27 --> N22
    N25 --> N26
    N25 --> N1
    N28 --> N9
    N29 --> N17
    N20 --> N6
    N20 --> N21
    N9 --> N10
    N11 --> N13
    N11 --> N12
    N13 --> N9
    N24 --> N25
    N10 --> N11
    N23 --> N24
    N22 --> N23
    N18 --> N19
    N17 --> N18
    N19 --> N20
```

## Fluxo (.json) :

```json
{
  "id": "IYgbtNpyB4E6Jbxo",
  "meta": {
    "instanceId": "35ae520798f87e479496aa54e1a1f89ffdf43eee77986511d08258a12b1edc98",
    "templateCredsSetupCompleted": true
  },
  "name": "2. Refresh Pipedrive tokens",
  "tags": [],
  "nodes": [
    {
      "id": "2b66edcd-c71a-4dac-971f-deb1b09ef85b",
      "name": "Stop and Error",
      "type": "n8n-nodes-base.stopAndError",
      "position": [
        1460,
        -80
      ],
      "parameters": {
        "errorMessage": "Token refresh failed"
      },
      "typeVersion": 1,
      "alwaysOutputData": false
    },
    {
      "id": "b48d6760-766e-4b39-be35-89de7dc3ab5e",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        60,
        -300
      ],
      "parameters": {
        "color": 5,
        "width": 872,
        "height": 97,
        "content": "## Step 2:\nCreate a workflow to refresh your access token when the access token requires a refresh."
      },
      "typeVersion": 1
    },
    {
      "id": "6119eef3-9ffa-45a1-b238-412738e7529e",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        280,
        -80
      ],
      "parameters": {
        "height": 211,
        "content": "\n\n\n\n\n\n\n\nPost unique data to identify your row in Database and be able to fetch the existing access and refresh token"
      },
      "typeVersion": 1
    },
    {
      "id": "2d76be21-95e1-4747-b761-126b133e8264",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        980,
        -220
      ],
      "parameters": {
        "content": "## Get token from pipedrive"
      },
      "typeVersion": 1
    },
    {
      "id": "9a44eb63-9d31-4b24-9171-1f9a828a5c52",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        100,
        -740
      ],
      "parameters": {
        "color": 5,
        "width": 995,
        "height": 82,
        "content": "## Step 1:\nSave Refresh token and Access token to DB when authenticated by user and installed.  "
      },
      "typeVersion": 1
    },
    {
      "id": "f3247e6a-7c1c-4479-9f83-f3bc4146f254",
      "name": "Insert",
      "type": "n8n-nodes-base.supabase",
      "position": [
        1600,
        -660
      ],
      "parameters": {
        "tableId": "App_tok",
        "fieldsUi": {
          "fieldValues": [
            {
              "fieldId": "ref_token",
              "fieldValue": "={{ $node[\"Generate Refresh Token from authcode\"].json[\"body\"][\"refresh_token\"] }}"
            },
            {
              "fieldId": "acc_token",
              "fieldValue": "={{ $node[\"Generate Refresh Token from authcode\"].json[\"body\"][\"access_token\"] }}"
            },
            {
              "fieldId": "Platform",
              "fieldValue": "Pipedrive"
            },
            {
              "fieldId": "created_at",
              "fieldValue": "={{$now.toUTC().toString()}}"
            },
            {
              "fieldId": "updated_at",
              "fieldValue": "={{$now.toUTC().toString()}}"
            }
          ]
        }
      },
      "credentials": {
        "supabaseApi": {
          "id": "tlmP1CXY3ExzjJDs",
          "name": "Supabase Automation"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "f7ad45d0-7055-45f4-9971-031ffebfdbda",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        500,
        -640
      ],
      "parameters": {
        "content": "You can also use SET NODE + tobase64 function as done in step 2"
      },
      "typeVersion": 1
    },
    {
      "id": "e14e2dac-e84b-475f-a01b-14bb723eedc8",
      "name": "Sticky Note5",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        100,
        200
      ],
      "parameters": {
        "color": 5,
        "width": 1644,
        "height": 80,
        "content": "## Step 3:\nMake an actual API call. In this example, we are using search person API. Please refer to Pipedrive API documentation for your specific use case. "
      },
      "typeVersion": 1
    },
    {
      "id": "b450c928-e0e4-4f49-829e-03b61828d4d9",
      "name": "Get Pipedrive Token",
      "type": "n8n-nodes-base.supabase",
      "position": [
        600,
        660
      ],
      "parameters": {
        "filters": {
          "conditions": [
            {
              "keyName": "Platform",
              "keyValue": "Pipedrive"
            },
            {
              "keyName": "AppId",
              "keyValue": "57db0bab2932f657"
            }
          ]
        },
        "tableId": "App_tok",
        "operation": "get"
      },
      "credentials": {
        "supabaseApi": {
          "id": "tlmP1CXY3ExzjJDs",
          "name": "Supabase Automation"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "f92a957a-d0ef-4037-8657-74e7fe74fe6d",
      "name": "Get contact from Pipedrive",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        900,
        660
      ],
      "parameters": {
        "url": "=https://priyajain-sandbox.pipedrive.com/api/v2/persons/search?fields=email&term={{ $node[\"Receive request\"].json[\"body\"][\"person\"][\"email\"] }}",
        "options": {
          "response": {
            "response": {
              "fullResponse": true
            }
          }
        },
        "sendHeaders": true,
        "headerParameters": {
          "parameters": [
            {
              "name": "Accept",
              "value": "application/json"
            },
            {
              "name": "Authorization",
              "value": "=Bearer {{ $node[\"Get Pipedrive Token\"].json[\"acc_token\"] }}"
            }
          ]
        }
      },
      "typeVersion": 4,
      "continueOnFail": true,
      "alwaysOutputData": false
    },
    {
      "id": "bff21156-3da0-4cf3-b3de-c24d8abe7577",
      "name": "Access Token Invalid",
      "type": "n8n-nodes-base.if",
      "position": [
        1160,
        700
      ],
      "parameters": {
        "conditions": {
          "boolean": [
            {
              "value1": "={{ $json[\"error\"][\"message\"].includes(\"Invalid token: access token is invalid\") }}",
              "value2": "={{ true }}"
            }
          ]
        },
        "combineOperation": "any"
      },
      "typeVersion": 1
    },
    {
      "id": "9fd832b1-2af9-48c2-9d57-86a9f34bdd78",
      "name": "Success",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        1440,
        720
      ],
      "parameters": {
        "options": {
          "responseCode": 200
        },
        "respondWith": "json",
        "responseBody": "={{ $node[\"Get contact from Pipedrive\"].json[\"body\"][\"data\"][\"items\"][\"0\"][\"item\"][\"name\"] }}"
      },
      "typeVersion": 1
    },
    {
      "id": "daf33b32-ff7b-4d7e-8fd0-d54dfaddf405",
      "name": "Refresh Access Token",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1360,
        320
      ],
      "parameters": {
        "url": "http://localhost:5678/webhook/937a8843-a28a-400a-b473-bdc598366fa0",
        "method": "POST",
        "options": {},
        "jsonBody": "{\n\n  \"appId\":\"57db0bab2932f657\"\n\n}",
        "sendBody": true,
        "specifyBody": "json",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpBasicAuth"
      },
      "credentials": {
        "httpBasicAuth": {
          "id": "E2RYFiR9PotuglZv",
          "name": "PJ demo"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "6759a890-6c2a-4bb1-aae9-9b8723b9e143",
      "name": "Sticky Note6",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        580,
        420
      ],
      "parameters": {
        "width": 668,
        "content": "## Loop back to fecth the  refreshed Access Token\n### Note:\nYou can add further conditions and use Switch  statemen tinstead of IF to validate API response based on your use case."
      },
      "typeVersion": 1
    },
    {
      "id": "d975ce9f-2ef2-46b1-9d30-4f6e06e19b7e",
      "name": "Sticky Note7",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        120,
        -960
      ],
      "parameters": {
        "width": 1413,
        "content": "## 1. This workflow helps you create your own Oauth 2.0 token refresh system. It helps you have better control of your oauth 2.0 auth process.\n## 2. I am using Pipedrive API here. However, you can re-use this for other similar applications. "
      },
      "typeVersion": 1
    },
    {
      "id": "40d59a94-563d-459c-91d0-4206c2a19704",
      "name": "Sticky Note8",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        180,
        580
      ],
      "parameters": {
        "height": 248,
        "content": "A 3rd partyapplication posting the request to the webhook"
      },
      "typeVersion": 1
    },
    {
      "id": "03945766-570c-47db-82c6-2c973e45106d",
      "name": "convert clientId and secret to base64",
      "type": "n8n-nodes-base.code",
      "position": [
        560,
        -560
      ],
      "parameters": {
        "jsCode": "// Loop over input items and add a new field called 'myNewField' to the JSON of each one\nconst client_id = \"57db0bab2932f657\";\nconst client_secret = \"edfaba095e9e7ddefe2e960ce2e98345230a016d\";\n\n// Combine client_id and client_secret with a colon\nconst combinedString = client_id+\":\"+client_secret;\n\n// Encode the combined string in Base64\nconst encodedString = Buffer.from(combinedString).toString('base64');\n\n// Create the Authorization header value\nconst authorizationHeader = `Basic ${encodedString}`;\n\nreturn {\"authheader\":authorizationHeader};"
      },
      "typeVersion": 2
    },
    {
      "id": "8ca6eb93-6994-4536-b61e-d884c8515929",
      "name": "Generate Refresh Token from authcode",
      "type": "n8n-nodes-base.httpRequest",
      "maxTries": 2,
      "position": [
        820,
        -560
      ],
      "parameters": {
        "url": "https://oauth.pipedrive.com/oauth/token",
        "method": "POST",
        "options": {
          "response": {
            "response": {
              "fullResponse": true
            }
          }
        },
        "sendBody": true,
        "contentType": "form-urlencoded",
        "sendHeaders": true,
        "bodyParameters": {
          "parameters": [
            {
              "name": "grant_type",
              "value": "authorization_code"
            },
            {
              "name": "code",
              "value": "={{$node[\"catch Auth code\"].json[\"query\"][\"code\"]}}"
            },
            {
              "name": "redirect_uri",
              "value": "={{ $node[\"catch Auth code\"].json[\"webhookUrl\"] }}"
            }
          ]
        },
        "headerParameters": {
          "parameters": [
            {
              "name": "Authorization",
              "value": "={{$node[\"convert clientId and secret to base64\"].json[\"authheader\"]}}"
            }
          ]
        }
      },
      "retryOnFail": false,
      "typeVersion": 4,
      "alwaysOutputData": false
    },
    {
      "id": "9c1b22e1-fd50-4c70-91cf-f4ea8cc7d3ac",
      "name": "Look for the related record in Supabase",
      "type": "n8n-nodes-base.supabase",
      "position": [
        1060,
        -540
      ],
      "parameters": {
        "filters": {
          "conditions": [
            {
              "keyName": "Platform",
              "keyValue": "Pipedrive"
            }
          ]
        },
        "tableId": "App_tok",
        "operation": "get"
      },
      "credentials": {
        "supabaseApi": {
          "id": "tlmP1CXY3ExzjJDs",
          "name": "Supabase Automation"
        }
      },
      "typeVersion": 1,
      "alwaysOutputData": true
    },
    {
      "id": "53602a58-d47a-4133-b9ec-4ea421a75eea",
      "name": "IF rec not found",
      "type": "n8n-nodes-base.if",
      "position": [
        1260,
        -540
      ],
      "parameters": {
        "conditions": {
          "number": [
            {
              "value1": "={{ $json.values().length }}",
              "operation": "equal"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "id": "38e5d91c-1bea-4f7a-8336-98748005d02e",
      "name": "Update tokns in the record",
      "type": "n8n-nodes-base.supabase",
      "position": [
        1600,
        -460
      ],
      "parameters": {
        "filters": {
          "conditions": [
            {
              "keyName": "Platform",
              "keyValue": "Pipedrive",
              "condition": "eq"
            }
          ]
        },
        "tableId": "App_tok",
        "fieldsUi": {
          "fieldValues": [
            {
              "fieldId": "acc_token",
              "fieldValue": "={{ $node[\"Generate Refresh Token from authcode\"].json[\"body\"][\"access_token\"] }}"
            },
            {
              "fieldId": "ref_token",
              "fieldValue": "={{ $node[\"Generate Refresh Token from authcode\"].json[\"body\"][\"refresh_token\"] }}"
            },
            {
              "fieldId": "updated_at",
              "fieldValue": "={{$now.toUTC().toString()}}"
            }
          ]
        },
        "matchType": "allFilters",
        "operation": "update"
      },
      "credentials": {
        "supabaseApi": {
          "id": "tlmP1CXY3ExzjJDs",
          "name": "Supabase Automation"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "43a2613d-7793-48c9-8934-57d9b713f5fe",
      "name": "Supabase- look for the record",
      "type": "n8n-nodes-base.supabase",
      "position": [
        600,
        -140
      ],
      "parameters": {
        "filters": {
          "conditions": [
            {
              "keyName": "Platform",
              "keyValue": "Pipedrive"
            },
            {
              "keyName": "AppId",
              "keyValue": "={{ $node[\"Webhook\"].json[\"body\"][\"appId\"] }}"
            }
          ]
        },
        "tableId": "App_tok",
        "operation": "get"
      },
      "credentials": {
        "supabaseApi": {
          "id": "tlmP1CXY3ExzjJDs",
          "name": "Supabase Automation"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "366bd343-419c-4a77-b2ce-e6124a6cc291",
      "name": "combine client id and secret",
      "type": "n8n-nodes-base.set",
      "position": [
        840,
        -140
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "4330b857-6184-4ad8-82dc-a8b806ab8077",
              "name": "authheader",
              "type": "string",
              "value": "57db0bab2932f657:edfaba095e9e7ddefe2e960ce2e98345230a016d"
            }
          ]
        }
      },
      "typeVersion": 3.3
    },
    {
      "id": "156acb8f-3a23-40ec-b011-9db8bfa6d98b",
      "name": "Get Pipedrive acess token",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1060,
        -140
      ],
      "parameters": {
        "url": "https://oauth.pipedrive.com/oauth/token",
        "method": "POST",
        "options": {},
        "sendBody": true,
        "contentType": "form-urlencoded",
        "sendHeaders": true,
        "bodyParameters": {
          "parameters": [
            {
              "name": "grant_type",
              "value": "refresh_token"
            },
            {
              "name": "refresh_token",
              "value": "={{ $node[\"Supabase- look for the record\"].json[\"ref_token\"] }}"
            }
          ]
        },
        "headerParameters": {
          "parameters": [
            {
              "name": "Authorization",
              "value": "=Basic {{ $json[\"authheader\"].base64Encode() }}"
            }
          ]
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "3e20309e-6d50-444c-b9e1-cf6d6982e546",
      "name": "IF success",
      "type": "n8n-nodes-base.if",
      "position": [
        1240,
        -140
      ],
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{ Object.keys($input.first().json)[0]}}",
              "value2": "access_token"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "id": "1e991aa7-9888-404d-8f80-bb6ce0a3b777",
      "name": "Update thr row with new access token",
      "type": "n8n-nodes-base.supabase",
      "position": [
        1420,
        -280
      ],
      "parameters": {
        "filters": {
          "conditions": [
            {
              "keyName": "Platform",
              "keyValue": "Pipedrive",
              "condition": "eq"
            }
          ]
        },
        "tableId": "App_tok",
        "fieldsUi": {
          "fieldValues": [
            {
              "fieldId": "acc_token",
              "fieldValue": "={{ $node[\"Get Pipedrive acess token\"].json[\"access_token\"] }}"
            },
            {
              "fieldId": "ref_token",
              "fieldValue": "={{ $node[\"Get Pipedrive acess token\"].json[\"refresh_token\"] }}"
            }
          ]
        },
        "matchType": "allFilters",
        "operation": "update"
      },
      "credentials": {
        "supabaseApi": {
          "id": "tlmP1CXY3ExzjJDs",
          "name": "Supabase Automation"
        }
      },
      "typeVersion": 1,
      "alwaysOutputData": true
    },
    {
      "id": "d0989bad-9176-44a2-86ce-db07a5e8a34c",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "position": [
        340,
        -140
      ],
      "webhookId": "937a8843-a28a-400a-b473-bdc598366fa0",
      "parameters": {
        "path": "937a8843-a28a-400a-b473-bdc598366fa0",
        "options": {},
        "httpMethod": "POST",
        "responseMode": "lastNode",
        "authentication": "basicAuth"
      },
      "credentials": {
        "httpBasicAuth": {
          "id": "E2RYFiR9PotuglZv",
          "name": "PJ demo"
        }
      },
      "typeVersion": 2
    },
    {
      "id": "108a2ea1-de2a-4df3-9d9f-0ce1b27a52e9",
      "name": "Receive request",
      "type": "n8n-nodes-base.webhook",
      "position": [
        280,
        680
      ],
      "webhookId": "47704458-bfa6-4d95-adf1-97fc78e35d8a",
      "parameters": {
        "path": "47704458-bfa6-4d95-adf1-97fc78e35d8a",
        "options": {},
        "httpMethod": "POST",
        "responseMode": "responseNode",
        "authentication": "basicAuth"
      },
      "credentials": {
        "httpBasicAuth": {
          "id": "E2RYFiR9PotuglZv",
          "name": "PJ demo"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "f983cfd1-52db-4839-88af-6386ec7c7256",
      "name": "catch Auth code",
      "type": "n8n-nodes-base.webhook",
      "position": [
        300,
        -560
      ],
      "webhookId": "aae545fb-a69d-4e20-91ce-65f105d0ea2f",
      "parameters": {
        "path": "aae545fb-a69d-4e20-91ce-65f105d0ea2f",
        "options": {}
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {
    "Receive request": [
      {
        "json": {
          "body": {
            "person": {
              "email": "priya+solar@psw.com"
            }
          },
          "query": {},
          "params": {},
          "headers": {
            "host": "http://localhost:5678",
            "accept": "*/*",
            "user-agent": "PostmanRuntime/7.39.0",
            "content-type": "application/json",
            "authorization": "Basic xxxxxxx==",
            "cache-control": "no-cache",
            "postman-token": "41b79257-xxxx-xxxx-xxxx-9e004cae4e9e",
            "content-length": "52",
            "accept-encoding": "gzip, deflate, br",
            "x-forwarded-for": "54.86.50.139",
            "x-forwarded-host": "localhost:5678",
            "x-forwarded-proto": "https"
          },
          "webhookUrl": "http://localhost:5678/webhook-test/47704458-bfa6-4d95-adf1-97fc78e35d8a",
          "executionMode": "test"
        }
      }
    ]
  },
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "54499ed8-4677-400a-9e03-d0d84f8a97b5",
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Supabase- look for the record",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "IF success": {
      "main": [
        [
          {
            "node": "Update thr row with new access token",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Stop and Error",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Receive request": {
      "main": [
        [
          {
            "node": "Get Pipedrive Token",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "catch Auth code": {
      "main": [
        [
          {
            "node": "convert clientId and secret to base64",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "IF rec not found": {
      "main": [
        [
          {
            "node": "Insert",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Update tokns in the record",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Pipedrive Token": {
      "main": [
        [
          {
            "node": "Get contact from Pipedrive",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Access Token Invalid": {
      "main": [
        [
          {
            "node": "Refresh Access Token",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Success",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Refresh Access Token": {
      "main": [
        [
          {
            "node": "Get Pipedrive Token",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Pipedrive acess token": {
      "main": [
        [
          {
            "node": "IF success",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get contact from Pipedrive": {
      "main": [
        [
          {
            "node": "Access Token Invalid",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "combine client id and secret": {
      "main": [
        [
          {
            "node": "Get Pipedrive acess token",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Supabase- look for the record": {
      "main": [
        [
          {
            "node": "combine client id and secret",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Generate Refresh Token from authcode": {
      "main": [
        [
          {
            "node": "Look for the related record in Supabase",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "convert clientId and secret to base64": {
      "main": [
        [
          {
            "node": "Generate Refresh Token from authcode",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Look for the related record in Supabase": {
      "main": [
        [
          {
            "node": "IF rec not found",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-345"></a>

## Template 345 - Gerador de gráfico e upload para Google Drive

- **Nome:** Gerador de gráfico e upload para Google Drive
- **Descrição:** Gera um gráfico de linha a partir de dados JSON e faz upload da imagem para o Google Drive.
- **Funcionalidade:** • Geração de gráfico dinâmico: Cria um gráfico de linha usando arrays de labels e dados fornecidos em JSON.
• Uso de dados de teste editáveis: Permite definir dados JSON de exemplo diretamente no fluxo para testes rápidos.
• Disparo manual: Inicia o processo manualmente para testar a geração e envio do gráfico.
• Upload para Google Drive: Salva o arquivo de imagem gerado na conta e pasta especificadas.
• Orientações de personalização: Fornece instruções integradas para alterar tipo de gráfico, aparência, fontes de dados e destino de saída.
- **Ferramentas:** • QuickChart: Serviço que gera imagens de gráficos a partir de configurações JSON.
• Google Drive: Serviço de armazenamento em nuvem usado para salvar o arquivo de imagem gerado.

## Fluxo visual

```mermaid
flowchart LR
    N1["QuickChart"]
    N2["Edit Fields: Set JSON data to test"]
    N3["Google Drive: Upload File"]
    N4["Sticky Note"]
    N5["When clicking ‘Test workflow’"]

    N1 --> N3
    N5 --> N2
    N2 --> N1
```

## Fluxo (.json) :

```json
{
  "meta": {
    "instanceId": "c6511943b220d4ab672ac957465b13db475def5fbbd0b0e41240952f5fd0c300"
  },
  "nodes": [
    {
      "id": "e0721f8a-d157-4ec4-91b3-94060a841dc8",
      "name": "QuickChart",
      "type": "n8n-nodes-base.quickChart",
      "position": [
        240,
        -40
      ],
      "parameters": {
        "data": "={{ $json.jsonData.salesData }}",
        "chartType": "line",
        "labelsMode": "array",
        "labelsArray": "={{ $json.jsonData.labels }}",
        "chartOptions": {},
        "datasetOptions": {}
      },
      "typeVersion": 1
    },
    {
      "id": "b178ca51-357f-4731-8953-75e2370edc2d",
      "name": "Edit Fields: Set JSON data to test",
      "type": "n8n-nodes-base.set",
      "position": [
        -80,
        -40
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "1b3ae0ac-7fa5-406c-8e61-d6a9a6c27f07",
              "name": "jsonData",
              "type": "object",
              "value": "={ \"reportTitle\": \"Quarterly Sales\", \"labels\": [\"Q1\", \"Q2\", \"Q3\", \"Q4\"], \"salesData\": [1250, 1800, 1550, 2100] }"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "393665db-f6a6-4294-afd8-3a9f32192c64",
      "name": "Google Drive: Upload File",
      "type": "n8n-nodes-base.googleDrive",
      "position": [
        520,
        -40
      ],
      "parameters": {
        "name": "=chart.{{ $binary.data.fileExtension }}",
        "driveId": {
          "__rl": true,
          "mode": "list",
          "value": "My Drive"
        },
        "options": {},
        "folderId": {
          "__rl": true,
          "mode": "list",
          "value": "root",
          "cachedResultName": "/ (Root folder)"
        }
      },
      "credentials": {
        "googleDriveOAuth2Api": {
          "id": "Vt3z79hk8lh9TUQq",
          "name": "Google Drive account"
        }
      },
      "typeVersion": 3
    },
    {
      "id": "c4f2df73-50dc-4b9f-bcb8-43644c0cbed9",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -600,
        -740
      ],
      "parameters": {
        "width": 1460,
        "height": 1060,
        "content": "## Chart Generator\n**Generate Dynamic Line Chart from JSON Data to Upload to Google Drive\n### How to Use & Customize\n\n* **Change Input Data:** Modify the `labels` and `salesData` arrays within the `Edit Fields: Set JSON data to test` node to use your own data. Ensure the number of labels matches the number of data points.\n* **Use Real Data Sources:** Replace the `Edit Fields: Set JSON data to test` node with nodes that fetch data from real sources like:\n    * HTTP Request (APIs)\n    * Postgres / MongoDB nodes (Databases)\n    * Google Sheets node\n    * Ensure the output data from your source node is formatted similarly (providing `labels` and `salesData` arrays). You might need another Set node to structure the data correctly before the QuickChart node.\n* **Change Chart Type:** In the QuickChart node, modify the `Chart Type` parameter (e.g., change from `line` to `bar`, `pie`, `doughnut`, etc.).\n* **Customize Chart Appearance:** Explore the `Chart Options` parameter within the QuickChart node to add titles, change colors, modify axes, etc., using QuickChart's standard JSON configuration options.\n* **Use Datasets (Recommended for Complex Charts):** For multiple lines/bars or more control, configure datasets explicitly in the QuickChart node:\n    * Remove the expression from the top-level `Data` field.\n    * Go to `Dataset Options` -&gt; `Add option` -&gt; `Add dataset`.\n    * Set the `Data` field within the dataset using an expression like `{{ $json.jsonData.salesData }}`.\n    * You can add multiple datasets this way.\n* **Change Output Destination:** Replace the `Google Drive: Upload File` node with other nodes to handle the chart image differently:\n    * `Write Binary File`: Save the chart to the local filesystem where n8n is running.\n    * `Slack` / `Discord` / `Telegram`: Send the chart to messaging platforms.\n    * `Move Binary Data`: Convert the image to Base64 to embed in HTML or return via webhook response."
      },
      "typeVersion": 1
    },
    {
      "id": "1af3cfc6-f690-4af2-a812-4a4da118a55c",
      "name": "When clicking ‘Test workflow’",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        -400,
        -40
      ],
      "parameters": {},
      "typeVersion": 1
    }
  ],
  "pinData": {},
  "connections": {
    "QuickChart": {
      "main": [
        [
          {
            "node": "Google Drive: Upload File",
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
            "node": "Edit Fields: Set JSON data to test",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Edit Fields: Set JSON data to test": {
      "main": [
        [
          {
            "node": "QuickChart",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-346"></a>

## Template 346 - Obter data e hora local

- **Nome:** Obter data e hora local
- **Descrição:** Ao ser acionado manualmente, o fluxo obtém a data e hora local com base no fuso horário definido em uma variável de ambiente e retorna componentes e uma string formatada.
- **Funcionalidade:** • Acionamento manual: inicia a execução quando o usuário aciona o gatilho.
• Determinação do fuso horário: utiliza o valor da variável de ambiente GENERIC_TIMEZONE para definir o fuso horário a ser usado.
• Cálculo da data e hora local: obtém o instante atual no fuso horário especificado.
• Extração de componentes: devolve year, month (zero-indexado), day, hour, minute, second e millisecond como campos separados.
• Formatação legível: gera uma string formatada no padrão 'YYYY-MM-DD HH:mm:ss.SSS Z'.
• Saída estruturada: retorna um objeto contendo os campos detalhados e a representação formatada.
- **Ferramentas:** • Moment / Moment-Timezone: biblioteca para manipulação e formatação de datas com suporte a fusos horários.
• Variável de ambiente GENERIC_TIMEZONE: valor que determina o fuso horário usado para calcular a data e hora local.

## Fluxo visual

```mermaid
flowchart LR
    N1["On clicking 'execute'"]
    N2["Get Local Datetime"]

    N1 --> N2
```

## Fluxo (.json) :

```json
{
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        250,
        300
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Get Local Datetime",
      "type": "n8n-nodes-base.function",
      "position": [
        450,
        300
      ],
      "parameters": {
        "functionCode": "const moment = require('moment');\n\nlet date = moment().tz($env['GENERIC_TIMEZONE']);\n\nlet year = date.year();\nlet month = date.month(); // zero-indexed!\nlet day = date.date();\nlet hour = date.hours();\nlet minute = date.minutes();\nlet second = date.seconds();\nlet millisecond = date.millisecond();\nlet formatted = date.format('YYYY-MM-DD HH:mm:ss.SSS Z');\n\nreturn [\n  {\n    json: {\n      utc: date,\n      year: year,\n      month: month, // zero-indexed!\n      day: day,\n      hour: hour,\n      minute: minute,\n      second: second,\n      millisecond: millisecond,\n      formatted: formatted\n    }\n  }\n];\n"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "Get Local Datetime",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-347"></a>

## Template 347 - Triagem automática de CV com IA

- **Nome:** Triagem automática de CV com IA
- **Descrição:** Automatiza o recebimento e a avaliação de candidaturas, extraindo informações dos CVs, gerando resumos, avaliando compatibilidade com um perfil desejado e registrando os resultados.
- **Funcionalidade:** • Recebimento de CVs via formulário: coleta nome, email e arquivo de CV (PDF).
• Upload do CV para armazenamento em nuvem: salva o PDF em uma pasta dedicada.
• Conversão e extração de texto do PDF: transforma o CV em texto para processamento.
• Extração de dados pessoais e qualificações via IA: obtém cidade, telefone, data de nascimento, formação, histórico profissional e habilidades.
• Geração de resumo conciso: produz um resumo de 100 palavras ou menos com as informações mais relevantes.
• Avaliação de compatibilidade com o perfil desejado: compara o candidato com o perfil procurado e atribui uma nota de 1 a 10, incluindo justificativa.
• Registro dos resultados em planilha: acrescenta uma linha com dados pessoais, resumo, habilidades, formação, histórico, nota e considerações.
- **Ferramentas:** • Formulário online: interface para candidatos enviarem nome, email e CV em PDF.
• Google Drive: armazenamento dos arquivos de CV em uma pasta específica.
• Google Sheets: planilha para registrar os dados extraídos, o resumo e a avaliação do candidato.
• OpenAI (modelo de linguagem): usado para extração estruturada de informações, sumarização e avaliação do candidato (ex.: GPT-4o-mini).

## Fluxo visual

```mermaid
flowchart LR
    N1["On form submission"]
    N2["Extract from File"]
    N3["Qualifications"]
    N4["Summarization Chain"]
    N5["Merge"]
    N6["Profile Wanted"]
    N7["Google Sheets"]
    N8["Structured Output Parser"]
    N9["HR Expert"]
    N10["Personal Data"]
    N11["Upload CV"]
    N12["OpenAI"]
    N13["Sticky Note"]
    N14["Sticky Note1"]
    N15["Sticky Note2"]
    N16["Sticky Note3"]
    N17["Sticky Note4"]
    N18["Sticky Note5"]

    N5 --> N4
    N9 --> N7
    N10 --> N5
    N6 --> N9
    N3 --> N5
    N2 --> N3
    N2 --> N10
    N1 --> N2
    N1 --> N11
    N4 --> N6
```

## Fluxo (.json) :

```json
{
  "id": "t1P14FvfibKYCh3E",
  "meta": {
    "instanceId": "a4bfc93e975ca233ac45ed7c9227d84cf5a2329310525917adaf3312e10d5462",
    "templateCredsSetupCompleted": true
  },
  "name": "HR-focused automation pipeline with AI",
  "tags": [],
  "nodes": [
    {
      "id": "b1092f93-502c-4af0-962e-2b69311b92a3",
      "name": "On form submission",
      "type": "n8n-nodes-base.formTrigger",
      "position": [
        -520,
        -200
      ],
      "webhookId": "2a87705d-8ba1-41f1-80ef-85f364ce253e",
      "parameters": {
        "options": {},
        "formTitle": "Send CV",
        "formFields": {
          "values": [
            {
              "fieldLabel": "Name",
              "placeholder": "Name",
              "requiredField": true
            },
            {
              "fieldType": "email",
              "fieldLabel": "Email",
              "placeholder": "Email",
              "requiredField": true
            },
            {
              "fieldType": "file",
              "fieldLabel": "CV",
              "requiredField": true,
              "acceptFileTypes": ".pdf"
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "77edfe2a-4c6a-48c8-8dc9-b275491be090",
      "name": "Extract from File",
      "type": "n8n-nodes-base.extractFromFile",
      "position": [
        -160,
        -200
      ],
      "parameters": {
        "options": {},
        "operation": "pdf",
        "binaryPropertyName": "CV"
      },
      "typeVersion": 1
    },
    {
      "id": "ebf2e194-3515-4c0a-8745-790b63bf336f",
      "name": "Qualifications",
      "type": "@n8n/n8n-nodes-langchain.informationExtractor",
      "position": [
        160,
        -100
      ],
      "parameters": {
        "text": "={{ $json.text }}",
        "options": {
          "systemPromptTemplate": "You are an expert extraction algorithm.\nOnly extract relevant information from the text.\nIf you do not know the value of an attribute asked to extract, you may omit the attribute's value."
        },
        "attributes": {
          "attributes": [
            {
              "name": "Educational qualification",
              "required": true,
              "description": "Summary of your academic career. Focus on your high school and university studies. Summarize in 100 words maximum and also include your grade if applicable."
            },
            {
              "name": "Job History",
              "required": true,
              "description": "Work history summary. Focus on your most recent work experiences. Summarize in 100 words maximum"
            },
            {
              "name": "Skills",
              "required": true,
              "description": "Extract the candidate’s technical skills. What software and frameworks they are proficient in. Make a bulleted list."
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "id": "4f40404c-1d47-4bde-9b4b-16367cf11e4f",
      "name": "Summarization Chain",
      "type": "@n8n/n8n-nodes-langchain.chainSummarization",
      "position": [
        900,
        -220
      ],
      "parameters": {
        "options": {
          "summarizationMethodAndPrompts": {
            "values": {
              "prompt": "=Write a concise summary of the following:\n\nCity: {{ $json.output.city }}\nBirthdate: {{ $json.output.birthdate }}\nEducational qualification: {{ $json.output[\"Educational qualification\"] }}\nJob History: {{ $json.output[\"Job History\"] }}\nSkills: {{ $json.output.Skills }}\n\nUse 100 words or less. Be concise and conversational.",
              "combineMapPrompt": "=Write a concise summary of the following:\n\nCity: {{ $json.output.city }}\nBirthdate: {{ $json.output.birthdate }}\nEducational qualification: {{ $json.output[\"Educational qualification\"] }}\nJob History: {{ $json.output[\"Job History\"] }}\nSkills: {{ $json.output.Skills }}\n\nUse 100 words or less. Be concise and conversational."
            }
          }
        }
      },
      "typeVersion": 2
    },
    {
      "id": "9f9c5f16-1dc2-4928-aef8-284daeb6be51",
      "name": "Merge",
      "type": "n8n-nodes-base.merge",
      "position": [
        660,
        -220
      ],
      "parameters": {
        "mode": "combine",
        "options": {},
        "combineBy": "combineAll"
      },
      "typeVersion": 3
    },
    {
      "id": "51bd14cc-2c54-4f72-b162-255f7e277aff",
      "name": "Profile Wanted",
      "type": "n8n-nodes-base.set",
      "position": [
        1300,
        -220
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "a3d049b0-5a70-4e7b-a6f2-81447da5282a",
              "name": "profile_wanted",
              "type": "string",
              "value": "We are a web agency and we are looking for a full-stack web developer who knows how to use PHP, Python and Javascript. He has experience in the sector and lives in Northern Italy."
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "4a120e5d-b849-4a29-b7f3-12c653552367",
      "name": "Google Sheets",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        1960,
        -220
      ],
      "parameters": {
        "columns": {
          "value": {
            "CITY": "={{ $('Merge').item.json.output.city }}",
            "DATA": "={{ $now.format('dd/LL/yyyy') }}",
            "NAME": "={{ $('On form submission').item.json.Nome }}",
            "VOTE": "={{ $json.output.vote }}",
            "EMAIL": "={{ $('On form submission').item.json.Email }}",
            "SKILLS": "={{ $('Merge').item.json.output.Skills }}",
            "TELEFONO": "={{ $('Merge').item.json.output.telephone }}",
            "SUMMARIZE": "={{ $('Summarization Chain').item.json.response.text }}",
            "EDUCATIONAL": "={{ $('Merge').item.json.output[\"Educational qualification\"] }}",
            "JOB HISTORY": "={{ $('Merge').item.json.output[\"Job History\"] }}",
            "DATA NASCITA": "={{ $('Merge').item.json.output.birthdate }}",
            "CONSIDERATION": "={{ $json.output.consideration }}"
          },
          "schema": [
            {
              "id": "DATA",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "DATA",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "NAME",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "NAME",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "PHONE",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "PHONE",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "CITY",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "CITY",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "EMAIL",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "EMAIL",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "DATA NASCITA",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "DATA NASCITA",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "EDUCATIONAL",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "EDUCATIONAL",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "JOB HISTORY",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "JOB HISTORY",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "SKILLS",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "SKILLS",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "SUMMARIZE",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "SUMMARIZE",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "VOTE",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "VOTE",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "CONSIDERATION",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "CONSIDERATION",
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
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1ssz5RvN1Hr20Q31pnYnbjCLu1MGBvoLttBAjXunMRQE/edit#gid=0",
          "cachedResultName": "Foglio1"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "1ssz5RvN1Hr20Q31pnYnbjCLu1MGBvoLttBAjXunMRQE",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1ssz5RvN1Hr20Q31pnYnbjCLu1MGBvoLttBAjXunMRQE/edit?usp=drivesdk",
          "cachedResultName": "Ricerca WebDev"
        }
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "JYR6a64Qecd6t8Hb",
          "name": "Google Sheets account"
        }
      },
      "typeVersion": 4.5
    },
    {
      "id": "a154d8a5-9f85-45bb-b082-f702c13c3507",
      "name": "Structured Output Parser",
      "type": "@n8n/n8n-nodes-langchain.outputParserStructured",
      "position": [
        1720,
        -20
      ],
      "parameters": {
        "schemaType": "manual",
        "inputSchema": "{\n\t\"type\": \"object\",\n\t\"properties\": {\n\t\t\"vote\": {\n\t\t\t\"type\": \"string\"\n\t\t},\n\t\t\"consideration\": {\n\t\t\t\"type\": \"string\"\n\t\t}\n\t}\n}"
      },
      "typeVersion": 1.2
    },
    {
      "id": "037ac851-7885-4b78-ac75-dfa0ebb6003d",
      "name": "HR Expert",
      "type": "@n8n/n8n-nodes-langchain.chainLlm",
      "position": [
        1560,
        -220
      ],
      "parameters": {
        "text": "=Profilo ricercato:\n{{ $json.profile_wanted }}\n\nCandidato:\n{{ $('Summarization Chain').item.json.response.text }}",
        "messages": {
          "messageValues": [
            {
              "message": "Sei un esperto HR e devi capire se il candidato è in linea con il profilo ricercato dall'azienda.\n\nDevi dare un voto da 1 a 10 dove 1 significa che il candidato non è in linea con quanto richiesto mentre 10 significa che è il candidato ideale perchè rispecchia in toto il profilo cercato.\n\nInoltre nel campo \"consideration\" motiva il perchè hai dato quel voto. "
            }
          ]
        },
        "promptType": "define",
        "hasOutputParser": true
      },
      "typeVersion": 1.5
    },
    {
      "id": "ed5744c4-df06-4a01-a103-af4dd470d482",
      "name": "Personal Data",
      "type": "@n8n/n8n-nodes-langchain.informationExtractor",
      "position": [
        160,
        -280
      ],
      "parameters": {
        "text": "={{ $json.text }}",
        "options": {
          "systemPromptTemplate": "You are an expert extraction algorithm.\nOnly extract relevant information from the text.\nIf you do not know the value of an attribute asked to extract, you may omit the attribute's value."
        },
        "schemaType": "manual",
        "inputSchema": "{\n\t\"type\": \"object\",\n\t\"properties\": {\n\t\t\"telephone\": {\n\t\t\t\"type\": \"string\"\n\t\t},\n      \"city\": {\n\t\t\t\"type\": \"string\"\n\t\t},\n      \"birthdate\": {\n\t\t\t\"type\": \"string\"\n\t\t}\n\t}\n}"
      },
      "typeVersion": 1
    },
    {
      "id": "181c1249-b05c-4c35-8cac-5f9738cc1fe6",
      "name": "Upload CV",
      "type": "n8n-nodes-base.googleDrive",
      "position": [
        -160,
        -380
      ],
      "parameters": {
        "name": "=CV-{{ $now.format('yyyyLLdd') }}-{{ $json.CV[0].filename }}",
        "driveId": {
          "__rl": true,
          "mode": "list",
          "value": "My Drive"
        },
        "options": {},
        "folderId": {
          "__rl": true,
          "mode": "list",
          "value": "1tzeSpx4D3EAGXa3Wg-gqGbdaUk6LIZTV",
          "cachedResultUrl": "https://drive.google.com/drive/folders/1tzeSpx4D3EAGXa3Wg-gqGbdaUk6LIZTV",
          "cachedResultName": "CV"
        },
        "inputDataFieldName": "CV"
      },
      "credentials": {
        "googleDriveOAuth2Api": {
          "id": "HEy5EuZkgPZVEa9w",
          "name": "Google Drive account"
        }
      },
      "typeVersion": 3
    },
    {
      "id": "d31ee1c4-e4be-41d9-8f36-e6fb797ced8e",
      "name": "OpenAI",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        920,
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
          "id": "CDX6QM4gLYanh0P4",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "0290cb72-a581-4aff-8b5d-1aa63e0a630f",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -560,
        -680
      ],
      "parameters": {
        "color": 3,
        "width": 540,
        "content": "## HR Expert \nThis workflow automates the process of handling job applications by extracting relevant information from submitted CVs, analyzing the candidate's qualifications against a predefined profile, and storing the results in a Google Sheet"
      },
      "typeVersion": 1
    },
    {
      "id": "361084ff-9735-4a56-8988-be573391838b",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -240,
        -460
      ],
      "parameters": {
        "width": 300,
        "height": 420,
        "content": "The CV is uploaded to Google Drive and converted so that it can be processed\n"
      },
      "typeVersion": 1
    },
    {
      "id": "4b6f004f-c77b-4522-99d4-737a68f6cfac",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        120,
        -380
      ],
      "parameters": {
        "width": 360,
        "height": 440,
        "content": "The essential information for evaluating the candidate is collected in two different chains"
      },
      "typeVersion": 1
    },
    {
      "id": "73e11af9-65e3-4fcd-bb99-8a3f212ce9fb",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        860,
        -300
      ],
      "parameters": {
        "width": 320,
        "height": 240,
        "content": "Summary of relevant information useful for classifying the candidate"
      },
      "typeVersion": 1
    },
    {
      "id": "606711d1-8e6d-44b3-91ac-c047d8a4054f",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1240,
        -300
      ],
      "parameters": {
        "width": 220,
        "height": 240,
        "content": "Characteristics of the profile sought by the company that intends to hire the candidate"
      },
      "typeVersion": 1
    },
    {
      "id": "89c3210c-c599-41dc-97a3-bf8df2beb751",
      "name": "Sticky Note5",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1500,
        -300
      ],
      "parameters": {
        "width": 360,
        "height": 240,
        "content": "Candidate evaluation with vote and considerations of the HR agent relating the profile sought with the candidate's skills"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "594728c0-b842-404d-8810-c6f7f3f4631d",
  "connections": {
    "Merge": {
      "main": [
        [
          {
            "node": "Summarization Chain",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI": {
      "ai_languageModel": [
        [
          {
            "node": "Qualifications",
            "type": "ai_languageModel",
            "index": 0
          },
          {
            "node": "Summarization Chain",
            "type": "ai_languageModel",
            "index": 0
          },
          {
            "node": "HR Expert",
            "type": "ai_languageModel",
            "index": 0
          },
          {
            "node": "Personal Data",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "HR Expert": {
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
    "Upload CV": {
      "main": [
        []
      ]
    },
    "Personal Data": {
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
    "Profile Wanted": {
      "main": [
        [
          {
            "node": "HR Expert",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Qualifications": {
      "main": [
        [
          {
            "node": "Merge",
            "type": "main",
            "index": 1
          }
        ]
      ]
    },
    "Extract from File": {
      "main": [
        [
          {
            "node": "Qualifications",
            "type": "main",
            "index": 0
          },
          {
            "node": "Personal Data",
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
            "node": "Extract from File",
            "type": "main",
            "index": 0
          },
          {
            "node": "Upload CV",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Summarization Chain": {
      "main": [
        [
          {
            "node": "Profile Wanted",
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
            "node": "HR Expert",
            "type": "ai_outputParser",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-348"></a>

## Template 348 - Upload de foto para SharePoint

- **Nome:** Upload de foto para SharePoint
- **Descrição:** Fluxo que autentica usando credenciais de aplicação, baixa uma imagem de teste e a envia para uma pasta especificada no SharePoint/OneDrive através da API Microsoft Graph.
- **Funcionalidade:** • Configurar credenciais sensíveis: Armazena TENANT_ID, CLIENT_ID e CLIENT_SECRET para uso na autenticação.
• Autenticação via client credentials: Solicita um token de acesso ao endpoint de autenticação da Microsoft usando grant_type=client_credentials.
• Baixar imagem de teste: Faz download de uma imagem pública para usar como arquivo de exemplo.
• Definir destino do arquivo: Define TARGET_FOLDER e FILE_NAME para determinar o caminho de destino no drive.
• Upload de arquivo binário: Envia o conteúdo da imagem para a API Microsoft Graph usando PUT no endpoint de conteúdo do drive.
• Uso demonstrativo de valores em claro: Mantém valores de teste no fluxo para demonstração, com indicação de que em produção devem ser armazenados de forma segura.
- **Ferramentas:** • Microsoft Identity Platform (Azure AD): Emite tokens OAuth2 para autenticação de aplicações com base em TENANT_ID, CLIENT_ID e CLIENT_SECRET.
• Microsoft Graph API / SharePoint / OneDrive: API usada para acessar o drive e gravar o arquivo no caminho especificado (/sites/root/drive/root:...:/content).
• Picsum Photos: Serviço público de imagens usado para fornecer a foto de teste a ser enviada.

## Fluxo visual

```mermaid
flowchart LR
    N1["When clicking ‘Test workflow’"]
    N2["Upload photo"]
    N3["Set config (sensitive data)"]
    N4["Get photo (for testing purposes)"]
    N5["Set destination"]
    N6["Sticky Note"]
    N7["Sticky Note1"]
    N8["Sticky Note2"]
    N9["Authentication"]

    N9 --> N4
    N5 --> N2
    N3 --> N9
    N4 --> N5
    N1 --> N3
```

## Fluxo (.json) :

```json
{
  "meta": {
    "instanceId": "97d44c78f314fab340d7a5edaf7e2c274a7fbb8a7cd138f53cc742341e706fe7",
    "templateCredsSetupCompleted": true
  },
  "nodes": [
    {
      "id": "1ec0e1ad-0666-417b-b5af-b381b06e126f",
      "name": "When clicking ‘Test workflow’",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        -120,
        180
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "c34a92d3-b4bd-4c2f-9fa0-66832729a31c",
      "name": "Upload photo",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        980,
        180
      ],
      "parameters": {
        "url": "=https://graph.microsoft.com/v1.0/sites/root/drive/root:{{ $json.TARGET_FOLDER }}/{{ $json.FILE_NAME }}:/content",
        "method": "PUT",
        "options": {},
        "sendBody": true,
        "contentType": "binaryData",
        "sendHeaders": true,
        "headerParameters": {
          "parameters": [
            {
              "name": "Authorization",
              "value": "=Bearer {{ $json.access_token }}"
            },
            {
              "name": "Content-Type",
              "value": "application/octet-stream"
            }
          ]
        },
        "inputDataFieldName": "data"
      },
      "typeVersion": 4.2
    },
    {
      "id": "49ce594c-83c7-4b47-be03-6811ebdcc57b",
      "name": "Set config (sensitive data)",
      "type": "n8n-nodes-base.set",
      "position": [
        100,
        180
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "399d42f3-41e0-4043-9a57-85771bf5cd07",
              "name": "TENANT_ID",
              "type": "string",
              "value": "00000000-0000-0000-0000-000000000000"
            },
            {
              "id": "dd63a519-3681-46c4-b122-ab379ed11c42",
              "name": "CLIENT_ID",
              "type": "string",
              "value": "00000000-0000-0000-0000-000000000000"
            },
            {
              "id": "4d50c934-c306-4198-853a-68198b8b84eb",
              "name": "CLIENT_SECRET",
              "type": "string",
              "value": "uU~8Q~THEQLIE2TX7UsecretT2g_JCADyxBxN0bx3"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "53b78aa9-d86f-461b-bff5-bd2a63a693b5",
      "name": "Get photo (for testing purposes)",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        540,
        180
      ],
      "parameters": {
        "url": "https://fastly.picsum.photos/id/459/200/300.jpg?hmac=4Cn5sZqOdpuzOwSTs65XA75xvN-quC4t9rfYYyoTCEI",
        "options": {}
      },
      "typeVersion": 4.2
    },
    {
      "id": "a551951c-f192-4b15-accb-ca936baef9a8",
      "name": "Set destination",
      "type": "n8n-nodes-base.set",
      "position": [
        760,
        180
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "9f66b3f9-c161-45f4-bdc0-8cf736b53eda",
              "name": "TARGET_FOLDER",
              "type": "string",
              "value": "/uploads/pictures from n8n"
            },
            {
              "id": "e8584729-2746-48a0-ad80-d0308a49e195",
              "name": "FILE_NAME",
              "type": "string",
              "value": "example.jpg"
            }
          ]
        },
        "includeOtherFields": true
      },
      "typeVersion": 3.4
    },
    {
      "id": "66129973-bf5f-4799-b676-2ee40fd2b519",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -240,
        -220
      ],
      "parameters": {
        "width": 320,
        "height": 200,
        "content": "## Prerequisites\n1. [Create an application user](https://learn.microsoft.com/en-us/power-platform/admin/manage-application-users)\n2. Ensure the following permissions are set:\n- Sites.ReadWrite.All - for SharePoint site access\n- Files.ReadWrite.All - for file upload operations\n"
      },
      "typeVersion": 1
    },
    {
      "id": "43bbf2cd-3ac5-4c46-b3c0-bd6158dbe25e",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        160,
        -280
      ],
      "parameters": {
        "width": 320,
        "height": 340,
        "content": "## Authentication\nFor a succesful authentication it is required to provide:\n\n- TENANT_ID\n- CLIENT_ID\n- CLIENT_SECRET\n---\n## Attention!\nFor demonstration purposes and template restrictions we store these values in a 'Set' node but in production environment please ensure safety of such data via utilizing credentials, secure vault or any other safe way of storing such information."
      },
      "typeVersion": 1
    },
    {
      "id": "daa3e6b9-a9ea-4bb4-8e2d-faa516c699ea",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        620,
        -280
      ],
      "parameters": {
        "width": 440,
        "height": 340,
        "content": "## Set destination\nIn this step we will set the destination.\nThe destination is made of two parameters:\n\n- TARGET_FOLDER\n- FILE_NAME\n---\n### Example\nLet's say this is our desired file location:\n`https://contoso.sharepoint.com/uploads/pictures from n8n/example.jpg`\n\nThus we will set the following:\n- TARGET_FOLDER = `/uploads/pictures from n8n`\n- FILE_NAME = `example.jpg`\n"
      },
      "typeVersion": 1
    },
    {
      "id": "52bd314b-6a5e-499a-904e-a7e9becbbd59",
      "name": "Authentication",
      "type": "n8n-nodes-base.httpRequest",
      "notes": "Get an access token for graph API",
      "position": [
        320,
        180
      ],
      "parameters": {
        "url": "=https://login.microsoftonline.com/{{ $json.TENANT_ID }}/oauth2/token",
        "method": "POST",
        "options": {},
        "sendBody": true,
        "contentType": "form-urlencoded",
        "bodyParameters": {
          "parameters": [
            {
              "name": "grant_type",
              "value": "client_credentials"
            },
            {
              "name": "client_id",
              "value": "={{ $json.CLIENT_ID }}"
            },
            {
              "name": "client_secret",
              "value": "={{ $json.CLIENT_SECRET }}"
            },
            {
              "name": "resource",
              "value": "https://graph.microsoft.com"
            }
          ]
        }
      },
      "notesInFlow": true,
      "typeVersion": 4.2
    }
  ],
  "pinData": {},
  "connections": {
    "Authentication": {
      "main": [
        [
          {
            "node": "Get photo (for testing purposes)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set destination": {
      "main": [
        [
          {
            "node": "Upload photo",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set config (sensitive data)": {
      "main": [
        [
          {
            "node": "Authentication",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get photo (for testing purposes)": {
      "main": [
        [
          {
            "node": "Set destination",
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
            "node": "Set config (sensitive data)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-349"></a>

## Template 349 - Backend AI para extensão Chrome

- **Nome:** Backend AI para extensão Chrome
- **Descrição:** Backend que recebe imagens de gráficos via webhook, envia para um serviço de IA para análise técnica e devolve a análise em texto ao solicitante.
- **Funcionalidade:** • Receber imagem via webhook: aceita requisições HTTP POST contendo imagens em base64 ou dados do gráfico.
• Enviar imagem para análise por IA: encaminha a imagem e um prompt especializado ao serviço de IA para gerar insights técnicos.
• Gerar análise em linguagem simples: produz uma explicação sobre a direção do mercado, indicadores técnicos e um aviso de não ser aconselhamento vinculante, usando linguagem acessível para iniciantes.
• Retornar resposta ao cliente: envia o texto gerado de volta ao remetente como resposta HTTP.
- **Ferramentas:** • OpenAI: serviço de inteligência artificial usado para analisar imagens de gráficos e gerar texto explicativo (modelo gpt-4o-mini).
• Endpoint HTTP/Webhook: ponto de entrada que recebe pedidos da extensão e entrega respostas ao cliente.
• Extensão Chrome (frontend): componente que captura imagens dos gráficos e envia ao backend para receber a análise.

## Fluxo visual

```mermaid
flowchart LR
    N1["Webhook"]
    N2["OpenAI"]
    N3["Respond to Webhook"]
    N4["Sticky Note"]
    N5["Sticky Note1"]

    N2 --> N3
    N1 --> N2
```

## Fluxo (.json) :

```json
{
  "id": "Q8On8rR6BkmPzDUd",
  "meta": {
    "instanceId": "f57770b08f6a574802832e927ed1b0063c627ffc5b95965abf0d4a7396150138"
  },
  "name": "chrome extension backend with AI",
  "tags": [],
  "nodes": [
    {
      "id": "0f38fe62-36d9-43da-a992-a3981377e89e",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "position": [
        -220,
        -20
      ],
      "webhookId": "e9a97dd5-f1e7-4d5b-a6f1-be5f0c9eb96c",
      "parameters": {
        "path": "e9a97dd5-f1e7-4d5b-a6f1-be5f0c9eb96c",
        "options": {},
        "httpMethod": "POST",
        "responseMode": "responseNode"
      },
      "typeVersion": 2
    },
    {
      "id": "83959562-edf5-4d37-bd11-47186c6a31c7",
      "name": "OpenAI",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "position": [
        -40,
        -20
      ],
      "parameters": {
        "text": "You are an expert financial analyst tasked with providing an advanced technical analyses of a stock or crypto currency chart provided. Your analysis will be based on various technical indicators and will provide simple insights for novice traders. Just explain to traders were you expect the market is moving. Also warn them this is not a binding advice. Make sure to explain everything in infant language.",
        "modelId": {
          "__rl": true,
          "mode": "list",
          "value": "gpt-4o-mini",
          "cachedResultName": "GPT-4O-MINI"
        },
        "options": {},
        "resource": "image",
        "inputType": "base64",
        "operation": "analyze"
      },
      "credentials": {
        "openAiApi": {
          "id": "8MS1muoK4z86fxUs",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1.7
    },
    {
      "id": "c6f1f833-7ba3-49c5-86df-f586e6bb5975",
      "name": "Respond to Webhook",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        140,
        -20
      ],
      "parameters": {
        "options": {},
        "respondWith": "text",
        "responseBody": "={{ $json.content }}"
      },
      "typeVersion": 1.1
    },
    {
      "id": "e3a38a76-283b-4567-a8da-315ef1e2bc4f",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -260,
        -140
      ],
      "parameters": {
        "width": 620,
        "height": 300,
        "content": "## N8N en OpenAI image analyser"
      },
      "typeVersion": 1
    },
    {
      "id": "8e7e26db-8767-4727-ab0c-900b50a73411",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -80,
        180
      ],
      "parameters": {
        "color": 5,
        "height": 340,
        "content": "## AI prompt\nYou are an expert financial analyst tasked with providing an advanced technical analyses of a stock or crypto currency chart provided. Your analysis will be based on various technical indicators and will provide simple insights for novice traders. Just explain to traders were you expect the market is moving. Also warn them this is not a binding advice. Make sure to explain everything in infant language."
      },
      "typeVersion": 1
    }
  ],
  "active": true,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "caf32442-e9c5-466a-8888-9abd2c1b3449",
  "connections": {
    "OpenAI": {
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
    "Webhook": {
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

<a id="template-350"></a>

## Template 350 - Servidor MCP para GitHub (ver e comentar issues)

- **Nome:** Servidor MCP para GitHub (ver e comentar issues)
- **Descrição:** Permite que clientes MCP consultem e comentem issues de um repositório GitHub, expondo operações para obter as últimas issues, recuperar comentários de uma issue e adicionar comentários.
- **Funcionalidade:** • Recepção de requisições MCP: aceita chamadas de clientes MCP e roteia para a operação solicitada.
• Recuperar últimas issues: busca as issues mais recentes de um repositório especificado.
• Recuperar comentários de uma issue: obtém os detalhes de uma issue e todos os comentários associados.
• Adicionar comentário a uma issue: cria um comentário em uma issue identificada pelo número.
• Simplificação e agregação de dados: transforma as respostas da API do GitHub em estruturas simplificadas e agrega resultados para resposta única.
• Parametrização de entrada: aceita parâmetros como operação, repositório, número da issue e texto do comentário para controlar o comportamento.
• Integração autenticada com API do GitHub: utiliza credenciais para listar issues, buscar comentários e criar comentários de forma segura.
• Orientações de segurança: recomenda exigir autenticação no servidor MCP antes de uso em produção.
- **Ferramentas:** • GitHub: plataforma para hospedar repositórios, issues e comentários; usada via API autenticada para listar issues, ler comentários e criar comentários.
• Cliente MCP (por exemplo, Claude Desktop): cliente que se conecta ao servidor MCP para enviar solicitações e receber respostas.

## Fluxo visual

```mermaid
flowchart LR
    N1["When Executed by Another Workflow"]
    N2["Operation"]
    N3["Sticky Note"]
    N4["Sticky Note1"]
    N5["Sticky Note3"]
    N6["Github MCP Server"]
    N7["Get Latest Issues"]
    N8["Add Issue Comment"]
    N9["Simplify Issues"]
    N10["Aggregate Results"]
    N11["Get Issue Comments"]
    N12["Get Comments"]
    N13["Simplify Comments"]
    N14["Aggregate Comments"]
    N15["Get Many Issues"]
    N16["Get Single Issue"]
    N17["Create Comment"]
    N18["Get Response"]
    N19["Sticky Note2"]

    N2 --> N15
    N2 --> N16
    N2 --> N17
    N12 --> N13
    N17 --> N18
    N15 --> N9
    N9 --> N10
    N16 --> N12
    N13 --> N14
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
      "id": "b0224d75-763d-4f06-8aa3-3f1b4c5ca96d",
      "name": "When Executed by Another Workflow",
      "type": "n8n-nodes-base.executeWorkflowTrigger",
      "position": [
        800,
        500
      ],
      "parameters": {
        "workflowInputs": {
          "values": [
            {
              "name": "operation"
            },
            {
              "name": "repo"
            },
            {
              "name": "issueNumber"
            },
            {
              "name": "text"
            }
          ]
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "dd0e2ff0-af31-4503-a276-65682a3009a8",
      "name": "Operation",
      "type": "n8n-nodes-base.switch",
      "position": [
        980,
        500
      ],
      "parameters": {
        "rules": {
          "values": [
            {
              "outputKey": "getLatestIssues",
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
                    "rightValue": "getLatestIssues"
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "getIssueComments",
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
                    "rightValue": "getIssueComments"
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "addIssueComment",
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
                    "rightValue": "addIssueComment"
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
      "id": "bc35f181-e3a4-4aa4-8132-26cd4a6ced8a",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        0,
        120
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
      "id": "e4c8d338-08ad-4c47-935b-b5ea53dc59d7",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        700,
        120
      ],
      "parameters": {
        "color": 7,
        "width": 560,
        "height": 300,
        "content": "## 2. Build Simple Support Tools with Github Node\n[Read more about the Github Node](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.github)\n\nWhilst it may be easier to just let the Agent provide the full raw SQL statement,\nit may expose you or your organisation to a real security risk where in the worst\ncase, data may be unknowingly leaked or deleted.\n\nForcing the agent to provide only the parameters of the query\nmeans we can guard somewhat against this risk and also allows\nuse of query parameters as best practice against SQL injection attacks.\n"
      },
      "typeVersion": 1
    },
    {
      "id": "5d6a5f6d-24e8-48ed-8409-8cd24cc2e668",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        0,
        0
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
      "id": "fd11a97d-cd3d-4356-81d3-4266f65ef606",
      "name": "Github MCP Server",
      "type": "@n8n/n8n-nodes-langchain.mcpTrigger",
      "position": [
        160,
        300
      ],
      "webhookId": "61848df7-3619-4ccf-831b-d6408e0d6519",
      "parameters": {
        "path": "61848df7-3619-4ccf-831b-d6408e0d6519"
      },
      "typeVersion": 1
    },
    {
      "id": "b8fd8431-71fa-44d1-abdb-b50e6a8a940f",
      "name": "Get Latest Issues",
      "type": "@n8n/n8n-nodes-langchain.toolWorkflow",
      "position": [
        160,
        540
      ],
      "parameters": {
        "name": "getLatestIssues",
        "workflowId": {
          "__rl": true,
          "mode": "id",
          "value": "={{ $workflow.id }}"
        },
        "description": "Retrieves the latest issues from the github respository.",
        "workflowInputs": {
          "value": {
            "repo": "n8n-io/n8n",
            "text": "null",
            "operation": "getLatestIssues",
            "issueNumber": "null"
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
              "id": "repo",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "repo",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "issueNumber",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "issueNumber",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "text",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "text",
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
      "id": "a11f7b8a-aaa9-41de-a693-6d0463e48d10",
      "name": "Add Issue Comment",
      "type": "@n8n/n8n-nodes-langchain.toolWorkflow",
      "position": [
        480,
        540
      ],
      "parameters": {
        "name": "addIssueComment",
        "workflowId": {
          "__rl": true,
          "mode": "id",
          "value": "={{ $workflow.id }}"
        },
        "description": "Call this tool to add a comment to the github issue.",
        "workflowInputs": {
          "value": {
            "repo": "n8n-io/n8n",
            "text": "={{ /*n8n-auto-generated-fromAI-override*/ $fromAI('text', ``, 'string') }}",
            "operation": "addIssueComment",
            "issueNumber": "={{ /*n8n-auto-generated-fromAI-override*/ $fromAI('issueNumber', ``, 'string') }}"
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
              "id": "repo",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "repo",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "issueNumber",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "issueNumber",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "text",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "text",
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
      "id": "57e8370b-caf0-4632-98e3-78316b2cb262",
      "name": "Simplify Issues",
      "type": "n8n-nodes-base.set",
      "position": [
        1500,
        320
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "6d5eb037-7e52-4595-a2da-bb183674ea2a",
              "name": "issue_number",
              "type": "number",
              "value": "={{ $json.number }}"
            },
            {
              "id": "3d365039-f012-444c-a383-c6c70fb93e9d",
              "name": "title",
              "type": "string",
              "value": "={{ $json.title }}"
            },
            {
              "id": "20a1b658-c56c-4578-9b1f-350b454da2d2",
              "name": "url",
              "type": "string",
              "value": "={{ $json.url }}"
            },
            {
              "id": "0eb6930d-2ea9-4a83-bab7-5f673e79c1d1",
              "name": "reported_by",
              "type": "string",
              "value": "={{ $json.user.login }}"
            },
            {
              "id": "2d71c6de-ab54-4721-9e1c-5193350a5110",
              "name": "state",
              "type": "string",
              "value": "={{ $json.state }}"
            },
            {
              "id": "474166aa-4bfa-4230-bce4-28df2de47bed",
              "name": "created_at",
              "type": "string",
              "value": "={{ $json.created_at }}"
            },
            {
              "id": "e4784fc1-4438-4d7a-a2f5-86be077ae7ae",
              "name": "updated_at",
              "type": "string",
              "value": "={{ $json.updated_at }}"
            },
            {
              "id": "e0639b60-4a08-406a-be8e-c3565a519f0c",
              "name": "body",
              "type": "string",
              "value": "={{ $json.body }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "632b1286-7e4a-457b-8544-6ca8f2affb9f",
      "name": "Aggregate Results",
      "type": "n8n-nodes-base.aggregate",
      "position": [
        1680,
        320
      ],
      "parameters": {
        "options": {},
        "aggregate": "aggregateAllItemData",
        "destinationFieldName": "response"
      },
      "typeVersion": 1
    },
    {
      "id": "447327bc-0b42-47ec-80c0-14d6f521d047",
      "name": "Get Issue Comments",
      "type": "@n8n/n8n-nodes-langchain.toolWorkflow",
      "position": [
        320,
        600
      ],
      "parameters": {
        "name": "getIssueComments",
        "workflowId": {
          "__rl": true,
          "mode": "id",
          "value": "={{ $workflow.id }}"
        },
        "description": "Retrieves the issue and associated comments and discussion",
        "workflowInputs": {
          "value": {
            "repo": "n8n-io/n8n",
            "text": "null",
            "operation": "getIssueComments",
            "issueNumber": "={{ /*n8n-auto-generated-fromAI-override*/ $fromAI('issueNumber', ``, 'string') }}"
          },
          "schema": [
            {
              "id": "operation",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "operation",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "repo",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "repo",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "issueNumber",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "issueNumber",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "text",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "text",
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
      "id": "f5c59a05-54e4-4aa5-bef3-192e07adffb0",
      "name": "Get Comments",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1500,
        500
      ],
      "parameters": {
        "url": "={{ $json.comments_url }}",
        "options": {},
        "authentication": "predefinedCredentialType",
        "nodeCredentialType": "githubApi"
      },
      "credentials": {
        "githubApi": {
          "id": "kA70YRmLeHDqZbXA",
          "name": "GitHub account"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "3fe80456-9fb5-47bb-80d9-484123571a8f",
      "name": "Simplify Comments",
      "type": "n8n-nodes-base.set",
      "position": [
        1680,
        500
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "6e09ed44-a72c-4915-84f4-0796b45158a7",
              "name": "id",
              "type": "number",
              "value": "={{ $json.id }}"
            },
            {
              "id": "76c34251-7f40-42bc-bb98-17e7fe52d9ed",
              "name": "issue_url",
              "type": "string",
              "value": "={{ $json.issue_url }}"
            },
            {
              "id": "1094dd36-d18d-4ada-ac49-5347f0f245ae",
              "name": "user",
              "type": "string",
              "value": "={{ $json.user.login }}"
            },
            {
              "id": "59b50536-4e0a-46bc-919b-685066253f45",
              "name": "author_association",
              "type": "string",
              "value": "={{ $json.author_association }}"
            },
            {
              "id": "6253bae9-aaff-4a88-9e5a-64126ed80cc4",
              "name": "body",
              "type": "string",
              "value": "={{ $json.body }}"
            },
            {
              "id": "3944598d-8204-45a0-9e0b-448d3cfa5a87",
              "name": "created_at",
              "type": "string",
              "value": "={{ $json.created_at }}"
            },
            {
              "id": "3f395b51-6e57-4d07-9cf9-9a03e7a40c51",
              "name": "updated_at",
              "type": "string",
              "value": "={{ $json.updated_at }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "7926ae2d-5408-4b10-88f3-e6ebfe5f9619",
      "name": "Aggregate Comments",
      "type": "n8n-nodes-base.aggregate",
      "position": [
        1860,
        500
      ],
      "parameters": {
        "options": {},
        "aggregate": "aggregateAllItemData",
        "destinationFieldName": "response"
      },
      "typeVersion": 1
    },
    {
      "id": "af2b4c0f-4a83-44a2-bae8-b3c45861d820",
      "name": "Get Many Issues",
      "type": "n8n-nodes-base.github",
      "position": [
        1320,
        320
      ],
      "webhookId": "e08dcf3e-66bb-4ba5-a868-d8c41a98bc95",
      "parameters": {
        "limit": 10,
        "owner": {
          "__rl": true,
          "mode": "name",
          "value": "={{ $json.repo.split('/')[0] }}"
        },
        "resource": "repository",
        "repository": {
          "__rl": true,
          "mode": "name",
          "value": "={{ $json.repo.split('/')[1] }}"
        },
        "getRepositoryIssuesFilters": {
          "sort": "created"
        }
      },
      "credentials": {
        "githubApi": {
          "id": "kA70YRmLeHDqZbXA",
          "name": "GitHub account"
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "50568171-5f46-4338-a799-a1854ebc425e",
      "name": "Get Single Issue",
      "type": "n8n-nodes-base.github",
      "position": [
        1320,
        500
      ],
      "webhookId": "e08dcf3e-66bb-4ba5-a868-d8c41a98bc95",
      "parameters": {
        "owner": {
          "__rl": true,
          "mode": "name",
          "value": "={{ $json.repo.split('/')[0] }}"
        },
        "operation": "get",
        "repository": {
          "__rl": true,
          "mode": "name",
          "value": "={{ $json.repo.split('/')[1] }}"
        },
        "issueNumber": "={{ $json.issueNumber }}"
      },
      "credentials": {
        "githubApi": {
          "id": "kA70YRmLeHDqZbXA",
          "name": "GitHub account"
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "1a12fadd-e436-4731-ad66-b9d9cdb9c61c",
      "name": "Create Comment",
      "type": "n8n-nodes-base.github",
      "position": [
        1320,
        680
      ],
      "webhookId": "e08dcf3e-66bb-4ba5-a868-d8c41a98bc95",
      "parameters": {
        "body": "={{ $json.text }}",
        "owner": {
          "__rl": true,
          "mode": "name",
          "value": "={{ $json.repo.split('/')[0] }}"
        },
        "operation": "createComment",
        "repository": {
          "__rl": true,
          "mode": "name",
          "value": "={{ $json.repo.split('/')[1] }}"
        },
        "issueNumber": "={{ $json.issueNumber }}"
      },
      "credentials": {
        "githubApi": {
          "id": "kA70YRmLeHDqZbXA",
          "name": "GitHub account"
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "b90acf56-c871-49de-95d0-1c6ceb1799f7",
      "name": "Get Response",
      "type": "n8n-nodes-base.set",
      "position": [
        1500,
        680
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "65631bfa-7448-4188-8cc1-b812361ae9b1",
              "name": "response",
              "type": "string",
              "value": "ok"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "da360f61-4251-4f0f-8081-3b502e9981c9",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -460,
        -480
      ],
      "parameters": {
        "width": 440,
        "height": 1260,
        "content": "## Try It Out!\n### This n8n demonstrates how to build your own Github MCP server to personalise it to your organisation's repositories, issues and pull requests.\n\nThis n8n implementation, though not as fully featured as the official MCP server offered by Github, allows you to control precisely what access and/or functionality is granted to users which can make MCP use simpler and in some cases, more secure. The use-case in this template is to simply view and comment on issues within a specific repository but can be extended to meet the needs of your team.\n\nThis MCP example is based off an official MCP reference implementation which can be found here https://github.com/modelcontextprotocol/servers/tree/main/src/github\n\n### How it works\n* A MCP server trigger is used and connected to 3 custom workflow tools. We're using custom workflow tools as there is quite a few nodes required for each task.\n* Behind these tools are regular Github nodes although preconfigured with credentials and targeted repository.\n* The \"Get Issue Comments\" and \"Create Issue Comment\" tools depend on obtaining an Issue Number first. The agent should call the \"Get Latest Issues\" tool for this.\n\n### How to use\n* This Github MCP server allows any compatible MCP client to view and comment on Github Issues. You will need to have a Github account and repository access available before you can use this server.\n* Connect your MCP client by following the n8n guidelines here - https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger/#integrating-with-claude-desktop\n* Try the following queries in your MCP client:\n  * \"Can you get me the latest issues about MCP?\"\n  * \"What is the current progress on Issue 12345?\"\n  * \"Please can you add a comment to Issue 12345 that they should try installing the latest version and see if that works?\"\n\n### Requirements\n* Github for account and repository access. The repository need not be your own but you'll still need to ensure you have the correct permissions.\n* MCP Client or Agent for usage such as Claude Desktop - https://claude.ai/download\n\n### Customising this workflow\n* Extend this template to interactive with pull requests or workflows within your own company's Github repositories. Alternatively,  pull in metrics and generate reports for programme managers.\n* Remember to set the MCP server to require credentials before going to production and sharing this MCP server with others!"
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
            "node": "Get Many Issues",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Get Single Issue",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Create Comment",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Comments": {
      "main": [
        [
          {
            "node": "Simplify Comments",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Create Comment": {
      "main": [
        [
          {
            "node": "Get Response",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Many Issues": {
      "main": [
        [
          {
            "node": "Simplify Issues",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Simplify Issues": {
      "main": [
        [
          {
            "node": "Aggregate Results",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Single Issue": {
      "main": [
        [
          {
            "node": "Get Comments",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Add Issue Comment": {
      "ai_tool": [
        [
          {
            "node": "Github MCP Server",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Get Latest Issues": {
      "ai_tool": [
        [
          {
            "node": "Github MCP Server",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Simplify Comments": {
      "main": [
        [
          {
            "node": "Aggregate Comments",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Issue Comments": {
      "ai_tool": [
        [
          {
            "node": "Github MCP Server",
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

<a id="template-351"></a>

## Template 351 - Agente de IA acionado por Siri

- **Nome:** Agente de IA acionado por Siri
- **Descrição:** Recebe entrada falada via atalho do Siri, envia para um agente de IA que gera uma resposta curta e a devolve para ser ditada pelo Siri.
- **Funcionalidade:** • Receber entrada pelo atalho: Aceita requisições HTTP enviadas pelo atalho do Apple Shortcuts com a transcrição da fala.
• Processamento com contexto: Insere informações de contexto (data, hora e instruções do sistema) antes de enviar ao agente de IA.
• Geração de resposta concisa: Utiliza um modelo de linguagem para produzir respostas curtas e otimizadas para entrega por voz.
• Responder ao atalho: Retorna a resposta em texto para que o Siri a dite ao usuário.
• Configuração de credenciais e URL: Permite configurar a credencial do serviço de IA e fornece o URL de produção para o atalho.
• Extensibilidade do contexto: Suporta adicionar mais contexto (por exemplo dados de apps) para personalizar respostas.
- **Ferramentas:** • Apple Shortcuts: Atalho no iOS/macOS que captura a fala do usuário e envia a requisição ao fluxo.
• Siri: Assistente de voz que ativa o atalho e reproduz a resposta ditada.
• Serviço de modelo de linguagem (ex.: OpenAI - gpt-4o-mini ou alternativas como Groq): Gera a resposta textual a partir da entrada e do contexto.
• Endpoint HTTP/Webhook: URL público que recebe as requisições do atalho e encaminha para processamento.

## Fluxo visual

```mermaid
flowchart LR
    N1["OpenAI Chat Model"]
    N2["Sticky Note"]
    N3["Respond to Apple Shortcut"]
    N4["Sticky Note1"]
    N5["Sticky Note2"]
    N6["AI Agent"]
    N7["When called by Apple Shortcut"]

    N6 --> N3
    N7 --> N6
```

## Fluxo (.json) :

```json
{
  "meta": {
    "instanceId": "205b3bc06c96f2dc835b4f00e1cbf9a937a74eeb3b47c99d0c30b0586dbf85aa",
    "templateId": "2436"
  },
  "nodes": [
    {
      "id": "b24c6e28-3c9e-4069-9e87-49b2efd47257",
      "name": "OpenAI Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        1200,
        660
      ],
      "parameters": {
        "model": "gpt-4o-mini",
        "options": {}
      },
      "credentials": {
        "openAiApi": {
          "id": "AzPPV759YPBxJj3o",
          "name": "Max's DevRel OpenAI account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "c71a3e22-f0fd-4377-9be2-32438b282430",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        200,
        240
      ],
      "parameters": {
        "color": 7,
        "width": 636.2128494576581,
        "height": 494.9629292914819,
        "content": "![Siri Template Thumbnail](https://uploads.n8n.io/devrel/wf-siri-header.png#full-width)\n## \"Hey Siri, Ask Agent\" workflow\n**Made by [Max Tkacz](https://www.linkedin.com/in/maxtkacz) during the [30 Day AI Sprint](https://30dayaisprint.notion.site/)**\n\nThis template integrates with Apple Shortcuts to trigger an n8n AI Agent via a \"Hey Siri\" command. The shortcut prompts for spoken input, transcribes it, and sends it to the workflow's `When Called by Apple Shortcut` Webhook trigger. The AI Agent processes the input and Siri dictates the response back to you.\n\nThe workflow also passes the current date and time to the `AI Agent`, which you can extend with additional context, like data from an App node, for more customized responses.\n\n"
      },
      "typeVersion": 1
    },
    {
      "id": "a4ec93c3-eefa-4006-b02c-f995fb7bc410",
      "name": "Respond to Apple Shortcut",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        1640,
        460
      ],
      "parameters": {
        "options": {},
        "respondWith": "text",
        "responseBody": "={{ $json.output }}"
      },
      "typeVersion": 1.1
    },
    {
      "id": "942b284e-e26a-4534-8f33-eb92b0a88fdb",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        200,
        760
      ],
      "parameters": {
        "color": 7,
        "width": 280.2462120317618,
        "height": 438.5821431288714,
        "content": "### Set up steps\n1. Add an OpenAI API credential in `OpenAI Chat Model` node, or replace it with another model. Try `Groq` if you want a free alternative (can be used with free Groq account, no CC).\n2. Copy the \"Production URL\" from `When called by Apple Shortcut` node, you'll need this when setting up the shortcut.\n3. Save and activate this n8n workflow.\n4. Download the [Apple Shortcut here](https://uploads.n8n.io/devrel/ask-agent.shortcut), open it on macOS or iOS. This adds the shortcut to your device.\n5. Open the shortcut and swap URL in `Get contents of\" step to the \"Production URL\" you copied from `When called by Apple Shortcut`.\n6. Test it by saying \"Hey Siri, AI Agent\", then ask a question."
      },
      "typeVersion": 1
    },
    {
      "id": "ebb9e886-546a-429c-b4b5-35c0a7b6370e",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        503.6292958565226,
        760
      ],
      "parameters": {
        "color": 7,
        "width": 330.5152611046425,
        "height": 240.6839895136402,
        "content": "### ... or watch set up video [5 min]\n[![Siri Template Thumbnail](https://uploads.n8n.io/devrel/thumb-siri.png#full-width)](https://youtu.be/dewsB-4iGA8)\n"
      },
      "typeVersion": 1
    },
    {
      "id": "5a842fa9-be8c-4ba8-996b-a26a53273b3f",
      "name": "AI Agent",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        1240,
        460
      ],
      "parameters": {
        "text": "=Here is my request: {{ $json.body.input }}\n",
        "agent": "conversationalAgent",
        "options": {
          "systemMessage": "=## Task\nYou are a helpful assistant. Provide concise replies as the user receives them via voice on their mobile phone. Avoid using symbols like \"\\n\" to prevent them from being narrated.\n\n## Context\n- Today is {{ $now.format('dd LLL yy') }}.\n- Current time: {{ $now.format('h:mm a') }} in Berlin, Germany.\n- When asked, you are an AI Agent running as an n8n workflow.\n\n## Output\nKeep responses short and clear, optimized for voice delivery. Don't hallucinate, if you don't know the answer, say you don't know. "
        },
        "promptType": "define",
        "hasOutputParser": true
      },
      "typeVersion": 1.6
    },
    {
      "id": "598d22d5-7472-44c5-ab2e-69c8bbb23ddd",
      "name": "When called by Apple Shortcut",
      "type": "n8n-nodes-base.webhook",
      "position": [
        980,
        460
      ],
      "webhookId": "f0224b4b-1644-4d3d-9f12-01a9c04879e4",
      "parameters": {
        "path": "assistant",
        "options": {},
        "httpMethod": "POST",
        "responseMode": "responseNode"
      },
      "typeVersion": 2
    }
  ],
  "pinData": {},
  "connections": {
    "AI Agent": {
      "main": [
        [
          {
            "node": "Respond to Apple Shortcut",
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
    "When called by Apple Shortcut": {
      "main": [
        [
          {
            "node": "AI Agent",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-352"></a>

## Template 352 - Indexação e busca de ensaios com Milvus

- **Nome:** Indexação e busca de ensaios com Milvus
- **Descrição:** Coleta ensaios do site de Paul Graham, transforma o texto em vetores e carrega em um banco Milvus para permitir consultas por meio de um agente conversacional.
- **Funcionalidade:** • Coleta de links de ensaios: acessa a página de artigos e extrai os links dos ensaios.
• Limitação de itens processados: processa apenas os primeiros 3 ensaios para carregamento rápido.
• Extração de texto limpo: busca cada ensaio e extrai o conteúdo textual, ignorando imagens e navegação.
• Divisão de texto em fragmentos: fragmenta os textos com tamanho configurado (chunkSize 6000) para indexação eficiente.
• Geração de embeddings: usa serviço de embeddings para transformar fragmentos textuais em vetores.
• Inserção em banco de vetores: limpa e popula uma coleção Milvus (nomeada) com os vetores gerados.
• Disponibilização como ferramenta de busca: configura o armazenamento vetorial para ser utilizado como ferramenta de recuperação por um agente de IA.
• Agente conversacional integrado: permite receber mensagens de chat e utilizar a base vetorial para responder consultas relevantes.
- **Ferramentas:** • Milvus: banco de dados vetorial usado para armazenar e recuperar embeddings (coleção configurada para limpeza e inserção).
• OpenAI: fornece o modelo de chat (ex.: gpt-4o-mini) e o serviço de embeddings para criar vetores a partir do texto.
• paulgraham.com: fonte pública dos ensaios que são raspados e processados para indexação.

## Fluxo visual

```mermaid
flowchart LR
    N1["When clicking 'Execute Workflow'"]
    N2["Fetch Essay List"]
    N3["Extract essay names"]
    N4["Split out into items"]
    N5["Fetch essay texts"]
    N6["Limit to first 3"]
    N7["Extract Text Only"]
    N8["Sticky Note3"]
    N9["Sticky Note5"]
    N10["Recursive Character Text Splitter1"]
    N11["Milvus Vector Store"]
    N12["AI Agent"]
    N13["When chat message received"]
    N14["Sticky Note"]
    N15["Default Data Loader"]
    N16["Milvus Vector Store as tool"]
    N17["Sticky Note1"]
    N18["Embeddings OpenAI"]
    N19["OpenAI Chat Model"]
    N20["Embeddings OpenAI1"]
    N21["Sticky Note2"]

    N2 --> N3
    N6 --> N5
    N7 --> N11
    N5 --> N7
    N3 --> N4
    N4 --> N6
    N13 --> N12
    N1 --> N2
```

## Fluxo (.json) :

```json
{
  "id": "A5R7XYSzrCJKlw9k",
  "meta": {
    "instanceId": "2c4c1e23e7b067270c08aab616bada21d0c384d16f212b23cf1143c6baa09219",
    "templateCredsSetupCompleted": true
  },
  "name": "Agent Milvus tool",
  "tags": [
    {
      "id": "msnDWKHQmwMDxWQH",
      "name": "Milvus",
      "createdAt": "2025-04-16T12:48:14.539Z",
      "updatedAt": "2025-04-16T12:48:14.539Z"
    },
    {
      "id": "tnCpo8hq8uKrdASK",
      "name": "AI",
      "createdAt": "2025-04-16T12:47:57.976Z",
      "updatedAt": "2025-04-16T12:47:57.976Z"
    }
  ],
  "nodes": [
    {
      "id": "cfe6264a-2be1-4d1e-974b-ee05ca8ae9ab",
      "name": "When clicking \"Execute Workflow\"",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        -280,
        -40
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "c0665cc9-2bce-48db-a3bc-15baac68e569",
      "name": "Fetch Essay List",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        -20,
        -40
      ],
      "parameters": {
        "url": "http://www.paulgraham.com/articles.html",
        "options": {}
      },
      "typeVersion": 4.2
    },
    {
      "id": "00bcdc0b-eb6d-41eb-ac0d-a6710d6232e4",
      "name": "Extract essay names",
      "type": "n8n-nodes-base.html",
      "position": [
        180,
        -40
      ],
      "parameters": {
        "options": {},
        "operation": "extractHtmlContent",
        "extractionValues": {
          "values": [
            {
              "key": "essay",
              "attribute": "href",
              "cssSelector": "table table a",
              "returnArray": true,
              "returnValue": "attribute"
            }
          ]
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "523c319e-d1c7-4214-a725-dc557f6471a2",
      "name": "Split out into items",
      "type": "n8n-nodes-base.splitOut",
      "position": [
        380,
        -40
      ],
      "parameters": {
        "options": {},
        "fieldToSplitOut": "essay"
      },
      "typeVersion": 1
    },
    {
      "id": "be155368-99f5-43b3-ba6c-50cccf2b72d2",
      "name": "Fetch essay texts",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        780,
        -40
      ],
      "parameters": {
        "url": "=http://www.paulgraham.com/{{ $json.essay }}",
        "options": {}
      },
      "typeVersion": 4.2
    },
    {
      "id": "92af113c-dd71-4ddd-b50a-f5932392ed82",
      "name": "Limit to first 3",
      "type": "n8n-nodes-base.limit",
      "position": [
        580,
        -40
      ],
      "parameters": {
        "maxItems": 3
      },
      "typeVersion": 1
    },
    {
      "id": "1a1893c4-e8b2-454a-b49f-a0b0f3c01aca",
      "name": "Extract Text Only",
      "type": "n8n-nodes-base.html",
      "position": [
        1100,
        -40
      ],
      "parameters": {
        "options": {},
        "operation": "extractHtmlContent",
        "extractionValues": {
          "values": [
            {
              "key": "data",
              "cssSelector": "body",
              "skipSelectors": "img,nav"
            }
          ]
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "d14ae606-f002-4fde-a896-bf1c7fa675b2",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -100,
        -160
      ],
      "parameters": {
        "width": 1071.752021563343,
        "height": 285.66037735849045,
        "content": "## Scrape latest Paul Graham essays"
      },
      "typeVersion": 1
    },
    {
      "id": "dfb0cb32-9d7c-4588-b75e-0b79231eb72a",
      "name": "Sticky Note5",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1020,
        -160
      ],
      "parameters": {
        "width": 625,
        "height": 607,
        "content": "## Load into Milvus vector database"
      },
      "typeVersion": 1
    },
    {
      "id": "862a1a02-50e2-42af-9fa9-eb3a4f2ca463",
      "name": "Recursive Character Text Splitter1",
      "type": "@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter",
      "position": [
        1440,
        300
      ],
      "parameters": {
        "options": {},
        "chunkSize": 6000
      },
      "typeVersion": 1
    },
    {
      "id": "91ac110a-57db-44b1-b22f-d2a63f22f173",
      "name": "Milvus Vector Store",
      "type": "@n8n/n8n-nodes-langchain.vectorStoreMilvus",
      "position": [
        1320,
        -40
      ],
      "parameters": {
        "mode": "insert",
        "options": {
          "clearCollection": true
        },
        "milvusCollection": {
          "__rl": true,
          "mode": "list",
          "value": "n8n_test",
          "cachedResultName": "n8n_test"
        }
      },
      "credentials": {
        "milvusApi": {
          "id": "8tMHHoLiWXIAXa7S",
          "name": "Milvus account"
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "456e917f-d466-4ec8-8df9-3774ba58151d",
      "name": "AI Agent",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        60,
        360
      ],
      "parameters": {
        "options": {}
      },
      "typeVersion": 1.9
    },
    {
      "id": "a5c5f308-097d-4fe0-92be-d717fd1e0b74",
      "name": "When chat message received",
      "type": "@n8n/n8n-nodes-langchain.chatTrigger",
      "position": [
        -280,
        360
      ],
      "webhookId": "cd2703a7-f912-46fe-8787-3fb83ea116ab",
      "parameters": {
        "options": {}
      },
      "typeVersion": 1.1
    },
    {
      "id": "dc352f07-335f-47cb-8270-32a4a0b87df7",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -460,
        -200
      ],
      "parameters": {
        "width": 280,
        "height": 180,
        "content": "## Step 1\n1. Set up a Milvus server based on [this guide](https://milvus.io/docs/install_standalone-docker-compose.md). And then create a collection named `n8n_test`.\n2. Click this workflow to load scrape and load Paul Graham essays to Milvus collection.\n"
      },
      "typeVersion": 1
    },
    {
      "id": "5c9e9871-c9c1-458e-b35c-eab87ac5ca26",
      "name": "Default Data Loader",
      "type": "@n8n/n8n-nodes-langchain.documentDefaultDataLoader",
      "position": [
        1360,
        180
      ],
      "parameters": {
        "options": {},
        "jsonData": "={{ $('Extract Text Only').item.json.data }}",
        "jsonMode": "expressionData"
      },
      "typeVersion": 1
    },
    {
      "id": "5b202001-525c-4481-a263-56b69c9b1bd8",
      "name": "Milvus Vector Store as tool",
      "type": "@n8n/n8n-nodes-langchain.vectorStoreMilvus",
      "position": [
        180,
        560
      ],
      "parameters": {
        "mode": "retrieve-as-tool",
        "toolName": "milvus_knowledge_base",
        "toolDescription": "useful when you need to retrieve information",
        "milvusCollection": {
          "__rl": true,
          "mode": "list",
          "value": "n8n_test",
          "cachedResultName": "n8n_test"
        }
      },
      "credentials": {
        "milvusApi": {
          "id": "8tMHHoLiWXIAXa7S",
          "name": "Milvus account"
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "6b5b95c7-dde2-4c3f-952b-97a8f5c267c9",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -460,
        260
      ],
      "parameters": {
        "width": 280,
        "height": 120,
        "content": "## Step 2\nStart to chat with the AI Agent with Milvus tool"
      },
      "typeVersion": 1
    },
    {
      "id": "5ccfe636-2bb3-4026-98f0-57ba8d5780f0",
      "name": "Embeddings OpenAI",
      "type": "@n8n/n8n-nodes-langchain.embeddingsOpenAi",
      "position": [
        1220,
        200
      ],
      "parameters": {
        "options": {}
      },
      "credentials": {
        "openAiApi": {
          "id": "hH2PTDH4fbS7fdPv",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "982622e9-af05-4ee2-ae7d-166c47f75ce9",
      "name": "OpenAI Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        20,
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
          "id": "hH2PTDH4fbS7fdPv",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "abd97878-cce6-44a0-8bae-91536ea48b6b",
      "name": "Embeddings OpenAI1",
      "type": "@n8n/n8n-nodes-langchain.embeddingsOpenAi",
      "position": [
        200,
        740
      ],
      "parameters": {
        "options": {}
      },
      "credentials": {
        "openAiApi": {
          "id": "hH2PTDH4fbS7fdPv",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "00d49aab-3200-44fc-a0fc-8f7f22998617",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -80,
        300
      ],
      "parameters": {
        "color": 7,
        "width": 574,
        "height": 629,
        "content": ""
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "8e6f0bb5-1fb5-48fc-8a1f-488362be4ef7",
  "connections": {
    "Fetch Essay List": {
      "main": [
        [
          {
            "node": "Extract essay names",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Limit to first 3": {
      "main": [
        [
          {
            "node": "Fetch essay texts",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Embeddings OpenAI": {
      "ai_embedding": [
        [
          {
            "node": "Milvus Vector Store",
            "type": "ai_embedding",
            "index": 0
          }
        ]
      ]
    },
    "Extract Text Only": {
      "main": [
        [
          {
            "node": "Milvus Vector Store",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Fetch essay texts": {
      "main": [
        [
          {
            "node": "Extract Text Only",
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
    "Embeddings OpenAI1": {
      "ai_embedding": [
        [
          {
            "node": "Milvus Vector Store as tool",
            "type": "ai_embedding",
            "index": 0
          }
        ]
      ]
    },
    "Default Data Loader": {
      "ai_document": [
        [
          {
            "node": "Milvus Vector Store",
            "type": "ai_document",
            "index": 0
          }
        ]
      ]
    },
    "Extract essay names": {
      "main": [
        [
          {
            "node": "Split out into items",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Split out into items": {
      "main": [
        [
          {
            "node": "Limit to first 3",
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
            "node": "AI Agent",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Milvus Vector Store as tool": {
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
    "When clicking \"Execute Workflow\"": {
      "main": [
        [
          {
            "node": "Fetch Essay List",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Recursive Character Text Splitter1": {
      "ai_textSplitter": [
        [
          {
            "node": "Default Data Loader",
            "type": "ai_textSplitter",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-353"></a>

## Template 353 - Resumo de vídeos YouTube e chat via Telegram

- **Nome:** Resumo de vídeos YouTube e chat via Telegram
- **Descrição:** Recebe URLs de vídeos do YouTube, extrai a transcrição, gera um resumo estruturado com o modelo GPT-4o-mini e permite conversas sobre o conteúdo via Telegram.
- **Funcionalidade:** • Recepção de URLs: Aceita URLs de vídeo via webhook ou mensagem no Telegram.
• Extração de ID do vídeo: Analisa a URL para obter o identificador do vídeo.
• Obtenção de transcrição: Recupera a transcrição/legenda do vídeo a partir do serviço de transcrição do YouTube.
• Segmentação da transcrição: Divide a transcrição em segmentos para processamento mais eficiente.
• Concatenação e armazenamento: Concatena os segmentos e atualiza ou armazena a transcrição completa em um documento para referência posterior.
• Geração de resumo estruturado: Usa o modelo GPT-4o-mini para produzir um resumo formatado com seção geral, momentos-chave e instruções quando aplicável.
• Envio de resumo: Entrega o resumo gerado de volta ao usuário via Telegram e responde ao webhook quando necessário.
• Assistente interativo: Permite que usuários enviem perguntas pelo Telegram sobre o vídeo; o agente consulta a transcrição armazenada antes de responder.
• Memória de sessão: Mantém um buffer de memória por sessão para contextualizar conversas e perguntas subsequentes.
- **Ferramentas:** • Telegram: Canal de entrada e saída para mensagens dos usuários (envio de URLs e recebimento de resumos/respostas).
• OpenAI (gpt-4o-mini): Gera resumos estruturados e responde a perguntas sobre o conteúdo da transcrição.
• Serviço de transcrição do YouTube: Fornece a transcrição/legendas do vídeo a partir do ID do vídeo.
• Google Docs: Armazena e atualiza a transcrição completa para referência e pesquisa pelo agente de resposta.
• Webhook endpoint: Ponto HTTP para receber URLs de vídeo ou eventos externos diretamente.

## Fluxo visual

```mermaid
flowchart LR
    N1["Split Transcript into Segments"]
    N2["Extract YouTube URL from Input"]
    N3["Extract Video ID from URL"]
    N4["gpt-4o-mini"]
    N5["Generate Summary with GPT-4o-mini"]
    N6["Concatenate Transcript Segments"]
    N7["Trigger on Telegram Message"]
    N8["Extract YouTube Transcript"]
    N9["Send Summary via Telegram"]
    N10["Receive YouTube URL via Webhook"]
    N11["Send Response to Webhook"]
    N12["Telegram Trigger"]
    N13["Retrieve Transcript from Google Docs"]
    N14["Update Transcript in Google Docs"]
    N15["Handle User Questions via AI"]
    N16["OpenAI Chat Model"]
    N17["Window Buffer Memory"]
    N18["Google Docs2"]
    N19["Send AI Response via Telegram"]
    N20["Sticky Note"]
    N21["Sticky Note1"]
    N22["Sticky Note2"]

    N12 --> N15
    N3 --> N8
    N9 --> N11
    N8 --> N1
    N7 --> N2
    N15 --> N19
    N2 --> N3
    N1 --> N6
    N6 --> N5
    N6 --> N13
    N10 --> N2
    N5 --> N9
    N13 --> N14
```

## Fluxo (.json) :

```json
{
  "id": "KgoL0qrLYZUJFuAS",
  "meta": {
    "instanceId": "53cd73f110e7e1f0aa170e039c302b8f2a1790f1200f176610cac2d761dfa4b7"
  },
  "name": "Summarize YouTube Videos & Chat About Content with GPT-4o-mini via Telegram",
  "tags": [],
  "nodes": [
    {
      "id": "a9cb4358-f9ec-4d81-9422-f1b7133f1f2a",
      "name": "Split Transcript into Segments",
      "type": "n8n-nodes-base.splitOut",
      "position": [
        800,
        680
      ],
      "parameters": {
        "options": {},
        "fieldToSplitOut": "transcript"
      },
      "typeVersion": 1
    },
    {
      "id": "03650773-fd85-4ecb-a218-0d18e2f88e68",
      "name": "Extract YouTube URL from Input",
      "type": "n8n-nodes-base.set",
      "position": [
        580,
        220
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "3ee42e4c-3cee-4934-97e7-64c96b5691ed",
              "name": "youtubeUrl",
              "type": "string",
              "value": "={{ $json.chatInput || $json.query.url}}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "9b55683c-6b04-44e6-8af2-ef69a50e783a",
      "name": "Extract Video ID from URL",
      "type": "n8n-nodes-base.code",
      "position": [
        580,
        460
      ],
      "parameters": {
        "language": "python",
        "pythonCode": "# Loop over input items and add a new field called 'myNewField' to the JSON of each one\nfor item in _input.all():\n  item.json.myNewField = 1\nreturn _input.all()"
      },
      "typeVersion": 2
    },
    {
      "id": "8552bb5d-c857-4a4e-b97b-7482b5e97244",
      "name": "gpt-4o-mini",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        1280,
        960
      ],
      "parameters": {
        "options": {}
      },
      "credentials": {
        "openAiApi": {
          "id": "ZjnhmdYT28d52ebY",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "5cea6925-cbf7-47a4-9a26-45f42f91c074",
      "name": "Generate Summary with GPT-4o-mini",
      "type": "@n8n/n8n-nodes-langchain.chainLlm",
      "position": [
        1260,
        760
      ],
      "parameters": {
        "text": "=Please analyze the given text and create a structured summary following these guidelines:\n\n1. *General Summary*:\n   - Provide a concise overview of the main topic or purpose of the text in one paragraph.\n   - Focus on the essence of the content without excessive detail.\n\n2. *Key Moments*:\n   - List the most important points, events, or concepts from the text.\n   - Use bullet points for clarity.\n   - Keep each point short and focused.\n   - Highlight key terms using HTML bold tags (<b>term</b>).\n\n3. *Instructions (if applicable)*:\n   - If the text is a tutorial or instructional, list the steps in a clear order.\n   - Use numbered points for steps.\n   - If not applicable, state: \"This text does not contain instructions.\"\n\n4. *Format requirements*:\n   - Use markdown for headers (e.g., ## General Summary) and bullet points.\n   - Use HTML bold tags (<b>term</b>) for emphasis instead of markdown bold.\n   - Do not use tables; use simple text for lists or comparisons (e.g., \"Element: opis\").\n   - Ensure the message is simple and displays correctly in the Telegram app, avoiding unsupported features like nested lists or tables.\n\nHere is the text: {{ $json.concatenated_text }}",
        "promptType": "define"
      },
      "typeVersion": 1.4
    },
    {
      "id": "cba394e4-3ae3-4506-a1d9-7b8ffbdf5d93",
      "name": "Concatenate Transcript Segments",
      "type": "n8n-nodes-base.summarize",
      "position": [
        1000,
        680
      ],
      "parameters": {
        "options": {},
        "fieldsToSummarize": {
          "values": [
            {
              "field": "text",
              "separateBy": " ",
              "aggregation": "concatenate"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "id": "c4b266bd-ab23-4823-8f2c-f12704bad58f",
      "name": "Trigger on Telegram Message",
      "type": "@n8n/n8n-nodes-langchain.chatTrigger",
      "position": [
        360,
        100
      ],
      "webhookId": "da4bfbb8-d077-4ea1-8d2d-08d408002213",
      "parameters": {
        "options": {}
      },
      "typeVersion": 1.1
    },
    {
      "id": "57f22922-29fd-402e-b5c3-79cb133209cd",
      "name": "Extract YouTube Transcript",
      "type": "n8n-nodes-youtube-transcription-kasha.youtubeTranscripter",
      "position": [
        580,
        680
      ],
      "parameters": {
        "videoId": "={{ $json.videoId}}"
      },
      "typeVersion": 1
    },
    {
      "id": "196453ad-8a63-4fbc-9dc3-37a1ee611857",
      "name": "Send Summary via Telegram",
      "type": "n8n-nodes-base.telegram",
      "position": [
        1660,
        760
      ],
      "webhookId": "7159b4c8-984a-4c86-aa32-84e55d406745",
      "parameters": {
        "text": "={{ $json.text }}\n\n\n{{ $('Extract YouTube URL from Input').item.json.youtubeUrl}}",
        "additionalFields": {
          "parse_mode": "HTML",
          "appendAttribution": false
        }
      },
      "credentials": {
        "telegramApi": {
          "id": "MR8ATMwMsj9Ux1De",
          "name": "YoutubeTranscriptChat"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "7754143b-9449-427c-9e04-e91434c4bc74",
      "name": "Receive YouTube URL via Webhook",
      "type": "n8n-nodes-base.webhook",
      "position": [
        360,
        320
      ],
      "webhookId": "8f0beaaf-b2c3-4148-8006-3b73fa146f60",
      "parameters": {
        "path": "8f0beaaf-b2c3-4148-8006-3b73fa146f60",
        "options": {},
        "responseMode": "responseNode"
      },
      "typeVersion": 2
    },
    {
      "id": "e9aaec56-2458-49a4-989e-eb4af03441b9",
      "name": "Send Response to Webhook",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        1860,
        760
      ],
      "parameters": {
        "options": {}
      },
      "typeVersion": 1.1
    },
    {
      "id": "bac178f2-be91-4f28-a024-d7dbef11c442",
      "name": "Telegram Trigger",
      "type": "n8n-nodes-base.telegramTrigger",
      "position": [
        240,
        1040
      ],
      "webhookId": "254daa2a-41b8-49f7-8781-52c7e573de70",
      "parameters": {
        "updates": [
          "message"
        ],
        "additionalFields": {}
      },
      "credentials": {
        "telegramApi": {
          "id": "MR8ATMwMsj9Ux1De",
          "name": "YoutubeTranscriptChat"
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "128b8e7a-9b56-4d98-a270-9f627f188b8b",
      "name": "Retrieve Transcript from Google Docs",
      "type": "n8n-nodes-base.googleDocs",
      "position": [
        1280,
        520
      ],
      "parameters": {
        "operation": "get",
        "documentURL": "1-NdqfoVWfG1gpjltzJthw_MZeyAlGF3d3gYiIOBLbPk"
      },
      "credentials": {
        "googleDocsOAuth2Api": {
          "id": "N5fN0xR3iI0aCpms",
          "name": "Google Docs account 2"
        }
      },
      "typeVersion": 2
    },
    {
      "id": "d4377188-fac7-4d48-8ef4-747f9dd39cf0",
      "name": "Update Transcript in Google Docs",
      "type": "n8n-nodes-base.googleDocs",
      "position": [
        1480,
        520
      ],
      "parameters": {
        "actionsUi": {
          "actionFields": [
            {
              "text": "={{ $json.content }}",
              "action": "replaceAll",
              "replaceText": "={{ $('Concatenate Transcript Segments').item.json.concatenated_text }}"
            }
          ]
        },
        "operation": "update",
        "documentURL": "={{ $json.documentId }}"
      },
      "credentials": {
        "googleDocsOAuth2Api": {
          "id": "N5fN0xR3iI0aCpms",
          "name": "Google Docs account 2"
        }
      },
      "typeVersion": 2
    },
    {
      "id": "25504013-f1e0-4556-a318-dbc482bde4fa",
      "name": "Handle User Questions via AI",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        440,
        1040
      ],
      "parameters": {
        "text": "={{ $json.message.text }}",
        "options": {
          "systemMessage": "You are a tool for answering user questions about a YouTube video based on its transcript, which is available in a Google Docs document. Always check the transcript content before responding and ensure your answers are consistent with it."
        },
        "promptType": "define"
      },
      "typeVersion": 1.7
    },
    {
      "id": "562ce57d-600e-4bb2-a5a2-e6d005f840bd",
      "name": "OpenAI Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        380,
        1220
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
          "id": "ZjnhmdYT28d52ebY",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "39ba9c74-a5c1-455e-b51b-9d36bce76635",
      "name": "Window Buffer Memory",
      "type": "@n8n/n8n-nodes-langchain.memoryBufferWindow",
      "position": [
        540,
        1260
      ],
      "parameters": {
        "sessionKey": "={{ $json.message.text }}",
        "sessionIdType": "customKey"
      },
      "typeVersion": 1.3
    },
    {
      "id": "1983dc09-f74f-4863-8b2c-9069bc6d64d9",
      "name": "Google Docs2",
      "type": "n8n-nodes-base.googleDocsTool",
      "position": [
        660,
        1280
      ],
      "parameters": {
        "operation": "get",
        "documentURL": "1-NdqfoVWfG1gpjltzJthw_MZeyAlGF3d3gYiIOBLbPk"
      },
      "credentials": {
        "googleDocsOAuth2Api": {
          "id": "N5fN0xR3iI0aCpms",
          "name": "Google Docs account 2"
        }
      },
      "typeVersion": 2
    },
    {
      "id": "4dfcba99-98e5-49e4-b8bd-31fb841a0985",
      "name": "Send AI Response via Telegram",
      "type": "n8n-nodes-base.telegram",
      "position": [
        840,
        1040
      ],
      "webhookId": "63608fd8-27e6-4b87-8021-95f7441b7ca1",
      "parameters": {
        "text": "={{ $json.output }}",
        "additionalFields": {
          "parse_mode": "HTML",
          "appendAttribution": false
        }
      },
      "credentials": {
        "telegramApi": {
          "id": "MR8ATMwMsj9Ux1De",
          "name": "YoutubeTranscriptChat"
        }
      },
      "retryOnFail": true,
      "typeVersion": 1.2
    },
    {
      "id": "29c22c9f-cca2-459f-8ef0-577c6e1ddd93",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        0,
        0
      ],
      "parameters": {
        "color": 5,
        "width": 540,
        "height": 500,
        "content": "## Get a video URL\nGet video url via webhook or message\n\nFor this I recommend using a shortcut \nif you are using apple. \nThis allows you to share a video\ndirectly to n8n via webhook\n"
      },
      "typeVersion": 1
    },
    {
      "id": "7a987035-42cc-4b52-b4e3-f75194173a58",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1200,
        360
      ],
      "parameters": {
        "color": 4,
        "width": 540,
        "height": 360,
        "content": "## Load memory \nUploading the transcript about the memory in google docs so you can then ask questions about the film"
      },
      "typeVersion": 1
    },
    {
      "id": "2c7446b3-d7bf-4d0c-9b07-87e6ffaea0da",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        40,
        900
      ],
      "parameters": {
        "color": 3,
        "width": 1020,
        "height": 600,
        "content": "## Ask AI about video"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "0b743433-f1cf-4a8c-9c4e-4b7778d6391a",
  "connections": {
    "gpt-4o-mini": {
      "ai_languageModel": [
        [
          {
            "node": "Generate Summary with GPT-4o-mini",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Google Docs2": {
      "ai_tool": [
        [
          {
            "node": "Handle User Questions via AI",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Telegram Trigger": {
      "main": [
        [
          {
            "node": "Handle User Questions via AI",
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
            "node": "Handle User Questions via AI",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Extract Video ID from URL": {
      "main": [
        [
          {
            "node": "Extract YouTube Transcript",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Send Summary via Telegram": {
      "main": [
        [
          {
            "node": "Send Response to Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract YouTube Transcript": {
      "main": [
        [
          {
            "node": "Split Transcript into Segments",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Trigger on Telegram Message": {
      "main": [
        [
          {
            "node": "Extract YouTube URL from Input",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Handle User Questions via AI": {
      "main": [
        [
          {
            "node": "Send AI Response via Telegram",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract YouTube URL from Input": {
      "main": [
        [
          {
            "node": "Extract Video ID from URL",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Split Transcript into Segments": {
      "main": [
        [
          {
            "node": "Concatenate Transcript Segments",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Concatenate Transcript Segments": {
      "main": [
        [
          {
            "node": "Generate Summary with GPT-4o-mini",
            "type": "main",
            "index": 0
          },
          {
            "node": "Retrieve Transcript from Google Docs",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Receive YouTube URL via Webhook": {
      "main": [
        [
          {
            "node": "Extract YouTube URL from Input",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Generate Summary with GPT-4o-mini": {
      "main": [
        [
          {
            "node": "Send Summary via Telegram",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Retrieve Transcript from Google Docs": {
      "main": [
        [
          {
            "node": "Update Transcript in Google Docs",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-354"></a>

## Template 354 - Encontrar e resumir oportunidades no Reddit

- **Nome:** Encontrar e resumir oportunidades no Reddit
- **Descrição:** Busca posts em um subreddit com palavras-chave, filtra por critérios, identifica posts com potencial de negócio via IA, gera resumos e registra os resultados em uma planilha.
- **Funcionalidade:** • Busca por posts: Pesquisa posts em um subreddit específico usando palavras-chave e ordenação definida.
• Filtragem por métricas e data: Remove posts com poucos upvotes, com conteúdo vazio ou que sejam antigos (ex.: mais de 180 dias).
• Extração de campos chave: Seleciona campos importantes como upvotes, número de inscritos do subreddit, conteúdo do post, URL e data.
• Classificação por IA: Usa um modelo de linguagem para decidir se o post descreve um problema ou necessidade de negócio (saída: yes/no).
• Resumo por IA: Gera um resumo executivo do conteúdo dos posts classificados como oportunidade.
• Preparação e merge de dados: Organiza e combina campos e resumos em um formato final para registro.
• Armazenamento: Anexa os resultados formatados em uma planilha para acompanhamento posterior.
- **Ferramentas:** • Reddit (API de busca): Fonte dos posts, permite pesquisar por subreddit, palavra-chave e ordenar resultados.
• OpenRouter (modelo GPT-4.1-mini): Serviço de modelo de linguagem usado para classificar posts e gerar resumos executivos.
• Google Sheets: Planilha online usada como destino final para salvar os registros e resumos gerados.

## Fluxo visual

```mermaid
flowchart LR
    N1["When clicking ‘Test workflow’"]
    N2["Post Summarization"]
    N3["Merge Input"]
    N4["Output The Results"]
    N5["Merge 3 Inputs"]
    N6["Filter Posts By Features"]
    N7["Filter Posts By Content"]
    N8["Select Key Fields"]
    N9["Get Posts"]
    N10["Sticky Note"]
    N11["Sticky Note2"]
    N12["Sticky Note3"]
    N13["OpenRouter Chat Model"]
    N14["OpenRouter Chat Model1"]
    N15["Basic LLM Chain"]
    N16["Edit Fields"]
    N17["Edit Fields1"]

    N9 --> N6
    N16 --> N5
    N3 --> N7
    N17 --> N5
    N5 --> N4
    N15 --> N3
    N8 --> N3
    N8 --> N15
    N2 --> N16
    N7 --> N2
    N7 --> N17
    N6 --> N8
    N1 --> N9
```

## Fluxo (.json) :

```json
{
  "meta": {
    "instanceId": "5b9aff0ecdeb17791c04b93eac72e39e69151cfa63708980e5d936abe9308b8c"
  },
  "nodes": [
    {
      "id": "b0a2f427-1788-4707-b2ca-07b7ba9878ab",
      "name": "When clicking ‘Test workflow’",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        -2040,
        1040
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "9bf6edaf-e2ad-4702-8730-0600775531cb",
      "name": "Post Summarization",
      "type": "@n8n/n8n-nodes-langchain.chainSummarization",
      "position": [
        20,
        680
      ],
      "parameters": {
        "options": {}
      },
      "typeVersion": 2
    },
    {
      "id": "9541106a-af9c-4326-91b1-07f68c9ee386",
      "name": "Merge Input",
      "type": "n8n-nodes-base.merge",
      "position": [
        -720,
        980
      ],
      "parameters": {
        "mode": "combine",
        "options": {},
        "combineBy": "combineByPosition"
      },
      "typeVersion": 3
    },
    {
      "id": "b0ad0465-0daa-48f6-a9c5-8dadca2ca4e1",
      "name": "Output The Results",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        1140,
        820
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
          "value": 979106892,
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1cIMIh_DjoWXMDaJEH-AyTZbnAha6TxthCSSEam4NLsE/edit#gid=979106892",
          "cachedResultName": "Find-Leads"
        },
        "documentId": {
          "__rl": true,
          "mode": "id",
          "value": "1cIMIh_DjoWXMDaJEH-AyTZbnAha6TxthCSSEam4NLsE"
        }
      },
      "typeVersion": 4.5
    },
    {
      "id": "16c397ea-1625-43c6-8602-9150a79858a4",
      "name": "Merge 3 Inputs",
      "type": "n8n-nodes-base.merge",
      "position": [
        800,
        820
      ],
      "parameters": {
        "mode": "combine",
        "options": {},
        "combineBy": "combineByPosition"
      },
      "typeVersion": 3
    },
    {
      "id": "f59b3a35-9502-4a69-8b18-6760538765ab",
      "name": "Filter Posts By Features",
      "type": "n8n-nodes-base.if",
      "position": [
        -1620,
        1040
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
      "id": "d88efb10-91cf-4ac0-9f7b-796bfa8a75ab",
      "name": "Filter Posts By Content",
      "type": "n8n-nodes-base.if",
      "position": [
        -460,
        980
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
      "id": "405f37a4-d3a8-4d92-8add-ad232be014b7",
      "name": "Select Key Fields",
      "type": "n8n-nodes-base.set",
      "position": [
        -1380,
        1020
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
      "id": "6a6143e1-6181-45a0-988f-e8ed7e634bd8",
      "name": "Get Posts",
      "type": "n8n-nodes-base.reddit",
      "position": [
        -1820,
        1040
      ],
      "parameters": {
        "keyword": "how do I find leads",
        "operation": "search",
        "subreddit": "=Entrepreneur",
        "additionalFields": {
          "sort": "hot"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "1937b724-18a1-4b5b-8338-1752f478eccf",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -2140,
        800
      ],
      "parameters": {
        "width": 880,
        "height": 440,
        "content": "# Data Extraction\n## Retrieves recent posts from specific Reddit community (subreddit)\n## Filters content by keywords and upvotes"
      },
      "typeVersion": 1
    },
    {
      "id": "5d4a1df6-16a5-473e-b6b4-42e7966a5cd2",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -1140,
        580
      ],
      "parameters": {
        "color": 4,
        "width": 820,
        "height": 660,
        "content": "# Transformation Step\n## Analyze using LLM (AI)\n## Filter for business opportunities"
      },
      "typeVersion": 1
    },
    {
      "id": "399afd5a-ced1-447b-95de-a7191632d266",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -200,
        480
      ],
      "parameters": {
        "color": 6,
        "width": 1460,
        "height": 760,
        "content": "#Transformation 2nd Step + Load to Gsheet\n## Insight Generation \n## Generates executive summaries of key opportunities\n## Submit findings in Google Sheets"
      },
      "typeVersion": 1
    },
    {
      "id": "571bf6e7-ef36-4a7d-9e9d-e97aef4e7015",
      "name": "OpenRouter Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenRouter",
      "position": [
        -1100,
        940
      ],
      "parameters": {
        "model": "openai/gpt-4.1-mini",
        "options": {}
      },
      "typeVersion": 1
    },
    {
      "id": "7e157fc9-a7cd-42d4-80d5-233308a2441a",
      "name": "OpenRouter Chat Model1",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenRouter",
      "position": [
        40,
        860
      ],
      "parameters": {
        "model": "openai/gpt-4.1-mini",
        "options": {}
      },
      "typeVersion": 1
    },
    {
      "id": "9f2020d1-77f2-4dbc-b6ce-7dae7acd1263",
      "name": "Basic LLM Chain",
      "type": "@n8n/n8n-nodes-langchain.chainLlm",
      "position": [
        -1100,
        760
      ],
      "parameters": {
        "text": "=Decide whether this reddit post is describing a business-related problem or a need for a solution.",
        "messages": {
          "messageValues": [
            {
              "message": "The post should mention a specific challenge or requirement that a business is trying to address. Is this post about a business problem or need for a solution ? Output only yes or no"
            },
            {
              "type": "HumanMessagePromptTemplate",
              "message": "=Reddit post:  {{ $json.postcontent }}"
            }
          ]
        },
        "promptType": "define"
      },
      "typeVersion": 1.6
    },
    {
      "id": "b048b2f6-3c46-4ad2-8255-5b0509e9da0f",
      "name": "Edit Fields",
      "type": "n8n-nodes-base.set",
      "position": [
        460,
        680
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "7038812d-f325-4196-89b6-3623d81dec7b",
              "name": "summary",
              "type": "string",
              "value": "={{ $json.response.text }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "924219fa-ae4d-44b3-a42d-e2c67dc85545",
      "name": "Edit Fields1",
      "type": "n8n-nodes-base.set",
      "position": [
        280,
        960
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "1f34c3f3-7be7-474c-9026-7058807a7b3d",
              "name": "date",
              "type": "string",
              "value": "={{ $json.date }}"
            },
            {
              "id": "0e0e5227-e37b-43fc-8a88-2bb76631108d",
              "name": "subreddit_subscribers",
              "type": "number",
              "value": "={{ $json.subreddit_subscribers }}"
            },
            {
              "id": "68e2ca82-6b1d-42ec-acc7-b784e9ed61b5",
              "name": "url",
              "type": "string",
              "value": "={{ $json.url }}"
            },
            {
              "id": "946800a2-ec8b-4f99-a4db-9248bf305747",
              "name": "upvotes",
              "type": "string",
              "value": "={{ $json.upvotes }}"
            },
            {
              "id": "da86d4d3-db84-44e3-a684-38aff2fd5b77",
              "name": "postcontent",
              "type": "string",
              "value": "={{ $json.postcontent }}"
            },
            {
              "id": "b67148e1-67a5-4b10-be6c-c819ff910be0",
              "name": "business_opportunity",
              "type": "string",
              "value": "={{ $json.output }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    }
  ],
  "pinData": {
    "Merge Input": [
      {
        "url": "https://www.reddit.com/r/smallbusiness/comments/1iqletb/need_help_and_advice_for_a_business_name_idea/",
        "date": "2025-02-16T13:42:12.000+08:00",
        "output": "yes",
        "upvotes": "4",
        "postcontent": "Hello guys,\n\nMy partner and I are planning to open an accounting business that will focus on tax services such as filling taxes and tax advisor and we have plan for future to add wealth management and capital advising. Initially, we were thinking of using the name \"Global Solutions,\" but we found out that another company already has it, so we can’t use it.\n\nWe’re looking for a professional name that’s easy to pronounce and somewhat similar to \"Global Solutions.\" Also, unique enough that we won’t want to change it in the future. Any ideas or suggestions would be greatly appreciated! We would love to list all name suggestions to share with my partner so we can pick the best one.\n\nThanks in advance for your help! Appreciate it! ",
        "subreddit_subscribers": 1944498
      },
      {
        "url": "https://www.reddit.com/r/smallbusiness/comments/1iob5ez/business_acquisition_loan_what_are_my_odds_what/",
        "date": "2025-02-13T12:34:29.000+08:00",
        "output": "yes",
        "upvotes": "3",
        "postcontent": "Hello!  \nLongtime friends have offered to sell my their local biz.    \n12 years running, last year did 950k gross, 325K SDE.  \nYOY growth has been good.  \n650k price.  \nThey have offered to seller finance up to 61.5% of the purchase price so far.  \nThey might go even higher on the seller financing if I ask.\n\n**The good (about me):**  \n  \n\\- I have good credit, probably 720+.  \n\\- I do have \\~200k equity in my home, I'm willing to collateralize.  \n  \n**The ugly (about me):**  \n  \n\\- I have only 5% down possible for equity injection, but would prefer 0%  \nI read that with a SBA 7(a) loan the seller can do 5% of my equity injection with a standby note (deferred payment until SBA loan is paid off).  I'm not sure if that could be done in tandem with another (much larger) note that would be payable (in payments) at closing.  \n  \n\\- I've had no / negative income the last couple of years.  I took some time off from my 20+ year profession, lived off of savings and some credit while I explored other career paths because I needed a change.  I did learn a couple of high value trades, and did incur some expenses in that process.\n\n\\- No direct industry experience.  I do have much professional experience I bring to the table, but not in this industry.  I have managed people on my team... but not employees.  \n\n**The rest:**  \n  \nThey are willing to hire me as store manager now, if that helps.    \nThey will be providing complete training and ongoing support.  \nIt is a simple business, really.  \nThey obviously believe in their business, given the willingness to seller finance so much of it.  \n  \nWhat are the odds I could get a SBA 7(a) loan with 5% down?  \nAre there any loans with 0% down?  \n  \nI would like to get an extra 50k or so for startup costs - it is an acquisition however I'm going to have startup expenses like first and last months lease payments, jurisdictional inspections, electricity deposit, liability insurance / workman's comp, that sort of stuff.\n\nI realize the scenario is not ideal, however it seems to me there should be SOME option out there given that all I have to do is not mess up the business!  It's a great business, well loved in the community.  \nThere is good room in the revenue for me to make accelerated loan repayments, establish business savings, grow the business, and even pay myself enough to cover my living expenses.  That is one heck of a deal, I have to find some way to pull this off!\n\nI'm willing to look at less fantastic loan offers with higher rates.    \nIt really seems to me that some entity would be willing to lend based on the cashflow / success / stability of the existing business.\n\nOne idea I had - if sellers would be willing to carry 100% for 12-24 months, would I then likely have an easier time qualifying for a SBA 7(a) loan to pay off their note, or part of it (depending on what they want)?\n\nAnother idea - store manager -&gt; partner -&gt; partner buyout  \nI do need to find out their maximum timeline for getting out.  \n  \nHad I known a couple of years ago this was going to come up, I would have made different decisions!  \nI really don't want to sell my house and rent something in order to do this, but I'm considering that as a last resort.  \nIf these weren't my longtime friends whom I trust with my life, I wouldn't consider this.  I'd be too chicken.  This is like winning the lottery to me, frankly... I'm not the perfect buyer on paper but they really want me to have it.  They know it will be my baby, as it has been theirs.\n\nGrateful for any solutions / ideas, thank you in advance!  =D\n\n",
        "subreddit_subscribers": 1944498
      },
      {
        "url": "https://www.reddit.com/r/smallbusiness/comments/1ikcdi5/seeking_a_reliable_alternative_to_stripe_for/",
        "date": "2025-02-08T10:09:44.000+08:00",
        "output": "yes",
        "upvotes": "3",
        "postcontent": "Hi everyone,\n\nI'm looking for advice on the **best alternative to Stripe** for my service-based business. Here’s the situation:\n\n* I handle **monthly recurring payments** from customers who prefer paying by **credit card**.\n* My customers provide me with their credit card information, and I need a solution to **send invoices** or **auto-charge their cards monthly** without issues.\n\n# Problems I’ve Faced:\n\n1. **Stripe**: I’ve lost countless disputes despite providing proof of service, and I’m fed up with their **chargeback process**.\n2. **Square**: I processed just **two paid invoices totaling $180**, and they **deactivated my account**, holding my money for **90 days**!\n\nI’m desperate to find a platform that:\n\n* Allows **invoicing** and **recurring auto-charges**.\n* Has **minimal chargebacks or disputes**, or at least a fair dispute resolution process. or **BEST: no disputes at all**\n* Doesn’t hold funds unnecessarily or shut down accounts without notice.\n\nI’m open to hearing about **any reliable options**, whether they are traditional payment processors, blockchain-based platforms, or other innovative solutions.\n\n**Please help!** Any advice would mean the world to me right now.\n\nThank you in advance for your suggestions!",
        "subreddit_subscribers": 1944498
      },
      {
        "url": "https://www.reddit.com/r/smallbusiness/comments/1ibkmzd/business_number_being_used_to_spam_call_people/",
        "date": "2025-01-28T05:28:30.000+08:00",
        "output": "yes",
        "upvotes": "7",
        "postcontent": "So I just got off the phone with the umpteenth person who has gotten a spam call from someone spoofing with our business number, and I’m just waiting for the day that we start getting negative reviews based on this.\n\nWe’ve gotten angry calls from people for a number of scams, and apparently it’s repeated calls to them.\n\nI feel bad, cos those calls make me mad too, but I get tired of getting cussed out several times a week, and having to explain what spam calls are. I haven’t found any solutions online that look like they’d actually solve the problem.\n\nDoes anyone else get this with their business numbers?",
        "subreddit_subscribers": 1944498
      },
      {
        "url": "https://www.reddit.com/r/smallbusiness/comments/1i43orw/im_a_small_business_owner_which_software_should_i/",
        "date": "2025-01-18T17:06:49.000+08:00",
        "output": "yes",
        "upvotes": "38",
        "postcontent": "I generate about $100k in annual revenue and don’t have payroll. What software would you recommend, and why? Currently, I create invoices using Excel, but I’m looking for a more efficient solution to send invoices and receive payments seamlessly.\n\nAlso, is there a fee every time I receive a payment? For example, if I receive $20k, $10k, $30k, or $40k?",
        "subreddit_subscribers": 1944498
      },
      {
        "url": "https://www.reddit.com/r/smallbusiness/comments/1i1euah/small_business_automation_can_someone_help_me/",
        "date": "2025-01-15T03:54:19.000+08:00",
        "output": "yes",
        "upvotes": "3",
        "postcontent": "So I am looking for ways to bring some automations to my business by leveraging the technology available and I started with programing a smart chat bot for my website that literally is an agent who knows everything about my company which is nice when I am not around.  Then I took it further and thought that I could make automated virtual receptionist for my company which I did which makes life better because when I am on a job I miss probably a few calls a day and then when I try to reach them back, they usually have already started to talk to other competitors and then it gets challenging from there.  So this has been my solution and now I never miss a call and started building automations to even sell for me on my products and services that I offer and now even can send a booking link to them by text and email and this has allowed me to convert better and not miss an opportunity that comes my way.  I say all this because I created another on that is used strictly to role play with and I need testers to help me refine and debug it.  Essentially I just need other business owners to role play with my agent and provide any feedback that would make it better or enhance it.  \n\nIf you're willing to help me test it just call 1-855-449-7005.  Thanks in advance to anyone who tries it out!            ",
        "subreddit_subscribers": 1944498
      },
      {
        "url": "https://www.reddit.com/r/smallbusiness/comments/1hzlhcg/customer_emailcommunication_tracker/",
        "date": "2025-01-12T20:17:33.000+08:00",
        "output": "yes",
        "upvotes": "3",
        "postcontent": "What system do you use for customer communication?\n\nLooking for recommendations on CSR communication. I have a retail store with one full time retail manager and a handful of seasonal and part time associates. \n\nWebsite inquiries for retail are routed to a generic email of which all associates can respond. The goal was that with a generic email (accessed from one terminal plus an iPad) customers would get responded to quickly but Mozilla Thunderbird’s interface is clunky and associates never remember to “file” completed conversations. \n\nI am frugal (hence one email address) but am willing to invest in a solution that can better track inquiries (only a handful a week) to provide a better experience. Just curious what you might use that works well. ",
        "subreddit_subscribers": 1944498
      },
      {
        "url": "https://www.reddit.com/r/smallbusiness/comments/1hyzgts/had_a_customer_fire_themselves_and_it_felt_good/",
        "date": "2025-01-12T00:24:35.000+08:00",
        "output": "yes",
        "upvotes": "57",
        "postcontent": "My work had a newer customer that we were happy to have because we knew they were working with our competition. We did some work for them and they would blame us for their problems. We would offer solutions and never hear back and to top it off they paid late. I also met the owner at a trade show and he treated me like I wasn't even there when I went to say thank you. He just looked at me blankly and ignored me. So we stopped calling.\n\nThen a half year later they send some work in. I quoted it extremely high. They asked for a price discount so they could get the job for their customer. I went down 10% knowing it was still high. Then the owner emailed back about his 25 year relationship with our competitor and how they would do it at half the price. \n\nI felt happy wasting their time and money. Also, if our competitor is so great, why did they start sending us work? \n\nI'm glad we won't hear from them. I have many other customers that are fantastic to work with and pay on time. ",
        "subreddit_subscribers": 1944498
      },
      {
        "url": "https://www.reddit.com/r/smallbusiness/comments/1hnqv0q/attention_business_owners_using_benchco/",
        "date": "2024-12-28T06:31:18.000+08:00",
        "output": "yes",
        "upvotes": "8",
        "postcontent": "You may have seen in your email that [Bench.co](http://Bench.co) is closing its doors for bookkeeping services. They are giving business owners until **March 7th, 2025**, at **5 PM** ET to download their financial data.\n\nDon't wait until the last minute! This is absolutely critical - your financial data is too important to risk losing. The timing couldn't be worse in the middle of the holidays and so close to year-end... and the lack of advance warning is frustrating.\n\nI know this situation will leave many business owners scrambling for a new bookkeeping solution. But don’t stress—there are excellent alternatives out there that can serve you even better!\n\nI primarily wanted to make this post to alert people of the closure (in case you missed the email) and encourage everyone to secure their data ASAP. If you're looking for a reliable path forward, I'd recommend exploring smaller firms or individual remote bookkeepers. Many offer highly personalized services at a wide range of prices - with services often far better quality than Bench.\n\nI'm not here to promote my business, but if you're feeling overwhelmed or don't know where to start, I'm happy to chat and share advice based on my experience running a remote bookkeeping and accounting firm. At the end of the day, I hope all Bench clients find a bookkeeping service that's a better fit: personalized, reliable, and capable of supporting your business long-term.\n\n  \nTo add a question and make sure I'm following the sub rules: \n\nWhat are you currently doing for your bookkeeping and accounting? How did you find that solution and what do you wish was different about it?",
        "subreddit_subscribers": 1944498
      }
    ]
  },
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
    "Edit Fields": {
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
    "Edit Fields1": {
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
    "Basic LLM Chain": {
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
    "Select Key Fields": {
      "main": [
        [
          {
            "node": "Merge Input",
            "type": "main",
            "index": 1
          },
          {
            "node": "Basic LLM Chain",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Post Summarization": {
      "main": [
        [
          {
            "node": "Edit Fields",
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
            "node": "Basic LLM Chain",
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
            "node": "Post Summarization",
            "type": "ai_languageModel",
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
            "node": "Edit Fields1",
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

<a id="template-355"></a>

## Template 355 - Conversão e compressão de PDFs

- **Nome:** Conversão e compressão de PDFs
- **Descrição:** Fluxo que gera um PDF a partir de HTML e também permite baixar um PDF por URL para compactá-lo.
- **Funcionalidade:** • Geração de PDF a partir de HTML: Recebe conteúdo HTML e converte em um arquivo PDF.
• Compactação de PDF (arquivo binário): Aplica compressão a um PDF já disponível em formato binário.
• Compactação de PDF a partir de URL: Faz o download de um PDF usando um URL fornecido e em seguida o compacta.
• Definição de URL via código: Permite definir programaticamente o caminho do PDF de entrada.
• Execução manual para testes: Inicia o fluxo manualmente para validação e testes.
- **Ferramentas:** • CustomJS API: Serviço/API utilizado para converter HTML em PDF e para compactar arquivos PDF.
• Servidor externo de arquivos: Fonte que hospeda PDFs acessíveis por URL (usado como origem dos PDFs a serem compactados).

## Fluxo visual

```mermaid
flowchart LR
    N1["HTML to PDF"]
    N2["Compress PDF file"]
    N3["When clicking ‘Test workflow’"]
    N4["Compress PDF file1"]
    N5["Set PDF URL"]
    N6["Sticky Note"]
    N7["Sticky Note1"]
    N8["Sticky Note2"]
    N9["Sticky Note3"]

    N1 --> N2
    N5 --> N4
    N3 --> N1
    N3 --> N5
```

## Fluxo (.json) :

```json
{
  "meta": {
    "instanceId": "7599ed929ea25767a019b87ecbc83b90e16a268cb51892887b450656ac4518a2"
  },
  "nodes": [
    {
      "id": "b962ef3d-b0ad-4b21-bb15-61b6521bfd03",
      "name": "HTML to PDF",
      "type": "@custom-js/n8n-nodes-pdf-toolkit.html2Pdf",
      "position": [
        220,
        0
      ],
      "parameters": {
        "htmlInput": "<h1>Hello World</h1>"
      },
      "credentials": {
        "customJsApi": {
          "id": "h29wo2anYKdANAzm",
          "name": "CustomJS account"
        }
      },
      "notesInFlow": false,
      "typeVersion": 1
    },
    {
      "id": "988f427e-7eca-43e5-a77d-c69a92ec6158",
      "name": "Compress PDF file",
      "type": "@custom-js/n8n-nodes-pdf-toolkit.CompressPDF",
      "position": [
        460,
        0
      ],
      "parameters": {},
      "credentials": {
        "customJsApi": {
          "id": "h29wo2anYKdANAzm",
          "name": "CustomJS account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "bbbf9fb1-2fc2-4de1-9854-149b63c7070c",
      "name": "When clicking ‘Test workflow’",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        0,
        100
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "492b07d3-4643-4d1e-acbb-b0a7b7fde350",
      "name": "Compress PDF file1",
      "type": "@custom-js/n8n-nodes-pdf-toolkit.CompressPDF",
      "position": [
        460,
        200
      ],
      "parameters": {
        "resource": "url",
        "field_name": "={{ $json.path }}"
      },
      "credentials": {
        "customJsApi": {
          "id": "h29wo2anYKdANAzm",
          "name": "CustomJS account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "d60193ff-0bf6-4692-83e2-d0e1e59c5656",
      "name": "Set PDF URL",
      "type": "n8n-nodes-base.code",
      "position": [
        220,
        200
      ],
      "parameters": {
        "jsCode": "return {\"json\": {\"path\": \"https://www.nlbk.niedersachsen.de/download/164891/Test-pdf_3.pdf.pdf\"}};"
      },
      "typeVersion": 2
    },
    {
      "id": "c68fc714-fc5a-456d-9126-ccbcfedce3ca",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        140,
        -100
      ],
      "parameters": {
        "color": 4,
        "height": 260,
        "content": "### HTML to PDF\n- Request HTML Data\n- Convert HTML to PDF"
      },
      "typeVersion": 1
    },
    {
      "id": "5388484e-5b74-4ece-90a0-75fc3d9963b5",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        380,
        -100
      ],
      "parameters": {
        "color": 5,
        "width": 260,
        "height": 260,
        "content": "### Compress Pages from PDF\n- Compress PDF as a binary file."
      },
      "typeVersion": 1
    },
    {
      "id": "014c6536-0270-4ac7-881a-4334816a9ffb",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        140,
        160
      ],
      "parameters": {
        "color": 3,
        "height": 260,
        "content": "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n### Set PDF URL\n- Request PDF from URL."
      },
      "typeVersion": 1
    },
    {
      "id": "f6e18c8b-3109-414b-a539-dbb586d6e75e",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        380,
        160
      ],
      "parameters": {
        "color": 2,
        "width": 260,
        "height": 260,
        "content": "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n### Compress Pages from PDF\n- Compress PDF as a binary file."
      },
      "typeVersion": 1
    }
  ],
  "pinData": {},
  "connections": {
    "HTML to PDF": {
      "main": [
        [
          {
            "node": "Compress PDF file",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set PDF URL": {
      "main": [
        [
          {
            "node": "Compress PDF file1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Compress PDF file": {
      "main": [
        []
      ]
    },
    "When clicking ‘Test workflow’": {
      "main": [
        [
          {
            "node": "HTML to PDF",
            "type": "main",
            "index": 0
          },
          {
            "node": "Set PDF URL",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-356"></a>

## Template 356 - Rastreamento de horários e pausas

- **Nome:** Rastreamento de horários e pausas
- **Descrição:** Automatiza o registro do horário de início, duração de pausas e horário de término em um banco de dados diário, recebendo comandos via requisição HTTP e respondendo com confirmações.
- **Funcionalidade:** • Receber comandos via endpoint HTTP: aceita requisições POST com método (start, break, end).
• Roteamento por tipo de ação: direciona o fluxo conforme o valor do campo "method" na requisição.
• Verificar existência do registro do dia: consulta o banco de dados por data (formato dd.MM.yyyy) para encontrar a página do dia atual.
• Criar registro de início: cria uma nova página com a hora de início quando não existe registro para o dia.
• Atualizar horário de término: atualiza a página existente definindo a hora de término quando solicitado.
• Registrar ou atualizar duração da pausa: grava ou atualiza o campo de minutos de pausa com o valor recebido.
• Evitar duplicações e validar estado: checa se início ou fim já foram registrados e retorna mensagens apropriadas.
• Responder ao solicitante: envia mensagens de confirmação ou erro como resposta à requisição HTTP.
- **Ferramentas:** • Notion: armazena o banco de dados "Time Tracker" e permite criar/atualizar páginas diárias com campos de início, fim e pausa.
• Atalho iOS: origina as requisições HTTP enviando parâmetros (method, duration/pause) para controlar o registro.
• Endpoint HTTP (Webhook): ponto de entrada público que recebe as requisições do atalho e devolve respostas de texto.

## Fluxo visual

```mermaid
flowchart LR
    N1["Create new page"]
    N2["Update page with end date"]
    N3["If pause_in_minuten is empty"]
    N4["If page responded"]
    N5["If page exist"]
    N6["If page exist1"]
    N7["If"]
    N8["Set Break Duration"]
    N9["Update break duration for current day"]
    N10["Set break duration for current day"]
    N11["Get notion page by date"]
    N12["Set Message - End time already tracked"]
    N13["Set Message - End time tracked"]
    N14["Set Message - Start time not yet tracked"]
    N15["Set Message - Start not yet tracked"]
    N16["Set Message - Break time tracked"]
    N17["Set Message - Break time updated"]
    N18["Set Message - Start time already tracked"]
    N19["Set Message - Start time already tracked1"]
    N20["Get notion page with todays date"]
    N21["Switch"]
    N22["Get notion page with todays date1"]
    N23["Sticky Note"]
    N24["Sticky Note1"]
    N25["Sticky Note2"]
    N26["Sticky Note3"]
    N27["Sticky Note4"]
    N28["Respond to Webhook"]
    N29["Sticky Note5"]
    N30["Webhook - Track Time"]

    N7 --> N2
    N7 --> N12
    N21 --> N20
    N21 --> N8
    N21 --> N22
    N5 --> N18
    N5 --> N1
    N6 --> N7
    N6 --> N14
    N1 --> N19
    N4 --> N3
    N4 --> N15
    N8 --> N11
    N30 --> N21
    N11 --> N4
    N2 --> N13
    N3 --> N10
    N3 --> N9
    N13 --> N28
    N20 --> N5
    N16 --> N28
    N17 --> N28
    N22 --> N6
    N10 --> N16
    N15 --> N28
    N9 --> N17
    N12 --> N28
    N18 --> N28
    N14 --> N28
    N19 --> N28
```

## Fluxo (.json) :

```json
{
  "id": "pdgNdag49lwoTxUP",
  "meta": {
    "instanceId": "46264913bc099c31e7222b2cfd112772e1c7867192afd7716e58254079b3333f",
    "templateCredsSetupCompleted": true
  },
  "name": "Track Working Time and Pauses",
  "tags": [],
  "nodes": [
    {
      "id": "1ae951f1-acfa-4bd2-800e-22c7628e862d",
      "name": "Create new page",
      "type": "n8n-nodes-base.notion",
      "position": [
        1260,
        -120
      ],
      "parameters": {
        "title": "Tracked Time via n8n",
        "options": {
          "icon": "🤖"
        },
        "resource": "databasePage",
        "databaseId": {
          "__rl": true,
          "mode": "list",
          "value": "1117f2f5-baf9-8054-b33b-efb4d8a3c7ab",
          "cachedResultUrl": "https://www.notion.so/1117f2f5baf98054b33befb4d8a3c7ab",
          "cachedResultName": "Time Tracker"
        },
        "propertiesUi": {
          "propertyValues": [
            {
              "key": "Start|date",
              "date": "={{ $now }}"
            }
          ]
        }
      },
      "credentials": {
        "notionApi": {
          "id": "03mmrqQX1rffebZp",
          "name": "Notion David"
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "490d1893-3828-4df6-8c0a-0a1476fc8727",
      "name": "Update page with end date",
      "type": "n8n-nodes-base.notion",
      "position": [
        1560,
        780
      ],
      "parameters": {
        "pageId": {
          "__rl": true,
          "mode": "id",
          "value": "={{ $json.id }}"
        },
        "options": {},
        "resource": "databasePage",
        "operation": "update",
        "propertiesUi": {
          "propertyValues": [
            {
              "key": "End|date",
              "date": "={{ $now }}"
            }
          ]
        }
      },
      "credentials": {
        "notionApi": {
          "id": "03mmrqQX1rffebZp",
          "name": "Notion David"
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "daef6212-b852-45ba-8100-103e231837cb",
      "name": "If pause_in_minuten is empty",
      "type": "n8n-nodes-base.if",
      "position": [
        1540,
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
              "id": "6ec8bb5f-d860-47a8-b631-c9535716ddc5",
              "operator": {
                "type": "number",
                "operation": "empty",
                "singleValue": true
              },
              "leftValue": "={{ $json.property_break }}",
              "rightValue": ""
            }
          ]
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "ef724c03-885e-4066-b776-a84fe001a14a",
      "name": "If page responded",
      "type": "n8n-nodes-base.if",
      "position": [
        1260,
        260
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
              "id": "2130bdb4-54be-4d43-90bb-36f57826f2dc",
              "operator": {
                "type": "object",
                "operation": "notEmpty",
                "singleValue": true
              },
              "leftValue": "={{ $json }}",
              "rightValue": ""
            }
          ]
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "aa51a557-7eec-410a-9cdd-1dac3e2e104d",
      "name": "If page exist",
      "type": "n8n-nodes-base.if",
      "position": [
        980,
        -200
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
              "id": "2130bdb4-54be-4d43-90bb-36f57826f2dc",
              "operator": {
                "type": "object",
                "operation": "notEmpty",
                "singleValue": true
              },
              "leftValue": "={{ $json }}",
              "rightValue": ""
            }
          ]
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "738aa465-bd04-4c4e-9846-02ae66139789",
      "name": "If page exist1",
      "type": "n8n-nodes-base.if",
      "position": [
        980,
        840
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
              "id": "2130bdb4-54be-4d43-90bb-36f57826f2dc",
              "operator": {
                "type": "object",
                "operation": "notEmpty",
                "singleValue": true
              },
              "leftValue": "={{ $json }}",
              "rightValue": ""
            }
          ]
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "4547c3fd-6373-401a-9d33-caa1e9f5545e",
      "name": "If",
      "type": "n8n-nodes-base.if",
      "position": [
        1260,
        840
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
              "id": "6ec8bb5f-d860-47a8-b631-c9535716ddc5",
              "operator": {
                "type": "object",
                "operation": "empty",
                "singleValue": true
              },
              "leftValue": "={{ $json.property_end }}",
              "rightValue": ""
            }
          ]
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "70424282-dcce-4f1a-aba0-af0e7947a4fd",
      "name": "Set Break Duration",
      "type": "n8n-nodes-base.set",
      "position": [
        740,
        260
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "9261c98a-3099-4409-b697-8c28f6ec0c06",
              "name": "break_duration",
              "type": "number",
              "value": "={{ $json.body.duration }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "ad1bd9ce-d7cc-4359-954b-8976f593c272",
      "name": "Update break duration for current day",
      "type": "n8n-nodes-base.notion",
      "position": [
        1820,
        320
      ],
      "parameters": {
        "pageId": {
          "__rl": true,
          "mode": "id",
          "value": "={{ $json.id }}"
        },
        "options": {},
        "resource": "databasePage",
        "operation": "update",
        "propertiesUi": {
          "propertyValues": [
            {
              "key": "Break|number",
              "numberValue": "={{ $('Set Break Duration').item.json.break_duration }}"
            }
          ]
        }
      },
      "credentials": {
        "notionApi": {
          "id": "03mmrqQX1rffebZp",
          "name": "Notion David"
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "622eddf9-f719-412f-a07e-45e4d8390798",
      "name": "Set break duration for current day",
      "type": "n8n-nodes-base.notion",
      "position": [
        1820,
        140
      ],
      "parameters": {
        "pageId": {
          "__rl": true,
          "mode": "id",
          "value": "={{ $json.id }}"
        },
        "options": {},
        "resource": "databasePage",
        "operation": "update",
        "propertiesUi": {
          "propertyValues": [
            {
              "key": "Break|number",
              "numberValue": "={{ $('Set Break Duration').item.json.break_duration }}"
            }
          ]
        }
      },
      "credentials": {
        "notionApi": {
          "id": "03mmrqQX1rffebZp",
          "name": "Notion David"
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "29a96903-43f4-439d-9d35-95d557f7c544",
      "name": "Get notion page by date",
      "type": "n8n-nodes-base.notion",
      "position": [
        980,
        260
      ],
      "parameters": {
        "limit": 1,
        "filters": {
          "conditions": [
            {
              "key": "Date|formula",
              "condition": "equals",
              "textValue": "={{ $now.format('dd.MM.yyyy') }}",
              "returnType": "text"
            }
          ]
        },
        "options": {},
        "resource": "databasePage",
        "operation": "getAll",
        "databaseId": {
          "__rl": true,
          "mode": "list",
          "value": "1117f2f5-baf9-8054-b33b-efb4d8a3c7ab",
          "cachedResultUrl": "https://www.notion.so/1117f2f5baf98054b33befb4d8a3c7ab",
          "cachedResultName": "Time Tracker"
        },
        "filterType": "manual"
      },
      "credentials": {
        "notionApi": {
          "id": "03mmrqQX1rffebZp",
          "name": "Notion David"
        }
      },
      "typeVersion": 2.2,
      "alwaysOutputData": true
    },
    {
      "id": "bca3aff3-2d7d-4cc0-8842-5de6db67fccd",
      "name": "Set Message - End time already tracked",
      "type": "n8n-nodes-base.set",
      "position": [
        2080,
        960
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "419d7570-d1ce-44b1-814c-7757da92a188",
              "name": "message",
              "type": "string",
              "value": "End time already tracked."
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "a774ac50-49f3-420b-96c5-e97f46857f02",
      "name": "Set Message - End time tracked",
      "type": "n8n-nodes-base.set",
      "position": [
        2080,
        780
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "419d7570-d1ce-44b1-814c-7757da92a188",
              "name": "message",
              "type": "string",
              "value": "End Time Tracked!"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "f50f5fc4-cf29-406b-940f-e8294c459b7f",
      "name": "Set Message - Start time not yet tracked",
      "type": "n8n-nodes-base.set",
      "position": [
        2080,
        1140
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "419d7570-d1ce-44b1-814c-7757da92a188",
              "name": "message",
              "type": "string",
              "value": "Today's start time not yet tracked!"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "0450fc1d-9c3b-4af6-b5a4-52dc971a1a2e",
      "name": "Set Message - Start not yet tracked",
      "type": "n8n-nodes-base.set",
      "position": [
        2080,
        520
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "419d7570-d1ce-44b1-814c-7757da92a188",
              "name": "message",
              "type": "string",
              "value": "Today's start time not yet tracked!"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "fa1855df-e3b5-4052-b26a-7be840bcaf0c",
      "name": "Set Message - Break time tracked",
      "type": "n8n-nodes-base.set",
      "position": [
        2080,
        140
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "419d7570-d1ce-44b1-814c-7757da92a188",
              "name": "message",
              "type": "string",
              "value": "=Tracked {{ $('Set Break Duration').item.json.break_duration }} minutes as break time."
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "3ba94d34-18e8-49d8-8924-4837d815e183",
      "name": "Set Message - Break time updated",
      "type": "n8n-nodes-base.set",
      "position": [
        2080,
        320
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "419d7570-d1ce-44b1-814c-7757da92a188",
              "name": "message",
              "type": "string",
              "value": "=Updated break time to {{ $('Set Break Duration').item.json.break_duration }} minutes."
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "42465160-7eec-43ed-93ad-1d73745911a0",
      "name": "Set Message - Start time already tracked",
      "type": "n8n-nodes-base.set",
      "position": [
        2080,
        -300
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "419d7570-d1ce-44b1-814c-7757da92a188",
              "name": "message",
              "type": "string",
              "value": "Start time already tracked."
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "8d35a443-f8ef-40fd-b7a0-8933a7a38b27",
      "name": "Set Message - Start time already tracked1",
      "type": "n8n-nodes-base.set",
      "position": [
        2080,
        -120
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "419d7570-d1ce-44b1-814c-7757da92a188",
              "name": "message",
              "type": "string",
              "value": "Start time tracked."
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "ee6e5e70-1d27-4edc-88d8-74b44611df39",
      "name": "Get notion page with todays date",
      "type": "n8n-nodes-base.notion",
      "position": [
        740,
        -200
      ],
      "parameters": {
        "limit": 1,
        "filters": {
          "conditions": [
            {
              "key": "Date|formula",
              "condition": "equals",
              "textValue": "={{ $now.format('dd.MM.yyyy') }}",
              "returnType": "text"
            }
          ]
        },
        "options": {},
        "resource": "databasePage",
        "operation": "getAll",
        "databaseId": {
          "__rl": true,
          "mode": "list",
          "value": "1117f2f5-baf9-8054-b33b-efb4d8a3c7ab",
          "cachedResultUrl": "https://www.notion.so/1117f2f5baf98054b33befb4d8a3c7ab",
          "cachedResultName": "Time Tracker"
        },
        "filterType": "manual"
      },
      "credentials": {
        "notionApi": {
          "id": "03mmrqQX1rffebZp",
          "name": "Notion David"
        }
      },
      "typeVersion": 2.2,
      "alwaysOutputData": true
    },
    {
      "id": "875f1969-4958-4450-87a5-aad1f65b3a9d",
      "name": "Switch",
      "type": "n8n-nodes-base.switch",
      "position": [
        260,
        260
      ],
      "parameters": {
        "rules": {
          "values": [
            {
              "outputKey": "Start",
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
                      "operation": "equals"
                    },
                    "leftValue": "={{ $json.body.method }}",
                    "rightValue": "start"
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "Break",
              "conditions": {
                "options": {
                  "leftValue": "",
                  "caseSensitive": true,
                  "typeValidation": "strict"
                },
                "combinator": "and",
                "conditions": [
                  {
                    "id": "6ddd1f12-a0d8-42df-9776-dff0f44ba82c",
                    "operator": {
                      "name": "filter.operator.equals",
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $json.body.method }}",
                    "rightValue": "break"
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "End",
              "conditions": {
                "options": {
                  "leftValue": "",
                  "caseSensitive": true,
                  "typeValidation": "strict"
                },
                "combinator": "and",
                "conditions": [
                  {
                    "id": "61550dac-65a2-4e4b-99a8-4df4a357cec0",
                    "operator": {
                      "name": "filter.operator.equals",
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $json.body.method }}",
                    "rightValue": "end"
                  }
                ]
              },
              "renameOutput": true
            }
          ]
        },
        "options": {}
      },
      "typeVersion": 3.1
    },
    {
      "id": "ab59018e-a41c-4c48-9aa7-33d123cb2215",
      "name": "Get notion page with todays date1",
      "type": "n8n-nodes-base.notion",
      "position": [
        740,
        840
      ],
      "parameters": {
        "limit": 1,
        "filters": {
          "conditions": [
            {
              "key": "Date|formula",
              "condition": "equals",
              "textValue": "={{ $now.format('dd.MM.yyyy') }}",
              "returnType": "text"
            }
          ]
        },
        "options": {},
        "resource": "databasePage",
        "operation": "getAll",
        "databaseId": {
          "__rl": true,
          "mode": "list",
          "value": "1117f2f5-baf9-8054-b33b-efb4d8a3c7ab",
          "cachedResultUrl": "https://www.notion.so/1117f2f5baf98054b33befb4d8a3c7ab",
          "cachedResultName": "Time Tracker"
        },
        "filterType": "manual"
      },
      "credentials": {
        "notionApi": {
          "id": "03mmrqQX1rffebZp",
          "name": "Notion David"
        }
      },
      "typeVersion": 2.2,
      "alwaysOutputData": true
    },
    {
      "id": "8cbdbe7f-3c32-48bb-bce6-80b918a7c31e",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        480,
        -400
      ],
      "parameters": {
        "width": 2127.3212174343475,
        "height": 469.85870733996774,
        "content": "## Track start time"
      },
      "typeVersion": 1
    },
    {
      "id": "e930da00-916b-4767-a34e-b985d97090ca",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        480,
        108.01971369783018
      ],
      "parameters": {
        "width": 2127.3212174343475,
        "height": 596.8497421429678,
        "content": "## Track break duration"
      },
      "typeVersion": 1
    },
    {
      "id": "6b77fcde-e3ed-4cfa-bd89-9d1cc6660591",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        480,
        740
      ],
      "parameters": {
        "width": 2127.3212174343475,
        "height": 627.9984865286092,
        "content": "## Track end time"
      },
      "typeVersion": 1
    },
    {
      "id": "85b40d37-3a55-4346-8c94-60eb2f8b6dba",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -104.58827842609037,
        -400
      ],
      "parameters": {
        "color": 4,
        "width": 538.9177312302156,
        "height": 1760.750302860566,
        "content": "## API Endpoint Trigger"
      },
      "typeVersion": 1
    },
    {
      "id": "c09f93f1-a2c0-4146-8853-5283bd419a73",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -102.50502117110727,
        -680
      ],
      "parameters": {
        "color": 6,
        "width": 534.5813587043364,
        "height": 247.95862766773985,
        "content": "## Setup instructions\nVisit our [Unitize Documents](https://docs.unitize.de) to create a copy of the Time Tracker database as well as download the iOS Shortcut."
      },
      "typeVersion": 1
    },
    {
      "id": "bfe988d1-81c5-4c70-affd-220cfc5016da",
      "name": "Respond to Webhook",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        2780,
        320
      ],
      "parameters": {
        "options": {},
        "respondWith": "text",
        "responseBody": "={{ $json.message }}"
      },
      "typeVersion": 1.1
    },
    {
      "id": "585efbae-ec10-4ef4-90a0-7bad55b4a150",
      "name": "Sticky Note5",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2640,
        -400
      ],
      "parameters": {
        "color": 4,
        "width": 415.1572200385813,
        "height": 1766.1026447605514,
        "content": "## Respond to iOS Shortcut"
      },
      "typeVersion": 1
    },
    {
      "id": "b75485ce-d365-4743-a4ee-e16799e12c24",
      "name": "Webhook - Track Time",
      "type": "n8n-nodes-base.webhook",
      "position": [
        -20,
        260
      ],
      "webhookId": "752a7723-87b6-470f-a7d3-f627f6457e39",
      "parameters": {
        "path": "track-time",
        "options": {},
        "httpMethod": "POST",
        "responseMode": "responseNode"
      },
      "typeVersion": 2
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "f0e95932-b61d-4fcf-a3a6-5cef415fd8fe",
  "connections": {
    "If": {
      "main": [
        [
          {
            "node": "Update page with end date",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Set Message - End time already tracked",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch": {
      "main": [
        [
          {
            "node": "Get notion page with todays date",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Set Break Duration",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Get notion page with todays date1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "If page exist": {
      "main": [
        [
          {
            "node": "Set Message - Start time already tracked",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Create new page",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "If page exist1": {
      "main": [
        [
          {
            "node": "If",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Set Message - Start time not yet tracked",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Create new page": {
      "main": [
        [
          {
            "node": "Set Message - Start time already tracked1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "If page responded": {
      "main": [
        [
          {
            "node": "If pause_in_minuten is empty",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Set Message - Start not yet tracked",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set Break Duration": {
      "main": [
        [
          {
            "node": "Get notion page by date",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Webhook - Track Time": {
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
    "Get notion page by date": {
      "main": [
        [
          {
            "node": "If page responded",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Update page with end date": {
      "main": [
        [
          {
            "node": "Set Message - End time tracked",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "If pause_in_minuten is empty": {
      "main": [
        [
          {
            "node": "Set break duration for current day",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Update break duration for current day",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set Message - End time tracked": {
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
    "Get notion page with todays date": {
      "main": [
        [
          {
            "node": "If page exist",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set Message - Break time tracked": {
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
    "Set Message - Break time updated": {
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
    "Get notion page with todays date1": {
      "main": [
        [
          {
            "node": "If page exist1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set break duration for current day": {
      "main": [
        [
          {
            "node": "Set Message - Break time tracked",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set Message - Start not yet tracked": {
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
    "Update break duration for current day": {
      "main": [
        [
          {
            "node": "Set Message - Break time updated",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set Message - End time already tracked": {
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
    "Set Message - Start time already tracked": {
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
    "Set Message - Start time not yet tracked": {
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
    "Set Message - Start time already tracked1": {
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

<a id="template-357"></a>

## Template 357 - Iniciar workflows com tag 'Auto start'

- **Nome:** Iniciar workflows com tag 'Auto start'
- **Descrição:** Ao ser executado, obtém todos os workflows da instância e ativa aqueles que possuem a tag 'Auto start', permitindo que workflows importados ou recém-carregados iniciem automaticamente.
- **Funcionalidade:** • Disparo manual/automático de início: Pode ser executado manualmente para testes ou agendado/acionado após a inicialização para executar automaticamente.
• Obtenção de workflows: Consulta todos os workflows disponíveis na instância através da API.
• Verificação de tags: Verifica se a lista de tags de cada workflow contém a tag "Auto start".
• Ativação de workflows: Ativa os workflows que têm a tag indicada, garantindo que os fluxos marcados sejam executados.
• Compatibilidade com deploy automatizado: Projetado para integrar-se a processos de importação/implantação que trazem workflows para a instância.
- **Ferramentas:** • API de gestão de workflows: Interface HTTP usada para listar e ativar workflows; requer chave de API para autenticação.
• Pipeline de CI/CD: Integração opcional para acionar o fluxo após processos automatizados de deploy/importação.
• Plataforma de containers/órquestrador: Ambiente que executa o serviço e importa workflows, permitindo rodar este fluxo no boot (por exemplo, contêineres Docker ou orquestradores).

## Fluxo visual

```mermaid
flowchart LR
    N1["n8n"]
    N2["TAG? Auto start"]
    N3["n8n1"]
    N4["When clicking ‘Test workflow’"]
    N5["Sticky Note4"]

    N1 --> N2
    N2 --> N3
    N4 --> N1
```

## Fluxo (.json) :

```json
{
  "nodes": [
    {
      "id": "142277c6-73a5-4b99-9e94-72655bbe0ea8",
      "name": "n8n",
      "type": "n8n-nodes-base.n8n",
      "position": [
        -420,
        -120
      ],
      "parameters": {
        "filters": {},
        "requestOptions": {}
      },
      "credentials": {
        "n8nApi": {
          "id": "4v19HuBPwx43oswi",
          "name": "n8n account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "6adf03cb-4194-4616-99d0-6495a660c283",
      "name": "TAG? Auto start",
      "type": "n8n-nodes-base.if",
      "position": [
        -180,
        -120
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
              "id": "03241d00-9ec1-4215-8036-2d219a7874cb",
              "operator": {
                "type": "array",
                "operation": "contains",
                "rightType": "any"
              },
              "leftValue": "={{ $json.tags.map((obj) => obj.name) }}",
              "rightValue": "Auto start"
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "8bd4868a-6dec-48b9-8593-36badf42d7ff",
      "name": "n8n1",
      "type": "n8n-nodes-base.n8n",
      "position": [
        100,
        -120
      ],
      "parameters": {
        "operation": "activate",
        "workflowId": {
          "__rl": true,
          "mode": "id",
          "value": "={{ $json.id }}"
        },
        "requestOptions": {}
      },
      "credentials": {
        "n8nApi": {
          "id": "4v19HuBPwx43oswi",
          "name": "n8n account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "c2b7a716-ab5f-4e49-b340-eab6721c52e4",
      "name": "When clicking ‘Test workflow’",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        -640,
        -120
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "0090a343-73fd-4c53-b80b-27dd2789a849",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -680,
        -580
      ],
      "parameters": {
        "color": 5,
        "width": 620,
        "height": 420,
        "content": "# Auto Starter\n\nOn importing workflows these will not be auto started, even if the old version was running. To fix this we created this workflow that can be run after n8n starts. It fits in our auto deploy pipeline and modified n8n container that will import workflows, start n8n and start the tagged workflows.\n\n- Start this workflow after n8n starts.\n- It will get all workflows in the running n8n instance.\n- If the files have a tag **'Auto start'** the workflow will be started.\n\n\n**Configuration**\n- You need a a **n8n api key** configured."
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "n8n": {
      "main": [
        [
          {
            "node": "TAG? Auto start",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "TAG? Auto start": {
      "main": [
        [
          {
            "node": "n8n1",
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
            "node": "n8n",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-358"></a>

## Template 358 - Adicionar/Atualizar contato no ActiveCampaign

- **Nome:** Adicionar/Atualizar contato no ActiveCampaign
- **Descrição:** Fluxo acionado manualmente que cria ou atualiza um contato no ActiveCampaign usando o e-mail e campos opcionais de nome.
- **Funcionalidade:** • Início manual: o fluxo é iniciado ao clicar em 'executar', permitindo acionamento manual quando necessário.
• Criação/atualização de contato: envia um endereço de e-mail para o ActiveCampaign e cria um novo contato ou atualiza um existente.
• Campos adicionais de contato: permite incluir primeiro nome e sobrenome para o contato.
• Atualização condicional: se o contato já existir (mesmo e-mail), os dados são atualizados automaticamente.
• Autenticação via credenciais: usa credenciais configuradas do ActiveCampaign para realizar a operação.
- **Ferramentas:** • ActiveCampaign: plataforma de automação de marketing e CRM usada para criar, atualizar e gerenciar contatos e campanhas.

## Fluxo visual

```mermaid
flowchart LR
    N1["On clicking 'execute'"]
    N2["ActiveCampaign"]

    N1 --> N2
```

## Fluxo (.json) :

```json
{
  "name": "",
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        600,
        250
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "ActiveCampaign",
      "type": "n8n-nodes-base.activeCampaign",
      "position": [
        800,
        250
      ],
      "parameters": {
        "email": "",
        "updateIfExists": true,
        "additionalFields": {
          "lastName": "",
          "firstName": ""
        }
      },
      "credentials": {
        "activeCampaignApi": "ActiveCampaign"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "ActiveCampaign",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-359"></a>

## Template 359 - Assistente de documentos por Telegram

- **Nome:** Assistente de documentos por Telegram
- **Descrição:** Um assistente via Telegram que recebe PDFs, extrai texto, indexa trechos em um banco vetorial e responde a perguntas usando um modelo de linguagem, com suporte a mensagens formatadas e divisão de respostas longas.
- **Funcionalidade:** • Recepção de mensagens e documentos pelo Telegram: Detecta textos, comandos e arquivos enviados pelos usuários.
• Suporte a PDF: Aceita upload de arquivos PDF, recusa tipos não suportados e informa o usuário.
• Download e extração de texto do PDF: Faz o download do arquivo enviado e extrai o conteúdo textual.
• Quebra de texto em trechos: Divide o conteúdo em partes menores apropriadas para geração de embeddings e armazenamento.
• Geração de embeddings: Converte trechos de texto em vetores semânticos para indexação.
• Armazenamento em banco vetorial: Insere embeddings e metadados em uma tabela vetorial para busca por similaridade.
• Busca por similaridade para resposta contextualizada: Recupera trechos relevantes do banco vetorial quando a pergunta referencia documentos.
• Geração de respostas com modelo de linguagem: Combina memória do usuário e trechos recuperados para gerar respostas coerentes.
• Pós-processamento de formatação HTML: Remove tags não suportadas pelo Telegram e escapa caracteres especiais no texto.
• Chunking de mensagens longas: Divide respostas extensas em partes respeitando o limite de ~4096 caracteres do Telegram.
• Mensagens de status: Envia notificações sobre processamento do documento, conclusão e erros/arquivos não suportados.
• Integração opcional de dados em tempo real: Permite incluir informações externas, como condições climáticas, quando solicitado.
- **Ferramentas:** • Telegram API: Canal de comunicação com os usuários para receber mensagens, arquivos e enviar respostas formatadas.
• Google Gemini (PaLM): Modelo de linguagem usado para gerar respostas e para criar embeddings semânticos dos trechos de texto.
• Supabase (com extensão pgvector): Banco de dados para armazenar embeddings, conteúdo e metadados, permitindo buscas por similaridade.
• OpenWeatherMap: Serviço opcional para fornecer dados meteorológicos em tempo real quando solicitado pelo usuário.

## Fluxo visual

```mermaid
flowchart LR
    N1["Google Gemini Chat Model"]
    N2["OpenWeatherMap"]
    N3["AI Agent"]
    N4["Telegram Trigger"]
    N5["Telegram"]
    N6["Think"]
    N7["Embeddings Google Gemini"]
    N8["Default Data Loader"]
    N9["Recursive Character Text Splitter"]
    N10["Extract from File"]
    N11["Answer questions with a vector store"]
    N12["Supabase Vector Store"]
    N13["Sticky Note10"]
    N14["Sticky Note11"]
    N15["Telegram - Embedding Complete"]
    N16["Supabase - Save Embeddings"]
    N17["Command Router"]
    N18["Telegram - Download file"]
    N19["Aggregate"]
    N20["Fallback- No formatting"]
    N21["Split Out"]
    N22["Simple Memory"]
    N23["Handle formatting and split"]
    N24["Sticky Note"]
    N25["Manual Mapping"]
    N26["Unsupported message"]
    N27["Send processing document message"]
    N28["Send embedding Started message"]

    N3 --> N23
    N5 --> N20
    N19 --> N15
    N21 --> N25
    N17 --> N18
    N17 --> N3
    N17 --> N26
    N25 --> N5
    N4 --> N17
    N10 --> N16
    N10 --> N28
    N18 --> N10
    N18 --> N27
    N16 --> N19
    N23 --> N21
```

## Fluxo (.json) :

```json
{
  "id": "LL0TBxEbXoK2zhqp",
  "meta": {
    "instanceId": "af80dcc2dbd3882359ca17a5fe5b2d4bd4ca3cf3cbe39546ecc263e2e97807e5",
    "templateId": "self-building-ai-agent",
    "templateCredsSetupCompleted": true
  },
  "name": "AI Document Assistant via Telegram + Supabase",
  "tags": [
    {
      "id": "Fo1OtHUY0RXxPbjJ",
      "name": "google-gemini",
      "createdAt": "2025-05-01T23:10:32.399Z",
      "updatedAt": "2025-05-01T23:10:32.399Z"
    },
    {
      "id": "HcgCSAB27xdCFyCf",
      "name": "vectorstore",
      "createdAt": "2025-05-01T23:10:13.148Z",
      "updatedAt": "2025-05-01T23:10:13.148Z"
    },
    {
      "id": "NFkP0TdshXJdwIOG",
      "name": "chatbot",
      "createdAt": "2025-05-01T23:09:53.855Z",
      "updatedAt": "2025-05-01T23:09:53.855Z"
    },
    {
      "id": "QXeMQNrN4XlEXs1I",
      "name": "telegram",
      "createdAt": "2025-05-01T23:09:23.634Z",
      "updatedAt": "2025-05-01T23:09:23.634Z"
    },
    {
      "id": "RLZgltwJo60sK1Dm",
      "name": "embeddings",
      "createdAt": "2025-05-01T23:10:20.621Z",
      "updatedAt": "2025-05-01T23:10:20.621Z"
    },
    {
      "id": "fMH2im2pHJBOzkXp",
      "name": "document-qa",
      "createdAt": "2025-05-01T23:10:07.948Z",
      "updatedAt": "2025-05-01T23:10:07.948Z"
    },
    {
      "id": "ghpuX9kkAqpLyIVR",
      "name": "n8n-ai",
      "createdAt": "2025-05-01T23:10:38.373Z",
      "updatedAt": "2025-05-01T23:10:38.373Z"
    },
    {
      "id": "tSHEttl48VrqMYiV",
      "name": "supabase",
      "createdAt": "2025-05-01T23:10:16.583Z",
      "updatedAt": "2025-05-01T23:10:16.583Z"
    }
  ],
  "nodes": [
    {
      "id": "0213dfab-a1b2-42c9-9ab1-8a0f1de4c4c0",
      "name": "Google Gemini Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatGoogleGemini",
      "position": [
        480,
        40
      ],
      "parameters": {
        "options": {},
        "modelName": "models/gemini-2.5-flash-preview-04-17"
      },
      "credentials": {
        "googlePalmApi": {
          "id": "QuysglXiB421WI90",
          "name": "Google Gemini(PaLM) Api account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "9c166f83-8ea4-4dc7-8ea2-92ec186c9f32",
      "name": "OpenWeatherMap",
      "type": "n8n-nodes-base.openWeatherMapTool",
      "position": [
        740,
        -100
      ],
      "parameters": {
        "cityName": "={{ /*n8n-auto-generated-fromAI-override*/ $fromAI('City', ``, 'string') }}"
      },
      "credentials": {
        "openWeatherMapApi": {
          "id": "MCzSGdWHBJE7l1aN",
          "name": "OpenWeatherMap account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "aa0abeff-b5e9-497b-9d9c-8f79721a5c11",
      "name": "AI Agent",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        480,
        -320
      ],
      "parameters": {
        "text": "={{ $json.message.text }}",
        "options": {
          "systemMessage": "=4. If the user sends you a message starting with / sign, it means this is a Telegram bot command. For example, all users send /start command as their first message. Try to figure out what these commands mean and reply accodringly.\nUser can only send pdf files and text messages and let them know that this type is not supported if it was not a PDF file or text.\nAt first let them know that they can ask questions about sent PDF files you can use your own capabilities as well. \nGenerate a detailed, well-structured response ,\nFormat the response strictly using Telegram's supported HTML syntax. Use tags like <b>, <i>, <u>, <s>, <span class=\"tg-spoiler\">, <code>, <pre> (with optional <code class=\"language-...\"> inside), <a href=\"...\">, and <blockquote> where appropriate.\n\nStructure the content logically using paragraphs and distinct sections. **Be mindful that this text might need to be split into multiple messages due to character limits (Telegram's limit is around 4096 characters per message). Try to make sections or paragraphs relatively self-contained where possible to facilitate splitting.**\n\n**Ensure all <, >, and & symbols within the *text content* (i.e., not part of an HTML tag or entity) are replaced with the corresponding HTML entities: < with &lt;, > with &gt;, and & with &amp;.**\n\nMaintain proper nesting of HTML tags according to Telegram's rules. While the final splitting will be handled by a script, aim for a structure that is easy to break into logical parts without leaving tags improperly open mid-message."
        },
        "promptType": "define",
        "hasOutputParser": true
      },
      "typeVersion": 1.9
    },
    {
      "id": "72b85aff-4fe7-4705-a07c-463f381cb806",
      "name": "Telegram Trigger",
      "type": "n8n-nodes-base.telegramTrigger",
      "position": [
        -20,
        100
      ],
      "webhookId": "d4f286b2-8094-40e3-aeb2-813eb1895ecf",
      "parameters": {
        "updates": [
          "message"
        ],
        "additionalFields": {}
      },
      "credentials": {
        "telegramApi": {
          "id": "jOxapcl3g1n1HrCE",
          "name": "Telegram account"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "ea716dba-2856-40a8-ad73-86132f52dda8",
      "name": "Telegram",
      "type": "n8n-nodes-base.telegram",
      "onError": "continueErrorOutput",
      "position": [
        1540,
        -320
      ],
      "webhookId": "137d8d2f-a941-4803-8646-8932525360c3",
      "parameters": {
        "text": "={{ $json.text }}",
        "chatId": "={{ $json.chatId }}",
        "additionalFields": {
          "parse_mode": "HTML",
          "appendAttribution": false
        }
      },
      "credentials": {
        "telegramApi": {
          "id": "jOxapcl3g1n1HrCE",
          "name": "Telegram account"
        }
      },
      "typeVersion": 1.2,
      "alwaysOutputData": true
    },
    {
      "id": "59a22620-0d26-4e19-940a-5c07efccbdfa",
      "name": "Think",
      "type": "@n8n/n8n-nodes-langchain.toolThink",
      "position": [
        640,
        -100
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "7bb66887-c9c6-4057-bbc0-306d1e20ea12",
      "name": "Embeddings Google Gemini",
      "type": "@n8n/n8n-nodes-langchain.embeddingsGoogleGemini",
      "position": [
        840,
        340
      ],
      "parameters": {
        "modelName": "models/text-embedding-004"
      },
      "credentials": {
        "googlePalmApi": {
          "id": "QuysglXiB421WI90",
          "name": "Google Gemini(PaLM) Api account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "668db8fd-3d5f-433a-8ccb-4bea237107ce",
      "name": "Default Data Loader",
      "type": "@n8n/n8n-nodes-langchain.documentDefaultDataLoader",
      "position": [
        1220,
        460
      ],
      "parameters": {
        "options": {}
      },
      "typeVersion": 1
    },
    {
      "id": "d1495354-bfc0-4ef1-9102-dc3577580d5b",
      "name": "Recursive Character Text Splitter",
      "type": "@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter",
      "position": [
        1440,
        620
      ],
      "parameters": {
        "options": {}
      },
      "typeVersion": 1
    },
    {
      "id": "6a8e5ce6-4c52-4ca0-962f-045ea42dac7c",
      "name": "Extract from File",
      "type": "n8n-nodes-base.extractFromFile",
      "position": [
        1020,
        480
      ],
      "parameters": {
        "options": {},
        "operation": "pdf"
      },
      "typeVersion": 1,
      "alwaysOutputData": true
    },
    {
      "id": "3f4a9da9-0364-4861-a6f3-33b1d5c501e0",
      "name": "Answer questions with a vector store",
      "type": "@n8n/n8n-nodes-langchain.toolVectorStore",
      "position": [
        860,
        -60
      ],
      "parameters": {
        "description": "Use this data if the user's question appears to reference an uploaded file, document content, or specific information that might be stored in prior user documents. If not relevant, ignore this source."
      },
      "typeVersion": 1.1
    },
    {
      "id": "933a93c7-9401-4bac-9b9c-395866b46d61",
      "name": "Supabase Vector Store",
      "type": "@n8n/n8n-nodes-langchain.vectorStoreSupabase",
      "position": [
        760,
        80
      ],
      "parameters": {
        "options": {
          "queryName": "match_documents"
        },
        "tableName": {
          "__rl": true,
          "mode": "list",
          "value": "user_knowledge_base",
          "cachedResultName": "user_knowledge_base"
        }
      },
      "credentials": {
        "supabaseApi": {
          "id": "jq6dt73fwyUImYqH",
          "name": "Supabase account"
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "5f37c202-a1ca-4ee0-9de0-267349adffbd",
      "name": "Sticky Note10",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        360,
        200
      ],
      "parameters": {
        "color": 5,
        "width": 1625,
        "height": 779,
        "content": "✅ Scenario 2 – Document Upload and Embedding\n\nFlow for downloading a document sent via Telegram, extracting its text, generating embeddings, and inserting them into Supabase Vector Store."
      },
      "typeVersion": 1
    },
    {
      "id": "6e9c1070-90bc-4ab7-a8a0-62461bede708",
      "name": "Sticky Note11",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        360,
        -420
      ],
      "parameters": {
        "color": 5,
        "width": 1625,
        "height": 599,
        "content": "✅ Scenario 1 – Chatbot Interaction\n\nFlow for handling user messages sent to the bot. Includes accessing weather data, answering questions based on user-uploaded documents, and running code using a code execution tool."
      },
      "typeVersion": 1
    },
    {
      "id": "3b211a14-6813-459f-8d23-b40fc0eb4bd6",
      "name": "Telegram - Embedding Complete",
      "type": "n8n-nodes-base.telegram",
      "position": [
        1760,
        320
      ],
      "webhookId": "4eaead72-f9a7-49a3-95ca-b3bc8f6b9a95",
      "parameters": {
        "text": "=✅ Document saved!\nFeel free to start asking questions about it.",
        "chatId": "={{ $('Command Router').item.json.message.chat.id }}",
        "additionalFields": {
          "appendAttribution": false
        }
      },
      "credentials": {
        "telegramApi": {
          "id": "jOxapcl3g1n1HrCE",
          "name": "Telegram account"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "05703266-aaed-491d-87a6-ed7f96a9c49a",
      "name": "Supabase - Save Embeddings",
      "type": "@n8n/n8n-nodes-langchain.vectorStoreSupabase",
      "position": [
        1200,
        320
      ],
      "parameters": {
        "mode": "insert",
        "options": {},
        "tableName": {
          "__rl": true,
          "mode": "list",
          "value": "user_knowledge_base",
          "cachedResultName": "user_knowledge_base"
        }
      },
      "credentials": {
        "supabaseApi": {
          "id": "jq6dt73fwyUImYqH",
          "name": "Supabase account"
        }
      },
      "typeVersion": 1.1,
      "alwaysOutputData": false
    },
    {
      "id": "3b7db0e6-b551-4698-921a-306e837ceffc",
      "name": "Command Router",
      "type": "n8n-nodes-base.switch",
      "position": [
        160,
        100
      ],
      "parameters": {
        "rules": {
          "values": [
            {
              "outputKey": "document",
              "conditions": {
                "options": {
                  "version": 2,
                  "leftValue": "",
                  "caseSensitive": true,
                  "typeValidation": "loose"
                },
                "combinator": "and",
                "conditions": [
                  {
                    "id": "895b32db-777d-4d8e-b1d3-596cc9863d09",
                    "operator": {
                      "type": "boolean",
                      "operation": "exists",
                      "singleValue": true
                    },
                    "leftValue": "={{ $json.message.document }}",
                    "rightValue": "={{ $json.message.document }}"
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "text",
              "conditions": {
                "options": {
                  "version": 2,
                  "leftValue": "",
                  "caseSensitive": true,
                  "typeValidation": "loose"
                },
                "combinator": "and",
                "conditions": [
                  {
                    "id": "26c12573-8e00-4832-8410-73d2d739c455",
                    "operator": {
                      "type": "boolean",
                      "operation": "exists",
                      "singleValue": true
                    },
                    "leftValue": "={{ $json.message.text }}",
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
        },
        "looseTypeValidation": true
      },
      "typeVersion": 3.2
    },
    {
      "id": "fa06fc6c-3661-4065-81fc-09f93d6a4a25",
      "name": "Telegram - Download file",
      "type": "n8n-nodes-base.telegram",
      "position": [
        600,
        540
      ],
      "webhookId": "11b8f884-34bc-401c-8978-b28507d96e40",
      "parameters": {
        "fileId": "={{ $('Telegram Trigger').item.json.message.document.file_id }}",
        "resource": "file"
      },
      "credentials": {
        "telegramApi": {
          "id": "jOxapcl3g1n1HrCE",
          "name": "Telegram account"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "756a36aa-187d-48ca-894c-f8c9a79a4794",
      "name": "Aggregate",
      "type": "n8n-nodes-base.aggregate",
      "notes": "This is used to flag the end of progress—no real aggregation.",
      "position": [
        1580,
        320
      ],
      "parameters": {
        "options": {},
        "fieldsToAggregate": {
          "fieldToAggregate": [
            {}
          ]
        }
      },
      "notesInFlow": true,
      "typeVersion": 1
    },
    {
      "id": "3b49f357-5d21-4710-bd32-3218d23b1bd9",
      "name": "Fallback- No formatting",
      "type": "n8n-nodes-base.telegram",
      "notes": "This is used if, even after HTML formatting,g Telegram wasn't able to process the text, so we send it without formatting.",
      "position": [
        1740,
        -260
      ],
      "webhookId": "dd2182fe-0b11-4d96-9838-30d60bf8c229",
      "parameters": {
        "text": "={{ $('Manual Mapping').item.json.text }}",
        "chatId": "={{ $('Manual Mapping').item.json.chatId }}",
        "additionalFields": {
          "appendAttribution": false
        }
      },
      "credentials": {
        "telegramApi": {
          "id": "jOxapcl3g1n1HrCE",
          "name": "Telegram account"
        }
      },
      "notesInFlow": true,
      "typeVersion": 1.2
    },
    {
      "id": "eafdbacb-17e5-4de6-a4e9-b986140353e5",
      "name": "Split Out",
      "type": "n8n-nodes-base.splitOut",
      "position": [
        1120,
        -320
      ],
      "parameters": {
        "options": {},
        "fieldToSplitOut": "output"
      },
      "typeVersion": 1
    },
    {
      "id": "538be3ed-4bd6-4295-ac11-e4d46b943f5a",
      "name": "Simple Memory",
      "type": "@n8n/n8n-nodes-langchain.memoryBufferWindow",
      "position": [
        540,
        -100
      ],
      "parameters": {
        "sessionKey": "={{ $('Telegram Trigger').item.json.message.from.id }}",
        "sessionIdType": "customKey"
      },
      "typeVersion": 1.3
    },
    {
      "id": "0afca77d-0e08-4f04-a6d3-b107c1dd54f9",
      "name": "Handle formatting and split",
      "type": "n8n-nodes-base.code",
      "notes": "This is used to prevent Markdown issues in Telegram while sending messages.",
      "position": [
        900,
        -320
      ],
      "parameters": {
        "language": "python",
        "pythonCode": "import re\nimport html\n\ngemini_output_text = _('AI Agent').first().json.output;\n# Regex to match any HTML tag <...>\nHTML_TAG_PATTERN = re.compile(r'(<[^>]*?>)', re.IGNORECASE)\n\n# List of UNSUPPORTED Telegram HTML tag names\nUNSUPPORTED_TAG_NAMES = [\n    'p', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ul', 'ol',\n    'table', 'thead', 'tbody', 'tr', 'td', 'th', 'div', 'br', 'font',\n    'span', # Span is unsupported *unless* it has the specific class\n    'a'     # A is unsupported *unless* it has the href attribute\n    # Add more unsupported tags if you encounter them\n]\n\n# Regex to match unsupported opening or closing tags based on the names list\n# This pattern is simplified and might misinterpret complex attributes\nUNSUPPORTED_TAG_PATTERN = re.compile(r'</?(' + '|'.join(UNSUPPORTED_TAG_NAMES) + r')\\b[^>]*?>', re.IGNORECASE)\n\n# Regex to match a span tag *without* the class=\"tg-spoiler\" attribute\n# This tries to capture the tag and its content to remove both\nUNSUPPORTED_SPAN_FULL_PATTERN = re.compile(r'<span(?! class=\"tg-spoiler\"\\b)[^>]*?>.*?</span>', re.IGNORECASE | re.DOTALL) # DOTALL allows . to match newlines\n\n# Regex to match an a tag *without* an href attribute\n# This tries to capture the tag and its content to remove both\nUNSUPPORTED_A_FULL_PATTERN = re.compile(r'<a(?![^>]*href=)[^>]*?>.*?</a>', re.IGNORECASE | re.DOTALL)\n\n\n# --- Cleaning Function (Regex Only) ---\n\ndef unescape_common_html_entities(text):\n    \"\"\"\n    Unescapes a limited set of common HTML entities in text.\n    Does NOT use html.unescape for maximum compatibility with \"no external library\" rule.\n    \"\"\"\n    # Order matters: &amp; must be replaced first!\n    text = text.replace('&amp;', '&')\n    text = text.replace('&lt;', '<')\n    text = text.replace('&gt;', '>')\n    text = text.replace('&quot;', '\"')\n    text = text.replace('&apos;', \"'\")\n    # Add more common entities here if needed, e.g., text = text.replace('&nbsp;', ' ')\n    return text\n\n\ndef clean_html_regex_only(html_string):\n    \"\"\"\n    Cleans HTML string using regex: removes unsupported tags and escapes text content.\n    Handles &apos; and other basic entities.\n    WARNING: This is a regex-based approach and is NOT as robust as using an HTML parser.\n    It may fail on complex or malformed HTML.\n\n    Args:\n        html_string (str): The input HTML string.\n\n    Returns:\n        str: The cleaned HTML string.\n    \"\"\"\n    # 1. Remove unsupported tags and their content where specific attributes are missing\n    # Process specific full patterns first\n    cleaned_text = UNSUPPORTED_SPAN_FULL_PATTERN.sub('', html_string)\n    cleaned_text = UNSUPPORTED_A_FULL_PATTERN.sub('', cleaned_text)\n\n    # 2. Remove remaining unsupported opening/closing tags, leaving content behind\n    cleaned_text = UNSUPPORTED_TAG_PATTERN.sub('', cleaned_text)\n\n    # 3. Split the remaining string into tags and text segments\n    # This pattern captures the tags themselves so we can differentiate them from text\n    parts = HTML_TAG_PATTERN.split(cleaned_text)\n\n    cleaned_parts = []\n    for part in parts:\n        if not part:\n            continue\n\n        if HTML_TAG_PATTERN.fullmatch(part):\n            # If the part is a tag (matches the full tag pattern)\n            # We assume at this point it's a supported tag due to previous removal steps.\n            # Keep the tag as is.\n            cleaned_parts.append(part)\n        else:\n            # If the part is text content\n            # 1. Unescape common HTML entities (like &apos;) that might be in the text\n            unescaped_text = unescape_common_html_entities(part)\n\n            # 2. Escape the literal characters <, >, & that are *in* the text content\n            # This ensures only the characters themselves are escaped, not entities.\n            # Need to escape & first to avoid issues with '&amp;' if it resulted from unescaping or was original.\n            re_escaped_text = unescaped_text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')\n\n            cleaned_parts.append(re_escaped_text)\n\n    # Join the processed parts back into a single string\n    return \"\".join(cleaned_parts)\n\n# --- Splitting Logic ---\nSPLIT_PATTERN_REGEX_ONLY = re.compile(r'(</blockquote>|</pre>|\\n\\n|\\s{2,}|(?<=[.!?])\\s+|<[a-z]+[^>]*?>|</[a-z]+>)', flags=re.IGNORECASE)\n\n\ndef split_telegram_message_regex_only(text, max_length=4096):\n    \"\"\"\n    Splits text into multiple messages based on character count and basic patterns.\n    Operates on text already cleaned by clean_html_regex_only.\n    Does NOT guarantee HTML tag integrity across splits due to lack of parsing.\n\n    Args:\n        text (str): The input text (preferably cleaned by clean_html_regex_only).\n        max_length (int): The maximum length for each message part.\n\n    Returns:\n        list: A list of strings, where each string is a message part.\n    \"\"\"\n    if len(text) <= max_length:\n        return [text]\n\n    messages = []\n    current_chunk = \"\"\n\n    # Split by the defined pattern\n    parts = SPLIT_PATTERN_REGEX_ONLY.split(text)\n\n    for part in parts:\n        # Handle parts that are None (can happen with split) or just short whitespace\n        if part is None or (not part.strip() and len(part) < 2 and part != '\\n\\n'):\n             if part is not None and len(part) > 0: # Keep meaningful whitespace splits like \\n\\n\n                  if len(current_chunk) + len(part) <= max_length:\n                       current_chunk += part\n                  else:\n                       # Split happens within meaningful whitespace, finalize chunk\n                       if current_chunk.strip(): # Only add if chunk has content\n                            messages.append(current_chunk.strip())\n                       current_chunk = part # Start new chunk with the whitespace\n             continue # Skip to next part\n\n\n        # Check if adding the current part exceeds the max length\n        if len(current_chunk) + len(part) > max_length:\n            # If the current chunk is empty or only whitespace after stripping,\n            # it means the 'part' itself is too long to fit in a new chunk.\n            if not current_chunk.strip():\n                # Handle very long individual parts (e.g., a huge code block line, a very long word, a single huge tag)\n                # Hard split the long part. WARNING: This can break tags, words, or escape sequences.\n                while len(part) > max_length:\n                    messages.append(part[:max_length])\n                    part = part[max_length:]\n                if part.strip():\n                    current_chunk = part # Remaining part starts a new chunk\n                else:\n                     current_chunk = \"\" # If remainder is just whitespace, clear\n            else:\n                # The current part makes the chunk too long, finalize the current chunk\n                messages.append(current_chunk.strip())\n                # Start a new chunk with the current part\n                current_chunk = part # Keep original part for the new chunk\n\n        else:\n            # Add the current part to the chunk\n            current_chunk += part\n\n    # Add the last chunk\n    if current_chunk.strip(): # Only add if the final chunk has content\n        messages.append(current_chunk.strip())\n\n    # Clean up any empty messages that might have been created\n    messages = [msg for msg in messages if msg.strip()]\n\n    return messages\n  \ncleaned_html_regex = clean_html_regex_only(gemini_output_text)\nmessage_parts_regex = split_telegram_message_regex_only(cleaned_html_regex)\n\nreturn dict({'output': message_parts_regex })"
      },
      "typeVersion": 2
    },
    {
      "id": "dbea9e13-6ad4-4eb3-8da1-9db9e2116283",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2000,
        -420
      ],
      "parameters": {
        "width": 1960,
        "height": 3520,
        "content": "# 🤖 Telegram AI Assistant for Your Documents (n8n + Supabase + Gemini)\n\nThis project transforms a standard **Telegram bot** into your dedicated AI assistant – designed to understand and answer questions based on **your own documents**. It seamlessly integrates the power of **Google Gemini** for advanced language capabilities and **Supabase's vector database** for efficient, intelligent document retrieval. Built entirely within the no-code platform **n8n**, it allows you to deploy a sophisticated document chatbot without writing a single line of code.\n\nSimply upload any PDF document to the bot, and instantly gain the ability to chat with it, querying its contents as if it were a knowledgeable expert on your uploaded files.\n\n---\n## 📹 Watch the Bot in Action\n\n[![𝗨𝗻𝗹𝗲𝗮𝘀𝗵𝗶𝗻𝗴 𝗔𝗜 𝗼𝗻 𝗠𝘆 𝗕𝗼𝗼𝗸𝘀𝗵𝗲𝗹𝗳: 𝗙𝗹𝗼𝘄 𝗣𝗿𝗼𝗴𝗿𝗮𝗺𝗺𝗶𝗻𝗴 𝗣𝗼𝘄𝗲𝗿𝘀 𝗮 𝗡𝗲𝘅𝘁-𝗟𝗲𝘃𝗲𝗹 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗕𝗼𝘁🤖](https://img.youtube.com/vi/r_KGyJApy5M/maxresdefault.jpg)](https://www.youtube.com/watch?v=r_KGyJApy5M)\n\n**▶️ Click the image above to watch a live demo on YouTube.** \n\nThis video provides a live demonstration of the bot's core features and how it interacts. See a quick walkthrough of its capabilities and user flow.\n\n---\n\n## ✨ Ignite Your Workflow: Use Cases\n\nThis project empowers two core interactions:\n\n### 1. Conversational AI Interface (User Inquiry → Telegram Bot → Intelligent Answers)\n- Users pose questions directly to the Telegram bot.\n- The bot generates relevant, informative answers using the cutting-edge capabilities of the Google Gemini LLM.\n- Leveraging a powerful vector search mechanism, it can pull specific, contextual information from previously uploaded documents to provide highly relevant and informed responses.\n- (Optional) Augment answers with real-time data, like current **weather information**.\n\n### 2. Effortless Document Integration (User Upload PDF → Processing → Searchable Knowledge)\n- Users upload a PDF document directly to the bot.\n- The workflow automatically parses the document content, converts it into numerical representations called embeddings using Gemini's embedding models.\n- These embeddings, alongside the document's text content, are then securely stored in a dedicated **Supabase vector table**, creating a searchable knowledge base.\n- Immediately after successful processing, the document becomes part of the bot's memory, enabling users to ask questions about its contents via the standard chat interface.\n\n---\n## 🧠 Core Intelligence Features\n\n- ✅ **Pure No-Code**: Developed and managed entirely within the intuitive [n8n](https://n8n.io) automation platform.\n- 📄 **Seamless PDF Integration**: Easily upload and process PDF documents to expand the bot's knowledge.\n- 🧠 **Powered by Google Gemini**: Utilizes Gemini for both generating document embeddings and formulating intelligent conversational responses.\n- 🗂 **Vector Database Memory (Supabase)**: Employs **Supabase as a robust vector database** for storing and efficiently searching document embeddings, providing the bot with long-term memory about your content.\n- **⚡️ Rapid & Private Retrieval**: The vector search allows for swift identification and retrieval of the most relevant document snippets based on the user's query. This approach enhances response speed and significantly improves data privacy, as **the original document content remains securely stored in your Supabase instance, and only the user's query and the retrieved relevant chunks are sent to the LLM for generating a response.**\n- 🧹 **Intelligent HTML Post-processing**: Cleans the LLM's responses by removing HTML tags not supported by Telegram while preserving essential formatting and correctly escaping special characters in the text content.\n- 📤 **Adaptive Message Chunking**: Splits lengthy AI-generated answers into multiple messages that adhere to Telegram's 4096-character limit, ensuring the full response is delivered cleanly.\n- 🌦️ **Dynamic Weather Data**: (Optional) Integrates with OpenWeatherMap to provide current weather information upon request.\n- **📝 Note on Usage**: This workflow is designed primarily for **personal, single-user** scenarios. It processes each message independently and **does not include multi-user session management**, making it unsuitable for public deployment where different users require separate conversational contexts. For a session-based Telegram bot implemented in Python, you may refer to this project, which is a multi-model telegram bot: [https://github.com/mohamadghaffari/gemini-tel-bot](https://github.com/mohamadghaffari/gemini-tel-bot).\n---\n\n## 🛠 Getting Started: Setup\n\n### 1. Deploy the Workflow in n8n\n\n- Click the \"Use this workflow\" button on the n8n template page.\n- This will open the workflow directly in your n8n instance, ready for configuration.\n\n\n### 2. Connect Your Services: Configure Credentials\n\nCreate API credentials for the following services within your n8n instance:\n\n| Service          | Purpose                          |\n|------------------|------------------------------------|\n| Telegram API     | Receiving user messages & sending replies |\n| Google Gemini    | Generating embeddings & LLM responses |\n| Supabase         | Storing & searching document vectors |\n| OpenWeatherMap   | (Optional) Fetching weather data    |\n\n### 3. Prepare Your Supabase Knowledge Base\n\nSet up a vector-enabled table in your Supabase project to store your document embeddings. Execute the following SQL commands in your Supabase SQL Editor:\n\n``` sql\n-- Enable the pgvector extension to work with embedding vectors\ncreate extension vector;\n\n-- Create a table to store your documents and their embeddings\ncreate table user_knowledge_base (\n  id bigserial primary key,\n  content text, -- Stores the text chunk from the document\n  metadata jsonb, -- Stores document information (e.g., filename, page number)\n  embedding vector(768) -- Stores the vector representation (embedding) generated by Gemini. Adjust dimension if using a different model.\n);\n\n-- Create a function to perform vector similarity search against your documents\ncreate function match_documents (\n  query_embedding vector(768),\n  match_count int default null,\n  filter jsonb DEFAULT '{}'\n) returns table (\n  id bigint,\n  content text,\n  metadata jsonb,\n  similarity float\n)\nlanguage plpgsql\nas $$\n#variable_conflict use_column\nbegin\n  return query\n  select\n    id,\n    content,\n    metadata,\n    -- Calculate cosine similarity: 1 - cosine distance (using the '<=>' operator provided by pgvector)\n    1 - (user_knowledge_base.embedding <=> query_embedding) as similarity\n  from user_knowledge_base\n  where metadata @> filter -- Optional: filter results based on metadata\n  order by user_knowledge_base.embedding <=> query_embedding -- Order by similarity (closest first)\n  limit match_count; -- Limit the number of results\nend;\n$$;\n````\n\nThis sets up the necessary table and a function to perform vector similarity searches, allowing you to find document chunks most similar to a user's query.\n-----\n\n## 📚 Integrated Technologies\n\nThis project brings together powerful tools:\n\n  - [n8n](https://n8n.io) – The central hub for workflow automation and integration.\n  - [Telegram Bot API](https://core.telegram.org/bots/api) – The communication layer for user interaction.\n  - [Supabase](https://supabase.com/) + [pgvector Extension](https://www.google.com/search?q=https://supabase.com/docs/guides/ai/vector-embeddings) – Provides a scalable database with powerful vector search capabilities.\n  - [Google Gemini API](https://ai.google.dev/) – The intelligence engine for embeddings and text generation.\n  - [OpenWeatherMap API](https://openweathermap.org/api) – (Optional) For adding real-time weather features.\n\n-----\n"
      },
      "typeVersion": 1
    },
    {
      "id": "965ba2bd-747d-4718-a76e-9f7d685dcea4",
      "name": "Manual Mapping",
      "type": "n8n-nodes-base.set",
      "position": [
        1320,
        -320
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "cdeb5bf1-c91c-44ae-bebd-ab3f4ba2561a",
              "name": "text",
              "type": "string",
              "value": "={{ $json.output }}"
            },
            {
              "id": "7cd7d120-96fa-4539-b343-25bc9b75abb4",
              "name": "chatId",
              "type": "number",
              "value": "={{ $('Command Router').item.json.message.from.id }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "c6a315f1-6f0b-4127-b377-b7b12975929f",
      "name": "Unsupported message",
      "type": "n8n-nodes-base.telegram",
      "position": [
        500,
        760
      ],
      "webhookId": "52f3456a-06ef-4799-b245-0293213dcc4b",
      "parameters": {
        "text": "Unsupported command or file. 😓 Please upload a valid PDF document or ask your question regarding your files.",
        "chatId": "={{ $('Command Router').item.json.message.chat.id }}",
        "additionalFields": {
          "appendAttribution": false
        }
      },
      "credentials": {
        "telegramApi": {
          "id": "jOxapcl3g1n1HrCE",
          "name": "Telegram account"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "375bd185-3836-4f25-8708-d6dcd79b2675",
      "name": "Send processing document message",
      "type": "n8n-nodes-base.telegram",
      "position": [
        920,
        720
      ],
      "webhookId": "32ade357-f14b-4d10-91f2-02c8aa6e198e",
      "parameters": {
        "text": "=<b>Processing document...</b>\n<b>Please wait...⏳</b>",
        "chatId": "={{ $('Command Router').item.json.message.chat.id }}",
        "additionalFields": {
          "parse_mode": "HTML",
          "appendAttribution": false
        }
      },
      "credentials": {
        "telegramApi": {
          "id": "jOxapcl3g1n1HrCE",
          "name": "Telegram account"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "d01f8b15-e495-46cf-bfdf-20b4399c23d7",
      "name": "Send embedding Started message",
      "type": "n8n-nodes-base.telegram",
      "position": [
        1220,
        660
      ],
      "webhookId": "32ade357-f14b-4d10-91f2-02c8aa6e198e",
      "parameters": {
        "text": "=<b>Document processed ✅ </b> \n<b>Num of pages:</b> {{ $json.numpages }} \n<b>Creator:</b> {{ $json.info.Creator }}\n<b>Title:</b> {{ $json.info.Title }} \n<b>Version:</b> {{ $json.version }}",
        "chatId": "={{ $('Command Router').item.json.message.chat.id }}",
        "additionalFields": {
          "parse_mode": "HTML",
          "appendAttribution": false
        }
      },
      "credentials": {
        "telegramApi": {
          "id": "jOxapcl3g1n1HrCE",
          "name": "Telegram account"
        }
      },
      "typeVersion": 1.2
    }
  ],
  "active": true,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "749ec7d0-e135-478a-b02e-9241dbf4ab68",
  "connections": {
    "Think": {
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
            "node": "Handle formatting and split",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Telegram": {
      "main": [
        [],
        [
          {
            "node": "Fallback- No formatting",
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
            "node": "Telegram - Embedding Complete",
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
            "node": "Manual Mapping",
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
    "Command Router": {
      "main": [
        [
          {
            "node": "Telegram - Download file",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "AI Agent",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Unsupported message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Manual Mapping": {
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
    "OpenWeatherMap": {
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
    "Telegram Trigger": {
      "main": [
        [
          {
            "node": "Command Router",
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
            "node": "Supabase - Save Embeddings",
            "type": "main",
            "index": 0
          },
          {
            "node": "Send embedding Started message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Default Data Loader": {
      "ai_document": [
        [
          {
            "node": "Supabase - Save Embeddings",
            "type": "ai_document",
            "index": 0
          }
        ]
      ]
    },
    "Supabase Vector Store": {
      "ai_vectorStore": [
        [
          {
            "node": "Answer questions with a vector store",
            "type": "ai_vectorStore",
            "index": 0
          }
        ]
      ]
    },
    "Embeddings Google Gemini": {
      "ai_embedding": [
        [
          {
            "node": "Supabase - Save Embeddings",
            "type": "ai_embedding",
            "index": 0
          },
          {
            "node": "Supabase Vector Store",
            "type": "ai_embedding",
            "index": 0
          }
        ]
      ]
    },
    "Google Gemini Chat Model": {
      "ai_languageModel": [
        [
          {
            "node": "AI Agent",
            "type": "ai_languageModel",
            "index": 0
          },
          {
            "node": "Answer questions with a vector store",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Telegram - Download file": {
      "main": [
        [
          {
            "node": "Extract from File",
            "type": "main",
            "index": 0
          },
          {
            "node": "Send processing document message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Supabase - Save Embeddings": {
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
    "Handle formatting and split": {
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
    "Send embedding Started message": {
      "main": [
        []
      ]
    },
    "Recursive Character Text Splitter": {
      "ai_textSplitter": [
        [
          {
            "node": "Default Data Loader",
            "type": "ai_textSplitter",
            "index": 0
          }
        ]
      ]
    },
    "Answer questions with a vector store": {
      "ai_tool": [
        [
          {
            "node": "AI Agent",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-360"></a>

## Template 360 - Automatizar marcação de fulfillment em pedidos Shopify

- **Nome:** Automatizar marcação de fulfillment em pedidos Shopify
- **Descrição:** Fluxo que localiza pedidos não cumpridos, verifica pedidos com mais de 24 horas e cria fulfillments automaticamente usando os identificadores de fulfillment orders do Shopify.
- **Funcionalidade:** • Disparo agendado: Executa o processo em intervalos regulares para verificar novos pedidos pendentes.
• Configuração de loja: Define o identificador da loja a ser usado nas chamadas à API.
• Recuperação de pedidos não cumpridos: Consulta a loja para obter todos os pedidos com status de fulfillment "unfulfilled".
• Filtragem por idade do pedido: Seleciona apenas pedidos com mais de 24 horas desde a criação.
• Processamento em lote/iterativo: Percorre cada pedido filtrado para tratar individualmente.
• Recuperação de fulfillment orders: Solicita a lista de fulfillment orders de cada pedido para obter o ID necessário.
• Criação de fulfillment: Envia uma requisição para marcar o fulfillment order como cumprido e notificar o cliente.
- **Ferramentas:** • Shopify Admin API: Usada para listar pedidos, recuperar fulfillment orders de um pedido e criar fulfillments via endpoints REST (autenticação por access token).

## Fluxo visual

```mermaid
flowchart LR
    N1["When clicking ‘Test workflow’"]
    N2["Sticky Note"]
    N3["Loop Over Items"]
    N4["Sticky Note1"]
    N5["Schedule Trigger"]
    N6["Filter Orders"]
    N7["Get Fulfillment Orders"]
    N8["Sticky Note2"]
    N9["Set Global"]
    N10["Sticky Note4"]
    N11["Sticky Note5"]
    N12["Get all Unfulfilled orders"]
    N13["Mark fulfillment orders as fulfilled"]

    N9 --> N12
    N6 --> N3
    N3 --> N7
    N5 --> N9
    N7 --> N13
    N12 --> N6
    N1 --> N9
    N13 --> N3
```

## Fluxo (.json) :

```json
{
  "meta": {
    "instanceId": "e634e668fe1fc93a75c4f2a7fc0dad807ca318b79654157eadb9578496acbc76",
    "templateCredsSetupCompleted": true
  },
  "nodes": [
    {
      "id": "30da4d86-83ef-4226-ad2e-d73f531bd4ed",
      "name": "When clicking ‘Test workflow’",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        0,
        100
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "bd57625d-03f2-48b3-94b5-2653214682eb",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        700,
        -280
      ],
      "parameters": {
        "height": 440,
        "content": "## Filtering orders for fulfillment 👇\nFilter the valid orders for programatically fulfillments\n\n- you exclusively sell digital downloads or digital gift cards\n- you use fulfillment services for all your products\n"
      },
      "typeVersion": 1
    },
    {
      "id": "5928c16f-b842-42e3-9c81-ac9b796d22ff",
      "name": "Loop Over Items",
      "type": "n8n-nodes-base.splitInBatches",
      "position": [
        1060,
        0
      ],
      "parameters": {
        "options": {}
      },
      "typeVersion": 3
    },
    {
      "id": "4509fb4e-fed0-4424-94a2-55d1c56a5d5a",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1320,
        -180
      ],
      "parameters": {
        "height": 340,
        "content": "## Get fulfillment orders 👇\n[Retrieves a list of fulfillment orders for a specific order.](https://shopify.dev/docs/api/admin-rest/2025-01/resources/fulfillmentorder#get-orders-order-id-fulfillment-orders)\n\n\n"
      },
      "typeVersion": 1
    },
    {
      "id": "76e16b42-01a3-4c88-a64b-a408b4bb9f40",
      "name": "Schedule Trigger",
      "type": "n8n-nodes-base.scheduleTrigger",
      "position": [
        0,
        -160
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
      "id": "1835c0d1-c7d3-4db6-b898-d604c8df7ad1",
      "name": "Filter Orders",
      "type": "n8n-nodes-base.filter",
      "position": [
        760,
        0
      ],
      "parameters": {
        "options": {},
        "conditions": {
          "options": {
            "version": 2,
            "leftValue": "",
            "caseSensitive": true,
            "typeValidation": "loose"
          },
          "combinator": "and",
          "conditions": [
            {
              "id": "3fdde26b-82ef-42f1-ba36-d4fe667f8866",
              "operator": {
                "type": "number",
                "operation": "gt"
              },
              "leftValue": "={{ (new Date().getTime() - new Date($json.created_at).getTime()) / (1000 * 60 * 60) }}\n",
              "rightValue": 24
            }
          ]
        },
        "looseTypeValidation": true
      },
      "typeVersion": 2.2
    },
    {
      "id": "977c3b8d-e3a9-4146-bc4c-e06e67f26a9e",
      "name": "Get Fulfillment Orders",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1380,
        20
      ],
      "parameters": {
        "url": "=https://{{ $('Set Global').item.json['store-id'] }}.myshopify.com/admin/api/2025-01/orders/{{ $json.id }}/fulfillment_orders.json",
        "options": {},
        "authentication": "predefinedCredentialType",
        "nodeCredentialType": "shopifyAccessTokenApi"
      },
      "credentials": {
        "shopifyAccessTokenApi": {
          "id": "vtyKGPLLdjc7MLea",
          "name": "Shopify Access Token account"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "cf4c99c4-882c-4706-9cb9-8c154549545b",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        240,
        -180
      ],
      "parameters": {
        "width": 232,
        "height": 346,
        "content": "## Edit this node 👇\n\nGet your store ID and replace in the GET url"
      },
      "typeVersion": 1
    },
    {
      "id": "3a33e89b-ecf5-4be1-b3e4-9c20c00c7c1c",
      "name": "Set Global",
      "type": "n8n-nodes-base.set",
      "position": [
        300,
        0
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "78289fb1-8a1a-46a2-973e-f5f2a7309993",
              "name": "store-id",
              "type": "string",
              "value": "{store-id}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "68dffeba-705c-42b5-851e-893964a51176",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1680,
        -180
      ],
      "parameters": {
        "width": 232,
        "height": 346,
        "content": "## Create fulfillment  👇\n\n[Creates a fulfillment for one or many fulfillment orders](https://shopify.dev/docs/api/admin-rest/2025-04/resources/fulfillment#post-fulfillments)\n- `notify_customer` to send notifications to customer"
      },
      "typeVersion": 1
    },
    {
      "id": "24137672-00d7-4fa0-9238-f2dca7900adf",
      "name": "Sticky Note5",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -440,
        -300
      ],
      "parameters": {
        "width": 372,
        "height": 546,
        "content": "## Shopify Fulfillment Automation with n8n\nShopify store owners who want to automate the fulfillment process, whether for entire orders or specific products (like personalization items). However, the challenge lies in retrieving the [Fulfillment Order ID](https://shopify.dev/docs/api/admin-rest/2025-01/resources/fulfillmentorder#get-orders-order-id-fulfillment-orders) (not [Order ID](https://shopify.dev/docs/api/admin-rest/2025-01/resources/order#get-orders-order-id?fields=id,line-items,name,total-price))—a crucial piece needed to trigger fulfillment.\n\nThis n8n workflow can:\n\n- Get all unfulfilled orders from Shopify store.\n\n- Retrieve the Fulfillment Order ID (using the \"List Fulfillment Orders\" action).\n\n- Create a fulfillment request (using \"Mark fulfillment orders as fulfilled\").\n\n- Handle edge cases, like partially fulfilled orders or errors in API responses.\n\n"
      },
      "typeVersion": 1
    },
    {
      "id": "bfb340f2-1fb6-4be7-823a-d24d6d8361be",
      "name": "Get all Unfulfilled orders",
      "type": "n8n-nodes-base.shopify",
      "position": [
        540,
        0
      ],
      "parameters": {
        "options": {
          "fulfillmentStatus": "unfulfilled"
        },
        "operation": "getAll",
        "returnAll": true,
        "authentication": "accessToken"
      },
      "credentials": {
        "shopifyAccessTokenApi": {
          "id": "vtyKGPLLdjc7MLea",
          "name": "Shopify Access Token account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "8350fcaf-1bf8-4af1-a716-816b19a4b892",
      "name": "Mark fulfillment orders as fulfilled",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1740,
        20
      ],
      "parameters": {
        "url": "=https://{{ $('Set Global').item.json['store-id'] }}.myshopify.com/admin/api/2025-01/fulfillments.json",
        "method": "POST",
        "options": {},
        "jsonBody": "={\"fulfillment\":{\"line_items_by_fulfillment_order\":[{\"fulfillment_order_id\":{{ $json.fulfillment_orders[0].id }}}],\"notify_customer\":true}}",
        "sendBody": true,
        "specifyBody": "json",
        "authentication": "predefinedCredentialType",
        "nodeCredentialType": "shopifyAccessTokenApi"
      },
      "credentials": {
        "shopifyAccessTokenApi": {
          "id": "vtyKGPLLdjc7MLea",
          "name": "Shopify Access Token account"
        }
      },
      "typeVersion": 4.2
    }
  ],
  "pinData": {},
  "connections": {
    "Set Global": {
      "main": [
        [
          {
            "node": "Get all Unfulfilled orders",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Filter Orders": {
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
    "Loop Over Items": {
      "main": [
        [],
        [
          {
            "node": "Get Fulfillment Orders",
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
            "node": "Set Global",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Fulfillment Orders": {
      "main": [
        [
          {
            "node": "Mark fulfillment orders as fulfilled",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get all Unfulfilled orders": {
      "main": [
        [
          {
            "node": "Filter Orders",
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
            "node": "Set Global",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Mark fulfillment orders as fulfilled": {
      "main": [
        [
          {
            "node": "Loop Over Items",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-361"></a>

## Template 361 - Extrair e consolidar listas de pessoas

- **Nome:** Extrair e consolidar listas de pessoas
- **Descrição:** O fluxo pesquisa listas na web sobre um determinado grupo de pessoas em um local, extrai os nomes e identificadores, remove duplicados e adiciona os resultados a uma planilha.
- **Funcionalidade:** • Início manual: executa o fluxo manualmente para testar ou rodar sob demanda.
• Definição de parâmetros: recebe termos 'who' e 'where' para direcionar a busca (ex.: "Top \"Build in Public\" influencers" em X).
• Pesquisa na web e extração de links: realiza uma busca (Google) e retorna até 10 resultados não patrocinados com título e URL.
• Formatação dos resultados: transforma a resposta da busca em uma lista de URLs para processamento posterior.
• Extração de pessoas por página: para cada URL, extrai até 20 itens com nome, identificador (handle/ID) e URL.
• Limpeza e deduplicação: filtra itens sem nome, remove parâmetros das URLs e elimina entradas duplicadas por URL.
• Inserção em planilha: adiciona cada item único em uma planilha com colunas (Who?, Where?, Name, ID or Handle, URL, Added on).
- **Ferramentas:** • Airtop: serviço de extração/IA usado para analisar páginas e transformar conteúdo em dados estruturados conforme esquemas definidos.
• Google Search: motor de busca usado como fonte inicial de resultados (pesquisa do tipo 'who on where').
• Google Sheets: planilha online utilizada para armazenar e organizar os resultados finais.

## Fluxo visual

```mermaid
flowchart LR
    A[When clicking 'Test workflow'] --> B[Parameters]
    B --> C[Get urls]
    C --> D[Format results]
    D --> E[Get people]
    E --> F[Dedupe results]
    F --> G[Add to spreadsheet]

    classDef trigger fill:#e8f5e9,stroke:#2e7d32,color:#1b5e20;
    classDef transform fill:#fff8e1,stroke:#f9a825,color:#5d4037;
    classDef action fill:#e3f2fd,stroke:#1565c0,color:#0d47a1;

    class A trigger;
    class B,D,F transform;
    class C,E,G action;
```

## Fluxo (.json) :

```json
{
  "id": "VwU1zMhcgzgPS9ak",
  "meta": {
    "instanceId": "660cf2c29eb19fa42319afac3bd2a4a74c6354b7c006403f6cba388968b63f5d",
    "templateCredsSetupCompleted": true
  },
  "name": "List Builder",
  "tags": [
    {
      "id": "a8B9vqj0vNLXcKVQ",
      "name": "template",
      "createdAt": "2025-04-04T15:38:37.785Z",
      "updatedAt": "2025-04-04T15:38:37.785Z"
    }
  ],
  "nodes": [
    {
      "id": "1a6aa574-467d-40b0-a9a5-a5537bede3de",
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
      "id": "62db9366-7e6f-4346-9de8-9fa730d059ed",
      "name": "Format results",
      "type": "n8n-nodes-base.code",
      "position": [
        660,
        0
      ],
      "parameters": {
        "jsCode": "// Get first input item\nconst input = $input.first().json.data.modelResponse\n// Parse list of links\nconst listOfLinks = JSON.parse(input).results\n// Format node's output\nconst output = listOfLinks.map((item) => ({\n  json: { url: item.url }\n}))\n\nreturn output;"
      },
      "typeVersion": 2
    },
    {
      "id": "fa960de3-8dd6-40a3-aa59-634ad250f5d1",
      "name": "Get urls",
      "type": "n8n-nodes-base.airtop",
      "position": [
        440,
        0
      ],
      "parameters": {
        "url": "=https://www.google.com/search?q={{ encodeURI($json.who+' on ' + $json.where) }}",
        "prompt": "=Those are search results, return up to 10 non-sponsored results that lead to a web page with a list of {{$json.who}} on {{$json.where}}. For each return the title and URL.",
        "resource": "extraction",
        "operation": "query",
        "sessionMode": "new",
        "additionalFields": {
          "outputSchema": "{  \"type\": \"object\",  \"properties\": {    \"results\": {      \"type\": \"array\",      \"items\": {        \"type\": \"object\",        \"properties\": {          \"title\": {            \"type\": \"string\",            \"description\": \"The title of the search result.\"          },          \"url\": {            \"type\": \"string\",            \"description\": \"The URL of the webpage.\"          }        },        \"required\": [          \"title\",          \"url\"        ],        \"additionalProperties\": false      },      \"description\": \"A list of up to 10 non-sponsored search results.\"    }  },  \"required\": [    \"results\"  ],  \"additionalProperties\": false,  \"$schema\": \"http://json-schema.org/draft-07/schema#\"}"
        }
      },
      "credentials": {
        "airtopApi": {
          "id": "byhouJF8RLH5DkmY",
          "name": "Airtop"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "d75dbdce-7a7e-4a30-81b0-6e8fa5221f55",
      "name": "Get people",
      "type": "n8n-nodes-base.airtop",
      "position": [
        880,
        0
      ],
      "parameters": {
        "url": "={{ $json.url }}",
        "prompt": "=This is a list of {{ $('Parameters').item.json.who }} on {{ $('Parameters').item.json.where }}.\nExtract up to 20 items. For each person extract: \n- name \n- handle or ID \n- URL",
        "resource": "extraction",
        "operation": "query",
        "sessionMode": "new",
        "additionalFields": {
          "outputSchema": "{\n  \"$schema\": \"http://json-schema.org/draft-07/schema#\",\n  \"type\": \"object\",\n  \"properties\": {\n    \"items\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the item.\"\n          },\n          \"identifier\": {\n            \"type\": \"string\",\n            \"description\": \"The unique identifier or handle for the item.\"\n          },\n          \"url\": {\n            \"type\": \"string\",\n            \"description\": \"The URL to access the item or its related resource.\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"identifier\",\n          \"url\"\n        ],\n        \"additionalProperties\": false\n      }\n    }\n  },\n  \"required\": [\n    \"items\"\n  ],\n  \"additionalProperties\": false\n}"
        }
      },
      "credentials": {
        "airtopApi": {
          "id": "byhouJF8RLH5DkmY",
          "name": "Airtop"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "285ce6af-bda8-4025-872e-f5f8c4a56b3c",
      "name": "Dedupe results",
      "type": "n8n-nodes-base.code",
      "position": [
        1100,
        0
      ],
      "parameters": {
        "jsCode": "const allResults = []\n\nfor (const inputItem of $input.all()) {\n  // Parse input to JSON\n  const input = inputItem.json.data.modelResponse\n  const results = JSON.parse(input).items\n  // clean results\n  const cleanedResults = results\n    .filter((res) => res.name) // only those with name\n    .map((res) => ({\n      ...res,\n      url: res.url.split('?')[0] // clean url\n    }))\n  // add results to list\n  allResults.push(...cleanedResults)\n}\n\n// Dedupe urls\nconst uniqueList = allResults.filter((item, index, self) =>\n  index === self.findIndex((t) => (t.url === item.url))\n);\n\nreturn uniqueList.map((item) => ({\n  json: {...item}\n}));"
      },
      "typeVersion": 2
    },
    {
      "id": "fdc86d5c-4df3-48b9-9cf6-a5ddc3b45c90",
      "name": "Add to spreadsheet",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        1320,
        0
      ],
      "parameters": {
        "columns": {
          "value": {
            "URL": "={{ $json.url }}",
            "Name": "={{ $json.name }}",
            "Who?": "={{ $('Parameters').first().json.who }}",
            "Where?": "={{ $('Parameters').first().json.where }}",
            "Added on": "={{ $now }}",
            "ID or Handle": "={{ $json.identifier }}"
          },
          "schema": [
            {
              "id": "Who?",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Who?",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Where?",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Where?",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Name",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Name",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "ID or Handle",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "ID or Handle",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "URL",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "URL",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Added on",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Added on",
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
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/150eh4t5GyEBN_TcO5TDeNWpE2GzHR4hQWoNRbUpw7A0/edit#gid=0",
          "cachedResultName": "Sheet1"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "150eh4t5GyEBN_TcO5TDeNWpE2GzHR4hQWoNRbUpw7A0",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/150eh4t5GyEBN_TcO5TDeNWpE2GzHR4hQWoNRbUpw7A0/edit?usp=drivesdk",
          "cachedResultName": "List Builder"
        }
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "CwpCAR1HwgHZpRtJ",
          "name": "Google Drive"
        }
      },
      "typeVersion": 4.5
    },
    {
      "id": "44c54497-741c-4c48-b4f9-0c5c836d10ad",
      "name": "Parameters",
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
              "id": "bc2d3cb9-b7d0-4c3f-b392-53262d60441e",
              "name": "who",
              "type": "string",
              "value": "Top \"Build in Public\" influencers"
            },
            {
              "id": "b2cfa361-c80a-4945-bc0e-23eac5edebd6",
              "name": "where",
              "type": "string",
              "value": "X"
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
  "versionId": "a2572aec-54cb-4bbb-b503-09d1d0beb64f",
  "connections": {
    "Get urls": {
      "main": [
        [
          {
            "node": "Format results",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get people": {
      "main": [
        [
          {
            "node": "Dedupe results",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Parameters": {
      "main": [
        [
          {
            "node": "Get urls",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Dedupe results": {
      "main": [
        [
          {
            "node": "Add to spreadsheet",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Format results": {
      "main": [
        [
          {
            "node": "Get people",
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
            "node": "Parameters",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
