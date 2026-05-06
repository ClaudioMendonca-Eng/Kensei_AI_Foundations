# PACK 1999 TEMPLATES PARTE 10 - Bloco 4

Templates neste bloco: 20

## Sumário

- [Template 2388 - Treinamento personalizado de modelo OpenAI](#template-2388)
- [Template 2391 - Chat com arquivo e citações](#template-2391)
- [Template 2392 - Criar, atualizar e obter perfil Humantic AI](#template-2392)
- [Template 2394 - Cadeia LLM e agente com ferramenta](#template-2394)
- [Template 2396 - Repetição de tentativa com exclusão de erro conhecido](#template-2396)
- [Template 2399 - Extração e resumo de SERP com Bright Data](#template-2399)
- [Template 2401 - Embeddings de imagem (cores + keywords)](#template-2401)
- [Template 2403 - Teste A/B de prompts para agente de chat](#template-2403)
- [Template 2405 - Resposta automática a pedidos de agendamento](#template-2405)
- [Template 2407 - Mensagens de boas-vindas e despedida no Telegram](#template-2407)
- [Template 2408 - Rascunhos automáticos de resposta por IA](#template-2408)
- [Template 2410 - Exportar objetos Zammad para Excel](#template-2410)
- [Template 2412 - Exportar tickets do Linear para Google Sheets](#template-2412)
- [Template 2414 - Servidor MCP para busca e leitura de arquivos no Google Drive](#template-2414)
- [Template 2415 - Sincronizar planilha de livros semanalmente](#template-2415)
- [Template 2416 - Detecção e resposta a stickers do Telegram](#template-2416)
- [Template 2417 - Exportar planilha Google para HTML via webhook](#template-2417)
- [Template 2420 - Responder webhook de chamada Retell com variáveis dinâmicas](#template-2420)
- [Template 2422 - Salvar anexos do Gmail em pastas por empresa e mês no Drive](#template-2422)
- [Template 2424 - Criação diária de playlist AI News](#template-2424)

---

<a id="template-2388"></a>

## Template 2388 - Treinamento personalizado de modelo OpenAI

- **Nome:** Treinamento personalizado de modelo OpenAI
- **Descrição:** Este fluxo automatiza o download de um arquivo de treinamento, envia-o ao OpenAI para fine-tuning, cria o job de treinamento e utiliza o modelo resultante para responder mensagens de chat.
- **Funcionalidade:** • Início manual para testes: permite acionar o fluxo manualmente para testar o processo.
• Download do arquivo de treinamento: localiza e baixa um arquivo .jsonl hospedado no Google Drive (com opção de conversão de formatos quando aplicável).
• Upload do arquivo para treinamento: envia o arquivo baixado para a plataforma de treinamento com o propósito definido de fine-tune.
• Criação do job de fine-tuning via API: solicita a criação de um job de treinamento apontando para o arquivo carregado e definindo o modelo base a ser ajustado.
• Uso do modelo fine-tunado em chat: recebe mensagens via webhook e responde utilizando o modelo customizado gerado pelo fine-tuning.
• Documentação embutida: inclui notas com instruções sobre o formato do arquivo .jsonl e o fluxo do processo.
- **Ferramentas:** • Google Drive: armazena e fornece o arquivo de treinamento (.jsonl) e permite conversão/extração do conteúdo para download.
• OpenAI: serviço para receber o arquivo, executar o fine-tuning (criar jobs) e disponibilizar o modelo customizado para uso em chat.

## Fluxo visual

```mermaid
flowchart LR
    N1["When clicking ‘Test workflow’"]
    N2["Google Drive"]
    N3["AI Agent"]
    N4["When chat message received"]
    N5["OpenAI Chat Model"]
    N6["Sticky Note1"]
    N7["Sticky Note2"]
    N8["Upload File"]
    N9["Create Fine-tuning Job"]

    N8 --> N9
    N2 --> N8
    N4 --> N3
    N1 --> N2
```

## Fluxo (.json) :

```json
{
  "id": "gAzsjTGbfWuvAObi",
  "meta": {
    "instanceId": "a4bfc93e975ca233ac45ed7c9227d84cf5a2329310525917adaf3312e10d5462",
    "templateCredsSetupCompleted": true
  },
  "name": "Fine-tuning with OpenAI models",
  "tags": [
    {
      "id": "2VG6RbmUdJ2VZbrj",
      "name": "Google Drive",
      "createdAt": "2024-12-04T16:50:56.177Z",
      "updatedAt": "2024-12-04T16:50:56.177Z"
    },
    {
      "id": "paTcf5QZDJsC2vKY",
      "name": "OpenAI",
      "createdAt": "2024-12-04T16:52:10.768Z",
      "updatedAt": "2024-12-04T16:52:10.768Z"
    }
  ],
  "nodes": [
    {
      "id": "ff65c2db-6a94-4e56-a10c-2538c9617df6",
      "name": "When clicking ‘Test workflow’",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        220,
        320
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "208fc618-0543-4552-bd65-9c808c879d88",
      "name": "Google Drive",
      "type": "n8n-nodes-base.googleDrive",
      "position": [
        440,
        320
      ],
      "parameters": {
        "fileId": {
          "__rl": true,
          "mode": "list",
          "value": "1wvlEcbxFIENvqL-bACzlLEfy5gA6uF9J",
          "cachedResultUrl": "https://drive.google.com/file/d/1wvlEcbxFIENvqL-bACzlLEfy5gA6uF9J/view?usp=drivesdk",
          "cachedResultName": "test_fine_tuning.jsonl"
        },
        "options": {
          "binaryPropertyName": "data.jsonl",
          "googleFileConversion": {
            "conversion": {
              "docsToFormat": "application/pdf"
            }
          }
        },
        "operation": "download"
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
      "id": "3580d925-c8c9-446f-bfa4-faae5ed3f44a",
      "name": "AI Agent",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        500,
        800
      ],
      "parameters": {
        "options": {}
      },
      "typeVersion": 1.7
    },
    {
      "id": "d309da46-c44e-47b7-bb46-5ee6fe7e6964",
      "name": "When chat message received",
      "type": "@n8n/n8n-nodes-langchain.chatTrigger",
      "position": [
        220,
        800
      ],
      "webhookId": "88151d03-e7f5-4c9a-8190-7cff8e849ca2",
      "parameters": {
        "options": {}
      },
      "typeVersion": 1.1
    },
    {
      "id": "84b896f7-d1dd-4485-a088-3c7f8154a406",
      "name": "OpenAI Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        380,
        1000
      ],
      "parameters": {
        "model": "ft:gpt-4o-mini-2024-07-18:n3w-italia::AsVfsl7B",
        "options": {}
      },
      "credentials": {
        "openAiApi": {
          "id": "CDX6QM4gLYanh0P4",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "3bff93e4-70c3-48c7-b0b3-d2a9881689c4",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        220,
        560
      ],
      "parameters": {
        "width": 556.5145228215765,
        "height": 211.35269709543567,
        "content": "# Step 2\n\nOnce the .jsonl file for training is uploaded (See the entire process here.: https://platform.openai.com/finetune/), a \"new model\" will be created and made available via your API. OpenAI will automatically train it based on the uploaded .jsonl file. If the training is successful, the new model will be accessible via API.\n\neg. ft:gpt-4o-mini-2024-07-18:n3w-italia::XXXXX7B"
      },
      "typeVersion": 1
    },
    {
      "id": "ea67edd7-986d-47cd-bc1a-5df49851e27b",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        220,
        -5.676348547717737
      ],
      "parameters": {
        "width": 777.3941908713687,
        "height": 265.161825726141,
        "content": "# Step 1\n\nCreate the training file .jsonl with the following syntax and upload it to Drive.\n\n{\"messages\": [{\"role\": \"system\", \"content\": \"You are an experienced and helpful travel assistant.\"}, {\"role\": \"user\", \"content\": \"What documents are needed to travel to the United States?\"}, {\"role\": \"assistant\", \"content\": \"To travel to the United States, you will need a valid passport and an ESTA authorization, which you can apply for online. Make sure to check the specific requirements based on your nationality.\"}]}\n....\n\nThe file will be uploaded here: https://platform.openai.com/storage/files\n\n"
      },
      "typeVersion": 1
    },
    {
      "id": "87df3b85-01ac-41db-b5b6-a236871fa4e2",
      "name": "Upload File",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "position": [
        660,
        320
      ],
      "parameters": {
        "options": {
          "purpose": "fine-tune"
        },
        "resource": "file",
        "binaryPropertyName": "data.jsonl"
      },
      "credentials": {
        "openAiApi": {
          "id": "CDX6QM4gLYanh0P4",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1.8
    },
    {
      "id": "c8ec10d4-ff83-461f-94ac-45b68d298276",
      "name": "Create Fine-tuning Job",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        900,
        320
      ],
      "parameters": {
        "url": "https://api.openai.com/v1/fine_tuning/jobs",
        "method": "POST",
        "options": {},
        "jsonBody": "={\n \"training_file\": \"{{ $json.id }}\",\n \"model\": \"gpt-4o-mini-2024-07-18\"\n} ",
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
            }
          ]
        }
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "0WeSLPyZXOxqMuzn",
          "name": "OpenAI API"
        }
      },
      "typeVersion": 4.2
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "a4aa95f5-132b-4aa3-a7f5-3bb316e00133",
  "connections": {
    "Upload File": {
      "main": [
        [
          {
            "node": "Create Fine-tuning Job",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Drive": {
      "main": [
        [
          {
            "node": "Upload File",
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
    "When clicking ‘Test workflow’": {
      "main": [
        [
          {
            "node": "Google Drive",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2391"></a>

## Template 2391 - Chat com arquivo e citações

- **Nome:** Chat com arquivo e citações
- **Descrição:** Baixa um arquivo do Google Drive, gera embeddings com OpenAI, armazena vetores em Pinecone e responde perguntas usando os trechos mais relevantes com citações.
- **Funcionalidade:** • Baixar arquivo: Baixa um arquivo a partir de um URL do Google Drive e adiciona metadados como nome, extensão e URL.
• Dividir texto em trechos: Segmenta o conteúdo em chunks com sobreposição configurada para preservar contexto.
• Gerar embeddings: Cria vetores de embeddings usando o serviço de embeddings para representar semanticamente os trechos.
• Inserir no banco vetorial: Insere os embeddings e metadados em um índice no banco vetorial para busca semântica.
• Disparador de chat: Recebe consultas via webhook e define o número máximo de trechos a recuperar.
• Recuperar trechos relevantes: Consulta o índice vetorial para obter os top-K trechos mais relevantes para a pergunta.
• Preparar contexto: Concatena os trechos recuperados em um contexto que será enviado ao modelo de linguagem.
• Responder com citações: Gera a resposta com o modelo de linguagem, extrai os índices dos trechos usados e formata citações legíveis.
- **Ferramentas:** • Google Drive: Armazenamento e fornecimento do arquivo a ser indexado (download a partir de um link).
• OpenAI: Geração de embeddings e uso do modelo de linguagem para produzir respostas baseadas no contexto.
• Pinecone: Banco de vetores para inserir, indexar e consultar embeddings, permitindo recuperação semântica.

## Fluxo visual

```mermaid
flowchart LR
    N1["When clicking 'Execute Workflow'"]
    N2["Embeddings OpenAI"]
    N3["Sticky Note"]
    N4["Default Data Loader"]
    N5["Set file URL in Google Drive"]
    N6["Sticky Note2"]
    N7["Add in metadata"]
    N8["Download file"]
    N9["Chat Trigger"]
    N10["Prepare chunks"]
    N11["Embeddings OpenAI2"]
    N12["OpenAI Chat Model"]
    N13["Set max chunks to send to model"]
    N14["Structured Output Parser"]
    N15["Compose citations"]
    N16["Generate response"]
    N17["Sticky Note1"]
    N18["Answer the query based on chunks"]
    N19["Sticky Note4"]
    N20["Get top chunks matching query"]
    N21["Add to Pinecone vector store"]
    N22["Recursive Character Text Splitter"]

    N9 --> N13
    N8 --> N7
    N10 --> N18
    N7 --> N21
    N15 --> N16
    N5 --> N8
    N20 --> N10
    N13 --> N20
    N18 --> N15
    N1 --> N5
```

## Fluxo (.json) :

```json
{
  "meta": {
    "instanceId": "cb484ba7b742928a2048bf8829668bed5b5ad9787579adea888f05980292a4a7",
    "templateId": "1960"
  },
  "nodes": [
    {
      "id": "296a935f-bd02-44bc-9e1e-3e4d6a307e38",
      "name": "When clicking \"Execute Workflow\"",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        260,
        240
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "61a38c00-f196-4b01-9274-c5e0f4c511bc",
      "name": "Embeddings OpenAI",
      "type": "@n8n/n8n-nodes-langchain.embeddingsOpenAi",
      "position": [
        1060,
        460
      ],
      "parameters": {
        "options": {}
      },
      "credentials": {
        "openAiApi": {
          "id": "VQtv7frm7eLiEDnd",
          "name": "OpenAi account 7"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "816066bd-02e8-4de2-bcee-ab81d890435a",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        426.9261940355327,
        60.389291053299075
      ],
      "parameters": {
        "color": 7,
        "width": 1086.039382705461,
        "height": 728.4168721167887,
        "content": "## 1. Setup: Fetch file from Google Drive, split it into chunks and insert into a vector database\nNote that running this part multiple times will insert multiple copies into your DB"
      },
      "typeVersion": 1
    },
    {
      "id": "30cd81ad-d658-4c33-9a38-68e33b74cdae",
      "name": "Default Data Loader",
      "type": "@n8n/n8n-nodes-langchain.documentDefaultDataLoader",
      "position": [
        1240,
        460
      ],
      "parameters": {
        "options": {
          "metadata": {
            "metadataValues": [
              {
                "name": "file_url",
                "value": "={{ $json.file_url }}"
              },
              {
                "name": "file_name",
                "value": "={{ $('Add in metadata').item.json.file_name }}"
              }
            ]
          }
        },
        "dataType": "binary"
      },
      "typeVersion": 1
    },
    {
      "id": "718f09e0-67be-41a6-a90d-f58e64ffee4d",
      "name": "Set file URL in Google Drive",
      "type": "n8n-nodes-base.set",
      "position": [
        480,
        240
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "50025ff5-1b53-475f-b150-2aafef1c4c21",
              "name": "file_url",
              "type": "string",
              "value": " https://drive.google.com/file/d/11Koq9q53nkk0F5Y8eZgaWJUVR03I4-MM/view"
            }
          ]
        }
      },
      "typeVersion": 3.3
    },
    {
      "id": "8f536a96-a6b1-4291-9cac-765759c396a8",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -40,
        140
      ],
      "parameters": {
        "height": 350.7942096493649,
        "content": "# Try me out\n1. In Pinecone, create an index with 1536 dimensions and select it in the two vector store nodes\n2. Populate Pinecone by clicking the 'test workflow' button below\n3. Click the 'chat' button below and enter the following:\n\n_Which email provider does the creator of Bitcoin use?_"
      },
      "typeVersion": 1
    },
    {
      "id": "ec7c9407-93c3-47a6-90f2-6e6056f5af84",
      "name": "Add in metadata",
      "type": "n8n-nodes-base.code",
      "position": [
        900,
        240
      ],
      "parameters": {
        "mode": "runOnceForEachItem",
        "jsCode": "// Add a new field called 'myNewField' to the JSON of the item\n$input.item.json.file_name = $input.item.binary.data.fileName;\n$input.item.json.file_ext = $input.item.binary.data.fileExtension;\n$input.item.json.file_url = $('Set file URL in Google Drive').item.json.file_url\n\nreturn $input.item;"
      },
      "typeVersion": 2
    },
    {
      "id": "ab3131d5-4b04-48b4-b5d5-787e3ed18917",
      "name": "Download file",
      "type": "n8n-nodes-base.googleDrive",
      "position": [
        680,
        240
      ],
      "parameters": {
        "fileId": {
          "__rl": true,
          "mode": "url",
          "value": "={{ $json.file_url }}"
        },
        "options": {},
        "operation": "download"
      },
      "credentials": {
        "googleDriveOAuth2Api": {
          "id": "176",
          "name": "Google Drive account (David)"
        }
      },
      "typeVersion": 3
    },
    {
      "id": "764a865c-7efe-4eec-a34c-cc87c5f085b1",
      "name": "Chat Trigger",
      "type": "@n8n/n8n-nodes-langchain.chatTrigger",
      "position": [
        260,
        960
      ],
      "webhookId": "1727c687-aed0-49cf-96af-e7796819fbb3",
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "36cd9a8d-7d89-49b3-8a81-baa278201a21",
      "name": "Prepare chunks",
      "type": "n8n-nodes-base.code",
      "position": [
        1080,
        960
      ],
      "parameters": {
        "jsCode": "let out = \"\"\nfor (const i in $input.all()) {\n let itemText = \"--- CHUNK \" + i + \" ---\\n\"\n itemText += $input.all()[i].json.document.pageContent + \"\\n\"\n itemText += \"\\n\"\n out += itemText\n}\n\nreturn {\n 'context': out\n};"
      },
      "typeVersion": 2
    },
    {
      "id": "6356bce2-9aae-43ed-97ce-a27cbfb80df9",
      "name": "Embeddings OpenAI2",
      "type": "@n8n/n8n-nodes-langchain.embeddingsOpenAi",
      "position": [
        700,
        1180
      ],
      "parameters": {
        "options": {}
      },
      "credentials": {
        "openAiApi": {
          "id": "VQtv7frm7eLiEDnd",
          "name": "OpenAi account 7"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "8fb697ea-f2e5-4105-b6c8-ab869c2e5ab2",
      "name": "OpenAI Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        1320,
        1180
      ],
      "parameters": {
        "options": {}
      },
      "credentials": {
        "openAiApi": {
          "id": "VQtv7frm7eLiEDnd",
          "name": "OpenAi account 7"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "9a2b0152-d008-42cb-bc10-495135d5ef45",
      "name": "Set max chunks to send to model",
      "type": "n8n-nodes-base.set",
      "position": [
        480,
        960
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "236047ff-75a2-47fd-b338-1e9763c4015e",
              "name": "chunks",
              "type": "number",
              "value": 4
            }
          ]
        },
        "includeOtherFields": true
      },
      "typeVersion": 3.3
    },
    {
      "id": "f2ab813f-0f0c-4d3a-a1de-7896ad736698",
      "name": "Structured Output Parser",
      "type": "@n8n/n8n-nodes-langchain.outputParserStructured",
      "position": [
        1500,
        1180
      ],
      "parameters": {
        "jsonSchema": "{\n \"type\": \"object\",\n \"properties\": {\n \"answer\": {\n \"type\": \"string\"\n },\n \"citations\": {\n \"type\": \"array\",\n \"items\": {\n \"type\": \"number\"\n }\n }\n }\n}"
      },
      "typeVersion": 1
    },
    {
      "id": "ada2a38b-0f6e-4115-97c0-000e97a5e62e",
      "name": "Compose citations",
      "type": "n8n-nodes-base.set",
      "position": [
        1680,
        960
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "67ecefcf-a30c-4cc4-89ca-b9b23edd6585",
              "name": "citations",
              "type": "array",
              "value": "={{ $json.citations.map(i => '[' + $('Get top chunks matching query').all()[$json.citations].json.document.metadata.file_name + ', lines ' + $('Get top chunks matching query').all()[$json.citations].json.document.metadata['loc.lines.from'] + '-' + $('Get top chunks matching query').all()[$json.citations].json.document.metadata['loc.lines.to'] + ']') }}"
            }
          ]
        },
        "includeOtherFields": true
      },
      "typeVersion": 3.3
    },
    {
      "id": "8e115308-532e-4afd-b766-78e54c861f33",
      "name": "Generate response",
      "type": "n8n-nodes-base.set",
      "position": [
        1900,
        960
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "d77956c4-0ff4-4c64-80c2-9da9d4c8ad34",
              "name": "text",
              "type": "string",
              "value": "={{ $json.answer }} {{ $if(!$json.citations.isEmpty(), \"\\n\" + $json.citations.join(\"\"), '') }}"
            }
          ]
        }
      },
      "typeVersion": 3.3
    },
    {
      "id": "40c5f9d8-38da-41ac-ab99-98f6010ba8bf",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        428.71587064297796,
        840
      ],
      "parameters": {
        "color": 7,
        "width": 1693.989843925635,
        "height": 548.5086735412393,
        "content": "## 2. Chat with file, getting citations in reponse"
      },
      "typeVersion": 1
    },
    {
      "id": "ef357a2b-bc8d-43f7-982f-73c3a85a60be",
      "name": "Answer the query based on chunks",
      "type": "@n8n/n8n-nodes-langchain.chainLlm",
      "position": [
        1300,
        960
      ],
      "parameters": {
        "text": "=Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer. Important: In your response, also include the the indexes of the chunks you used to generate the answer.\n\n{{ $json.context }}\n\nQuestion: {{ $(\"Chat Trigger\").first().json.chatInput }}\nHelpful Answer:",
        "promptType": "define",
        "hasOutputParser": true
      },
      "typeVersion": 1.4
    },
    {
      "id": "cbb1b60c-b396-4f0e-8dc6-dfa41dbb178e",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        442.5682587140436,
        150.50554725042372
      ],
      "parameters": {
        "color": 7,
        "width": 179.58883583572606,
        "height": 257.75985739596473,
        "content": "Will fetch the Bitcoin whitepaper, but you can change this"
      },
      "typeVersion": 1
    },
    {
      "id": "1a5511b9-5a24-40d5-a5b1-830376226e4e",
      "name": "Get top chunks matching query",
      "type": "@n8n/n8n-nodes-langchain.vectorStorePinecone",
      "position": [
        700,
        960
      ],
      "parameters": {
        "mode": "load",
        "topK": "={{ $json.chunks }}",
        "prompt": "={{ $json.chatInput }}",
        "options": {},
        "pineconeIndex": {
          "__rl": true,
          "mode": "list",
          "value": "test-index",
          "cachedResultName": "test-index"
        }
      },
      "credentials": {
        "pineconeApi": {
          "id": "eDN8BmzFKMhUNsia",
          "name": "PineconeApi account (David)"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "d8d210cf-f12e-4e82-9b28-f531d2ff14a6",
      "name": "Add to Pinecone vector store",
      "type": "@n8n/n8n-nodes-langchain.vectorStorePinecone",
      "position": [
        1120,
        240
      ],
      "parameters": {
        "mode": "insert",
        "options": {},
        "pineconeIndex": {
          "__rl": true,
          "mode": "list",
          "value": "test-index",
          "cachedResultName": "test-index"
        }
      },
      "credentials": {
        "pineconeApi": {
          "id": "eDN8BmzFKMhUNsia",
          "name": "PineconeApi account (David)"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "c501568b-fb49-487d-bced-757e3d7ed13c",
      "name": "Recursive Character Text Splitter",
      "type": "@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter",
      "position": [
        1240,
        620
      ],
      "parameters": {
        "chunkSize": 3000,
        "chunkOverlap": 200
      },
      "typeVersion": 1
    }
  ],
  "pinData": {},
  "connections": {
    "Chat Trigger": {
      "main": [
        [
          {
            "node": "Set max chunks to send to model",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Download file": {
      "main": [
        [
          {
            "node": "Add in metadata",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Prepare chunks": {
      "main": [
        [
          {
            "node": "Answer the query based on chunks",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Add in metadata": {
      "main": [
        [
          {
            "node": "Add to Pinecone vector store",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Compose citations": {
      "main": [
        [
          {
            "node": "Generate response",
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
            "node": "Add to Pinecone vector store",
            "type": "ai_embedding",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Chat Model": {
      "ai_languageModel": [
        [
          {
            "node": "Answer the query based on chunks",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Embeddings OpenAI2": {
      "ai_embedding": [
        [
          {
            "node": "Get top chunks matching query",
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
            "node": "Add to Pinecone vector store",
            "type": "ai_document",
            "index": 0
          }
        ]
      ]
    },
    "Structured Output Parser": {
      "ai_outputParser": [
        [
          {
            "node": "Answer the query based on chunks",
            "type": "ai_outputParser",
            "index": 0
          }
        ]
      ]
    },
    "Set file URL in Google Drive": {
      "main": [
        [
          {
            "node": "Download file",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get top chunks matching query": {
      "main": [
        [
          {
            "node": "Prepare chunks",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set max chunks to send to model": {
      "main": [
        [
          {
            "node": "Get top chunks matching query",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Answer the query based on chunks": {
      "main": [
        [
          {
            "node": "Compose citations",
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
            "node": "Set file URL in Google Drive",
            "type": "main",
            "index": 0
          }
        ]
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
    }
  }
}
```

<a id="template-2392"></a>

## Template 2392 - Criar, atualizar e obter perfil Humantic AI

- **Nome:** Criar, atualizar e obter perfil Humantic AI
- **Descrição:** Fluxo que cria um perfil usando uma URL (ex.: LinkedIn), faz o download de um arquivo (possível currículo), atualiza o perfil enviando esse arquivo e, por fim, recupera o perfil com uma persona específica.
- **Funcionalidade:** • Início manual: inicia o processo por execução manual.
• Criação de perfil no Humantic AI: registra um novo perfil usando uma URL de usuário (ex.: LinkedIn) como identificador.
• Download de arquivo via HTTP: recupera um arquivo remoto (por exemplo, currículo) fornecido pela etapa anterior.
• Atualização do perfil com envio de currículo: aplica atualização ao perfil existente e anexa o arquivo baixado ao perfil.
• Recuperação do perfil com persona: obtém os dados do perfil finalizando com uma opção de persona (por exemplo, "hiring") para adaptar a saída.
- **Ferramentas:** • Humantic AI: API/plataforma para criar, atualizar e recuperar perfis e gerar insights de personalidade.
• HTTP / URLs públicas: serviço de transferência via HTTP usado para baixar arquivos remotos (por exemplo, currículos ou documentos).

## Fluxo visual

```mermaid
flowchart LR
    N1["On clicking 'execute'"]
    N2["Humantic AI"]
    N3["HTTP Request"]
    N4["Humantic AI1"]
    N5["Humantic AI2"]

    N2 --> N3
    N3 --> N4
    N4 --> N5
    N1 --> N2
```

## Fluxo (.json) :

```json
{
  "id": "127",
  "name": "Create, update, and get a profile in Humantic AI",
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        290,
        300
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Humantic AI",
      "type": "n8n-nodes-base.humanticAi",
      "position": [
        490,
        300
      ],
      "parameters": {
        "userId": "https://www.linkedin.com/in/harshil1712/"
      },
      "credentials": {
        "humanticAiApi": "humantic"
      },
      "typeVersion": 1
    },
    {
      "name": "HTTP Request",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        690,
        300
      ],
      "parameters": {
        "url": "",
        "options": {},
        "responseFormat": "file"
      },
      "typeVersion": 1
    },
    {
      "name": "Humantic AI1",
      "type": "n8n-nodes-base.humanticAi",
      "position": [
        890,
        300
      ],
      "parameters": {
        "userId": "={{$node[\"Humantic AI\"].json[\"results\"][\"userid\"]}}",
        "operation": "update",
        "sendResume": true
      },
      "credentials": {
        "humanticAiApi": "humantic"
      },
      "typeVersion": 1
    },
    {
      "name": "Humantic AI2",
      "type": "n8n-nodes-base.humanticAi",
      "position": [
        1090,
        300
      ],
      "parameters": {
        "userId": "={{$node[\"Humantic AI\"].json[\"results\"][\"userid\"]}}",
        "options": {
          "persona": [
            "hiring"
          ]
        },
        "operation": "get"
      },
      "credentials": {
        "humanticAiApi": "humantic"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "Humantic AI": {
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
            "node": "Humantic AI1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Humantic AI1": {
      "main": [
        [
          {
            "node": "Humantic AI2",
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
            "node": "Humantic AI",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2394"></a>

## Template 2394 - Cadeia LLM e agente com ferramenta

- **Nome:** Cadeia LLM e agente com ferramenta
- **Descrição:** Fluxo demonstra duas abordagens: um nó de cadeia LLM codificado que envia um prompt para um modelo de linguagem, e um agente que usa uma ferramenta de consulta (Wikipedia) para responder perguntas.
- **Funcionalidade:** • Execução manual: Inicia o fluxo ao acionar a execução manual.
• Entradas de exemplo: Fornece entradas pré-definidas para teste (ex.: "Tell me a joke" e "What year was Einstein born?").
• Cadeia LLM personalizada: Constrói um template de prompt a partir da entrada e o encaminha para um modelo de linguagem para gerar a resposta.
• Agente com ferramenta: Executa um agente de chat que pode chamar uma ferramenta de consulta para obter informações externas antes de responder.
• Nós de código customizados: Implementa lógica customizada para criar a cadeia LLM e para expor a ferramenta de consulta ao agente.
• Integração com modelos externos: Encaminha prompts para provedores de LLM para geração de texto.
- **Ferramentas:** • OpenAI: Provedor de modelos de linguagem utilizado para gerar respostas e servir como LLM no fluxo.
• LangChain: Biblioteca para criar templates de prompt, encadear LLMs e construir agentes e ferramentas.
• Wikipedia: Fonte externa de conhecimento consultada pelo agente para obter informações factuais.



## Fluxo visual

```mermaid
flowchart LR
    N1["OpenAI"]
    N2["Sticky Note"]
    N3["When clicking 'Execute Workflow'"]
    N4["Set"]
    N5["Set1"]
    N6["Chat OpenAI"]
    N7["Sticky Note1"]
    N8["Custom - Wikipedia"]
    N9["Custom - LLM Chain Node"]
    N10["Agent"]

    N4 --> N9
    N5 --> N10
    N3 --> N4
    N3 --> N5
```

## Fluxo (.json) :

```json
{
  "id": "q2MJWAqpKF2BCJkq",
  "meta": {
    "instanceId": "021d3c82ba2d3bc090cbf4fc81c9312668bcc34297e022bb3438c5c88a43a5ff"
  },
  "name": "LangChain - Example - Code Node Example",
  "tags": [
    {
      "id": "snf16n0p2UrGP838",
      "name": "LangChain - Example",
      "createdAt": "2023-09-25T16:21:55.962Z",
      "updatedAt": "2023-09-25T16:21:55.962Z"
    }
  ],
  "nodes": [
    {
      "id": "ad1a920e-1048-4b58-9c4a-a0469a1f189d",
      "name": "OpenAI",
      "type": "@n8n/n8n-nodes-langchain.lmOpenAi",
      "position": [
        900,
        628
      ],
      "parameters": {
        "options": {}
      },
      "credentials": {
        "openAiApi": {
          "id": "4jRB4A20cPycBqP5",
          "name": "OpenAI account - n8n"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "7dd04ecd-f169-455c-9c90-140140e37542",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        800,
        340
      ],
      "parameters": {
        "width": 432,
        "height": 237,
        "content": "## Self-coded LLM Chain Node"
      },
      "typeVersion": 1
    },
    {
      "id": "05ad7d68-5dc8-42f2-8274-fcb5bdeb68cb",
      "name": "When clicking \"Execute Workflow\"",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        280,
        428
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "39e2fd34-3261-44a1-aa55-96f169d55aad",
      "name": "Set",
      "type": "n8n-nodes-base.set",
      "position": [
        620,
        428
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "input",
              "value": "Tell me a joke"
            }
          ]
        },
        "options": {}
      },
      "typeVersion": 2
    },
    {
      "id": "42a3184c-0c62-4e79-9220-7a93e313317e",
      "name": "Set1",
      "type": "n8n-nodes-base.set",
      "position": [
        620,
        820
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "input",
              "value": "What year was Einstein born?"
            }
          ]
        },
        "options": {}
      },
      "typeVersion": 2
    },
    {
      "id": "4e2af29d-7fc4-484b-8028-1b9a84d60172",
      "name": "Chat OpenAI",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        731,
        1108
      ],
      "parameters": {
        "options": {}
      },
      "credentials": {
        "openAiApi": {
          "id": "4jRB4A20cPycBqP5",
          "name": "OpenAI account - n8n"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "334e9176-3a18-4838-84cb-70e8154f1a30",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        880,
        1028
      ],
      "parameters": {
        "width": 320.2172923777021,
        "height": 231,
        "content": "## Self-coded Tool Node"
      },
      "typeVersion": 1
    },
    {
      "id": "05e0d5c6-df18-42ba-99b6-a2b65633a14d",
      "name": "Custom - Wikipedia",
      "type": "@n8n/n8n-nodes-langchain.code",
      "position": [
        971,
        1108
      ],
      "parameters": {
        "code": {
          "supplyData": {
            "code": "console.log('Custom Wikipedia Node runs');\nconst { WikipediaQueryRun } = require('langchain/tools');\nreturn new WikipediaQueryRun();"
          }
        },
        "outputs": {
          "output": [
            {
              "type": "ai_tool"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "id": "9c729e9a-f173-430c-8bcd-74101b614891",
      "name": "Custom - LLM Chain Node",
      "type": "@n8n/n8n-nodes-langchain.code",
      "position": [
        880,
        428
      ],
      "parameters": {
        "code": {
          "execute": {
            "code": "const { PromptTemplate } = require('langchain/prompts');\n\nconst query = $input.item.json.input;\nconst prompt = PromptTemplate.fromTemplate(query);\nconst llm = await this.getInputConnectionData('ai_languageModel', 0);\nlet chain = prompt.pipe(llm);\nconst output = await chain.invoke();\nreturn [ {json: { output } } ];"
          }
        },
        "inputs": {
          "input": [
            {
              "type": "main"
            },
            {
              "type": "ai_languageModel",
              "required": true,
              "maxConnections": 1
            }
          ]
        },
        "outputs": {
          "output": [
            {
              "type": "main"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "id": "6427bbf0-49a6-4810-9744-87d88151e914",
      "name": "Agent",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        880,
        820
      ],
      "parameters": {
        "options": {}
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "e14a709d-08fe-4ed7-903a-fb2bae80b28a",
  "connections": {
    "Set": {
      "main": [
        [
          {
            "node": "Custom - LLM Chain Node",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set1": {
      "main": [
        [
          {
            "node": "Agent",
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
            "node": "Custom - LLM Chain Node",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Chat OpenAI": {
      "ai_languageModel": [
        [
          {
            "node": "Agent",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Custom - Wikipedia": {
      "ai_tool": [
        [
          {
            "node": "Agent",
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
            "node": "Set",
            "type": "main",
            "index": 0
          },
          {
            "node": "Set1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2396"></a>

## Template 2396 - Repetição de tentativa com exclusão de erro conhecido

- **Nome:** Repetição de tentativa com exclusão de erro conhecido
- **Descrição:** Fluxo que tenta repetir uma operação até um máximo de tentativas, aguardando entre tentativas e interrompendo as repetições se um erro conhecido for detectado.
- **Funcionalidade:** • Início manual: Permite disparar o fluxo manualmente para testes ou execuções pontuais.
• Contador de tentativas: Inicializa e mantém um contador de tentativas para controlar o número de rétries.
• Verificação de limite de tentativas: Avalia se ainda há tentativas disponíveis antes de continuar.
• Incremento do contador: Atualiza o contador após cada tentativa falhada.
• Espera entre tentativas: Introduz uma pausa configurável (padrão 5s) antes de tentar novamente.
• Detecção de erro conhecido: Analisa a mensagem de erro (por exemplo, contém "could not be found") e direciona para um caminho específico sem continuar as repetições.
• Ramificação de sucesso e falha: Continua o processamento em caminhos separados para sucesso, erro conhecido ou erro após esgotar tentativas.
• Parada ao atingir limite: Finaliza com erro quando o número máximo de tentativas é alcançado.
• Nó substituível: Ponto reservado para inserir a operação real que recupera os dados (API, consulta, etc.) com saída de erro habilitada.
- **Ferramentas:** • Serviço de dados externo (API, banco de dados, etc.): Recurso alvo que fornece os dados consultados e pode retornar falhas ou mensagens de erro específicas.
• Sistema de notificação/monitoramento (opcional): Ferramenta externa para alertar ou registrar quando o limite de tentativas é atingido ou ocorrem erros recorrentes.

## Fluxo visual

```mermaid
flowchart LR
    N1["Retry limit reached"]
    N2["Set tries"]
    N3["Update tries"]
    N4["Wait"]
    N5["Catch known error"]
    N6["Replace Me"]
    N7["Success"]
    N8["Known Error"]
    N9["Sticky Note"]
    N10["Sticky Note1"]
    N11["Sticky Note2"]
    N12["Manual Trigger"]
    N13["Sticky Note3"]
    N14["Sticky Note4"]
    N15["Sticky Note5"]
    N16["Sticky Note6"]
    N17["Sticky Note7"]
    N18["If tries left"]
    N19["Sticky Note8"]

    N4 --> N3
    N2 --> N6
    N6 --> N7
    N6 --> N5
    N3 --> N18
    N18 --> N2
    N18 --> N1
    N12 --> N2
    N5 --> N8
    N5 --> N4
```

## Fluxo (.json) :

```json
{
  "id": "qAzZekQuABuH8uho",
  "meta": {
    "instanceId": "fb8bc2e315f7f03c97140b30aa454a27bc7883a19000fa1da6e6b571bf56ad6d"
  },
  "name": "Retry on fail except for known error Template",
  "tags": [],
  "nodes": [
    {
      "id": "fa6fb462-8c1b-4cab-a9f6-876e67688786",
      "name": "Retry limit reached",
      "type": "n8n-nodes-base.stopAndError",
      "position": [
        -940,
        500
      ],
      "parameters": {
        "errorMessage": "Retry limit reached"
      },
      "typeVersion": 1
    },
    {
      "id": "9627165d-1854-4a4f-b840-721f8d779b89",
      "name": "Set tries",
      "type": "n8n-nodes-base.set",
      "position": [
        -940,
        260
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "cd93a7f6-4c06-4e8a-8d0d-e812c5ec4bc5",
              "name": "tries",
              "type": "number",
              "value": "={{ $json.tries || 0 }}"
            }
          ]
        },
        "includeOtherFields": true
      },
      "typeVersion": 3.4
    },
    {
      "id": "466efd16-4922-4e61-bc81-d8e8a1d8ea61",
      "name": "Update tries",
      "type": "n8n-nodes-base.set",
      "position": [
        -60,
        500
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "df3c9b29-afa6-4e08-868d-5b7e8202eefa",
              "name": "tries",
              "type": "number",
              "value": "={{ $('Set tries').item.json.tries + 1 }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "a787761f-0a9d-4834-9a65-ac3b9a65b23e",
      "name": "Wait",
      "type": "n8n-nodes-base.wait",
      "position": [
        -280,
        500
      ],
      "webhookId": "9d3b561f-4afd-478c-8f6e-60641d4f1d0b",
      "parameters": {},
      "typeVersion": 1.1
    },
    {
      "id": "ff46ce53-69ca-4f88-8cc9-21b8d1e5557a",
      "name": "Catch known error",
      "type": "n8n-nodes-base.if",
      "position": [
        -500,
        380
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
              "id": "6a379b06-0b04-4ae4-9bf9-394bd40744b7",
              "operator": {
                "type": "string",
                "operation": "contains"
              },
              "leftValue": "={{ $json.error }}",
              "rightValue": "could not be found"
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "0e9c282a-b521-4549-8ad5-9783b4d614b3",
      "name": "Replace Me",
      "type": "n8n-nodes-base.noOp",
      "onError": "continueErrorOutput",
      "position": [
        -720,
        260
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "3b2b6839-65b9-4b0e-8e10-2010014fc8d9",
      "name": "Success",
      "type": "n8n-nodes-base.noOp",
      "position": [
        -500,
        140
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "8d972714-8dcb-4ad6-8b5f-fb30a5f3294f",
      "name": "Known Error",
      "type": "n8n-nodes-base.noOp",
      "position": [
        -280,
        260
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "e98cdc4a-73a4-41d1-bf5e-2a3bcfbf23af",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -560,
        280
      ],
      "parameters": {
        "width": 220,
        "height": 240,
        "content": "## Set filter\nFilter by status code or error message."
      },
      "typeVersion": 1
    },
    {
      "id": "e5b76cd3-d90a-4d4b-a659-ff142558cbac",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -780,
        80
      ],
      "parameters": {
        "width": 220,
        "height": 320,
        "content": "## Replace Node\nReplace this by the Node which retrieves the admired data.\nEnable error branch in Node Settings and connect the outputs like in this example"
      },
      "typeVersion": 1
    },
    {
      "id": "7ca409e6-7faf-48d5-972e-abbba3f011ef",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -1220,
        420
      ],
      "parameters": {
        "width": 220,
        "height": 220,
        "content": "## Set max tries\nChange if needed, default is 3"
      },
      "typeVersion": 1
    },
    {
      "id": "a13168eb-c4d1-46dd-857b-9a5e13ed1059",
      "name": "Manual Trigger",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        -1160,
        260
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "44c17908-96df-471b-97fc-9ce4c3acb3bb",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -340,
        400
      ],
      "parameters": {
        "width": 220,
        "height": 240,
        "content": "## Set Wait\nChange duration if needed, default is 5s"
      },
      "typeVersion": 1
    },
    {
      "id": "da7413f0-7962-4cf1-90ad-168cfc3d4c0d",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -560,
        80
      ],
      "parameters": {
        "color": 7,
        "width": 220,
        "height": 200,
        "content": "Continue here, if the request succeeded"
      },
      "typeVersion": 1
    },
    {
      "id": "e95c4b6a-2c63-4916-a239-91463728262a",
      "name": "Sticky Note5",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -340,
        200
      ],
      "parameters": {
        "color": 7,
        "width": 220,
        "height": 200,
        "content": "Continue here, if the request failed"
      },
      "typeVersion": 1
    },
    {
      "id": "8d8f7df0-35e3-4b94-96a3-6d4593732d0e",
      "name": "Sticky Note6",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -1000,
        420
      ],
      "parameters": {
        "color": 7,
        "width": 220,
        "height": 220,
        "content": "Stop here, if all tries have failed"
      },
      "typeVersion": 1
    },
    {
      "id": "893b3e51-f30f-4e2f-9e96-e1fc6f8dd0a3",
      "name": "Sticky Note7",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -1000,
        200
      ],
      "parameters": {
        "color": 7,
        "width": 220,
        "height": 220,
        "content": "Define counter for tries"
      },
      "typeVersion": 1
    },
    {
      "id": "cd1b1abb-dbd3-4023-8a6b-49c4ff5510a8",
      "name": "If tries left",
      "type": "n8n-nodes-base.if",
      "position": [
        -1160,
        500
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
              "id": "b18f784a-4386-4ced-a9e1-ce5a21ad036e",
              "operator": {
                "type": "number",
                "operation": "lt"
              },
              "leftValue": "={{ $json.tries }}",
              "rightValue": 3
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "ccce734b-c726-4b0a-9d37-7bd6df90e840",
      "name": "Sticky Note8",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -120,
        440
      ],
      "parameters": {
        "color": 7,
        "width": 220,
        "height": 220,
        "content": "Update counter for tries"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "ad610eea-ad27-4a3b-b662-edea474bc5ff",
  "connections": {
    "Wait": {
      "main": [
        [
          {
            "node": "Update tries",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set tries": {
      "main": [
        [
          {
            "node": "Replace Me",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Replace Me": {
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
            "node": "Catch known error",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Update tries": {
      "main": [
        [
          {
            "node": "If tries left",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "If tries left": {
      "main": [
        [
          {
            "node": "Set tries",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Retry limit reached",
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
            "node": "Set tries",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Catch known error": {
      "main": [
        [
          {
            "node": "Known Error",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Wait",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2399"></a>

## Template 2399 - Extração e resumo de SERP com Bright Data

- **Nome:** Extração e resumo de SERP com Bright Data
- **Descrição:** Fluxo que realiza uma pesquisa no Google via Bright Data, extrai o conteúdo textual dos resultados, gera um resumo com modelos de linguagem e envia o resultado formatado para um endpoint HTTP.
- **Funcionalidade:** • Início manual de teste: Permite acionar o fluxo manualmente para testes.
• Configuração de consulta de busca: Define a consulta de pesquisa e a zona do serviço de scraping.
• Requisição ao Bright Data Web Scraper API: Executa a busca no Google e obtém o HTML bruto da página de resultados.
• Extração de conteúdo textual: Remove HTML, CSS e scripts para produzir texto limpo dos resultados de busca.
• Resumo com modelo LLM: Gera um sumário dos resultados usando modelos avançados de linguagem.
• Agente de formatação e roteamento: Formata os resultados em um payload estruturado pronto para envio.
• Envio para Webhook HTTP: Publica o resultado formatado para um endpoint externo configurável.
• Orientações de configuração: Inclui notas para ajustar a query de busca e a URL do webhook antes de executar.
- **Ferramentas:** • Bright Data Web Scraper API: Serviço de scraping usado para buscar a página de resultados do Google e retornar o HTML bruto.
• Google Gemini (PaLM) API: Modelos de linguagem utilizados para extração, análise e sumarização do conteúdo textual.
• Webhook HTTP endpoint (ex.: webhook.site): Endpoint externo que recebe o payload final com o resumo e os resultados formatados.

## Fluxo visual

```mermaid
flowchart LR
    N1["When clicking ‘Test workflow’"]
    N2["Google Gemini Chat Model"]
    N3["Summarization Chain"]
    N4["Google Gemini Chat Model For Summarization"]
    N5["Google Gemini Chat Model1"]
    N6["Webhook HTTP Request"]
    N7["Sticky Note"]
    N8["Sticky Note1"]
    N9["Google Search Data Extractor"]
    N10["Perform Google Search Request"]
    N11["Google Search Expert AI Agent"]
    N12["Set Google Search Query"]

    N3 --> N11
    N12 --> N10
    N9 --> N3
    N10 --> N9
    N1 --> N12
```

## Fluxo (.json) :

```json
{
  "id": "GcSlNHOnN39cPhRA",
  "meta": {
    "instanceId": "885b4fb4a6a9c2cb5621429a7b972df0d05bb724c20ac7dac7171b62f1c7ef40",
    "templateCredsSetupCompleted": true
  },
  "name": "Google Search Engine Results Page Extraction with Bright Data",
  "tags": [
    {
      "id": "Kujft2FOjmOVQAmJ",
      "name": "Engineering",
      "createdAt": "2025-04-09T01:31:00.558Z",
      "updatedAt": "2025-04-09T01:31:00.558Z"
    },
    {
      "id": "ddPkw7Hg5dZhQu2w",
      "name": "AI",
      "createdAt": "2025-04-13T05:38:08.053Z",
      "updatedAt": "2025-04-13T05:38:08.053Z"
    }
  ],
  "nodes": [
    {
      "id": "c40156b9-b7ba-449b-8362-f8b8cd27a36d",
      "name": "When clicking ‘Test workflow’",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        200,
        -440
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "d98ae28e-a94f-43a1-9bfe-362adbc61c69",
      "name": "Google Gemini Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatGoogleGemini",
      "position": [
        960,
        -240
      ],
      "parameters": {
        "options": {},
        "modelName": "models/gemini-2.0-flash-exp"
      },
      "credentials": {
        "googlePalmApi": {
          "id": "YeO7dHZnuGBVQKVZ",
          "name": "Google Gemini(PaLM) Api account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "984acfe6-acd7-4817-b2d5-6d2aab511bae",
      "name": "Summarization Chain",
      "type": "@n8n/n8n-nodes-langchain.chainSummarization",
      "position": [
        1320,
        -440
      ],
      "parameters": {
        "options": {}
      },
      "typeVersion": 2
    },
    {
      "id": "6b5e26bf-8802-40d4-bc44-62c086c00f7c",
      "name": "Google Gemini Chat Model For Summarization",
      "type": "@n8n/n8n-nodes-langchain.lmChatGoogleGemini",
      "position": [
        1320,
        -260
      ],
      "parameters": {
        "options": {},
        "modelName": "models/gemini-2.0-flash-exp"
      },
      "credentials": {
        "googlePalmApi": {
          "id": "YeO7dHZnuGBVQKVZ",
          "name": "Google Gemini(PaLM) Api account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "1669f59a-eff8-41ad-a6eb-758eec7ed74a",
      "name": "Google Gemini Chat Model1",
      "type": "@n8n/n8n-nodes-langchain.lmChatGoogleGemini",
      "position": [
        1620,
        -200
      ],
      "parameters": {
        "options": {},
        "modelName": "models/gemini-2.0-flash-exp"
      },
      "credentials": {
        "googlePalmApi": {
          "id": "YeO7dHZnuGBVQKVZ",
          "name": "Google Gemini(PaLM) Api account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "ad6c4a15-13e0-49fa-9048-bc1838ba0ef9",
      "name": "Webhook HTTP Request",
      "type": "@n8n/n8n-nodes-langchain.toolHttpRequest",
      "position": [
        1960,
        -200
      ],
      "parameters": {
        "url": "https://webhook.site/ce41e056-c097-48c8-a096-9b876d3abbf7",
        "method": "POST",
        "sendBody": true,
        "parametersBody": {
          "values": [
            {
              "name": "search_summary",
              "value": "={{ $json.response.text }}",
              "valueProvider": "fieldValue"
            },
            {
              "name": "search_result"
            }
          ]
        },
        "toolDescription": "Extract the response and format a structured JSON response"
      },
      "typeVersion": 1.1
    },
    {
      "id": "dc5985c2-02cd-47d0-b518-8dc9d8302998",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        220,
        -780
      ],
      "parameters": {
        "width": 400,
        "height": 300,
        "content": "## Bright Data Google Search SERP (Search Engine Results Page)\n\nDeals with the Google Search using the Bright Data Web Scraper API.\n\nThe Information Extraction, Summarization and AI Agent are being used to demonstrate the usage of the N8N AI capabilities.\n\n**Please make sure to Set the Google Search Query and update the Webhook Notification URL**"
      },
      "typeVersion": 1
    },
    {
      "id": "38b1a20b-9d62-45d9-9399-0b927a6e882a",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        720,
        -780
      ],
      "parameters": {
        "width": 480,
        "height": 300,
        "content": "## LLM Usages\n\nGoogle Gemini Flash Exp model is being used.\n\nGoogle Search Data Extractor using the n8n Infromation Extractor node.\n\nSummarization Chain is being used for the summarization of search results.\n\nThe AI Agent formats the search result and pushes it to the Webhook via HTTP Request"
      },
      "typeVersion": 1
    },
    {
      "id": "3019d6eb-cf84-43fd-bb98-f7eed6c9c75f",
      "name": "Google Search Data Extractor",
      "type": "@n8n/n8n-nodes-langchain.informationExtractor",
      "position": [
        960,
        -440
      ],
      "parameters": {
        "text": "={{ $json.data }}",
        "options": {
          "systemPromptTemplate": "You are an expert HTML extractor. Your job is to analyze the search result and \nstrip out the html, css, scripts and produce a textual data."
        },
        "attributes": {
          "attributes": [
            {
              "name": "textual_response",
              "description": "Textual Response"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "id": "e82e62cf-6618-405a-943f-d2933771e051",
      "name": "Perform Google Search Request",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        720,
        -440
      ],
      "parameters": {
        "url": "https://api.brightdata.com/request",
        "method": "POST",
        "options": {},
        "sendBody": true,
        "sendHeaders": true,
        "authentication": "genericCredentialType",
        "bodyParameters": {
          "parameters": [
            {
              "name": "zone",
              "value": "={{ $json.zone }}"
            },
            {
              "name": "url",
              "value": "=https://www.google.com/search?q={{ encodeURI($json.search_query) }}"
            },
            {
              "name": "format",
              "value": "raw"
            }
          ]
        },
        "genericAuthType": "httpHeaderAuth",
        "headerParameters": {
          "parameters": [
            {}
          ]
        }
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "kdbqXuxIR8qIxF7y",
          "name": "Header Auth account"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "0d4baa4c-4f6d-4bb2-8964-73d9cf2a391c",
      "name": "Google Search Expert AI Agent",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        1680,
        -440
      ],
      "parameters": {
        "text": "=You are an expert Google Search Expert. You need to format the search result  and push it to the Webhook via HTTP Request. Here is the search result - {{ $('Google Search Data Extractor').item.json.output.textual_response }}",
        "options": {},
        "promptType": "define"
      },
      "typeVersion": 1.8
    },
    {
      "id": "433d4369-f750-40bd-8e46-8368f535e99f",
      "name": "Set Google Search Query",
      "type": "n8n-nodes-base.set",
      "position": [
        440,
        -440
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "3aedba66-f447-4d7a-93c0-8158c5e795f9",
              "name": "search_query",
              "type": "string",
              "value": "Bright Data"
            },
            {
              "id": "4e7ee31d-da89-422f-8079-2ff2d357a0ba",
              "name": "zone",
              "type": "string",
              "value": "serp_api1"
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
  "versionId": "3573d57f-de02-4ce6-bfdf-5e83a8a5d7d0",
  "connections": {
    "Summarization Chain": {
      "main": [
        [
          {
            "node": "Google Search Expert AI Agent",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Webhook HTTP Request": {
      "ai_tool": [
        [
          {
            "node": "Google Search Expert AI Agent",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Set Google Search Query": {
      "main": [
        [
          {
            "node": "Perform Google Search Request",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Gemini Chat Model": {
      "ai_languageModel": [
        [
          {
            "node": "Google Search Data Extractor",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Google Gemini Chat Model1": {
      "ai_languageModel": [
        [
          {
            "node": "Google Search Expert AI Agent",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Google Search Data Extractor": {
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
    "Google Search Expert AI Agent": {
      "main": [
        []
      ]
    },
    "Perform Google Search Request": {
      "main": [
        [
          {
            "node": "Google Search Data Extractor",
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
            "node": "Set Google Search Query",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Gemini Chat Model For Summarization": {
      "ai_languageModel": [
        [
          {
            "node": "Summarization Chain",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2401"></a>

## Template 2401 - Embeddings de imagem (cores + keywords)

- **Nome:** Embeddings de imagem (cores + keywords)
- **Descrição:** Converte uma imagem em um documento semântico combinando informações de cor e palavras-chave geradas por um modelo multimodal, cria embeddings e os armazena para busca vetorial.
- **Funcionalidade:** • Download da imagem: baixa a imagem a partir de um arquivo armazenado no Google Drive.
• Extração de informação de cor: obtém estatísticas dos canais de cor e identifica a cor de fundo.
• Redimensionamento da imagem: ajusta a imagem para 512x512 quando necessário para melhorar a análise.
• Geração de palavras-chave semânticas: utiliza um modelo multimodal para extrair uma lista abrangente de keywords que descrevem a imagem (assuntos, cores, humor, técnicas, etc.).
• Combinação e formatação do documento: junta as keywords e as estatísticas de cor em um documento único com metadata (formato, cor de fundo, fonte).
• Geração de embeddings: cria vetores de embedding a partir do documento combinado para uso em busca semântica.
• Inserção em loja vetorial: armazena os embeddings em uma store vetorial para permitir buscas por similaridade.
• Busca por similaridade: permite consultar o conjunto de embeddings usando prompts de texto para localizar imagens relacionadas.
• Pré-processamento de texto: divide o texto em partes apropriadas para indexação quando necessário.
• Aviso de uso: inclui um alerta explícito para não utilizar o processo para análise médica ou diagnóstico.
- **Ferramentas:** • Google Drive: armazenamento e fornecimento do arquivo de imagem de origem.
• OpenAI (modelos multimodais e de embeddings): análise da imagem para extração de keywords e geração de embeddings vetoriais.
• Serviço de armazenamento vetorial (em memória ou externo): armazena e recupera embeddings para buscas por similaridade.

## Fluxo visual

```mermaid
flowchart LR
    N1["When clicking 'Test workflow'"]
    N2["Google Drive"]
    N3["Get Color Information"]
    N4["Resize Image"]
    N5["Default Data Loader"]
    N6["Recursive Character Text Splitter"]
    N7["Sticky Note"]
    N8["Sticky Note1"]
    N9["Sticky Note2"]
    N10["Combine Image Analysis"]
    N11["Document for Embedding"]
    N12["Sticky Note3"]
    N13["Sticky Note4"]
    N14["Sticky Note5"]
    N15["Sticky Note6"]
    N16["Embeddings OpenAI1"]
    N17["Sticky Note7"]
    N18["Sticky Note8"]
    N19["Get Image Keywords"]
    N20["In-Memory Vector Store"]
    N21["Embeddings OpenAI"]
    N22["Search for Image"]

    N2 --> N3
    N2 --> N4
    N4 --> N19
    N19 --> N10
    N3 --> N10
    N10 --> N11
    N11 --> N20
    N1 --> N2
```

## Fluxo (.json) :

```json
{
  "meta": {
    "instanceId": "26ba763460b97c249b82942b23b6384876dfeb9327513332e743c5f6219c2b8e"
  },
  "nodes": [
    {
      "id": "141638a4-b340-473f-a800-be7dbdcff131",
      "name": "When clicking \"Test workflow\"",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        695,
        380
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "6ccdaca5-f620-4afa-bed6-92f3a450687d",
      "name": "Google Drive",
      "type": "n8n-nodes-base.googleDrive",
      "position": [
        875,
        380
      ],
      "parameters": {
        "fileId": {
          "__rl": true,
          "mode": "list",
          "value": "0B43u2YYOTJR2cC1BRkptZ3N4QTk4NEtxRko5cjhKUUFyemw0",
          "cachedResultUrl": "https://drive.google.com/file/d/0B43u2YYOTJR2cC1BRkptZ3N4QTk4NEtxRko5cjhKUUFyemw0/view?usp=drivesdk&resourcekey=0-UJ8EfTMMBRNVyBb6KhN2Tg",
          "cachedResultName": "0B0A0255.jpeg"
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
      "id": "b0c2f7a4-a336-4705-aeda-411f2518aaef",
      "name": "Get Color Information",
      "type": "n8n-nodes-base.editImage",
      "position": [
        1200,
        200
      ],
      "parameters": {
        "operation": "information"
      },
      "typeVersion": 1
    },
    {
      "id": "3e42b3f1-6900-4622-8c0d-2d9a27a7e1c9",
      "name": "Resize Image",
      "type": "n8n-nodes-base.editImage",
      "position": [
        1200,
        580
      ],
      "parameters": {
        "width": 512,
        "height": 512,
        "options": {},
        "operation": "resize",
        "resizeOption": "onlyIfLarger"
      },
      "typeVersion": 1
    },
    {
      "id": "00425bb2-289e-4a09-8fcb-52319281483c",
      "name": "Default Data Loader",
      "type": "@n8n/n8n-nodes-langchain.documentDefaultDataLoader",
      "position": [
        2300,
        380
      ],
      "parameters": {
        "options": {
          "metadata": {
            "metadataValues": [
              {
                "name": "source",
                "value": "={{ $('Document for Embedding').item.json.metadata.source }}"
              },
              {
                "name": "format",
                "value": "={{ $('Document for Embedding').item.json.metadata.format }}"
              },
              {
                "name": "backgroundColor",
                "value": "={{ $('Document for Embedding').item.json.metadata.backgroundColor }}"
              }
            ]
          }
        }
      },
      "typeVersion": 1
    },
    {
      "id": "06dbdf39-9d72-460e-a29c-1ae4e9f3552a",
      "name": "Recursive Character Text Splitter",
      "type": "@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter",
      "position": [
        2300,
        500
      ],
      "parameters": {
        "options": {}
      },
      "typeVersion": 1
    },
    {
      "id": "139cac42-c006-4c9d-8298-ade845e137a7",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1140,
        100
      ],
      "parameters": {
        "color": 7,
        "width": 372,
        "height": 288,
        "content": "### Get Color Channels\n[Source: https://www.pinecone.io/learn/series/image-search/color-histograms/](https://www.pinecone.io/learn/series/image-search/color-histograms/)"
      },
      "typeVersion": 1
    },
    {
      "id": "9b8584ae-067c-4515-b194-32986ba3bf8b",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1140,
        418
      ],
      "parameters": {
        "color": 7,
        "width": 376.4067897296865,
        "height": 335.30166772984643,
        "content": "### Generate Image Keywords\n[Source: https://www.pinecone.io/learn/series/image-search/bag-of-visual-words/](https://www.pinecone.io/learn/series/image-search/bag-of-visual-words/)\n\nNote, OpenAI Image models work best when image is resized to 512x512."
      },
      "typeVersion": 1
    },
    {
      "id": "7f2c27d7-9947-42fa-aafb-78f4f95ac433",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        240,
        540
      ],
      "parameters": {
        "color": 3,
        "width": 359.1981770749933,
        "height": 98.40143173756314,
        "content": "⚠️ **Multimodal embedding is not designed analyze medical images for diagnostic features or disease patterns.** Please do not use Multimodal embedding for medical purposes."
      },
      "typeVersion": 1
    },
    {
      "id": "cb6b4a82-db5f-41f0-94dc-6cfabe0905eb",
      "name": "Combine Image Analysis",
      "type": "n8n-nodes-base.merge",
      "position": [
        1700,
        260
      ],
      "parameters": {
        "mode": "combine",
        "options": {},
        "combinationMode": "mergeByPosition"
      },
      "typeVersion": 2.1
    },
    {
      "id": "1ba33665-3ebb-4b23-989d-eec53dfd225a",
      "name": "Document for Embedding",
      "type": "n8n-nodes-base.set",
      "position": [
        1860,
        257
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "8204b731-24e2-4993-9e6d-4cea80393580",
              "name": "data",
              "type": "string",
              "value": "=## keywords\\n\n{{ $json.content }}\\n\n## color information:\\n\n{{ JSON.stringify($json[\"Channel Statistics\"]) }}"
            },
            {
              "id": "ca49cccf-ea4e-4362-bf49-ac836c8758d3",
              "name": "metadata",
              "type": "object",
              "value": "={ \"format\": \"{{ $json.format }}\", \"backgroundColor\": \"{{ $json[\"Background Color\"] }}\", \"source\": \"{{ $binary.data.fileName }}\" } "
            }
          ]
        }
      },
      "typeVersion": 3.3
    },
    {
      "id": "5d01a2fd-0190-48fc-b588-d5872c5cd793",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        640,
        250.0169327052916
      ],
      "parameters": {
        "color": 7,
        "width": 418.6907913057789,
        "height": 316.7698949693208,
        "content": "## 1. Get the Source Image\nIn this demo, we just need an image file. We'll pull an image from google drive but you can use all input trigger or source you prefer."
      },
      "typeVersion": 1
    },
    {
      "id": "4c9825f3-6a2b-4fd2-bdb1-e49f8d947e7a",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1098.439755647174,
        -145.1609149026466
      ],
      "parameters": {
        "color": 7,
        "width": 462.52060804115854,
        "height": 938.3723985625845,
        "content": "## 2. Image Embedding Methods\n[Read more about working with images in n8n](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.editimage)\n\nThere are a [myriad of image embedding techniques](https://www.pinecone.io/learn/series/image-search/) some which involve specialised models and some which do a simplified image-to-text representation.\nIn this demo, we'll use the simplified text representation methods: collecting color channel information and using Multimodal LLMs to produce keywords for the image. Together, these will form the document we'll embed to represent our image for search."
      },
      "typeVersion": 1
    },
    {
      "id": "e4035987-16c0-4d03-9e20-5f2042a6a020",
      "name": "Sticky Note5",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1600,
        120
      ],
      "parameters": {
        "color": 7,
        "width": 418.6907913057789,
        "height": 343.6004071339855,
        "content": "## 3. Generate Embedding Doc\nIt is important to define your metadata for later filtering and retrieval purposes.\n\n"
      },
      "typeVersion": 1
    },
    {
      "id": "91fe4c5c-c063-48e2-b248-801c11880c69",
      "name": "Sticky Note6",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2060,
        -11.068945113406585
      ],
      "parameters": {
        "color": 7,
        "width": 532.5269726975372,
        "height": 665.9365418117011,
        "content": "## 3. Store in Vector Store\n[Read more about vector stores](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreinmemory)\n\nOnce our document is ready, we can just insert into any vector store to make it ready for searching. When searching, be sure to defined the same vector store index used here!\nNote: Metadata is defined in the document loader which must be mapped manually.\n\n"
      },
      "typeVersion": 1
    },
    {
      "id": "6e8ffa06-ddec-463a-b8d6-581ad7095398",
      "name": "Embeddings OpenAI1",
      "type": "@n8n/n8n-nodes-langchain.embeddingsOpenAi",
      "position": [
        2680,
        547
      ],
      "parameters": {
        "options": {}
      },
      "credentials": {
        "openAiApi": {
          "id": "8gccIjcuf3gvaoEr",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "3dea73b2-6aa1-4158-945e-a5d6bea65244",
      "name": "Sticky Note7",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2620,
        200
      ],
      "parameters": {
        "color": 7,
        "width": 400.96585774172854,
        "height": 512.739000439197,
        "content": "## 4. Try it out!\n[Read more about vector stores](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreinmemory)\n\nHere's a quick test to use a simple text prompt to search for the image. Next step would be to implement image-to-image search by using the \"Embedding Doc\" to search rather to store in the vector database.\n\n"
      },
      "typeVersion": 1
    },
    {
      "id": "f6a543d4-df3b-456c-8f85-4dca29029b55",
      "name": "Sticky Note8",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        240,
        140
      ],
      "parameters": {
        "width": 359.6648027457353,
        "height": 384.6280362222034,
        "content": "## Try It Out!\n### This workflow does the following:\n* Downloads a selected image from Google Drive.\n* Extracts colour channel information from the image.\n* Generates semantic keywords of the iamge using OpenAI vision model.\n* Combines extracted and generated data to create an embedding document for the image.\n* Inserts this document into a vector store to allow for vector search on the original image. \n\n### Need Help?\nJoin the [Discord](https://discord.com/invite/XPKeKXeB7d) or ask in the [Forum](https://community.n8n.io/)!\n\nHappy Hacking!"
      },
      "typeVersion": 1
    },
    {
      "id": "1b1e8568-3779-4ee1-b520-517246d9bf86",
      "name": "Get Image Keywords",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "position": [
        1360,
        580
      ],
      "parameters": {
        "text": "Extract all possible semantic keywords which describe the image. Be comprehensive and be sure to identify subjects (if applicable) such as biological and non-biological objects, lightning, mood, tone, color, special effects, camera and/or techniques used if known. Respond with a comma-separated list.",
        "options": {
          "detail": "high"
        },
        "resource": "image",
        "inputType": "base64",
        "operation": "analyze"
      },
      "credentials": {
        "openAiApi": {
          "id": "8gccIjcuf3gvaoEr",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1.3
    },
    {
      "id": "724acae9-75d2-4421-b5a3-b920f7bda825",
      "name": "In-Memory Vector Store",
      "type": "@n8n/n8n-nodes-langchain.vectorStoreInMemory",
      "position": [
        2180,
        200
      ],
      "parameters": {
        "mode": "insert",
        "memoryKey": "image_embeddings"
      },
      "typeVersion": 1
    },
    {
      "id": "52afd512-0d55-4ae3-9377-4cb324c571a8",
      "name": "Embeddings OpenAI",
      "type": "@n8n/n8n-nodes-langchain.embeddingsOpenAi",
      "position": [
        2180,
        420
      ],
      "parameters": {
        "options": {}
      },
      "credentials": {
        "openAiApi": {
          "id": "8gccIjcuf3gvaoEr",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "c769f279-22ef-4cb1-aef3-9089bb92a0a4",
      "name": "Search for Image",
      "type": "@n8n/n8n-nodes-langchain.vectorStoreInMemory",
      "position": [
        2680,
        387
      ],
      "parameters": {
        "mode": "load",
        "prompt": "student having fun",
        "memoryKey": "image_embeddings"
      },
      "typeVersion": 1
    }
  ],
  "pinData": {},
  "connections": {
    "Google Drive": {
      "main": [
        [
          {
            "node": "Get Color Information",
            "type": "main",
            "index": 0
          },
          {
            "node": "Resize Image",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Resize Image": {
      "main": [
        [
          {
            "node": "Get Image Keywords",
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
            "node": "In-Memory Vector Store",
            "type": "ai_embedding",
            "index": 0
          }
        ]
      ]
    },
    "Embeddings OpenAI1": {
      "ai_embedding": [
        [
          {
            "node": "Search for Image",
            "type": "ai_embedding",
            "index": 0
          }
        ]
      ]
    },
    "Get Image Keywords": {
      "main": [
        [
          {
            "node": "Combine Image Analysis",
            "type": "main",
            "index": 1
          }
        ]
      ]
    },
    "Default Data Loader": {
      "ai_document": [
        [
          {
            "node": "In-Memory Vector Store",
            "type": "ai_document",
            "index": 0
          }
        ]
      ]
    },
    "Get Color Information": {
      "main": [
        [
          {
            "node": "Combine Image Analysis",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Combine Image Analysis": {
      "main": [
        [
          {
            "node": "Document for Embedding",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Document for Embedding": {
      "main": [
        [
          {
            "node": "In-Memory Vector Store",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "When clicking \"Test workflow\"": {
      "main": [
        [
          {
            "node": "Google Drive",
            "type": "main",
            "index": 0
          }
        ]
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
    }
  }
}
```

<a id="template-2403"></a>

## Template 2403 - Teste A/B de prompts para agente de chat

- **Nome:** Teste A/B de prompts para agente de chat
- **Descrição:** Gerencia e executa testes A/B de prompts para um agente de conversação, garantindo consistência da variante por sessão e preservando o histórico de conversas para contexto.
- **Funcionalidade:** • Recepção de mensagem de chat: Inicia o fluxo ao receber uma mensagem com identificação de sessão.
• Definição de valores de caminho (baseline/alternative): Define e permite editar os textos do prompt baseline e alternativo.
• Verificação de sessão existente: Consulta a tabela de sessões para determinar se o chat já tem uma variante atribuída.
• Atribuição aleatória de variante à sessão: Quando a sessão não existe, grava o ID da sessão e atribui aleatoriamente a variante (50/50).
• Seleção do prompt apropriado: Usa a informação armazenada da sessão para escolher entre o prompt baseline ou o alternativo para todas as interações dessa sessão.
• Agente de IA com memória: Envia a entrada do usuário e o prompt selecionado ao modelo de linguagem, utilizando o histórico salvo para fornecer contexto contínuo.
• Armazenamento de histórico de conversas: Persiste mensagens por sessão em um banco de dados relacional para memória de longo prazo e recuperação futura.
• Facilidade de configuração: Permite trocar o modelo de linguagem ou ajustar parâmetros do teste sem alterar a lógica central.
- **Ferramentas:** • Supabase: Banco de dados gerenciado usado para registrar sessões de teste A/B e armazenar o flag que indica qual variante usar.
• OpenAI: Provedor de modelos de linguagem responsável por gerar as respostas do agente com base no prompt selecionado.
• PostgreSQL: Banco de dados relacional utilizado para armazenar o histórico de chat por sessão (memória do agente).

## Fluxo visual

```mermaid
flowchart LR
    N1["When chat message received"]
    N2["AI Agent"]
    N3["Check If Session Exists"]
    N4["If Session Does Exist"]
    N5["Assign Path To Session"]
    N6["Define Path Values"]
    N7["OpenAI Chat Model"]
    N8["Postgres Chat Memory"]
    N9["Sticky Note1"]
    N10["Sticky Note"]
    N11["Sticky Note2"]
    N12["Get Correct Prompt"]
    N13["Sticky Note6"]
    N14["Sticky Note8"]
    N15["Sticky Note5"]
    N16["Sticky Note3"]

    N6 --> N3
    N12 --> N2
    N4 --> N12
    N4 --> N5
    N5 --> N12
    N3 --> N4
    N1 --> N6
```

## Fluxo (.json) :

```json
{
  "id": "TEA7K9MSVQGCWKe6",
  "meta": {
    "instanceId": "ac63467607103d9c95dd644384984672b90b1cb03e07edbaf18fe72b2a6c45bb",
    "templateCredsSetupCompleted": true
  },
  "name": "A/B Split Testing",
  "tags": [],
  "nodes": [
    {
      "id": "e8404493-4297-4169-a72f-89e668ae5fbc",
      "name": "When chat message received",
      "type": "@n8n/n8n-nodes-langchain.chatTrigger",
      "position": [
        -1460,
        -140
      ],
      "webhookId": "334e3a8d-73d2-4d3c-9927-158c1169ef5e",
      "parameters": {
        "options": {}
      },
      "typeVersion": 1.1
    },
    {
      "id": "582e1c1b-12ff-42ff-8130-48f94eebd706",
      "name": "AI Agent",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        220,
        -160
      ],
      "parameters": {
        "text": "={{ $('When chat message received').item.json.chatInput }}",
        "options": {
          "systemMessage": "={{ $json.prompt }}"
        },
        "promptType": "define"
      },
      "typeVersion": 1.7
    },
    {
      "id": "39ca5c70-11d4-4f86-bde5-0f9827297be9",
      "name": "Check If Session Exists",
      "type": "n8n-nodes-base.supabase",
      "position": [
        -960,
        -140
      ],
      "parameters": {
        "filters": {
          "conditions": [
            {
              "keyName": "session_id",
              "keyValue": "={{ $('When chat message received').item.json.sessionId }}"
            }
          ]
        },
        "tableId": "split_test_sessions",
        "operation": "get"
      },
      "credentials": {
        "supabaseApi": {
          "id": "1iEg1EzFrF29iqp2",
          "name": "Supabase (bsde.ai)"
        }
      },
      "executeOnce": false,
      "typeVersion": 1,
      "alwaysOutputData": true
    },
    {
      "id": "35f2c270-9571-41ba-ab7c-47a6742d7d90",
      "name": "If Session Does Exist",
      "type": "n8n-nodes-base.if",
      "position": [
        -720,
        -140
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
              "id": "4270c464-6874-45d2-aa3b-606f45544c3d",
              "operator": {
                "type": "number",
                "operation": "exists",
                "singleValue": true
              },
              "leftValue": "={{ $json.id }}",
              "rightValue": ""
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "ec00ad92-96e9-4936-a547-2a2715ff5c32",
      "name": "Assign Path To Session",
      "type": "n8n-nodes-base.supabase",
      "position": [
        -400,
        -20
      ],
      "parameters": {
        "tableId": "split_test_sessions",
        "fieldsUi": {
          "fieldValues": [
            {
              "fieldId": "show_alternative",
              "fieldValue": "={{ Math.random() < 0.5 }}"
            },
            {
              "fieldId": "session_id",
              "fieldValue": "={{ $('When chat message received').item.json.sessionId }}"
            }
          ]
        }
      },
      "credentials": {
        "supabaseApi": {
          "id": "1iEg1EzFrF29iqp2",
          "name": "Supabase (bsde.ai)"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "92ee7145-30ae-41e9-bc04-eef03b84485e",
      "name": "Define Path Values",
      "type": "n8n-nodes-base.set",
      "position": [
        -1200,
        -140
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "9581a184-a120-4b1f-8408-cfe97520d107",
              "name": "baseline_value",
              "type": "string",
              "value": "The dog's name is Ben"
            },
            {
              "id": "1752f2c4-4ce4-4893-b8db-1c59131c298a",
              "name": "alternative_value",
              "type": "string",
              "value": "The dog's name is Tom"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "23c1b4e2-2ba2-4237-bb4b-b92da127d201",
      "name": "OpenAI Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        300,
        60
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
          "id": "1OMpAMAKR9l3eUDI",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "be3f14b9-68c7-457d-b5bf-a6abbadf5b67",
      "name": "Postgres Chat Memory",
      "type": "@n8n/n8n-nodes-langchain.memoryPostgresChat",
      "position": [
        480,
        60
      ],
      "parameters": {
        "tableName": "n8n_split_test_chat_histories",
        "sessionKey": "={{ $('When chat message received').item.json.sessionId }}",
        "sessionIdType": "customKey"
      },
      "credentials": {
        "postgres": {
          "id": "tzLXHvhykxvYghPC",
          "name": "bsde.ai Supabase (Session Pooler)"
        }
      },
      "typeVersion": 1.3
    },
    {
      "id": "1c20d274-2482-4551-a4ea-64860eb35276",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -1520,
        -260
      ],
      "parameters": {
        "color": 7,
        "width": 220,
        "height": 300,
        "content": "## 1. Receive Message\n\n"
      },
      "typeVersion": 1
    },
    {
      "id": "ee22d3b1-d447-4e35-8ac4-d093edf6deee",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -1280,
        -340
      ],
      "parameters": {
        "color": 7,
        "width": 1340,
        "height": 500,
        "content": "## 2. Determine Prompt for LLM\n"
      },
      "typeVersion": 1
    },
    {
      "id": "7d90ec00-5fca-4b0d-bc1f-e8b8c179b960",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        80,
        -240
      ],
      "parameters": {
        "color": 7,
        "width": 520,
        "height": 440,
        "content": "## 3. AI Agent"
      },
      "typeVersion": 1
    },
    {
      "id": "b9b9e0e8-53c1-4d6a-bbdc-c2a13d740dfb",
      "name": "Get Correct Prompt",
      "type": "n8n-nodes-base.set",
      "position": [
        -80,
        -160
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "08de68ec-0f12-43ee-98ab-59d8a414f114",
              "name": "prompt",
              "type": "string",
              "value": "={{ $json.show_alternative ? $('Define Path Values').item.json.alternative_value : $('Define Path Values').item.json.baseline_value }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "2b78ce9b-e6b4-4744-8ddf-00f8ae990fc8",
      "name": "Sticky Note6",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -1260,
        -240
      ],
      "parameters": {
        "color": 5,
        "width": 220,
        "height": 260,
        "content": "### Modification\nSet the values of the  baseline and alternative prompts"
      },
      "typeVersion": 1
    },
    {
      "id": "0646f176-407a-41ee-b602-34bd681fc421",
      "name": "Sticky Note8",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        100,
        40
      ],
      "parameters": {
        "color": 5,
        "width": 340,
        "height": 140,
        "content": "### Modification\nReplace this sub-node \nto use a different language\n model"
      },
      "typeVersion": 1
    },
    {
      "id": "a391018c-5d28-4384-89e1-0435758a6945",
      "name": "Sticky Note5",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -1480,
        -600
      ],
      "parameters": {
        "width": 520,
        "height": 240,
        "content": "### Setup\n1. Create a table in Supabase called **split_test_sessions**. It needs to have the following columns: **session_id** (`text`) and **show_alternative** (`bool`)\n2. Add your **Supabase**, **OpenAI**, and **PostgreSQL** credentials\n3. Modify the **Define Path Values** node to set the baseline and alternative prompt values.\n4. Activate the workflow and test by sending messages through n8n's inbuilt chat\n5. Experiment with different chat sessions to test see both prompts in action"
      },
      "typeVersion": 1
    },
    {
      "id": "2382d146-f0c1-4de6-9e90-b17c304df692",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -2120,
        -360
      ],
      "parameters": {
        "width": 560,
        "height": 480,
        "content": "\n## Split Test Different Agent Prompts with Supabase and OpenAI\n### Use Case\nOftentimes, it's useful to test different settings for a large language model in production against various metrics. Split testing is a good method for doing this.\n### What it Does\nThis workflow randomly assigns chat sessions to one of two prompts, the baseline and the alternative. The agent will use the same prompt for all interactions in that chat session.\n### How it Works\n1. When messages arrive, a table containing information regarding session ID and which prompt to use is checked to see if the chat already exists\n2. If it does not, the session ID is added to the table and a prompt is randomly assigned\n3. These values are then used to generate a response\n### Next Steps\n- Modify the workflow to test different LLM settings such as temperature\n- Add a method to measure the efficacy of the two alternative prompts"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "339c6f2f-e4d1-4922-9442-2c1a78e96067",
  "connections": {
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
    "Define Path Values": {
      "main": [
        [
          {
            "node": "Check If Session Exists",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Correct Prompt": {
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
    "Postgres Chat Memory": {
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
    "If Session Does Exist": {
      "main": [
        [
          {
            "node": "Get Correct Prompt",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Assign Path To Session",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Assign Path To Session": {
      "main": [
        [
          {
            "node": "Get Correct Prompt",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Check If Session Exists": {
      "main": [
        [
          {
            "node": "If Session Does Exist",
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
            "node": "Define Path Values",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2405"></a>

## Template 2405 - Resposta automática a pedidos de agendamento

- **Nome:** Resposta automática a pedidos de agendamento
- **Descrição:** Detecta e-mails que sugerem marcar reunião ou chamada e responde automaticamente propondo horários com base na disponibilidade do calendário.
- **Funcionalidade:** • Monitoramento de e-mails não lidos: Verifica periodicamente a caixa de entrada em busca de novas mensagens não lidas.
• Classificação do conteúdo: Usa um modelo de linguagem para avaliar se o e-mail solicita um agendamento.
• Consulta de disponibilidade de calendário: Recupera eventos futuros para determinar horários livres dentro de um intervalo definido.
• Composição inteligente de resposta: Gera uma resposta que propõe horários específicos, garantindo intervalos entre compromissos e adicionando 15 minutos de buffer quando necessário.
• Envio de resposta e organização: Responde ao remetente por e-mail e marca a mensagem original como lida.
- **Ferramentas:** • OpenAI (modelo LLM): Classificação do texto do e-mail e geração da resposta em linguagem natural.
• Gmail: Recebimento de e-mails, envio de respostas e marcação das mensagens como lidas.
• Google Calendar: Leitura dos eventos e verificação da disponibilidade para sugerir horários apropriados.



## Fluxo visual

```mermaid
flowchart LR
    N1["Sticky Note"]
    N2["Sticky Note1"]
    N3["OpenAI Chat Model"]
    N4["OpenAI Chat Model1"]
    N5["Send reply"]
    N6["Gmail Trigger"]
    N7["Classify appointment"]
    N8["Agent"]
    N9["Google Calendar"]
    N10["Mark as read"]

    N8 --> N5
    N8 --> N10
    N6 --> N7
    N7 --> N8
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
      "id": "eaa31cde-3017-400d-aac8-999def8cc227",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -340,
        -780
      ],
      "parameters": {
        "width": 617,
        "height": 490,
        "content": "## Check if incoming email is about appointment\nWe use LLM to check subject and body of the email and determine if it's an appointment request. "
      },
      "typeVersion": 1
    },
    {
      "id": "b03d3f72-d1d8-49a7-bcc1-a476fd5c4ad7",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        400,
        -780
      ],
      "parameters": {
        "width": 796,
        "height": 482,
        "content": "## Get calendar availability and compose a response\nMake sure to update the Workflow ID if you are running this as 2 workflows"
      },
      "typeVersion": 1
    },
    {
      "id": "29ce0093-c4c8-41cc-be69-334de3a1d1a2",
      "name": "OpenAI Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        -60,
        -460
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
      "id": "5176f475-704b-446e-b368-ffa395bb089e",
      "name": "OpenAI Chat Model1",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        480,
        -460
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
      "id": "0e8a75dd-ce68-46c3-972c-32b15e04b254",
      "name": "Send reply",
      "type": "n8n-nodes-base.gmail",
      "position": [
        940,
        -660
      ],
      "webhookId": "0f18d414-1b14-4d2e-9fc2-d2d302372dc6",
      "parameters": {
        "message": "={{ $json.output }}",
        "options": {},
        "messageId": "={{ $('Gmail Trigger').first().json.id }}",
        "operation": "reply"
      },
      "credentials": {
        "gmailOAuth2": {
          "id": "Sf5Gfl9NiFTNXFWb",
          "name": "Gmail account"
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "bf154384-274a-4cdd-977d-890220948a9d",
      "name": "Gmail Trigger",
      "type": "n8n-nodes-base.gmailTrigger",
      "position": [
        -280,
        -640
      ],
      "parameters": {
        "filters": {
          "readStatus": "unread",
          "includeSpamTrash": false
        },
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
          "id": "Sf5Gfl9NiFTNXFWb",
          "name": "Gmail account"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "5a268b34-38ea-4e55-87ab-8a616e2aa1fa",
      "name": "Classify appointment",
      "type": "@n8n/n8n-nodes-langchain.textClassifier",
      "position": [
        -60,
        -640
      ],
      "parameters": {
        "options": {
          "fallback": "discard"
        },
        "inputText": "=Please evaluate the following email to determine if it suggests scheduling a meeting or a call:\nSubject: {{ $json.Subject }}\nSnippet: {{ $json.snippet }}",
        "categories": {
          "categories": [
            {
              "category": "is_appointment",
              "description": "email Is requesting an appointment"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "id": "7b5a8468-09e5-4575-97cb-9175ee02b19d",
      "name": "Agent",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        500,
        -660
      ],
      "parameters": {
        "text": "=Sender: {{ $('Gmail Trigger').first().json.From }}\nSubject: {{ $('Gmail Trigger').first().json.Subject }}\nEmail Text: {{ $('Gmail Trigger').first().json.snippet }}",
        "options": {
          "systemMessage": "=You are an email scheduling assistant. Based on the received email, check my availability and propose an appropriate response. \nAim to get a specific time, rather than just a day. When checking my availability, make sure that there's enough time in between meetings.\nIf I'm not available, ALWAYS propose a new time based on my availability. When proposing a new time, always leave 15 minutes buffer from previous meeting.\nToday date and time is: {{ $now.toISO() }}."
        },
        "promptType": "define"
      },
      "typeVersion": 1.8
    },
    {
      "id": "b61e8061-5719-4c30-97da-e306e7b79b76",
      "name": "Google Calendar",
      "type": "n8n-nodes-base.googleCalendarTool",
      "position": [
        680,
        -460
      ],
      "parameters": {
        "options": {},
        "timeMax": "={{ $now.plus(1, 'month').toISO() }}",
        "timeMin": "={{ $now.minus(1, 'day').toISO() }}",
        "calendar": {
          "__rl": true,
          "mode": "id",
          "value": "your_email@gmail.com"
        },
        "operation": "getAll",
        "returnAll": true
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
      "id": "47e07b6c-d432-4111-b33e-56d6c305c40c",
      "name": "Mark as read",
      "type": "n8n-nodes-base.gmail",
      "position": [
        940,
        -480
      ],
      "webhookId": "7e2d851b-c9f3-471c-875d-0da7c2c3b561",
      "parameters": {
        "messageId": "={{ $('Gmail Trigger').first().json.id }}",
        "operation": "markAsRead"
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
    "Agent": {
      "main": [
        [
          {
            "node": "Send reply",
            "type": "main",
            "index": 0
          },
          {
            "node": "Mark as read",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Gmail Trigger": {
      "main": [
        [
          {
            "node": "Classify appointment",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Calendar": {
      "ai_tool": [
        [
          {
            "node": "Agent",
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
            "node": "Classify appointment",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Chat Model1": {
      "ai_languageModel": [
        [
          {
            "node": "Agent",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Classify appointment": {
      "main": [
        [
          {
            "node": "Agent",
            "type": "main",
            "index": 0
          }
        ],
        []
      ]
    }
  }
}
```

<a id="template-2407"></a>

## Template 2407 - Mensagens de boas-vindas e despedida no Telegram

- **Nome:** Mensagens de boas-vindas e despedida no Telegram
- **Descrição:** Fluxo que detecta quando um usuário entra ou sai de um chat do Telegram e envia mensagens de boas-vindas ou despedida para um canal.
- **Funcionalidade:** • Detecção de novos membros: identifica eventos de new_chat_member e extrai o primeiro nome para uso na mensagem.
• Envio de boas-vindas: envia uma mensagem personalizada de boas-vindas para o canal @comunidadn8 incluindo o primeiro nome do usuário.
• Detecção de saída de membros: identifica eventos de left_chat_member e extrai o primeiro nome para uso na mensagem.
• Envio de despedida: envia uma mensagem de despedida personalizada para o canal @comunidadn8 incluindo o primeiro nome do usuário.
• Filtragem de nomes vazios: verifica se o campo first_name está vazio e evita o envio quando não houver nome disponível.
- **Ferramentas:** • Telegram: plataforma de mensagens e API de bot utilizada para receber atualizações de chat (entradas/saídas) e enviar mensagens ao canal.

## Fluxo visual

```mermaid
flowchart LR
    N1["Saludos-IF"]
    N2["Saludos-IF1"]
    N3["S-Telegram"]
    N4["Saludos-TelegramTrigger"]
    N5["S-Telegram2"]

    N1 --> N5
    N2 --> N3
    N4 --> N2
    N4 --> N1
```

## Fluxo (.json) :

```json
{
  "id": "27",
  "name": "N8N Español - BOT",
  "nodes": [
    {
      "name": "Saludos-IF",
      "type": "n8n-nodes-base.if",
      "position": [
        450,
        450
      ],
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$node[\"Saludos-TelegramTrigger\"].json[\"message\"][\"new_chat_member\"][\"first_name\"]}}",
              "operation": "isEmpty"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Saludos-IF1",
      "type": "n8n-nodes-base.if",
      "position": [
        490,
        630
      ],
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$node[\"Saludos-TelegramTrigger\"].json[\"message\"][\"left_chat_member\"][\"first_name\"]}}",
              "operation": "isEmpty"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "S-Telegram",
      "type": "n8n-nodes-base.telegram",
      "position": [
        700,
        660
      ],
      "parameters": {
        "text": "=✖️ {{$node[\"Saludos-TelegramTrigger\"].json[\"message\"][\"left_chat_member\"][\"first_name\"]}} DEP. 🙏 Que los Dioses te protejan.",
        "chatId": "=@comunidadn8n",
        "additionalFields": {}
      },
      "credentials": {
        "telegramApi": "N8N Español - BOT"
      },
      "typeVersion": 1
    },
    {
      "name": "Saludos-TelegramTrigger",
      "type": "n8n-nodes-base.telegramTrigger",
      "position": [
        260,
        560
      ],
      "webhookId": "4ef8c98e-e617-4d36-9c6d-04fae7e9298c",
      "parameters": {
        "updates": [
          "*"
        ],
        "additionalFields": {}
      },
      "credentials": {
        "telegramApi": "N8N Español - BOT"
      },
      "typeVersion": 1
    },
    {
      "name": "S-Telegram2",
      "type": "n8n-nodes-base.telegram",
      "position": [
        730,
        460
      ],
      "parameters": {
        "text": "=✔️ {{$node[\"Saludos-TelegramTrigger\"].json[\"message\"][\"new_chat_member\"][\"first_name\"]}}, ¡bienvenid@ a N8N en Españoll!  🙌",
        "chatId": "=@comunidadn8n",
        "additionalFields": {}
      },
      "credentials": {
        "telegramApi": "N8N Español - BOT"
      },
      "typeVersion": 1
    }
  ],
  "active": true,
  "settings": {},
  "connections": {
    "Saludos-IF": {
      "main": [
        [],
        [
          {
            "node": "S-Telegram2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Saludos-IF1": {
      "main": [
        [],
        [
          {
            "node": "S-Telegram",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Saludos-TelegramTrigger": {
      "main": [
        [
          {
            "node": "Saludos-IF1",
            "type": "main",
            "index": 0
          },
          {
            "node": "Saludos-IF",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2408"></a>

## Template 2408 - Rascunhos automáticos de resposta por IA

- **Nome:** Rascunhos automáticos de resposta por IA
- **Descrição:** Monitora emails recebidos, avalia se precisam de resposta e cria rascunhos de respostas gerados por IA dentro da mesma conversa.
- **Funcionalidade:** • Monitoramento de emails recebidos: verifica continuamente a caixa de entrada e ignora mensagens enviadas por si mesmo.
• Avaliação automática de necessidade de resposta: usa um modelo de linguagem para decidir se o email requer uma resposta (retorna true/false).
• Geração de rascunho de resposta por IA: cria respostas profissionais em tom business casual, mantendo a língua do email original e seguindo instruções específicas (iniciar com "Hello," e terminar com "Best,").
• Tratamento de perguntas de sim/não: quando apropriado, gera duas versões de resposta (afirmativa e negativa) separadas por um delimitador definido.
• Uso de placeholders: insere marcadores como "[YOUR_ANSWER_HERE]" quando a informação não está disponível.
• Criação de rascunho na conversa: salva a resposta como rascunho no mesmo thread do email, definindo destinatário e assunto (prefixado com "Re:") e formatando o corpo em HTML.
• Verificação periódica: executa checagens regulares (a cada minuto) para processar novos emails.
- **Ferramentas:** • Gmail: plataforma de email usada para receber mensagens e salvar rascunhos no mesmo encadeamento de conversa.
• OpenAI: serviços de modelos de linguagem (GPT) usados para avaliar se é necessária uma resposta e para gerar o texto do rascunho.

## Fluxo visual

```mermaid
flowchart LR
    N1["Gmail Trigger"]
    N2["If Needs Reply"]
    N3["JSON Parser"]
    N4["OpenAI Chat"]
    N5["Sticky Note"]
    N6["Sticky Note1"]
    N7["Sticky Note2"]
    N8["Sticky Note3"]
    N9["OpenAI Chat Model"]
    N10["Gmail - Create Draft"]
    N11["Assess if message needs a reply"]
    N12["Generate email reply"]

    N1 --> N11
    N2 --> N12
    N12 --> N10
    N11 --> N2
```

## Fluxo (.json) :

```json
{
  "id": "aOQANirVMuWrH0ZD",
  "meta": {
    "instanceId": "b78ce2d06ac74b90a581919cf44503cf07404c11eda5c3847597226683145618"
  },
  "name": "Gmail AI auto-responder: create draft replies to incoming emails",
  "tags": [],
  "nodes": [
    {
      "id": "2a9ff08f-919a-41a8-980b-8c2bca3059e4",
      "name": "Gmail Trigger",
      "type": "n8n-nodes-base.gmailTrigger",
      "position": [
        -332.809175564116,
        566.0845437534399
      ],
      "parameters": {
        "simple": false,
        "filters": {
          "q": "-from:me"
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
          "id": "ofvBTX8A0aWfQb2O",
          "name": "Gmail account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "3ef14615-0045-404f-a21b-2c65a52f4be8",
      "name": "If Needs Reply",
      "type": "n8n-nodes-base.if",
      "position": [
        240,
        560
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
              "id": "53849246-ad32-4845-9976-9f9688f5a6f2",
              "operator": {
                "type": "boolean",
                "operation": "true",
                "singleValue": true
              },
              "leftValue": "={{ $json.needsReply }}",
              "rightValue": "true"
            }
          ]
        }
      },
      "typeVersion": 2
    },
    {
      "id": "36968dd5-8d51-4184-a05a-587b6c95aa82",
      "name": "JSON Parser",
      "type": "@n8n/n8n-nodes-langchain.outputParserStructured",
      "position": [
        100,
        720
      ],
      "parameters": {
        "jsonSchema": "{\n \"type\": \"object\",\n \"properties\": {\n \"needsReply\": {\n \"type\": \"boolean\"\n }\n },\n \"required\": [\"needsReply\"]\n}\n"
      },
      "typeVersion": 1
    },
    {
      "id": "2a64dce8-e2f0-475e-a366-a02084293aad",
      "name": "OpenAI Chat",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        -92.809175564116,
        726.0845437534399
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
          "id": "13ffkrNMlQMfvbZy",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "be892ff8-0981-4b34-9c93-7674ddd90360",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -429.809175564116,
        461.08454375343996
      ],
      "parameters": {
        "width": 304.10628068244364,
        "height": 394.42512272977456,
        "content": "## When I receive an Email\n"
      },
      "typeVersion": 1
    },
    {
      "id": "9d92839a-9ff2-436c-8abb-2f43e07c1ace",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -112.809175564116,
        460.08454375343996
      ],
      "parameters": {
        "width": 556,
        "height": 397,
        "content": "## ... that Needs a Reply\n"
      },
      "typeVersion": 1
    },
    {
      "id": "3cd77609-684c-44e2-9cdc-9479cfd836bd",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        460,
        460
      ],
      "parameters": {
        "width": 333.19082443588354,
        "height": 400.08454375343996,
        "content": "## Generate a Reply"
      },
      "typeVersion": 1
    },
    {
      "id": "b123cf31-767d-48bb-a0ba-79a69f6da585",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        807.190824435884,
        461.08454375343996
      ],
      "parameters": {
        "width": 326,
        "height": 395,
        "content": "## ...as a Draft in the conversation"
      },
      "typeVersion": 1
    },
    {
      "id": "1a87c416-6b1c-4526-a2b6-20468c95ea0e",
      "name": "OpenAI Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        480,
        680
      ],
      "parameters": {
        "model": "gpt-4-turbo",
        "options": {}
      },
      "credentials": {
        "openAiApi": {
          "id": "13ffkrNMlQMfvbZy",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "84b4d516-252e-444e-b998-2d4aa0f89653",
      "name": "Gmail - Create Draft",
      "type": "n8n-nodes-base.gmail",
      "position": [
        900,
        560
      ],
      "parameters": {
        "message": "={{ $json.text.replace(/\\n/g, \"<br />\\n\") }}",
        "options": {
          "sendTo": "={{ $('Gmail Trigger').item.json.headers.from }}",
          "threadId": "={{ $('Gmail Trigger').item.json.threadId }}"
        },
        "subject": "=Re: {{ $('Gmail Trigger').item.json.headers.subject }}",
        "resource": "draft",
        "emailType": "html"
      },
      "credentials": {
        "gmailOAuth2": {
          "id": "ofvBTX8A0aWfQb2O",
          "name": "Gmail account"
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "86017ff4-9c57-4b2a-9cd9-f62571a05ffd",
      "name": "Assess if message needs a reply",
      "type": "@n8n/n8n-nodes-langchain.chainLlm",
      "position": [
        -92.809175564116,
        566.0845437534399
      ],
      "parameters": {
        "prompt": "=Subject: {{ $json.subject }}\nMessage:\n{{ $json.textAsHtml }} ",
        "messages": {
          "messageValues": [
            {
              "message": "Your task is to assess if the message requires a response. Return in JSON format true if it does, false otherwise.\nMarketing emails don't require a response."
            }
          ]
        }
      },
      "typeVersion": 1.3
    },
    {
      "id": "cab1e7e5-93dc-4850-a471-e285cdbe2058",
      "name": "Generate email reply",
      "type": "@n8n/n8n-nodes-langchain.chainLlm",
      "position": [
        500,
        520
      ],
      "parameters": {
        "text": "=Subject: {{ $('Gmail Trigger').item.json.subject }}\nMessage: {{ $('Gmail Trigger').item.json.textAsHtml }}",
        "messages": {
          "messageValues": [
            {
              "message": "You're a helpful personal assistant and your task is to draft replies on my behalf to my incoming emails. Whenever I provide some text from an email, return an appropriate draft reply for it and nothing else.\nEnsure that the reply is suitable for a professional email setting and addresses the topic in a clear, structured, and detailed manner.\nDo not make things up.\n\nDetailed instructions:\n- Be concise and maintain a business casual tone.\n- Start with \"Hello,\", and end with \"Best,\"\n- When replying to yes-no questions, draft 2 responses: one affirmative and one negative separated by \" - - - - - - - OR - - - - - - - \"\n- If you don't know an answer, you can leave placeholders like \"[YOUR_ANSWER_HERE]\".\n- Don't use any special formatting, only plain text.\n- Reply in the same language as the inbound email."
            }
          ]
        },
        "promptType": "define"
      },
      "typeVersion": 1.4
    }
  ],
  "active": true,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "c4448c34-1f75-4479-805e-20d8a69a7e00",
  "connections": {
    "JSON Parser": {
      "ai_outputParser": [
        [
          {
            "node": "Assess if message needs a reply",
            "type": "ai_outputParser",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Chat": {
      "ai_languageModel": [
        [
          {
            "node": "Assess if message needs a reply",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Gmail Trigger": {
      "main": [
        [
          {
            "node": "Assess if message needs a reply",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "If Needs Reply": {
      "main": [
        [
          {
            "node": "Generate email reply",
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
            "node": "Generate email reply",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Generate email reply": {
      "main": [
        [
          {
            "node": "Gmail - Create Draft",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Assess if message needs a reply": {
      "main": [
        [
          {
            "node": "If Needs Reply",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2410"></a>

## Template 2410 - Exportar objetos Zammad para Excel

- **Nome:** Exportar objetos Zammad para Excel
- **Descrição:** Este fluxo extrai usuários, papéis, grupos e organizações do Zammad, normaliza os registros e gera arquivos Excel separados com os dados exportados.
- **Funcionalidade:** • Gatilho manual de execução: permite iniciar o processo quando o usuário aciona o teste.
• Configuração de variáveis básicas: define a URL base do Zammad e a chave de API para autenticação.
• Recuperação de dados do Zammad: consulta e obtém todos os usuários, organizações, papéis (roles) e grupos via API.
• Normalização dos objetos: mapeia e padroniza campos para objetos universais de usuário, organização, papel e grupo.
• Filtragem opcional: possibilita aplicar condições para incluir ou excluir registros antes da exportação.
• Conversão para Excel: cria arquivos .xlsx separados (nomes personalizados) contendo Usuários, Organizações, Papéis e Grupos.
- **Ferramentas:** • Zammad API: plataforma de helpdesk usada para fornecer os dados de usuários, organizações, papéis e grupos via endpoints REST.
• Arquivo Excel (.xlsx): formato de saída utilizado para exportar e armazenar os dados de forma tabular.

## Fluxo visual

```mermaid
flowchart LR
    N1["When clicking ‘Test workflow’"]
    N2["Zammad Univeral User Object"]
    N3["Zammad Univeral Organization Object"]
    N4["Zammad Univeral Role Object"]
    N5["Get all Organizations"]
    N6["Get all Roles"]
    N7["Convert to Excel Organizations"]
    N8["Convert to Excel Roles"]
    N9["Convert to Excel Users"]
    N10["Get all Users"]
    N11["Zammad Univeral Group Object"]
    N12["Get all Groups"]
    N13["If"]
    N14["Basic Variables"]
    N15["Convert to Excel Groups"]
    N16["Filter Groups if needed"]
    N17["Filter Roles if needed"]
    N18["Filter Organizations if needed"]

    N13 --> N9
    N6 --> N4
    N10 --> N2
    N12 --> N11
    N14 --> N6
    N14 --> N12
    N5 --> N3
    N17 --> N8
    N16 --> N15
    N4 --> N17
    N2 --> N13
    N11 --> N16
    N18 --> N7
    N1 --> N10
    N1 --> N14
    N1 --> N5
    N3 --> N18
```

## Fluxo (.json) :

```json
{
  "id": "IXumIzS9WtPAhKFX",
  "meta": {
    "instanceId": "494d0146a0f47676ad70a44a32086b466621f62da855e3eaf0ee51dee1f76753",
    "templateCredsSetupCompleted": true
  },
  "name": "Export Zammad Objects Users, Roles, Groups and Organizations to Excel",
  "tags": [],
  "nodes": [
    {
      "id": "59b12a25-d90f-47f0-a043-a51f71f5761e",
      "name": "When clicking ‘Test workflow’",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        -120,
        -80
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "259acda6-75be-4011-b021-56321ab10478",
      "name": "Zammad Univeral User Object",
      "type": "n8n-nodes-base.set",
      "position": [
        600,
        -80
      ],
      "parameters": {
        "values": {
          "number": [
            {
              "name": "user_id",
              "value": "={{ $json.id }}"
            },
            {
              "name": "organization_id",
              "value": "={{ $json.organization_id }}"
            }
          ],
          "string": [
            {
              "name": "email",
              "value": "={{ $json.email }}"
            },
            {
              "name": "firstname",
              "value": "={{ $json.firstname }}"
            },
            {
              "name": "lastname",
              "value": "={{ $json.lastname }}"
            },
            {
              "name": "role_ids",
              "value": "={{ $json.role_ids.join() }}\n"
            },
            {
              "name": "groups",
              "value": "={{ $json.group_ids }}"
            }
          ]
        },
        "options": {},
        "keepOnlySet": true
      },
      "typeVersion": 1
    },
    {
      "id": "57c68cc2-f5d6-4425-9dc2-b2d6b21f0026",
      "name": "Zammad Univeral Organization Object",
      "type": "n8n-nodes-base.set",
      "position": [
        600,
        160
      ],
      "parameters": {
        "values": {
          "number": [
            {
              "name": "organization_id",
              "value": "={{ $json.id }}"
            },
            {
              "name": "name",
              "value": "={{ $json.name }}"
            }
          ]
        },
        "options": {},
        "keepOnlySet": true
      },
      "typeVersion": 1
    },
    {
      "id": "c40b275c-1d33-4604-8073-3651641c94ed",
      "name": "Zammad Univeral Role Object",
      "type": "n8n-nodes-base.set",
      "position": [
        600,
        400
      ],
      "parameters": {
        "values": {
          "number": [
            {
              "name": "role_id",
              "value": "={{ $json.id }}"
            },
            {
              "name": "name",
              "value": "={{ $json.name }}"
            }
          ]
        },
        "options": {},
        "keepOnlySet": true
      },
      "typeVersion": 1
    },
    {
      "id": "29a257db-955d-4ff3-a7bb-f9a888f96e78",
      "name": "Get all Organizations",
      "type": "n8n-nodes-base.zammad",
      "position": [
        340,
        160
      ],
      "parameters": {
        "resource": "organization",
        "operation": "getAll",
        "returnAll": true
      },
      "credentials": {
        "zammadTokenAuthApi": {
          "id": "fj5GuzcJuNLQeMxz",
          "name": "Zammad Token Auth account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "b4a9c2ca-b110-46ba-b5b9-2e8d8e357dfb",
      "name": "Get all Roles",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        340,
        400
      ],
      "parameters": {
        "url": "={{ $json.zammad_base_url }}/api/v1/roles",
        "options": {},
        "sendHeaders": true,
        "headerParameters": {
          "parameters": [
            {
              "name": "Authorization",
              "value": "=Bearer {{ $json.zammad_api_key }}"
            }
          ]
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "9f5049cc-37ca-4069-86a1-75dffa9c2c96",
      "name": "Convert to Excel Organizations",
      "type": "n8n-nodes-base.convertToFile",
      "position": [
        1320,
        140
      ],
      "parameters": {
        "options": {
          "fileName": "Zammad_Organizations.xlsx"
        },
        "operation": "xlsx"
      },
      "typeVersion": 1.1
    },
    {
      "id": "1a05b494-919c-4e53-8772-8c504e667f1c",
      "name": "Convert to Excel Roles",
      "type": "n8n-nodes-base.convertToFile",
      "position": [
        1340,
        380
      ],
      "parameters": {
        "options": {
          "fileName": "Zammad_Roles.xlsx"
        },
        "operation": "xlsx"
      },
      "typeVersion": 1.1
    },
    {
      "id": "f1160af5-fcee-421d-9ede-b6f56ac0ce8d",
      "name": "Convert to Excel Users",
      "type": "n8n-nodes-base.convertToFile",
      "position": [
        1300,
        -100
      ],
      "parameters": {
        "options": {
          "fileName": "Zammad_Users.xslx"
        },
        "operation": "xlsx"
      },
      "typeVersion": 1.1
    },
    {
      "id": "192c5342-5140-48f9-acb0-d14a41064fa3",
      "name": "Get all Users",
      "type": "n8n-nodes-base.zammad",
      "position": [
        340,
        -80
      ],
      "parameters": {
        "filters": {},
        "operation": "getAll",
        "returnAll": true
      },
      "credentials": {
        "zammadTokenAuthApi": {
          "id": "fj5GuzcJuNLQeMxz",
          "name": "Zammad Token Auth account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "ae687777-c1cb-4a23-ae1e-aa34febc27d6",
      "name": "Zammad Univeral Group Object",
      "type": "n8n-nodes-base.set",
      "position": [
        620,
        620
      ],
      "parameters": {
        "values": {
          "number": [
            {
              "name": "group_id",
              "value": "={{ $json.id }}"
            },
            {
              "name": "name",
              "value": "={{ $json.name }}"
            }
          ]
        },
        "options": {},
        "keepOnlySet": true
      },
      "typeVersion": 1
    },
    {
      "id": "0d38e0b3-1a59-4a8f-9a04-8526aba91fd5",
      "name": "Get all Groups",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        340,
        620
      ],
      "parameters": {
        "url": "={{ $json.zammad_base_url }}/api/v1/groups",
        "options": {},
        "sendHeaders": true,
        "headerParameters": {
          "parameters": [
            {
              "name": "Authorization",
              "value": "=Bearer {{ $json.zammad_api_key }}"
            }
          ]
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "e30bd0ad-9772-4af7-9012-99199fee65b2",
      "name": "If",
      "type": "n8n-nodes-base.if",
      "position": [
        900,
        -80
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
              "id": "0ca9d3a3-b726-4396-8cec-4a74c8e3949b",
              "operator": {
                "type": "object",
                "operation": "exists",
                "singleValue": true
              },
              "leftValue": "={{ $json }}",
              "rightValue": 1781
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "2a83536e-e250-425a-aac7-f26ede0caf54",
      "name": "Basic Variables",
      "type": "n8n-nodes-base.set",
      "position": [
        60,
        400
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "68b32087-5e23-4590-8042-0061234ce479",
              "name": "zammad_base_url",
              "type": "string",
              "value": "-put-your-zammad-base-url-"
            },
            {
              "id": "7db7572e-2524-4f2a-a1d6-b44330662c30",
              "name": "zammad_api_key",
              "type": "string",
              "value": "-put-your-api-key-"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "db6a3024-9778-4d1e-8b25-34f2ee3ec26f",
      "name": "Convert to Excel Groups",
      "type": "n8n-nodes-base.convertToFile",
      "position": [
        1340,
        600
      ],
      "parameters": {
        "options": {
          "fileName": "Zammad_Groups.xlsx"
        },
        "operation": "xlsx"
      },
      "typeVersion": 1.1
    },
    {
      "id": "bd191e0d-927d-44ca-afe6-fa6c7f3d59a2",
      "name": "Filter Groups if needed",
      "type": "n8n-nodes-base.if",
      "position": [
        900,
        620
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
              "id": "0ca9d3a3-b726-4396-8cec-4a74c8e3949b",
              "operator": {
                "type": "object",
                "operation": "exists",
                "singleValue": true
              },
              "leftValue": "={{ $json }}",
              "rightValue": {}
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "c7c7b6b4-7faa-48b4-b7d8-6782dd1e4187",
      "name": "Filter Roles if needed",
      "type": "n8n-nodes-base.if",
      "position": [
        900,
        400
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
              "id": "0ca9d3a3-b726-4396-8cec-4a74c8e3949b",
              "operator": {
                "type": "object",
                "operation": "exists",
                "singleValue": true
              },
              "leftValue": "={{ $json }}",
              "rightValue": 1781
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "a255bc7b-5d35-4671-852e-53f2b0980c26",
      "name": "Filter Organizations if needed",
      "type": "n8n-nodes-base.if",
      "position": [
        900,
        160
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
              "id": "0ca9d3a3-b726-4396-8cec-4a74c8e3949b",
              "operator": {
                "type": "object",
                "operation": "exists",
                "singleValue": true
              },
              "leftValue": "={{ $json }}",
              "rightValue": 1781
            }
          ]
        }
      },
      "typeVersion": 2.2
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "8282fc5a-1ed4-4730-8e08-3d9f279dc3b5",
  "connections": {
    "If": {
      "main": [
        [
          {
            "node": "Convert to Excel Users",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get all Roles": {
      "main": [
        [
          {
            "node": "Zammad Univeral Role Object",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get all Users": {
      "main": [
        [
          {
            "node": "Zammad Univeral User Object",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get all Groups": {
      "main": [
        [
          {
            "node": "Zammad Univeral Group Object",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Basic Variables": {
      "main": [
        [
          {
            "node": "Get all Roles",
            "type": "main",
            "index": 0
          },
          {
            "node": "Get all Groups",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get all Organizations": {
      "main": [
        [
          {
            "node": "Zammad Univeral Organization Object",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Filter Roles if needed": {
      "main": [
        [
          {
            "node": "Convert to Excel Roles",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Filter Groups if needed": {
      "main": [
        [
          {
            "node": "Convert to Excel Groups",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Zammad Univeral Role Object": {
      "main": [
        [
          {
            "node": "Filter Roles if needed",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Zammad Univeral User Object": {
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
    "Zammad Univeral Group Object": {
      "main": [
        [
          {
            "node": "Filter Groups if needed",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Filter Organizations if needed": {
      "main": [
        [
          {
            "node": "Convert to Excel Organizations",
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
            "node": "Get all Users",
            "type": "main",
            "index": 0
          },
          {
            "node": "Basic Variables",
            "type": "main",
            "index": 0
          },
          {
            "node": "Get all Organizations",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Zammad Univeral Organization Object": {
      "main": [
        [
          {
            "node": "Filter Organizations if needed",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2412"></a>

## Template 2412 - Exportar tickets do Linear para Google Sheets

- **Nome:** Exportar tickets do Linear para Google Sheets
- **Descrição:** Busca diariamente os tickets de um time no Linear, normaliza os dados e grava/atualiza-os em uma planilha do Google Sheets.
- **Funcionalidade:** • Agendamento diário: Executa o fluxo automaticamente em uma frequência diária.
• Consulta à API do Linear (GraphQL): Recupera issues filtradas por time, trazendo campos como id, título, prioridade, datas, estado, ciclo, estimate e labels.
• Paginação automática: Verifica pageInfo.hasNextPage e usa endCursor para obter todas as páginas de resultados.
• Separação de tickets: Divide a lista de issues em itens individuais para processamento item a item.
• Definição de campos personalizados: Preenche valores padrão (por exemplo estimate = 1) e transforma rótulos em string para facilitar a exportação.
• Normalização dos dados: Achata objetos aninhados em campos simples para facilitar filtragem e mapeamento na planilha.
• Gravação em planilha do Google: Insere ou atualiza linhas na planilha usando o campo id como chave de correspondência.
• Retentativa em falhas: Tenta novamente operações de gravação em caso de erro para aumentar confiabilidade.
- **Ferramentas:** • Linear API (GraphQL): Fonte dos tickets/issues do time, fornece dados detalhados via consultas GraphQL.
• Google Sheets: Destino para armazenamento e atualização dos tickets em formato de planilha.

## Fluxo visual

```mermaid
flowchart LR
    N1["Every day at 06:00"]
    N2["Get all your team's tickets"]
    N3["Sticky Note1"]
    N4["if has next page"]
    N5["Get end cursor"]
    N6["Get next page"]
    N7["Sticky Note"]
    N8["Split out the tickets"]
    N9["Sticky Note2"]
    N10["Set custom fields"]
    N11["Sticky Note3"]
    N12["Sticky Note4"]
    N13["Write tickets to Sheets"]
    N14["Flatten object to have simple fields to filter by"]

    N6 --> N4
    N6 --> N8
    N5 --> N6
    N4 --> N5
    N10 --> N14
    N1 --> N2
    N8 --> N10
    N2 --> N8
    N2 --> N4
    N14 --> N13
```

## Fluxo (.json) :

```json
{
  "nodes": [
    {
      "id": "58c69358-3d02-41c3-b50c-6e57452523a2",
      "name": "Every day at 06:00",
      "type": "n8n-nodes-base.scheduleTrigger",
      "position": [
        960,
        600
      ],
      "parameters": {
        "rule": {
          "interval": [
            {
              "triggerAtHour": 9
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "id": "0a388351-6aec-45c4-a142-e89b338be155",
      "name": "Get all your team's tickets",
      "type": "n8n-nodes-base.graphql",
      "position": [
        1200,
        600
      ],
      "parameters": {
        "query": "query ($filter: IssueFilter) {\n  issues(filter: $filter, first: 100) {\n    pageInfo {\n      hasNextPage\n      endCursor\n    }\n    nodes {\n      id\n      identifier\n      url\n      title\n      priorityLabel\n      createdAt\n      completedAt\n      state {\n        type\n        name\n      }\n      cycle {\n        number\n      }\n      estimate\n      labels { nodes { name } }\n    }\n  }\n}",
        "endpoint": "https://api.linear.app/graphql",
        "variables": "={\n  \"filter\": {\n    \"team\": {\n      \"name\":  {\n        \"eq\": \"Adore\"\n      }\n    }\n  }\n}",
        "requestFormat": "json",
        "authentication": "headerAuth"
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "QNQL42DMISvQl50S",
          "name": "Linear api "
        }
      },
      "typeVersion": 1
    },
    {
      "id": "91f29056-f934-4c15-8e98-2a202753971d",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1200,
        460
      ],
      "parameters": {
        "color": 7,
        "width": 256.14371825927645,
        "height": 100,
        "content": "👇🏽 Set your team name here in the filter. \n(Our team's name is Adore)"
      },
      "typeVersion": 1
    },
    {
      "id": "8efeb08c-fbba-4c07-9ef8-e22afa39f328",
      "name": "if has next page",
      "type": "n8n-nodes-base.if",
      "position": [
        1400,
        780
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
              "id": "f5ab21aa-b2e0-4885-9278-6756c2c544f9",
              "operator": {
                "type": "boolean",
                "operation": "true",
                "singleValue": true
              },
              "leftValue": "={{ $json.data.issues.pageInfo.hasNextPage }}",
              "rightValue": 0
            }
          ]
        }
      },
      "typeVersion": 2
    },
    {
      "id": "fdfba048-ae14-45fb-88be-e354d7003fdb",
      "name": "Get end cursor",
      "type": "n8n-nodes-base.set",
      "position": [
        1620,
        920
      ],
      "parameters": {
        "fields": {
          "values": [
            {
              "name": "after",
              "stringValue": "={{ $json.data.issues.pageInfo.endCursor }}"
            }
          ]
        },
        "include": "none",
        "options": {}
      },
      "typeVersion": 3.2
    },
    {
      "id": "db37b327-d939-4a8b-bd5c-ff99c2191a54",
      "name": "Get next page",
      "type": "n8n-nodes-base.graphql",
      "position": [
        1880,
        920
      ],
      "parameters": {
        "query": "=query ($filter: IssueFilter) {\n  issues(filter: $filter, first: 100, after: \"{{ $json.after }}\") {\n    nodes {\n      id\n      identifier\n      url\n      title\n      priorityLabel\n      createdAt\n      completedAt\n      state {\n        type\n        name\n      }\n      cycle {\n        number\n      }\n      estimate\n      labels { nodes { name } }\n    }\n    pageInfo {\n      hasNextPage\n      endCursor\n    }\n  }\n}",
        "endpoint": "https://api.linear.app/graphql",
        "variables": "={\n  \"filter\": {\n    \"team\": {\n      \"name\":  {\n        \"eq\": \"Adore\"\n      }\n    }\n  }\n}",
        "requestFormat": "json",
        "authentication": "headerAuth"
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "QNQL42DMISvQl50S",
          "name": "Linear api "
        }
      },
      "typeVersion": 1
    },
    {
      "id": "f7857473-966e-433e-a7d7-9c4e4bdb670a",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2060,
        940
      ],
      "parameters": {
        "color": 7,
        "width": 256.14371825927645,
        "height": 100,
        "content": "👈🏽 Set your team name here in the filter. \n(Our team's name is Adore)"
      },
      "typeVersion": 1
    },
    {
      "id": "75365be8-d111-4bc8-9da8-77e8d3a1de6c",
      "name": "Split out the tickets",
      "type": "n8n-nodes-base.splitOut",
      "position": [
        2020,
        600
      ],
      "parameters": {
        "options": {},
        "fieldToSplitOut": "data.issues.nodes"
      },
      "typeVersion": 1
    },
    {
      "id": "691a8299-9c96-4520-a56b-7edf3bee42b5",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2240,
        460
      ],
      "parameters": {
        "color": 7,
        "width": 256.14371825927645,
        "height": 100,
        "content": "👇🏽 Adjust any custom fields. Here we set labels and default estimate of 1"
      },
      "typeVersion": 1
    },
    {
      "id": "4ff13ada-6534-4171-8704-4917b247727d",
      "name": "Set custom fields",
      "type": "n8n-nodes-base.set",
      "position": [
        2240,
        600
      ],
      "parameters": {
        "fields": {
          "values": [
            {
              "name": "estimate",
              "type": "numberValue",
              "numberValue": "={{ $json.estimate ?? 1 }}"
            },
            {
              "name": "labels",
              "stringValue": "={{ $json.labels.nodes.map((label) => label.name).toString() }}"
            }
          ]
        },
        "options": {}
      },
      "typeVersion": 3.2
    },
    {
      "id": "02577d21-656e-425b-9924-37a34c822fe8",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        740,
        300
      ],
      "parameters": {
        "color": 5,
        "width": 403.45318928152614,
        "height": 280.9004675550071,
        "content": "### 👨‍🎤 Setup\n1. Add Linear API header key\n2. Add Google sheets creds\n3. Update which teams to get tickets from in Graphql Nodes\n4. Update which Google Sheets page to write all the tickets to. \n **You only need to add one column, id. Google Sheets node in automatic mapping mode will handle adding the rest of the columns.**\n5. Set any custom data on each ticket\n6. Activate workflow 🚀"
      },
      "typeVersion": 1
    },
    {
      "id": "6344a764-20f0-4f46-bdc8-1599c2f9ba95",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2700,
        780
      ],
      "parameters": {
        "color": 7,
        "width": 256.14371825927645,
        "height": 100,
        "content": "👆🏽 Update which Google sheet to write to"
      },
      "typeVersion": 1
    },
    {
      "id": "ba08e0c7-1607-4bcd-8b37-99a6145b0cba",
      "name": "Write tickets to Sheets",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        2720,
        600
      ],
      "parameters": {
        "columns": {
          "value": {},
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
            }
          ],
          "mappingMode": "autoMapInputData",
          "matchingColumns": [
            "id"
          ]
        },
        "options": {},
        "operation": "appendOrUpdate",
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": 2072772685,
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1pQxSIZ2dSoA8Fmr3B4EId9VOQXH1hVuOZgCHxcaKN7k/edit#gid=2072772685",
          "cachedResultName": "Sheet2"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "1pQxSIZ2dSoA8Fmr3B4EId9VOQXH1hVuOZgCHxcaKN7k",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1pQxSIZ2dSoA8Fmr3B4EId9VOQXH1hVuOZgCHxcaKN7k/edit?usp=drivesdk",
          "cachedResultName": "Adore tickets"
        }
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "xNiEr671wxZVfjs6",
          "name": "Google Sheets account 3"
        }
      },
      "retryOnFail": true,
      "typeVersion": 4.2,
      "waitBetweenTries": 5000
    },
    {
      "id": "df3ae898-1f09-4be3-a96a-f1f9cba58730",
      "name": "Flatten object to have simple fields to filter by",
      "type": "n8n-nodes-base.code",
      "position": [
        2480,
        600
      ],
      "parameters": {
        "mode": "runOnceForEachItem",
        "jsCode": "function flattenObject(ob) {\n    var toReturn = {};\n\n    for (var i in ob) {\n        if (!ob.hasOwnProperty(i)) continue;\n\n        if ((typeof ob[i]) == 'object' && ob[i] !== null) {\n            var flatObject = flattenObject(ob[i]);\n            for (var x in flatObject) {\n                if (!flatObject.hasOwnProperty(x)) continue;\n\n                toReturn[i + '.' + x] = flatObject[x];\n            }\n        } else {\n            toReturn[i] = ob[i];\n        }\n    }\n    return toReturn;\n}\n\nreturn flattenObject($input.item.json);"
      },
      "typeVersion": 2
    }
  ],
  "pinData": {},
  "connections": {
    "Get next page": {
      "main": [
        [
          {
            "node": "if has next page",
            "type": "main",
            "index": 0
          },
          {
            "node": "Split out the tickets",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get end cursor": {
      "main": [
        [
          {
            "node": "Get next page",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "if has next page": {
      "main": [
        [
          {
            "node": "Get end cursor",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set custom fields": {
      "main": [
        [
          {
            "node": "Flatten object to have simple fields to filter by",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Every day at 06:00": {
      "main": [
        [
          {
            "node": "Get all your team's tickets",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Split out the tickets": {
      "main": [
        [
          {
            "node": "Set custom fields",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get all your team's tickets": {
      "main": [
        [
          {
            "node": "Split out the tickets",
            "type": "main",
            "index": 0
          },
          {
            "node": "if has next page",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Flatten object to have simple fields to filter by": {
      "main": [
        [
          {
            "node": "Write tickets to Sheets",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2414"></a>

## Template 2414 - Servidor MCP para busca e leitura de arquivos no Google Drive

- **Nome:** Servidor MCP para busca e leitura de arquivos no Google Drive
- **Descrição:** Fluxo que expõe um servidor MCP para permitir que clientes pesquisem, baixem e obtenham o conteúdo de arquivos armazenados no Google Drive, convertendo binários em texto e oferecendo análises multimodais quando necessário.
- **Funcionalidade:** • Receber requisições MCP: Ativa um endpoint MCP para aceitar comandos de clientes/agents.
• Pesquisa de arquivos no Drive: Permite buscar arquivos por query e limitar resultados.
• Download de arquivos alvo: Baixa arquivos especificados (por ID) do Google Drive.
• Conversão automática de formatos do Drive: Converte documentos e apresentações (ex.: Google Docs/Slides) para formatos textuais ou PDF.
• Detecção de tipo de arquivo: Classifica arquivos em PDF, CSV, imagem, áudio ou vídeo para processamento adequado.
• Extração de texto de PDFs: Extrai e retorna o texto contido em arquivos PDF.
• Parsing de CSVs: Converte linhas e células de CSV em texto estruturado para resposta.
• Análise de imagens multimodal: Usa modelo de IA para descrever ou extrair informações de imagens quando aplicável.
• Transcrição de áudio: Converte áudio para texto usando serviço de transcrição.
• Resposta textual ao cliente MCP: Garante que todas as saídas para o cliente sejam em formato de texto legível.
• Integração com workflows internos: Permite execução por outros fluxos fornecendo inputs como operation, folderId e fileId.
• Mensagem de segurança: Recomenda ativar autenticação no servidor MCP antes de produção.
- **Ferramentas:** • Google Drive: Armazenamento e fonte dos arquivos a serem pesquisados e baixados.
• Serviço de modelos multimodais (ex.: OpenAI): Análise de imagens e transcrição/entendimento de áudio.
• Clientes/agents MCP (ex.: Claude Desktop): Conectam-se ao servidor MCP para enviar comandos e receber respostas.



## Fluxo visual

```mermaid
flowchart LR
    N1["Sticky Note"]
    N2["Sticky Note3"]
    N3["When Executed by Another Workflow"]
    N4["Google Drive MCP Server"]
    N5["Sticky Note1"]
    N6["Download File1"]
    N7["FileType"]
    N8["Operation"]
    N9["Extract from PDF"]
    N10["Extract from CSV"]
    N11["Get PDF Response"]
    N12["Get CSV Response"]
    N13["Read File From GDrive"]
    N14["Search Files from Gdrive"]
    N15["Analyse Image"]
    N16["Transcribe Audio"]
    N17["Sticky Note2"]

    N7 --> N9
    N7 --> N10
    N7 --> N15
    N7 --> N16
    N8 --> N6
    N6 --> N7
    N10 --> N12
    N9 --> N11
    N3 --> N8
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
      "id": "fb5b682b-5e30-497e-b465-c3369bb3c2e3",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -32,
        -20
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
      "id": "cfc2c7f1-a6ee-42a9-b955-e5bce012b6e1",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -40,
        -160
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
      "id": "79586d35-0582-4da8-91da-5bc8451c2089",
      "name": "When Executed by Another Workflow",
      "type": "n8n-nodes-base.executeWorkflowTrigger",
      "position": [
        800,
        360
      ],
      "parameters": {
        "workflowInputs": {
          "values": [
            {
              "name": "operation"
            },
            {
              "name": "folderId"
            },
            {
              "name": "fileId"
            }
          ]
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "02aee033-58e8-4f33-a18d-b872840e81d8",
      "name": "Google Drive MCP Server",
      "type": "@n8n/n8n-nodes-langchain.mcpTrigger",
      "position": [
        160,
        160
      ],
      "webhookId": "a289c719-fb71-4b08-97c6-79d12645dc7e",
      "parameters": {
        "path": "a289c719-fb71-4b08-97c6-79d12645dc7e"
      },
      "typeVersion": 1
    },
    {
      "id": "e0e50653-d98a-4ad4-a2ed-e1b73332c380",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        680,
        -20
      ],
      "parameters": {
        "color": 7,
        "width": 1340,
        "height": 860,
        "content": "## 2. Handle Multiple Binary Formats via Conversion and AI\n[Read more about the PostgreSQL Node](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postgres/)\n\nMCP clients (or rather, the AI agents) still expect and require text responses from our MCP server.\nN8N can provide the right conversion tools to parse most text formats such as PDF, CSV and XML.\nFor images, audio and video, consider using multimodal LLMs to describe or transcribe the file instead."
      },
      "typeVersion": 1
    },
    {
      "id": "6be1ff49-5edc-42d2-87de-09d207ee7733",
      "name": "Download File1",
      "type": "n8n-nodes-base.googleDrive",
      "position": [
        1160,
        360
      ],
      "parameters": {
        "fileId": {
          "__rl": true,
          "mode": "id",
          "value": "={{ $json.fileId }}"
        },
        "options": {
          "googleFileConversion": {
            "conversion": {
              "docsToFormat": "text/plain",
              "slidesToFormat": "application/pdf"
            }
          }
        },
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
      "id": "91b0a549-0494-48a1-bdf3-6c2b91409d01",
      "name": "FileType",
      "type": "n8n-nodes-base.switch",
      "position": [
        1340,
        320
      ],
      "parameters": {
        "rules": {
          "values": [
            {
              "outputKey": "pdf",
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
                    "id": "7b6958ce-d553-4379-a5d6-743f39b342d0",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $binary.data.mimeType }}",
                    "rightValue": "application/pdf"
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "csv",
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
                    "id": "d0816a37-ac06-49e3-8d63-17fcd061e33f",
                    "operator": {
                      "name": "filter.operator.equals",
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $binary.data.mimeType }}",
                    "rightValue": "text/csv"
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "image",
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
                    "id": "589540e1-1439-41e3-ba89-b27f5e936190",
                    "operator": {
                      "type": "boolean",
                      "operation": "true",
                      "singleValue": true
                    },
                    "leftValue": "={{\n[\n  'image/jpeg',\n  'image/jpg',\n  'image/png',\n  'image/gif'\n].some(mimeType => $binary.data.mimeType === mimeType)\n}}",
                    "rightValue": ""
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "audio",
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
                    "id": "b8fc61a1-6057-4db3-960e-b8ddcbdd0f31",
                    "operator": {
                      "type": "string",
                      "operation": "contains"
                    },
                    "leftValue": "={{ $binary.data.mimeType }}",
                    "rightValue": "audio"
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "video",
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
                    "id": "959d65a6-372f-4978-b2d1-f28aa1e372c6",
                    "operator": {
                      "type": "string",
                      "operation": "contains"
                    },
                    "leftValue": "={{ $binary.data.mimeType }}",
                    "rightValue": "video"
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
      "id": "d88ed202-1121-41db-859d-b31d53d46292",
      "name": "Operation",
      "type": "n8n-nodes-base.switch",
      "position": [
        980,
        360
      ],
      "parameters": {
        "rules": {
          "values": [
            {
              "outputKey": "ReadFile",
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
                    "id": "b03bb746-dc4e-469c-b8e6-a34c0aa8d0a6",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $json.operation }}",
                    "rightValue": "readFile"
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
      "id": "7e8791e6-24c2-441a-8efb-7f4375f2519b",
      "name": "Extract from PDF",
      "type": "n8n-nodes-base.extractFromFile",
      "position": [
        1620,
        80
      ],
      "parameters": {
        "options": {},
        "operation": "pdf"
      },
      "typeVersion": 1
    },
    {
      "id": "2b33623c-cea4-4a83-80ef-f852b9a3d126",
      "name": "Extract from CSV",
      "type": "n8n-nodes-base.extractFromFile",
      "position": [
        1620,
        260
      ],
      "parameters": {
        "options": {
          "encoding": "utf-8",
          "headerRow": false,
          "relaxQuotes": true,
          "includeEmptyCells": true
        }
      },
      "typeVersion": 1
    },
    {
      "id": "6ca2542d-225e-4a65-b5ce-3edafb11379c",
      "name": "Get PDF Response",
      "type": "n8n-nodes-base.set",
      "position": [
        1780,
        80
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "a481cde3-b8ec-4d97-aa13-4668bd66c24d",
              "name": "response",
              "type": "string",
              "value": "={{ $json.text }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "3d1c4aa6-cac1-4957-ab7e-3134368e4b53",
      "name": "Get CSV Response",
      "type": "n8n-nodes-base.set",
      "position": [
        1780,
        260
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "a481cde3-b8ec-4d97-aa13-4668bd66c24d",
              "name": "response",
              "type": "string",
              "value": "={{\n$input.all()\n  .map(item => item.json.row.map(cell => `\"${cell}\"`).join(','))\n  .join('\\n')\n}}"
            }
          ]
        }
      },
      "executeOnce": true,
      "typeVersion": 3.4
    },
    {
      "id": "141444f9-e937-41f9-ab97-09624646ddba",
      "name": "Read File From GDrive",
      "type": "@n8n/n8n-nodes-langchain.toolWorkflow",
      "position": [
        400,
        380
      ],
      "parameters": {
        "name": "ReadFile",
        "workflowId": {
          "__rl": true,
          "mode": "id",
          "value": "={{ $workflow.id }}"
        },
        "description": "Call this tool to download and read the contents of a file within google drive.",
        "workflowInputs": {
          "value": {
            "fileId": "={{ /*n8n-auto-generated-fromAI-override*/ $fromAI('fileId', ``, 'string') }}",
            "folderId": "={{ /*n8n-auto-generated-fromAI-override*/ $fromAI('folderId', ``, 'string') }}",
            "operation": "readFile"
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
              "id": "folderId",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "folderId",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "fileId",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "fileId",
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
      "id": "b5851527-0b57-447b-ac8c-10408a684862",
      "name": "Search Files from Gdrive",
      "type": "n8n-nodes-base.googleDriveTool",
      "position": [
        240,
        380
      ],
      "parameters": {
        "limit": 10,
        "filter": {
          "driveId": {
            "mode": "list",
            "value": "My Drive"
          },
          "whatToSearch": "files"
        },
        "options": {},
        "resource": "fileFolder",
        "queryString": "={{ /*n8n-auto-generated-fromAI-override*/ $fromAI('Search_Query', ``, 'string') }}"
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
      "id": "98197c91-c7e9-4fbb-a2b1-c16c873fa0a1",
      "name": "Analyse Image",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "position": [
        1620,
        440
      ],
      "parameters": {
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
          "id": "8gccIjcuf3gvaoEr",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1.8
    },
    {
      "id": "b44a787a-c670-47e1-b87e-d880425ce610",
      "name": "Transcribe Audio",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "position": [
        1620,
        620
      ],
      "parameters": {
        "options": {},
        "resource": "audio",
        "operation": "transcribe"
      },
      "credentials": {
        "openAiApi": {
          "id": "8gccIjcuf3gvaoEr",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1.8
    },
    {
      "id": "1e1a358d-769e-48c9-bf27-6a3cfaaacb14",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -500,
        -420
      ],
      "parameters": {
        "width": 440,
        "height": 1060,
        "content": "## Try It Out!\n### This n8n demonstrates how to build a simple Google Drive MCP server to search and get contents of files from Google Drive.\n\nThis MCP example is based off an official MCP reference implementation which can be found here -https://github.com/modelcontextprotocol/servers/tree/main/src/gdrive\n\n### How it works\n* A MCP server trigger is used and connected to 1x Google Drive tool and 1x Custom Workflow tool.\n* The Google Drive tool is set to perform a search on files within our Google Drive folder.\n* The Custom Workflow tool downloads target files found in our drive and converts the binaries to their text representation. Eg. PDFs have only their text contents extracted and returned to the MCP client.\n\n### How to use\n* This Google Drive MCP server allows any compatible MCP client to manage a person or shared Google Drive. Simple select a drive or for better control, specify a folder within the drive to scope the operations to.\n* Connect your MCP client by following the n8n guidelines here - https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger/#integrating-with-claude-desktop\n* Try the following queries in your MCP client:\n  * \"Please help me search for last month's expense reports.\"\n * \"What does the company policy document say about cancellations and refunds?\"\n\n### Requirements\n* Google Drive for documents.\n* OpenAI for image and audio understanding.\n* MCP Client or Agent for usage such as Claude Desktop - https://claude.ai/download\n\n### Customising this workflow\n* Add additional capabilities such as renaming, moving and/or deleting files.\n* Remember to set the MCP server to require credentials before going to production and sharing this MCP server with others!"
      },
      "typeVersion": 1
    }
  ],
  "pinData": {},
  "connections": {
    "FileType": {
      "main": [
        [
          {
            "node": "Extract from PDF",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Extract from CSV",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Analyse Image",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Transcribe Audio",
            "type": "main",
            "index": 0
          }
        ],
        []
      ]
    },
    "Operation": {
      "main": [
        [
          {
            "node": "Download File1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Download File1": {
      "main": [
        [
          {
            "node": "FileType",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract from CSV": {
      "main": [
        [
          {
            "node": "Get CSV Response",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract from PDF": {
      "main": [
        [
          {
            "node": "Get PDF Response",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Read File From GDrive": {
      "ai_tool": [
        [
          {
            "node": "Google Drive MCP Server",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Search Files from Gdrive": {
      "ai_tool": [
        [
          {
            "node": "Google Drive MCP Server",
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

<a id="template-2415"></a>

## Template 2415 - Sincronizar planilha de livros semanalmente

- **Nome:** Sincronizar planilha de livros semanalmente
- **Descrição:** A cada semana, o fluxo lê dados de uma planilha e insere registros na tabela de livros do banco de dados.
- **Funcionalidade:** • Agendamento semanal: Dispara o processo automaticamente uma vez por semana às 05:00.
• Leitura de planilha: Lê os dados de uma planilha online especificada como fonte de itens a importar.
• Inserção no banco de dados: Insere os registros lidos na tabela de livros, mapeando colunas como título e preço.
• Inserção com prioridade e ignorar erros de duplicidade: Executa inserções com prioridade baixa e ignora conflitos ou duplicatas conforme configuração.
- **Ferramentas:** • Google Sheets: Planilha online utilizada como fonte dos dados dos livros.
• MySQL: Banco de dados relacional onde os registros de livros são inseridos.



## Fluxo visual

```mermaid
flowchart LR
    N1["Cron"]
    N2["MySQL - insert"]
    N3["Google Sheets - read"]

    N1 --> N3
    N3 --> N2
```

## Fluxo (.json) :

```json
{
  "nodes": [
    {
      "name": "Cron",
      "type": "n8n-nodes-base.cron",
      "position": [
        100,
        160
      ],
      "parameters": {
        "triggerTimes": {
          "item": [
            {
              "hour": 5,
              "mode": "everyWeek"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "MySQL - insert",
      "type": "n8n-nodes-base.mySql",
      "position": [
        500,
        160
      ],
      "parameters": {
        "table": "books",
        "columns": "title, price",
        "options": {
          "ignore": true,
          "priority": "LOW_PRIORITY"
        }
      },
      "credentials": {
        "mySql": {
          "id": "82",
          "name": "MySQL account"
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Google Sheets - read",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        300,
        160
      ],
      "parameters": {
        "options": {},
        "sheetId": "qwertz",
        "authentication": "oAuth2"
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "2",
          "name": "google_sheets_oauth"
        }
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Cron": {
      "main": [
        [
          {
            "node": "Google Sheets - read",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Sheets - read": {
      "main": [
        [
          {
            "node": "MySQL - insert",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2416"></a>

## Template 2416 - Detecção e resposta a stickers do Telegram

- **Nome:** Detecção e resposta a stickers do Telegram
- **Descrição:** Escuta mensagens recebidas por um bot do Telegram e responde com informações do sticker caso a mensagem contenha um; caso contrário, informa que nenhuma figurinha foi encontrada.
- **Funcionalidade:** • Recepção de mensagens do Telegram: Inicia o fluxo ao receber mensagens enviadas ao bot.
• Verificação de presença de sticker: Avalia se a mensagem recebida contém um sticker.
• Resposta com detalhes do sticker: Quando há sticker, envia uma mensagem personalizada contendo o primeiro nome do remetente, o ID do arquivo do sticker e o nome do conjunto de stickers.
• Notificação quando não há sticker: Quando não há sticker na mensagem, envia uma mensagem informando a ausência de sticker.
• Uso do identificador do chat: Obtém o ID do chat da mensagem para encaminhar a resposta ao usuário correto.
- **Ferramentas:** • Telegram Bot API: Plataforma utilizada para receber mensagens do usuário e enviar respostas, incluindo envio de texto e leitura de metadados de stickers (file_id, set_name).

## Fluxo visual

```mermaid
flowchart LR
    N1["Telegram Trigger"]
    N2["Return Sticker"]
    N3["Return no Sticker found"]
    N4["Look for Sticker"]

    N4 --> N2
    N4 --> N3
    N1 --> N4
```

## Fluxo (.json) :

```json
{
  "nodes": [
    {
      "name": "Telegram Trigger",
      "type": "n8n-nodes-base.telegramTrigger",
      "position": [
        450,
        300
      ],
      "parameters": {
        "updates": [
          "message"
        ]
      },
      "credentials": {
        "telegramApi": ""
      },
      "typeVersion": 1
    },
    {
      "name": "Return Sticker",
      "type": "n8n-nodes-base.telegram",
      "position": [
        850,
        200
      ],
      "parameters": {
        "text": "=Hi {{$node[\"Look for Sticker\"].data[\"message\"][\"from\"][\"first_name\"]}}!\nThe ID of the sticker is: {{$node[\"Look for Sticker\"].data[\"message\"][\"sticker\"][\"file_id\"]}}\nIt is part of the sticker-set: {{$node[\"Look for Sticker\"].data[\"message\"][\"sticker\"][\"set_name\"]}}",
        "chatId": "={{$node[\"Look for Sticker\"].data[\"message\"][\"chat\"][\"id\"]}}",
        "additionalFields": {}
      },
      "credentials": {
        "telegramApi": ""
      },
      "typeVersion": 1
    },
    {
      "name": "Return no Sticker found",
      "type": "n8n-nodes-base.telegram",
      "position": [
        850,
        400
      ],
      "parameters": {
        "text": "=Hi {{$node[\"Look for Sticker\"].data[\"message\"][\"from\"][\"first_name\"]}}!\nYour message did not contain any sticker.",
        "chatId": "={{$node[\"Look for Sticker\"].data[\"message\"][\"chat\"][\"id\"]}}",
        "additionalFields": {}
      },
      "credentials": {
        "telegramApi": "n8nTestBot"
      },
      "typeVersion": 1
    },
    {
      "name": "Look for Sticker",
      "type": "n8n-nodes-base.if",
      "position": [
        650,
        300
      ],
      "parameters": {
        "conditions": {
          "boolean": [
            {
              "value1": "={{!!$node[\"Telegram Trigger\"].data[\"message\"][\"sticker\"]}}",
              "value2": true
            }
          ]
        }
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Look for Sticker": {
      "main": [
        [
          {
            "node": "Return Sticker",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Return no Sticker found",
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
            "node": "Look for Sticker",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2417"></a>

## Template 2417 - Exportar planilha Google para HTML via webhook

- **Nome:** Exportar planilha Google para HTML via webhook
- **Descrição:** Recebe uma requisição HTTP, lê uma planilha do Google Sheets e converte os dados em um arquivo HTML retornado como resposta.
- **Funcionalidade:** • Recepção de requisição HTTP: Inicia o fluxo ao receber uma chamada no endpoint configurado.
• Leitura de planilha do Google Sheets: Acessa uma planilha específica usando credenciais para obter os dados.
• Conversão para HTML: Converte os dados da planilha em um arquivo no formato HTML.
• Retorno do arquivo ao solicitante: Envia o arquivo HTML gerado como resposta à requisição que disparou o fluxo.
- **Ferramentas:** • Google Sheets: Armazenamento de dados em planilha, fonte dos dados que serão exportados.
• Endpoint HTTP (webhook): Ponto de entrada que recebe as requisições que disparam a automação.
• Armazenamento temporário de arquivos no servidor: Geração e retenção do arquivo HTML para envio como resposta.

## Fluxo visual

```mermaid
flowchart LR
    N1["Read from Google Sheets"]
    N2["Create HTML file"]
    N3["Webhook"]

    N3 --> N1
    N1 --> N2
```

## Fluxo (.json) :

```json
{
  "nodes": [
    {
      "name": "Read from Google Sheets",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        460,
        300
      ],
      "parameters": {
        "options": {},
        "sheetId": "1uFISwZJ1rzkOnOSNocX-_n-ASSAznWGdpcPK3_KCvVo"
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "19",
          "name": "Tom's Google Sheets account"
        }
      },
      "typeVersion": 2
    },
    {
      "name": "Create HTML file",
      "type": "n8n-nodes-base.spreadsheetFile",
      "position": [
        680,
        300
      ],
      "parameters": {
        "options": {},
        "operation": "toFile",
        "fileFormat": "html"
      },
      "typeVersion": 1
    },
    {
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "position": [
        240,
        300
      ],
      "webhookId": "08569699-fea2-4856-80aa-fe878ab9dd4f",
      "parameters": {
        "path": "08569699-fea2-4856-80aa-fe878ab9dd4f",
        "options": {},
        "responseData": "firstEntryBinary",
        "responseMode": "lastNode"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Read from Google Sheets",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Read from Google Sheets": {
      "main": [
        [
          {
            "node": "Create HTML file",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2420"></a>

## Template 2420 - Responder webhook de chamada Retell com variáveis dinâmicas

- **Nome:** Responder webhook de chamada Retell com variáveis dinâmicas
- **Descrição:** Recebe o webhook de uma chamada inbound da Retell, busca o usuário por número de telefone em uma planilha e retorna as variáveis dinâmicas formatadas para a Retell.
- **Funcionalidade:** • Receber webhook com validação de IP: expõe um endpoint POST em um caminho configurável e aceita apenas chamadas do IP permitido.
• Extrair dados do payload: obtém o número de telefone e outros campos do corpo da requisição recebida.
• Buscar usuário por telefone: consulta uma planilha para localizar a linha cujo campo "Phone Number" corresponde ao número recebido.
• Mapear colunas para variáveis dinâmicas: converte colunas como First Name, Last name, E-Mail, User Variable 1/2 em chaves de dynamic_variables.
• Retornar resposta JSON compatível com Retell: envia um JSON estruturado contendo dynamic_variables para que a plataforma substitua as variáveis no agente.
• Configurável: permite alterar o caminho do webhook, a planilha e os nomes das variáveis conforme necessário.
- **Ferramentas:** • Retell: plataforma de agentes de voz que envia webhooks de chamadas inbound e consome variáveis dinâmicas via JSON.
• Google Sheets: planilha usada como banco de dados de usuários, consultada por número de telefone para obter os campos que alimentam as variáveis dinâmicas.

## Fluxo visual

```mermaid
flowchart LR
    N1["Webhook"]
    N2["Respond to Webhook"]
    N3["Get user in DB by Phone Number"]
    N4["Sticky Note1"]
    N5["Sticky Note3"]
    N6["Sticky Note"]
    N7["Sticky Note2"]

    N1 --> N3
    N3 --> N2
```

## Fluxo (.json) :

```json
{
  "meta": {
    "instanceId": "f4f5d195bb2162a0972f737368404b18be694648d365d6c6771d7b4909d28167",
    "templateCredsSetupCompleted": true
  },
  "nodes": [
    {
      "id": "9a8d7d07-a1b3-4bca-8e77-10da3a2abc45",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "position": [
        -160,
        0
      ],
      "webhookId": "7f35a3a8-54c3-49d7-879d-6c3429f0e5da",
      "parameters": {
        "path": "retell-dynamic-variables",
        "options": {
          "ipWhitelist": "100.20.5.228"
        },
        "httpMethod": "POST",
        "responseMode": "responseNode"
      },
      "typeVersion": 2
    },
    {
      "id": "79e77d72-6e13-428c-ad10-58e6930e2d90",
      "name": "Respond to Webhook",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        440,
        0
      ],
      "parameters": {
        "options": {},
        "respondWith": "json",
        "responseBody": "={\n  \"call_inbound\": {\n    \"dynamic_variables\": {\n        \"first_name\": \"{{ $json['First Name'] }}\",\n        \"last_name\": \"{{ $json['Last name'] }}\",\n        \"email\": \"{{ $json['E-Mail'] }}\",\n        \"variable_1\": \"{{ $json['User Variable 1'] }}\",\n        \"variable_2\": \"{{ $json['User Variable 2']}}\"\n    },\n    \"metadata\": {\n    }\n  }\n}"
      },
      "typeVersion": 1.1
    },
    {
      "id": "10919781-9750-417f-bba6-293bf99dbc3e",
      "name": "Get user in DB by Phone Number",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        140,
        0
      ],
      "parameters": {
        "options": {},
        "filtersUI": {
          "values": [
            {
              "lookupValue": "={{ $json.body.call_inbound.from_number }}",
              "lookupColumn": "Phone Number"
            }
          ]
        },
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": "gid=0",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1TYgk8PK5w2l8Q5NtepdyLvgtuHXBHcODy-2hXOPP6AU/edit#gid=0",
          "cachedResultName": "Users"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "1TYgk8PK5w2l8Q5NtepdyLvgtuHXBHcODy-2hXOPP6AU",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1TYgk8PK5w2l8Q5NtepdyLvgtuHXBHcODy-2hXOPP6AU/edit?usp=drivesdk",
          "cachedResultName": "Retell sample UserDB"
        }
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "ufBkeygvc1l17m5N",
          "name": "Baptiste AS - Google Sheets account"
        }
      },
      "typeVersion": 4.5
    },
    {
      "id": "de9a2ff5-690e-4e1e-ab5c-5a8825986871",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -880,
        -440
      ],
      "parameters": {
        "color": 7,
        "width": 601,
        "height": 1105,
        "content": "## Handle Retell's Inbound call webhooks\n\n## Overview\n- This workflow provides Retell agent builders with a simple way to populate [dynamic variables](https://docs.retellai.com/build/dynamic-variables) using n8n.\n- The workflow fetches user information from a Google Sheet based on the phone number and sends it back to Retell.\n- It is based on Retell's [Inbound Webhook Call](https://docs.retellai.com/features/inbound-call-webhook).\n- Retell is a service that lets you create Voice Agents that handle voice calls simply, based on a prompt or using a conversational flow builder.\n\n## Prerequisites\n- Have a [Retell AI Account](https://www.retellai.com/)\n- [Create a Retell agent](https://docs.retellai.com/get-started/quick-start)\n- [Purchase a phone number](https://docs.retellai.com/deploy/purchase-number) and associate it with your agent\n- Create a Google Sheets - for example, [make a copy of this one](https://docs.google.com/spreadsheets/d/1TYgk8PK5w2l8Q5NtepdyLvgtuHXBHcODy-2hXOPP6AU/edit?usp=sharing).\n- Your Google Sheet must have at least one column with the phone number. The remaining columns will be used to populate your Retell agent’s dynamic variables.\n- All fields are returned as strings to Retell (variables are replaced as text)\n\n## How it works\n- The webhook call is received from Retell. We filter the call using their whitelisted IP address.\n- It extracts data from the webhook call and uses it to retrieve the user from Google Sheets.\n- It formats the data in the response to match Retell's expected format.\n- Retell uses this data to replace [dynamic variables](https://docs.retellai.com/build/dynamic-variables#dynamic-variables) in the prompts.\n\n\n## How to use it\nSee the description for screenshots!\n- Set the webhook name (keep it as POST).\n- Copy the Webhook URL (e.g., `https://your-instance.app.n8n.cloud/webhook/retell-dynamic-variables`) and paste it into Retell's interface. Navigate to \"Phone Numbers\", click on the phone number, and enable \"Add an inbound webhook\".\n- In your prompt (e.g., \"welcome message\"), use the variable with this syntax: `{{variable_name}}` (see [Retell's documentation](https://docs.retellai.com/build/dynamic-variables)).\n- These variables will be dynamically replaced by the data in your Google Sheet.\n\n\n## Notes\n- In Google Sheets, the phone number must start with `'+'`.\n- Phone numbers must be formatted like the example: with the `+`, extension, and no spaces.\n- You can use any database—just replace Google Sheets with your own, making sure to keep the phone number formatting consistent.\n"
      },
      "typeVersion": 1
    },
    {
      "id": "55b087bf-d51f-4660-94c7-3742915ff79b",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -220,
        -120
      ],
      "parameters": {
        "color": 5,
        "width": 220,
        "height": 300,
        "content": "Change the path if needed"
      },
      "typeVersion": 1
    },
    {
      "id": "bd6a7c81-5125-4f46-a1ba-86029d3a0eda",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        80,
        -120
      ],
      "parameters": {
        "color": 5,
        "width": 220,
        "height": 300,
        "content": "Replace with your own Google Sheets, including the dynamic variables of your Retell Agent"
      },
      "typeVersion": 1
    },
    {
      "id": "7105c832-ffbe-4d36-90ec-b8c868388c4e",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        380,
        -120
      ],
      "parameters": {
        "color": 5,
        "width": 220,
        "height": 300,
        "content": "Adapt the response to match your Retell dynamic variables"
      },
      "typeVersion": 1
    }
  ],
  "pinData": {},
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Get user in DB by Phone Number",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get user in DB by Phone Number": {
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

<a id="template-2422"></a>

## Template 2422 - Salvar anexos do Gmail em pastas por empresa e mês no Drive

- **Nome:** Salvar anexos do Gmail em pastas por empresa e mês no Drive
- **Descrição:** Recebe e-mails filtrados, valida o remetente em uma lista de permissões, organiza e armazena anexos no Google Drive em pastas por empresa e por ano/mês, criando pastas quando necessário.
- **Funcionalidade:** • Monitoramento de e-mails com filtro: Verifica periodicamente uma etiqueta específica para novos e-mails.
• Download e separação de anexos: Baixa os anexos do e-mail e divide cada arquivo em itens individuais para processamento.
• Validação por lista de permissões: Consulta uma planilha para mapear o e-mail do remetente à empresa correspondente.
• Verificação/criação de pasta da empresa: Procura uma pasta com o nome da empresa no Drive e cria caso não exista.
• Verificação/criação de pasta YYYY/MM: Gera o nome de pasta ano/mês a partir da data do e-mail, verifica sua existência e cria se necessário dentro da pasta da empresa.
• Upload de arquivos com metadados: Faz upload de cada anexo para a pasta correta, prefixando o nome com timestamp e adicionando propriedades como remetente e horário recebido.
• OCR e propriedades do arquivo: Aplica configuração de OCR (idioma inglês) e armazena metadados personalizados no arquivo do Drive.
- **Ferramentas:** • Gmail: Fonte dos e-mails monitorados e provedora dos anexos a serem processados.
• Google Sheets: Planilha usada como lista de permissões para mapear remetentes às empresas.
• Google Drive: Local de armazenamento onde pastas por empresa e por ano/mês são verificadas/criadas e onde os arquivos são enviados.

## Fluxo visual

```mermaid
flowchart LR
    N1["Search For Folder"]
    N2["Create Month Folder"]
    N3["Check If Folder Exists"]
    N4["Gmail Trigger"]
    N5["Gmail"]
    N6["Split Up Binary Data1"]
    N7["Note2"]
    N8["YYYY/MM"]
    N9["Loop Over Items"]
    N10["Note3"]
    N11["Company Folder Exists"]
    N12["Create Company Folder"]
    N13["Note4"]
    N14["Sticky Note4"]
    N15["Lookup in Sheets"]
    N16["Search Company Folder1"]
    N17["Sticky Note"]
    N18["Sticky Note2"]
    N19["Upload To Folder"]

    N5 --> N6
    N8 --> N1
    N4 --> N15
    N9 --> N19
    N15 --> N16
    N19 --> N9
    N1 --> N3
    N2 --> N5
    N11 --> N8
    N11 --> N12
    N12 --> N8
    N6 --> N9
    N3 --> N5
    N3 --> N2
    N16 --> N11
```

## Fluxo (.json) :

```json
{
  "meta": {
    "instanceId": "5e2cdd86a9e1ca2fc82cc63db38d1710d5d6a5c6fe352258a6f7112815bcd512"
  },
  "nodes": [
    {
      "id": "13188ea7-7e66-4955-89d0-82ba4dc08dc9",
      "name": "Search For Folder",
      "type": "n8n-nodes-base.googleDrive",
      "position": [
        -2420,
        500
      ],
      "parameters": {
        "filter": {
          "folderId": {
            "__rl": true,
            "mode": "id",
            "value": "={{ $json.id }}"
          }
        },
        "options": {},
        "resource": "fileFolder",
        "queryString": "={{$json.folderName}}"
      },
      "credentials": {
        "googleDriveOAuth2Api": {
          "id": "VypmUgEf64twpmiZ",
          "name": "Google Drive account"
        }
      },
      "typeVersion": 3,
      "alwaysOutputData": true
    },
    {
      "id": "ed2ababb-7022-43e1-b638-0132c08ef701",
      "name": "Create Month Folder",
      "type": "n8n-nodes-base.googleDrive",
      "position": [
        -2060,
        680
      ],
      "parameters": {
        "name": "={{ $('YYYY/MM').first().json.folderName }}",
        "driveId": {
          "__rl": true,
          "mode": "list",
          "value": "My Drive"
        },
        "options": {},
        "folderId": {
          "__rl": true,
          "mode": "id",
          "value": "={{ $('YYYY/MM').item.json.id }}"
        },
        "resource": "folder"
      },
      "credentials": {
        "googleDriveOAuth2Api": {
          "id": "VypmUgEf64twpmiZ",
          "name": "Google Drive account"
        }
      },
      "typeVersion": 3
    },
    {
      "id": "f5f2365d-0977-48b1-bd2e-29b7707839d9",
      "name": "Check If Folder Exists",
      "type": "n8n-nodes-base.if",
      "position": [
        -2240,
        500
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
              "id": "09b62415-cb8f-478e-b6d3-aa463fe70c81",
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
      "typeVersion": 2.2
    },
    {
      "id": "c27b0a9d-8ee2-4eae-963c-14256ffae0b8",
      "name": "Gmail Trigger",
      "type": "n8n-nodes-base.gmailTrigger",
      "position": [
        -4400,
        780
      ],
      "parameters": {
        "simple": false,
        "filters": {
          "labelIds": [
            "Label_2"
          ]
        },
        "options": {},
        "pollTimes": {
          "item": [
            {
              "mode": "everyX",
              "unit": "minutes",
              "value": 15
            }
          ]
        }
      },
      "credentials": {
        "gmailOAuth2": {
          "id": "HI2iZSvhvC5XOdpp",
          "name": "Gmail account 2"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "3eac8c53-1b20-4511-9f2a-f5e838ca0fa0",
      "name": "Gmail",
      "type": "n8n-nodes-base.gmail",
      "position": [
        -1720,
        460
      ],
      "webhookId": "e62ae049-d968-4e6a-a62d-06963c8e592f",
      "parameters": {
        "simple": false,
        "options": {
          "downloadAttachments": true
        },
        "messageId": "={{ $('Gmail Trigger').item.json.id }}",
        "operation": "get"
      },
      "credentials": {
        "gmailOAuth2": {
          "id": "HI2iZSvhvC5XOdpp",
          "name": "Gmail account 2"
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "bfae9bb5-6915-4968-8b5e-e72dd46bda55",
      "name": "Split Up Binary Data1",
      "type": "n8n-nodes-base.function",
      "position": [
        -1560,
        460
      ],
      "parameters": {
        "functionCode": "let results = [];\n\nfor (item of items) {\n    for (key of Object.keys(item.binary)) {\n        results.push({\n            json: {\n                fileName: item.binary[key].fileName\n            },\n            binary: {\n                data: item.binary[key],\n            }\n        });\n    }\n}\n\nreturn results;"
      },
      "typeVersion": 1
    },
    {
      "id": "baf55ab9-511f-4404-a2cc-b1c848f6f5c5",
      "name": "Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -1800,
        280
      ],
      "parameters": {
        "color": 7,
        "width": 920,
        "height": 660,
        "content": "## Upload attachments to Drive\nIncoming files are split up into individual items, each with a single binary data object under the `data` key.\nFiles names are prefixed with the current timestamp"
      },
      "typeVersion": 1
    },
    {
      "id": "5d706d3a-db17-4f5f-9eac-ba91c470dbdd",
      "name": "YYYY/MM",
      "type": "n8n-nodes-base.set",
      "position": [
        -2600,
        500
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "143b3b94-a8d7-46b6-8ea8-2e70c082f5b1",
              "name": "=folderName",
              "type": "string",
              "value": "={{\n  new Date($('Gmail Trigger').item.json.date).getUTCFullYear() \n  + '/' + \n  String(new Date($('Gmail Trigger').item.json.date).getUTCMonth() + 1).padStart(2, '0')\n}}\n"
            }
          ]
        },
        "includeOtherFields": true
      },
      "typeVersion": 3.4
    },
    {
      "id": "b20a3833-f648-454d-999b-d799727e18e8",
      "name": "Loop Over Items",
      "type": "n8n-nodes-base.splitInBatches",
      "position": [
        -1320,
        460
      ],
      "parameters": {
        "options": {}
      },
      "typeVersion": 3
    },
    {
      "id": "bb8c0d21-de74-4abf-bf6c-5eef3f301513",
      "name": "Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -2680,
        280
      ],
      "parameters": {
        "color": 7,
        "width": 820,
        "height": 660,
        "content": "# Checks if YYYY/MM Folder exists\n## If the directory doesn't exist it is created"
      },
      "typeVersion": 1
    },
    {
      "id": "40971ca3-91d3-4651-8137-e973dbd2dbbd",
      "name": "Company Folder Exists",
      "type": "n8n-nodes-base.if",
      "position": [
        -3180,
        500
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
              "id": "09b62415-cb8f-478e-b6d3-aa463fe70c81",
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
      "typeVersion": 2.2
    },
    {
      "id": "086ff643-ca10-46ec-92b5-8a014fd3bf3f",
      "name": "Create Company Folder",
      "type": "n8n-nodes-base.googleDrive",
      "position": [
        -2920,
        620
      ],
      "parameters": {
        "name": "={{ $('Lookup in Sheets').item.json.company }}",
        "driveId": {
          "__rl": true,
          "mode": "list",
          "value": "My Drive"
        },
        "options": {},
        "folderId": {
          "__rl": true,
          "mode": "list",
          "value": "18ry0AUtrpp3re6u3zQvvs0BQUGFmBKN9",
          "cachedResultUrl": "https://drive.google.com/drive/folders/18ry0AUtrpp3re6u3zQvvs0BQUGFmBKN9",
          "cachedResultName": "Invoices"
        },
        "resource": "folder"
      },
      "credentials": {
        "googleDriveOAuth2Api": {
          "id": "VypmUgEf64twpmiZ",
          "name": "Google Drive account"
        }
      },
      "typeVersion": 3
    },
    {
      "id": "7792afb7-61d9-402f-814b-f4625cd012bc",
      "name": "Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -3500,
        120
      ],
      "parameters": {
        "color": 7,
        "width": 760,
        "height": 820,
        "content": "# Checks if a folder with the company of the email exists\n## If it doesn't the directory is created"
      },
      "typeVersion": 1
    },
    {
      "id": "1f61ea45-49e6-4018-91ad-2144c1bbc19a",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -4120,
        280
      ],
      "parameters": {
        "color": 6,
        "width": 560,
        "height": 660,
        "content": "# 2. Google Sheets Whitelist Config\n\n## To filter contacts against a whitelist:\n### 1. Make a copy of [this spreadsheet](https://docs.google.com/spreadsheets/d/1tTz9BflstxVL18YG11Ny1eiDj3FcjvtZ619b_bHx8h4/edit?usp=sharing)\n**OR** create a Google Sheet with two columns:\n| **email**     | **company**      |\n\n\n### 2. Add whitelisted emails and their company as rows in the sheet and configure this node **Document** and **Sheet** to point to it.\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
      },
      "typeVersion": 1
    },
    {
      "id": "f7009cc2-8194-40c9-98e9-edc4a29c5ce8",
      "name": "Lookup in Sheets",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        -3900,
        780
      ],
      "parameters": {
        "options": {},
        "filtersUI": {
          "values": [
            {
              "lookupValue": "={{ $('Gmail Trigger').item.json.from.value[0].address }}",
              "lookupColumn": "email"
            }
          ]
        },
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": "gid=0",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1gZE7EbLJqfMzQlPoCgE0eeqee_F1Lh9eIwhHsVmYKdw/edit#gid=0",
          "cachedResultName": "Sheet1"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "1gZE7EbLJqfMzQlPoCgE0eeqee_F1Lh9eIwhHsVmYKdw",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1gZE7EbLJqfMzQlPoCgE0eeqee_F1Lh9eIwhHsVmYKdw/edit?usp=drivesdk",
          "cachedResultName": "Contacts Whitelist"
        }
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "63dUs6P8a2b5ed5J",
          "name": "Google Sheets account"
        }
      },
      "typeVersion": 4.5,
      "alwaysOutputData": false
    },
    {
      "id": "932afe12-3341-4f77-88ab-0b558e0d6ee2",
      "name": "Search Company Folder1",
      "type": "n8n-nodes-base.googleDrive",
      "position": [
        -3440,
        500
      ],
      "parameters": {
        "filter": {
          "whatToSearch": "folders"
        },
        "options": {},
        "resource": "fileFolder",
        "queryString": "={{ $('Lookup in Sheets').item.json.company }}"
      },
      "credentials": {
        "googleDriveOAuth2Api": {
          "id": "VypmUgEf64twpmiZ",
          "name": "Google Drive account"
        }
      },
      "typeVersion": 3,
      "alwaysOutputData": true
    },
    {
      "id": "b9e66cf4-365a-4d11-bff9-48bf28be9e96",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -4740,
        280
      ],
      "parameters": {
        "color": 6,
        "width": 560,
        "height": 660,
        "content": "# 1. Trigger Settings and Filters\n\n## Configure the interval to check for new emails and apply filters to process only some emails\n\n**For example**: To create a filter that applies a label to emails **with attachments** containing the words \"invoice\" or \"receipt,\" follow these steps:\n\n1. Open your Gmail and click on the burger menu button next to the search bar to open the search options.\n2. In the `Has the words` field type in 'invoice receipt'\n3. Check the `Has attachment` checkbox\n4. Click on the \"Create filter with this search\" option at the bottom of the search window.\n5. In the filter options, select the \"Apply the label\" option and choose or create a label for these emails.\n6. Click \"Create filter\" to save your new filter.\n\n\n\n\n\n\n\n\n\n\n\n"
      },
      "typeVersion": 1
    },
    {
      "id": "2a932450-d0e9-44b4-adfb-2254b8e6e547",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -3000,
        220
      ],
      "parameters": {
        "color": 6,
        "height": 540,
        "content": "# 3. Configure storage location\n## Set where to store files from the `parent folder` dropdown"
      },
      "typeVersion": 1
    },
    {
      "id": "247e4ed7-ebff-4392-adf2-4a63e80e04f4",
      "name": "Upload To Folder",
      "type": "n8n-nodes-base.googleDrive",
      "position": [
        -1100,
        480
      ],
      "parameters": {
        "name": "={{ Date.now();}}-{{ $('Loop Over Items').item.binary.data.fileName }} ",
        "driveId": {
          "__rl": true,
          "mode": "list",
          "value": "My Drive",
          "cachedResultUrl": "https://drive.google.com/drive/my-drive",
          "cachedResultName": "My Drive"
        },
        "options": {
          "ocrLanguage": "en",
          "propertiesUi": {
            "propertyValues": [
              {
                "key": "sender",
                "value": "={{ $('Gmail').item.json.from.value[0].address }}"
              },
              {
                "key": "time_received",
                "value": "={{ $('Gmail').item.json.date }}"
              }
            ]
          }
        },
        "folderId": {
          "__rl": true,
          "mode": "id",
          "value": "={{ $('Search For Folder').first().json.id || $('Create Month Folder').item.json.id }}"
        },
        "inputDataFieldName": "=data"
      },
      "credentials": {
        "googleDriveOAuth2Api": {
          "id": "VypmUgEf64twpmiZ",
          "name": "Google Drive account"
        }
      },
      "typeVersion": 3
    }
  ],
  "pinData": {},
  "connections": {
    "Gmail": {
      "main": [
        [
          {
            "node": "Split Up Binary Data1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "YYYY/MM": {
      "main": [
        [
          {
            "node": "Search For Folder",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Gmail Trigger": {
      "main": [
        [
          {
            "node": "Lookup in Sheets",
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
            "node": "Upload To Folder",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Lookup in Sheets": {
      "main": [
        [
          {
            "node": "Search Company Folder1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Upload To Folder": {
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
    "Search For Folder": {
      "main": [
        [
          {
            "node": "Check If Folder Exists",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Create Month Folder": {
      "main": [
        [
          {
            "node": "Gmail",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Company Folder Exists": {
      "main": [
        [
          {
            "node": "YYYY/MM",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Create Company Folder",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Create Company Folder": {
      "main": [
        [
          {
            "node": "YYYY/MM",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Split Up Binary Data1": {
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
    "Check If Folder Exists": {
      "main": [
        [
          {
            "node": "Gmail",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Create Month Folder",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Search Company Folder1": {
      "main": [
        [
          {
            "node": "Company Folder Exists",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2424"></a>

## Template 2424 - Criação diária de playlist AI News

- **Nome:** Criação diária de playlist AI News
- **Descrição:** Automatiza a criação diária de uma playlist do YouTube com os vídeos recentes de uma lista de canais, atualiza IDs no Google Sheets e notifica por Telegram.
- **Funcionalidade:** • Agendamento diário: Dispara o fluxo em horário programado (ex.: 07:15).
• Criação de playlist datada: Cria uma nova playlist do YouTube com a data no título (formato YYMMDD) seguida de "AI News".
• Leitura da lista de canais: Recupera canais de uma planilha do Google Sheets para saber quais canais verificar.
• Busca de vídeos recentes: Consulta a API do YouTube para obter os vídeos publicados nas últimas 24 horas (máx. 5 por canal).
• Filtragem de lives futuras: Exclui transmissões marcadas como "upcoming" para não adicioná-las à playlist.
• Adição de vídeos à playlist: Insere cada vídeo encontrado na playlist recém-criada.
• Salvamento do ID da playlist: Grava o ID da nova playlist em uma planilha para referência futura.
• Exclusão da playlist anterior: Opcionalmente apaga a playlist criada no dia anterior usando o ID salvo (recomendado desativar na primeira execução).
• Notificação: Envia uma mensagem via Telegram quando a playlist é atualizada.
• Fluxo auxiliar para completar lista de canais: Workflow separado que converte nomes de usuário (@) em IDs de canal e atualiza a planilha (útil ao adicionar novos canais).
• Gatilho manual para testes: Permite executar partes do fluxo manualmente para validação.
- **Ferramentas:** • YouTube API: Usada para buscar canais e vídeos, criar playlists e adicionar itens às playlists.
• Google Sheets: Armazena a lista de canais, IDs de canal, links e o ID da playlist gerada para uso futuro.
• Telegram: Envia notificações quando a playlist é criada/atualizada.

## Fluxo visual

```mermaid
flowchart LR
    N1["Read Channel Names"]
    N2["Get Videos"]
    N3["Split Out"]
    N4["Sticky Note"]
    N5["Sticky Note1"]
    N6["Create Playlist"]
    N7["Delete Old Playlist"]
    N8["Sticky Note2"]
    N9["Sticky Note3"]
    N10["YouTube"]
    N11["Sticky Note4"]
    N12["Filter Out Upcoming"]
    N13["Save Playlist ID"]
    N14["Google Sheets"]
    N15["Telegram"]
    N16["Sticky Note5"]
    N17["0715 Trigger"]
    N18["Get Channels"]
    N19["Update Google Sheet"]
    N20["When clicking ‘Test workflow’"]
    N21["Read Channel Names1"]
    N22["Sticky Note6"]
    N23["Sticky Note7"]

    N10 --> N15
    N3 --> N12
    N2 --> N3
    N17 --> N6
    N17 --> N14
    N18 --> N19
    N14 --> N7
    N6 --> N13
    N13 --> N1
    N1 --> N2
    N12 --> N10
    N21 --> N18
    N20 --> N21
```

## Fluxo (.json) :

```json
{
  "id": "2LFEJVoSkeZMndiM",
  "meta": {
    "instanceId": "d73587d68bda6969e611b1d966e9e2b0ae078a8d2666ab57d6d9dcd379a0ce36",
    "templateCredsSetupCompleted": true
  },
  "name": "YT AI News Playlist Creator/AI News Form Updater",
  "tags": [],
  "nodes": [
    {
      "id": "a871e87e-dc02-4364-83b3-fe378ca60687",
      "name": "Read Channel Names",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        860,
        100
      ],
      "parameters": {
        "options": {},
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": 944489068,
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1RNah4ZZsLxflQXvMq8AEn3BFpscOC2ygMZ1dPTlk-Kk/edit#gid=944489068",
          "cachedResultName": "AI News Channels"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "1RNah4ZZsLxflQXvMq8AEn3BFpscOC2ygMZ1dPTlk-Kk",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1RNah4ZZsLxflQXvMq8AEn3BFpscOC2ygMZ1dPTlk-Kk/edit?usp=drivesdk",
          "cachedResultName": "Media Links"
        }
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "hVq7KRYH68lYmtEB",
          "name": "Google Sheets account"
        }
      },
      "typeVersion": 4.5
    },
    {
      "id": "bcc83a11-e7e1-4bcb-a054-a2f0cc26c5f0",
      "name": "Get Videos",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1020,
        100
      ],
      "parameters": {
        "url": "https://www.googleapis.com/youtube/v3/search",
        "options": {},
        "sendQuery": true,
        "queryParameters": {
          "parameters": [
            {
              "name": "part",
              "value": "snippet"
            },
            {
              "name": "publishedAfter",
              "value": "={{ $now.minus(1, 'day') }}"
            },
            {
              "name": "maxResults",
              "value": "5"
            },
            {
              "name": "channel_id",
              "value": "={{ $('Read Channel Names').item.json['Channel Id'] }}"
            },
            {
              "name": "order",
              "value": "date"
            },
            {
              "name": "key",
              "value": "AddYourAPIKeyHere"
            }
          ]
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "6da4a908-1705-4d3a-8f1a-aa73e36866c7",
      "name": "Split Out",
      "type": "n8n-nodes-base.splitOut",
      "position": [
        1160,
        100
      ],
      "parameters": {
        "options": {},
        "fieldToSplitOut": "items"
      },
      "typeVersion": 1
    },
    {
      "id": "1f7ab323-fb52-4a41-bf71-9594e4d1c78d",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        140,
        0
      ],
      "parameters": {
        "width": 220,
        "height": 260,
        "content": "## Initiation\nThis section starts the workflow sets the time."
      },
      "typeVersion": 1
    },
    {
      "id": "e17f2b65-3320-46aa-b360-2366691053cd",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        800,
        0
      ],
      "parameters": {
        "color": 5,
        "width": 660,
        "height": 260,
        "content": "## Getting the Videos\nThis section grabs the videos."
      },
      "typeVersion": 1
    },
    {
      "id": "d950c171-0993-4e51-8942-18dca557c70a",
      "name": "Create Playlist",
      "type": "n8n-nodes-base.youTube",
      "position": [
        440,
        100
      ],
      "parameters": {
        "title": "={{ $today.format('yyLLdd') }} AI News",
        "options": {},
        "resource": "playlist",
        "operation": "create"
      },
      "credentials": {
        "youTubeOAuth2Api": {
          "id": "alrF3L4QeYVd4Ckn",
          "name": "YouTube account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "1d292e23-4efc-4377-aacf-8c5b9c54e524",
      "name": "Delete Old Playlist",
      "type": "n8n-nodes-base.youTube",
      "position": [
        580,
        -220
      ],
      "parameters": {
        "options": {},
        "resource": "playlist",
        "operation": "delete",
        "playlistId": "={{ $json['New Playlist ID'] }}"
      },
      "credentials": {
        "youTubeOAuth2Api": {
          "id": "alrF3L4QeYVd4Ckn",
          "name": "YouTube account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "26ddb0d4-4ae8-485c-8909-00c70230ce76",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        400,
        -340
      ],
      "parameters": {
        "color": 3,
        "width": 380,
        "height": 280,
        "content": "## Delete Yesterday's Playlist\nThis section deletes the playlist created yesterday. (do not include this on your first run; or, your workflow will stop)"
      },
      "typeVersion": 1
    },
    {
      "id": "c4756eb6-c080-48dd-9941-511fbf405fbe",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        400,
        0
      ],
      "parameters": {
        "color": 4,
        "width": 360,
        "height": 260,
        "content": "## Create New AI News Playlist\nThis section creates today's playlist."
      },
      "typeVersion": 1
    },
    {
      "id": "33308ef0-fb86-4bce-a81f-0c5ddc4215a1",
      "name": "YouTube",
      "type": "n8n-nodes-base.youTube",
      "position": [
        1580,
        100
      ],
      "parameters": {
        "options": {},
        "videoId": "={{ $('Split Out').item.json.id.videoId }}",
        "resource": "playlistItem",
        "playlistId": "={{ $('Create Playlist').item.json.id }}"
      },
      "credentials": {
        "youTubeOAuth2Api": {
          "id": "alrF3L4QeYVd4Ckn",
          "name": "YouTube account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "2db4a5e2-f177-4c45-a890-8bf140971882",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1500,
        0
      ],
      "parameters": {
        "color": 6,
        "width": 280,
        "height": 260,
        "content": "## Add Videos to Playlist\nThis section adds videos to the playlist created today."
      },
      "typeVersion": 1
    },
    {
      "id": "7c2945de-9912-4db0-bd4f-6c222b8ebeaf",
      "name": "Filter Out Upcoming",
      "type": "n8n-nodes-base.filter",
      "position": [
        1300,
        100
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
          "combinator": "or",
          "conditions": [
            {
              "id": "8884d2e9-b06d-4347-9635-846d7dea168f",
              "operator": {
                "type": "string",
                "operation": "notEquals"
              },
              "leftValue": "={{ $json.snippet.liveBroadcastContent }}",
              "rightValue": "upcoming"
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "d822a00b-acfc-4838-ae50-37103e581cbf",
      "name": "Save Playlist ID",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        600,
        100
      ],
      "parameters": {
        "columns": {
          "value": {
            "Playlist Group": "AI News",
            "New Playlist ID": "={{ $json.id }}"
          },
          "schema": [
            {
              "id": "Playlist Group",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "Playlist Group",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "New Playlist ID",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "New Playlist ID",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "row_number",
              "type": "string",
              "display": true,
              "removed": true,
              "readOnly": true,
              "required": false,
              "displayName": "row_number",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            }
          ],
          "mappingMode": "defineBelow",
          "matchingColumns": [
            "Playlist Group"
          ],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {},
        "operation": "update",
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": 1541621778,
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1RNah4ZZsLxflQXvMq8AEn3BFpscOC2ygMZ1dPTlk-Kk/edit#gid=1541621778",
          "cachedResultName": "PlaylistId"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "1RNah4ZZsLxflQXvMq8AEn3BFpscOC2ygMZ1dPTlk-Kk",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1RNah4ZZsLxflQXvMq8AEn3BFpscOC2ygMZ1dPTlk-Kk/edit?usp=drivesdk",
          "cachedResultName": "Media Links"
        }
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "hVq7KRYH68lYmtEB",
          "name": "Google Sheets account"
        }
      },
      "typeVersion": 4.5
    },
    {
      "id": "bbbcbe5b-5594-44cb-bb1d-897498b61810",
      "name": "Google Sheets",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        440,
        -220
      ],
      "parameters": {
        "options": {},
        "filtersUI": {
          "values": [
            {
              "lookupValue": "AI News",
              "lookupColumn": "Playlist Group"
            }
          ]
        },
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": 1541621778,
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1RNah4ZZsLxflQXvMq8AEn3BFpscOC2ygMZ1dPTlk-Kk/edit#gid=1541621778",
          "cachedResultName": "PlaylistId"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "1RNah4ZZsLxflQXvMq8AEn3BFpscOC2ygMZ1dPTlk-Kk",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1RNah4ZZsLxflQXvMq8AEn3BFpscOC2ygMZ1dPTlk-Kk/edit?usp=drivesdk",
          "cachedResultName": "Media Links"
        }
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "hVq7KRYH68lYmtEB",
          "name": "Google Sheets account"
        }
      },
      "typeVersion": 4.5
    },
    {
      "id": "20d814e1-4f1e-4313-949b-961556cd40bf",
      "name": "Telegram",
      "type": "n8n-nodes-base.telegram",
      "position": [
        1880,
        100
      ],
      "webhookId": "5007b956-14f6-4275-ab8d-2c47050b6007",
      "parameters": {
        "text": "Your AI News YT Playlist has been updated.",
        "additionalFields": {}
      },
      "credentials": {
        "telegramApi": {
          "id": "FeG2VD9QbvSMvLxW",
          "name": "Dinar Newscaster"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "b0cfab69-ad82-4d65-8106-0bd4b23dfdb3",
      "name": "Sticky Note5",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1820,
        0
      ],
      "parameters": {
        "color": 6,
        "width": 280,
        "height": 260,
        "content": "## Notification of Completion (optional)"
      },
      "typeVersion": 1
    },
    {
      "id": "57ef08c8-b7ca-4af6-963a-67a3d2b80176",
      "name": "0715 Trigger",
      "type": "n8n-nodes-base.scheduleTrigger",
      "position": [
        180,
        100
      ],
      "parameters": {
        "rule": {
          "interval": [
            {
              "triggerAtHour": 7,
              "triggerAtMinute": 15
            }
          ]
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "d3003e8a-aa46-437e-b246-b9030578ea49",
      "name": "Get Channels",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        800,
        -640
      ],
      "parameters": {
        "url": "https://www.googleapis.com/youtube/v3/search",
        "options": {},
        "sendQuery": true,
        "queryParameters": {
          "parameters": [
            {
              "name": "q",
              "value": "={{ $json['Channel User Name'] }}"
            },
            {
              "name": "type",
              "value": "channel"
            },
            {
              "name": "maxResults",
              "value": "1"
            },
            {
              "name": "part",
              "value": "snippet"
            },
            {
              "name": "key",
              "value": "AIzaSyARU7upVG5hzoaMHIMaBEXjcYtayo8vPJ4"
            }
          ]
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "fde3bac7-77be-4322-9b74-2cb7b9ddd17c",
      "name": "Update Google Sheet",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        1000,
        -640
      ],
      "parameters": {
        "columns": {
          "value": {
            "Link": "=https://www.youtube.com/{{ $('Read Channel Names1').item.json['Channel User Name'] }}",
            "Channel Id": "={{ $json.items[0].id.channelId }}",
            "row_number": "={{ $('Read Channel Names1').item.json.row_number }}",
            "Channel Name": "={{ $json.items[0].snippet.channelTitle }}"
          },
          "schema": [
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
              "id": "Link",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Link",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Channel Id",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Channel Id",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Channel User Name",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "Channel User Name",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
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
          "mappingMode": "defineBelow",
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
          "value": 944489068,
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1RNah4ZZsLxflQXvMq8AEn3BFpscOC2ygMZ1dPTlk-Kk/edit#gid=944489068",
          "cachedResultName": "AI News Channels"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "1RNah4ZZsLxflQXvMq8AEn3BFpscOC2ygMZ1dPTlk-Kk",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1RNah4ZZsLxflQXvMq8AEn3BFpscOC2ygMZ1dPTlk-Kk/edit?usp=drivesdk",
          "cachedResultName": "Media Links"
        }
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "hVq7KRYH68lYmtEB",
          "name": "Google Sheets account"
        }
      },
      "typeVersion": 4.5
    },
    {
      "id": "2b1e067b-436a-4536-ad9f-c55862d496c9",
      "name": "When clicking ‘Test workflow’",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        440,
        -640
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "1dd572c5-6762-40a0-88aa-d6a9fa2ca0a3",
      "name": "Read Channel Names1",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        620,
        -640
      ],
      "parameters": {
        "options": {},
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": 944489068,
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1RNah4ZZsLxflQXvMq8AEn3BFpscOC2ygMZ1dPTlk-Kk/edit#gid=944489068",
          "cachedResultName": "AI News Channels"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "1RNah4ZZsLxflQXvMq8AEn3BFpscOC2ygMZ1dPTlk-Kk",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1RNah4ZZsLxflQXvMq8AEn3BFpscOC2ygMZ1dPTlk-Kk/edit?usp=drivesdk",
          "cachedResultName": "Media Links"
        }
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "hVq7KRYH68lYmtEB",
          "name": "Google Sheets account"
        }
      },
      "typeVersion": 4.5
    },
    {
      "id": "43466e82-dc55-4d4e-a6ff-ff2ed977fb3c",
      "name": "Sticky Note6",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        380,
        -740
      ],
      "parameters": {
        "width": 820,
        "height": 260,
        "content": "## Create your Channel List\nThis section needs to be put into it's own workflow: this workflow gathers information needed to gather videos for the playlist.  This workflow only needs to be run when a new channel name is added to the Google Sheet."
      },
      "typeVersion": 1
    },
    {
      "id": "149373af-ad35-49bc-b751-6ac919d218b0",
      "name": "Sticky Note7",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1260,
        -740
      ],
      "parameters": {
        "width": 820,
        "height": 700,
        "content": "## Instructions\n1. To set this up, you need to create a Google Sheet with the following headings in line 1:\n\n   Channel User Name\n   Channel Name\n   Channel Link\n   Channel ID\n\n2. Copy the 'Create your Channel List' into it's own workflow and link the Sheets links to your new sheet.\n\n3. To get the 'Create your Channel List' to work, you need to visit each channel's page that you want included in your playlist; you need to get the \"@\" name of the channel and add it to the 'Channel User Name' column of your Google Sheet.\n\n   For example: if you wanted to include this channel: Recruit Training Videos - Corporal Stock \n   You would look for this name, to add to the next available row of the 'Channel User Name' column: @CorporalStock\n\n4. Once you add all Channel User Names, run the 'Create your Channel list workflow, and it will fill in the remaining details.\n\n5. Now the 'YT Playlist Creator' can be run; but for the first time, disconnect the 'Delete Yesterday's Playlist' leg, or the workflow will error and stop (because there is no 'Yesterday's Playlist'.\n\nNote: this was made to create a playlist every day, delete yesterday's playlist, and only get the last 8 videos posted within the last 24 hours.  I choose to put the date (YYMMDD format) in front of the playlist, to ensure that it doesn't conflict with another playlist.\n\n   Also, I have it notifying me in Telegram, so I know that the new playlist is posted."
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "timezone": "Asia/Manila",
    "executionOrder": "v1"
  },
  "versionId": "c154607b-f3b1-4f41-bf77-faec36ce3716",
  "connections": {
    "YouTube": {
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
    "Split Out": {
      "main": [
        [
          {
            "node": "Filter Out Upcoming",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Videos": {
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
    "0715 Trigger": {
      "main": [
        [
          {
            "node": "Create Playlist",
            "type": "main",
            "index": 0
          },
          {
            "node": "Google Sheets",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Channels": {
      "main": [
        [
          {
            "node": "Update Google Sheet",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Sheets": {
      "main": [
        [
          {
            "node": "Delete Old Playlist",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Create Playlist": {
      "main": [
        [
          {
            "node": "Save Playlist ID",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Save Playlist ID": {
      "main": [
        [
          {
            "node": "Read Channel Names",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Read Channel Names": {
      "main": [
        [
          {
            "node": "Get Videos",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Filter Out Upcoming": {
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
    "Read Channel Names1": {
      "main": [
        [
          {
            "node": "Get Channels",
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
            "node": "Read Channel Names1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
