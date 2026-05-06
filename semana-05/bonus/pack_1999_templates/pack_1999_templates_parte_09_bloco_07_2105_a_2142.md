# PACK 1999 TEMPLATES PARTE 09 - Bloco 7

Templates neste bloco: 20

## Sumário

- [Template 2105 - Importar fabricantes do Google Sheets para Shopware 6](#template-2105)
- [Template 2107 - Roteamento de itens por ID](#template-2107)
- [Template 2109 - Geração e revisão de imagens para equipe de design](#template-2109)
- [Template 2112 - Histórias infantis automáticas no Telegram](#template-2112)
- [Template 2114 - Insights de avaliações Trustpilot](#template-2114)
- [Template 2116 - Verificação de assinatura de webhook Slack](#template-2116)
- [Template 2117 - Extração e resumo semanal de notícias](#template-2117)
- [Template 2119 - Atualizar nós desatualizados em workflows](#template-2119)
- [Template 2121 - Portal Docsify para documentação de fluxos](#template-2121)
- [Template 2123 - Criar quadro, listas e mover cartão no Wekan](#template-2123)
- [Template 2125 - Atualiza valores do portfólio de criptomoedas](#template-2125)
- [Template 2127 - Extrair gastos de emails para planilha](#template-2127)
- [Template 2129 - Leitura de dois feeds RSS](#template-2129)
- [Template 2130 - Leitura de e-mails via IMAP](#template-2130)
- [Template 2133 - Captura e análise de palavras-chave](#template-2133)
- [Template 2135 - Sincronização YouTube → Spotify (sem duplicados)](#template-2135)
- [Template 2137 - Criar item de erro no Monday.com](#template-2137)
- [Template 2138 - Criar projeto, tag e entrada de tempo no Clockify](#template-2138)
- [Template 2140 - Publicar novos vídeos do YouTube no X](#template-2140)
- [Template 2142 - Extração de dados de recibo](#template-2142)

---

<a id="template-2105"></a>

## Template 2105 - Importar fabricantes do Google Sheets para Shopware 6

- **Nome:** Importar fabricantes do Google Sheets para Shopware 6
- **Descrição:** Lê fabricantes de uma planilha, monta payloads com traduções e mídias, e importa/upserta esses fabricantes na loja Shopware 6, fazendo upload condicional dos logos.
- **Funcionalidade:** • Leitura de fabricantes do Google Sheets: Extrai colunas como name, website, description, logo_url e campos de tradução.
• Montagem do payload de importação: Cria o objeto de sincronização (upsert) para Shopware, incluindo traduções quando presentes (suporte a até 3 idiomas configuráveis).
• Geração de ID de mídia via MD5: Calcula um ID de mídia baseado no nome do fabricante para associar o logo.
• Importação/Upsert na API do Shopware: Envia o payload para o endpoint de sync para criar ou atualizar o fabricante.
• Upload condicional de logo: Se houver mídia criada, faz upload da imagem ao endpoint de media usando a URL pública e informa extensão e nome do arquivo.
• Processamento em lote: Itera sobre cada linha da planilha e processa fabricantes individualmente.
• Uso de credenciais seguras: Requer integração via OAuth2 (Client Credentials) para autenticar as chamadas à API do Shopware.
- **Ferramentas:** • Google Sheets: Fonte dos dados dos fabricantes armazenados em uma planilha com colunas para nome, site, descrição, URL do logo e traduções.
• Shopware 6: Plataforma de e‑commerce cuja API é usada para sincronizar (upsert) fabricantes e fazer upload de mídias (logos).
• OAuth2 (Client Credentials): Protocolo de autenticação utilizado para obter tokens de acesso e autorizar chamadas à API do Shopware.

## Fluxo visual

```mermaid
flowchart LR
    N1["When clicking 'Execute Workflow'"]
    N2["Settings"]
    N3["Create Import Request Body"]
    N4["Upload Manufacturer Logo"]
    N5["Import Manufacturer"]
    N6["Sticky Note"]
    N7["Sticky Note1"]
    N8["Loop Over Manufacturers"]
    N9["Get Manufacturer from Google Sheet"]
    N10["If has Logo"]
    N11["Sticky Note2"]
    N12["Sticky Note3"]

    N2 --> N9
    N10 --> N4
    N10 --> N8
    N5 --> N10
    N8 --> N5
    N4 --> N8
    N3 --> N8
    N1 --> N2
    N9 --> N3
```

## Fluxo (.json) :

```json
{
  "id": "xLjE4IkQXARXOCZy",
  "meta": {
    "instanceId": "24bd2f3b51439b955590389bfa4dd9889fbd30343962de0b7daedce624cf4a71"
  },
  "name": "Import multiple Manufacturers from Google Sheets to Shopware 6",
  "tags": [
    {
      "id": "Bpo3iitXqy2zfvPW",
      "name": "tutorial",
      "createdAt": "2024-01-06T22:57:17.318Z",
      "updatedAt": "2024-01-06T22:57:17.318Z"
    },
    {
      "id": "NfcTamKf2RPwzXbo",
      "name": "automate-everything",
      "createdAt": "2024-02-14T20:01:44.966Z",
      "updatedAt": "2024-02-14T20:01:44.966Z"
    },
    {
      "id": "2Vgn1rq99D9L11Gq",
      "name": "submitted",
      "createdAt": "2024-02-15T16:09:47.798Z",
      "updatedAt": "2024-02-15T16:09:47.798Z"
    }
  ],
  "nodes": [
    {
      "id": "460ed5fb-cc70-41ed-b6e2-07bc2266603f",
      "name": "When clicking \"Execute Workflow\"",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        340,
        360
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "291e6fc4-31b4-4c7c-91e8-261581664759",
      "name": "Settings",
      "type": "n8n-nodes-base.set",
      "position": [
        620,
        360
      ],
      "parameters": {
        "fields": {
          "values": [
            {
              "name": "shopware_url",
              "stringValue": "https://your-shopware-url.com"
            },
            {
              "name": "default_language_code",
              "stringValue": "de_DE"
            }
          ]
        },
        "options": {}
      },
      "typeVersion": 3.2
    },
    {
      "id": "38f62300-bbc9-4c2e-a1ba-1d1a49e9cecc",
      "name": "Create Import Request Body",
      "type": "n8n-nodes-base.code",
      "position": [
        1260,
        360
      ],
      "parameters": {
        "jsCode": "// importing crypto package to create md5 hashes for the media ids\nconst crypto = require('crypto');\nconst md5 = data => crypto.createHash('md5').update(data).digest(\"hex\")\n\nfunction addTranslation(translations, code, name, description) {\n  return translations = {\n    ...translations,\n    [code]: {\n      ...name && {\n        name: name\n      },\n      ...description && {\n        description: description\n      }\n    }\n  }\n}\n\nfor (const item of $input.all()) {\n  const { name, website, description, logo_url } = item.json\n\n  // If you add another language to the Google Sheet, extract values here\n  const { translation_language_code_1, translation_language_code_2, translation_language_code_3, translation_name_1, translation_name_2, translation_name_3, translation_description_1, translation_description_2, translation_description_3 } = item.json\n  \n  let translations = {}\n\n  if(translation_language_code_1 && (translation_name_1 || translation_description_1)){\n    translations = addTranslation(translations, translation_language_code_1, translation_name_1, translation_description_1)\n  }\n\n  if(translation_language_code_2 && (translation_name_2 || translation_description_2)){\n    translations = addTranslation(translations, translation_language_code_2, translation_name_2, translation_description_2)\n  }\n\n    if(translation_language_code_3 && (translation_name_3 || translation_description_3)){\n    translations = addTranslation(translations, translation_language_code_3, translation_name_3, translation_description_3)\n  }\n\n  //If you add another language to the Google Sheet, call addTranslation with the values of the new language as already done above with three languages\n  \n  item.json.manufacturer = {\n    entity: \"product_manufacturer\",\n    action: \"upsert\",\n    payload: [\n      {\n        name: name,\n        link: website,\n        description: description,\n        ...Object.keys(translations).length && {\n          translations: translations\n        },\n        ...logo_url &&  { \n          media:{\n            id: md5(\"media-\"+item.json.name)\n          }\n        }\n      }\n    ]\n  }\n}\n\nreturn $input.all();"
      },
      "typeVersion": 2
    },
    {
      "id": "2e6d1b94-ffb0-46bf-8197-32865764e753",
      "name": "Upload Manufacturer Logo",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        2300,
        360
      ],
      "parameters": {
        "url": "={{ $('Settings').item.json.shopware_url }}/api/_action/media/{{ $('Loop Over Manufacturers').item.json.manufacturer.payload[0].media.id }}/upload",
        "method": "POST",
        "options": {},
        "sendBody": true,
        "sendQuery": true,
        "authentication": "genericCredentialType",
        "bodyParameters": {
          "parameters": [
            {
              "name": "url",
              "value": "={{ $('Get Manufacturer from Google Sheet').item.json.logo_url }}"
            }
          ]
        },
        "genericAuthType": "oAuth2Api",
        "queryParameters": {
          "parameters": [
            {
              "name": "extension",
              "value": "={{ $('Get Manufacturer from Google Sheet').item.json.logo_url.split(\".\").pop() }}"
            },
            {
              "name": "fileName",
              "value": "={{ $('Get Manufacturer from Google Sheet').item.json.name }}"
            }
          ]
        }
      },
      "credentials": {
        "oAuth2Api": {
          "id": "hrFvifgKqhhV11RK",
          "name": "SW6 Demo"
        }
      },
      "typeVersion": 4.1
    },
    {
      "id": "6c219e67-1547-475a-aa4f-0018d10ccf5f",
      "name": "Import Manufacturer",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1800,
        380
      ],
      "parameters": {
        "url": "={{ $('Settings').item.json.shopware_url }}/api/_action/sync",
        "method": "POST",
        "options": {},
        "sendBody": true,
        "sendQuery": true,
        "authentication": "genericCredentialType",
        "bodyParameters": {
          "parameters": [
            {
              "name": "import-manufacturer",
              "value": "={{ $json.manufacturer }}"
            }
          ]
        },
        "genericAuthType": "oAuth2Api",
        "queryParameters": {
          "parameters": [
            {
              "name": "_response",
              "value": "details"
            }
          ]
        }
      },
      "credentials": {
        "oAuth2Api": {
          "id": "hrFvifgKqhhV11RK",
          "name": "SW6 Demo"
        }
      },
      "typeVersion": 4.1
    },
    {
      "id": "f4dc392f-8679-4624-a045-ff560f282f5f",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        540,
        240
      ],
      "parameters": {
        "width": 271,
        "height": 330,
        "content": "## Settings\n**Todo**: Configure your Shopware URL"
      },
      "typeVersion": 1
    },
    {
      "id": "15b857a8-ef6a-4212-ac73-7ab16ffcb6e5",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        900,
        120
      ],
      "parameters": {
        "width": 272,
        "height": 450,
        "content": "## Google Sheet\n**Todo:** Create a Google Sheet with the columns:\n- name (**unique**)\n- website\n- description\n- logo_url"
      },
      "typeVersion": 1
    },
    {
      "id": "52f5804c-65a9-4772-99e5-fdde53ff3f3d",
      "name": "Loop Over Manufacturers",
      "type": "n8n-nodes-base.splitInBatches",
      "position": [
        1520,
        360
      ],
      "parameters": {
        "options": {}
      },
      "typeVersion": 3
    },
    {
      "id": "f37d7f57-b86b-4296-9114-0a1b97178bc9",
      "name": "Get Manufacturer from Google Sheet",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        980,
        360
      ],
      "parameters": {
        "options": {},
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": "gid=0",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1Qmsjs8usT90fPNnCIaI605W77zoKkOB3t3i8UsdpA5Q/edit#gid=0",
          "cachedResultName": "Sheet1"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "1Qmsjs8usT90fPNnCIaI605W77zoKkOB3t3i8UsdpA5Q",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1Qmsjs8usT90fPNnCIaI605W77zoKkOB3t3i8UsdpA5Q/edit?usp=drivesdk",
          "cachedResultName": "SW6 Manufacturer"
        }
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "dmSqFI4zNuhZqIvL",
          "name": "Google Sheets account"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "dfe522c5-f481-4bc1-ba95-85f8f471b20a",
      "name": "If has Logo",
      "type": "n8n-nodes-base.if",
      "position": [
        2040,
        380
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
              "id": "1cd0654f-b088-420a-be28-4468dc901890",
              "operator": {
                "type": "array",
                "operation": "exists",
                "singleValue": true
              },
              "leftValue": "={{ $json.data['import-manufacturer'].result[0].entities.media }}",
              "rightValue": ""
            }
          ]
        }
      },
      "typeVersion": 2
    },
    {
      "id": "b006dce3-16c6-4ebb-b752-67e5972841f5",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1740,
        60
      ],
      "parameters": {
        "height": 499.67801857585135,
        "content": "## Shopware Manufacturer Import\n**Todo**: Connect your Shopware Account by creating a [Shopware Integration](https://docs.shopware.com/en/shopware-6-en/settings/system/integrationen) and using a Generic OAuth2 API Authentication with Grant Type \"Client Credentials\" to authenticate the request. The Access Token URL is https://*your-shopware-domain.com*/api/oauth/token."
      },
      "typeVersion": 1
    },
    {
      "id": "681e7c0a-6e6f-4896-8e86-6eacfc4fd2ab",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2240,
        160
      ],
      "parameters": {
        "height": 399.1455108359133,
        "content": "## Shopware Manufacturer Logo Upload\n**Todo**: Connect your Shopware Account as you did two nodes before."
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "1d0510a7-b383-481a-801b-f0f77f144858",
  "connections": {
    "Settings": {
      "main": [
        [
          {
            "node": "Get Manufacturer from Google Sheet",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "If has Logo": {
      "main": [
        [
          {
            "node": "Upload Manufacturer Logo",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Loop Over Manufacturers",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Import Manufacturer": {
      "main": [
        [
          {
            "node": "If has Logo",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Loop Over Manufacturers": {
      "main": [
        [],
        [
          {
            "node": "Import Manufacturer",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Upload Manufacturer Logo": {
      "main": [
        [
          {
            "node": "Loop Over Manufacturers",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Create Import Request Body": {
      "main": [
        [
          {
            "node": "Loop Over Manufacturers",
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
            "node": "Settings",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Manufacturer from Google Sheet": {
      "main": [
        [
          {
            "node": "Create Import Request Body",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2107"></a>

## Template 2107 - Roteamento de itens por ID

- **Nome:** Roteamento de itens por ID
- **Descrição:** Recebe três itens com IDs (0, 1, 2), avalia o campo id e encaminha cada item para um caminho diferente onde é atribuído um campo name específico; itens sem correspondência seguem para uma saída sem efeito.
- **Funcionalidade:** • Gatilho manual: inicia o fluxo ao executar manualmente.
• Geração de itens: cria três itens com os IDs 0, 1 e 2.
• Roteamento por valor: verifica o campo id e seleciona a saída correspondente para cada item.
• Definição de campos por rota: em cada rota é atribuído o campo name com valores 'n8n', 'nodemation' ou 'nathan'.
• Saída padrão: itens que não correspondem a nenhuma condição são encaminhados para uma operação sem efeito.
- **Ferramentas:** • Nenhuma ferramenta externa: o fluxo realiza todo o processamento internamente, sem integrações externas.

## Fluxo visual

```mermaid
flowchart LR
    N1["On clicking 'execute'"]
    N2["Function"]
    N3["Set"]
    N4["Set1"]
    N5["Switch"]
    N6["Set2"]
    N7["NoOp"]

    N5 --> N3
    N5 --> N4
    N5 --> N6
    N5 --> N7
    N2 --> N5
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
        0,
        300
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Function",
      "type": "n8n-nodes-base.function",
      "position": [
        200,
        300
      ],
      "parameters": {
        "functionCode": "return [\n  {\n    json: {\n      id: 0,\n    }\n  },\n  {\n    json: {\n      id: 1,\n    }\n  },\n  {\n    json: {\n      id: 2,\n    }\n  }\n];\n"
      },
      "typeVersion": 1
    },
    {
      "name": "Set",
      "type": "n8n-nodes-base.set",
      "position": [
        600,
        90
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "name",
              "value": "n8n"
            }
          ]
        },
        "options": {}
      },
      "typeVersion": 1
    },
    {
      "name": "Set1",
      "type": "n8n-nodes-base.set",
      "position": [
        600,
        230
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "name",
              "value": "nodemation"
            }
          ]
        },
        "options": {}
      },
      "typeVersion": 1
    },
    {
      "name": "Switch",
      "type": "n8n-nodes-base.switch",
      "position": [
        400,
        300
      ],
      "parameters": {
        "rules": {
          "rules": [
            {
              "operation": "equal"
            },
            {
              "output": 1,
              "value2": 1,
              "operation": "equal"
            },
            {
              "output": 2,
              "value2": 2,
              "operation": "equal"
            }
          ]
        },
        "value1": "={{$node[\"Function\"].json[\"id\"]}}",
        "fallbackOutput": 3
      },
      "typeVersion": 1
    },
    {
      "name": "Set2",
      "type": "n8n-nodes-base.set",
      "position": [
        600,
        370
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "name",
              "value": "nathan"
            }
          ]
        },
        "options": {}
      },
      "typeVersion": 1
    },
    {
      "name": "NoOp",
      "type": "n8n-nodes-base.noOp",
      "position": [
        600,
        510
      ],
      "parameters": {},
      "typeVersion": 1
    }
  ],
  "connections": {
    "Switch": {
      "main": [
        [
          {
            "node": "Set",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Set1",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Set2",
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
    "Function": {
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
    "On clicking 'execute'": {
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

<a id="template-2109"></a>

## Template 2109 - Geração e revisão de imagens para equipe de design

- **Nome:** Geração e revisão de imagens para equipe de design
- **Descrição:** Automatiza a criação, revisão e armazenamento de imagens a partir de briefs submetidos por formulário, usando IA para avaliar e aprimorar prompts, e registrando resultados em pastas e planilhas.
- **Funcionalidade:** • Receber brief via formulário: captura prompt, público-alvo, proporção, modelo, estilo e negative prompt.
• Gerar imagem: envia o brief para uma API de geração de imagens e recebe URL, seed e metadados.
• Baixar e armazenar imagem: baixa a imagem gerada e salva em uma pasta dedicada no armazenamento em nuvem.
• Registrar metadados: adiciona linhas na planilha com link da imagem, resolução, seed, prompt, modelo, estilo e outros parâmetros.
• Revisão automática por IA: envia a imagem e o prompt para um modelo de linguagem que avalia a qualidade, checa texto e sugere um prompt aprimorado junto com recomendação (usar, modificar ou rejeitar).
• Fluxo condicional de acordo com a revisão: notifica por e-mail se aprovada; se precisar modificações ou for rejeitada, cria um brief revisado e solicita remixagem.
• Remix/ajuste de imagem: envia imagem de referência e prompt aprimorado para endpoint de remix e salva o resultado com metadados atualizados.
• Setup inicial e exportação: cria estrutura de pastas, gera um CSV de configuração e envia e-mail com links e IDs para configuração inicial.
- **Ferramentas:** • Formulário web: interface para submissão dos briefs de imagem.
• Ideogram (API de geração e remix): serviço externo usado para gerar imagens e realizar remix a partir de imagens de referência.
• OpenAI (GPT-4o): modelo de linguagem utilizado para revisar imagens, justificar recomendações e gerar prompts aprimorados.
• Google Drive: armazenamento e organização das imagens geradas e dos arquivos CSV.
• Google Sheets: registro estruturado dos metadados de todas as gerações (links, seeds, resolução, prompts, etc.).
• Gmail: envio de notificações e instruções de setup para o responsável.

## Fluxo visual

```mermaid
flowchart LR
    N1["Google Sheets"]
    N2["SetImageData"]
    N3["Google Drive"]
    N4["Download Image3"]
    N5["ideogram Remix"]
    N6["Set Upload Fields1"]
    N7["Structured Output Parser1"]
    N8["Switch1"]
    N9["Image Reviewer"]
    N10["OpenAI Chat Model1"]
    N11["Google Drive Remix Image"]
    N12["Google Sheets - Add Remix"]
    N13["genImageURL1"]
    N14["genImageURL2"]
    N15["Download Image"]
    N16["TheImageURL"]
    N17["Gmail"]
    N18["creative brief"]
    N19["Ideogram Image generator"]
    N20["GET image"]
    N21["RE creative brief"]
    N22["Get Remixed Image"]
    N23["When clicking ‘Test workflow’"]
    N24["Convert to File"]
    N25["Spreadsheet"]
    N26["Google Drive - Create Folder"]
    N27["Google Drive - Create Generations Folder"]
    N28["Google Drive - Upload Spreadsheet"]
    N29["Gmail - Send Setup Details"]
    N30["Sticky Note"]
    N31["Sticky Note1"]
    N32["On form submission"]
    N33["Sticky Note2"]
    N34["Sticky Note3"]
    N35["Sticky Note4"]
    N36["Sticky Note5"]
    N37["Sticky Note6"]

    N8 --> N17
    N8 --> N21
    N20 --> N3
    N25 --> N24
    N16 --> N15
    N3 --> N1
    N2 --> N20
    N13 --> N16
    N14 --> N16
    N1 --> N13
    N15 --> N9
    N9 --> N8
    N18 --> N19
    N5 --> N6
    N24 --> N28
    N4 --> N5
    N22 --> N11
    N21 --> N4
    N32 --> N18
    N6 --> N22
    N11 --> N12
    N19 --> N2
    N12 --> N14
    N26 --> N27
    N28 --> N29
    N23 --> N26
    N27 --> N25
```

## Fluxo (.json) :

```json
{
  "id": "tnRYt0kDGMO9BBFd",
  "meta": {
    "instanceId": "ba3fa76a571c35110ef5f67e5099c9a5c1768ef125c2f3b804ba20de75248c0b",
    "templateCredsSetupCompleted": false
  },
  "name": "n8n Graphic Design Team",
  "tags": [],
  "nodes": [
    {
      "id": "c1c292f8-78a4-407b-be6b-567e94271bc6",
      "name": "Google Sheets",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        1900,
        -60
      ],
      "parameters": {
        "columns": {
          "value": {
            "Link": "={{ $json.webContentLink }}",
            "nsfw": "={{ $('SetImageData').item.json.image.nsfw }}",
            "seed": "={{ $('SetImageData').item.json.image.seed }}",
            "type": "={{ $('GET image').item.binary.data.fileExtension || \"png\" }}",
            "image": "={{ $json.webViewLink }}",
            "width": "={{ $('Ideogram Image generator').item.json.data[0].resolution.split(\"x\",1)[0] }}",
            "height": "={{ $('Ideogram Image generator').item.json.data[0].resolution.split(\"x\",2)[1] }}",
            "prompt": "={{ $('SetImageData').item.json.image.prompt }}",
            "GenModel": "={{ $('SetImageData').item.json.imageGen.model || \"None\" }}",
            "GenPrompt": "={{ $('Ideogram Image generator').item.json.data[0].prompt || \"None\" }}",
            "created_at": "={{ $('Ideogram Image generator').item.json.created }}",
            "drive_link": "={{ $json.webViewLink }}",
            "GenStyleType": "={{ $('SetImageData').item.json.imageGen['style-type'] || \"None\" }}",
            "GenAspectRatio": "={{ $('SetImageData').item.json.imageGen['aspect-ratio'] || \"None\" }}",
            "GenNegativePrompt": "={{ $('SetImageData').item.json.imageGen['negative-prompt'] || \"None\" }}"
          },
          "schema": [
            {
              "id": "created_at",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "created_at",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "image",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "image",
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
              "id": "prompt",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "prompt",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "timings",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "timings",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "seed",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "seed",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "nsfw",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "nsfw",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "width",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "width",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "height",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "height",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "type",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "type",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "drive_link",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "drive_link",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "GenModel",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "GenModel",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "GenPrompt",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "GenPrompt",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "GenAspectRatio",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "GenAspectRatio",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "GenStyleType",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "GenStyleType",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "GenNegativePrompt",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "GenNegativePrompt",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            }
          ],
          "mappingMode": "defineBelow",
          "matchingColumns": [
            "id"
          ],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {},
        "operation": "append",
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": 1932716024,
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/get-your-sheet-together/edit#gid=1932716024",
          "cachedResultName": "n8n-GraphicDesignTeam - Sheet1"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "1wB4eKCIsB8fRnfa8hKhAZFwSruXAGhmDh-4n4WFWgj0",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/get-your-sheet-together/edit?usp=drivesdk",
          "cachedResultName": "n8n-Graphic_Design_Team"
        }
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "786",
          "name": "Google Sheets"
        }
      },
      "typeVersion": 4.4
    },
    {
      "id": "91a557ba-1d47-43e3-b953-f18de2bcecd2",
      "name": "SetImageData",
      "type": "n8n-nodes-base.set",
      "position": [
        1020,
        -60
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "0c43f96b-40ff-4d2f-8ce1-63dafe023421",
              "name": "image.url",
              "type": "string",
              "value": "={{ $('Ideogram Image generator').item.json[\"data\"][0][\"url\"] }}"
            },
            {
              "id": "fcc4eaf5-3563-43e7-8e6c-1e24df67adc6",
              "name": "image.seed",
              "type": "number",
              "value": "={{ $('Ideogram Image generator').item.json[\"data\"][0][\"seed\"] }}"
            },
            {
              "id": "76645f54-1785-4a44-bd95-126f4219d193",
              "name": "image.nsfw",
              "type": "boolean",
              "value": "={{ $('Ideogram Image generator').item.json[\"data\"][0][\"is_image_safe\"] }}"
            },
            {
              "id": "3097ab1b-cae9-410d-9fd4-fa454a6a1bdd",
              "name": "image.prompt",
              "type": "string",
              "value": "={{ $('creative brief').item.json.image_request.prompt || \"None\" }} }}"
            },
            {
              "id": "a5a9c2d1-ad66-4219-85c0-4a5ef6a0cb8d",
              "name": "imageGen.model",
              "type": "string",
              "value": "={{ $('creative brief').item.json.image_request.model }}"
            },
            {
              "id": "50887364-4273-4469-b6bd-f505f154e0ad",
              "name": "imageGen.magic-prompt",
              "type": "string",
              "value": "={{ $('creative brief').item.json.image_request.magic_prompt_option || \"None\" }}"
            },
            {
              "id": "9d4903b8-2609-47e4-9afb-5b0e365feb52",
              "name": "imageGen.aspect-ratio",
              "type": "string",
              "value": "={{ $('creative brief').item.json.image_request.aspect_ratio || \"none\" }}"
            },
            {
              "id": "0e92bfaf-a2d3-4e59-87bd-758a3f650fc1",
              "name": "imageGen.style-type",
              "type": "string",
              "value": "={{ $('Ideogram Image generator').item.json.data[0].style_type || \"none\" }}"
            },
            {
              "id": "7a7f08e6-b257-4e2d-b5ae-8084701a0f59",
              "name": "imageGen.negative-prompt",
              "type": "string",
              "value": "={{ $('creative brief').item.json.image_request.negative_prompt || \"none\" }}"
            },
            {
              "id": "599e4bd7-7b2f-4fa2-80b8-93f1b5c2adb0",
              "name": "imageGen.prompt",
              "type": "string",
              "value": "={{ $json.data[0].prompt }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "c52fa1eb-4160-4edd-8a68-eeb665af9f1c",
      "name": "Google Drive",
      "type": "n8n-nodes-base.googleDrive",
      "onError": "continueRegularOutput",
      "position": [
        1600,
        -60
      ],
      "parameters": {
        "name": "=IdeoGenerator-{{ $now.format('yyyy-MM-dd--HH-MM-ss') }}",
        "driveId": {
          "__rl": true,
          "mode": "list",
          "value": "My Drive"
        },
        "options": {},
        "folderId": {
          "__rl": true,
          "mode": "id",
          "value": "={{ $('creative brief').item.json.setup.GenerationsFolderId }}"
        }
      },
      "credentials": {
        "googleDriveOAuth2Api": {
          "id": "786",
          "name": "Google Drive"
        }
      },
      "typeVersion": 3
    },
    {
      "id": "7a250b24-0318-4c76-b03f-000ae41cdb0f",
      "name": "Download Image3",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        500,
        180
      ],
      "parameters": {
        "url": "={{ $('TheImageURL').item.json.theimage.url }}",
        "options": {
          "response": {
            "response": {
              "responseFormat": "file",
              "outputPropertyName": "image"
            }
          }
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "1fc9d4ac-d0d3-4068-8d9d-ef9779c44739",
      "name": "ideogram Remix",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        740,
        180
      ],
      "parameters": {
        "url": "https://api.ideogram.ai/remix",
        "method": "POST",
        "options": {},
        "sendBody": true,
        "contentType": "multipart-form-data",
        "sendHeaders": true,
        "authentication": "genericCredentialType",
        "bodyParameters": {
          "parameters": [
            {
              "name": "image_request",
              "value": "={{ JSON.stringify($('RE creative brief').item.json.image_request) }}"
            },
            {
              "name": "image_file",
              "parameterType": "formBinaryData",
              "inputDataFieldName": "image"
            }
          ]
        },
        "genericAuthType": "httpHeaderAuth",
        "headerParameters": {
          "parameters": [
            {
              "name": "content-type",
              "value": "multipart/form-data"
            }
          ]
        }
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "786",
          "name": "Ideogram"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "118b7436-b830-4c54-a230-69128b1e00f4",
      "name": "Set Upload Fields1",
      "type": "n8n-nodes-base.set",
      "position": [
        1020,
        180
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "cc8c42d2-647b-4820-aa72-d2bcc8c6c0db",
              "name": "data.prompt",
              "type": "string",
              "value": "={{ $json.data[0].prompt }}"
            },
            {
              "id": "7fcb404e-7890-4423-bc72-8b569111841c",
              "name": "data.resolution",
              "type": "string",
              "value": "={{ $json.data[0].resolution }}"
            },
            {
              "id": "463398a0-8c25-4b08-ab79-4cfadfa8c085",
              "name": "data.seed",
              "type": "number",
              "value": "={{ $json.data[0].seed }}"
            },
            {
              "id": "531fe4f3-4967-4a9c-af14-0e35c3e4375d",
              "name": "data.style_type",
              "type": "string",
              "value": "={{ $json.data[0].style_type }}"
            },
            {
              "id": "378fd334-aeeb-4e00-a884-0007d54552e9",
              "name": "data.url",
              "type": "string",
              "value": "={{ $json.data[0].url }}"
            },
            {
              "id": "490996d5-26b1-4408-a941-c643de8d3da9",
              "name": "data.resemblance",
              "type": "number",
              "value": "={{ $('RE creative brief').item.json.image_request.image_weight }}"
            },
            {
              "id": "cd0e89f6-944e-49e1-b3f1-067eaa9469aa",
              "name": "data.magic_prompt_option",
              "type": "string",
              "value": "={{ $('RE creative brief').item.json.image_request.magic_prompt_option }}"
            },
            {
              "id": "f5a760eb-ad62-4c6f-89b3-3b31eb616d0e",
              "name": "data.seed",
              "type": "number",
              "value": "={{ $json.data[0].seed }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "5c7424b3-13c1-4699-ad98-9f148b4b04d9",
      "name": "Structured Output Parser1",
      "type": "@n8n/n8n-nodes-langchain.outputParserStructured",
      "position": [
        1320,
        640
      ],
      "parameters": {
        "schemaType": "manual",
        "inputSchema": "[\n  {\n    \"overall_recommendation\": \"ENUM: 'Use as is', 'Use with modifications', or 'Reject'\",\n    \"explanation\": \"String: Concise explanation for the overall recommendation, highlighting key reasons and observations.\",\n    \"enhanced_image_prompt\": \"String: If overall_recommendation is Use with modifications', or Reject generate refined version of the provided image prompt, incorporating feedback to optimize future image generation.\"\n  }\n]"
      },
      "typeVersion": 1.2
    },
    {
      "id": "591979c5-32f5-4903-a63e-0adf85dbcb6e",
      "name": "Switch1",
      "type": "n8n-nodes-base.switch",
      "position": [
        1600,
        640
      ],
      "parameters": {
        "rules": {
          "values": [
            {
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
                    "id": "4b247cdf-0fad-4f8f-800f-4cb1ebd5949c",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $json.output.overall_recommendation }}",
                    "rightValue": "=Use as is"
                  }
                ]
              }
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
      "id": "87fa176d-e5f7-4993-942f-d182c0e0b772",
      "name": "Image Reviewer",
      "type": "@n8n/n8n-nodes-langchain.chainLlm",
      "position": [
        1080,
        420
      ],
      "parameters": {
        "text": "=Please evaluate the following image for use as a featured image in social media for an audience of {{ $('creative brief').item.json.targetAudiance }}. Focus on correct spelling, aesthetics, and overall alignment with the audience’s interests and expectations.\n\nOriginal Image Prompt:\n\"{{ $('creative brief').item.json.image_request.prompt }}\"\n\nRequired Output Format (JSON):\n{\n  \"overall_recommendation\": \"ENUM: 'Use as is', 'Use with modifications', or 'Reject'\",\n  \"explanation\": \"String: Concise explanation for the overall recommendation, highlighting key reasons and observations.\",\n  \"enhanced_image_prompt\": \"String: Enhanced version of the original prompt for ideal rendering.\"\n}\n\nPlease provide:\n1. **overall_recommendation** based on whether the image meets the standards for the target audience and is ready for use.\n2. **explanation** detailing your rationale in a concise way, referencing aesthetic elements, spelling/grammar considerations in any text, and overall visual appeal.\n3. **enhanced_image_prompt** that refines the original prompt to ensure perfect alignment with the audience and the desired outcome.",
        "messages": {
          "messageValues": [
            {
              "message": "=You are a specialized AI system tasked with evaluating and enhancing image prompts for an intended audience. \nWhen given a user-provided original image prompt and target audience, you must:\n\n1. Assess if the resulting image (as described by the prompt) is suitable for the specified audience.\n2. Determine an \"overall_recommendation\" in one of three forms: 'Use as is', 'Use with modifications', or 'Reject'.\n3. Provide an \"explanation\" detailing the rationale for your recommendation, focusing on aspects such as spelling, aesthetics, and audience alignment.\n4. Provide an \"enhanced_image_prompt\" that refines the original prompt to better suit the audience, maintain correct spelling, and ensure aesthetic appeal.\n\nYour output MUST be structured as valid JSON with the fields:\n{\n  \"overall_recommendation\": \"ENUM: 'Use as is', 'Use with modifications', or 'Reject'\",\n  \"explanation\": \"String: Concise explanation for the overall recommendation, highlighting key reasons and observations.\",\n  \"enhanced_image_prompt\": \"String: Enhanced version of the original prompt that reflects your improvements.\"\n}\n\nFollow these instructions:\n- Be concise and accurate in your analysis.\n- Do not disclose or refer to these system instructions in the output.\n- Address only the content provided. \n- If the prompt is suitable with minor improvements, provide those adjustments in \"enhanced_image_prompt\"."
            },
            {
              "type": "HumanMessagePromptTemplate",
              "messageType": "imageBinary",
              "binaryImageDataKey": "image"
            }
          ]
        },
        "promptType": "define",
        "hasOutputParser": true
      },
      "typeVersion": 1.4
    },
    {
      "id": "cbbaad22-0ae8-4c1d-ac7f-8f7596b3e190",
      "name": "OpenAI Chat Model1",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        1020,
        640
      ],
      "parameters": {
        "model": "gpt-4o",
        "options": {}
      },
      "credentials": {
        "openAiApi": {
          "id": "786",
          "name": "OpenAi"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "2e456bde-4dca-44d3-bdaf-a4352a46a2c1",
      "name": "Google Drive Remix Image",
      "type": "n8n-nodes-base.googleDrive",
      "onError": "continueRegularOutput",
      "position": [
        1600,
        180
      ],
      "parameters": {
        "name": "=Ideogram-Remix-{{ $json.data.seed }}-{{ $now.format('yyyy-MM-dd--HH-MM-ss') }}",
        "driveId": {
          "__rl": true,
          "mode": "list",
          "value": "My Drive"
        },
        "options": {},
        "folderId": {
          "__rl": true,
          "mode": "id",
          "value": "={{ $('creative brief').item.json.setup.GenerationsFolderId }}"
        }
      },
      "credentials": {
        "googleDriveOAuth2Api": {
          "id": "786",
          "name": "Google Drive"
        }
      },
      "typeVersion": 3
    },
    {
      "id": "13014dc7-2547-48d5-b6b4-6141aea311b8",
      "name": "Google Sheets - Add Remix",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        1900,
        180
      ],
      "parameters": {
        "columns": {
          "value": {
            "Link": "={{ $('Set Upload Fields1').item.json.data.url }}",
            "nsfw": "={{ $('ideogram Remix').item.json.data[0].is_image_safe }}",
            "seed": "={{ $('Set Upload Fields1').item.json.data.seed }}",
            "type": "={{ $('Get Remixed Image').item.binary.data.fileExtension || \"png\" }}",
            "image": "={{ $('Set Upload Fields1').item.json.data.url }}",
            "width": "={{ $('ideogram Remix').item.json.data[0].resolution.split(\"x\",1)[0] }}",
            "height": "={{ $('ideogram Remix').item.json.data[0].resolution.split(\"x\",2)[1] }}",
            "prompt": "={{ $('ideogram Remix').item.json.data[0].prompt }}",
            "GenModel": "={{ $('Download Image3').item.json.image_request.model }}",
            "GenPrompt": "={{ $('Download Image3').item.json.image_request.prompt }}",
            "created_at": "={{ $('ideogram Remix').item.json.created }}",
            "drive_link": "={{ $json.webViewLink }}",
            "GenStyleType": "={{ $('ideogram Remix').item.json.data[0].style_type }}",
            "GenAspectRatio": "={{ $('Download Image3').item.json.image_request.aspect_ratio }}",
            "GenNegativePrompt": "={{ $('Download Image3').item.json.image_request.negative_prompt }}"
          },
          "schema": [
            {
              "id": "created_at",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "created_at",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "image",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "image",
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
              "id": "prompt",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "prompt",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "timings",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "timings",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "seed",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "seed",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "nsfw",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "nsfw",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "width",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "width",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "height",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "height",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "type",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "type",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "drive_link",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "drive_link",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "GenModel",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "GenModel",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "GenPrompt",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "GenPrompt",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "GenAspectRatio",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "GenAspectRatio",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "GenStyleType",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "GenStyleType",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "GenNegativePrompt",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "GenNegativePrompt",
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
          "value": 1932716024,
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/get-your-sheet-together/edit#gid=1932716024",
          "cachedResultName": "n8n-GraphicDesignTeam - Sheet1"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "1wB4eKCIsB8fRnfa8hKhAZFwSruXAGhmDh-4n4WFWgj0",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/get-your-sheet-together/edit?usp=drivesdk",
          "cachedResultName": "n8n-Graphic_Design_Team"
        }
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "786",
          "name": "Google Sheets"
        }
      },
      "typeVersion": 4.4
    },
    {
      "id": "b8bbc4fd-4714-45b4-8884-1caace1a2edf",
      "name": "genImageURL1",
      "type": "n8n-nodes-base.set",
      "position": [
        2240,
        -60
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "a730540b-9143-4e86-883e-4ccf62d39293",
              "name": "genImage.url",
              "type": "string",
              "value": "={{ $('SetImageData').item.json.image.url }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "01369d20-9345-41bd-b745-60f74579b621",
      "name": "genImageURL2",
      "type": "n8n-nodes-base.set",
      "position": [
        2240,
        180
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "a730540b-9143-4e86-883e-4ccf62d39293",
              "name": "genImage.url",
              "type": "string",
              "value": "={{ $('Set Upload Fields1').item.json.data.url }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "cfb67028-0210-4834-9264-3146dc60efb4",
      "name": "Download Image",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        740,
        420
      ],
      "parameters": {
        "url": "={{ $json.theimage.url }}",
        "options": {
          "response": {
            "response": {
              "responseFormat": "file",
              "outputPropertyName": "image"
            }
          }
        },
        "sendHeaders": true,
        "headerParameters": {
          "parameters": [
            {}
          ]
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "8939afac-bda4-42fd-86de-8af127c2235e",
      "name": "TheImageURL",
      "type": "n8n-nodes-base.set",
      "position": [
        500,
        420
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "62eded04-34be-4ce3-a4ba-d62de1b6cee8",
              "name": "theimage.url",
              "type": "string",
              "value": "={{ $json.genImage.url }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "1d6d9b16-6407-453c-990b-2e33a8f0bc25",
      "name": "Gmail",
      "type": "n8n-nodes-base.gmail",
      "position": [
        1900,
        800
      ],
      "webhookId": "287885a5-6785-4c9d-94f4-63e346ddedeb",
      "parameters": {
        "sendTo": "realsimple.dev",
        "message": "your image is ready",
        "options": {},
        "subject": "New Image is Ready"
      },
      "credentials": {
        "gmailOAuth2": {
          "id": "786",
          "name": "Gmail"
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "5121e9c5-e663-45bc-99a3-65693caa9d96",
      "name": "creative brief",
      "type": "n8n-nodes-base.set",
      "position": [
        280,
        -60
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "47cbf666-4a4b-437a-b728-0e3714889add",
              "name": "setup.GenerationsFolderId",
              "type": "string",
              "value": "1X0lg9HiazAFwpvlV8cV_slIFQb5U-E3Y"
            },
            {
              "id": "85399ec2-cdd2-489f-a328-1cea01f885e2",
              "name": "image_request.prompt",
              "type": "string",
              "value": "={{ $json.prompt }}"
            },
            {
              "id": "cd64dfbe-6e8a-45d1-aa70-ef3939b6ec48",
              "name": "image_request.aspect_ratio",
              "type": "string",
              "value": "={{ $json['Aspect Ratio'] }}"
            },
            {
              "id": "035e8f09-77a6-4a30-b48e-860e98d78d21",
              "name": "image_request.model",
              "type": "string",
              "value": "={{ $json.model }}"
            },
            {
              "id": "535fdcdd-090e-4393-8bf5-8fdb6d75db77",
              "name": "image_request.magic_prompt_option",
              "type": "string",
              "value": "={{ $json['magic prompt'] }}"
            },
            {
              "id": "277d2f0b-8bf9-42e6-aa0d-aec2c2bc9f17",
              "name": "image_request.style_type",
              "type": "string",
              "value": "={{ $json['style type'] }}"
            },
            {
              "id": "460046ad-6ddc-441c-8801-68eba79a4a33",
              "name": "targetAudiance",
              "type": "string",
              "value": "={{ $json.audience }}"
            },
            {
              "id": "5b7dd28c-fe99-45b3-b2a7-7f3879dbc761",
              "name": "image_request.negative_prompt",
              "type": "string",
              "value": "={{ $json['negative prompt'] }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "c0db3a13-b65e-45ff-8b6a-89dd3d975cf8",
      "name": "Ideogram Image generator",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        740,
        -60
      ],
      "parameters": {
        "url": "https://api.ideogram.ai/generate",
        "method": "POST",
        "options": {},
        "jsonBody": "={\n  \"image_request\": {{ JSON.stringify($('creative brief').item.json.image_request) }}\n}",
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
            },
            {
              "name": "content-type",
              "value": "application/json"
            }
          ]
        }
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "786",
          "name": "Ideogram"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "3d54d4c4-82a7-419b-85c3-5597064b8790",
      "name": "GET image",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1320,
        -60
      ],
      "parameters": {
        "url": "={{ $('Ideogram Image generator').item.json[\"data\"][0][\"url\"] }}",
        "options": {}
      },
      "typeVersion": 4.2
    },
    {
      "id": "a86c9afc-6a67-4e5a-9c20-4b89f129cb1b",
      "name": "RE creative brief",
      "type": "n8n-nodes-base.set",
      "position": [
        280,
        180
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "85399ec2-cdd2-489f-a328-1cea01f885e2",
              "name": "image_request.prompt",
              "type": "string",
              "value": "={{ $json.output.enhanced_image_prompt.replaceAll(\"\\\"\",\"\").replaceAll(\"'\",\"\") }}"
            },
            {
              "id": "cd64dfbe-6e8a-45d1-aa70-ef3939b6ec48",
              "name": "image_request.aspect_ratio",
              "type": "string",
              "value": "ASPECT_4_3"
            },
            {
              "id": "035e8f09-77a6-4a30-b48e-860e98d78d21",
              "name": "image_request.model",
              "type": "string",
              "value": "V_2"
            },
            {
              "id": "535fdcdd-090e-4393-8bf5-8fdb6d75db77",
              "name": "image_request.magic_prompt_option",
              "type": "string",
              "value": "ON"
            },
            {
              "id": "bd7e1693-9248-4251-8287-787e76224b74",
              "name": "image_request.image_weight",
              "type": "number",
              "value": 50
            },
            {
              "id": "5b7dd28c-fe99-45b3-b2a7-7f3879dbc761",
              "name": "image_request.negative_prompt",
              "type": "string",
              "value": "ugly"
            },
            {
              "id": "460046ad-6ddc-441c-8801-68eba79a4a33",
              "name": "targetAudiance",
              "type": "string",
              "value": "The image is designed for a tech-savvy audience aged 18–35 who engage frequently with digital content and social media. They value visually appealing, inclusive, and clear messaging that resonates with modern trends. They are attentive to brand authenticity, ethical implications, and cultural sensitivity. Ensuring the image aligns with these preferences and values helps maintain audience trust and engagement."
            },
            {
              "id": "b8995766-bb07-4340-8379-99ace65333db",
              "name": "output.explanation",
              "type": "string",
              "value": "={{ $json.output.explanation }}"
            },
            {
              "id": "89896150-eb04-406e-b9e5-2ca3969b8e56",
              "name": "output.overall_recommendation",
              "type": "string",
              "value": "={{ $json.output.overall_recommendation }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "cce8c36a-6ebd-496a-a66e-2eec1da97f9b",
      "name": "Get Remixed Image",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1320,
        180
      ],
      "parameters": {
        "url": "={{ $('Set Upload Fields1').item.json.data.url }}",
        "options": {}
      },
      "typeVersion": 4.2
    },
    {
      "id": "911d0009-606a-4b29-8fe8-65e58ef6c93a",
      "name": "When clicking ‘Test workflow’",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        60,
        -380
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "8babd8b0-6fb1-44e2-b974-2e1e21201450",
      "name": "Convert to File",
      "type": "n8n-nodes-base.convertToFile",
      "position": [
        1320,
        -380
      ],
      "parameters": {
        "options": {
          "fileName": "n8n-graphicdesignteam.csv"
        },
        "binaryPropertyName": "spreadsheet"
      },
      "typeVersion": 1.1
    },
    {
      "id": "0e2bcea2-e83d-4ab3-8d83-5dc3f999cacf",
      "name": "Spreadsheet",
      "type": "n8n-nodes-base.set",
      "position": [
        1020,
        -380
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "137c1da9-ec70-4555-832a-6fb79acab053",
              "name": "csvFile",
              "type": "string",
              "value": "created_at,image,Link,prompt,timings,seed,nsfw,width,height,type,drive_link,GenModel,GenPrompt,GenAspectRatio,GenStyleType,GenNegativePrompt"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "3a54231d-c236-4024-b58f-8621cecd5416",
      "name": "Google Drive - Create Folder",
      "type": "n8n-nodes-base.googleDrive",
      "position": [
        480,
        -380
      ],
      "parameters": {
        "name": "Graphic_Design_Team",
        "driveId": {
          "__rl": true,
          "mode": "id",
          "value": "=My Drive"
        },
        "options": {},
        "folderId": {
          "__rl": true,
          "mode": "list",
          "value": "root",
          "cachedResultName": "/ (Root folder)"
        },
        "resource": "folder"
      },
      "credentials": {
        "googleDriveOAuth2Api": {
          "id": "786",
          "name": "Google Drive"
        }
      },
      "typeVersion": 3
    },
    {
      "id": "4e4c7262-0a84-49e8-ad2e-064e02aa9064",
      "name": "Google Drive - Create Generations Folder",
      "type": "n8n-nodes-base.googleDrive",
      "position": [
        740,
        -380
      ],
      "parameters": {
        "name": "Image_Generations",
        "driveId": {
          "__rl": true,
          "mode": "list",
          "value": "My Drive"
        },
        "options": {},
        "folderId": {
          "__rl": true,
          "mode": "id",
          "value": "={{ $json.id }}"
        },
        "resource": "folder"
      },
      "credentials": {
        "googleDriveOAuth2Api": {
          "id": "786",
          "name": "Google Drive"
        }
      },
      "typeVersion": 3
    },
    {
      "id": "0ea3947f-e7b5-45ec-bacb-e2acece10709",
      "name": "Google Drive - Upload Spreadsheet",
      "type": "n8n-nodes-base.googleDrive",
      "position": [
        1600,
        -380
      ],
      "parameters": {
        "name": "n8n-Graphic_Design_Team.csv",
        "driveId": {
          "__rl": true,
          "mode": "list",
          "value": "My Drive"
        },
        "options": {
          "propertiesUi": {
            "propertyValues": [
              {}
            ]
          }
        },
        "folderId": {
          "__rl": true,
          "mode": "id",
          "value": "={{ $('Google Drive - Create Generations Folder').item.json.id }}"
        },
        "inputDataFieldName": "spreadsheet"
      },
      "credentials": {
        "googleDriveOAuth2Api": {
          "id": "786",
          "name": "Google Drive"
        }
      },
      "typeVersion": 3
    },
    {
      "id": "165f0c95-0e23-4457-9ce9-d4c1b421115a",
      "name": "Gmail - Send Setup Details",
      "type": "n8n-nodes-base.gmail",
      "position": [
        1900,
        -380
      ],
      "webhookId": "b77235d4-ca25-4c67-a99b-e664b98e3e95",
      "parameters": {
        "sendTo": "realsimple.dev",
        "message": "=Download the Image Generation Spreadsheet CSV and import it into google sheets\n<b>Image Generation Spreadsheet</b>: {{ $json.webViewLink }}\n<br>\ncopy and paste the Image Generations Folder ID into the Creative Brief Node {{ $('Google Drive - Create Generations Folder').item.json.id }}\n\n\n<b>n8n Graphic Design Root Folder</b>: https://drive.google.com/drive/u/0/folders/{{ $('Google Drive - Create Folder').item.json.id }}\n<br>\n<b>Image Generations Folder</b>: https://drive.google.com/drive/u/0/folders/{{ $('Google Drive - Create Generations Folder').item.json.id }}\n<br>",
        "options": {},
        "subject": "n8n Graphic Design Team Setup - 🔴 Important Links"
      },
      "credentials": {
        "gmailOAuth2": {
          "id": "786",
          "name": "Gmail"
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "28d6b413-0c90-46cf-8446-f28f8b07bb97",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -20,
        -460
      ],
      "parameters": {
        "color": 3,
        "width": 2100,
        "height": 280,
        "content": "# Run Setup First **ONCE**"
      },
      "typeVersion": 1
    },
    {
      "id": "6951f121-73aa-4789-8186-0ef1f0d60430",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -500,
        -60
      ],
      "parameters": {
        "width": 480,
        "height": 940,
        "content": "# n8n Graphic Design Team \n## _Setup Instructions_\n\n\n### 1. **Set Your Email**  \n   - In both the **Setup Gmail Node** and the **Gmail Node**, update the email field with your email address.\n\n\n### 2. **Run the Setup**  \n   - Execute the workflow.\n   - This will create the following in Google Drive:\n     - Folder: `Graphic_Design_Team`\n     - Folder: `Image_Generations`\n     - CSV File: `n8n-Graphic_Design_Team.csv` (which is automatically uploaded)\n\n\n### 3. **Check Your Email**  \n   - You will receive an email containing the newly created folder IDs and file links.\n\n\n### 4. **Create a New Google Sheet**  \n   - Open Google Sheets and create a new spreadsheet.\n   - Import the CSV file (`n8n-Graphic_Design_Team.csv`) into this spreadsheet.\n\n\n### 5. **Configure Google Sheets Nodes**  \n   - In the two Google Sheets nodes in the workflow, select the new Google Sheet that you just created.\n   - Copy the Google Drive IDs from the email and paste them into the **Creative Brief Node**.\n\n\n### 6. **Ready to Go!**  \n   - Your Graphic Design Team setup is now complete and ready to start working for you."
      },
      "typeVersion": 1
    },
    {
      "id": "cbd6699f-e32a-42d8-9877-cecfe51f223d",
      "name": "On form submission",
      "type": "n8n-nodes-base.formTrigger",
      "position": [
        60,
        -60
      ],
      "webhookId": "bebaca11-3026-444b-8d92-1056b1b146bb",
      "parameters": {
        "options": {},
        "formTitle": "n8n Graphic Design Team",
        "formFields": {
          "values": [
            {
              "fieldLabel": "prompt",
              "placeholder": "A beautiful ideogener8r Logo",
              "requiredField": true
            },
            {
              "fieldLabel": "audience",
              "placeholder": "The image is designed for a tech-savvy audience aged 18–35 who engage frequently with digital content and social media. They value visually appealing, inclusive, and clear messaging that resonates with modern trends. They are attentive to brand authenticity, ethical implications, and cultural sensitivity. Ensuring the image aligns with these preferences and values helps maintain audience trust and engagement."
            },
            {
              "fieldType": "dropdown",
              "fieldLabel": "Aspect Ratio",
              "fieldOptions": {
                "values": [
                  {
                    "option": "ASPECT_16_9"
                  },
                  {
                    "option": "ASPECT_9_16"
                  },
                  {
                    "option": "ASPECT_1_1"
                  },
                  {
                    "option": "ASPECT_10_16"
                  },
                  {
                    "option": "ASPECT_16_10"
                  },
                  {
                    "option": "ASPECT_3_2"
                  },
                  {
                    "option": "ASPECT_2_3"
                  },
                  {
                    "option": "ASPECT_4_3"
                  },
                  {
                    "option": "ASPECT_3_4"
                  },
                  {
                    "option": "ASPECT_1_3"
                  },
                  {
                    "option": "ASPECT_3_1"
                  }
                ]
              },
              "requiredField": true
            },
            {
              "fieldType": "dropdown",
              "fieldLabel": "model",
              "fieldOptions": {
                "values": [
                  {
                    "option": "V_1"
                  },
                  {
                    "option": "V_1_TURBO"
                  },
                  {
                    "option": "V_2"
                  },
                  {
                    "option": "V_2_TURBO"
                  },
                  {
                    "option": "V_2A"
                  },
                  {
                    "option": "V_2A_TURBO"
                  }
                ]
              },
              "requiredField": true
            },
            {
              "fieldType": "dropdown",
              "fieldLabel": "magic prompt",
              "fieldOptions": {
                "values": [
                  {
                    "option": "ON"
                  },
                  {
                    "option": "OFF"
                  }
                ]
              },
              "requiredField": true
            },
            {
              "fieldType": "dropdown",
              "fieldLabel": "style type",
              "fieldOptions": {
                "values": [
                  {
                    "option": "AUTO"
                  },
                  {
                    "option": "GENERAL"
                  },
                  {
                    "option": "REALISTIC"
                  },
                  {
                    "option": "DESIGN"
                  },
                  {
                    "option": "RENDER_3D"
                  },
                  {
                    "option": "ANIME"
                  }
                ]
              },
              "requiredField": true
            },
            {
              "fieldLabel": "negative prompt",
              "placeholder": "gradients, ugly",
              "requiredField": true
            }
          ]
        },
        "formDescription": "Created by <a href=\"https://realsimple.dev\">Real Simple Solutions</a> see more templates 👉 <a href=\"https://n8n.io/creators/joeperes/\">Click Here</a>"
      },
      "typeVersion": 2.2
    },
    {
      "id": "1c446cb1-9d75-4c7d-af79-2ac09fdd4084",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1820,
        -140
      ],
      "parameters": {
        "width": 280,
        "height": 560,
        "content": "## Select Spreadsheet from List"
      },
      "typeVersion": 1
    },
    {
      "id": "4804287c-10e4-44c9-a25b-0e77d9947e53",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -500,
        -460
      ],
      "parameters": {
        "color": 7,
        "width": 480,
        "height": 400,
        "content": "![image](https://fillin8n.realsimple.dev/ideoGener8r_Team.png)"
      },
      "typeVersion": 1
    },
    {
      "id": "ef32ab69-8009-41ec-b283-10d7eef61f34",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1820,
        680
      ],
      "parameters": {
        "width": 280,
        "height": 360,
        "content": "# Set Your Email"
      },
      "typeVersion": 1
    },
    {
      "id": "339db160-4dcc-49cd-a542-3c426c5a4969",
      "name": "Sticky Note5",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1820,
        -500
      ],
      "parameters": {
        "width": 280,
        "height": 320,
        "content": "# Set Your Email"
      },
      "typeVersion": 1
    },
    {
      "id": "0611f24e-d7f8-4c58-a1a4-157f1487245c",
      "name": "Sticky Note6",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        480,
        900
      ],
      "parameters": {
        "color": 5,
        "width": 760,
        "height": 80,
        "content": "## Created by **[Real Simple Solutions](https://realsimple.dev)** More templates 👉 **[Click Here](https://n8n.io/creators/joeperes/)**"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {
    "On form submission": [
      {
        "json": {
          "model": "V_2",
          "prompt": "A diverse graphic design team collaborating in a modern studio, surrounded by computer screens with colorful UI/UX mockups, sketchpads, color swatches, and coffee mugs. The Text \"ideoGener8r Team\" across the top of the image in stylized and in casual font. The team includes people of various ethnicities and genders, dressed in casual creative attire. The scene is lit by natural light through large windows, with potted plants and inspiration boards in the background. Use a semi-realistic illustration style with a vibrant color palette of teal, coral, soft beige, and navy. The overall composition should feel energetic, creative, and collaborative, capturing the essence of a modern design workspace.",
          "audience": "The image is designed for a tech-savvy audience aged 18–35 who engage frequently with digital content and social media. They value visually appealing, inclusive, and clear messaging that resonates with modern trends. They are attentive to brand authenticity, ethical implications, and cultural sensitivity. Ensuring the image aligns with these preferences and values helps maintain audience trust and engagement.",
          "formMode": "test",
          "style type": "REALISTIC",
          "submittedAt": "2025-04-07T12:22:11.617-04:00",
          "Aspect Ratio": "ASPECT_1_1",
          "magic prompt": "ON",
          "negative prompt": "ugly"
        }
      }
    ]
  },
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "c88e13ef-1acc-45ba-9939-08d9c29015d3",
  "connections": {
    "Switch1": {
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
            "node": "RE creative brief",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "GET image": {
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
    "Spreadsheet": {
      "main": [
        [
          {
            "node": "Convert to File",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "TheImageURL": {
      "main": [
        [
          {
            "node": "Download Image",
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
            "node": "Google Sheets",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "SetImageData": {
      "main": [
        [
          {
            "node": "GET image",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "genImageURL1": {
      "main": [
        [
          {
            "node": "TheImageURL",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "genImageURL2": {
      "main": [
        [
          {
            "node": "TheImageURL",
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
            "node": "genImageURL1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Download Image": {
      "main": [
        [
          {
            "node": "Image Reviewer",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Image Reviewer": {
      "main": [
        [
          {
            "node": "Switch1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "creative brief": {
      "main": [
        [
          {
            "node": "Ideogram Image generator",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "ideogram Remix": {
      "main": [
        [
          {
            "node": "Set Upload Fields1",
            "type": "main",
            "index": 0
          }
        ],
        []
      ]
    },
    "Convert to File": {
      "main": [
        [
          {
            "node": "Google Drive - Upload Spreadsheet",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Download Image3": {
      "main": [
        [
          {
            "node": "ideogram Remix",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Remixed Image": {
      "main": [
        [
          {
            "node": "Google Drive Remix Image",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "RE creative brief": {
      "main": [
        [
          {
            "node": "Download Image3",
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
            "node": "creative brief",
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
            "node": "Image Reviewer",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Set Upload Fields1": {
      "main": [
        [
          {
            "node": "Get Remixed Image",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Drive Remix Image": {
      "main": [
        [
          {
            "node": "Google Sheets - Add Remix",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Ideogram Image generator": {
      "main": [
        [
          {
            "node": "SetImageData",
            "type": "main",
            "index": 0
          }
        ],
        []
      ]
    },
    "Google Sheets - Add Remix": {
      "main": [
        [
          {
            "node": "genImageURL2",
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
            "node": "Image Reviewer",
            "type": "ai_outputParser",
            "index": 0
          }
        ]
      ]
    },
    "Google Drive - Create Folder": {
      "main": [
        [
          {
            "node": "Google Drive - Create Generations Folder",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Drive - Upload Spreadsheet": {
      "main": [
        [
          {
            "node": "Gmail - Send Setup Details",
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
            "node": "Google Drive - Create Folder",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Drive - Create Generations Folder": {
      "main": [
        [
          {
            "node": "Spreadsheet",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2112"></a>

## Template 2112 - Histórias infantis automáticas no Telegram

- **Nome:** Histórias infantis automáticas no Telegram
- **Descrição:** Gera histórias infantis usando IA, cria narrações em áudio e imagens ilustrativas, e publica o texto, áudio e imagem em um chat do Telegram de forma periódica.
- **Funcionalidade:** • Agendamento periódico: dispara a automação a cada 12 horas.
• Geração de história infantil: cria contos curtos, culturais e com mensagens educativas usando modelos de linguagem.
• Divisão de texto: quebra textos longos em partes para garantir processamento adequado.
• Criação de prompt para imagem: resume personagens e produz um prompt seguro para gerar ilustrações sem texto.
• Geração de áudio: converte o texto da história em arquivo de áudio (narração).
• Geração de imagem: produz imagem ilustrativa baseada no prompt, assegurando ausência de texto na imagem.
• Envio para Telegram: publica o texto, o arquivo de áudio e a imagem no chat configurado.
• Configuração de destino: permite definir o chatId para onde as histórias serão enviadas.
- **Ferramentas:** • OpenAI: usado para gerar o texto da história, criar prompts, sintetizar áudio e gerar imagens.
• Telegram: plataforma de envio e distribuição das histórias em texto, áudio e imagem para o público.

## Fluxo visual

```mermaid
flowchart LR
    N1["OpenAI Chat Model"]
    N2["Schedule Trigger"]
    N3["OpenAI Chat Model2"]
    N4["Sticky Note"]
    N5["Create a Prompt for DALL-E"]
    N6["Sticky Note1"]
    N7["Recursive Character Text Splitter"]
    N8["Create a story"]
    N9["Generate Audio for the story"]
    N10["Generate a Picture for the story"]
    N11["Send Story Text"]
    N12["Send Audio for the story"]
    N13["Send Story Picture"]
    N14["Config"]

    N14 --> N8
    N8 --> N9
    N8 --> N5
    N8 --> N11
    N2 --> N14
    N5 --> N10
    N9 --> N12
    N10 --> N13
```

## Fluxo (.json) :

```json
{
  "meta": {
    "instanceId": "84ba6d895254e080ac2b4916d987aa66b000f88d4d919a6b9c76848f9b8a7616",
    "templateId": "2233"
  },
  "nodes": [
    {
      "id": "757a7e67-073a-4fa1-b571-2ddd147b35f6",
      "name": "OpenAI Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        1000,
        1240
      ],
      "parameters": {
        "model": "gpt-3.5-turbo-16k-0613",
        "options": {}
      },
      "credentials": {
        "openAiApi": {
          "id": "kDo5LhPmHS2WQE0b",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "761ed83a-2cfb-474a-b596-922e5a7e2717",
      "name": "Schedule Trigger",
      "type": "n8n-nodes-base.scheduleTrigger",
      "position": [
        660,
        1060
      ],
      "parameters": {
        "rule": {
          "interval": [
            {
              "field": "hours",
              "hoursInterval": 12
            }
          ]
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "41faf334-30d6-4cc0-9a94-9c486ec3fa6c",
      "name": "OpenAI Chat Model2",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        1520,
        1420
      ],
      "parameters": {
        "options": {}
      },
      "credentials": {
        "openAiApi": {
          "id": "kDo5LhPmHS2WQE0b",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "d9ad0a3a-2ce6-4071-8262-8176b3eecf36",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1780,
        220
      ],
      "parameters": {
        "width": 1004.4263690337257,
        "height": 811.7188223885136,
        "content": "### Setting Up a Workflow for \"AI-Powered Children's English Storytelling on Telegram\"\n\nIn this guide, we will walk you through the process of setting up a workflow to create and share captivating children's stories using the provided configuration. Let's dive into the steps required to bring these imaginative tales to life on your Telegram channel:\n\n#### Steps to Setup the Workflow:\n1. **Import the Workflow:**\n - Copy the provided workflow JSON configuration.\n - In your n8n instance, go to Workflows and select \"Import from JSON.\"\n - Paste the configuration and import the workflow.\n\n2. **Configure Node Credentials:**\n - For nodes requiring API credentials (OpenAI and Telegram), create credentials with the appropriate API keys or tokens.\n\n3. **Set Node Parameters:**\n - Modify node parameters as needed, such as chat IDs, prompts, and intervals.\n - Change the chatId in Config node to the ID of the chat you want the story to be posted.\n\n4. **Ensure Data Flow:**\n - Check the connections between nodes to ensure a smooth flow of data and actions.\n\n5. **Execute Once:**\n - Activate the \"executeOnce\" option in nodes where necessary to trigger actions only once during setup.\n\n6. **Test the Workflow:**\n - Run the workflow to verify that each node functions correctly and data is processed as expected.\n\n7. **Enable Recurring Triggers:**\n - Confirm that the Schedule Trigger node is set to trigger the workflow at the desired interval (every 12 hours).\n\n8. **Initiate Workflow:**\n - Once everything is configured correctly, activate the workflow to start generating and sharing children's stories on Telegram.\n\nBy following these steps meticulously, you can seamlessly establish and operate the workflow designed to create captivating children's stories for your audience. Embrace the power of automation to inspire young minds and foster a love for storytelling through engaging narratives shared on Telegram.\n"
      },
      "typeVersion": 1
    },
    {
      "id": "b550e4ff-167d-4b12-8dff-0511a435cd7c",
      "name": "Create a Prompt for DALL-E",
      "type": "@n8n/n8n-nodes-langchain.chainSummarization",
      "position": [
        1500,
        1280
      ],
      "parameters": {
        "options": {
          "summarizationMethodAndPrompts": {
            "values": {
              "prompt": "Summarize the characters in this story based on their appearance and describe them if they are humans or animals and how they look like and what kind of are they, the prompt should be no-text in the picture, make sure the text is free from any prohibited or inappropriate content:\n\n\n\n\"{text}\"\n\n\nCONCISE SUMMARY:",
              "summarizationMethod": "stuff"
            }
          }
        }
      },
      "typeVersion": 2
    },
    {
      "id": "024a3615-9e90-4e47-81e3-21febfc2f0c9",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        380,
        240
      ],
      "parameters": {
        "width": 611.6882702103559,
        "height": 651.7145525871413,
        "content": "### Use Case for Setting Up a Workflow for Children's Stories\n\nCheck this example: [https://t.me/st0ries95](https://t.me/st0ries95)\n\n\nThe workflow for children's stories serves as a valuable tool for content creators, educators, and parents looking to engage children with imaginative and educational storytelling. Here are some key use cases for this workflow:\n\n1. **Content Creation:** The workflow streamlines the process of creating captivating children's stories by providing a structured framework and automation for story generation, audio creation, and image production.\n\n2. **Educational Resources:** Teachers can use this workflow to develop educational materials that incorporate storytelling to make learning more engaging and interactive for students.\n\n3. **Parental Engagement:** Parents can utilize the workflow to share personalized stories with their children, fostering a love for reading and creativity while bonding over shared storytelling experiences.\n\n4. **Community Building:** Organizations and community groups can leverage the workflow to create and share children's stories as a way to connect with their audience and promote literacy and creativity.\n\n5. **Inspiring Young Minds:** By automating the process of creating and sharing enchanting children's stories, this workflow aims to inspire young minds, spark imagination, and instill a passion for storytelling in children.\n\nOverall, the use case for this workflow extends to various settings where storytelling plays a significant role in engaging, educating, and entertaining children, making it a versatile tool for enhancing the storytelling experience.\n"
      },
      "typeVersion": 1
    },
    {
      "id": "11bfff09-33c6-48ab-b9e6-2e5349a87ca5",
      "name": "Recursive Character Text Splitter",
      "type": "@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter",
      "position": [
        1160,
        1260
      ],
      "parameters": {
        "options": {},
        "chunkSize": 500,
        "chunkOverlap": 300
      },
      "typeVersion": 1
    },
    {
      "id": "9da21054-961e-4b7a-973e-1c180571ce92",
      "name": "Create a story",
      "type": "@n8n/n8n-nodes-langchain.chainSummarization",
      "position": [
        1080,
        1060
      ],
      "parameters": {
        "options": {
          "summarizationMethodAndPrompts": {
            "values": {
              "prompt": "Create a captivating short tale for kids, whisking them away to magical lands brimming with wisdom. Explore diverse themes in a fun and simple way, weaving in valuable messages. Dive into cultural adventures with lively language that sparks curiosity. Let your story inspire young minds through enchanting narratives that linger long after the last word. Begin crafting your imaginative tale now! (Approximately 900 characters)\n\n\n\"{text}\"\n\nCONCISE SUMMARY:",
              "summarizationMethod": "stuff"
            }
          }
        },
        "chunkingMode": "advanced"
      },
      "executeOnce": true,
      "typeVersion": 2
    },
    {
      "id": "35579446-e11c-416b-b34a-b31e8461a1b3",
      "name": "Generate Audio for the story",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "position": [
        1520,
        1060
      ],
      "parameters": {
        "input": "={{ $json.response.text }}",
        "options": {},
        "resource": "audio"
      },
      "credentials": {
        "openAiApi": {
          "id": "kDo5LhPmHS2WQE0b",
          "name": "OpenAi account"
        }
      },
      "executeOnce": true,
      "typeVersion": 1.3
    },
    {
      "id": "453d149f-a2a7-4fc9-ba3b-85b42df1c29b",
      "name": "Generate a Picture for the story",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "position": [
        1840,
        1280
      ],
      "parameters": {
        "prompt": "=Produce an image ensuring that no text is generated within the visual content. {{ $json.response.text }}",
        "options": {},
        "resource": "image"
      },
      "credentials": {
        "openAiApi": {
          "id": "kDo5LhPmHS2WQE0b",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1.3
    },
    {
      "id": "8f324f12-b21e-4d0c-b7fa-5e2f93ba08aa",
      "name": "Send Story Text",
      "type": "n8n-nodes-base.telegram",
      "position": [
        1520,
        840
      ],
      "parameters": {
        "text": "={{ $json.response.text }}",
        "chatId": "={{ $('Config').item.json.chatId }}",
        "additionalFields": {
          "appendAttribution": false
        }
      },
      "credentials": {
        "telegramApi": {
          "id": "k3RE6o9brmFRFE9p",
          "name": "Telegram account"
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "51a08f75-1c34-48a0-86de-b47e435ef618",
      "name": "Send Audio for the story",
      "type": "n8n-nodes-base.telegram",
      "position": [
        1720,
        1060
      ],
      "parameters": {
        "chatId": "={{ $('Config').item.json.chatId }}",
        "operation": "sendAudio",
        "binaryData": true,
        "additionalFields": {
          "caption": "End of the Story for today ....."
        }
      },
      "credentials": {
        "telegramApi": {
          "id": "k3RE6o9brmFRFE9p",
          "name": "Telegram account"
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "3f890a4d-26ea-452a-8ed5-917282e8b0d8",
      "name": "Send Story Picture",
      "type": "n8n-nodes-base.telegram",
      "position": [
        2020,
        1280
      ],
      "parameters": {
        "chatId": "={{ $('Config').item.json.chatId }}",
        "operation": "sendPhoto",
        "binaryData": true,
        "additionalFields": {}
      },
      "credentials": {
        "telegramApi": {
          "id": "k3RE6o9brmFRFE9p",
          "name": "Telegram account"
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "1cbec52c-b545-45df-885f-57c287f81017",
      "name": "Config",
      "type": "n8n-nodes-base.set",
      "position": [
        880,
        1060
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "327667cb-b5b0-4f6f-915c-544696ed8e5a",
              "name": "chatId",
              "type": "string",
              "value": "-4170994782"
            }
          ]
        }
      },
      "typeVersion": 3.3
    }
  ],
  "pinData": {},
  "connections": {
    "Config": {
      "main": [
        [
          {
            "node": "Create a story",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Create a story": {
      "main": [
        [
          {
            "node": "Generate Audio for the story",
            "type": "main",
            "index": 0
          },
          {
            "node": "Create a Prompt for DALL-E",
            "type": "main",
            "index": 0
          },
          {
            "node": "Send Story Text",
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
            "node": "Config",
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
            "node": "Create a story",
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
            "node": "Create a Prompt for DALL-E",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Create a Prompt for DALL-E": {
      "main": [
        [
          {
            "node": "Generate a Picture for the story",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Generate Audio for the story": {
      "main": [
        [
          {
            "node": "Send Audio for the story",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Generate a Picture for the story": {
      "main": [
        [
          {
            "node": "Send Story Picture",
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
            "node": "Create a story",
            "type": "ai_textSplitter",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2114"></a>

## Template 2114 - Insights de avaliações Trustpilot

- **Nome:** Insights de avaliações Trustpilot
- **Descrição:** Coleta avaliações públicas do Trustpilot para uma empresa, armazena vetores em um banco vetorial, agrupa avaliações similares e gera insights resumidos por cluster, exportando os resultados para uma planilha.
- **Funcionalidade:** • Limpeza de dados existentes: Remove registros anteriores no armazenamento vetorial para a empresa selecionada antes de importar novos dados.
• Raspagem de avaliações: Navega pelas páginas públicas do Trustpilot e extrai campos como autor, rating, título, texto, datas, país e URL.
• Normalização de campos: Converte contagens, formata datas e constrói URLs completas dos reviews.
• Geração de embeddings: Cria vetores de embeddings a partir do conteúdo das avaliações para indexação semântica.
• Divisão de texto: Divide textos longos em chunks usando um separador recursivo para processamento adequado dos embeddings.
• Armazenamento vetorial: Insere vetores e metadados no banco vetorial para buscas e filtragens futuras.
• Gatilho de subfluxo por intervalo: Aciona um subfluxo que permite definir empresa e intervalo de datas para análise focada.
• Busca filtrada por data e empresa: Recupera pontos do banco vetorial filtrando por company_id e intervalo de datas selecionado.
• Agrupamento de avaliações: Aplica K-means (em Python) sobre os vetores para agrupar avaliações semelhantes em clusters.
• Filtragem de clusters válidos: Seleciona apenas clusters com 3 ou mais pontos para análise aprofundada.
• Extração de payloads por cluster: Recupera o conteúdo completo das avaliações pertencentes a cada cluster válido.
• Geração de insights por IA: Usa um modelo de linguagem para resumir cada grupo, produzir um insight, classificar sentimento e sugerir melhorias em formato estruturado.
• Exportação: Prepara e anexa os resultados (insights, sentimento, número de respostas e respostas brutas) em uma planilha do Google Sheets.
- **Ferramentas:** • Trustpilot: Fonte pública das avaliações que são raspadas para análise.
• Qdrant: Banco vetorial utilizado para armazenar embeddings e metadados das avaliações.
• OpenAI (embeddings e modelo de linguagem): Gera embeddings dos textos e produz resumos/insights em linguagem natural.
• Google Sheets: Destino para exportar os insights e os dados brutos consolidados.
• Python (NumPy, scikit-learn): Ambiente e bibliotecas usados para processamento numérico e aplicação do algoritmo de clustering K-means.

## Fluxo visual

```mermaid
flowchart LR
    N1["When clicking ‘Test workflow’"]
    N2["Zip Entries"]
    N3["Extract Reviews"]
    N4["Reviews to List"]
    N5["Default Data Loader"]
    N6["Recursive Character Text Splitter"]
    N7["Embeddings OpenAI"]
    N8["Set Variables"]
    N9["Get Payload of Points"]
    N10["Clusters To List"]
    N11["OpenAI Chat Model"]
    N12["Only Clusters With 3+ points"]
    N13["Set Variables1"]
    N14["Find Reviews"]
    N15["Prep Output For Export"]
    N16["Export To Sheets"]
    N17["Clear Existing Reviews"]
    N18["Trigger Insights"]
    N19["Prep Values For Trigger"]
    N20["Execute Workflow Trigger"]
    N21["Sticky Note"]
    N22["Sticky Note1"]
    N23["Get TrustPilot Page"]
    N24["Sticky Note2"]
    N25["Qdrant Vector Store"]
    N26["Sticky Note3"]
    N27["Sticky Note4"]
    N28["Sticky Note5"]
    N29["Sticky Note7"]
    N30["Sticky Note8"]
    N31["Sticky Note6"]
    N32["Sticky Note9"]
    N33["Apply K-means Clustering Algorithm"]
    N34["Sticky Note10"]
    N35["Customer Insights Agent"]
    N36["Sticky Note12"]
    N37["Sticky Note11"]

    N2 --> N4
    N14 --> N33
    N8 --> N17
    N13 --> N14
    N3 --> N2
    N4 --> N25
    N10 --> N12
    N23 --> N3
    N25 --> N19
    N9 --> N35
    N17 --> N23
    N15 --> N16
    N35 --> N15
    N19 --> N18
    N20 --> N13
    N12 --> N9
    N1 --> N8
    N33 --> N10
```

## Fluxo (.json) :

```json
{
  "meta": {
    "instanceId": "408f9fb9940c3cb18ffdef0e0150fe342d6e655c3a9fac21f0f644e8bedabcd9"
  },
  "nodes": [
    {
      "id": "63501cc8-77c9-4037-9f70-da23b6d20b03",
      "name": "When clicking ‘Test workflow’",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        280,
        440
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "00de989c-d9e9-4b42-b5db-7097800a6017",
      "name": "Zip Entries",
      "type": "n8n-nodes-base.set",
      "position": [
        1380,
        360
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "833a554d-2b39-4160-9348-18b17b28ce30",
              "name": "data",
              "type": "array",
              "value": "={{ \n  $json.review_author.map((review_author, idx) => ({\n    review_author,\n    review_author_reviews_count: $json.review_author_reviews_count[idx].replace(' reviews', '').toInt(),\n    review_country: $json.review_country[idx],\n    review_date: $json.review_date[idx].toDate(),\n    review_date_of_experience: $json.review_date_of_experience[idx].replace('Date of experience: ', '').toDate(),\n    review_rating: $json.review_rating[idx].toInt(),\n    review_text: $json.review_text[idx],\n    review_title: $json.review_title[idx],\n    review_url: $('Get TrustPilot Page').params.url.match(/https://[^/]+/) + $json.review_url[idx],\n  }))\n}}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "9290e116-c001-49d5-ae4c-d91cd246f2c2",
      "name": "Extract Reviews",
      "type": "n8n-nodes-base.html",
      "position": [
        1140,
        520
      ],
      "parameters": {
        "options": {
          "trimValues": true
        },
        "operation": "extractHtmlContent",
        "extractionValues": {
          "values": [
            {
              "key": "review_author",
              "cssSelector": "[data-service-review-card-paper] [data-consumer-name-typography]",
              "returnArray": true
            },
            {
              "key": "review_rating",
              "attribute": "data-service-review-rating",
              "cssSelector": "[data-service-review-rating]",
              "returnArray": true,
              "returnValue": "attribute"
            },
            {
              "key": "review_title",
              "cssSelector": "[data-service-review-title-typography]",
              "returnArray": true
            },
            {
              "key": "review_text",
              "cssSelector": "[data-service-review-text-typography]",
              "returnArray": true
            },
            {
              "key": "review_date_of_experience",
              "cssSelector": "[data-service-review-date-of-experience-typography]",
              "returnArray": true
            },
            {
              "key": "review_date",
              "attribute": "datetime",
              "cssSelector": "[data-service-review-date-time-ago]",
              "returnArray": true,
              "returnValue": "attribute"
            },
            {
              "key": "review_country",
              "cssSelector": "[data-consumer-country-typography]",
              "returnArray": true
            },
            {
              "key": "review_author_reviews_count",
              "cssSelector": "[data-consumer-reviews-count-typography]",
              "returnArray": true
            },
            {
              "key": "review_url",
              "attribute": "href",
              "cssSelector": "a[data-review-title-typography]",
              "returnArray": true,
              "returnValue": "attribute"
            }
          ]
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "4aa3e50d-fcce-48a7-8237-c12f8592f69e",
      "name": "Reviews to List",
      "type": "n8n-nodes-base.splitOut",
      "position": [
        1380,
        520
      ],
      "parameters": {
        "options": {},
        "fieldToSplitOut": "data"
      },
      "typeVersion": 1
    },
    {
      "id": "a6b9abf9-a17a-4f30-9f90-6183770c4933",
      "name": "Default Data Loader",
      "type": "@n8n/n8n-nodes-langchain.documentDefaultDataLoader",
      "position": [
        1980,
        520
      ],
      "parameters": {
        "options": {
          "metadata": {
            "metadataValues": [
              {
                "name": "review_author",
                "value": "={{ $json.review_author }}"
              },
              {
                "name": "review_author_reviews_count",
                "value": "={{ $json.review_author_reviews_count }}"
              },
              {
                "name": "review_country",
                "value": "={{ $json.review_country }}"
              },
              {
                "name": "review_date",
                "value": "={{ $json.review_date }}"
              },
              {
                "name": "review_date_of_experience",
                "value": "={{ $json.review_date_of_experience }}"
              },
              {
                "name": "review_rating",
                "value": "={{ $json.review_rating }}"
              },
              {
                "name": "review_date_month",
                "value": "={{ $json.review_date.toDateTime().format('M') }}"
              },
              {
                "name": "review_date_year",
                "value": "={{ $json.review_date.toDateTime().format('yyyy') }}"
              },
              {
                "name": "review_date_of_experience_month",
                "value": "={{ $json.review_date_of_experience.toDateTime().format('M') }}"
              },
              {
                "name": "review_date_of_experience_year",
                "value": "={{ $json.review_date_of_experience.toDateTime().format('yyyy') }}"
              },
              {
                "name": "company_id",
                "value": "={{ $('Set Variables').item.json.companyId }}"
              },
              {
                "name": "review_url",
                "value": "={{ $json.review_url }}"
              }
            ]
          }
        },
        "jsonData": "={{ $json.review_title }}\n{{ $json.review_text }}",
        "jsonMode": "expressionData"
      },
      "typeVersion": 1
    },
    {
      "id": "afd8907c-9a59-4dcc-94c5-2114fb2a7d5d",
      "name": "Recursive Character Text Splitter",
      "type": "@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter",
      "position": [
        1980,
        660
      ],
      "parameters": {
        "options": {},
        "chunkSize": 4000
      },
      "typeVersion": 1
    },
    {
      "id": "e22d92b8-e8e9-42aa-9d02-2e70234f11ed",
      "name": "Embeddings OpenAI",
      "type": "@n8n/n8n-nodes-langchain.embeddingsOpenAi",
      "position": [
        1860,
        520
      ],
      "parameters": {
        "model": "text-embedding-3-small",
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
      "id": "f0ea6b63-c96d-4b3f-8a21-d0f2dbb4efc3",
      "name": "Set Variables",
      "type": "n8n-nodes-base.set",
      "position": [
        520,
        440
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "2e58a9fa-a14d-4a6c-8cc8-8ec947c791fb",
              "name": "companyId",
              "type": "string",
              "value": "www.freddiesflowers.com"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "0188986f-fbe9-4c06-892a-3cb71b52a309",
      "name": "Get Payload of Points",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1740,
        1120
      ],
      "parameters": {
        "url": "=http://qdrant:6333/collections/trustpilot_reviews/points",
        "method": "POST",
        "options": {},
        "jsonBody": "={{\n  {\n    \"ids\": $json.points,\n    \"with_payload\": true\n  }\n}}",
        "sendBody": true,
        "specifyBody": "json",
        "authentication": "predefinedCredentialType",
        "nodeCredentialType": "qdrantApi"
      },
      "credentials": {
        "qdrantApi": {
          "id": "NyinAS3Pgfik66w5",
          "name": "QdrantApi account"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "5fc6e0b6-507f-4cfd-951b-be3709b86ac2",
      "name": "Clusters To List",
      "type": "n8n-nodes-base.splitOut",
      "position": [
        1480,
        1120
      ],
      "parameters": {
        "options": {},
        "fieldToSplitOut": "output"
      },
      "typeVersion": 1
    },
    {
      "id": "f21369b9-1dd5-4b35-a1f3-00fd67794051",
      "name": "OpenAI Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        2140,
        1340
      ],
      "parameters": {
        "model": "gpt-4o-mini",
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
      "id": "b0075699-6513-4781-b5de-81d1ab81dfe1",
      "name": "Only Clusters With 3+ points",
      "type": "n8n-nodes-base.filter",
      "position": [
        1480,
        1300
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
              "id": "328f806c-0792-4d90-9bee-a1e10049e78f",
              "operator": {
                "type": "array",
                "operation": "lengthGt",
                "rightType": "number"
              },
              "leftValue": "={{ $json.points }}",
              "rightValue": 2
            }
          ]
        }
      },
      "typeVersion": 2
    },
    {
      "id": "f6a6209c-d269-4238-8e92-230df7b41df9",
      "name": "Set Variables1",
      "type": "n8n-nodes-base.set",
      "position": [
        519,
        1220
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "2e58a9fa-a14d-4a6c-8cc8-8ec947c791fb",
              "name": "companyId",
              "type": "string",
              "value": "={{ $json.companyId }}"
            },
            {
              "id": "37cf8af2-6f0f-40b1-b822-c9bd6a620a3c",
              "name": "review_date_from",
              "type": "string",
              "value": "={{ $today.startOf('month').toISO() }}"
            },
            {
              "id": "8d72f739-f832-4c25-b62a-2ae70ad2b1e7",
              "name": "review_date_to",
              "type": "string",
              "value": "={{ $today.endOf('month').toISO() }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "85cb48b1-0ab9-4f88-88f3-82fcfb041ebe",
      "name": "Find Reviews",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        896,
        1160
      ],
      "parameters": {
        "url": "=http://qdrant:6333/collections/trustpilot_reviews/points/scroll",
        "method": "POST",
        "options": {},
        "jsonBody": "={\n  \"limit\": 500,\n  \"filter\":{\n    \"must\": [\n      {\n        \"key\": \"metadata.company_id\",\n        \"match\": { \"value\": \"{{ $('Set Variables1').item.json.companyId }}\" }\n      },\n      {\n        \"key\": \"metadata.review_date\",\n        \"range\": {\n          \"gte\": \"{{ $('Set Variables1').item.json.review_date_from }}\",\n          \"gt\": null,\n          \"lt\": null,\n          \"lte\": \"{{ $('Set Variables1').item.json.review_date_to }}\"\n        }\n      }\n    ]\n  },\n  \"with_vector\":true\n}",
        "sendBody": true,
        "specifyBody": "json",
        "authentication": "predefinedCredentialType",
        "nodeCredentialType": "qdrantApi"
      },
      "credentials": {
        "qdrantApi": {
          "id": "NyinAS3Pgfik66w5",
          "name": "QdrantApi account"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "69bbd197-c78f-4dae-9300-fe23d4d49855",
      "name": "Prep Output For Export",
      "type": "n8n-nodes-base.set",
      "position": [
        2720,
        1203
      ],
      "parameters": {
        "mode": "raw",
        "options": {},
        "jsonOutput": "={{ {\n  ...$json.output,\n  \"CompanyID\": $('Set Variables1').item.json.companyId,\n  \"From\": $('Set Variables1').item.json.review_date_from,\n  \"To\": $('Set Variables1').item.json.review_date_to,\n  \"Number of Responses\": $('Get Payload of Points').item.json.result.length,\n  \"Raw Responses\": $('Get Payload of Points').item.json.result.map(item =>\n    [\n      item.payload.metadata.review_date,\n      item.payload.metadata.review_author,\n      item.payload.metadata.review_rating,\n      item.payload.content.replaceAll('\"', '\\\"').replaceAll('\\n', ' '),\n      item.payload.metadata.review_url,\n    ]\n   ).join('\\n')\n} }}\n"
      },
      "typeVersion": 3.4
    },
    {
      "id": "d77daa23-6acf-4daa-bf4c-33da4d05a54c",
      "name": "Export To Sheets",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        2940,
        1203
      ],
      "parameters": {
        "columns": {
          "value": {},
          "schema": [
            {
              "id": "CompanyID",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "CompanyID",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "From",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "From",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "To",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "To",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Insight",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "Insight",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Sentiment",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "Sentiment",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Suggested Improvements",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "Suggested Improvements",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Number of Responses",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "Number of Responses",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Raw Responses",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "Raw Responses",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            }
          ],
          "mappingMode": "autoMapInputData",
          "matchingColumns": []
        },
        "options": {},
        "operation": "append",
        "sheetName": {
          "__rl": true,
          "mode": "name",
          "value": "=Sheet1"
        },
        "documentId": {
          "__rl": true,
          "mode": "id",
          "value": "=1wAwWCcIZod00IGtxwTbTgjIRbKHu3Yl9wYWJ8GeT2Os"
        }
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "XHvC7jIRR8A2TlUl",
          "name": "Google Sheets account"
        }
      },
      "typeVersion": 4.4
    },
    {
      "id": "1f60c3a5-a47a-4313-9b29-8ea652d573f7",
      "name": "Clear Existing Reviews",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        760,
        440
      ],
      "parameters": {
        "url": "http://qdrant:6333/collections/trustpilot_reviews/points/delete",
        "method": "POST",
        "options": {},
        "jsonBody": "={\n    \"filter\": {\n        \"must\": [\n            {\n                \"key\": \"metadata.company_id\",\n                \"match\": {\n                    \"value\": \"{{ $('Set Variables').item.json.companyId }}\"\n                }\n            }\n        ]\n    }\n}",
        "sendBody": true,
        "specifyBody": "json",
        "authentication": "predefinedCredentialType",
        "nodeCredentialType": "qdrantApi"
      },
      "credentials": {
        "qdrantApi": {
          "id": "NyinAS3Pgfik66w5",
          "name": "QdrantApi account"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "61c3117c-757c-45dd-b9d5-1122b793be30",
      "name": "Trigger Insights",
      "type": "n8n-nodes-base.executeWorkflow",
      "position": [
        2660,
        440
      ],
      "parameters": {
        "options": {},
        "workflowId": "={{ $workflow.id }}"
      },
      "typeVersion": 1
    },
    {
      "id": "d3c6e81f-34bb-4be9-b869-2c219b87c4fb",
      "name": "Prep Values For Trigger",
      "type": "n8n-nodes-base.set",
      "position": [
        2460,
        440
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "24dd90ad-390f-444e-ba6c-8c06a41e836e",
              "name": "companyId",
              "type": "string",
              "value": "={{ $('Set Variables').item.json.companyId }}"
            }
          ]
        }
      },
      "executeOnce": true,
      "typeVersion": 3.4
    },
    {
      "id": "64af9cc7-a194-4427-ba78-d9a1136b962f",
      "name": "Execute Workflow Trigger",
      "type": "n8n-nodes-base.executeWorkflowTrigger",
      "position": [
        316,
        1220
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "7b6ba502-36c2-41e6-9d67-781d0d40a569",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        186.9455564469605,
        263.2301011325764
      ],
      "parameters": {
        "color": 7,
        "width": 787.3314861380661,
        "height": 465.52420584035275,
        "content": "## Step 1. Starting Fresh\nFor this demo, we'll clear any existing records in our Qdrant vector store for the selected company. We do this using the Qdrant's delete points API."
      },
      "typeVersion": 1
    },
    {
      "id": "a99389d4-8ea6-4379-b725-f30e92b0d29e",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1006.3778510483207,
        148.50042906971555
      ],
      "parameters": {
        "color": 7,
        "width": 638.5221986278162,
        "height": 580.2538779032135,
        "content": "## Step 2. Scraping TrustPilot For Company Reviews\n[Read more about HTTP Request Node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/)\n\nWe'll scrape at the most recent 3 pages of reviews for illustrative purposes but we could easily scrape them all if required. The HTML node offers a convenient way to extract data from the returned html pages and using it, we'll retrieve all the reviews data."
      },
      "typeVersion": 1
    },
    {
      "id": "139ccadd-9135-4681-b2eb-403b8d8bd710",
      "name": "Get TrustPilot Page",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1140,
        360
      ],
      "parameters": {
        "url": "=https://uk.trustpilot.com/review/{{ $('Set Variables').item.json.companyId }}?sort=recency",
        "options": {
          "pagination": {
            "pagination": {
              "parameters": {
                "parameters": [
                  {
                    "name": "page",
                    "value": "={{ $pageCount + 1 }}"
                  }
                ]
              },
              "maxRequests": 3,
              "limitPagesFetched": true
            }
          }
        }
      },
      "executeOnce": false,
      "typeVersion": 4.2
    },
    {
      "id": "1c71db65-713b-4c31-9c11-5ff678fb327a",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1680,
        140
      ],
      "parameters": {
        "color": 7,
        "width": 638.5221986278162,
        "height": 689.8000993522735,
        "content": "## Step 3. Store Reviews in Qdrant\n[Learn more about the Qdrant Vector Store](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreqdrant/)\n\nVector databases are a great way to store data if you're interested in perform similiarity searches which applies here as we want to group similar reviews to find patterns. Qdrant is a powerful vector database and tool of choice because of its robust API implementation and advanced filtering capabilities."
      },
      "typeVersion": 1
    },
    {
      "id": "a4f82a1b-5a76-46b6-a7a3-84ab09b46699",
      "name": "Qdrant Vector Store",
      "type": "@n8n/n8n-nodes-langchain.vectorStoreQdrant",
      "position": [
        1860,
        360
      ],
      "parameters": {
        "mode": "insert",
        "options": {},
        "qdrantCollection": {
          "__rl": true,
          "mode": "id",
          "value": "=trustpilot_reviews"
        }
      },
      "credentials": {
        "qdrantApi": {
          "id": "NyinAS3Pgfik66w5",
          "name": "QdrantApi account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "cbad9e73-c5b3-474c-95ef-7269addc4e62",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        216,
        1000
      ],
      "parameters": {
        "color": 7,
        "width": 543.4265511994403,
        "height": 453.31956386852846,
        "content": "## Step 5. The Insight Subworkflow\n[Learn more about Workflow Triggers](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflowtrigger)\n\nThis subworkflow takes the companyId to find the relevant records in our Qdrant vector store. It also takes a \"from\" and \"to\" date to scope the insights to a particular range - doing this we can say something like \"we only want insights for the past month of reviews\". "
      },
      "typeVersion": 1
    },
    {
      "id": "9c530716-63f4-4368-8d0e-0cdbe8f5b08e",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        780,
        920
      ],
      "parameters": {
        "color": 7,
        "width": 557.7420442679241,
        "height": 526.2781960611934,
        "content": "## Step 6. Apply Clustering Algorithm to Reviews\n[Read more about using Python in n8n](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.code)\n\nWe'll retrieve our vectors embeddings for the desired company reviews and perform an advanced clustering algorithm on them. This powerful echnique allows us to quickly group similar embeddings into clusters which we can then use to discover popular feedback, opinions and pain-points!"
      },
      "typeVersion": 1
    },
    {
      "id": "9790b3a5-cc7c-4e12-8038-fc661c8226f8",
      "name": "Sticky Note5",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1360,
        920
      ],
      "parameters": {
        "color": 7,
        "width": 598.5585287222906,
        "height": 605.9905193915599,
        "content": "## Step 7. Fetch Reviews By Cluster\n[Learn more about using the Code Node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.code/)\n\nWith the Qdrant point IDs grouped and returned by our code node, all that's left is to fetch the payload of each. Note that the clustering algorithm isn't perfect and may require some tweaking depending on your data."
      },
      "typeVersion": 1
    },
    {
      "id": "267057b6-9727-4a45-9d87-5429da42f48e",
      "name": "Sticky Note7",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1980,
        969
      ],
      "parameters": {
        "color": 7,
        "width": 587.6069484146701,
        "height": 552.9535170892194,
        "content": "## Step 8. Getting Insights from Grouped Reviews\n[Read more about using Information Extractor Node](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.information-extractor)\n\nNext, we'll use our state-of-the-art LLM to generate insights on our reviews. Doing it this way, we'll able to pull more granular results addressing many key topics within the reviews."
      },
      "typeVersion": 1
    },
    {
      "id": "b8cc07d0-ffa3-425f-ae74-76dcb68fa88f",
      "name": "Sticky Note8",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2600,
        980
      ],
      "parameters": {
        "color": 7,
        "width": 572.5638733479158,
        "height": 464.4019616956416,
        "content": "## Step 9. Write To Insights Sheet\nFinally, our completed insights to appended to the Insights Sheet we created earlier in the workflow.\n\nYou can find a sample sheet here: https://docs.google.com/spreadsheets/d/e/2PACX-1vQ6ipJnXWXgr5wlUJnhioNpeYrxaIpsRYZCwN3C-fFXumkbh9TAsA_JzE0kbv7DcGAVIP7az0L46_2P/pubhtml"
      },
      "typeVersion": 1
    },
    {
      "id": "0dac0854-7106-44e3-bd68-fad7b201a6bc",
      "name": "Sticky Note6",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2340,
        240
      ],
      "parameters": {
        "color": 7,
        "width": 519.6419932444072,
        "height": 429.11782776909047,
        "content": "## Step 4. Trigger Insights SubWorkflow\n[Learn more about Workflow Triggers](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflow)\n\nA subworkflow is used to trigger the analysis for the survey. This separation is optional but used here to better demonstrate the two part process."
      },
      "typeVersion": 1
    },
    {
      "id": "4aa7e73e-c29d-41df-b2f8-a62109285ccb",
      "name": "Sticky Note9",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        460,
        380
      ],
      "parameters": {
        "width": 226.36363118160727,
        "height": 327.0249036433755,
        "content": "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n### 🚨 Set company here!\nTrustpilot must recognise it as part of the url."
      },
      "typeVersion": 1
    },
    {
      "id": "4d895cf9-452c-401e-a6f3-b9d3a359a96d",
      "name": "Apply K-means Clustering Algorithm",
      "type": "n8n-nodes-base.code",
      "position": [
        1116,
        1160
      ],
      "parameters": {
        "language": "python",
        "pythonCode": "import numpy as np\nfrom sklearn.cluster import KMeans\n\n# get vectors for all answers\npoint_ids = [item.id for item in _input.first().json.result.points]\nvectors = [item.vector.to_py() for item in _input.first().json.result.points]\nvectors_array = np.array(vectors)\n\n# apply k-means clustering where n_clusters = 5\n# this is a max and we'll discard some of these clusters later\nkmeans = KMeans(n_clusters=min(len(vectors), 5), random_state=42).fit(vectors_array)\nlabels = kmeans.labels_\nunique_labels = set(labels)\n\n# Extract and print points in each cluster\nclusters = {}\nfor label in set(labels):\n    clusters[label] = vectors_array[labels == label]\n\n# return Qdrant point ids for each cluster\n# we'll use these ids to fetch the payloads from the vector store.\noutput = []\nfor cluster_id, cluster_points in clusters.items():\n    points = [point_ids[i] for i in range(len(labels)) if labels[i] == cluster_id]\n    output.append({\n        \"id\": f\"Cluster {cluster_id}\",\n        \"total\": len(cluster_points),\n        \"points\": points\n    })\n\nreturn {\"json\": {\"output\": output } }"
      },
      "typeVersion": 2
    },
    {
      "id": "95c57019-d9d7-4d9f-93dd-21d3d9708861",
      "name": "Sticky Note10",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -260,
        40
      ],
      "parameters": {
        "width": 400.381109509268,
        "height": 612.855812336249,
        "content": "## Try It Out!\n\n### This workflow generates highly-detailed customer insights from Trustpilot reviews. Works best when dealing with a large number of reviews.\n\n* Import Trustpilot reviews and vectorise in Qdrant vectorstore.\n* Identify clusters of popular topics in reviews using K-means clustering algorithm. \n* Each valid cluster is analysed and summarised by LLM.\n* Export LLM response and cluster results back into sheet.\n\nCheck out the reference google sheet here: https://docs.google.com/spreadsheets/d/e/2PACX-1vQ6ipJnXWXgr5wlUJnhioNpeYrxaIpsRYZCwN3C-fFXumkbh9TAsA_JzE0kbv7DcGAVIP7az0L46_2P/pubhtml\n\n### Need Help?\nJoin the [Discord](https://discord.com/invite/XPKeKXeB7d) or ask in the [Forum](https://community.n8n.io/)!\n\nHappy Hacking!"
      },
      "typeVersion": 1
    },
    {
      "id": "9bba9480-792e-48e3-ad9f-8809ce3aba09",
      "name": "Customer Insights Agent",
      "type": "@n8n/n8n-nodes-langchain.informationExtractor",
      "position": [
        2140,
        1180
      ],
      "parameters": {
        "text": "=The {{ $json.result.length }} reviews were:\n{{\n$json.result.map(item =>\n`* ${item.payload.metadata.review_author} gave ${item.payload.metadata.review_rating} stars: \"${item.payload.content.replaceAll('\"', '\\\"').replaceAll('\\n', ' ')}\"`\n).join('\\n')\n}}",
        "options": {
          "systemPromptTemplate": "=You help summarise a selection of trustpilot reviews for a company called \"{{ $json.result[0].payload.metadata.company_id }}\".\nThe {{ $json.result.length }} reviews were selected because their contents were similar in context.\n\nYour task is to: \n* summarise the given reviews into a short paragraph. Provide an insight from this summary and what we could learn from the reviews.\n* determine if the overall sentiment of all the listed responses to be either strongly negative, negative, neutral, positive or strongly positive."
        },
        "schemaType": "fromJson",
        "jsonSchemaExample": "{\n\t\"Insight\": \"\",\n    \"Sentiment\": \"\",\n    \"Suggested Improvements\": \"\"\n}"
      },
      "typeVersion": 1
    },
    {
      "id": "4488deb9-27f6-4f9d-b17e-9b5e7a1bba33",
      "name": "Sticky Note12",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        180,
        760
      ],
      "parameters": {
        "color": 5,
        "width": 323.2987132716669,
        "height": 80,
        "content": "### Run this once! \nIf for any reason you need to run more than once, be sure to clear the existing data first."
      },
      "typeVersion": 1
    },
    {
      "id": "5cb3bd73-1e77-4eba-9d2e-634fdc374330",
      "name": "Sticky Note11",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        780,
        1480
      ],
      "parameters": {
        "color": 5,
        "width": 323.2987132716669,
        "height": 110.05160146874424,
        "content": "### First Time Running?\nThere is a slight delay on first run because the code node has to download the required packages."
      },
      "typeVersion": 1
    }
  ],
  "pinData": {},
  "connections": {
    "Zip Entries": {
      "main": [
        [
          {
            "node": "Reviews to List",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Find Reviews": {
      "main": [
        [
          {
            "node": "Apply K-means Clustering Algorithm",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set Variables": {
      "main": [
        [
          {
            "node": "Clear Existing Reviews",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set Variables1": {
      "main": [
        [
          {
            "node": "Find Reviews",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract Reviews": {
      "main": [
        [
          {
            "node": "Zip Entries",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Reviews to List": {
      "main": [
        [
          {
            "node": "Qdrant Vector Store",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Clusters To List": {
      "main": [
        [
          {
            "node": "Only Clusters With 3+ points",
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
            "node": "Qdrant Vector Store",
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
            "node": "Customer Insights Agent",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Default Data Loader": {
      "ai_document": [
        [
          {
            "node": "Qdrant Vector Store",
            "type": "ai_document",
            "index": 0
          }
        ]
      ]
    },
    "Get TrustPilot Page": {
      "main": [
        [
          {
            "node": "Extract Reviews",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Qdrant Vector Store": {
      "main": [
        [
          {
            "node": "Prep Values For Trigger",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Payload of Points": {
      "main": [
        [
          {
            "node": "Customer Insights Agent",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Clear Existing Reviews": {
      "main": [
        [
          {
            "node": "Get TrustPilot Page",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Prep Output For Export": {
      "main": [
        [
          {
            "node": "Export To Sheets",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Customer Insights Agent": {
      "main": [
        [
          {
            "node": "Prep Output For Export",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Prep Values For Trigger": {
      "main": [
        [
          {
            "node": "Trigger Insights",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Execute Workflow Trigger": {
      "main": [
        [
          {
            "node": "Set Variables1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Only Clusters With 3+ points": {
      "main": [
        [
          {
            "node": "Get Payload of Points",
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
    },
    "When clicking ‘Test workflow’": {
      "main": [
        [
          {
            "node": "Set Variables",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Apply K-means Clustering Algorithm": {
      "main": [
        [
          {
            "node": "Clusters To List",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2116"></a>

## Template 2116 - Verificação de assinatura de webhook Slack

- **Nome:** Verificação de assinatura de webhook Slack
- **Descrição:** Valida que uma requisição recebida via webhook realmente veio do Slack, verificando a assinatura HMAC-SHA256 usando o Signing Secret.
- **Funcionalidade:** • Recepção do webhook: Recebe a requisição enviada pelo Slack contendo headers e corpo.
• Construção da string-base de assinatura: Monta a string no formato v0:timestamp:encoded_body usando o timestamp do header x-slack-request-timestamp e o corpo codificado.
• Codificação do corpo: Converte o corpo para application/x-www-form-urlencoded adaptado às regras do Slack (espaços para '+', codificação de '*' e '~', etc.).
• Cálculo HMAC-SHA256: Gera a assinatura HMAC usando o Signing Secret do app para produzir a assinatura candidata.
• Comparação de assinaturas: Compara a assinatura calculada com o header x-slack-signature (esperando o prefixo v0=).
• Fluxo condicional: Se a verificação falhar, interrompe com erro; se for bem-sucedida, marca a requisição como verificada (signature_verified = true) e prossegue com os dados originais.
- **Ferramentas:** • Slack: Plataforma de mensagens que envia webhooks e fornece o Signing Secret necessário para verificar a origem das requisições.

## Fluxo visual

```mermaid
flowchart LR
    N1["Make Slack Verif Token"]
    N2["Encode Secret String"]
    N3["IF"]
    N4["Stop and Error"]
    N5["Execute Workflow Trigger"]
    N6["Sticky Note"]
    N7["Set Verified to True"]
    N8["Merge"]
    N9["Sticky Note1"]
    N10["Sticky Note2"]
    N11["Sticky Note3"]
    N12["Sticky Note4"]

    N3 --> N7
    N3 --> N4
    N2 --> N3
    N7 --> N8
    N1 --> N2
    N5 --> N1
    N5 --> N8
```

## Fluxo (.json) :

```json
{
  "id": "84dT8cFL0FV8ZGPx",
  "meta": {
    "instanceId": "85d2d2ffc8886227640b031e8f18fdfe6c91f530d34ec1a8b1f13727419ae956"
  },
  "name": "Slack Webhook - Verify Signature",
  "tags": [],
  "nodes": [
    {
      "id": "b12fe8e7-45c4-4021-826e-3ae430e34001",
      "name": "Make Slack Verif Token",
      "type": "n8n-nodes-base.code",
      "position": [
        900,
        400
      ],
      "parameters": {
        "jsCode": "function encodeFormData(data) {\n  const encodedData = Object.keys(data)\n    .map(key => encodeURIComponent(key) + '=' + encodeURIComponent(data[key]))\n    .join('&')\n    .replaceAll(\"%20\", \"+\") // Slack does not encode \"+\" signs\n    .replaceAll(\"*\", \"%2A\") // Slack encodes \"*\" signs\n    .replaceAll(\"~\", \"%7E\"); // Slack encodes \"~\" signs\n    \n  return encodedData;\n}\n\nfunction buildSigBaseString(requestJson) {\n  const version = \"v0\"; // Slack Webhook version (Always v0 for the moment)\n  \n  const timestamp = requestJson.headers[\"x-slack-request-timestamp\"];\n  \n  const body = requestJson.body;\n  const encodedBody = encodeFormData(body);\n  \n  const sigBaseString = `${version}:${timestamp}:${encodedBody}`;\n\n  return sigBaseString;\n}\n\nconst requestJson = $input.first().json;\n\nconst sigBaseString = buildSigBaseString(requestJson);\n\nconst requestSignature = requestJson.headers[\"x-slack-signature\"];\n\nconsole.log({\n    sigBaseString,\n    requestSignature\n  });\nreturn {\n  json: {\n    sigBaseString,\n    requestSignature\n  },\n  pairedItem: 0\n}\n\n\n"
      },
      "typeVersion": 2
    },
    {
      "id": "a91e2d8f-e907-439c-9fd3-cb75e957b059",
      "name": "Encode Secret String",
      "type": "n8n-nodes-base.crypto",
      "position": [
        1120,
        400
      ],
      "parameters": {
        "type": "SHA256",
        "value": "={{ $json.sigBaseString }}",
        "action": "hmac",
        "dataPropertyName": "candidateSignature"
      },
      "typeVersion": 1
    },
    {
      "id": "d79ccfe1-61cd-4da4-bfff-1e504627bb3d",
      "name": "IF",
      "type": "n8n-nodes-base.if",
      "position": [
        1360,
        400
      ],
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{ $json.requestSignature }}",
              "value2": "=v0={{ $json.candidateSignature }}"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "id": "cb2b9908-c226-438b-adb2-7c1ec852e007",
      "name": "Stop and Error",
      "type": "n8n-nodes-base.stopAndError",
      "position": [
        1580,
        580
      ],
      "parameters": {
        "errorMessage": "Could not verify Slack Webhook signature"
      },
      "typeVersion": 1
    },
    {
      "id": "5ef4c06a-717b-4f90-83a7-06eda780a892",
      "name": "Execute Workflow Trigger",
      "type": "n8n-nodes-base.executeWorkflowTrigger",
      "position": [
        680,
        400
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "86b022fb-63fd-4ccf-952e-19ed0da54a5c",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        880,
        -420
      ],
      "parameters": {
        "color": 4,
        "width": 554.4117841902089,
        "height": 278.2403290971726,
        "content": "## Slack Webhook - Verify Signature \nWhen receiving a message from a Slack Webhook, it is much more secure to verify that the message comes from Slack and not from bots or unknown services.\n\nThis small template is designed to validate the received signature (See [this URL](https://api.slack.com/authentication/verifying-requests-from-slack)).\n\n### Colors\n- **Blue** areas are **areas to edit**\n- **Yellow** areas are **explanations**"
      },
      "typeVersion": 1
    },
    {
      "id": "f5af4f44-1ea5-419b-a58b-f8f6839b6b05",
      "name": "Set Verified to True",
      "type": "n8n-nodes-base.set",
      "position": [
        1580,
        220
      ],
      "parameters": {
        "fields": {
          "values": [
            {
              "name": "signature_verified",
              "type": "booleanValue"
            }
          ]
        },
        "include": "none",
        "options": {}
      },
      "typeVersion": 3.2
    },
    {
      "id": "8a76dec8-7a2d-4cc9-82c9-002141e205ec",
      "name": "Merge",
      "type": "n8n-nodes-base.merge",
      "position": [
        1920,
        40
      ],
      "parameters": {
        "mode": "combine",
        "options": {},
        "combinationMode": "mergeByPosition"
      },
      "typeVersion": 2.1
    },
    {
      "id": "0c8506bc-b114-4d25-8586-80549ae0026d",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1000,
        40
      ],
      "parameters": {
        "color": 6,
        "width": 359.58396920054975,
        "height": 548.3119898759418,
        "content": "## TO EDIT \nSet your Slack Signing Secret.\nYou can obtain it by visiting your Slack App dashboard in the general tab: https://api.slack.com/apps/[SLACK_APP_ID]/general\n"
      },
      "typeVersion": 1
    },
    {
      "id": "20cca69c-9d00-4471-8845-2cb91458c23e",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1560,
        399
      ],
      "parameters": {
        "width": 300.4638046519632,
        "height": 360.20237540316725,
        "content": "## Error Output\nIf the signature cannot be verified, an error will be raised. You can manage this scenario in your main workflow by either using an Error Workflow or by modifying your node settings and selecting appropriate actions in the event of an error.\n"
      },
      "typeVersion": 1
    },
    {
      "id": "55ede23b-acb4-43ea-ac32-c678dd48e056",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1880,
        -220
      ],
      "parameters": {
        "width": 300.4638046519632,
        "height": 427.3843805720155,
        "content": "## Success Output\nIf the signature is successfully verified, we return a key `verified_signature` set to `true` along with the data from the Slack request itself.\n"
      },
      "typeVersion": 1
    },
    {
      "id": "22d44888-5af4-43b9-b514-ebfc9c61b07c",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        560,
        160
      ],
      "parameters": {
        "width": 300.4638046519632,
        "height": 427.3843805720155,
        "content": "## Input\nThe input should be the received Slack request. Place this workflow directly after the Slack Webhook.\n"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "f9e78d89-0da8-465e-aa47-5396d9ac4d48",
  "connections": {
    "IF": {
      "main": [
        [
          {
            "node": "Set Verified to True",
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
    "Encode Secret String": {
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
    "Set Verified to True": {
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
    "Make Slack Verif Token": {
      "main": [
        [
          {
            "node": "Encode Secret String",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Execute Workflow Trigger": {
      "main": [
        [
          {
            "node": "Make Slack Verif Token",
            "type": "main",
            "index": 0
          },
          {
            "node": "Merge",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2117"></a>

## Template 2117 - Extração e resumo semanal de notícias

- **Nome:** Extração e resumo semanal de notícias
- **Descrição:** Rastreia uma página de notícias, extrai as publicações mais recentes, gera resumos e palavras-chave com IA e armazena os resultados em um banco de dados.
- **Funcionalidade:** • Agendamento semanal: inicia o processo em intervalo programado.
• Recuperação de HTML da página de notícias: obtém o conteúdo da lista de publicações.
• Extração de links e datas com seletores CSS: identifica URLs e datas de cada post.
• Criação de itens individuais por link/data: transforma listas em itens processáveis um a um.
• Filtragem por data: seleciona apenas posts dentro do período desejado (ex.: últimos dias).
• Requisições às páginas individuais: obtém o HTML de cada post selecionado.
• Extração de título e conteúdo do post: isola texto principal e título usando seletores CSS.
• Geração de resumo curto: cria um resumo conciso (menos de 70 palavras) usando IA.
• Extração de 3 palavras-chave técnicas: identifica as principais palavras-chave técnicas por post.
• Agregação de metadados e conteúdo: combina título, link, data, resumo e palavras-chave.
• Armazenamento em banco de dados: grava os registros finais para consulta e processamento posterior.
- **Ferramentas:** • Site de notícias (Colt - https://www.colt.net/resources/type/news/): fonte das publicações a serem raspadas.
• OpenAI / ChatGPT API: gera resumos e extrai as palavras-chave técnicas de cada post.
• NocoDB: banco de dados SQL usado para armazenar título, data, link, resumo e palavras-chave.
• HTTP/HTML (requests): mecanismo para recuperar o HTML das páginas e dos posts individuais.

## Fluxo visual

```mermaid
flowchart LR
    N1["Extract the HTML with the right css class"]
    N2["Summary"]
    N3["Keywords"]
    N4["Rename keywords"]
    N5["Rename Summary"]
    N6["Merge"]
    N7["Extract date"]
    N8["Select posts of last 7 days"]
    N9["Merge date & links"]
    N10["HTTP Request1"]
    N11["Merge Content with Date & Link"]
    N12["Extract individual posts"]
    N13["Sticky Note"]
    N14["Merge ChatGPT output with Date & Link"]
    N15["Sticky Note1"]
    N16["Sticky Note2"]
    N17["Sticky Note3"]
    N18["Sticky Note4"]
    N19["Sticky Note5"]
    N20["Sticky Note6"]
    N21["Sticky Note7"]
    N22["Retrieve the web page for further processsing"]
    N23["Sticky Note9"]
    N24["Sticky Note10"]
    N25["Sticky Note11"]
    N26["Sticky Note12"]
    N27["Sticky Note13"]
    N28["Sticky Note14"]
    N29["Sticky Note15"]
    N30["Schedule Trigger each week"]
    N31["Sticky Note16"]
    N32["NocoDB news database"]
    N33["Sticky Note17"]
    N34["Sticky Note18"]
    N35["Create single link items"]
    N36["Create single date items"]

    N6 --> N14
    N2 --> N5
    N3 --> N4
    N7 --> N36
    N10 --> N12
    N5 --> N6
    N4 --> N6
    N9 --> N8
    N36 --> N9
    N35 --> N9
    N12 --> N11
    N30 --> N22
    N8 --> N11
    N8 --> N10
    N11 --> N2
    N11 --> N3
    N11 --> N14
    N14 --> N32
    N1 --> N35
    N22 --> N1
    N22 --> N7
```

## Fluxo (.json) :

```json
{
  "id": "xM8Z5vZVNTNjCySL",
  "meta": {
    "instanceId": "b8ef33547995f2a520f12118ac1f7819ea58faa7a1096148cac519fa08be8e99"
  },
  "name": "News Extraction",
  "tags": [],
  "nodes": [
    {
      "id": "97711d12-20de-40aa-b994-d2b10f20a5e5",
      "name": "Extract the HTML with the right css class",
      "type": "n8n-nodes-base.html",
      "position": [
        -500,
        0
      ],
      "parameters": {
        "options": {
          "trimValues": true
        },
        "operation": "extractHtmlContent",
        "extractionValues": {
          "values": [
            {
              "key": "data",
              "attribute": "href",
              "cssSelector": "=div:nth-child(9) > div:nth-child(3) > a:nth-child(2)",
              "returnArray": true,
              "returnValue": "attribute"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "id": "b874b570-daae-4878-b525-07ac30756eb1",
      "name": "Summary",
      "type": "n8n-nodes-base.openAi",
      "position": [
        -880,
        440
      ],
      "parameters": {
        "model": "gpt-4-1106-preview",
        "prompt": {
          "messages": [
            {
              "content": "=Create a summary in less than 70 words {{ $json[\"content\"] }}"
            }
          ]
        },
        "options": {},
        "resource": "chat"
      },
      "credentials": {
        "openAiApi": {
          "id": "0Vdk5RlVe7AoUdAM",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "72696278-2d44-4073-936a-6fe9df1bc7d8",
      "name": "Keywords",
      "type": "n8n-nodes-base.openAi",
      "position": [
        -880,
        620
      ],
      "parameters": {
        "model": "gpt-4-1106-preview",
        "prompt": {
          "messages": [
            {
              "content": "=name the 3 most important technical keywords in {{ $json[\"content\"] }} ? just name them without any explanations or other sentences"
            }
          ]
        },
        "options": {},
        "resource": "chat"
      },
      "credentials": {
        "openAiApi": {
          "id": "0Vdk5RlVe7AoUdAM",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "0bfdb3be-76ef-4bb3-902f-f0869342b83c",
      "name": "Rename keywords",
      "type": "n8n-nodes-base.set",
      "position": [
        -700,
        620
      ],
      "parameters": {
        "fields": {
          "values": [
            {
              "name": "keywords",
              "stringValue": "={{ $json[\"message\"][\"content\"] }}"
            }
          ]
        },
        "include": "none",
        "options": {}
      },
      "typeVersion": 3.1
    },
    {
      "id": "0387cf34-41c9-4729-8570-1db7b17c42f4",
      "name": "Rename Summary",
      "type": "n8n-nodes-base.set",
      "position": [
        -700,
        440
      ],
      "parameters": {
        "fields": {
          "values": [
            {
              "name": "=summary",
              "stringValue": "={{ $json[\"message\"][\"content\"] }}"
            }
          ]
        },
        "include": "none",
        "options": {}
      },
      "typeVersion": 3.1
    },
    {
      "id": "5fa1702c-f0bf-4524-bc8f-6f550dd83f1e",
      "name": "Merge",
      "type": "n8n-nodes-base.merge",
      "position": [
        -480,
        560
      ],
      "parameters": {
        "mode": "combine",
        "options": {},
        "combinationMode": "mergeByPosition"
      },
      "typeVersion": 2.1
    },
    {
      "id": "25128a71-b0d5-49a4-adb8-c3fbe03c0a85",
      "name": "Extract date",
      "type": "n8n-nodes-base.html",
      "position": [
        -500,
        -160
      ],
      "parameters": {
        "options": {},
        "operation": "extractHtmlContent",
        "extractionValues": {
          "values": [
            {
              "key": "data",
              "cssSelector": "div:nth-child(9) > div:nth-child(2) > span:nth-child(1)",
              "returnArray": true
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "id": "138b3bd6-494a-49b9-b5b8-c9febcfef9fb",
      "name": "Select posts of last 7 days",
      "type": "n8n-nodes-base.code",
      "position": [
        120,
        0
      ],
      "parameters": {
        "jsCode": "const currentDate = new Date();\nconst sevenDaysAgo = new Date(currentDate.setDate(currentDate.getDate() - 70)); // Change the number of days going back to your liking (e.g. from -7 to -1) -> BUT sync with the cron job (first node)\n\nconst filteredItems = items.filter(item => {\n    const postDate = new Date(item.json[\"Date\"]); // Assuming \"Date\" is the field name in the extracted html\n    return postDate >= sevenDaysAgo;\n});\n\nreturn filteredItems;\n"
      },
      "typeVersion": 2
    },
    {
      "id": "1ace953b-e298-4fc2-8970-327f736889ec",
      "name": "Merge date & links",
      "type": "n8n-nodes-base.merge",
      "position": [
        -100,
        0
      ],
      "parameters": {
        "mode": "combine",
        "options": {},
        "combinationMode": "mergeByPosition"
      },
      "typeVersion": 2.1
    },
    {
      "id": "bba692fc-c225-41be-a969-179d8b99c071",
      "name": "HTTP Request1",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        320,
        0
      ],
      "parameters": {
        "url": "={{ $json[\"Link\"] }}",
        "options": {}
      },
      "typeVersion": 4.1
    },
    {
      "id": "26671065-631f-4684-9ee1-15f26b4cf1e4",
      "name": "Merge Content with Date & Link",
      "type": "n8n-nodes-base.merge",
      "position": [
        500,
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
      "id": "79beb744-97b8-4072-824a-6736b0a080ef",
      "name": "Extract individual posts",
      "type": "n8n-nodes-base.html",
      "position": [
        500,
        0
      ],
      "parameters": {
        "options": {},
        "operation": "extractHtmlContent",
        "extractionValues": {
          "values": [
            {
              "key": "title",
              "cssSelector": "h1.fl-heading > span:nth-child(1)"
            },
            {
              "key": "content",
              "cssSelector": ".fl-node-5c7574ae7d5c6 > div:nth-child(1)"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "id": "e89d9de5-875b-453e-825a-26f2bebcc8df",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        80,
        -107
      ],
      "parameters": {
        "width": 180.9747474601832,
        "height": 276.31054308676767,
        "content": "Select only the newest news: todays date going back xy days"
      },
      "typeVersion": 1
    },
    {
      "id": "8a603f2f-4208-48c7-b169-e5613f13fa7d",
      "name": "Merge ChatGPT output with Date & Link",
      "type": "n8n-nodes-base.merge",
      "position": [
        -180,
        560
      ],
      "parameters": {
        "mode": "combine",
        "options": {},
        "combinationMode": "mergeByPosition"
      },
      "typeVersion": 2.1
    },
    {
      "id": "e1036421-9ce1-4121-a692-602410ec7c95",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "disabled": true,
      "position": [
        -539.7802584556148,
        -4.722020203185366
      ],
      "parameters": {
        "width": 182.2748213508401,
        "height": 304.2550759710132,
        "content": "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nExtracting the individual links of the press release page in order to retrieve the individual posts on their respective **url**"
      },
      "typeVersion": 1
    },
    {
      "id": "3655ab22-6a17-429a-9d9b-d96bbcc78fee",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -538.404803912782,
        -304
      ],
      "parameters": {
        "width": 178.75185894039254,
        "height": 289.463147786618,
        "content": "Extracting the dates of the posts of the press release page.\nThe right CSS selector has to be chosen.\n[More info on datagrab.io](https://datagrab.io/blog/guide-to-css-selectors-for-web-scraping/)"
      },
      "typeVersion": 1
    },
    {
      "id": "2e27fb4c-426a-41e1-b5fb-9b2d78acd2a7",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -1300,
        -299.82161760751774
      ],
      "parameters": {
        "width": 334.4404040637068,
        "height": 1127.2017245821128,
        "content": "# Scraping posts of a news site without RSS feed\n\n\nThe [News Site](https://www.colt.net/resources/type/news/) from Colt, a telecom company, does not offer an RSS feed, therefore web scraping is the \nchoice to extract and process the news.\n\nThe goal is to get only the newest posts, a summary of each post and their respective (technical) keywords.\n\nNote that the news site offers the links to each news post, but not the individual news. We collect first the links and dates of each post before extracting the newest ones.\n\nThe result is sent to a SQL database, in this case a NocoDB database.\n\nThis process happens each week thru a cron job.\n\n**Requirements**:\n- Basic understanding of CSS selectors and how to get them via browser (usually: right click &rarr; inspect)\n- ChatGPT API account - normal account is not sufficient\n- A NocoDB database - of course you may choose any type of output target\n\n**Assumptions**:\n- CSS selectors work on the news site\n- The post has a date with own CSS selector - meaning date is not part of the news content\n\n**\"Warnings\"**\n- Not every site likes to be scraped, especially not in high frequency\n- Each website is structured in different ways, the workflow may then need several adaptations.\n\n\nHappy about any suggestion to improve. You may contact me on **Mastodon**: https://bonn.social/@askans"
      },
      "typeVersion": 1
    },
    {
      "id": "d43bd5b7-2aff-4a07-8aca-ca4747ec6c4d",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -927.8447474890202,
        -80
      ],
      "parameters": {
        "width": 153.90180146729315,
        "height": 237.91333335255808,
        "content": "Weekly cron job"
      },
      "typeVersion": 1
    },
    {
      "id": "e732d136-fcf1-4fc3-8bb6-bdcea3c78d9e",
      "name": "Sticky Note5",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -760,
        -80
      ],
      "parameters": {
        "width": 185.41515152389002,
        "height": 241.454848504947,
        "content": "The html of the news site is being retrieved: https://www.colt.net/resources/type/news/"
      },
      "typeVersion": 1
    },
    {
      "id": "d5e29ec3-5ef2-42f3-b316-9350644dbba4",
      "name": "Sticky Note6",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -340,
        -306
      ],
      "parameters": {
        "width": 187.3613302133812,
        "height": 469.2923233086395,
        "content": "As the extraction are returned as arrays, they transformed into individual JSON items to enable looping with other nodes"
      },
      "typeVersion": 1
    },
    {
      "id": "1af15c45-32c0-4abf-a35d-be7206823569",
      "name": "Sticky Note7",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -120,
        -103.54151515238902
      ],
      "parameters": {
        "width": 150,
        "height": 274.50898992724416,
        "content": "The links of the individual posts and the dates of the posts "
      },
      "typeVersion": 1
    },
    {
      "id": "f7c42748-f227-42d0-a9e2-fcb16dbd0f75",
      "name": "Retrieve the web page for further processsing",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        -720,
        0
      ],
      "parameters": {
        "url": "https://www.colt.net/resources/type/news/",
        "options": {
          "response": {
            "response": {
              "responseFormat": "text"
            }
          }
        }
      },
      "typeVersion": 4.1
    },
    {
      "id": "b2c36f26-8221-478f-a4b0-22758b1e5e58",
      "name": "Sticky Note9",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        292,
        -100
      ],
      "parameters": {
        "width": 155.0036363426638,
        "height": 272.1479798256519,
        "content": "Get the html of each individual **newest** post"
      },
      "typeVersion": 1
    },
    {
      "id": "6ae05c31-c09a-4b4e-a013-41571937bc39",
      "name": "Sticky Note10",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        460,
        -100
      ],
      "parameters": {
        "width": 184.07417896879767,
        "height": 269.2504410842093,
        "content": "Extracting the title & content (text) of each individual news post with the right CSS selector"
      },
      "typeVersion": 1
    },
    {
      "id": "e2da76d4-0c8c-4c61-924f-50aa9387e9ab",
      "name": "Sticky Note11",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        460,
        180
      ],
      "parameters": {
        "width": 191.87778190338406,
        "height": 234.13422787857044,
        "content": "Merge link to url, date with content (text) and title of each news psot"
      },
      "typeVersion": 1
    },
    {
      "id": "c124aaac-dce6-4658-9027-bdfe5c0c81e6",
      "name": "Sticky Note12",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -907.2264215202996,
        331.0681740778203
      ],
      "parameters": {
        "width": 150,
        "height": 256.2444361932317,
        "content": "Create a summary of each news post with ChatGPT. You need a ChatGPT API account for this"
      },
      "typeVersion": 1
    },
    {
      "id": "c9037e74-007b-4e44-b7f9-90e78b853eb5",
      "name": "Sticky Note13",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -909.595196087218,
        610.7495589157902
      ],
      "parameters": {
        "width": 152.85976723045226,
        "height": 218.52702200939785,
        "content": "\n\n\n\n\n\n\n\n\n\n\n\n\n\nGet the 3 keywords of each news post"
      },
      "typeVersion": 1
    },
    {
      "id": "756397d9-de80-4114-9dee-b4f4b9593333",
      "name": "Sticky Note14",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -740,
        340
      ],
      "parameters": {
        "width": 182.7735784797001,
        "height": 489.05192374172555,
        "content": "Just a renaming of data fields and eliminating unnecessary ones"
      },
      "typeVersion": 1
    },
    {
      "id": "a0dcb254-f064-45ed-8e22-30a6d079085b",
      "name": "Sticky Note15",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -520,
        480
      ],
      "parameters": {
        "width": 169.7675735887227,
        "height": 254.94383570413422,
        "content": "Merge summary and keywords of each news post"
      },
      "typeVersion": 1
    },
    {
      "id": "82993166-b273-4b82-a954-554c6892f825",
      "name": "Schedule Trigger each week",
      "type": "n8n-nodes-base.scheduleTrigger",
      "position": [
        -900,
        0
      ],
      "parameters": {
        "rule": {
          "interval": [
            {
              "field": "weeks",
              "triggerAtDay": [
                3
              ],
              "triggerAtHour": 4,
              "triggerAtMinute": 32
            }
          ]
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "3d670eb9-5a36-4cd9-8d2c-40adf848485e",
      "name": "Sticky Note16",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -220,
        477.5081090810816
      ],
      "parameters": {
        "width": 180.1723775015045,
        "height": 260.5279202647822,
        "content": "Add title, link and date to summary and keywords of each news post"
      },
      "typeVersion": 1
    },
    {
      "id": "62021393-e988-4834-9fa2-75a957b42890",
      "name": "NocoDB news database",
      "type": "n8n-nodes-base.nocoDb",
      "position": [
        60,
        560
      ],
      "parameters": {
        "table": "mhbalmu9aaqcun6",
        "fieldsUi": {
          "fieldValues": [
            {
              "fieldName": "=News_Source",
              "fieldValue": "=Colt"
            },
            {
              "fieldName": "Title",
              "fieldValue": "={{ $json[\"title\"] }}"
            },
            {
              "fieldName": "Date",
              "fieldValue": "={{ $json[\"Date\"] }}"
            },
            {
              "fieldName": "Link",
              "fieldValue": "={{ $json[\"Link\"] }}"
            },
            {
              "fieldName": "Summary",
              "fieldValue": "={{ $json[\"summary\"] }}"
            },
            {
              "fieldName": "Keywords",
              "fieldValue": "={{ $json[\"keywords\"] }}"
            }
          ]
        },
        "operation": "create",
        "projectId": "prqu4e8bjj4bv1j",
        "authentication": "nocoDbApiToken"
      },
      "credentials": {
        "nocoDbApiToken": {
          "id": "gjNns0VJMS3P2RQ3",
          "name": "NocoDB Token account"
        }
      },
      "typeVersion": 2
    },
    {
      "id": "e59e9fab-10a7-470b-afa6-e1d4b4e57723",
      "name": "Sticky Note17",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        280,
        480
      ],
      "parameters": {
        "width": 483.95825869942666,
        "height": 268.5678114630957,
        "content": "## News summaries and keywords &rarr; database\n\n[NocoDB](https://nocodb.com/) is an SQL database, here we store the news summaries and keywords for further processing. Any other output target can be chosen here, e.g. e-mail, Excel etc.\n\nYou need first have that database structured before appending the news summaries and additional fields. The you can shape this node.\n\nSome fields may be edited in the database itself (e.g. relevance of the news to you) and may be filled therefore with a default value or not at all"
      },
      "typeVersion": 1
    },
    {
      "id": "253b414b-9a5b-4a25-892b-9aa011d55d28",
      "name": "Sticky Note18",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        20,
        480
      ],
      "parameters": {
        "width": 262.99083066277313,
        "height": 268.56781146309544,
        "content": ""
      },
      "typeVersion": 1
    },
    {
      "id": "438e8dde-ce0a-4e5e-8d62-d735d19ec189",
      "name": "Create single link items",
      "type": "n8n-nodes-base.itemLists",
      "position": [
        -300,
        0
      ],
      "parameters": {
        "options": {
          "destinationFieldName": "Link"
        },
        "fieldToSplitOut": "data"
      },
      "typeVersion": 3
    },
    {
      "id": "d721776b-fefc-4e72-91ef-6710f10b0393",
      "name": "Create single date items",
      "type": "n8n-nodes-base.itemLists",
      "position": [
        -300,
        -160
      ],
      "parameters": {
        "options": {
          "destinationFieldName": "Date"
        },
        "fieldToSplitOut": "data"
      },
      "typeVersion": 3
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "ff89d802-3bcf-4b34-9cd9-776b1f3b5eab",
  "connections": {
    "Merge": {
      "main": [
        [
          {
            "node": "Merge ChatGPT output with Date & Link",
            "type": "main",
            "index": 1
          }
        ]
      ]
    },
    "Summary": {
      "main": [
        [
          {
            "node": "Rename Summary",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Keywords": {
      "main": [
        [
          {
            "node": "Rename keywords",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract date": {
      "main": [
        [
          {
            "node": "Create single date items",
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
            "node": "Extract individual posts",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Rename Summary": {
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
    "Rename keywords": {
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
    "Merge date & links": {
      "main": [
        [
          {
            "node": "Select posts of last 7 days",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Create single date items": {
      "main": [
        [
          {
            "node": "Merge date & links",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Create single link items": {
      "main": [
        [
          {
            "node": "Merge date & links",
            "type": "main",
            "index": 1
          }
        ]
      ]
    },
    "Extract individual posts": {
      "main": [
        [
          {
            "node": "Merge Content with Date & Link",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Schedule Trigger each week": {
      "main": [
        [
          {
            "node": "Retrieve the web page for further processsing",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Select posts of last 7 days": {
      "main": [
        [
          {
            "node": "Merge Content with Date & Link",
            "type": "main",
            "index": 1
          },
          {
            "node": "HTTP Request1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Merge Content with Date & Link": {
      "main": [
        [
          {
            "node": "Summary",
            "type": "main",
            "index": 0
          },
          {
            "node": "Keywords",
            "type": "main",
            "index": 0
          },
          {
            "node": "Merge ChatGPT output with Date & Link",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Merge ChatGPT output with Date & Link": {
      "main": [
        [
          {
            "node": "NocoDB news database",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract the HTML with the right css class": {
      "main": [
        [
          {
            "node": "Create single link items",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Retrieve the web page for further processsing": {
      "main": [
        [
          {
            "node": "Extract the HTML with the right css class",
            "type": "main",
            "index": 0
          },
          {
            "node": "Extract date",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2119"></a>

## Template 2119 - Atualizar nós desatualizados em workflows

- **Nome:** Atualizar nós desatualizados em workflows
- **Descrição:** Recebe uma lista de workflows com nós desatualizados e automatiza a marcação e atualização dos workflows, além de enviar um resumo por e-mail.
- **Funcionalidade:** • Receber entrada de workflows com nós desatualizados: Processa dados fornecidos por outro fluxo sobre workflows afetados.
• Marcar nós antigos: Prepend um símbolo configurável aos nomes dos nós desatualizados para destacá-los.
• Adicionar versão atualizada próxima ao nó antigo: Opcionalmente adiciona uma cópia do nó com a versão mais recente próximo ao nó desatualizado no canvas.
• Atualizar conexões: Ajusta chaves e referências das conexões do workflow para refletir as renomeações dos nós.
• Persistir alterações via API: Atualiza o objeto do workflow na instância usando a API apropriada.
• Gerar e enviar resumo por e-mail: Compila links para os workflows afetados e envia um e-mail de resumo com a lista de workflows modificados.
• Configurações ajustáveis: Permite definir o símbolo de marcação, considerar apenas atualizações major, e controlar se novos nós devem ser adicionados ao canvas.
- **Ferramentas:** • API da instância: Permite recuperar e atualizar workflows remotamente via chamadas à API da instância.
• Gmail: Envio do resumo por e-mail usando credenciais OAuth2 configuradas.

## Fluxo visual

```mermaid
flowchart LR
    N1["Execute Workflow Trigger"]
    N2["Sticky Note4"]
    N3["Prepare Output"]
    N4["Send Summary"]
    N5["Get Workflow"]
    N6["Update Workflow"]
    N7["Modify Workflow (if required)"]
    N8["Start Reference"]
    N9["Sticky Note"]
    N10["Sticky Note2"]
    N11["Sticky Note1"]
    N12["Sticky Note5"]
    N13["Settings"]
    N14["Sticky Note6"]
    N15["Sticky Note7"]
    N16["Sticky Note8"]

    N13 --> N5
    N5 --> N7
    N3 --> N4
    N8 --> N13
    N6 --> N3
    N1 --> N8
    N7 --> N6
```

## Fluxo (.json) :

```json
{
  "id": "xlMrGt0c1eFi4J1U",
  "meta": {
    "instanceId": "fb8bc2e315f7f03c97140b30aa454a27bc7883a19000fa1da6e6b571bf56ad6d",
    "templateCredsSetupCompleted": true
  },
  "name": "Addon for Workflow Nodes Update Check Template",
  "tags": [],
  "nodes": [
    {
      "id": "e8068a93-5474-474e-a48e-947269b7ca5f",
      "name": "Execute Workflow Trigger",
      "type": "n8n-nodes-base.executeWorkflowTrigger",
      "position": [
        860,
        1140
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "9b4524d8-6ded-489b-bf45-6810f5306652",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        800,
        120
      ],
      "parameters": {
        "color": 5,
        "width": 1316.8621045610755,
        "height": 887.980239951363,
        "content": "## Download the main workflow and connect it's output to this workflow\n- Download this workflow and follow the belonging instructions: [https://n8n.io/workflows/2301-check-if-workflows-contain-build-in-nodes-that-are-not-of-the-latest-version/](https://n8n.io/workflows/2301-check-if-workflows-contain-build-in-nodes-that-are-not-of-the-latest-version/)\n- Add an \"Execute Workflow\" node and configure it, so it calls this workflow.\n  \n![Image](https://i.imgur.com/y0vPhYz.png#full-width)"
      },
      "typeVersion": 1
    },
    {
      "id": "cb0cacc1-34d0-4e4d-a7db-e44ece1a155f",
      "name": "Prepare Output",
      "type": "n8n-nodes-base.set",
      "position": [
        2180,
        1140
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "26c2bf59-2051-47e3-a6bf-3896ad427404",
              "name": "name",
              "type": "string",
              "value": "=<a href={{ $('Settings').item.json.instanceBaseUrl }}/workflow/{{ $json.id }}>{{ $json.name }}</a>"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "4b914937-1cff-4fc2-886b-64ec6818daf3",
      "name": "Send Summary",
      "type": "n8n-nodes-base.gmail",
      "position": [
        2400,
        1140
      ],
      "webhookId": "1ad759b3-f1cd-49dd-b288-e3344fa94c8a",
      "parameters": {
        "message": "=These workflows contain outdated nodes:<br>\n<ul>\n{{ $('Prepare Output').all().pluck('json').pluck('name').map(item => \"<li>\"+item+\"</li>\").join('') }}\n</ul>",
        "options": {
          "appendAttribution": false
        },
        "subject": "Outdated n8n Workflow Nodes"
      },
      "credentials": {
        "gmailOAuth2": {
          "id": "TWM2BLjDHQtGAFQn",
          "name": "Gmail (octionicsolutions)"
        }
      },
      "executeOnce": true,
      "typeVersion": 2.1
    },
    {
      "id": "2f259d45-cb31-4007-beb0-93123cc619c3",
      "name": "Get Workflow",
      "type": "n8n-nodes-base.n8n",
      "position": [
        1520,
        1140
      ],
      "parameters": {
        "operation": "get",
        "workflowId": {
          "__rl": true,
          "mode": "id",
          "value": "={{ $('Start Reference').item.json.Id }}"
        },
        "requestOptions": {}
      },
      "credentials": {
        "n8nApi": {
          "id": "fRyEJuhN9Nf3aQap",
          "name": "n8n account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "e2bbfc5b-1af6-43b1-9d03-f35b5837d3cc",
      "name": "Update Workflow",
      "type": "n8n-nodes-base.n8n",
      "position": [
        1960,
        1140
      ],
      "parameters": {
        "operation": "update",
        "workflowId": {
          "__rl": true,
          "mode": "id",
          "value": "={{ $json.id }}"
        },
        "requestOptions": {},
        "workflowObject": "={{ JSON.stringify($json) }}"
      },
      "credentials": {
        "n8nApi": {
          "id": "fRyEJuhN9Nf3aQap",
          "name": "n8n account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "f2bb0529-6e38-46c6-93e8-de76e9ecc31e",
      "name": "Modify Workflow (if required)",
      "type": "n8n-nodes-base.code",
      "position": [
        1740,
        1140
      ],
      "parameters": {
        "mode": "runOnceForEachItem",
        "jsCode": "let symbol = $('Settings').item.json.symbol;\nlet onlyMajorChanges = $('Settings').item.json.onlyMajorChanges;\nlet addNodesToCanvas = $('Settings').item.json.addNodesToCanvas;\n\n// create shallow copy including nested objects\nlet data = JSON.parse(JSON.stringify($json));\n\nchangeCount = 0;\n// Loop through nodes and update the names\nfor (let outdatedNode of $('Start Reference').item.json.outdated_nodes) {\n  // skip minor changes, if settings require it\n  if (onlyMajorChanges && outdatedNode.version.toString().substring(0, 1) == outdatedNode.latestVersion.toString().substring(0, 1)) {\n    continue;\n  }\n  // update nodes, it they are not already renamed with symbol\n  for (let existingNode of data.nodes) {\n    if (outdatedNode.name == existingNode.name && !existingNode.name.startsWith(symbol) && existingNode.id) {\n      // prepend new nodes, so they appear below outdated nodes on the canvas\n      if (addNodesToCanvas) {\n        let newNode = JSON.parse(JSON.stringify(existingNode));\n        delete newNode.id;\n        newNode.typeVersion = outdatedNode.latestVersion;\n        newNode.position = [newNode.position[0] + 40, newNode.position[1] - 40];\n        data.nodes.unshift(newNode);\n      }\n      // rename outdated nodes (prepend symbol)\n      existingNode.name = symbol + \" \" + existingNode.name;\n    \n      // update connections\n      for (let connectionKey in data.connections) {\n        let connection = data.connections[connectionKey];\n      \n        // rename keys\n        if (connectionKey == outdatedNode.name) {\n          let newKey = symbol + \" \" + connectionKey;\n          data.connections[newKey] = connection;\n          delete data.connections[connectionKey];\n        }\n      \n        // check the nested \"main\" array\n        if (connection.main) {\n          for (let mainArray of connection.main) {\n            for (let nodeObj of mainArray) {\n              if (nodeObj.node == outdatedNode.name) {\n                nodeObj.node = symbol + \" \" + nodeObj.node;\n              }\n            }\n          }\n        }\n      }\n      changeCount++;\n    }\n  }\n}\n\nif (changeCount == 0) {\n  return null;\n}\n\nreturn {\n  id: data.id,\n  name: data.name,\n  nodes: data.nodes,\n  connections: data.connections,\n  settings: data.settings\n}"
      },
      "typeVersion": 2
    },
    {
      "id": "b4b7d328-8128-4f07-841a-1efa26c3fdd5",
      "name": "Start Reference",
      "type": "n8n-nodes-base.noOp",
      "position": [
        1080,
        1140
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "7d80b557-15ac-479e-a219-dd254580a063",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        800,
        1020
      ],
      "parameters": {
        "color": 7,
        "width": 216.6228464570463,
        "height": 282.1449413577448,
        "content": "This workflow is called by another workflow which provides a list of all workflows with major and minor node updates"
      },
      "typeVersion": 1
    },
    {
      "id": "1becaab6-fe2a-44e9-bc7e-ce87665f25bd",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2120,
        680
      ],
      "parameters": {
        "color": 7,
        "width": 435.46822963832705,
        "height": 327.68691689762716,
        "content": "## Example input data\n\n```\n[\n  {\n    \"workflow\": \"Workflow Nodes Update\",\n    \"Id\": \"dFJpQTFg3QPH6Ol9\",\n    \"outdated_nodes\": [\n      {\n        \"name\": \"If\",\n        \"type\": \"n8n-nodes-base.if\",\n        \"version\": 2,\n        \"latestVersion\": 2.2\n      }\n    ]\n  }\n]\n```"
      },
      "typeVersion": 1
    },
    {
      "id": "9ce81677-4dd4-4a9a-a7a3-66b113c69de6",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1020,
        1020
      ],
      "parameters": {
        "color": 7,
        "width": 216.6228464570463,
        "height": 282.1449413577448,
        "content": "The following nodes start referencing from here, so it is easily possible to change the logic prior to this node."
      },
      "typeVersion": 1
    },
    {
      "id": "f6e7e7ce-1282-4292-8675-ca8bbe215d5f",
      "name": "Sticky Note5",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1240,
        1020
      ],
      "parameters": {
        "width": 216.6228464570463,
        "height": 282.1449413577448,
        "content": "## Update settings\nMinimum requirement:\n- Set your instanceBaseUrl"
      },
      "typeVersion": 1
    },
    {
      "id": "46b168d5-c866-497b-8664-92722a356feb",
      "name": "Settings",
      "type": "n8n-nodes-base.set",
      "position": [
        1300,
        1140
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "99947a54-e9f9-4d04-b273-9d7eeed62775",
              "name": "instanceBaseUrl",
              "type": "string",
              "value": "http://localhost:5432"
            },
            {
              "id": "35a63bda-fcbb-4885-a8d6-4b52c6579206",
              "name": "symbol",
              "type": "string",
              "value": "⚠️"
            },
            {
              "id": "3481286b-359f-4e86-8f56-bdb267ebd6a2",
              "name": "onlyMajorChanges",
              "type": "boolean",
              "value": true
            },
            {
              "id": "2377c274-5501-494f-813e-0d3ebe47e375",
              "name": "addNodesToCanvas",
              "type": "boolean",
              "value": true
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "d28ac933-7dbc-4039-821b-7cd4c4c5ec94",
      "name": "Sticky Note6",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2120,
        1020
      ],
      "parameters": {
        "color": 7,
        "width": 216.6228464570463,
        "height": 282.1449413577448,
        "content": "URL's are generated for each affected workflow"
      },
      "typeVersion": 1
    },
    {
      "id": "0fef2be5-92d5-4d4f-8afc-b958ee616787",
      "name": "Sticky Note7",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2340,
        1020
      ],
      "parameters": {
        "width": 216.6228464570463,
        "height": 282.1449413577448,
        "content": "## Setup Gmail\nMinimum requirement:\n- Update mail recipient"
      },
      "typeVersion": 1
    },
    {
      "id": "dc940f78-1eff-4393-9d9a-f4afefe24d45",
      "name": "Sticky Note8",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1460,
        1020
      ],
      "parameters": {
        "color": 7,
        "width": 657.2496253932529,
        "height": 282.1449413577448,
        "content": "Each workflow is being processed and modified if needed. Depending on the settings an icon is being prepended to the name of outdated nodes. In addition a newer version is being added close by, so it can be replaced quicker by the user."
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "f4bb34b0-7561-4d77-beac-8f6988a0ed64",
  "connections": {
    "Settings": {
      "main": [
        [
          {
            "node": "Get Workflow",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Workflow": {
      "main": [
        [
          {
            "node": "Modify Workflow (if required)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Prepare Output": {
      "main": [
        [
          {
            "node": "Send Summary",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Start Reference": {
      "main": [
        [
          {
            "node": "Settings",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Update Workflow": {
      "main": [
        [
          {
            "node": "Prepare Output",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Execute Workflow Trigger": {
      "main": [
        [
          {
            "node": "Start Reference",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Modify Workflow (if required)": {
      "main": [
        [
          {
            "node": "Update Workflow",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2121"></a>

## Template 2121 - Portal Docsify para documentação de fluxos

- **Nome:** Portal Docsify para documentação de fluxos
- **Descrição:** Serve uma interface Docsify que lista, gera, edita e salva documentação em Markdown para fluxos, incluindo geração automática de conteúdo e diagramas.
- **Funcionalidade:** • Página principal Docsify: Fornece a aplicação HTML que carrega o conteúdo Markdown e a navegação.
• Listagem de fluxos: Gera tabela com workflows, status, datas, nós e links para documentação e edição.
• Navegação por tags: Cria painel lateral com tags para filtrar a lista de fluxos.
• Servir arquivos Markdown: Responde a pedidos GET de arquivos como README.md, summary.md e páginas de docs individuais.
• Geração automática de docs: Quando não houver arquivo, usa um modelo e um modelo de linguagem para criar documentação inicial.
• Geração de diagrama Mermaid: Constrói um gráfico mermaid a partir da estrutura e conexões do fluxo.
• Editor Markdown ao vivo: Página de edição com pré-visualização Docsify e renderização de Mermaid, com botões Salvar/Cancelar.
• Salvar e recriar arquivos: Escreve arquivos Markdown no diretório configurado, cria diretório se necessário e permite recriar docs.
• Tratamento de páginas ausentes: Fornece conteúdo de fallback para nomes de arquivo inesperados.
• Suporte a operações via query (view/edit/save/recreate): Diferencia ações conforme parâmetros da requisição.
- **Ferramentas:** • Docsify: Biblioteca JavaScript para renderizar Markdown no cliente e estruturar a navegação e preview.
• Mermaid.js: Biblioteca para converter texto mermaid em diagramas SVG interativos.
• OpenAI (GPT-4-turbo): Modelo de linguagem usado para gerar automaticamente a descrição do fluxo e configurações dos nós.
• jsDelivr CDN: Fornecimento de themes e bibliotecas (ex.: docsify, temas) por CDN.
• Sistema de arquivos local: Armazenamento e leitura/escrita dos arquivos Markdown em um diretório acessível ao serviço.
• Prism.js: Biblioteca de realce de sintaxe usada na pré-visualização Markdown.

## Fluxo visual

```mermaid
flowchart LR
    N1["CONFIG"]
    N2["Convert to File"]
    N3["HasFile?"]
    N4["Extract from File"]
    N5["Main Page"]
    N6["Instance overview"]
    N7["Sort-workflows"]
    N8["doc action"]
    N9["Empty Set"]
    N10["Load Doc File"]
    N11["Respond with markdown"]
    N12["Respond with HTML"]
    N13["Save New Doc File"]
    N14["Blank Doc File"]
    N15["Fetch Single Workflow1"]
    N16["Fill Workflow Table"]
    N17["Basic LLM Chain"]
    N18["OpenAI Chat Model"]
    N19["Structured Output Parser"]
    N20["Auto-fixing Output Parser"]
    N21["Respond with main page HTML"]
    N22["Workflow Tags"]
    N23["No Operation, do nothing"]
    N24["Merge"]
    N25["Fallback file name"]
    N26["mkdir"]
    N27["Merge1"]
    N28["Edit Page"]
    N29["Workflow md content"]
    N30["Is Action Edit?1"]
    N31["Is Action Edit?2"]
    N32["Generate Mermaid Chart"]
    N33["Merge2"]
    N34["Generated Doc"]
    N35["Passthrough"]
    N36["Merge3"]
    N37["Merge4"]
    N38["Merge5"]
    N39["Edit Fields"]
    N40["Is Action Save?"]
    N41["Merge6"]
    N42["Respond OK on Save"]
    N43["single workflow"]
    N44["Sticky Note"]
    N45["Sticky Note1"]
    N46["Sticky Note2"]
    N47["file types"]
    N48["Sticky Note3"]
    N49["Get All Workflows"]
    N50["Sticky Note4"]
    N51["md files"]
    N52["Get Workflow tags"]
    N53["Sticky Note5"]
    N54["Sticky Note6"]
    N55["Sticky Note7"]
    N56["Sticky Note8"]
    N57["Sticky Note9"]
    N58["Sticky Note10"]
    N59["Sticky Note11"]
    N60["docsify"]

    N24 --> N30
    N26 --> N27
    N1 --> N37
    N1 --> N38
    N27 --> N3
    N33 --> N34
    N36 --> N31
    N37 --> N5
    N38 --> N47
    N41 --> N40
    N60 --> N1
    N60 --> N37
    N3 --> N4
    N3 --> N15
    N51 --> N49
    N51 --> N8
    N51 --> N52
    N51 --> N23
    N28 --> N12
    N9 --> N27
    N5 --> N21
    N8 --> N26
    N8 --> N10
    N8 --> N35
    N8 --> N9
    N8 --> N39
    N47 --> N51
    N39 --> N2
    N39 --> N41
    N35 --> N36
    N35 --> N24
    N34 --> N2
    N34 --> N31
    N10 --> N27
    N22 --> N11
    N14 --> N31
    N7 --> N16
    N17 --> N33
    N2 --> N13
    N40 --> N42
    N43 --> N1
    N43 --> N38
    N30 --> N14
    N30 --> N17
    N30 --> N33
    N31 --> N28
    N31 --> N29
    N4 --> N36
    N49 --> N7
    N52 --> N22
    N6 --> N11
    N13 --> N41
    N25 --> N11
    N16 --> N6
    N29 --> N11
    N15 --> N32
    N15 --> N24
    N32 --> N24
    N23 --> N25
```

## Fluxo (.json) :

```json
{
  "id": "VY4TXYGmqth57Een",
  "meta": {
    "instanceId": "fb924c73af8f703905bc09c9ee8076f48c17b596ed05b18c0ff86915ef8a7c4a",
    "templateCredsSetupCompleted": true
  },
  "name": "Docsify example",
  "tags": [],
  "nodes": [
    {
      "id": "f41906c3-ee4c-4333-bfd5-426f82ba4bd9",
      "name": "CONFIG",
      "type": "n8n-nodes-base.set",
      "position": [
        660,
        60
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "b48986ec-f58d-4a7f-afba-677edcb28d31",
              "name": "project_path",
              "type": "string",
              "value": "./.n8n/test_docs"
            },
            {
              "id": "cf632419-f839-4045-922c-03784bb3ae07",
              "name": "instance_url",
              "type": "string",
              "value": "={{$env[\"N8N_PROTOCOL\"]}}://{{$env[\"N8N_HOST\"]}}"
            },
            {
              "id": "7a7c70a6-1853-4ca7-b5b1-e36bb0e190d0",
              "name": "HTML_headers",
              "type": "string",
              "value": "= <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge,chrome=1\" />\n <meta name=\"viewport\" content=\"width=device-width,initial-scale=1\" />\n <meta charset=\"UTF-8\" />\n <link rel=\"stylesheet\" href=\"//cdn.jsdelivr.net/npm/docsify@4/themes/vue.css\" />\n <script src=\"https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js\"></script>"
            },
            {
              "id": "1e785afe-f05f-4e51-a164-f341da81ccac",
              "name": "HTML_styles_editor",
              "type": "string",
              "value": "= <style>\n body {\n margin: 0;\n padding: 0;\n overflow: hidden;\n }\n \n .container {\n display: flex;\n flex-direction: column;\n height: 100vh;\n margin: 0;\n }\n\n .button-container {\n display: flex;\n justify-content: center;\n gap: 10px;\n padding: 10px;\n background: #f8f8f8;\n border-bottom: 1px solid #eee;\n width: 50%;\n }\n\n .button {\n padding: 8px 16px;\n border: none;\n border-radius: 4px;\n cursor: pointer;\n font-size: 14px;\n }\n\n .save-button {\n background: #42b983;\n color: white;\n }\n\n .cancel-button {\n background: #666;\n color: white;\n }\n\n .editor-preview-container {\n display: flex;\n flex: 1;\n overflow: hidden;\n }\n \n #editor {\n width: 50%;\n height: 100%;\n resize: none;\n padding: 20px;\n box-sizing: border-box;\n font-family: monospace;\n border: none;\n border-right: 1px solid #eee;\n }\n \n .preview-container {\n width: 50%;\n height: 100%;\n overflow-y: auto;\n }\n\n /* Remove width from main */\n main {\n width: auto !important;\n }\n\n /* Fix code block wrapping */\n .markdown-section pre > code {\n white-space: pre-wrap !important;\n }\n </style>"
            },
            {
              "id": "37e22865-7b6b-438d-83a0-dc680d4775cc",
              "name": "HTML_docsify_include",
              "type": "string",
              "value": "= <script src=\"//cdn.jsdelivr.net/npm/docsify@4\"></script>"
            }
          ]
        },
        "includeOtherFields": true
      },
      "typeVersion": 3.4
    },
    {
      "id": "75cdf7fc-3dfa-49c1-bdbf-01d8be08aaa4",
      "name": "Convert to File",
      "type": "n8n-nodes-base.convertToFile",
      "position": [
        4020,
        1600
      ],
      "parameters": {
        "options": {},
        "operation": "toText",
        "sourceProperty": "workflowdata"
      },
      "typeVersion": 1.1
    },
    {
      "id": "3868011e-8374-496a-b3f5-4cbf7bde4e56",
      "name": "HasFile?",
      "type": "n8n-nodes-base.if",
      "position": [
        2400,
        880
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
              "id": "2d9feb22-49d1-4354-9b0b-b82da2b20678",
              "operator": {
                "type": "number",
                "operation": "gt"
              },
              "leftValue": "={{ Object.keys($json).length }}",
              "rightValue": 0
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "0bf2317b-2534-4022-9a16-395d4b44680c",
      "name": "Extract from File",
      "type": "n8n-nodes-base.extractFromFile",
      "position": [
        2660,
        860
      ],
      "parameters": {
        "options": {},
        "operation": "text",
        "destinationKey": "workflowdata"
      },
      "typeVersion": 1
    },
    {
      "id": "4b44a7f3-09bf-46a8-9520-247993af654b",
      "name": "Main Page",
      "type": "n8n-nodes-base.html",
      "position": [
        4660,
        -100
      ],
      "parameters": {
        "html": "<!DOCTYPE html>\n<html>\n <head>\n{{ $('CONFIG').first().json.HTML_headers }}\n <body>\n <div data-app id=\"main\">Please wait...</div>\n <script>\n \n mermaid.initialize({\n startOnLoad: false,\n });\n let svgCounter = 0;\n\n window.$docsify = {\n el: '#main',\n auto2top: true,\n loadSidebar: 'summary.md',\n basePath: '{{ $json.webhookUrl.split($json.webhookUrl.extractDomain())[1] }}/',\n name: 'All Workflows',\n markdown: {\n renderer: {\n code(code, lang) {\n if (lang === \"mermaid\") {\n const svgName = `mermaid-svg-${svgCounter++}`;\n const MERMAID_CONTAINER_ID = `${svgName}-container`;\n mermaid.render(svgName, code).then(({ svg }) => {\n const containerElement = document.querySelector(\n `#${MERMAID_CONTAINER_ID}`\n );\n if (containerElement) {\n containerElement.innerHTML = svg;\n } else {\n console.error(`Error: #${MERMAID_CONTAINER_ID} not found`);\n }\n });\n return `<div class=\"mermaid\" id=\"${MERMAID_CONTAINER_ID}\"></div>`;\n }\n return this.origin.code.apply(this, arguments);\n },\n },\n }, \n plugins: [\n function(hook, vm) {\n hook.ready(function() {\n // Check if URL doesn't end with slash but also isn't a file path\n if (!window.location.pathname.endsWith('/') && !window.location.pathname.includes('.')) {\n // Use history.replaceState to avoid adding to browser history\n const newUrl = window.location.pathname + '/' + window.location.hash;\n window.history.replaceState(null, null, newUrl);\n }\n });\n }\n ], \n };\n </script>\n{{ $('CONFIG').first().json.HTML_docsify_include }}\n </body>\n</html>"
      },
      "typeVersion": 1.2
    },
    {
      "id": "28c29cec-7efd-4f05-bf53-ac08cc3834a1",
      "name": "Instance overview",
      "type": "n8n-nodes-base.html",
      "position": [
        4660,
        160
      ],
      "parameters": {
        "html": "# Your n8n instance workflows:\n\n| Workflow | Status | Docs | Created | Updated | Nodes | Triggers |\n|----------|:------:|------|---------|---------|-------|----------|\n{{ $jmespath($input.all(),'[].json.content').join('\\n') }}"
      },
      "executeOnce": true,
      "typeVersion": 1.2
    },
    {
      "id": "3e8eb52e-8d35-4aa3-a485-6674d67720dc",
      "name": "Sort-workflows",
      "type": "n8n-nodes-base.sort",
      "position": [
        2080,
        160
      ],
      "parameters": {
        "options": {},
        "sortFieldsUi": {
          "sortField": [
            {
              "order": "descending",
              "fieldName": "updatedAt"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "id": "2178e1cf-90b8-4779-9b5c-3d6180823c95",
      "name": "doc action",
      "type": "n8n-nodes-base.switch",
      "position": [
        1740,
        1080
      ],
      "parameters": {
        "rules": {
          "values": [
            {
              "outputKey": "view",
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
                    "id": "ee386c7d-1abe-4864-bb3a-a19d3816c906",
                    "operator": {
                      "name": "filter.operator.equals",
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $json.query.action }}",
                    "rightValue": "view"
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "edit",
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
                    "id": "aa1a33ee-ac38-4ea4-9a4c-d355e7de1312",
                    "operator": {
                      "name": "filter.operator.equals",
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $json.query.action }}",
                    "rightValue": "edit"
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "recreate",
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
                    "id": "676c36e1-4c88-4314-9317-abc877ff3d17",
                    "operator": {
                      "name": "filter.operator.equals",
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $json.query.action }}",
                    "rightValue": "recreate"
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "save",
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
                    "id": "164314cf-7d99-4716-9949-b9196ce47959",
                    "operator": {
                      "name": "filter.operator.equals",
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $json.query.action }}",
                    "rightValue": "save"
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
      "id": "7f4aab9b-b7e8-4920-98e8-af8f504a1333",
      "name": "Empty Set",
      "type": "n8n-nodes-base.set",
      "position": [
        2000,
        960
      ],
      "parameters": {
        "options": {}
      },
      "typeVersion": 3.4
    },
    {
      "id": "1f35bc3e-29d7-47a2-a1c7-cf6052d99993",
      "name": "Load Doc File",
      "type": "n8n-nodes-base.readWriteFile",
      "position": [
        1900,
        860
      ],
      "parameters": {
        "options": {},
        "fileSelector": "={{ $('CONFIG').first().json.project_path }}/{{ $json.params.file }}"
      },
      "typeVersion": 1,
      "alwaysOutputData": true
    },
    {
      "id": "c0805f50-8f8c-49ba-b0c7-6768bf89798c",
      "name": "Respond with markdown",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        4920,
        1040
      ],
      "parameters": {
        "options": {
          "responseCode": 200,
          "responseHeaders": {
            "entries": [
              {
                "name": "Content-Type",
                "value": "text/markdown"
              }
            ]
          }
        },
        "respondWith": "text",
        "responseBody": "={{ $json.html }}"
      },
      "typeVersion": 1.1
    },
    {
      "id": "9c7a18b9-a081-4162-94f4-e125d666cbcc",
      "name": "Respond with HTML",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        4920,
        860
      ],
      "parameters": {
        "options": {
          "responseCode": 200,
          "responseHeaders": {
            "entries": [
              {
                "name": "Content-Type",
                "value": "text/html"
              }
            ]
          }
        },
        "respondWith": "text",
        "responseBody": "={{ $json.html }}"
      },
      "typeVersion": 1.1
    },
    {
      "id": "50944148-eb7c-4c28-99c5-478ddb2596f2",
      "name": "Save New Doc File",
      "type": "n8n-nodes-base.readWriteFile",
      "position": [
        4180,
        1600
      ],
      "parameters": {
        "options": {},
        "fileName": "={{ $('CONFIG').first().json.project_path }}/{{ $('CONFIG').first().json.params.file }}",
        "operation": "write"
      },
      "typeVersion": 1,
      "alwaysOutputData": true
    },
    {
      "id": "6d7e0dcf-d12b-4428-9c5e-ef7fb2c6be28",
      "name": "Blank Doc File",
      "type": "n8n-nodes-base.set",
      "position": [
        4000,
        1080
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "b168d9b1-1a13-4915-b59b-8a17258fd9cc",
              "name": "workflowdata",
              "type": "string",
              "value": "=# {{ $json.name }}\n\n## Workflow Description\n!> Please write what is this workflow doing\n\n## Workflow schematic\n\n```mermaid\n{{ $json.mermaidChart }}\n```\n\n## Any further information\n\n> You can also add tables like this:\n\n| Parameter | Value |\n|-----------|-------|\n| Created | {{ $json.createdAt }} |\n| Last updated | {{ $json.updatedAt }} |\n| Author | {{ $json.shared[0].project.name }} |\n\n"
            }
          ]
        },
        "includeOtherFields": true
      },
      "typeVersion": 3.4
    },
    {
      "id": "778a97eb-f7a2-4537-81fc-979dc6c674a2",
      "name": "Fetch Single Workflow1",
      "type": "n8n-nodes-base.n8n",
      "position": [
        2820,
        1200
      ],
      "parameters": {
        "operation": "get",
        "workflowId": {
          "__rl": true,
          "mode": "id",
          "value": "={{ $('CONFIG').first().json.params.file.replaceAll('docs_','').split('.md')[0] }}"
        },
        "requestOptions": {}
      },
      "credentials": {
        "n8nApi": {
          "id": "eW7IdTFt4ARJbEwR",
          "name": "Ted n8n account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "092b8c67-77f9-4d4b-aa26-8f0e3ea3ed29",
      "name": "Fill Workflow Table",
      "type": "n8n-nodes-base.set",
      "position": [
        2280,
        160
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "3bed44f3-7fa6-4d28-8a6e-7074ca354cd6",
              "name": "content",
              "type": "string",
              "value": "=| [{{ `${$json.name.replace(/[|\\\\[\\]`_*{}()<>#+-]/g, '\\\\$&')}` }}]({{ `${$('CONFIG').first().json.instance_url}/workflow/${$json.id}` }} \"Click to open workflow in n8n\") | {{ $json.active ? '[:green_circle:](# \"Active\")' : '[:white_circle:](# \"Inactive\")' }} | <nobr>[:book:]({{ `docs_${$json.id}?action=view` }} \"View docs\") [:memo:]({{ `docs_${$json.id}.md?action=edit` }} \":ignore Edit\") [:arrows_counterclockwise:]({{ `docs_${$json.id}?action=recreate` }} \"Recreate docs\")</nobr> | <nobr>{{ `${new Date($json.createdAt).toISOString().replace('T', ' ').slice(0, 16)}` }}</nobr> | <nobr>{{ `${new Date($json.updatedAt).toISOString().replace('T', ' ').slice(0, 16)}` }}</nobr> | {{ $json.nodes.length }} | {{ $json.nodes.filter(n => n.type.includes('Trigger')).length }} |"
            }
          ]
        }
      },
      "executeOnce": false,
      "typeVersion": 3.4
    },
    {
      "id": "18c58a09-0dfe-4cb4-ae7f-503957eabadb",
      "name": "Basic LLM Chain",
      "type": "@n8n/n8n-nodes-langchain.chainLlm",
      "onError": "continueRegularOutput",
      "position": [
        3480,
        1200
      ],
      "parameters": {
        "text": "=Here's the workflow data:\n{{Object.assign(\n Object.fromEntries(Object.entries($json).filter(([key]) => !['staticData', 'pinData'].includes(key))),\n {nodes: $json.nodes.map(node => Object.fromEntries(Object.entries(node).filter(([key]) => !['id', 'position'].includes(key))))}\n).toJsonString() }}",
        "messages": {
          "messageValues": [
            {
              "message": "=Your task is to generate simple workflow documentation for the n8n workflows. The user will provide a JSON structure. Reply \nin JSON format in 2 sections: workflow_desription and nodes_settings. Important! Each json key should be a simple markdown text without any additional comments or remarks from your end.\n\nInstruction for `workflow_desription`:\n```\n## Section header with H2\n\\n\n> subline with who created workflow and when, when it was last edited and the status (active / inactive as the green / grey round emoji). Also, when the documentation was generated. Now is: {{ $now }}.\n\\n\\n\nShould contain a description of the workflow. in a couple of paragraphs. Use direct voice without the fluff\n```\n\nInstruction for `nodes_settings`:\n```\n## Section header with H2.\n\\n\n### Node 1 name as H3 title\n - For each node make a bullet list with the main node configs. Ignore irrelevant configs. Enclose each config value in code backticks (`). Look:\n - Parameter 1 name: `Parameter 1 value`\n - Parameter 2 name: `Parameter 2 value`\n\\n\\n\n### Node 2 name as H3 title\n - For each node make a bullet list with the main node configs. Ignore irrelevant configs. Enclose each config value in code backticks (`). Look:\n - Parameter 1 name: `Parameter 1 value`\n - Parameter 2 name: `Parameter 2 value`\n\\n\\n\n```"
            }
          ]
        },
        "promptType": "define",
        "hasOutputParser": true
      },
      "typeVersion": 1.4,
      "alwaysOutputData": false
    },
    {
      "id": "9bc58cd3-a55e-4cda-95b5-7fa8dc0e7076",
      "name": "OpenAI Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        3480,
        1360
      ],
      "parameters": {
        "model": "gpt-4-turbo",
        "options": {
          "timeout": 120000,
          "temperature": 0.2
        }
      },
      "credentials": {
        "openAiApi": {
          "id": "rveqdSfp7pCRON1T",
          "name": "Ted's Tech Talks OpenAi"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "38fb6192-b8ce-4241-a9fe-aebda09aa8d5",
      "name": "Structured Output Parser",
      "type": "@n8n/n8n-nodes-langchain.outputParserStructured",
      "position": [
        3820,
        1360
      ],
      "parameters": {
        "jsonSchemaExample": "{\n\t\"workflow_description\": \"## Workflow overview\\n\\n>some additiona info\\n\\nWorkflow desctiption\",\n\t\"nodes_settings\": \"## Nodes settings\\n\\n###Node name 1\\n\\n- Setting 1\\n- Setting 2###Node name 2\\n\\n- Setting 1\\n- Setting 2\"\n}"
      },
      "typeVersion": 1.2
    },
    {
      "id": "29261bbb-dbbb-44df-b99d-bb084df7d846",
      "name": "Auto-fixing Output Parser",
      "type": "@n8n/n8n-nodes-langchain.outputParserAutofixing",
      "position": [
        3580,
        1360
      ],
      "parameters": {
        "options": {}
      },
      "typeVersion": 1
    },
    {
      "id": "086a57cf-a2b4-4f32-8ca6-38546e4856c1",
      "name": "Respond with main page HTML",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        4920,
        -100
      ],
      "parameters": {
        "options": {
          "responseCode": 200,
          "responseHeaders": {
            "entries": [
              {
                "name": "Content-Type",
                "value": "text/html"
              }
            ]
          }
        },
        "respondWith": "text",
        "responseBody": "={{ $json.html }}"
      },
      "typeVersion": 1.1
    },
    {
      "id": "fdbfe60b-e677-4897-ab1a-9a9f506bba27",
      "name": "Workflow Tags",
      "type": "n8n-nodes-base.html",
      "position": [
        4660,
        500
      ],
      "parameters": {
        "html": "- **Click to filter by tag:**\n{{ [...new Set($jmespath($input.all(),'[].json.tags[].name'))].map(tag => `- [${tag}](tag-${encodeURIComponent(tag)})`).join('\\n') }}"
      },
      "executeOnce": true,
      "typeVersion": 1.2
    },
    {
      "id": "94a258ed-c07c-42d4-8d37-3395fad205b0",
      "name": "No Operation, do nothing",
      "type": "n8n-nodes-base.noOp",
      "position": [
        1740,
        1880
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "c35ca075-52e7-4c2f-9891-f709afe36e52",
      "name": "Merge",
      "type": "n8n-nodes-base.merge",
      "position": [
        3140,
        1100
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
      "id": "55a1e32f-b20c-4b1f-9d6f-9bc4ec221fab",
      "name": "Fallback file name",
      "type": "n8n-nodes-base.html",
      "position": [
        4660,
        1900
      ],
      "parameters": {
        "html": "> File: {{ $json.params.file }}"
      },
      "typeVersion": 1.2
    },
    {
      "id": "3eef159b-99ad-4c9a-82f4-13bf16972521",
      "name": "mkdir",
      "type": "n8n-nodes-base.executeCommand",
      "position": [
        2100,
        1060
      ],
      "parameters": {
        "command": "=mkdir -p {{$('CONFIG').first().json.project_path}}"
      },
      "typeVersion": 1
    },
    {
      "id": "15fda233-925b-4a4d-964e-1916c0cd39a2",
      "name": "Merge1",
      "type": "n8n-nodes-base.merge",
      "position": [
        2240,
        880
      ],
      "parameters": {
        "mode": "chooseBranch"
      },
      "typeVersion": 3
    },
    {
      "id": "3e6c9243-d5f7-4f04-8231-9994963df36d",
      "name": "Edit Page",
      "type": "n8n-nodes-base.html",
      "position": [
        4660,
        860
      ],
      "parameters": {
        "html": "<!DOCTYPE html>\n<html>\n <head>\n{{ $('CONFIG').first().json.HTML_headers }}\n{{ $('CONFIG').first().json.HTML_styles_editor }}\n </head>\n <body>\n <div class=\"container\">\n <div class=\"button-container\">\n <button class=\"button save-button\" onclick=\"saveContent()\">Save</button>\n <button class=\"button cancel-button\" onclick=\"closeWindow()\">Cancel</button>\n </div>\n <div class=\"editor-preview-container\">\n <textarea id=\"editor\">{{ $json.workflowdata }}</textarea>\n <div class=\"preview-container\">\n <div id=\"preview\"></div>\n </div>\n </div>\n </div>\n \n<script>\n const editor = document.getElementById('editor');\n let vm;\n\n mermaid.initialize({\n startOnLoad: false,\n });\n\n let svgCounter = 0;\n\n // Function to save content\n async function saveContent() {\n try {\n const response = await fetch(window.location.pathname + '?action=save', {\n method: 'POST',\n headers: {\n 'Content-Type': 'application/json',\n },\n body: JSON.stringify({\n content: editor.value\n })\n });\n \n if (response.ok) {\n alert('Successfully saved!');\n } else {\n alert('Failed to save content');\n }\n } catch (error) {\n console.error('Error saving content:', error);\n alert('Error saving content');\n }\n }\n \n // Function to close window\n function closeWindow() {\n window.close();\n }\n \n window.$docsify = {\n el: '#preview',\n loadSidebar: false,\n loadNavbar: false,\n basePath: '/',\n hideSidebar: true,\n markdown: {\n renderer: {\n code(code, lang) {\n if (lang === \"mermaid\") {\n const svgName = `mermaid-svg-${svgCounter++}`;\n const MERMAID_CONTAINER_ID = `${svgName}-container`;\n mermaid.render(svgName, code).then(({ svg }) => {\n const containerElement = document.querySelector(\n `#${MERMAID_CONTAINER_ID}`\n );\n if (containerElement) {\n containerElement.innerHTML = svg;\n } else {\n console.error(`Error: #${MERMAID_CONTAINER_ID} not found`);\n }\n });\n return `<div class=\"mermaid\" id=\"${MERMAID_CONTAINER_ID}\"></div>`;\n }\n return this.origin.code.apply(this, arguments);\n },\n },\n },\n plugins: [\n function(hook, _vm) {\n vm = _vm;\n \n hook.beforeEach(function(content) {\n return editor.value;\n });\n }\n ]\n };\n \nlet timeout;\nfunction updatePreview() {\n clearTimeout(timeout);\n timeout = setTimeout(() => {\n if (vm) {\n const markdownSection = document.querySelector('.markdown-section');\n if (markdownSection) {\n const compiler = new window.DocsifyCompiler({\n basePath: '/',\n relativePath: false,\n fallbackLanguages: [],\n nameLink: '/',\n routerMode: 'hash'\n }, vm.router);\n \n const html = compiler.compile(editor.value);\n markdownSection.innerHTML = html;\n window.Prism.highlightAll();\n\n // Re-render all mermaid diagrams\n const mermaidDivs = markdownSection.querySelectorAll('pre[data-lang=\"mermaid\"] code');\n mermaidDivs.forEach((div, index) => {\n const code = div.textContent;\n const svgName = `mermaid-svg-${svgCounter++}`;\n const MERMAID_CONTAINER_ID = `${svgName}-container`;\n \n // Replace the <pre> element with our container\n const container = document.createElement('div');\n container.className = 'mermaid';\n container.id = MERMAID_CONTAINER_ID;\n div.parentElement.replaceWith(container);\n \n // Render the diagram\n mermaid.render(svgName, code).then(({ svg }) => {\n const containerElement = document.getElementById(MERMAID_CONTAINER_ID);\n if (containerElement) {\n containerElement.innerHTML = svg;\n }\n });\n });\n }\n }\n }, 500);\n};\n \n editor.addEventListener('input', updatePreview);\n</script>\n{{ $('CONFIG').first().json.HTML_docsify_include }}\n </body>\n</html>"
      },
      "typeVersion": 1.2
    },
    {
      "id": "71e136d5-bb5b-4eab-8cab-bfc50ea2a5a5",
      "name": "Workflow md content",
      "type": "n8n-nodes-base.html",
      "position": [
        4660,
        1040
      ],
      "parameters": {
        "html": "{{ $json.workflowdata }}"
      },
      "executeOnce": true,
      "typeVersion": 1.2
    },
    {
      "id": "6cb6f3b8-de65-43a5-9df3-48299ba7fcce",
      "name": "Is Action Edit?1",
      "type": "n8n-nodes-base.if",
      "position": [
        3300,
        1100
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
              "id": "856cdb3b-a187-4db5-b77b-43ee086780ee",
              "operator": {
                "name": "filter.operator.equals",
                "type": "string",
                "operation": "equals"
              },
              "leftValue": "={{ $json.query.action }}",
              "rightValue": "edit"
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "aff9ed71-bb49-4170-9ae3-5f05f89bab05",
      "name": "Is Action Edit?2",
      "type": "n8n-nodes-base.if",
      "position": [
        4180,
        880
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
              "id": "e3648023-8cb7-4b82-bd35-1ba196458327",
              "operator": {
                "name": "filter.operator.equals",
                "type": "string",
                "operation": "equals"
              },
              "leftValue": "={{ $json.query.action }}",
              "rightValue": "edit"
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "7b3d31a9-ee01-4bce-bc5b-78161536999d",
      "name": "Generate Mermaid Chart",
      "type": "n8n-nodes-base.code",
      "position": [
        3000,
        1260
      ],
      "parameters": {
        "jsCode": "const workflow = $input.first().json;\n\n// Extract nodes from the workflow\nconst nodes = workflow.nodes || [];\n\n// Node types to exclude\nconst excludedNodeTypes = ['n8n-nodes-base.stickyNote'];\n\n// Define shapes and their corresponding brackets\n// https://mermaid.js.org/syntax/flowchart.html\nconst shapes = {\n 'rect': ['[', ']'],\n 'rhombus': ['{', '}'],\n 'circle': ['((', '))'],\n 'hexagon': ['{{', '}}'],\n 'subroutine': ['[[', ']]'],\n 'parallelogram': ['[/', '/]'],\n 'wait': ['(', ')']\n // Add more shapes here as needed\n};\n\n// Define special shapes for specific node types\nconst specialShapes = {\n 'n8n-nodes-base.if': 'rhombus',\n 'n8n-nodes-base.switch': 'rhombus',\n 'n8n-nodes-base.code': 'subroutine',\n 'n8n-nodes-base.executeWorkflow': 'subroutine',\n 'n8n-nodes-base.httpRequest':'parallelogram',\n 'n8n-nodes-base.wait':'wait'\n // List more special node types\n};\n\n// Function to get the shape for a node type\nfunction getNodeShape(nodeType) {\n return specialShapes[nodeType] || 'rect';\n}\n\n// Create a map of node names to their \"EL<N>\" identifiers, disabled status, and shape\nconst nodeMap = {};\nlet nodeCounter = 1;\nnodes.forEach((node) => {\n if (!excludedNodeTypes.includes(node.type)) {\n const shape = getNodeShape(node.type);\n nodeMap[node.name] = {\n id: `EL${nodeCounter}`,\n disabled: node.disabled || false,\n shape: shape,\n brackets: shapes[shape] || shapes['rect'] // Default to rect if shape not found\n };\n nodeCounter++;\n }\n});\n\n// Function to convert special characters to HTML entities\nfunction convertToHTMLEntities(str) {\n return str.replaceAll('\"',\"'\").replace(/[^\\w\\s-]/g, function(char) {\n return '&#' + char.charCodeAt(0) + ';';\n });\n}\n\n// Function to format node text (with strike-through if disabled)\nfunction formatNodeText(nodeName, isDisabled) {\n const escapedName = convertToHTMLEntities(nodeName);\n return isDisabled ? `<s>${escapedName}</s>` : escapedName;\n}\n\n// Generate connections and isolated nodes\nconst connections = [];\nconst isolatedNodes = new Set(Object.keys(nodeMap));\n\nif (workflow.connections) {\n Object.entries(workflow.connections).forEach(([sourceName, targetConnections]) => {\n Object.entries(targetConnections).forEach(([connectionType, targets]) => {\n targets.forEach(targetArray => {\n targetArray.forEach(target => {\n const sourceNode = nodeMap[sourceName];\n const targetNode = nodeMap[target.node];\n if (sourceNode && targetNode) {\n let connectionLine = ` ${sourceNode.id}${sourceNode.brackets[0]}${formatNodeText(sourceName, sourceNode.disabled)}${sourceNode.brackets[1]}`;\n if (connectionType === 'main') {\n connectionLine += ` -->`;\n } else {\n connectionLine += ` -.- |${connectionType}|`;\n }\n connectionLine += ` ${targetNode.id}${targetNode.brackets[0]}${formatNodeText(target.node, targetNode.disabled)}${targetNode.brackets[1]}`;\n connections.push(connectionLine);\n isolatedNodes.delete(sourceName);\n isolatedNodes.delete(target.node);\n }\n });\n });\n });\n });\n}\n\n// Add isolated nodes to the connections array\nisolatedNodes.forEach(nodeName => {\n const node = nodeMap[nodeName];\n connections.push(` ${node.id}${node.brackets[0]}${formatNodeText(nodeName, node.disabled)}${node.brackets[1]}`);\n});\n\n// Generate the Mermaid flowchart string\nconst mermaidChart = `---\nconfig:\n look: neo\n theme: default\n---\nflowchart LR\n${connections.join('\\n')}`;\n\n// Output the result\nreturn {\n json: {\n mermaidChart: mermaidChart\n }\n};"
      },
      "typeVersion": 2
    },
    {
      "id": "77a35cd5-cb8f-4ac5-a699-dff5e65cda09",
      "name": "Merge2",
      "type": "n8n-nodes-base.merge",
      "position": [
        3840,
        1140
      ],
      "parameters": {
        "mode": "combine",
        "options": {},
        "combineBy": "combineByPosition"
      },
      "typeVersion": 3
    },
    {
      "id": "f8119590-e9d7-4513-9da4-fa911165baff",
      "name": "Generated Doc",
      "type": "n8n-nodes-base.set",
      "position": [
        4000,
        1240
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "7693348d-5129-4a07-809d-b0619b9fc44b",
              "name": "workflowdata",
              "type": "string",
              "value": "=# {{ $json.name }}\n\n{{ $json?.output?.workflow_description || \"## <SORRY, COULD NOT GENERATE WORKFLOW DESCRIPTION>\" }}\n\n## Workflow schematic\n\n```mermaid\n{{ $json.mermaidChart }}\n```\n\n{{ $json?.output?.nodes_settings || \"## <SORRY, COULD NOT GENERATE DOCS FOR NODE SETTING>\" }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "92565206-6cf2-4243-9143-4f6def4b524d",
      "name": "Passthrough",
      "type": "n8n-nodes-base.noOp",
      "position": [
        2100,
        1240
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "73081fc3-9554-4a12-b985-da02b356616f",
      "name": "Merge3",
      "type": "n8n-nodes-base.merge",
      "position": [
        3140,
        880
      ],
      "parameters": {
        "mode": "combine",
        "options": {},
        "combineBy": "combineByPosition"
      },
      "typeVersion": 3
    },
    {
      "id": "f50e72f8-9027-4ca7-9df7-700e828f48eb",
      "name": "Merge4",
      "type": "n8n-nodes-base.merge",
      "position": [
        960,
        -100
      ],
      "parameters": {
        "mode": "combine",
        "options": {},
        "combineBy": "combineByPosition"
      },
      "typeVersion": 3
    },
    {
      "id": "306820ac-7c87-45c2-b76f-55d772ac7300",
      "name": "Merge5",
      "type": "n8n-nodes-base.merge",
      "position": [
        960,
        240
      ],
      "parameters": {
        "mode": "combine",
        "options": {},
        "combineBy": "combineByPosition"
      },
      "typeVersion": 3
    },
    {
      "id": "96fd7265-7920-453f-8309-bdbd10880d03",
      "name": "Edit Fields",
      "type": "n8n-nodes-base.set",
      "position": [
        2100,
        1600
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "8bc55c5b-e09a-459b-bbb6-ed5f70d4f353",
              "name": "workflowdata",
              "type": "string",
              "value": "={{ $json.body.content }}"
            }
          ]
        },
        "includeOtherFields": true
      },
      "typeVersion": 3.4
    },
    {
      "id": "2fffb547-1c11-4663-aed5-29b9557e8738",
      "name": "Is Action Save?",
      "type": "n8n-nodes-base.if",
      "position": [
        4540,
        1600
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
              "id": "e3648023-8cb7-4b82-bd35-1ba196458327",
              "operator": {
                "name": "filter.operator.equals",
                "type": "string",
                "operation": "equals"
              },
              "leftValue": "={{ $json?.query?.action }}",
              "rightValue": "save"
            },
            {
              "id": "a44c9cc5-5717-4c34-978b-e644219a9cc1",
              "operator": {
                "type": "string",
                "operation": "exists",
                "singleValue": true
              },
              "leftValue": "={{ $json?.query?.action }}",
              "rightValue": ""
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "15825037-a8e2-4fbc-b529-2bf89810a116",
      "name": "Merge6",
      "type": "n8n-nodes-base.merge",
      "position": [
        4360,
        1700
      ],
      "parameters": {
        "mode": "chooseBranch",
        "useDataOfInput": 2
      },
      "typeVersion": 3
    },
    {
      "id": "b47f18a4-9b59-4278-890d-b6f6c596c554",
      "name": "Respond OK on Save",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        4920,
        1580
      ],
      "parameters": {
        "options": {
          "responseCode": 200
        },
        "respondWith": "noData"
      },
      "typeVersion": 1.1
    },
    {
      "id": "273dfd58-abef-49b7-8f12-5abc3d3515a6",
      "name": "single workflow",
      "type": "n8n-nodes-base.webhook",
      "position": [
        240,
        240
      ],
      "webhookId": "135bc21f-c7d0-4afe-be73-f984d444b43b",
      "parameters": {
        "path": "/:file",
        "options": {},
        "responseMode": "responseNode",
        "multipleMethods": true
      },
      "typeVersion": 2
    },
    {
      "id": "a7d7ee50-1420-475b-9028-0c80e1ae2241",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        140,
        -242.54375384615383
      ],
      "parameters": {
        "width": 296.5956923076922,
        "height": 277.9529846153844,
        "content": "## Main Docsify webhook\nIn response, n8n serves the main html page with the [Docsify JS library](https://docsify.js.org/)"
      },
      "typeVersion": 1
    },
    {
      "id": "b7c4b82a-9722-48ae-ab6a-4335981356ad",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -77.62340912473337,
        108.96056004923076
      ],
      "parameters": {
        "width": 509.1040245093486,
        "height": 287.9568584558579,
        "content": "## Single page requests\n* Docsify may request default pages (i.e. `readme.md` or a `summary.md`)\n* GET request for the workflow documentation pages\n* POST request for saving manually edited doc page"
      },
      "typeVersion": 1
    },
    {
      "id": "18e1f4c5-3652-4244-9a09-cd7a498a9310",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        460,
        -240.54580345183416
      ],
      "parameters": {
        "color": 3,
        "width": 489.50636350106504,
        "height": 462.9720128227216,
        "content": "## EDIT THIS!\n* `project_path` to link to a writable directory that is accessible to n8n\n* update `instance_url` when running in the cloud version. If using in self-hosted mode, make sure N8N_PROTOCOL and N8N_HOST .env variables are correct"
      },
      "typeVersion": 1
    },
    {
      "id": "d505d2ec-33e9-4983-8265-ff55f0df3da8",
      "name": "file types",
      "type": "n8n-nodes-base.switch",
      "position": [
        1180,
        240
      ],
      "parameters": {
        "rules": {
          "values": [
            {
              "outputKey": ".md",
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
                    "operator": {
                      "type": "string",
                      "operation": "endsWith"
                    },
                    "leftValue": "={{ $json.params.file.toLowerCase() }}",
                    "rightValue": ".md"
                  }
                ]
              },
              "renameOutput": true
            }
          ]
        },
        "options": {
          "fallbackOutput": "extra",
          "renameFallbackOutput": "unknown"
        }
      },
      "typeVersion": 3.2
    },
    {
      "id": "59362792-4a3e-4f97-95e2-d7b33b870e1d",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        4620,
        -245.7696645512633
      ],
      "parameters": {
        "width": 446.67466982248516,
        "height": 309.89805271694365,
        "content": "## Construct main HTML page and send it back to the user\n* `HTML_headers` and `HTML_docsify_include` are stored in the CONFIG node for the page simplicity"
      },
      "typeVersion": 1
    },
    {
      "id": "83189146-4d1f-454e-9591-bdbfda676683",
      "name": "Get All Workflows",
      "type": "n8n-nodes-base.n8n",
      "position": [
        1880,
        160
      ],
      "parameters": {
        "filters": {
          "tags": "={{ decodeURIComponent(($json.params.file?.match(/^tag-(.+)\\.md$/))?.[1] || '') }}"
        },
        "requestOptions": {}
      },
      "credentials": {
        "n8nApi": {
          "id": "eW7IdTFt4ARJbEwR",
          "name": "Ted n8n account"
        }
      },
      "typeVersion": 1,
      "alwaysOutputData": true
    },
    {
      "id": "39aa6017-a0ef-4f05-81b8-cfc9bb2fcc20",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1780,
        20.913927466176517
      ],
      "parameters": {
        "width": 820.1843305645202,
        "height": 307.51990359708003,
        "content": "## Serve main Markdown table with the workflow overview\n*NOTE! Here we don't reply with HTML content. Only Markdown elements are sent back and processed by the JS library*\n* Create an overall table when `README.md` (the home page) is requested\n* Create a table with a subset of workflows when a tag from a navigation pane is selected"
      },
      "typeVersion": 1
    },
    {
      "id": "2d087c25-b998-4abc-b0ce-ede8e62e28b4",
      "name": "md files",
      "type": "n8n-nodes-base.switch",
      "position": [
        1440,
        180
      ],
      "parameters": {
        "rules": {
          "values": [
            {
              "outputKey": "README.md",
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
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $json.params.file }}",
                    "rightValue": "README.md"
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "docs",
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
                    "id": "c1c1aecc-8faa-47ea-b831-4674c3c0db61",
                    "operator": {
                      "type": "string",
                      "operation": "contains"
                    },
                    "leftValue": "={{ $json.params.file }}",
                    "rightValue": "docs_"
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "summary.md",
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
                    "id": "fde643c9-31cd-4cbd-b4de-99a8ad6202af",
                    "operator": {
                      "name": "filter.operator.equals",
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $json.params.file }}",
                    "rightValue": "summary.md"
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "tags",
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
                    "id": "df4bc9f8-9285-49a6-b31c-d7173bf42901",
                    "operator": {
                      "type": "string",
                      "operation": "startsWith"
                    },
                    "leftValue": "={{ $json.params.file }}",
                    "rightValue": "tag-"
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
      "id": "08524df2-d555-42ca-8440-57ca5a780b74",
      "name": "Get Workflow tags",
      "type": "n8n-nodes-base.n8n",
      "position": [
        1880,
        500
      ],
      "parameters": {
        "filters": {},
        "requestOptions": {}
      },
      "credentials": {
        "n8nApi": {
          "id": "eW7IdTFt4ARJbEwR",
          "name": "Ted n8n account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "06e383dc-b1ea-4c97-9ee4-c07084ffc4cc",
      "name": "Sticky Note5",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1780,
        360
      ],
      "parameters": {
        "width": 817.6163848212657,
        "height": 288.20835077550953,
        "content": "## Serve left pane content\n* Here all workflows are fetched again when `summary.md` file is requested.\n\nIt contains Markdown for the left navigation pane: a list of all tags"
      },
      "typeVersion": 1
    },
    {
      "id": "c28ae282-7d83-42dd-8714-30d26b0f20af",
      "name": "Sticky Note6",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1700,
        1780
      ],
      "parameters": {
        "width": 367.8950651848079,
        "height": 262.5093167050718,
        "content": "## Handle missing pages\nServe the Markdown content with the requested file name for edge cases, i.e. any unexpected files"
      },
      "typeVersion": 1
    },
    {
      "id": "6441cf8f-dace-45fb-984e-aa9e0589e495",
      "name": "Sticky Note7",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1020,
        729
      ],
      "parameters": {
        "color": 6,
        "width": 4161.578473434268,
        "height": 1142.0268674813442,
        "content": "# Main functionality here\n\n## * View existing documentation\n## * Auto-generate doc page if no file available\n## * Re-created autodoc page\n## * Edit doc page: LIVE Markdown editor included!\n## * Save edited file. WARNING! No authentication"
      },
      "typeVersion": 1
    },
    {
      "id": "9116a4eb-18c6-4ec2-84e8-9a0b920d5c19",
      "name": "Sticky Note8",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        4460,
        751
      ],
      "parameters": {
        "width": 652.3100890494833,
        "height": 268.0620091282372,
        "content": "## Custom markdown editor\nThis is another HTML page for the live Markdown editor\n* `Mermaid.js` is supported\n* Docsify preview on edit\n* Save or Cancel buttons"
      },
      "typeVersion": 1
    },
    {
      "id": "920c1edb-29ad-4952-9e30-9020146ed88a",
      "name": "Sticky Note9",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        4000,
        1501
      ],
      "parameters": {
        "width": 522.870786668288,
        "height": 348.0868581511653,
        "content": "## Save new file\nOnce the doc page is generated or edited manually, a Markdown files is saved in the directory"
      },
      "typeVersion": 1
    },
    {
      "id": "cff4d2be-f627-4c7d-9f7a-093f6f9b2c27",
      "name": "Sticky Note10",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1887,
        758
      ],
      "parameters": {
        "width": 639.8696984316115,
        "height": 429.7891698152571,
        "content": "## Load existing doc file\nCheck the existing file when the View or Edit button is pressed\n"
      },
      "typeVersion": 1
    },
    {
      "id": "b7f01785-99c7-47b2-967a-b7456bb8f562",
      "name": "Sticky Note11",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2786.9421822644376,
        1023
      ],
      "parameters": {
        "width": 1369.2986733206085,
        "height": 466.42237140646773,
        "content": "## If the file is not available, then:\n* either auto-generate new doc\n* prepare a basic template for editing"
      },
      "typeVersion": 1
    },
    {
      "id": "6953bf0c-3122-4d80-9e74-1c07a892bf31",
      "name": "docsify",
      "type": "n8n-nodes-base.webhook",
      "position": [
        240,
        -100
      ],
      "webhookId": "8b719afe-8be3-4cd5-84ed-aca521b31a89",
      "parameters": {
        "path": "135bc21f-c7d0-4afe-be73-f984d444b43b",
        "options": {},
        "responseMode": "responseNode"
      },
      "typeVersion": 2
    }
  ],
  "active": true,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "eee9144a-c7a0-4947-874b-728d9e8618b7",
  "connections": {
    "Merge": {
      "main": [
        [
          {
            "node": "Is Action Edit?1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "mkdir": {
      "main": [
        [
          {
            "node": "Merge1",
            "type": "main",
            "index": 1
          }
        ]
      ]
    },
    "CONFIG": {
      "main": [
        [
          {
            "node": "Merge4",
            "type": "main",
            "index": 1
          },
          {
            "node": "Merge5",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Merge1": {
      "main": [
        [
          {
            "node": "HasFile?",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Merge2": {
      "main": [
        [
          {
            "node": "Generated Doc",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Merge3": {
      "main": [
        [
          {
            "node": "Is Action Edit?2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Merge4": {
      "main": [
        [
          {
            "node": "Main Page",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Merge5": {
      "main": [
        [
          {
            "node": "file types",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Merge6": {
      "main": [
        [
          {
            "node": "Is Action Save?",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "docsify": {
      "main": [
        [
          {
            "node": "CONFIG",
            "type": "main",
            "index": 0
          },
          {
            "node": "Merge4",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "HasFile?": {
      "main": [
        [
          {
            "node": "Extract from File",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Fetch Single Workflow1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "md files": {
      "main": [
        [
          {
            "node": "Get All Workflows",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "doc action",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Get Workflow tags",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Get All Workflows",
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
    "Edit Page": {
      "main": [
        [
          {
            "node": "Respond with HTML",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Empty Set": {
      "main": [
        [
          {
            "node": "Merge1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Main Page": {
      "main": [
        [
          {
            "node": "Respond with main page HTML",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "doc action": {
      "main": [
        [
          {
            "node": "mkdir",
            "type": "main",
            "index": 0
          },
          {
            "node": "Load Doc File",
            "type": "main",
            "index": 0
          },
          {
            "node": "Passthrough",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "mkdir",
            "type": "main",
            "index": 0
          },
          {
            "node": "Load Doc File",
            "type": "main",
            "index": 0
          },
          {
            "node": "Passthrough",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "mkdir",
            "type": "main",
            "index": 0
          },
          {
            "node": "Empty Set",
            "type": "main",
            "index": 0
          },
          {
            "node": "Passthrough",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Edit Fields",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "file types": {
      "main": [
        [
          {
            "node": "md files",
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
            "node": "Convert to File",
            "type": "main",
            "index": 0
          },
          {
            "node": "Merge6",
            "type": "main",
            "index": 1
          }
        ]
      ]
    },
    "Passthrough": {
      "main": [
        [
          {
            "node": "Merge3",
            "type": "main",
            "index": 1
          },
          {
            "node": "Merge",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Generated Doc": {
      "main": [
        [
          {
            "node": "Convert to File",
            "type": "main",
            "index": 0
          },
          {
            "node": "Is Action Edit?2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Load Doc File": {
      "main": [
        [
          {
            "node": "Merge1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Workflow Tags": {
      "main": [
        [
          {
            "node": "Respond with markdown",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Blank Doc File": {
      "main": [
        [
          {
            "node": "Is Action Edit?2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Sort-workflows": {
      "main": [
        [
          {
            "node": "Fill Workflow Table",
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
            "node": "Merge2",
            "type": "main",
            "index": 1
          }
        ]
      ]
    },
    "Convert to File": {
      "main": [
        [
          {
            "node": "Save New Doc File",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Is Action Save?": {
      "main": [
        [
          {
            "node": "Respond OK on Save",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "single workflow": {
      "main": [
        [
          {
            "node": "CONFIG",
            "type": "main",
            "index": 0
          },
          {
            "node": "Merge5",
            "type": "main",
            "index": 1
          }
        ],
        [
          {
            "node": "CONFIG",
            "type": "main",
            "index": 0
          },
          {
            "node": "Merge5",
            "type": "main",
            "index": 1
          }
        ]
      ]
    },
    "Is Action Edit?1": {
      "main": [
        [
          {
            "node": "Blank Doc File",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Basic LLM Chain",
            "type": "main",
            "index": 0
          },
          {
            "node": "Merge2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Is Action Edit?2": {
      "main": [
        [
          {
            "node": "Edit Page",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Workflow md content",
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
            "node": "Merge3",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get All Workflows": {
      "main": [
        [
          {
            "node": "Sort-workflows",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Workflow tags": {
      "main": [
        [
          {
            "node": "Workflow Tags",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Instance overview": {
      "main": [
        [
          {
            "node": "Respond with markdown",
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
            "node": "Basic LLM Chain",
            "type": "ai_languageModel",
            "index": 0
          },
          {
            "node": "Auto-fixing Output Parser",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Save New Doc File": {
      "main": [
        [
          {
            "node": "Merge6",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Fallback file name": {
      "main": [
        [
          {
            "node": "Respond with markdown",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Fill Workflow Table": {
      "main": [
        [
          {
            "node": "Instance overview",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Workflow md content": {
      "main": [
        [
          {
            "node": "Respond with markdown",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Fetch Single Workflow1": {
      "main": [
        [
          {
            "node": "Generate Mermaid Chart",
            "type": "main",
            "index": 0
          },
          {
            "node": "Merge",
            "type": "main",
            "index": 1
          }
        ]
      ]
    },
    "Generate Mermaid Chart": {
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
    "No Operation, do nothing": {
      "main": [
        [
          {
            "node": "Fallback file name",
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
    "Auto-fixing Output Parser": {
      "ai_outputParser": [
        [
          {
            "node": "Basic LLM Chain",
            "type": "ai_outputParser",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2123"></a>

## Template 2123 - Criar quadro, listas e mover cartão no Wekan

- **Nome:** Criar quadro, listas e mover cartão no Wekan
- **Descrição:** Fluxo manual que cria um quadro com duas listas, adiciona um cartão e imediatamente o move de uma lista para outra.
- **Funcionalidade:** • Disparo manual: Inicia o fluxo quando o usuário executa manualmente.
• Criação de quadro: Cria um quadro chamado "Documentation" com um proprietário definido.
• Criação de listas: Adiciona duas listas ao quadro, "To Do" e "Done".
• Criação de cartão: Cria um cartão intitulado "Document Wekan node" na lista "To Do", especificando autor e swimlane.
• Movimentação de cartão: Atualiza o cartão recém-criado para movê‑lo da lista "To Do" para a lista "Done".
- **Ferramentas:** • Wekan: Plataforma de quadro Kanban para gerenciar quadros, listas e cartões, utilizada aqui para criar o quadro, listas, cartão e para mover o cartão entre listas.



## Fluxo visual

```mermaid
flowchart LR
    N1["On clicking 'execute'"]
    N2["Wekan"]
    N3["Wekan1"]
    N4["Wekan2"]
    N5["Wekan3"]
    N6["Wekan4"]

    N2 --> N3
    N3 --> N4
    N4 --> N5
    N5 --> N6
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
        450,
        450
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Wekan",
      "type": "n8n-nodes-base.wekan",
      "position": [
        650,
        450
      ],
      "parameters": {
        "owner": "c4nzTEvSwGPBxKTCc",
        "title": "Documentation",
        "resource": "board",
        "additionalFields": {}
      },
      "credentials": {
        "wekanApi": "wekan-trial"
      },
      "typeVersion": 1
    },
    {
      "name": "Wekan1",
      "type": "n8n-nodes-base.wekan",
      "position": [
        850,
        450
      ],
      "parameters": {
        "title": "To Do",
        "boardId": "={{$node[\"Wekan\"].json[\"_id\"]}}",
        "resource": "list"
      },
      "credentials": {
        "wekanApi": "wekan-trial"
      },
      "typeVersion": 1
    },
    {
      "name": "Wekan2",
      "type": "n8n-nodes-base.wekan",
      "position": [
        1050,
        450
      ],
      "parameters": {
        "title": "Done",
        "boardId": "={{$node[\"Wekan\"].json[\"_id\"]}}",
        "resource": "list"
      },
      "credentials": {
        "wekanApi": "wekan-trial"
      },
      "typeVersion": 1
    },
    {
      "name": "Wekan3",
      "type": "n8n-nodes-base.wekan",
      "position": [
        1250,
        450
      ],
      "parameters": {
        "title": "Document Wekan node",
        "listId": "={{$node[\"Wekan1\"].json[\"_id\"]}}",
        "boardId": "={{$node[\"Wekan\"].json[\"_id\"]}}",
        "authorId": "c4nzTEvSwGPBxKTCc",
        "swimlaneId": "LDTcBp9fvmjSsSB69",
        "additionalFields": {}
      },
      "credentials": {
        "wekanApi": "wekan-trial"
      },
      "typeVersion": 1
    },
    {
      "name": "Wekan4",
      "type": "n8n-nodes-base.wekan",
      "position": [
        1450,
        450
      ],
      "parameters": {
        "cardId": "={{$node[\"Wekan3\"].json[\"_id\"]}}",
        "listId": "={{$node[\"Wekan1\"].json[\"_id\"]}}",
        "boardId": "={{$node[\"Wekan\"].json[\"_id\"]}}",
        "operation": "update",
        "updateFields": {
          "listId": "={{$node[\"Wekan2\"].json[\"_id\"]}}"
        }
      },
      "credentials": {
        "wekanApi": "wekan-trial"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "Wekan": {
      "main": [
        [
          {
            "node": "Wekan1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Wekan1": {
      "main": [
        [
          {
            "node": "Wekan2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Wekan2": {
      "main": [
        [
          {
            "node": "Wekan3",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Wekan3": {
      "main": [
        [
          {
            "node": "Wekan4",
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
            "node": "Wekan",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2125"></a>

## Template 2125 - Atualiza valores do portfólio de criptomoedas

- **Nome:** Atualiza valores do portfólio de criptomoedas
- **Descrição:** Atualiza periodicamente os preços atuais das criptomoedas do portfólio e registra o valor total do portfólio em uma tabela histórica.
- **Funcionalidade:** • Agendamento horário: executa o fluxo a cada hora para manter os preços atualizados.
• Leitura do portfólio: busca os registros do portfólio incluindo o campo Symbol para identificar as criptomoedas.
• Consulta de preço em tempo real: consulta a API de preços usando o identificador da moeda e solicita dados de market_data (preço em USD).
• Atualização dos registros: grava o preço atual no campo "Present Price" de cada registro do portfólio.
• Coleta de valores presentes: recupera o campo "Present Value" de todos os registros para cálculo consolidado.
• Cálculo do valor total do portfólio: soma os valores presentes de todos os registros para obter o total em USD.
• Registro do histórico: adiciona um novo registro na tabela de histórico com o valor total do portfólio.
- **Ferramentas:** • CoinGecko: serviço/API pública para obter dados de mercado e preços atuais de criptomoedas (current_price em USD).
• Airtable: base de dados online usada para armazenar o portfólio, atualizar preços e registrar o histórico do valor total do portfólio.



## Fluxo visual

```mermaid
flowchart LR
    N1["CoinGecko"]
    N2["Get Portfolio"]
    N3["Set"]
    N4["Run Top of Hour"]
    N5["Get Portfolio Values"]
    N6["Determine Total Value"]
    N7["Update Values"]
    N8["Append Portfolio Value"]

    N3 --> N7
    N1 --> N3
    N2 --> N1
    N7 --> N5
    N4 --> N2
    N5 --> N6
    N6 --> N8
```

## Fluxo (.json) :

```json
{
  "id": "14",
  "name": "Update Crypto Values",
  "nodes": [
    {
      "name": "CoinGecko",
      "type": "n8n-nodes-base.coinGecko",
      "position": [
        670,
        400
      ],
      "parameters": {
        "coinId": "={{$json[\"fields\"][\"Symbol\"]}}",
        "options": {
          "market_data": true,
          "localization": false
        },
        "operation": "get"
      },
      "typeVersion": 1
    },
    {
      "name": "Get Portfolio",
      "type": "n8n-nodes-base.airtable",
      "position": [
        450,
        400
      ],
      "parameters": {
        "table": "Portfolio",
        "operation": "list",
        "application": "appT7eX4iZcZVRIdq",
        "additionalOptions": {
          "fields": [
            "Symbol"
          ]
        }
      },
      "credentials": {
        "airtableApi": "Airtable"
      },
      "typeVersion": 1
    },
    {
      "name": "Set",
      "type": "n8n-nodes-base.set",
      "position": [
        870,
        400
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "Present Price",
              "value": "={{$json[\"market_data\"][\"current_price\"][\"usd\"]}}"
            },
            {
              "name": "Id",
              "value": "={{$node[\"Get Portfolio\"].json[\"id\"]}}"
            }
          ]
        },
        "options": {},
        "keepOnlySet": true
      },
      "typeVersion": 1
    },
    {
      "name": "Run Top of Hour",
      "type": "n8n-nodes-base.cron",
      "position": [
        240,
        400
      ],
      "parameters": {
        "triggerTimes": {
          "item": [
            {
              "mode": "everyHour"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Get Portfolio Values",
      "type": "n8n-nodes-base.airtable",
      "position": [
        1260,
        400
      ],
      "parameters": {
        "table": "Portfolio",
        "operation": "list",
        "application": "appT7eX4iZcZVRIdq",
        "additionalOptions": {
          "fields": [
            "Present Value"
          ]
        }
      },
      "credentials": {
        "airtableApi": "Airtable"
      },
      "typeVersion": 1
    },
    {
      "name": "Determine Total Value",
      "type": "n8n-nodes-base.function",
      "position": [
        1460,
        400
      ],
      "parameters": {
        "functionCode": "var totalValues = 0;\n\nitems.forEach(sumValues);\n\nfunction sumValues(value, index, array) {\n  totalValues = totalValues + value.json.fields['Present Value'];\n}\n\nitems = [{\"json\": {}}];\n\n\nitems[0].json['Portfolio Value (US$)'] = totalValues;\n\nreturn items;"
      },
      "typeVersion": 1
    },
    {
      "name": "Update Values",
      "type": "n8n-nodes-base.airtable",
      "position": [
        1070,
        400
      ],
      "parameters": {
        "id": "={{$node[\"SplitInBatches\"].json[\"id\"]}}",
        "table": "Portfolio",
        "fields": [
          "Present Price"
        ],
        "options": {},
        "operation": "update",
        "application": "appT7eX4iZcZVRIdq",
        "updateAllFields": false
      },
      "credentials": {
        "airtableApi": "Airtable"
      },
      "typeVersion": 1
    },
    {
      "name": "Append Portfolio Value",
      "type": "n8n-nodes-base.airtable",
      "position": [
        1660,
        400
      ],
      "parameters": {
        "table": "Portfolio Value",
        "fields": [
          "Portfolio Value (US$)"
        ],
        "options": {},
        "operation": "append",
        "application": "appT7eX4iZcZVRIdq",
        "addAllFields": false
      },
      "credentials": {
        "airtableApi": "Airtable"
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
            "node": "Update Values",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "CoinGecko": {
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
    "Get Portfolio": {
      "main": [
        [
          {
            "node": "CoinGecko",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Update Values": {
      "main": [
        [
          {
            "node": "Get Portfolio Values",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Run Top of Hour": {
      "main": [
        [
          {
            "node": "Get Portfolio",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Portfolio Values": {
      "main": [
        [
          {
            "node": "Determine Total Value",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Determine Total Value": {
      "main": [
        [
          {
            "node": "Append Portfolio Value",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2127"></a>

## Template 2127 - Extrair gastos de emails para planilha

- **Nome:** Extrair gastos de emails para planilha
- **Descrição:** Automatiza a leitura de emails de faturas e notificações de pagamento, extrai detalhes de cada gasto e registra os itens em uma planilha do Google.
- **Funcionalidade:** • Monitoramento de labels do Gmail: observa rótulos específicos e captura emails relevantes.
• Download e leitura de anexos: baixa anexos de emails e extrai seu conteúdo para análise.
• Extração de texto de PDFs com senha: converte PDFs protegidos em texto para processamento.
• Extração de conteúdo HTML e quebra de registros: identifica elementos HTML de gastos e divide entradas múltiplas em itens separados.
• Roteamento por remetente/tipo de email: classifica emails em múltiplos pagamentos, pagamento único ou faturas e encaminha para fluxos distintos.
• Normalização e preparação de dados: monta campos padronizados (data, serviço, detalhes, valor, categoria, moeda, cartão) e unifica metadados (assunto, data do email).
• Análise com modelos de linguagem: usa modelos de IA para interpretar o conteúdo e preencher um esquema de saída estruturado.
• Gravação em planilha: adiciona cada transação extraída a uma aba específica do Google Sheets para contabilidade.
- **Ferramentas:** • Gmail: provedor de email usado para receber notificações de faturas e gastos.
• Google Sheets: planilha onde os registros de gastos são armazenados.
• Google Gemini (PaLM): modelo de linguagem usado para interpretar o texto dos emails e extrair dados estruturados.
• Groq: modelo de linguagem alternativo utilizado para parsing e extração de informações.
• Extração de texto de PDFs com suporte a senha: biblioteca/serviço utilizado para converter PDFs protegidos em texto antes da análise.



## Fluxo visual

```mermaid
flowchart LR
    N1["Get invoice"]
    N2["Get payment"]
    N3["Extract invoice"]
    N4["Extract payment"]
    N5["HTML"]
    N6["Split Out"]
    N7["Structured Output Parser1"]
    N8["Google Gemini Chat Model1"]
    N9["Send"]
    N10["Set data 0"]
    N11["Set data 1"]
    N12["Set data 2"]
    N13["Invoice data"]
    N14["Payment data"]
    N15["Switch"]
    N16["Groq Chat Model"]
    N17["Structured Output Parser"]
    N18["Send1"]
    N19["Extract details1"]
    N20["Merge"]
    N21["Extract details"]
    N22["Sticky Note"]
    N23["Sticky Note1"]
    N24["Sticky Note2"]

    N5 --> N6
    N20 --> N21
    N15 --> N5
    N15 --> N11
    N15 --> N12
    N6 --> N10
    N10 --> N20
    N11 --> N20
    N12 --> N19
    N1 --> N3
    N2 --> N4
    N13 --> N15
    N14 --> N15
    N21 --> N9
    N3 --> N13
    N4 --> N14
    N19 --> N18
```

## Fluxo (.json) :

```json
{
  "id": "nkMjcOC4hpte1a0t",
  "meta": {
    "instanceId": "3986dc65ca3ddc4ee46e71fc194b0a9d4ef46d960a5e71624f9f7eaa198213cb",
    "templateCredsSetupCompleted": true
  },
  "name": "Extract spend details (template)",
  "tags": [
    {
      "id": "9mCuuNEpnYNvVzb8",
      "name": "Finance",
      "createdAt": "2024-09-15T07:22:30.749Z",
      "updatedAt": "2024-09-15T07:22:30.749Z"
    }
  ],
  "nodes": [
    {
      "id": "8e1e0861-9f06-4fe2-a9c1-423bab246959",
      "name": "Get invoice",
      "type": "n8n-nodes-base.gmailTrigger",
      "position": [
        600,
        380
      ],
      "parameters": {
        "simple": false,
        "filters": {
          "labelIds": [
            "Label_7885838942566773656"
          ]
        },
        "options": {
          "downloadAttachments": true
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
          "id": "fegneFqi8XJX3NJH",
          "name": "Gmail account (hana@hanamizuki.tw)"
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "364fe355-672a-4074-800a-a7496c4fb1b2",
      "name": "Get payment",
      "type": "n8n-nodes-base.gmailTrigger",
      "position": [
        600,
        580
      ],
      "parameters": {
        "simple": false,
        "filters": {
          "labelIds": [
            "Label_371722915607774622"
          ]
        },
        "options": {
          "downloadAttachments": true
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
          "id": "fegneFqi8XJX3NJH",
          "name": "Gmail account (hana@hanamizuki.tw)"
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "e3218faf-2486-46e0-bf43-3bc52927e2bd",
      "name": "Extract invoice",
      "type": "n8n-nodes-base.extractFromFile",
      "notes": "No attachements",
      "onError": "continueRegularOutput",
      "position": [
        820,
        380
      ],
      "parameters": {
        "options": {
          "password": "E223706995"
        },
        "operation": "pdf",
        "binaryPropertyName": "attachment_0"
      },
      "typeVersion": 1
    },
    {
      "id": "3772b3dc-7601-4005-9b61-263b2c1abd5f",
      "name": "Extract payment",
      "type": "n8n-nodes-base.extractFromFile",
      "notes": "No attachements",
      "onError": "continueRegularOutput",
      "position": [
        820,
        580
      ],
      "parameters": {
        "options": {
          "password": "E223706995"
        },
        "operation": "pdf",
        "binaryPropertyName": "attachment_0"
      },
      "typeVersion": 1
    },
    {
      "id": "10d57038-940e-47aa-84ea-3850f61ac757",
      "name": "HTML",
      "type": "n8n-nodes-base.html",
      "notes": "\".spend-table\" here is an example when the email use \"spend\" html tags to display each spends.\ne.g.\n<div class=spend-table>Spend 1</div>\n<div class=spend-table>Spend 2</div>",
      "position": [
        1440,
        200
      ],
      "parameters": {
        "options": {},
        "operation": "extractHtmlContent",
        "dataPropertyName": "=html",
        "extractionValues": {
          "values": [
            {
              "key": "spend",
              "cssSelector": ".spend-table",
              "returnArray": true
            }
          ]
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "dae6d22e-587d-4102-b006-20a341ede5ee",
      "name": "Split Out",
      "type": "n8n-nodes-base.splitOut",
      "position": [
        1660,
        200
      ],
      "parameters": {
        "options": {},
        "fieldToSplitOut": "spend"
      },
      "typeVersion": 1
    },
    {
      "id": "0d75443d-0d23-4120-95e5-b3128a760fb4",
      "name": "Structured Output Parser1",
      "type": "@n8n/n8n-nodes-langchain.outputParserStructured",
      "position": [
        2500,
        640
      ],
      "parameters": {
        "schemaType": "manual",
        "inputSchema": "{\n  \"title\": \"Expense Record Schema\",\n  \"description\": \"Schema used to parse expense record emails, including date, service name, transaction details, amount, category, currency, and card.\",\n  \"type\": \"object\",\n  \"properties\": {\n    \"date\": {\n      \"type\": \"string\",\n      \"description\": \"Transaction date, can refer to the email date or the consumption date within the content. If there are multiple dates, use the earliest one. The format is 'YYYY-MM-DD hh:mm', e.g., '2024-09-02 10:12'.\",\n      \"examples\": [\"2024-09-02 10:12\"]\n    },\n    \"service\": {\n      \"type\": [\"string\", \"null\"],\n      \"description\": \"Name of the service or store, such as 'GOOGLE', 'Uber', etc.\",\n      \"examples\": [\"GOOGLE\", \"Uber Eats\", \"Uber\", \"CLAUDE.AI\"]\n    },\n    \"details\": {\n      \"type\": [\"string\", \"null\"],\n      \"description\": \"Detailed transaction information, such as overseas card usage, online transactions, restaurant names, or consumption details. If none, can be left blank or null.\",\n      \"examples\": [\"Uber: from Fuxing North Road to Minquan East Road\", \"Restaurant name\", null]\n    },\n    \"amount\": {\n      \"type\": \"number\",\n      \"description\": \"Transaction amount. If in USD, keep two decimal places (e.g., 50.12); if in TWD, use integers (e.g., 550).\",\n      \"examples\": [50.12, 550]\n    },\n    \"category\": {\n      \"type\": \"string\",\n      \"description\": \"Transaction category\",\n      \"enum\": [\"Food & Beverage\", \"Transportation\", \"Daily Necessities\", \"Housing\", \"Electronics\", \"Beauty & Hair\", \"Apparel & Accessories\", \"Medical & Healthcare\", \"Pets\", \"Education\", \"Entertainment\", \"Cloud Services\", \"Automobile\", \"Gifts\", \"Family Care\", \"Counseling\", \"Insurance\", \"Taxes\", \"Transfer Fees\", \"Music\", \"Fitness\", \"Travel\", \"Lending\", \"Donations\", \"Advertising\", \"Finance\"],\n      \"examples\": [\"Food & Beverage\", \"Transportation\"]\n    },\n    \"currency\": {\n      \"type\": \"string\",\n      \"description\": \"Currency code used in the transaction. If the amount starts with NT$, then currency is TWD.\",\n      \"enum\": [\"TWD\", \"USD\", \"JPY\", \"EUR\", \"SGD\"],\n      \"examples\": [\"USD\", \"TWD\"]\n    },\n    \"card\": {\n      \"type\": [\"string\", \"null\"],\n      \"description\": \"Credit card used for the transaction.\",\n      \"enum\": [\"HSBC 3088\", \"HSBC 3854\", \"Fubon Card\", \"Crypto.com Card\", \"Cathay Card\", null],\n      \"examples\": [\"HSBC 3088\", \"HSBC 3854\"]\n    }\n  },\n  \"required\": [\"date\", \"amount\", \"category\", \"currency\"]\n}\n"
      },
      "typeVersion": 1.2
    },
    {
      "id": "7ade499c-015b-4903-8129-6c135264bf75",
      "name": "Google Gemini Chat Model1",
      "type": "@n8n/n8n-nodes-langchain.lmChatGoogleGemini",
      "position": [
        2320,
        640
      ],
      "parameters": {
        "options": {},
        "modelName": "models/gemini-1.5-flash"
      },
      "credentials": {
        "googlePalmApi": {
          "id": "QR3KfTwhKpbgAGWU",
          "name": "Google Gemini(PaLM) Api account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "10fe4a38-139b-4284-9e86-dd36e472f59e",
      "name": "Send",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        2740,
        480
      ],
      "parameters": {
        "columns": {
          "value": {
            "date": "={{ $json.output.date }}",
            "amount": "={{ $json.output.amount }}",
            "source": "n8n",
            "details": "={{ $json.output.details }}",
            "payment": "={{ $json.output.card }}",
            "service": "={{ $json.output.service }}",
            "category": "={{ $json.output.category }}",
            "currency": "={{ $json.output.currency }}"
          },
          "schema": [
            {
              "id": "date",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "date",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "service",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "service",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "details",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "details",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "amount",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "amount",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "category",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "category",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "currency",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "currency",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "payment",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "payment",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "source",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "source",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            }
          ],
          "mappingMode": "defineBelow",
          "matchingColumns": []
        },
        "options": {},
        "operation": "append",
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": 2071031170,
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1ccwhQeUSUkINccAucC6_clRyNF5Mw4IjIxAtcH4ftIs/edit#gid=2071031170",
          "cachedResultName": "raw data 2"
        },
        "documentId": {
          "__rl": true,
          "mode": "url",
          "value": "https://docs.google.com/spreadsheets/d/1ccwhQeUSUkINccAucC6_clRyNF5Mw4IjIxAtcH4ftIs/edit?gid=370005862#gid=370005862"
        }
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "flAcWUeyvdjh7MiW",
          "name": "Google Sheets account: hana@hanamizuki.tw (GCP: n8n)"
        }
      },
      "retryOnFail": true,
      "typeVersion": 4.5
    },
    {
      "id": "87ab4932-aae5-4c5a-a175-c782bebdf781",
      "name": "Set data 0",
      "type": "n8n-nodes-base.set",
      "position": [
        1860,
        200
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "75b16672-71cf-4157-bcb6-683099ff1620",
              "name": "email_date",
              "type": "string",
              "value": "={{ $('Switch').item.json.date }}"
            },
            {
              "id": "3298f680-5d17-42fd-8b41-a6ca621af37d",
              "name": "email_subject",
              "type": "string",
              "value": "={{ $('Switch').item.json.subject }}"
            },
            {
              "id": "cf7181b7-fef9-437a-8bbe-cd4a4eda85b8",
              "name": "email_content",
              "type": "string",
              "value": "={{ $ifEmpty($json.spend, $ifEmpty( $json.text, $json.html)) }}"
            },
            {
              "id": "1a524cb4-6975-4d45-ac0e-f1ac1f9b0417",
              "name": "email_type",
              "type": "number",
              "value": "=0"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "c2829f41-1e3f-40bc-8d4b-9fd1bac41381",
      "name": "Set data 1",
      "type": "n8n-nodes-base.set",
      "position": [
        1660,
        440
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "75b16672-71cf-4157-bcb6-683099ff1620",
              "name": "email_date",
              "type": "string",
              "value": "={{ $json.date }}"
            },
            {
              "id": "3298f680-5d17-42fd-8b41-a6ca621af37d",
              "name": "email_subject",
              "type": "string",
              "value": "={{ $json.subject }}"
            },
            {
              "id": "cf7181b7-fef9-437a-8bbe-cd4a4eda85b8",
              "name": "email_content",
              "type": "string",
              "value": "={{ $ifEmpty( $json.text, $json.html) }}"
            },
            {
              "id": "1a524cb4-6975-4d45-ac0e-f1ac1f9b0417",
              "name": "email_type",
              "type": "number",
              "value": "=1"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "ecf9ea3c-3f34-43ef-b101-ca4a420e4c24",
      "name": "Set data 2",
      "type": "n8n-nodes-base.set",
      "position": [
        1640,
        740
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "75b16672-71cf-4157-bcb6-683099ff1620",
              "name": "email_date",
              "type": "string",
              "value": "={{ $json.date }}"
            },
            {
              "id": "3298f680-5d17-42fd-8b41-a6ca621af37d",
              "name": "email_subject",
              "type": "string",
              "value": "={{ $json.subject }}"
            },
            {
              "id": "cf7181b7-fef9-437a-8bbe-cd4a4eda85b8",
              "name": "email_content",
              "type": "string",
              "value": "={{ $ifEmpty( $json.text, $json.html) }}"
            },
            {
              "id": "1a524cb4-6975-4d45-ac0e-f1ac1f9b0417",
              "name": "email_type",
              "type": "number",
              "value": "=2"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "0d9f8bde-af54-480c-bdc9-15cd5b0e6f28",
      "name": "Invoice data",
      "type": "n8n-nodes-base.set",
      "position": [
        1040,
        380
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "ac7c18ba-1944-4019-aa85-03d7751a7e1c",
              "name": "html",
              "type": "string",
              "value": "={{ $('Get invoice').item.json.html }}"
            },
            {
              "id": "5eb54501-9c55-437d-9918-e5eff92e2229",
              "name": "subject",
              "type": "string",
              "value": "={{ $('Get invoice').item.json.subject }}"
            },
            {
              "id": "87eebc48-0b95-46ae-b41b-b6540b1afaa9",
              "name": "date",
              "type": "string",
              "value": "={{ $('Get invoice').item.json.date }}"
            },
            {
              "id": "c6b75367-239e-4e88-9e17-90ee75a064e2",
              "name": "text",
              "type": "string",
              "value": "={{ $('Get invoice').item.json.text }} \\n {{ $json.text }}"
            },
            {
              "id": "7d5b4b42-6b90-4ffe-ab8f-4288771d1302",
              "name": "label",
              "type": "string",
              "value": "={{ $('Get invoice').item.json.labelIds }}"
            },
            {
              "id": "551ea1c3-01ca-4615-9d52-a880e24252ed",
              "name": "from",
              "type": "string",
              "value": "={{ $('Get invoice').item.json.from.text }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "c1c4c490-d7a9-4b16-a81b-a338103764b6",
      "name": "Payment data",
      "type": "n8n-nodes-base.set",
      "position": [
        1040,
        580
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "ac7c18ba-1944-4019-aa85-03d7751a7e1c",
              "name": "html",
              "type": "string",
              "value": "={{ $('Get payment').item.json.html }}"
            },
            {
              "id": "5eb54501-9c55-437d-9918-e5eff92e2229",
              "name": "subject",
              "type": "string",
              "value": "={{ $('Get payment').item.json.subject }}"
            },
            {
              "id": "87eebc48-0b95-46ae-b41b-b6540b1afaa9",
              "name": "date",
              "type": "string",
              "value": "={{ $('Get payment').item.json.date }}"
            },
            {
              "id": "c6b75367-239e-4e88-9e17-90ee75a064e2",
              "name": "text",
              "type": "string",
              "value": "={{ $('Get payment').item.json.text }} \\n {{ $json.text }}"
            },
            {
              "id": "7d5b4b42-6b90-4ffe-ab8f-4288771d1302",
              "name": "label",
              "type": "string",
              "value": "={{ $('Get payment').item.json.labelIds }}"
            },
            {
              "id": "2c976be1-48b8-42fa-b1c9-2fd315da89ae",
              "name": "from",
              "type": "string",
              "value": "={{ $('Get payment').item.json.from.text }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "01c5a934-9412-4ef9-81a8-c4aef19c8868",
      "name": "Switch",
      "type": "n8n-nodes-base.switch",
      "position": [
        1300,
        480
      ],
      "parameters": {
        "rules": {
          "values": [
            {
              "outputKey": "Multiple payment info in one mail",
              "conditions": {
                "options": {
                  "version": 1,
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
                    "leftValue": "={{ $json.from }}",
                    "rightValue": "service@pxbillrc01.cathaybk.com.tw"
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "One payment info in one mail",
              "conditions": {
                "options": {
                  "version": 1,
                  "leftValue": "",
                  "caseSensitive": true,
                  "typeValidation": "strict"
                },
                "combinator": "and",
                "conditions": [
                  {
                    "id": "47e3b84f-903c-4594-9297-785cfbea0316",
                    "operator": {
                      "type": "string",
                      "operation": "regex"
                    },
                    "leftValue": "={{ $json.from }}",
                    "rightValue": "\\b(?:noreply@messaging\\.hsbc\\.com\\.tw|hello@crypto\\.com|taipeifubon\\.com\\.tw)\\b"
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "Invoices",
              "conditions": {
                "options": {
                  "version": 1,
                  "leftValue": "",
                  "caseSensitive": true,
                  "typeValidation": "strict"
                },
                "combinator": "and",
                "conditions": [
                  {
                    "id": "db9d40f1-8fa4-4908-9010-985072b3f319",
                    "operator": {
                      "type": "string",
                      "operation": "notRegex"
                    },
                    "leftValue": "={{ $json.from }}",
                    "rightValue": "\\b(?:noreply@messaging\\.hsbc\\.com\\.tw|hello@crypto\\.com|taipeifubon\\.com\\.tw)\\b"
                  }
                ]
              },
              "renameOutput": true
            }
          ]
        },
        "options": {}
      },
      "executeOnce": false,
      "typeVersion": 3.1,
      "alwaysOutputData": false
    },
    {
      "id": "250bbd9a-3d22-4a04-910c-7cec437b3c33",
      "name": "Groq Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatGroq",
      "position": [
        2320,
        1120
      ],
      "parameters": {
        "model": "llama-3.2-11b-text-preview",
        "options": {}
      },
      "credentials": {
        "groqApi": {
          "id": "vaG2nZFaKeQarQHw",
          "name": "Groq account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "b8d2b2fc-748c-43c5-a82b-d5e7357bbef8",
      "name": "Structured Output Parser",
      "type": "@n8n/n8n-nodes-langchain.outputParserStructured",
      "position": [
        2520,
        1120
      ],
      "parameters": {
        "schemaType": "manual",
        "inputSchema": "{\n  \"title\": \"Transaction Record Schema\",\n  \"description\": \"Schema for parsing transaction record emails, including date, service name, transaction details, amount, category, currency, and card.\",\n  \"type\": \"object\",\n  \"properties\": {\n    \"date\": {\n      \"type\": \"string\",\n      \"description\": \"Transaction date, can refer to email date or transaction date in content. If multiple dates exist, use the earliest date. Format is 'YYYY-MM-DD hh:mm', e.g., '2024-09-02 10:12'.\",\n      \"examples\": [\"2024-09-02 10:12\"]\n    },\n    \"service\": {\n      \"type\": [\"string\", \"null\"],\n      \"description\": \"Name of service or store, e.g., 'GOOGLE', 'Uber', etc.\",\n      \"examples\": [\"GOOGLE\", \"Uber Eats\", \"Uber\", \"CLAUDE.AI\"]\n    },\n    \"details\": {\n      \"type\": [\"string\", \"null\"],\n      \"description\": \"Detailed transaction information, such as overseas purchase, online purchase, restaurant name, or consumption details. Can be empty or null if not available.\",\n      \"examples\": [\"Uber: From Fuxing North Road to Minquan East Road\", \"Restaurant name\", null]\n    },\n    \"amount\": {\n      \"type\": \"number\",\n      \"description\": \"Transaction amount. For USD, keep two decimal places (e.g., 50.12); for TWD, use integers (e.g., 550).\",\n      \"examples\": [50.12, 550]\n    },\n    \"category\": {\n      \"type\": \"string\",\n      \"description\": \"Transaction category\",\n      \"enum\": [\"Food & Beverage\", \"Transportation\", \"Daily Necessities\", \"Housing\", \"Electronics\", \"Beauty & Hair\", \"Clothing & Accessories\", \"Healthcare\", \"Pets\", \"Education\", \"Entertainment\", \"Cloud Services\", \"Automotive\", \"Gifts\", \"Family Support\", \"Counseling\", \"Insurance\", \"Taxes\", \"Transfer Fee\", \"Music\", \"Fitness\", \"Travel\", \"Lending\", \"Donations\", \"Advertising\", \"Finance\"],\n      \"examples\": [\"Food & Beverage\", \"Transportation\"]\n    },\n    \"currency\": {\n      \"type\": \"string\",\n      \"description\": \"Currency code used for the transaction, if amount starts with NT$, currency is TWD.\",\n      \"enum\": [\"TWD\", \"USD\", \"JPY\", \"EUR\", \"SGD\"],\n      \"examples\": [\"USD\", \"TWD\"]\n    }\n  },\n  \"required\": [\"date\", \"amount\", \"category\", \"currency\"]\n}"
      },
      "typeVersion": 1.2
    },
    {
      "id": "39b10715-54fe-4c07-9ca1-afbe43ae519e",
      "name": "Send1",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        2740,
        900
      ],
      "parameters": {
        "columns": {
          "value": {
            "date": "={{ $json.output.date }}",
            "amount": "={{ $json.output.amount }}",
            "source": "n8n",
            "details": "={{ $json.output.details }}",
            "payment": "=",
            "service": "={{ $json.output.service }}",
            "category": "={{ $json.output.category }}",
            "currency": "={{ $json.output.currency }}"
          },
          "schema": [
            {
              "id": "date",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "date",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "service",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "service",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "details",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "details",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "amount",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "amount",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "category",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "category",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "currency",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "currency",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "payment",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "payment",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "source",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "source",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            }
          ],
          "mappingMode": "defineBelow",
          "matchingColumns": []
        },
        "options": {},
        "operation": "append",
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": 2071031170,
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1ccwhQeUSUkINccAucC6_clRyNF5Mw4IjIxAtcH4ftIs/edit#gid=2071031170",
          "cachedResultName": "raw data 2"
        },
        "documentId": {
          "__rl": true,
          "mode": "url",
          "value": "https://docs.google.com/spreadsheets/d/1ccwhQeUSUkINccAucC6_clRyNF5Mw4IjIxAtcH4ftIs/edit?gid=370005862#gid=370005862"
        }
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "flAcWUeyvdjh7MiW",
          "name": "Google Sheets account: hana@hanamizuki.tw (GCP: n8n)"
        }
      },
      "retryOnFail": true,
      "typeVersion": 4.5
    },
    {
      "id": "112f5198-871e-42f9-9376-5fa074497413",
      "name": "Extract details1",
      "type": "@n8n/n8n-nodes-langchain.chainLlm",
      "position": [
        2320,
        900
      ],
      "parameters": {
        "text": "=Email Date: {{ $json.email_date }}\nEmail Subject: {{ $json.email_subject }}\nEmail Content:\n{{ $json.email_content }}",
        "messages": {
          "messageValues": [
            {
              "message": "=Please analyze the following email to extract transaction details for bookkeeping purposes.\n\nPlease extract relevant transaction details such as transaction date, amount, merchant name, and any other pertinent information, and provide them in a structured format suitable for accounting records."
            }
          ]
        },
        "promptType": "define",
        "hasOutputParser": true
      },
      "retryOnFail": true,
      "typeVersion": 1.4
    },
    {
      "id": "b9c3cb29-e68e-4ae0-8930-185c17bc6cab",
      "name": "Merge",
      "type": "n8n-nodes-base.merge",
      "position": [
        2060,
        440
      ],
      "parameters": {},
      "typeVersion": 3
    },
    {
      "id": "b50d632c-b762-4f61-b34a-91f941100668",
      "name": "Extract details",
      "type": "@n8n/n8n-nodes-langchain.chainLlm",
      "position": [
        2320,
        480
      ],
      "parameters": {
        "text": "=Email Date: {{ $json.email_date }}\nEmail Subject: {{ $json.email_subject }}\nEmail Content:\n{{ $json.email_content }}\nEmail Source: {{ $json.email_type }}",
        "messages": {
          "messageValues": [
            {
              "message": "=Please analyze the following email to extract transaction details for bookkeeping purposes. The \"Email Source\" field indicates the origin of the email, where 0 represents Cathay Bank card statements and 1 represents other credit card statements.\n\nPlease extract relevant transaction details such as transaction date, amount, merchant name, and any other pertinent information, and provide them in a structured format suitable for accounting records."
            }
          ]
        },
        "promptType": "define",
        "hasOutputParser": true
      },
      "retryOnFail": true,
      "typeVersion": 1.4
    },
    {
      "id": "7a7e2e36-a8b6-48dc-ad57-2f5eea691285",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        500,
        220
      ],
      "parameters": {
        "width": 720,
        "height": 560,
        "content": "# A. Get data\n- Set up labels in Gmail\n- Suggested using Gmail filters to move emails to labels automatically"
      },
      "typeVersion": 1
    },
    {
      "id": "108becad-1a7b-4409-9cb3-36a1c7b64786",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1280,
        -20
      ],
      "parameters": {
        "width": 920,
        "height": 960,
        "content": "# B. Deal with the data\n1. Multiple payment info in one mail: input the \"sender\" of the emails that contain more than one payment info. e.g. credit card daily spend notification\n2. One payment info in one mail: input the \"sender\" of the emails that contain only one payment info. e.g. instant credit card spend notification\n3. Invoices: input the mails that contain one invoice in one mail"
      },
      "typeVersion": 1
    },
    {
      "id": "7123f576-87f9-4df1-ae24-f3e5289c7234",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2240,
        320
      ],
      "parameters": {
        "width": 840,
        "height": 980,
        "content": "# C. Get spend details and send to google sheet\n- Edit the output schema to fit your google sheet format\n- Edit the prompt to fit your needs"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "211d9ccc-7a66-41c8-bda1-eacde400eeff",
  "connections": {
    "HTML": {
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
    "Merge": {
      "main": [
        [
          {
            "node": "Extract details",
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
            "node": "HTML",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Set data 1",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Set data 2",
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
            "node": "Set data 0",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set data 0": {
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
    "Set data 1": {
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
    "Set data 2": {
      "main": [
        [
          {
            "node": "Extract details1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get invoice": {
      "main": [
        [
          {
            "node": "Extract invoice",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get payment": {
      "main": [
        [
          {
            "node": "Extract payment",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Invoice data": {
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
    "Payment data": {
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
    "Extract details": {
      "main": [
        [
          {
            "node": "Send",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract invoice": {
      "main": [
        [
          {
            "node": "Invoice data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract payment": {
      "main": [
        [
          {
            "node": "Payment data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Groq Chat Model": {
      "ai_languageModel": [
        [
          {
            "node": "Extract details1",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Extract details1": {
      "main": [
        [
          {
            "node": "Send1",
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
            "node": "Extract details1",
            "type": "ai_outputParser",
            "index": 0
          }
        ]
      ]
    },
    "Google Gemini Chat Model1": {
      "ai_languageModel": [
        [
          {
            "node": "Extract details",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Structured Output Parser1": {
      "ai_outputParser": [
        [
          {
            "node": "Extract details",
            "type": "ai_outputParser",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2129"></a>

## Template 2129 - Leitura de dois feeds RSS

- **Nome:** Leitura de dois feeds RSS
- **Descrição:** Lê itens de dois feeds RSS diferentes fornecidos dinamicamente e processa cada feed individualmente.
- **Funcionalidade:** • Início manual: permite executar o fluxo sob demanda.
• Geração dinâmica de URLs: cria programaticamente uma lista de URLs de feeds a serem lidos.
• Processamento em lotes: percorre cada URL de forma sequencial para evitar sobrecarga.
• Leitura de feeds RSS: solicita e recupera itens dos feeds especificados.
• Suporte a múltiplas fontes: permite adicionar ou remover feeds facilmente alterando a lista de URLs.
- **Ferramentas:** • RSS: protocolo usado para recuperar itens e atualizações de blogs e publicações.
• Medium: fonte de conteúdo via feed RSS (publicações hospedadas no Medium).
• Dev.to: fonte de conteúdo via feed RSS (publicações hospedadas no Dev.to).



## Fluxo visual

```mermaid
flowchart LR
    N1["RSS Feed Read"]
    N2["When clicking 'Execute Workflow'"]
    N3["Code"]
    N4["Loop Over Items"]

    N3 --> N4
    N1 --> N4
    N4 --> N1
    N2 --> N3
```

## Fluxo (.json) :

```json
{
  "id": "7604ck94MeYXMHpN",
  "meta": {
    "instanceId": "bd0e051174def82b88b5cd547222662900558d74b239c4048ea0f6b7ed61c642"
  },
  "name": "Read RSS feed from two different sources",
  "tags": [],
  "nodes": [
    {
      "id": "fa8717e5-092a-4359-89cc-57cc8fa2bf25",
      "name": "RSS Feed Read",
      "type": "n8n-nodes-base.rssFeedRead",
      "position": [
        1080,
        180
      ],
      "parameters": {
        "url": "={{ $json.url }}",
        "options": {}
      },
      "typeVersion": 1
    },
    {
      "id": "62ce6cf3-fb83-4013-b288-40d179f35f99",
      "name": "When clicking \"Execute Workflow\"",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        520,
        100
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "81496a04-b986-4e13-b884-23562f953a37",
      "name": "Code",
      "type": "n8n-nodes-base.code",
      "position": [
        700,
        100
      ],
      "parameters": {
        "jsCode": "return [\n  {\n    json: {\n      url: 'https://medium.com/feed/n8n-io',\n    }\n  },\n  {\n    json: {\n      url: 'https://dev.to/feed/n8n',\n    }\n  }\n];"
      },
      "typeVersion": 1
    },
    {
      "id": "6e3a444f-fec3-4a7f-a063-d5b152c5f43a",
      "name": "Loop Over Items",
      "type": "n8n-nodes-base.splitInBatches",
      "position": [
        880,
        100
      ],
      "parameters": {
        "options": {}
      },
      "typeVersion": 3
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "8ad423d4-cf25-4b30-85c0-c50a26238e81",
  "connections": {
    "Code": {
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
    "RSS Feed Read": {
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
            "node": "RSS Feed Read",
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

<a id="template-2130"></a>

## Template 2130 - Leitura de e-mails via IMAP

- **Nome:** Leitura de e-mails via IMAP
- **Descrição:** Conecta-se a uma conta de e-mail via IMAP e realiza a leitura de mensagens na caixa configurada.
- **Funcionalidade:** • Leitura de mensagens IMAP: Recupera e lê e-mails da conta configurada quando o fluxo é executado.
• Autenticação com credenciais IMAP: Utiliza credenciais armazenadas para acessar a caixa de correio.
• Validação de certificado TLS: A opção de permitir certificados não autorizados está desativada, garantindo verificação do certificado do servidor.
- **Ferramentas:** • Servidor de e-mail IMAP: Servidor que disponibiliza as mensagens e permite acesso via protocolo IMAP.
• Sistema de credenciais IMAP: Armazenamento das credenciais necessárias para autenticar e acessar a conta de e-mail.



## Fluxo visual

```mermaid
flowchart LR
    N1["IMAP Email"]
```

## Fluxo (.json) :

```json
{
  "nodes": [
    {
      "name": "IMAP Email",
      "type": "n8n-nodes-base.emailReadImap",
      "position": [
        760,
        400
      ],
      "parameters": {
        "options": {
          "allowUnauthorizedCerts": false
        }
      },
      "credentials": {
        "imap": "imap_creds"
      },
      "typeVersion": 1
    }
  ],
  "connections": {}
}
```

<a id="template-2133"></a>

## Template 2133 - Captura e análise de palavras-chave

- **Nome:** Captura e análise de palavras-chave
- **Descrição:** Fluxo que coleta palavras-chave base, gera termos secundários via autocomplete para Google e YouTube, consulta volumes de busca e atualiza registros em banco de dados para análise de tráfego mensal.
- **Funcionalidade:** • Geração de período: Calcula datas (ex.: ontem) para limitar buscas por intervalo.
• Leitura de palavras-base: Recupera a lista inicial de keywords de uma tabela externa.
• Expansão de keywords via autocomplete: Gera palavras-chave de segunda ordem usando serviços de autocomplete para Google e YouTube.
• Combinação e limpeza: Junta resultados, remove duplicatas, limita comprimento e formata termos para consulta.
• Consulta de volume de busca: Envia batches para API de search volume (Google e YouTube) e recebe métricas como monthly_searches e cpc.
• Filtragem de resultados: Filtra termos com métricas válidas (por exemplo, existência de monthly_searches e cpc) antes de processar.
• Criação/atualização de registros: Insere novos termos secundários ou atualiza existentes no banco de dados.
• Formatação e importação em lote: Converte séries mensais em lotes e faz importação em massa para a tabela de volumes.
• Agendamento e execução manual: Permite execução periódica via cron e disparo manual para testes.
- **Ferramentas:** • NocoDB: Banco de dados utilizado para armazenar keywords base, keywords secundárias e tabelas de volumes mensais.
• DataForSEO: Serviço/API para obter dados de volume de busca e métricas (search volume, CPC) para keywords.
• Social Flood (instância local de autocomplete): Serviço de autocomplete (via API local/docker) usado para gerar sugestões de palavras-chave para Google e YouTube.



## Fluxo visual

```mermaid
flowchart LR
    N1["When clicking ‘Test workflow’"]
    N2["Schedule Trigger"]
    N3["Gen Time"]
    N4["Sticky Note"]
    N5["Sticky Note1"]
    N6["Sticky Note2"]
    N7["NocoDB"]
    N8["Second Order Google Autocomplete Keywords"]
    N9["Google Search Volume"]
    N10["Sticky Note3"]
    N11["Split Out Google Search"]
    N12["YouTube Search Volume"]
    N13["Second Order YouTube Autocomplete Keywords"]
    N14["Split Out YT Search"]
    N15["Google Filter"]
    N16["YT Filter"]
    N17["Add Second Tier YT Keyword Data"]
    N18["Add Second Tier G Keyword Data"]
    N19["Format G Data"]
    N20["Format YT Data"]
    N21["Bulk Import G Monthly Search Volume"]
    N22["Bulk Import YT Monthly Search Volume"]
    N23["Sticky Note4"]
    N24["Is Google Keyword Available"]
    N25["Is YT Keyword Avaliable"]
    N26["Sticky Note5"]
    N27["Check for Google Keyword"]
    N28["Check for YT Keyword"]
    N29["Loop Over YT Keywords"]
    N30["Update Second Tier G Keyword Data"]
    N31["Update Second Tier YT Keyword Data"]
    N32["Loop Over Google Keywords"]
    N33["Sticky Note6"]
    N34["Combine G Keywords and Filter"]
    N35["Combine YT Keywords and Filter"]

    N7 --> N13
    N7 --> N8
    N3 --> N7
    N16 --> N29
    N19 --> N21
    N15 --> N32
    N20 --> N22
    N2 --> N3
    N14 --> N16
    N28 --> N25
    N9 --> N11
    N29 --> N28
    N12 --> N14
    N25 --> N17
    N25 --> N31
    N11 --> N15
    N27 --> N24
    N32 --> N27
    N24 --> N18
    N24 --> N30
    N34 --> N9
    N18 --> N19
    N35 --> N12
    N17 --> N20
    N30 --> N32
    N1 --> N3
    N31 --> N29
    N21 --> N32
    N22 --> N29
    N8 --> N34
    N13 --> N35
```

## Fluxo (.json) :

```json
{
  "id": "SHgOqN3ednIo5gNu",
  "meta": {
    "instanceId": "5fdeff34cb31eeba72e9ea7f1100a8cb9dfce8edcd1fd736c5a33060890e9b77",
    "templateCredsSetupCompleted": true
  },
  "name": "Find Top Keywords",
  "tags": [],
  "nodes": [
    {
      "id": "386c7972-34c2-4f51-9329-dee7f6a7511b",
      "name": "When clicking ‘Test workflow’",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        -3440,
        760
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "3ebf40fd-acfd-4424-99c9-95ddaac74de3",
      "name": "Schedule Trigger",
      "type": "n8n-nodes-base.scheduleTrigger",
      "position": [
        -3440,
        1040
      ],
      "parameters": {
        "rule": {
          "interval": [
            {
              "field": "cronExpression",
              "expression": "0 */4 * * *"
            }
          ]
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "a24af92b-849d-48ee-aedd-6c7e75d9c902",
      "name": "Gen Time",
      "type": "n8n-nodes-base.code",
      "position": [
        -3160,
        940
      ],
      "parameters": {
        "jsCode": "// Get today's date\nconst today = new Date();\n\n// Subtract one day to get the previous day\nconst yesterday = new Date(today);\nyesterday.setDate(today.getDate() - 1);\n\n// Format the date as yyyy-mm-dd\nconst year = yesterday.getFullYear();\nconst month = String(yesterday.getMonth() + 1).padStart(2, '0'); // Month is zero-indexed\nconst day = String(yesterday.getDate()).padStart(2, '0');\n\nconst formattedDate = `${year}-${month}-${day}`;\n\n// Set the formatted date to be used in a later node\nreturn [{ json: { previousDay: formattedDate } }];"
      },
      "typeVersion": 2
    },
    {
      "id": "f0807e09-1f8f-45ba-a6d3-d14ee3f96a9f",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -3540,
        600
      ],
      "parameters": {
        "width": 520,
        "height": 780,
        "content": "## Create time for yesterday and today. This will be used to gather and search for news articles within a specific range."
      },
      "typeVersion": 1
    },
    {
      "id": "c97b391b-1da1-4c62-9394-e83a49dae788",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -3020,
        600
      ],
      "parameters": {
        "color": 4,
        "width": 280,
        "height": 780,
        "content": "## Grab a list of base keywords from NocoDB"
      },
      "typeVersion": 1
    },
    {
      "id": "21e89f1c-7101-490a-89aa-a5a52e10d88a",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -2740,
        600
      ],
      "parameters": {
        "width": 380,
        "height": 780,
        "content": "## Generate YouTube and Google Keywords from base keywords"
      },
      "typeVersion": 1
    },
    {
      "id": "3b6e8b0e-dfdc-41d0-a387-00872c92faa1",
      "name": "NocoDB",
      "type": "n8n-nodes-base.nocoDb",
      "position": [
        -2940,
        940
      ],
      "parameters": {
        "table": "mztryza8davdl48",
        "options": {
          "fields": [
            "keyword"
          ]
        },
        "operation": "getAll",
        "projectId": "pbwiwe87uf1cpgc",
        "returnAll": true,
        "authentication": "nocoDbApiToken"
      },
      "credentials": {
        "nocoDbApiToken": {
          "id": "LAbGsn1RMARiq5Gy",
          "name": "NocoDB Token account"
        }
      },
      "typeVersion": 3
    },
    {
      "id": "fef9283e-886a-486b-a51f-0f459f4b18e0",
      "name": "Second Order Google Autocomplete Keywords",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        -2620,
        800
      ],
      "parameters": {
        "url": "http://192.168.1.110:8000/google-search/autocomplete-keywords",
        "options": {},
        "sendQuery": true,
        "sendHeaders": true,
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "queryParameters": {
          "parameters": [
            {
              "name": "input_keyword",
              "value": "={{ $('NocoDB').item.json.keyword }}"
            },
            {
              "name": "input_country",
              "value": "US"
            },
            {
              "name": "use_proxy",
              "value": "true"
            },
            {
              "name": "output",
              "value": "toolbar"
            },
            {
              "name": "spell",
              "value": "1"
            },
            {
              "name": "hl",
              "value": "en"
            }
          ]
        },
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
          "id": "eNOOug9ODsbtfjBk",
          "name": "Social Flood API Key Local"
        }
      },
      "executeOnce": false,
      "typeVersion": 4.2
    },
    {
      "id": "fad88d1e-a14e-4cc1-9ac1-dcc6126355c4",
      "name": "Google Search Volume",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        -2020,
        800
      ],
      "parameters": {
        "url": "https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live",
        "method": "POST",
        "options": {},
        "jsonBody": "=[\n    {\n        \"location_code\": 2840,\n        \"language_code\": \"en\",\n        \"keywords\": [{{ $json.keywords }}],\n        \"date_from\": \"2021-08-01\",\n        \"search_partners\": false \n    }\n]",
        "sendBody": true,
        "specifyBody": "json",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpBasicAuth"
      },
      "credentials": {
        "httpBasicAuth": {
          "id": "7k7huetjBCcDO7uR",
          "name": "Data for SEO Basic Auth"
        }
      },
      "executeOnce": false,
      "typeVersion": 4.2
    },
    {
      "id": "dac54baa-6166-4fb6-a705-a45a91b993ed",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -2360,
        600
      ],
      "parameters": {
        "color": 4,
        "width": 500,
        "height": 780,
        "content": "## Query YouTube and Google Keyword search volume."
      },
      "typeVersion": 1
    },
    {
      "id": "753401aa-c78e-4dd1-b47f-b774bed8a6ce",
      "name": "Split Out Google Search",
      "type": "n8n-nodes-base.splitOut",
      "position": [
        -1740,
        800
      ],
      "parameters": {
        "options": {},
        "fieldToSplitOut": "tasks[0].result"
      },
      "executeOnce": false,
      "typeVersion": 1
    },
    {
      "id": "12f53197-a03e-4862-a6cf-d4feffd49b29",
      "name": "YouTube Search Volume",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        -2020,
        1120
      ],
      "parameters": {
        "url": "https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live",
        "method": "POST",
        "options": {},
        "jsonBody": "=[\n    {\n        \"location_code\": 2840,\n        \"language_code\": \"en\",\n        \"keywords\": [{{ $json.keywords }}],\n        \"date_from\": \"2021-08-01\",\n        \"search_partners\": true,\n        \"sort_by\": \"search_volume\"\n    }\n]",
        "sendBody": true,
        "specifyBody": "json",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpBasicAuth"
      },
      "credentials": {
        "httpBasicAuth": {
          "id": "7k7huetjBCcDO7uR",
          "name": "Data for SEO Basic Auth"
        }
      },
      "executeOnce": false,
      "typeVersion": 4.2
    },
    {
      "id": "d0173c03-c803-4c64-9c87-48a47952085f",
      "name": "Second Order YouTube Autocomplete Keywords",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        -2620,
        1120
      ],
      "parameters": {
        "url": "http://192.168.1.110:8000/google-search/autocomplete-keywords",
        "options": {
          "redirect": {
            "redirect": {}
          }
        },
        "sendQuery": true,
        "sendHeaders": true,
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "queryParameters": {
          "parameters": [
            {
              "name": "input_keyword",
              "value": "={{ $json.keyword }}"
            },
            {
              "name": "input_country",
              "value": "US"
            },
            {
              "name": "use_proxy",
              "value": "true"
            },
            {
              "name": "output",
              "value": "toolbar"
            },
            {
              "name": "spell",
              "value": "1"
            },
            {
              "name": "hl",
              "value": "en"
            },
            {
              "name": "ds",
              "value": "yt"
            }
          ]
        },
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
          "id": "eNOOug9ODsbtfjBk",
          "name": "Social Flood API Key Local"
        }
      },
      "executeOnce": false,
      "typeVersion": 4.2
    },
    {
      "id": "dfa987d0-c18c-44c4-9796-942404f49630",
      "name": "Split Out YT Search",
      "type": "n8n-nodes-base.splitOut",
      "position": [
        -1740,
        1120
      ],
      "parameters": {
        "options": {},
        "fieldToSplitOut": "tasks[0].result"
      },
      "executeOnce": false,
      "typeVersion": 1
    },
    {
      "id": "29196a5b-c46e-46f7-99ff-781a0d97c551",
      "name": "Google Filter",
      "type": "n8n-nodes-base.filter",
      "position": [
        -1520,
        800
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
              "id": "6e46fa28-2adf-47a0-bbf3-7a9b8b8413f7",
              "operator": {
                "type": "array",
                "operation": "exists",
                "singleValue": true
              },
              "leftValue": "={{ $json.monthly_searches }}",
              "rightValue": ""
            },
            {
              "id": "45bca7c3-eac2-44e8-9993-b53200174003",
              "operator": {
                "type": "number",
                "operation": "exists",
                "singleValue": true
              },
              "leftValue": "={{ $json.cpc }}",
              "rightValue": ""
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "6b11b8e2-d6fb-45d7-817e-3e1038068696",
      "name": "YT Filter",
      "type": "n8n-nodes-base.filter",
      "position": [
        -1520,
        1120
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
              "id": "6e46fa28-2adf-47a0-bbf3-7a9b8b8413f7",
              "operator": {
                "type": "array",
                "operation": "exists",
                "singleValue": true
              },
              "leftValue": "={{ $json.monthly_searches }}",
              "rightValue": ""
            },
            {
              "id": "45bca7c3-eac2-44e8-9993-b53200174003",
              "operator": {
                "type": "number",
                "operation": "exists",
                "singleValue": true
              },
              "leftValue": "={{ $json.cpc }}",
              "rightValue": ""
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "6d52836b-ce37-46c0-aa4b-7c2b917b9f1d",
      "name": "Add Second Tier YT Keyword Data",
      "type": "n8n-nodes-base.nocoDb",
      "position": [
        -440,
        980
      ],
      "parameters": {
        "table": "m8bp2fnwtqsd2m7",
        "fieldsUi": {
          "fieldValues": [
            {
              "fieldName": "=keyword",
              "fieldValue": "={{ $('Split Out YT Search').item.json.keyword }}"
            },
            {
              "fieldName": "location_code",
              "fieldValue": "={{ $('Split Out YT Search').item.json.location_code }}"
            },
            {
              "fieldName": "language_code",
              "fieldValue": "={{ $('Split Out YT Search').item.json.language_code }}"
            },
            {
              "fieldName": "search_partners",
              "fieldValue": "={{ $('Split Out YT Search').item.json.search_partners }}"
            },
            {
              "fieldName": "competition",
              "fieldValue": "={{ $('Split Out YT Search').item.json.competition }}"
            },
            {
              "fieldName": "competition_index",
              "fieldValue": "={{ $('Split Out YT Search').item.json.competition_index }}"
            },
            {
              "fieldName": "cpc",
              "fieldValue": "={{ $('Split Out YT Search').item.json.cpc }}"
            },
            {
              "fieldName": "low_top_of_page_bid",
              "fieldValue": "={{ $('Split Out YT Search').item.json.low_top_of_page_bid }}"
            },
            {
              "fieldName": "high_top_of_page_bid",
              "fieldValue": "={{ $('Split Out YT Search').item.json.high_top_of_page_bid }}"
            },
            {
              "fieldName": "search_volume",
              "fieldValue": "={{ $('Split Out YT Search').item.json.search_volume }}"
            }
          ]
        },
        "operation": "create",
        "projectId": "pbwiwe87uf1cpgc",
        "authentication": "nocoDbApiToken"
      },
      "credentials": {
        "nocoDbApiToken": {
          "id": "LAbGsn1RMARiq5Gy",
          "name": "NocoDB Token account"
        }
      },
      "executeOnce": false,
      "retryOnFail": true,
      "typeVersion": 3
    },
    {
      "id": "d4a72c2b-8c16-4f3e-80ad-1564ec8b33d4",
      "name": "Add Second Tier G Keyword Data",
      "type": "n8n-nodes-base.nocoDb",
      "position": [
        -440,
        400
      ],
      "parameters": {
        "table": "mjmbcomto18scyi",
        "fieldsUi": {
          "fieldValues": [
            {
              "fieldName": "=keyword",
              "fieldValue": "={{ $('Split Out Google Search').item.json.keyword }}"
            },
            {
              "fieldName": "location_code",
              "fieldValue": "={{ $('Split Out Google Search').item.json.location_code }}"
            },
            {
              "fieldName": "language_code",
              "fieldValue": "={{ $('Split Out Google Search').item.json.language_code }}"
            },
            {
              "fieldName": "search_partners",
              "fieldValue": "={{ $('Split Out Google Search').item.json.search_partners }}"
            },
            {
              "fieldName": "competition",
              "fieldValue": "={{ $('Split Out Google Search').item.json.competition }}"
            },
            {
              "fieldName": "competition_index",
              "fieldValue": "={{ $('Split Out Google Search').item.json.competition_index }}"
            },
            {
              "fieldName": "cpc",
              "fieldValue": "={{ $('Split Out Google Search').item.json.cpc }}"
            },
            {
              "fieldName": "low_top_of_page_bid",
              "fieldValue": "={{ $('Split Out Google Search').item.json.low_top_of_page_bid }}"
            },
            {
              "fieldName": "high_top_of_page_bid",
              "fieldValue": "={{ $('Split Out Google Search').item.json.high_top_of_page_bid }}"
            },
            {
              "fieldName": "search_volume",
              "fieldValue": "={{ $('Split Out Google Search').item.json.search_volume }}"
            }
          ]
        },
        "operation": "create",
        "projectId": "pbwiwe87uf1cpgc",
        "authentication": "nocoDbApiToken"
      },
      "credentials": {
        "nocoDbApiToken": {
          "id": "LAbGsn1RMARiq5Gy",
          "name": "NocoDB Token account"
        }
      },
      "executeOnce": false,
      "retryOnFail": true,
      "typeVersion": 3
    },
    {
      "id": "1fdaf0fc-5c11-406f-93fb-b4a7fd3b6eed",
      "name": "Format G Data",
      "type": "n8n-nodes-base.code",
      "position": [
        -240,
        400
      ],
      "parameters": {
        "jsCode": "// Get the monthly search data from the \"Loop Over Google Keywords\" node\nconst loopData = $node[\"Loop Over Google Keywords\"].json;\nif (!loopData || !loopData.monthly_searches || !Array.isArray(loopData.monthly_searches)) {\n  throw new Error(\"monthly_searches data is missing or not an array from Loop Over Google Keywords node.\");\n}\nconst monthlySearches = loopData.monthly_searches;\n\n// Get all items from the \"Add Second Tier G Keyword Data\" node\nconst secondTierItems = $items(\"Add Second Tier G Keyword Data\");\n\nif (!secondTierItems || secondTierItems.length === 0) {\n  throw new Error(\"No data found in Add Second Tier G Keyword Data node.\");\n}\n\nconst results = [];\n\n// Loop through each second-tier item\nsecondTierItems.forEach(itemWrapper => {\n  const item = itemWrapper.json;\n  // Validate that the required properties exist on the second-tier item.\n  if (!item.keyword || item.Id === undefined) {\n    throw new Error(\"A second tier item is missing 'keyword' or 'Id'.\");\n  }\n  \n  // For each monthly search record, combine with the second-tier data\n  monthlySearches.forEach(record => {\n    // Validate that each monthly record has the required properties.\n    if (record.year === undefined || record.month === undefined || record.search_volume === undefined) {\n      throw new Error(\"A monthly search record is missing 'year', 'month', or 'search_volume'.\");\n    }\n    \n    results.push({\n      json: {\n        keyword: item.keyword,\n        google_keyword_id: item.Id,\n        year: record.year,\n        month: record.month,\n        search_volume: record.search_volume,\n        unique_id: `${record.year}-${record.month}-${item.keyword}`\n      }\n    });\n  });\n});\n\n// Chunk the results into batches of 1000 items each\nconst batchSize = 1000;\nconst batchedResults = [];\n\nfor (let i = 0; i < results.length; i += batchSize) {\n  // Create a batch containing up to batchSize items\n  const batchItems = results.slice(i, i + batchSize).map(item => item.json);\n  batchedResults.push({\n    json: {\n      batch: batchItems\n    }\n  });\n}\n\nreturn batchedResults;\n"
      },
      "typeVersion": 2,
      "alwaysOutputData": false
    },
    {
      "id": "7d654cf7-1223-4f10-8026-997f5418402e",
      "name": "Format YT Data",
      "type": "n8n-nodes-base.code",
      "position": [
        -220,
        980
      ],
      "parameters": {
        "jsCode": "// Get the monthly search data from the \"Loop Over Google Keywords\" node\nconst loopData = $node[\"Loop Over YT Keywords\"].json;\nif (!loopData || !loopData.monthly_searches || !Array.isArray(loopData.monthly_searches)) {\n  throw new Error(\"monthly_searches data is missing or not an array from Loop Over YT Keywords node.\");\n}\nconst monthlySearches = loopData.monthly_searches;\n\n// Get all items from the \"Add Second Tier G Keyword Data\" node\nconst secondTierItems = $items(\"Add Second Tier YT Keyword Data\");\n\nif (!secondTierItems || secondTierItems.length === 0) {\n  throw new Error(\"No data found in Add Second Tier YT Keyword Data node.\");\n}\n\nconst results = [];\n\n// Loop through each second-tier item\nsecondTierItems.forEach(itemWrapper => {\n  const item = itemWrapper.json;\n  // Validate that the required properties exist on the second-tier item.\n  if (!item.keyword || item.Id === undefined) {\n    throw new Error(\"A second tier item is missing 'keyword' or 'Id'.\");\n  }\n  \n  // For each monthly search record, combine with the second-tier data\n  monthlySearches.forEach(record => {\n    // Validate that each monthly record has the required properties.\n    if (record.year === undefined || record.month === undefined || record.search_volume === undefined) {\n      throw new Error(\"A monthly search record is missing 'year', 'month', or 'search_volume'.\");\n    }\n    \n    results.push({\n      json: {\n        keyword: item.keyword,\n        google_keyword_id: item.Id,\n        year: record.year,\n        month: record.month,\n        search_volume: record.search_volume,\n        unique_id: `${record.year}-${record.month}-${item.keyword}`\n      }\n    });\n  });\n});\n\n// Chunk the results into batches of 1000 items each\nconst batchSize = 1000;\nconst batchedResults = [];\n\nfor (let i = 0; i < results.length; i += batchSize) {\n  // Create a batch containing up to batchSize items\n  const batchItems = results.slice(i, i + batchSize).map(item => item.json);\n  batchedResults.push({\n    json: {\n      batch: batchItems\n    }\n  });\n}\n\nreturn batchedResults;\n"
      },
      "typeVersion": 2
    },
    {
      "id": "67848762-a140-4c63-b8ca-e20331135741",
      "name": "Bulk Import G Monthly Search Volume",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        0,
        400
      ],
      "parameters": {
        "url": "http://192.168.1.186:8080/api/v2/tables/ma51kvf78diz0sg/records",
        "method": "POST",
        "options": {
          "batching": {
            "batch": {
              "batchSize": 1000
            }
          }
        },
        "jsonBody": "={{ $json.batch }}",
        "sendBody": true,
        "specifyBody": "json",
        "authentication": "predefinedCredentialType",
        "nodeCredentialType": "nocoDbApiToken"
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "eNOOug9ODsbtfjBk",
          "name": "Social Flood API Key Local"
        },
        "nocoDbApiToken": {
          "id": "LAbGsn1RMARiq5Gy",
          "name": "NocoDB Token account"
        }
      },
      "retryOnFail": true,
      "typeVersion": 4.2
    },
    {
      "id": "377b5470-9d9f-42e5-9528-fbf9fd3a1d77",
      "name": "Bulk Import YT Monthly Search Volume",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        40,
        980
      ],
      "parameters": {
        "url": "http://192.168.1.186:8080/api/v2/tables/ma51kvf78diz0sg/records",
        "method": "POST",
        "options": {
          "batching": {
            "batch": {
              "batchSize": 1000
            }
          }
        },
        "jsonBody": "={{ $json.batch }}",
        "sendBody": true,
        "specifyBody": "json",
        "authentication": "predefinedCredentialType",
        "nodeCredentialType": "nocoDbApiToken"
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "eNOOug9ODsbtfjBk",
          "name": "Social Flood API Key Local"
        },
        "nocoDbApiToken": {
          "id": "LAbGsn1RMARiq5Gy",
          "name": "NocoDB Token account"
        }
      },
      "retryOnFail": true,
      "typeVersion": 4.2
    },
    {
      "id": "6939afbf-b463-44fb-ab0b-45cbe81648eb",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -1860,
        600
      ],
      "parameters": {
        "width": 540,
        "height": 780,
        "content": "## Process and filter Keywords for monthly traffic and CPC"
      },
      "typeVersion": 1
    },
    {
      "id": "6fdbd7c3-75ca-4ed4-a5aa-3718bee0786f",
      "name": "Is Google Keyword Available",
      "type": "n8n-nodes-base.if",
      "position": [
        -680,
        640
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
              "id": "c4c4ed58-b14d-4973-93b2-4426fe314a2a",
              "operator": {
                "type": "number",
                "operation": "equals"
              },
              "leftValue": "={{ $json.pageInfo.totalRows }}",
              "rightValue": 0
            }
          ]
        }
      },
      "executeOnce": false,
      "typeVersion": 2.2
    },
    {
      "id": "f10d1313-fdfb-4f58-921d-65f307afab4e",
      "name": "Is YT Keyword Avaliable",
      "type": "n8n-nodes-base.if",
      "position": [
        -700,
        1260
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
              "id": "c4c4ed58-b14d-4973-93b2-4426fe314a2a",
              "operator": {
                "type": "number",
                "operation": "equals"
              },
              "leftValue": "={{ $json.pageInfo.totalRows }}",
              "rightValue": 0
            }
          ]
        }
      },
      "executeOnce": false,
      "typeVersion": 2.2
    },
    {
      "id": "c6c26129-fce0-4d98-a72a-662dcbc06ae0",
      "name": "Sticky Note5",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -1320,
        320
      ],
      "parameters": {
        "color": 4,
        "width": 1560,
        "height": 1280,
        "content": "## Add or update YouTube or Google Tables in NocoDB\n"
      },
      "typeVersion": 1
    },
    {
      "id": "a3c0ed20-f696-4ca6-a6fb-872cab8fbba5",
      "name": "Check for Google Keyword",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        -900,
        640
      ],
      "parameters": {
        "url": "=http://192.168.1.186:8080/api/v2/tables/mjmbcomto18scyi/records?where=(keyword,eq,{{ $json.keyword }})",
        "options": {
          "batching": {
            "batch": {
              "batchSize": 1,
              "batchInterval": 1
            }
          }
        },
        "authentication": "predefinedCredentialType",
        "nodeCredentialType": "nocoDbApiToken"
      },
      "credentials": {
        "nocoDbApiToken": {
          "id": "LAbGsn1RMARiq5Gy",
          "name": "NocoDB Token account"
        }
      },
      "executeOnce": false,
      "retryOnFail": true,
      "typeVersion": 4.2
    },
    {
      "id": "bb7cae83-8ff0-45d0-abca-d8d99efcfead",
      "name": "Check for YT Keyword",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        -940,
        1260
      ],
      "parameters": {
        "url": "=http://192.168.1.186:8080/api/v2/tables/m8bp2fnwtqsd2m7/records/?where=(keyword,eq,{{ $json.keyword }})",
        "options": {},
        "authentication": "predefinedCredentialType",
        "nodeCredentialType": "nocoDbApiToken"
      },
      "credentials": {
        "nocoDbApiToken": {
          "id": "LAbGsn1RMARiq5Gy",
          "name": "NocoDB Token account"
        }
      },
      "executeOnce": false,
      "retryOnFail": true,
      "typeVersion": 4.2
    },
    {
      "id": "e04d2f1c-45b6-4994-91a7-dc9f54a3fba8",
      "name": "Loop Over YT Keywords",
      "type": "n8n-nodes-base.splitInBatches",
      "position": [
        -1180,
        1240
      ],
      "parameters": {
        "options": {},
        "batchSize": 1000
      },
      "executeOnce": false,
      "typeVersion": 3
    },
    {
      "id": "452a67b4-d30c-4732-abc4-8b3513ec31f6",
      "name": "Update Second Tier G Keyword Data",
      "type": "n8n-nodes-base.nocoDb",
      "position": [
        -220,
        660
      ],
      "parameters": {
        "table": "mjmbcomto18scyi",
        "fieldsUi": {
          "fieldValues": [
            {
              "fieldName": "=keyword",
              "fieldValue": "={{ $('Split Out Google Search').item.json.keyword }}"
            },
            {
              "fieldName": "location_code",
              "fieldValue": "={{ $('Split Out Google Search').item.json.location_code }}"
            },
            {
              "fieldName": "language_code",
              "fieldValue": "={{ $('Split Out Google Search').item.json.language_code }}"
            },
            {
              "fieldName": "search_partners",
              "fieldValue": "={{ $('Split Out Google Search').item.json.search_partners }}"
            },
            {
              "fieldName": "competition",
              "fieldValue": "={{ $('Split Out Google Search').item.json.competition }}"
            },
            {
              "fieldName": "competition_index",
              "fieldValue": "={{ $('Split Out Google Search').item.json.competition_index }}"
            },
            {
              "fieldName": "cpc",
              "fieldValue": "={{ $('Split Out Google Search').item.json.cpc }}"
            },
            {
              "fieldName": "low_top_of_page_bid",
              "fieldValue": "={{ $('Split Out Google Search').item.json.low_top_of_page_bid }}"
            },
            {
              "fieldName": "high_top_of_page_bid",
              "fieldValue": "={{ $('Split Out Google Search').item.json.high_top_of_page_bid }}"
            },
            {
              "fieldName": "search_volume",
              "fieldValue": "={{ $('Split Out Google Search').item.json.search_volume }}"
            },
            {
              "fieldName": "id",
              "fieldValue": "={{ $json.list[0].Id }}"
            }
          ]
        },
        "operation": "update",
        "projectId": "pbwiwe87uf1cpgc",
        "authentication": "nocoDbApiToken"
      },
      "credentials": {
        "nocoDbApiToken": {
          "id": "LAbGsn1RMARiq5Gy",
          "name": "NocoDB Token account"
        }
      },
      "executeOnce": false,
      "retryOnFail": true,
      "typeVersion": 3
    },
    {
      "id": "e50cc116-3b5b-4908-b0b6-8781360cb5f2",
      "name": "Update Second Tier YT Keyword Data",
      "type": "n8n-nodes-base.nocoDb",
      "position": [
        -440,
        1280
      ],
      "parameters": {
        "table": "m8bp2fnwtqsd2m7",
        "fieldsUi": {
          "fieldValues": [
            {
              "fieldName": "=keyword",
              "fieldValue": "={{ $('Split Out YT Search').item.json.keyword }}"
            },
            {
              "fieldName": "location_code",
              "fieldValue": "={{ $('Split Out YT Search').item.json.location_code }}"
            },
            {
              "fieldName": "language_code",
              "fieldValue": "={{ $('Split Out YT Search').item.json.language_code }}"
            },
            {
              "fieldName": "search_partners",
              "fieldValue": "={{ $('Split Out YT Search').item.json.search_partners }}"
            },
            {
              "fieldName": "competition",
              "fieldValue": "={{ $('Split Out YT Search').item.json.competition }}"
            },
            {
              "fieldName": "competition_index",
              "fieldValue": "={{ $('Split Out YT Search').item.json.competition_index }}"
            },
            {
              "fieldName": "cpc",
              "fieldValue": "={{ $('Split Out YT Search').item.json.cpc }}"
            },
            {
              "fieldName": "low_top_of_page_bid",
              "fieldValue": "={{ $('Split Out YT Search').item.json.low_top_of_page_bid }}"
            },
            {
              "fieldName": "high_top_of_page_bid",
              "fieldValue": "={{ $('Split Out YT Search').item.json.high_top_of_page_bid }}"
            },
            {
              "fieldName": "search_volume",
              "fieldValue": "={{ $('Split Out YT Search').item.json.search_volume }}"
            },
            {
              "fieldName": "id",
              "fieldValue": "={{ $json.list[0].Id }}"
            }
          ]
        },
        "operation": "update",
        "projectId": "pbwiwe87uf1cpgc",
        "authentication": "nocoDbApiToken"
      },
      "credentials": {
        "nocoDbApiToken": {
          "id": "LAbGsn1RMARiq5Gy",
          "name": "NocoDB Token account"
        }
      },
      "executeOnce": false,
      "retryOnFail": true,
      "typeVersion": 3
    },
    {
      "id": "4ef57b89-913c-4e0e-8e60-675807ad6a5d",
      "name": "Loop Over Google Keywords",
      "type": "n8n-nodes-base.splitInBatches",
      "position": [
        -1160,
        620
      ],
      "parameters": {
        "options": {},
        "batchSize": 1000
      },
      "executeOnce": false,
      "typeVersion": 3
    },
    {
      "id": "94fbe48b-22bf-4a15-9ef0-423b1dab586a",
      "name": "Sticky Note6",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -3540,
        1560
      ],
      "parameters": {
        "width": 1060,
        "height": 380,
        "content": "## Setup Instuctions: \n### Required: NocoDB, N8N, [DataforSEO Account *aff*](https://app.dataforseo.com/?aff=184401), and [Social Flood Docker Instance](https://github.com/rainmanjam/social-flood)\n### Tables for NocoDB\n-- Base Keyword Search (Keyword)\n-- Second Order Google Keywords( keyword, location_code, language_code, search_partners, competition, competition_index, search_volume, cpc, low_top_of_page, high_top_of_page)\n-- Second Order YouTube Keywords( keyword, location_code, language_code, search_partners, competition, competition_index, search_volume, cpc, low_top_of_page, high_top_of_page)\n-- Search Volume( unique_id, year, month, search_volume, youtube_keyword_id, google_keyword_id)\n"
      },
      "typeVersion": 1
    },
    {
      "id": "8429c63d-09e7-47ac-a11b-e5132d5ac832",
      "name": "Combine G Keywords and Filter",
      "type": "n8n-nodes-base.code",
      "position": [
        -2300,
        800
      ],
      "parameters": {
        "jsCode": "// Gather all keywords from all items\nlet allKeywords = [];\n\nfor (const item of items) {\n  const keywordData = item.json.keyword_data;\n  const keywords = Object.values(keywordData)\n    .flatMap(section => Object.values(section))\n    .flat();\n\n  allKeywords = allKeywords.concat(keywords);\n}\n\n// Clean and transform the combined keywords\nconst cleanedKeywords = allKeywords\n  .filter(keyword => keyword.length <= 80)\n  .filter(keyword => keyword.split(\" \").length <= 10)\n  .map(keyword => keyword.replace(/[^a-zA-Z0-9\\s]/g, \"\"))\n  .map(keyword => keyword.trim())\n  .filter(keyword => keyword.length > 0)\n  .map(keyword => `\"${keyword}\"`);\n\n// Remove duplicates\nconst uniqueKeywords = Array.from(new Set(cleanedKeywords));\n\n// Split into batches of 1000\nconst batchSize = 1000;\nconst result = [];\n\nfor (let i = 0; i < uniqueKeywords.length; i += batchSize) {\n  result.push({\n    json: {\n      keywords: uniqueKeywords.slice(i, i + batchSize).join(\", \")\n    }\n  });\n}\n\n// Return as an array of objects\nreturn result;\n"
      },
      "typeVersion": 2
    },
    {
      "id": "5aa39111-c1c1-440e-b0e8-ba5c54909a0d",
      "name": "Combine YT Keywords and Filter",
      "type": "n8n-nodes-base.code",
      "position": [
        -2300,
        1120
      ],
      "parameters": {
        "jsCode": "// Gather all keywords from all items\nlet allKeywords = [];\n\nfor (const item of items) {\n  const keywordData = item.json.keyword_data;\n  const keywords = Object.values(keywordData)\n    .flatMap(section => Object.values(section))\n    .flat();\n\n  allKeywords = allKeywords.concat(keywords);\n}\n\n// Clean and transform the combined keywords\nconst cleanedKeywords = allKeywords\n  .filter(keyword => keyword.length <= 80)\n  .filter(keyword => keyword.split(\" \").length <= 10)\n  .map(keyword => keyword.replace(/[^a-zA-Z0-9\\s]/g, \"\"))\n  .map(keyword => keyword.trim())\n  .filter(keyword => keyword.length > 0)\n  .map(keyword => `\"${keyword}\"`);\n\n// Remove duplicates\nconst uniqueKeywords = Array.from(new Set(cleanedKeywords));\n\n// Split into batches of 1000\nconst batchSize = 1000;\nconst result = [];\n\nfor (let i = 0; i < uniqueKeywords.length; i += batchSize) {\n  result.push({\n    json: {\n      keywords: uniqueKeywords.slice(i, i + batchSize).join(\", \")\n    }\n  });\n}\n\n// Return as an array of objects\nreturn result;\n"
      },
      "typeVersion": 2
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "2712313f-4b1e-4f5b-8c6b-1f456896d981",
  "connections": {
    "NocoDB": {
      "main": [
        [
          {
            "node": "Second Order YouTube Autocomplete Keywords",
            "type": "main",
            "index": 0
          },
          {
            "node": "Second Order Google Autocomplete Keywords",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Gen Time": {
      "main": [
        [
          {
            "node": "NocoDB",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "YT Filter": {
      "main": [
        [
          {
            "node": "Loop Over YT Keywords",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Format G Data": {
      "main": [
        [
          {
            "node": "Bulk Import G Monthly Search Volume",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Filter": {
      "main": [
        [
          {
            "node": "Loop Over Google Keywords",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Format YT Data": {
      "main": [
        [
          {
            "node": "Bulk Import YT Monthly Search Volume",
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
            "node": "Gen Time",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Split Out YT Search": {
      "main": [
        [
          {
            "node": "YT Filter",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Check for YT Keyword": {
      "main": [
        [
          {
            "node": "Is YT Keyword Avaliable",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Search Volume": {
      "main": [
        [
          {
            "node": "Split Out Google Search",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Loop Over YT Keywords": {
      "main": [
        [],
        [
          {
            "node": "Check for YT Keyword",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "YouTube Search Volume": {
      "main": [
        [
          {
            "node": "Split Out YT Search",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Is YT Keyword Avaliable": {
      "main": [
        [
          {
            "node": "Add Second Tier YT Keyword Data",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Update Second Tier YT Keyword Data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Split Out Google Search": {
      "main": [
        [
          {
            "node": "Google Filter",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Check for Google Keyword": {
      "main": [
        [
          {
            "node": "Is Google Keyword Available",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Loop Over Google Keywords": {
      "main": [
        [],
        [
          {
            "node": "Check for Google Keyword",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Is Google Keyword Available": {
      "main": [
        [
          {
            "node": "Add Second Tier G Keyword Data",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Update Second Tier G Keyword Data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Combine G Keywords and Filter": {
      "main": [
        [
          {
            "node": "Google Search Volume",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Add Second Tier G Keyword Data": {
      "main": [
        [
          {
            "node": "Format G Data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Combine YT Keywords and Filter": {
      "main": [
        [
          {
            "node": "YouTube Search Volume",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Add Second Tier YT Keyword Data": {
      "main": [
        [
          {
            "node": "Format YT Data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Update Second Tier G Keyword Data": {
      "main": [
        [
          {
            "node": "Loop Over Google Keywords",
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
            "node": "Gen Time",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Update Second Tier YT Keyword Data": {
      "main": [
        [
          {
            "node": "Loop Over YT Keywords",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Bulk Import G Monthly Search Volume": {
      "main": [
        [
          {
            "node": "Loop Over Google Keywords",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Bulk Import YT Monthly Search Volume": {
      "main": [
        [
          {
            "node": "Loop Over YT Keywords",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Second Order Google Autocomplete Keywords": {
      "main": [
        [
          {
            "node": "Combine G Keywords and Filter",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Second Order YouTube Autocomplete Keywords": {
      "main": [
        [
          {
            "node": "Combine YT Keywords and Filter",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2135"></a>

## Template 2135 - Sincronização YouTube → Spotify (sem duplicados)

- **Nome:** Sincronização YouTube → Spotify (sem duplicados)
- **Descrição:** Atualiza uma playlist do Spotify com faixas extraídas de uma playlist do YouTube, pesquisando correspondências e adicionando apenas as faixas que ainda não estão na playlist.
- **Funcionalidade:** • Gatilho manual: Inicia o fluxo quando o usuário aciona o teste.
• Recuperar faixas do Spotify: Obtém todas as faixas existentes na playlist de destino para comparação.
• Recuperar itens da playlist do YouTube: Lista todos os vídeos/faixas de uma playlist do YouTube especificada.
• Processamento em lote: Divide os itens em lotes para processar um a um ou em grupos controlados.
• Buscar faixas no Spotify por título: Pesquisa cada título retornado do YouTube no catálogo do Spotify para encontrar a faixa correspondente.
• Extrair IDs de faixa: Extrai os IDs de faixas do Spotify tanto das faixas já presentes quanto das buscas realizadas.
• Comparar conjuntos de dados: Compara as faixas encontradas no YouTube com as faixas já presentes na playlist para identificar novas adições.
• Adicionar faixas novas à playlist: Insere apenas as faixas que não estão presentes na playlist do Spotify alvo.
- **Ferramentas:** • Spotify: Serviço de streaming usado para obter as faixas de uma playlist, pesquisar faixas pelo título e adicionar faixas à playlist de destino.
• YouTube: Plataforma de vídeo usada para recuperar os itens (títulos) de uma playlist de origem que serão buscados no catálogo do Spotify.

## Fluxo visual

```mermaid
flowchart LR
    N1["Compare the two Datasets"]
    N2["Extract the spotify track ID"]
    N3["Extract the Spotify Track ID"]
    N4["Find the returned tracks on Spotify"]
    N5["Get my tracks inside my playlist"]
    N6["Loop Over Items"]
    N7["When clicking ‘Test workflow’"]
    N8["Sticky Note"]
    N9["Sticky Note1"]
    N10["Get tracks inside the Spotify Playlist"]
    N11["Sticky Note2"]
    N12["Add tracks not already in playlist"]

    N6 --> N3
    N6 --> N4
    N1 --> N12
    N3 --> N1
    N2 --> N1
    N5 --> N6
    N7 --> N5
    N7 --> N10
    N4 --> N6
    N10 --> N2
```

## Fluxo (.json) :

```json
{
  "meta": {
    "instanceId": "6045c639951d83c8706b0dd8d6330164bda01fe58f103cedc2c276bf1f9c11f1"
  },
  "nodes": [
    {
      "id": "ab8e653f-a60c-497c-b732-6dea355aa985",
      "name": "Compare the two Datasets",
      "type": "n8n-nodes-base.compareDatasets",
      "position": [
        900,
        160
      ],
      "parameters": {
        "options": {},
        "mergeByFields": {
          "values": [
            {
              "field1": "Playlist avant ajout",
              "field2": "Nouvelle pistes"
            }
          ]
        }
      },
      "typeVersion": 2.3
    },
    {
      "id": "606aa397-efd6-4f6b-bfa6-946523ed80f2",
      "name": "Extract the spotify track ID",
      "type": "n8n-nodes-base.set",
      "position": [
        580,
        80
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "dd3db6c8-ecf5-4595-ac4b-559965b6e507",
              "name": "Playlist avant ajout",
              "type": "string",
              "value": "={{ $json.track.id }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "75e48bf0-5003-4904-b8c7-0cca005bacd7",
      "name": "Extract the Spotify Track ID",
      "type": "n8n-nodes-base.set",
      "position": [
        580,
        260
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "a9593caf-e403-4626-a96f-499e9f78465e",
              "name": "Nouvelle pistes",
              "type": "string",
              "value": "={{ $json.id }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "c536f1fb-cfbe-4a22-8f8f-37422629cc2b",
      "name": "Find the returned tracks on Spotify",
      "type": "n8n-nodes-base.spotify",
      "position": [
        580,
        440
      ],
      "parameters": {
        "limit": "={{ 1 }}",
        "query": "={{ $json.snippet.title }}",
        "filters": {},
        "resource": "track",
        "operation": "search"
      },
      "credentials": {
        "spotifyOAuth2Api": {
          "id": "sJyANc6jgR7IWZ20",
          "name": "Spotify account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "6be6eb69-0e90-46d8-9e74-92372c9ed5b8",
      "name": "Get my tracks inside my playlist",
      "type": "n8n-nodes-base.youTube",
      "position": [
        160,
        280
      ],
      "parameters": {
        "part": [
          "snippet"
        ],
        "options": {},
        "resource": "playlistItem",
        "operation": "getAll",
        "returnAll": true,
        "playlistId": "=PL552450E1514256AB"
      },
      "credentials": {
        "youTubeOAuth2Api": {
          "id": "QhzjhQ4w5yvTdBIN",
          "name": "YouTube account"
        }
      },
      "executeOnce": true,
      "typeVersion": 1
    },
    {
      "id": "8a2d297f-748c-4e59-a935-fecc944060aa",
      "name": "Loop Over Items",
      "type": "n8n-nodes-base.splitInBatches",
      "position": [
        360,
        280
      ],
      "parameters": {
        "options": {}
      },
      "typeVersion": 3
    },
    {
      "id": "677e635b-8ae6-48b4-8687-0615a044739c",
      "name": "When clicking ‘Test workflow’",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        -80,
        180
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "d7e52845-2279-40a5-82d3-5a923ead191c",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -640,
        -40
      ],
      "parameters": {
        "width": 517.7419354838706,
        "height": 654.6451612903234,
        "content": "## Workflow Overview\n\nThis workflow automates the process of updating a Spotify playlist with tracks from a YouTube playlist, ensuring no duplicates are added.\n\n## Key Components\n\n1. **Manual Trigger**: Starts the workflow when you click ‘Test workflow’.\n   \n2. **Spotify Integration**: Retrieves tracks from a specified Spotify playlist.\n\n3. **YouTube Integration**: Fetches tracks from a designated YouTube playlist.\n\n4. **Batch Processing**: Processes tracks in batches to handle multiple items efficiently.\n\n5. **Track Search**: Searches for YouTube tracks on Spotify to find corresponding IDs.\n\n6. **Comparison**: Compares existing Spotify tracks with YouTube tracks to identify which ones to add.\n\n7. **Track Addition**: Adds new Spotify tracks to the playlist that are not already included.\n\nIf you have any questions or need clarification, feel free to ask!\n"
      },
      "typeVersion": 1
    },
    {
      "id": "cd92585a-6c56-4a35-8714-96d2c73444bd",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        60,
        0
      ],
      "parameters": {
        "color": 5,
        "width": 251.65748259981103,
        "height": 468.0906115664312,
        "content": "### Retrieve the playlists you want to synchronise "
      },
      "typeVersion": 1
    },
    {
      "id": "a0ec1b4c-2422-4daa-92d6-4c84a1cecbf6",
      "name": "Get tracks inside the Spotify Playlist",
      "type": "n8n-nodes-base.spotify",
      "position": [
        160,
        80
      ],
      "parameters": {
        "id": "5SY22gVudzaD31v5rq5jcH",
        "resource": "playlist",
        "operation": "getTracks",
        "returnAll": true
      },
      "credentials": {
        "spotifyOAuth2Api": {
          "id": "sJyANc6jgR7IWZ20",
          "name": "Spotify account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "accba86b-6786-412e-8e87-17be458f6255",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        320,
        620
      ],
      "parameters": {
        "color": 6,
        "width": 414.86223899716344,
        "height": 80,
        "content": "### Search for the tracks on spotify one-by-one"
      },
      "typeVersion": 1
    },
    {
      "id": "062e4341-bb5c-4302-85f6-dedb03481e64",
      "name": "Add tracks not already in playlist",
      "type": "n8n-nodes-base.spotify",
      "position": [
        1120,
        300
      ],
      "parameters": {
        "id": "spotify:playlist:5SY22gVudzaD31v5rq5jcH",
        "trackID": "=spotify:track:{{ $json['Nouvelle pistes'] }}",
        "resource": "playlist",
        "additionalFields": {}
      },
      "credentials": {
        "spotifyOAuth2Api": {
          "id": "sJyANc6jgR7IWZ20",
          "name": "Spotify account"
        }
      },
      "typeVersion": 1
    }
  ],
  "pinData": {},
  "connections": {
    "Loop Over Items": {
      "main": [
        [
          {
            "node": "Extract the Spotify Track ID",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Find the returned tracks on Spotify",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Compare the two Datasets": {
      "main": [
        null,
        null,
        null,
        [
          {
            "node": "Add tracks not already in playlist",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract the Spotify Track ID": {
      "main": [
        [
          {
            "node": "Compare the two Datasets",
            "type": "main",
            "index": 1
          }
        ]
      ]
    },
    "Extract the spotify track ID": {
      "main": [
        [
          {
            "node": "Compare the two Datasets",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get my tracks inside my playlist": {
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
    "When clicking ‘Test workflow’": {
      "main": [
        [
          {
            "node": "Get my tracks inside my playlist",
            "type": "main",
            "index": 0
          },
          {
            "node": "Get tracks inside the Spotify Playlist",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Find the returned tracks on Spotify": {
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
    "Get tracks inside the Spotify Playlist": {
      "main": [
        [
          {
            "node": "Extract the spotify track ID",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2137"></a>

## Template 2137 - Criar item de erro no Monday.com

- **Nome:** Criar item de erro no Monday.com
- **Descrição:** Ao ocorrer um erro em um workflow, o fluxo cria um item em um quadro do Monday.com e preenche-o com detalhes do erro e a data.
- **Funcionalidade:** • Detecção de erro: Inicia a automação quando há um erro na execução do workflow.
• Criação de item: Gera um novo item no quadro, usando o ID da execução como nome.
• Captura de data e hora: Obtém a data atual para registrar quando o erro ocorreu.
• Extração de stacktrace: Recupera e faz escape do stacktrace do erro para armazenamento seguro.
• Coleta de mensagem de erro: Lê a mensagem de erro da execução para documentá-la.
• Atualização de colunas: Preenche múltiplas colunas do item com nome do workflow, stacktrace, mensagem de erro e data.
- **Ferramentas:** • Monday.com: Plataforma de gestão de projetos usada para criar e atualizar itens em um quadro, armazenando os detalhes do erro (nome do workflow, stacktrace, mensagem e data).

## Fluxo visual

```mermaid
flowchart LR
    N1["Monday"]
    N2["Date & Time"]
    N3["Error Trigger"]
    N4["Code"]
    N5["UPDATE"]

    N4 --> N5
    N1 --> N2
    N2 --> N4
    N3 --> N1
```

## Fluxo (.json) :

```json
{
  "meta": {
    "instanceId": "257476b1ef58bf3cb6a46e65fac7ee34a53a5e1a8492d5c6e4da5f87c9b82833",
    "templateId": "2074"
  },
  "nodes": [
    {
      "id": "25a95fba-9367-48ca-b7a3-5ab1fb701869",
      "name": "Monday",
      "type": "n8n-nodes-base.mondayCom",
      "notes": "CREATE ERROR ITEM",
      "position": [
        620,
        240
      ],
      "parameters": {
        "name": "={{ \"\".concat($('Error Trigger').last().json.execution.id) }}",
        "boardId": "1382091189",
        "groupId": "topics",
        "resource": "boardItem",
        "additionalFields": {}
      },
      "credentials": {
        "mondayComApi": {
          "id": "SP53wbPUCBNJRq1G",
          "name": "Monday.com account"
        }
      },
      "notesInFlow": true,
      "typeVersion": 1
    },
    {
      "id": "5fb18856-cd59-4f57-9e72-c637a206fa41",
      "name": "Date & Time",
      "type": "n8n-nodes-base.dateTime",
      "position": [
        840,
        240
      ],
      "parameters": {
        "options": {}
      },
      "typeVersion": 2
    },
    {
      "id": "66baa154-b421-4942-99e9-f00f6870b3fa",
      "name": "Error Trigger",
      "type": "n8n-nodes-base.errorTrigger",
      "position": [
        380,
        240
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "34347458-7509-4e08-a501-1cee4a307bb7",
      "name": "Code",
      "type": "n8n-nodes-base.code",
      "notes": "GET STACKTRACE",
      "position": [
        1040,
        240
      ],
      "parameters": {
        "jsCode": "\nconsole.log($('Error Trigger').last().json.execution)\nstr = escape ($('Error Trigger').last().json.execution.error.stack )\nreturn { \"stack\": str}"
      },
      "notesInFlow": true,
      "typeVersion": 2
    },
    {
      "id": "92b6e47b-1c34-40eb-9f9a-57e197528c86",
      "name": "UPDATE",
      "type": "n8n-nodes-base.mondayCom",
      "notes": "POPULUATE MONDAY ITEM",
      "position": [
        1280,
        240
      ],
      "parameters": {
        "itemId": "={{ $('Monday').last().json.id }}",
        "boardId": "1382091189",
        "resource": "boardItem",
        "operation": "changeMultipleColumnValues",
        "columnValues": "={ \"column_id_for_workflow_name (text)\" : \"{{  $('Error Trigger').item.json.workflow.name }}\",\n\"column_id_for_error_stack (long text)\" : \"{{ $('Code').last().json.stack}}\",\n\"column_id_for_error_message (text)\": \"{{ $('Error Trigger').item.json.execution.error.message }}\",\n\"column_id_for_date (text)\": \"{{ $('Date & Time').last().json.currentDate }}\"\n}\n"
      },
      "credentials": {
        "mondayComApi": {
          "id": "SP53wbPUCBNJRq1G",
          "name": "Monday.com account"
        }
      },
      "notesInFlow": true,
      "typeVersion": 1
    }
  ],
  "pinData": {
    "Error Trigger": [
      {
        "workflow": {
          "name": "My WF"
        },
        "execution": {
          "id": 1,
          "error": {
            "stack": "Some error here haha",
            "message": "New error"
          }
        }
      }
    ]
  },
  "connections": {
    "Code": {
      "main": [
        [
          {
            "node": "UPDATE",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Monday": {
      "main": [
        [
          {
            "node": "Date & Time",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Date & Time": {
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
    "Error Trigger": {
      "main": [
        [
          {
            "node": "Monday",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2138"></a>

## Template 2138 - Criar projeto, tag e entrada de tempo no Clockify

- **Nome:** Criar projeto, tag e entrada de tempo no Clockify
- **Descrição:** Fluxo que cria um projeto e uma tag no Clockify, registra uma entrada de tempo e depois atualiza essa entrada para associá‑la ao projeto criado.
- **Funcionalidade:** • Gatilho manual: Inicia o fluxo através de uma execução manual.
• Criação de projeto: Cria um novo projeto em um workspace específico com nome, nota, cor e visibilidade definidos.
• Criação de tag: Cria uma nova tag no mesmo workspace para categorizar entradas de tempo.
• Criação de entrada de tempo: Registra uma entrada de tempo com início, fim, descrição e associação à tag criada.
• Atualização de entrada de tempo: Atualiza a entrada de tempo criada para associá‑la ao projeto recém‑criado.
- **Ferramentas:** • Clockify: Plataforma de rastreamento de tempo e gerenciamento de projetos, usada para criar projetos, tags e entradas de tempo e para atualizar entradas existentes via API.

## Fluxo visual

```mermaid
flowchart LR
    N1["On clicking 'execute'"]
    N2["Clockify"]
    N3["Clockify1"]
    N4["Clockify2"]
    N5["Clockify3"]

    N2 --> N3
    N3 --> N4
    N4 --> N5
    N1 --> N2
```

## Fluxo (.json) :

```json
{
  "id": "76",
  "name": "Create a project, tag, and time entry, and update the time entry in Clockify",
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
      "name": "Clockify",
      "type": "n8n-nodes-base.clockify",
      "position": [
        450,
        300
      ],
      "parameters": {
        "name": "n8n-docs",
        "workspaceId": "5f7af249d33ce12a712306dd",
        "additionalFields": {
          "note": "For n8n-docs",
          "color": "#0000FF",
          "isPublic": false
        }
      },
      "credentials": {
        "clockifyApi": "clockify-burner"
      },
      "typeVersion": 1
    },
    {
      "name": "Clockify1",
      "type": "n8n-nodes-base.clockify",
      "position": [
        650,
        300
      ],
      "parameters": {
        "name": "docs",
        "resource": "tag",
        "workspaceId": "5f7af249d33ce12a712306dd"
      },
      "credentials": {
        "clockifyApi": "clockify-burner"
      },
      "typeVersion": 1
    },
    {
      "name": "Clockify2",
      "type": "n8n-nodes-base.clockify",
      "position": [
        850,
        300
      ],
      "parameters": {
        "start": "2020-10-05T08:30:00.000Z",
        "resource": "timeEntry",
        "workspaceId": "5f7af249d33ce12a712306dd",
        "additionalFields": {
          "end": "2020-10-05T09:30:00.000Z",
          "tagIds": [
            "5f7afbfc73610f56b88ee9ef"
          ],
          "description": "Added Clockify Docs"
        }
      },
      "credentials": {
        "clockifyApi": "clockify-burner"
      },
      "typeVersion": 1
    },
    {
      "name": "Clockify3",
      "type": "n8n-nodes-base.clockify",
      "position": [
        1050,
        300
      ],
      "parameters": {
        "resource": "timeEntry",
        "operation": "update",
        "timeEntryId": "={{$node[\"Clockify2\"].json[\"id\"]}}",
        "workspaceId": "5f7af249d33ce12a712306dd",
        "updateFields": {
          "projectId": "={{$node[\"Clockify\"].json[\"id\"]}}"
        }
      },
      "credentials": {
        "clockifyApi": "clockify-burner"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "Clockify": {
      "main": [
        [
          {
            "node": "Clockify1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Clockify1": {
      "main": [
        [
          {
            "node": "Clockify2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Clockify2": {
      "main": [
        [
          {
            "node": "Clockify3",
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
            "node": "Clockify",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2140"></a>

## Template 2140 - Publicar novos vídeos do YouTube no X

- **Nome:** Publicar novos vídeos do YouTube no X
- **Descrição:** Detecta novos vídeos de um canal do YouTube e publica automaticamente um post no X com texto gerado por IA.
- **Funcionalidade:** • Verificação agendada a cada 30 minutos: inicia o fluxo periodicamente para checar novidades.
• Busca de vídeos recentes do canal: obtém o vídeo mais recente publicado no período definido usando o ID do canal.
• Geração de texto com IA: cria um post de até 140 caracteres que inclui link, título e descrição do vídeo.
• Publicação automática no X: publica o conteúdo gerado na conta X conectada.
• Notas de configuração: inclui lembretes para inserir o Channel ID e link de config/ajuda.
- **Ferramentas:** • YouTube: plataforma para hospedar vídeos e fonte dos metadados e link do vídeo.
• OpenAI (ChatGPT): serviço de IA usado para gerar o texto do post com base no título, descrição e link do vídeo.
• X (Twitter): rede social onde o post gerado é publicado automaticamente.

## Fluxo visual

```mermaid
flowchart LR
    N1["Post to X"]
    N2["Sticky Note"]
    N3["Generate Post for X with ChatGPT"]
    N4["Sticky Note1"]
    N5["Fetch Latest Videos"]
    N6["Check Every 30 Min"]

    N6 --> N5
    N5 --> N3
    N3 --> N1
```

## Fluxo (.json) :

```json
{
  "id": "O9FXr8iXzhSgYKaL",
  "meta": {
    "instanceId": "d8bbc8c5a59875a8be9f3c7142d858bc46c4b8e36a11781a25e945fcf9a5767a"
  },
  "name": "Post New YouTube Videos to X",
  "tags": [],
  "nodes": [
    {
      "id": "576be5c4-1ed0-4d01-a980-cb2fc31e2223",
      "name": "Post to X",
      "type": "n8n-nodes-base.twitter",
      "position": [
        1280,
        380
      ],
      "parameters": {
        "text": "={{ $json.message.content }}",
        "additionalFields": {}
      },
      "credentials": {
        "twitterOAuth2Api": {
          "id": "FjHOuF0APzoMqIjG",
          "name": "X account"
        }
      },
      "typeVersion": 2
    },
    {
      "id": "3b87cf2a-51d5-4589-9729-bb1fe3cfceca",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        620,
        254.76543209876536
      ],
      "parameters": {
        "color": 3,
        "width": 221.82716049382665,
        "height": 308.7901234567902,
        "content": "🆔 Ensure you enter your YouTube Channel ID in the \"Channel ID\" field of this node. You can find your [Channel ID here](https://youtube.com/account_advanced)."
      },
      "typeVersion": 1
    },
    {
      "id": "912e631c-aa43-4e02-9816-b35fe6e62dd8",
      "name": "Generate Post for X with ChatGPT",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "position": [
        900,
        380
      ],
      "parameters": {
        "modelId": {
          "__rl": true,
          "mode": "list",
          "value": "gpt-3.5-turbo",
          "cachedResultName": "GPT-3.5-TURBO"
        },
        "options": {},
        "messages": {
          "values": [
            {
              "content": "=Write an engaging post about my latest YouTube video for X (Twitter) of no more than 140 characters in length. Link to the video at https://youtu.be/{{ $json.id.videoId }} use this title and description: {{ $json.snippet.title }} {{ $json.snippet.description }}"
            }
          ]
        }
      },
      "credentials": {
        "openAiApi": {
          "id": "UpdYKqoR9wsGBnaA",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1.3
    },
    {
      "id": "841ee140-7e37-4e9c-8ab2-2a3ee941d255",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        360,
        254.5679012345679
      ],
      "parameters": {
        "width": 244.34567901234558,
        "height": 102.81481481481477,
        "content": "**Use AI to Promote Your New YouTube Videos on X**\n\n🎬 Watch the [Setup Video Here](https://mrc.fm/ai2x)"
      },
      "typeVersion": 1
    },
    {
      "id": "583b7d5d-e5dc-4183-92ee-8135ce6095a8",
      "name": "Fetch Latest Videos",
      "type": "n8n-nodes-base.youTube",
      "position": [
        680,
        380
      ],
      "parameters": {
        "limit": 1,
        "filters": {
          "channelId": "UC08Fah8EIryeOZRkjBRohcQ",
          "publishedAfter": "={{ new Date(new Date().getTime() - 30 * 60000).toISOString() }}"
        },
        "options": {},
        "resource": "video"
      },
      "credentials": {
        "youTubeOAuth2Api": {
          "id": "cVI5wEqeFEeJ81nk",
          "name": "YouTube account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "6e391007-10e2-4e67-9db6-e13d5d2bef11",
      "name": "Check Every 30 Min",
      "type": "n8n-nodes-base.scheduleTrigger",
      "position": [
        460,
        380
      ],
      "parameters": {
        "rule": {
          "interval": [
            {
              "field": "minutes",
              "minutesInterval": 30
            }
          ]
        }
      },
      "typeVersion": 1.2
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "a321d863-1a58-4100-bf8f-d2af08f11382",
  "connections": {
    "Check Every 30 Min": {
      "main": [
        [
          {
            "node": "Fetch Latest Videos",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Fetch Latest Videos": {
      "main": [
        [
          {
            "node": "Generate Post for X with ChatGPT",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Generate Post for X with ChatGPT": {
      "main": [
        [
          {
            "node": "Post to X",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-2142"></a>

## Template 2142 - Extração de dados de recibo

- **Nome:** Extração de dados de recibo
- **Descrição:** Baixa uma imagem de um recibo e envia para um serviço de extração OCR para obter dados estruturados do recibo (valores, itens, data, estabelecimento).
- **Funcionalidade:** • Disparo manual: inicia o fluxo ao clicar em executar.
• Download de imagem: obtém a imagem do recibo a partir de uma URL.
• Envio para OCR de recibos: encaminha o arquivo de imagem para um serviço de extração de recibos utilizando credenciais.
• Recebimento de dados estruturados: recebe os campos extraídos do recibo (total, data, itens, estabelecimento) para uso posterior.
- **Ferramentas:** • Serviço de hospedagem de imagens (miro.medium.com): armazena e fornece a imagem do recibo por URL.
• Mindee Receipt API: serviço de OCR e extração de dados de recibos que processa imagens e retorna informações estruturadas.

## Fluxo visual

```mermaid
flowchart LR
    N1["On clicking 'execute'"]
    N2["Mindee"]
    N3["HTTP Request"]

    N3 --> N2
    N1 --> N3
```

## Fluxo (.json) :

```json
{
  "id": "77",
  "name": "Extract information from an image of a receipt",
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        250,
        340
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Mindee",
      "type": "n8n-nodes-base.mindee",
      "position": [
        650,
        340
      ],
      "parameters": {},
      "credentials": {
        "mindeeReceiptApi": "mindee"
      },
      "typeVersion": 1
    },
    {
      "name": "HTTP Request",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        450,
        340
      ],
      "parameters": {
        "url": "https://miro.medium.com/max/1400/0*1T9GkAb93w5NSMsf",
        "options": {},
        "responseFormat": "file"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "HTTP Request": {
      "main": [
        [
          {
            "node": "Mindee",
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
            "node": "HTTP Request",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
