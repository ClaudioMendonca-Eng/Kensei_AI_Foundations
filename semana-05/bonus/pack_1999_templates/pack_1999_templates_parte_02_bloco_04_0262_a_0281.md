# PACK 1999 TEMPLATES PARTE 02 - Bloco 4

Templates neste bloco: 20

## Sumário

- [Template 262 - Deploy MinIO com Docker (PUQ)](#template-262)
- [Template 263 - Notificação diária do tempo](#template-263)
- [Template 264 - Envio de certificados por e-mail em lotes](#template-264)
- [Template 265 - Conversa multi-agente escalável](#template-265)
- [Template 266 - Registrar transferências Wise → Airtable](#template-266)
- [Template 267 - Análise de redes sociais e email personalizado](#template-267)
- [Template 268 - Publicar no X usando perfil Airtop](#template-268)
- [Template 269 - Pesquisa web inteligente com reordenação semântica](#template-269)
- [Template 270 - Servidor MCP para calendário e funções](#template-270)
- [Template 271 - Detecção de Bounding Boxes com Gemini 2.0](#template-271)
- [Template 272 - Geração automática de relatórios de pesquisa](#template-272)
- [Template 273 - Orquestrador Master Multi‑Agente Pyragogy](#template-273)
- [Template 274 - Agente conversacional para consultas em Supabase](#template-274)
- [Template 275 - Gerar e enviar screenshots por e-mail](#template-275)
- [Template 276 - Leitura manual de JPGs de pasta](#template-276)
- [Template 277 - Criar tickets únicos no Jira a partir de alertas Splunk](#template-277)
- [Template 278 - Busca de torrent por título e adição ao Transmission](#template-278)
- [Template 279 - Salvar anexos de faturas por remetente e data](#template-279)
- [Template 280 - Resposta automática por IA a emails de informação](#template-280)
- [Template 281 - Notificar novo produto WooCommerce no Slack](#template-281)

---

<a id="template-262"></a>

## Template 262 - Deploy MinIO com Docker (PUQ)

- **Nome:** Deploy MinIO com Docker (PUQ)
- **Descrição:** Fluxo para provisionar e gerenciar um serviço MinIO em Docker, incluindo configuração de docker-compose, montagem de disco, proxy Nginx e controle via webhook com SSH.
- **Funcionalidade:** • Recepção de requisições via webhook com autenticação básica para controlar o deploy e operações do MinIO.
• Definição de parâmetros do ambiente (domínio, diretórios de clientes e montagem de disco).
• Validação de domínio e envio de resposta adequada (422 para domínio inválido).
• Geração de docker-compose para MinIO a partir de um template.
• Deploy e gerenciamento de containers via docker-compose (iniciar, parar, atualizações).
• Montagem e gerenciamento de disco virtual data.img com mount via fstab.
• Configuração e atualização de Nginx para servir o domínio e a console do MinIO (vhosts).
• Obtenção de informações do container (inspect, stats, logs) para monitoramento.
• Obtenção da versão do MinIO e lista de usuários via MinIO Client.
• Verificações de conectividade de serviços de proxy (nginx-proxy e let's encrypt companion).
• Resposta da API com resultados e status de cada operação.
- **Ferramentas:** • MinIO: servidor de armazenamento em contêiner.
• Docker: plataforma de containers.
• Docker Compose: orquestrador de containers.
• SSH: acesso remoto ao servidor para execução de comandos.
• Nginx: proxy reverso para domínio e console.
• MinIO Client (mc): gerência de usuários e operações administrativas do MinIO.
• Webhook HTTP externo: interface para disparo de ações (endpoint /docker-minio) com autenticação.

## Fluxo visual

```mermaid
flowchart LR
    N1["If"]
    N2["Parametrs"]
    N3["API"]
    N4["422-Invalid server domain"]
    N5["Code1"]
    N6["SSH"]
    N7["Container Actions"]
    N8["Service Actions"]
    N9["API answer"]
    N10["Inspect"]
    N11["Stat"]
    N12["Start"]
    N13["Stop"]
    N14["Test Connection1"]
    N15["Deploy"]
    N16["Suspend"]
    N17["Terminated"]
    N18["Unsuspend"]
    N19["Mount Disk"]
    N20["Unmount Disk"]
    N21["Log"]
    N22["ChangePackage"]
    N23["Sticky Note"]
    N24["Deploy-docker-compose"]
    N25["Version"]
    N26["Users"]
    N27["If1"]
    N28["MinIO"]
    N29["nginx"]
    N30["Container Stat"]
    N31["GET ACL"]
    N32["SET ACL"]
    N33["GET NET"]

    N1 --> N30
    N1 --> N7
    N1 --> N28
    N1 --> N27
    N1 --> N4
    N3 --> N2
    N27 --> N29
    N27 --> N8
    N21 --> N6
    N6 --> N5
    N11 --> N6
    N13 --> N6
    N5 --> N9
    N28 --> N25
    N28 --> N26
    N12 --> N6
    N26 --> N6
    N29 --> N24
    N15 --> N6
    N31 --> N6
    N33 --> N6
    N10 --> N6
    N32 --> N6
    N16 --> N6
    N25 --> N6
    N2 --> N1
    N18 --> N6
    N19 --> N6
    N17 --> N6
    N20 --> N6
    N22 --> N6
    N30 --> N10
    N30 --> N11
    N30 --> N21
    N8 --> N14
    N8 --> N15
    N8 --> N16
    N8 --> N18
    N8 --> N17
    N8 --> N22
    N14 --> N6
    N7 --> N12
    N7 --> N13
    N7 --> N19
    N7 --> N20
    N7 --> N31
    N7 --> N32
    N7 --> N33
    N24 --> N8
```

## Fluxo (.json) :

```json
{
  "id": "IJYpB2CIAdLk8Umg",
  "meta": {
    "instanceId": "ffb0782f8b2cf4278577cb919e0cd26141bc9ff8774294348146d454633aa4e3",
    "templateCredsSetupCompleted": true
  },
  "name": "puq-docker-minio-deploy",
  "tags": [],
  "nodes": [
    {
      "id": "d79fe295-a0b0-4871-8382-67d9af5d0d2c",
      "name": "If",
      "type": "n8n-nodes-base.if",
      "position": [
        -2060,
        -320
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
              "id": "b702e607-888a-42c9-b9a7-f9d2a64dfccd",
              "operator": {
                "type": "string",
                "operation": "equals"
              },
              "leftValue": "={{ $json.server_domain }}",
              "rightValue": "={{ $('API').item.json.body.server_domain }}"
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "52c088af-95ae-411f-b1fa-f50b8ea99b58",
      "name": "Parametrs",
      "type": "n8n-nodes-base.set",
      "position": [
        -2280,
        -320
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "a6328600-7ee0-4031-9bdb-fcee99b79658",
              "name": "server_domain",
              "type": "string",
              "value": "d01-test.uuq.pl"
            },
            {
              "id": "370ddc4e-0fc0-48f6-9b30-ebdfba72c62f",
              "name": "clients_dir",
              "type": "string",
              "value": "/opt/docker/clients"
            },
            {
              "id": "92202bb8-6113-4bc5-9a29-79d238456df2",
              "name": "mount_dir",
              "type": "string",
              "value": "/mnt"
            },
            {
              "id": "baa52df2-9c10-42b2-939f-f05ea85ea2be",
              "name": "screen_left",
              "type": "string",
              "value": "{{"
            },
            {
              "id": "2b19ed99-2630-412a-98b6-4be44d35d2e7",
              "name": "screen_right",
              "type": "string",
              "value": "}}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "9814333d-a9c1-4787-aed1-116db9395b88",
      "name": "API",
      "type": "n8n-nodes-base.webhook",
      "position": [
        -2600,
        -320
      ],
      "webhookId": "73068cf8-be17-4b10-b9a3-744f7e4843b0",
      "parameters": {
        "path": "docker-minio",
        "options": {},
        "httpMethod": [
          "POST"
        ],
        "responseMode": "responseNode",
        "authentication": "basicAuth",
        "multipleMethods": true
      },
      "credentials": {
        "httpBasicAuth": {
          "id": "J4uXcnEb1SIQ2VN7",
          "name": "MinIO"
        }
      },
      "typeVersion": 2
    },
    {
      "id": "a3e0156c-8033-4829-ab57-06e3708a7a09",
      "name": "422-Invalid server domain",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        -2100,
        0
      ],
      "parameters": {
        "options": {
          "responseCode": 422
        },
        "respondWith": "json",
        "responseBody": "[{\n  \"status\": \"error\",\n  \"error\": \"Invalid server domain\"\n}]"
      },
      "typeVersion": 1.1,
      "alwaysOutputData": false
    },
    {
      "id": "a5f410f8-ca52-4e85-b76f-651756c80de5",
      "name": "Code1",
      "type": "n8n-nodes-base.code",
      "position": [
        800,
        -240
      ],
      "parameters": {
        "mode": "runOnceForEachItem",
        "jsCode": "try {\n  if ($json.stdout === 'success') {\n    return {\n      json: {\n        status: 'success',\n        message: '',\n        data: '',\n      }\n    };\n  }\n\n  const parsedData = JSON.parse($json.stdout);\n\n  return {\n    json: {\n      status: parsedData.status === 'error' ? 'error' : 'success',\n      message: parsedData.message || (parsedData.status === 'error' ? 'An error occurred' : ''),\n      data: parsedData || '',\n    }\n  };\n\n} catch (error) {\n  return {\n    json: {\n      status: 'error',\n      message: $json.stdout??$json.error,\n      data: '',\n    }\n  };\n}"
      },
      "executeOnce": false,
      "retryOnFail": false,
      "typeVersion": 2,
      "alwaysOutputData": false
    },
    {
      "id": "e162574f-c3ce-4fd0-8b31-d251ea360389",
      "name": "SSH",
      "type": "n8n-nodes-base.ssh",
      "onError": "continueErrorOutput",
      "position": [
        500,
        -240
      ],
      "parameters": {
        "cwd": "=/",
        "command": "={{ $json.sh }}"
      },
      "credentials": {
        "sshPassword": {
          "id": "Cyjy61UWHwD2Xcd8",
          "name": "d01-test.uuq.pl-puq"
        }
      },
      "executeOnce": true,
      "typeVersion": 1
    },
    {
      "id": "70f53357-5cdc-428c-876c-77036d6736cc",
      "name": "Container Actions",
      "type": "n8n-nodes-base.switch",
      "position": [
        -1680,
        160
      ],
      "parameters": {
        "rules": {
          "values": [
            {
              "outputKey": "start",
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
                    "id": "66ad264d-5393-410c-bfa3-011ab8eb234a",
                    "operator": {
                      "name": "filter.operator.equals",
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $('API').item.json.body.command }}",
                    "rightValue": "container_start"
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "stop",
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
                    "id": "b48957a0-22c0-4ac0-82ef-abd9e7ab0207",
                    "operator": {
                      "name": "filter.operator.equals",
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $('API').item.json.body.command }}",
                    "rightValue": "container_stop"
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "mount_disk",
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
                    "id": "727971bf-4218-41c1-9b07-22df4b947852",
                    "operator": {
                      "name": "filter.operator.equals",
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $('API').item.json.body.command }}",
                    "rightValue": "container_mount_disk"
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "unmount_disk",
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
                    "id": "0c80b1d9-e7ca-4cf3-b3ac-b40fdf4dd8f8",
                    "operator": {
                      "name": "filter.operator.equals",
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $('API').item.json.body.command }}",
                    "rightValue": "container_unmount_disk"
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "container_get_acl",
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
                    "id": "755e1a9f-667a-4022-9cb5-3f8153f62e95",
                    "operator": {
                      "name": "filter.operator.equals",
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $('API').item.json.body.command }}",
                    "rightValue": "container_get_acl"
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "container_set_acl",
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
                    "id": "8d75626f-789e-42fc-be5e-3a4e93a9bbc6",
                    "operator": {
                      "name": "filter.operator.equals",
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $('API').item.json.body.command }}",
                    "rightValue": "container_set_acl"
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "container_get_net",
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
                    "id": "c49d811a-735c-42f4-8b77-d0cd47b3d2b8",
                    "operator": {
                      "name": "filter.operator.equals",
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $('API').item.json.body.command }}",
                    "rightValue": "container_get_net"
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
      "id": "901a657d-873c-4b92-9949-d03e73a5313c",
      "name": "Service Actions",
      "type": "n8n-nodes-base.switch",
      "position": [
        -900,
        -1300
      ],
      "parameters": {
        "rules": {
          "values": [
            {
              "outputKey": "test_connection",
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
                    "id": "3afdd2f1-fe93-47c2-95cd-bac9b1d94eeb",
                    "operator": {
                      "name": "filter.operator.equals",
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $('API').item.json.body.command }}",
                    "rightValue": "test_connection"
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "create",
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
                    "id": "102f10e9-ec6c-4e63-ba95-0fe6c7dc0bd1",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $('API').item.json.body.command }}",
                    "rightValue": "create"
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "suspend",
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
                    "id": "f62dfa34-6751-4b34-adcc-3d6ba1b21a8c",
                    "operator": {
                      "name": "filter.operator.equals",
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $('API').item.json.body.command }}",
                    "rightValue": "suspend"
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "unsuspend",
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
                    "id": "384d2026-b753-4c27-94c2-8f4fc189eb5f",
                    "operator": {
                      "name": "filter.operator.equals",
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $('API').item.json.body.command }}",
                    "rightValue": "unsuspend"
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "terminate",
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
                    "id": "0e190a97-827a-4e87-8222-093ff7048b21",
                    "operator": {
                      "name": "filter.operator.equals",
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $('API').item.json.body.command }}",
                    "rightValue": "terminate"
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "change_package",
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
                    "id": "6f7832f3-b61d-4517-ab6b-6007998136dd",
                    "operator": {
                      "name": "filter.operator.equals",
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $('API').item.json.body.command }}",
                    "rightValue": "change_package"
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
      "id": "1c59a844-f4ef-422f-abbf-288a55e11934",
      "name": "API answer",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        820,
        0
      ],
      "parameters": {
        "options": {
          "responseCode": 200
        },
        "respondWith": "allIncomingItems"
      },
      "typeVersion": 1.1,
      "alwaysOutputData": true
    },
    {
      "id": "c2019d97-1012-4089-84c3-305308f8603f",
      "name": "Inspect",
      "type": "n8n-nodes-base.set",
      "onError": "continueRegularOutput",
      "position": [
        -1160,
        -380
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "21f4453e-c136-4388-be90-1411ae78e8a5",
              "name": "sh",
              "type": "string",
              "value": "=#!/bin/bash\n\nCOMPOSE_DIR=\"{{ $('Parametrs').item.json.clients_dir }}/{{ $('API').item.json.body.domain }}\"\nCONTAINER_NAME=\"{{ $('API').item.json.body.domain }}\"\n\nINSPECT_JSON=\"{}\"\nif sudo docker ps -a --filter \"name=$CONTAINER_NAME\" | grep -q \"$CONTAINER_NAME\"; then\n  INSPECT_JSON=$(sudo docker inspect \"$CONTAINER_NAME\")\nfi\n\necho \"{\\\"inspect\\\": $INSPECT_JSON}\"\n\nexit 0\n"
            }
          ]
        }
      },
      "typeVersion": 3.4,
      "alwaysOutputData": true
    },
    {
      "id": "a274a2d1-2382-48a0-a94d-6ef89cd22a57",
      "name": "Stat",
      "type": "n8n-nodes-base.set",
      "onError": "continueRegularOutput",
      "position": [
        -1060,
        -240
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "21f4453e-c136-4388-be90-1411ae78e8a5",
              "name": "sh",
              "type": "string",
              "value": "=#!/bin/bash\n\nCOMPOSE_DIR=\"{{ $('Parametrs').item.json.clients_dir }}/{{ $('API').item.json.body.domain }}\"\nSTATUS_FILE=\"$COMPOSE_DIR/status.json\"\nIMG_FILE=\"$COMPOSE_DIR/data.img\"\nMOUNT_DIR=\"{{ $('Parametrs').item.json.mount_dir }}/{{ $('API').item.json.body.domain }}\"\nCONTAINER_NAME=\"{{ $('API').item.json.body.domain }}\"\n\n# Initialize empty container data\nINSPECT_JSON=\"{}\"\nSTATS_JSON=\"{}\"\n\n# Check if container is running\nif sudo docker ps -a --filter \"name=$CONTAINER_NAME\" | grep -q \"$CONTAINER_NAME\"; then\n  # Get Docker inspect info in JSON (as raw string)\n  INSPECT_JSON=$(sudo docker inspect \"$CONTAINER_NAME\")\n\n  # Get Docker stats info in JSON (as raw string)\n  STATS_JSON=$(sudo docker stats --no-stream --format \"{{ $('Parametrs').item.json.screen_left }}json .{{ $('Parametrs').item.json.screen_right }}\" \"$CONTAINER_NAME\")\n  STATS_JSON=${STATS_JSON:-'{}'}\nfi\n\n# Initialize disk info variables\nMOUNT_USED=\"N/A\"\nMOUNT_FREE=\"N/A\"\nMOUNT_TOTAL=\"N/A\"\nMOUNT_PERCENT=\"N/A\"\nIMG_SIZE=\"N/A\"\nIMG_PERCENT=\"N/A\"\nDISK_STATS_IMG=\"N/A\"\n\n# Check if mount directory exists and is accessible\nif [ -d \"$MOUNT_DIR\" ]; then\n  if mount | grep -q \"$MOUNT_DIR\"; then\n    # Get disk usage for mounted directory\n    DISK_STATS_MOUNT=$(df -h \"$MOUNT_DIR\" | tail -n 1)\n    MOUNT_USED=$(echo \"$DISK_STATS_MOUNT\" | awk '{print $3}')\n    MOUNT_FREE=$(echo \"$DISK_STATS_MOUNT\" | awk '{print $4}')\n    MOUNT_TOTAL=$(echo \"$DISK_STATS_MOUNT\" | awk '{print $2}')\n    MOUNT_PERCENT=$(echo \"$DISK_STATS_MOUNT\" | awk '{print $5}')\n  fi\nfi\n\n# Check if image file exists\nif [ -f \"$IMG_FILE\" ]; then\n  # Get disk usage for image file\n  IMG_SIZE=$(du -sh \"$IMG_FILE\" | awk '{print $1}')\nfi\n\n# Manually create a combined JSON object\nFINAL_JSON=\"{\\\"inspect\\\": $INSPECT_JSON, \\\"stats\\\": $STATS_JSON, \\\"disk\\\": {\\\"mounted\\\": {\\\"used\\\": \\\"$MOUNT_USED\\\", \\\"free\\\": \\\"$MOUNT_FREE\\\", \\\"total\\\": \\\"$MOUNT_TOTAL\\\", \\\"percent\\\": \\\"$MOUNT_PERCENT\\\"}, \\\"img_file\\\": {\\\"size\\\": \\\"$IMG_SIZE\\\"}}}\"\n\n# Output the result\necho \"$FINAL_JSON\"\n\nexit 0"
            }
          ]
        }
      },
      "typeVersion": 3.4,
      "alwaysOutputData": true
    },
    {
      "id": "3e80ebbe-bb8e-4fec-ab20-ba69271a48f8",
      "name": "Start",
      "type": "n8n-nodes-base.set",
      "onError": "continueRegularOutput",
      "position": [
        -1180,
        140
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "21f4453e-c136-4388-be90-1411ae78e8a5",
              "name": "sh",
              "type": "string",
              "value": "=#!/bin/bash\n\nCOMPOSE_DIR=\"{{ $('Parametrs').item.json.clients_dir }}/{{ $('API').item.json.body.domain }}\"\nIMG_FILE=\"$COMPOSE_DIR/data.img\"\nMOUNT_DIR=\"{{ $('Parametrs').item.json.mount_dir }}/{{ $('API').item.json.body.domain }}\"\n\n# Function to log an error, write to status file, and print to console\nhandle_error() {\n    echo \"error: $1\"\n    exit 1\n}\n\nif ! df -h | grep -q \"$MOUNT_DIR\"; then\n    handle_error \"The file $IMG_FILE is not mounted to $MOUNT_DIR\"\nfi\n\nif sudo docker ps --filter \"name={{ $('API').item.json.body.domain }}\" --filter \"status=running\" -q | grep -q .; then\n    handle_error \"{{ $('API').item.json.body.domain }} container is running\"\nfi\n\n# Change to the compose directory\ncd \"$COMPOSE_DIR\" > /dev/null 2>&1 || handle_error \"Failed to change directory to $COMPOSE_DIR\"\n\n# Start the Docker containers\nif ! sudo docker-compose up -d > /dev/null 2>error.log; then\n    ERROR_MSG=$(tail -n 10 error.log)\n    handle_error \"Docker-compose failed: $ERROR_MSG\"\nfi\n\n# Success\necho \"success\"\n\nexit 0\n"
            }
          ]
        }
      },
      "typeVersion": 3.4,
      "alwaysOutputData": true
    },
    {
      "id": "4e13ceea-a01f-438c-ba6f-27f55b88798b",
      "name": "Stop",
      "type": "n8n-nodes-base.set",
      "onError": "continueRegularOutput",
      "position": [
        -1060,
        240
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "21f4453e-c136-4388-be90-1411ae78e8a5",
              "name": "sh",
              "type": "string",
              "value": "=#!/bin/bash\n\nCOMPOSE_DIR=\"{{ $('Parametrs').item.json.clients_dir }}/{{ $('API').item.json.body.domain }}\"\nIMG_FILE=\"$COMPOSE_DIR/data.img\"\nMOUNT_DIR=\"{{ $('Parametrs').item.json.mount_dir }}/{{ $('API').item.json.body.domain }}\"\n\n# Function to log an error, write to status file, and print to console\nhandle_error() {\n    echo \"error: $1\"\n    exit 1\n}\n\n# Check if Docker container is running\nif ! sudo docker ps --filter \"name={{ $('API').item.json.body.domain }}\" --filter \"status=running\" -q | grep -q .; then\n    handle_error \"{{ $('API').item.json.body.domain }} container is not running\"\nfi\n\n# Stop and remove the Docker containers (also remove associated volumes)\nif ! sudo docker-compose -f \"$COMPOSE_DIR/docker-compose.yml\" down > /dev/null 2>&1; then\n    handle_error \"Failed to stop and remove docker-compose containers\"\nfi\n\necho \"success\"\n\nexit 0\n"
            }
          ]
        }
      },
      "typeVersion": 3.4,
      "alwaysOutputData": true
    },
    {
      "id": "afa7a4e2-85a6-420b-9e33-30802e9cbb7b",
      "name": "Test Connection1",
      "type": "n8n-nodes-base.set",
      "onError": "continueRegularOutput",
      "position": [
        -220,
        -1320
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "21f4453e-c136-4388-be90-1411ae78e8a5",
              "name": "sh",
              "type": "string",
              "value": "=#!/bin/bash\n\n# Function to log an error, print to console\nhandle_error() {\n    echo \"error: $1\"\n    exit 1\n}\n\n# Check if Docker is installed\nif ! command -v docker &> /dev/null; then\n    handle_error \"Docker is not installed\"\nfi\n\n# Check if Docker service is running\nif ! systemctl is-active --quiet docker; then\n    handle_error \"Docker service is not running\"\nfi\n\n# Check if nginx-proxy container is running\nif ! sudo docker ps --filter \"name=nginx-proxy\" --filter \"status=running\" -q > /dev/null; then\n    handle_error \"nginx-proxy container is not running\"\nfi\n\n# Check if letsencrypt-nginx-proxy-companion container is running\nif ! sudo docker ps --filter \"name=letsencrypt-nginx-proxy-companion\" --filter \"status=running\" -q > /dev/null; then\n    handle_error \"letsencrypt-nginx-proxy-companion container is not running\"\nfi\n\n# If everything is successful\necho \"success\"\n\nexit 0\n"
            }
          ]
        }
      },
      "typeVersion": 3.4,
      "alwaysOutputData": true
    },
    {
      "id": "6c8261b4-f024-4b8e-a11c-1f2305e03e1d",
      "name": "Deploy",
      "type": "n8n-nodes-base.set",
      "onError": "continueRegularOutput",
      "position": [
        -220,
        -1120
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "21f4453e-c136-4388-be90-1411ae78e8a5",
              "name": "sh",
              "type": "string",
              "value": "=#!/bin/bash\n\n# Get values for variables from templates\nDOMAIN=\"{{ $('API').item.json.body.domain }}\"\nCOMPOSE_DIR=\"{{ $('Parametrs').item.json.clients_dir }}/$DOMAIN\"\nCOMPOSE_FILE=\"$COMPOSE_DIR/docker-compose.yml\"\nSTATUS_FILE=\"$COMPOSE_DIR/status\"\nIMG_FILE=\"$COMPOSE_DIR/data.img\"\nNGINX_DIR=\"$COMPOSE_DIR/nginx\"\nVHOST_DIR=\"/opt/docker/nginx-proxy/nginx/vhost.d\"\nMOUNT_DIR=\"{{ $('Parametrs').item.json.mount_dir }}/$DOMAIN\"\nDOCKER_COMPOSE_TEXT='{{ $('Deploy-docker-compose').item.json[\"docker-compose\"] }}'\n\nNGINX_MAIN_ACL_FILE=\"$NGINX_DIR/$DOMAIN\"_acl\n\nNGINX_MAIN_TEXT='{{ $('nginx').item.json['main'] }}'\nNGINX_MAIN_FILE=\"$NGINX_DIR/$DOMAIN\"\nVHOST_MAIN_FILE=\"$VHOST_DIR/$DOMAIN\"\n\nNGINX_MAIN_LOCATION_TEXT='{{ $('nginx').item.json['main_location'] }}'\nNGINX_MAIN_LOCATION_FILE=\"$NGINX_DIR/$DOMAIN\"_location\nVHOST_MAIN_LOCATION_FILE=\"$VHOST_DIR/$DOMAIN\"_location\n\n\nNGINX_CONSOLE_ACL_FILE=\"$NGINX_DIR/console.$DOMAIN\"_acl\n\nNGINX_CONSOLE_TEXT='{{ $('nginx').item.json['console'] }}'\nNGINX_CONSOLE_FILE=\"$NGINX_DIR/console.$DOMAIN\"\nVHOST_CONSOLE_FILE=\"$VHOST_DIR/console.$DOMAIN\"\n\nNGINX_CONSOLE_LOCATION_TEXT='{{ $('nginx').item.json['console_location'] }}'\nNGINX_CONSOLE_LOCATION_FILE=\"$NGINX_DIR/console.$DOMAIN\"_location\nVHOST_CONSOLE_LOCATION_FILE=\"$VHOST_DIR/console.$DOMAIN\"_location\n\n\nDISK_SIZE=\"{{ $('API').item.json.body.disk }}\"\n\n# Function to handle errors: write to the status file and print the message to console\nhandle_error() {\n    STATUS_JSON=\"{\\\"status\\\": \\\"error\\\", \\\"message\\\": \\\"$1\\\"}\"\n    echo \"$STATUS_JSON\" | sudo tee \"$STATUS_FILE\" > /dev/null  # Write error to the status file\n    echo \"error: $1\"  # Print the error message to the console\n    exit 1  # Exit the script with an error code\n}\n\n# Check if the directory already exists. If yes, exit with an error.\nif [ -d \"$COMPOSE_DIR\" ]; then\n    echo \"error: Directory $COMPOSE_DIR already exists\"\n    exit 1\nfi\n\n# Create necessary directories with permissions\nsudo mkdir -p \"$COMPOSE_DIR\" > /dev/null 2>&1 || handle_error \"Failed to create $COMPOSE_DIR\"\nsudo mkdir -p \"$NGINX_DIR\" > /dev/null 2>&1 || handle_error \"Failed to create $NGINX_DIR\"\nsudo mkdir -p \"$MOUNT_DIR\" > /dev/null 2>&1 || handle_error \"Failed to create $MOUNT_DIR\"\n\n# Set permissions on the created directories\nsudo chmod -R 777 \"$COMPOSE_DIR\" > /dev/null 2>&1 || handle_error \"Failed to set permissions on $COMPOSE_DIR\"\nsudo chmod -R 777 \"$NGINX_DIR\" > /dev/null 2>&1 || handle_error \"Failed to set permissions on $NGINX_DIR\"\nsudo chmod -R 777 \"$MOUNT_DIR\" > /dev/null 2>&1 || handle_error \"Failed to set permissions on $MOUNT_DIR\"\n\n# Create docker-compose.yml file\necho \"$DOCKER_COMPOSE_TEXT\" | sudo tee \"$COMPOSE_FILE\" > /dev/null 2>&1 || handle_error \"Failed to create $COMPOSE_FILE\"\n\n# Create NGINX configuration files\necho \"\" | sudo tee \"$NGINX_MAIN_ACL_FILE\" > /dev/null 2>&1 || handle_error \"Failed to create $NGINX_MAIN_ACL_FILE\"\necho \"\" | sudo tee \"$NGINX_CONSOLE_ACL_FILE\" > /dev/null 2>&1 || handle_error \"Failed to create $NGINX_CONSOLE_ACL_FILE\"\n\necho \"$NGINX_MAIN_TEXT\" | sudo tee \"$NGINX_MAIN_FILE\" > /dev/null 2>&1 || handle_error \"Failed to create $NGINX_MAIN_FILE\"\necho \"$NGINX_MAIN_LOCATION_TEXT\" | sudo tee \"$NGINX_MAIN_LOCATION_FILE\" > /dev/null 2>&1 || handle_error \"Failed to create $NGINX_MAIN_LOCATION_FILE\"\n\necho \"$NGINX_CONSOLE_TEXT\" | sudo tee \"$NGINX_CONSOLE_FILE\" > /dev/null 2>&1 || handle_error \"Failed to create $NGINX_CONSOLE_FILE\"\necho \"$NGINX_CONSOLE_LOCATION_TEXT\" | sudo tee \"$NGINX_CONSOLE_LOCATION_FILE\" > /dev/null 2>&1 || handle_error \"Failed to create $NGINX_CONSOLE_LOCATION_FILE\"\n\n# Change to the compose directory\ncd \"$COMPOSE_DIR\" > /dev/null 2>&1 || handle_error \"Failed to change directory to $COMPOSE_DIR\"\n\n# Create data.img file if it doesn't exist\nif [ ! -f \"$IMG_FILE\" ]; then\n    sudo fallocate -l \"$DISK_SIZE\"G \"$IMG_FILE\" > /dev/null 2>&1 || sudo truncate -s \"$DISK_SIZE\"G \"$IMG_FILE\" > /dev/null 2>&1 || handle_error \"Failed to create $IMG_FILE\"\n    sudo mkfs.ext4 \"$IMG_FILE\" > /dev/null 2>&1 || handle_error \"Failed to format $IMG_FILE\"  # Format the image as ext4\n    sync  # Synchronize the data to disk\nfi\n\n# Add an entry to /etc/fstab for mounting if not already present\nif ! grep -q \"$IMG_FILE\" /etc/fstab; then\n    echo \"$IMG_FILE $MOUNT_DIR ext4 loop 0 0\" | sudo tee -a /etc/fstab > /dev/null || handle_error \"Failed to add entry to /etc/fstab\"\nfi\n\n# Mount all entries in /etc/fstab\nsudo mount -a || handle_error \"Failed to mount entries from /etc/fstab\"\n\n# Set permissions on the mount directory\nsudo chmod -R 777 \"$MOUNT_DIR\" > /dev/null 2>&1 || handle_error \"Failed to set permissions on $MOUNT_DIR\"\n\n# Copy NGINX configuration files instead of creating symbolic links\nsudo cp -f \"$NGINX_MAIN_FILE\" \"$VHOST_MAIN_FILE\" || handle_error \"Failed to copy $NGINX_MAIN_FILE to $VHOST_MAIN_FILE\"\nsudo chmod 777 \"$VHOST_MAIN_FILE\" || handle_error \"Failed to set permissions on $VHOST_MAIN_FILE\"\n\nsudo cp -f \"$NGINX_MAIN_LOCATION_FILE\" \"$VHOST_MAIN_LOCATION_FILE\" || handle_error \"Failed to copy $NGINX_MAIN_LOCATION_FILE to $VHOST_MAIN_LOCATION_FILE\"\nsudo chmod 777 \"$VHOST_MAIN_LOCATION_FILE\" || handle_error \"Failed to set permissions on $VHOST_MAIN_LOCATION_FILE\"\n\nsudo cp -f \"$NGINX_CONSOLE_FILE\" \"$VHOST_CONSOLE_FILE\" || handle_error \"Failed to copy $NGINX_CONSOLE_FILE to $VHOST_CONSOLE_FILE\"\nsudo chmod 777 \"$VHOST_CONSOLE_FILE\" || handle_error \"Failed to set permissions on $VHOST_CONSOLE_FILE\"\n\nsudo cp -f \"$NGINX_CONSOLE_LOCATION_FILE\" \"$VHOST_CONSOLE_LOCATION_FILE\" || handle_error \"Failed to copy $NGINX_CONSOLE_LOCATION_FILE to $VHOST_CONSOLE_LOCATION_FILE\"\nsudo chmod 777 \"$VHOST_CONSOLE_LOCATION_FILE\" || handle_error \"Failed to set permissions on $VHOST_CONSOLE_LOCATION_FILE\"\n\n# Start Docker containers using docker-compose\nif ! sudo docker-compose up -d > /dev/null 2>error.log; then\n    ERROR_MSG=$(tail -n 10 error.log)  # Read the last 10 lines from error.log\n    handle_error \"Docker-compose failed: $ERROR_MSG\"\nfi\n\n# If everything is successful, update the status file and print success message\necho \"active\" | sudo tee \"$STATUS_FILE\" > /dev/null\necho \"success\"\n\nexit 0\n"
            }
          ]
        }
      },
      "typeVersion": 3.4,
      "alwaysOutputData": true
    },
    {
      "id": "d2f48f02-1a75-445e-832b-f9bf1a4d4b71",
      "name": "Suspend",
      "type": "n8n-nodes-base.set",
      "onError": "continueRegularOutput",
      "position": [
        -220,
        -960
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "21f4453e-c136-4388-be90-1411ae78e8a5",
              "name": "sh",
              "type": "string",
              "value": "=#!/bin/bash\n\nDOMAIN=\"{{ $('API').item.json.body.domain }}\"\nCOMPOSE_DIR=\"{{ $('Parametrs').item.json.clients_dir }}/$DOMAIN\"\nCOMPOSE_FILE=\"$COMPOSE_DIR/docker-compose.yml\"\nSTATUS_FILE=\"$COMPOSE_DIR/status\"\nIMG_FILE=\"$COMPOSE_DIR/data.img\"\nNGINX_DIR=\"$COMPOSE_DIR/nginx\"\nVHOST_DIR=\"/opt/docker/nginx-proxy/nginx/vhost.d\"\nMOUNT_DIR=\"{{ $('Parametrs').item.json.mount_dir }}/$DOMAIN\"\n\nVHOST_MAIN_FILE=\"$VHOST_DIR/$DOMAIN\"\nVHOST_MAIN_LOCATION_FILE=\"$VHOST_DIR/$DOMAIN\"_location\nVHOST_CONSOLE_FILE=\"$VHOST_DIR/console.$DOMAIN\"\nVHOST_CONSOLE_LOCATION_FILE=\"$VHOST_DIR/console.$DOMAIN\"_location\n\n# Function to log an error, write to status file, and print to console\nhandle_error() {\n    STATUS_JSON=\"{\\\"status\\\": \\\"error\\\", \\\"message\\\": \\\"$1\\\"}\"\n    echo \"$STATUS_JSON\" | sudo tee \"$STATUS_FILE\" > /dev/null\n    echo \"error: $1\"\n    exit 1\n}\n\n# Stop and remove Docker containers (also remove associated volumes)\nif [ -f \"$COMPOSE_FILE\" ]; then\n    if ! sudo docker-compose -f \"$COMPOSE_FILE\" down > /dev/null 2>&1; then\n        handle_error \"Failed to stop and remove docker-compose containers\"\n    fi\nelse\n    echo \"Warning: docker-compose.yml not found, skipping container stop.\"\nfi\n\n# Remove mount entry from /etc/fstab if it exists\nif grep -q \"$IMG_FILE\" /etc/fstab; then\n    sudo sed -i \"\\|$(printf '%s\\n' \"$IMG_FILE\" | sed 's/[.[\\*^$]/\\\\&/g')|d\" /etc/fstab\nfi\n\n# Unmount the image if it is mounted\nif mount | grep -q \"$MOUNT_DIR\"; then\n    sudo umount \"$MOUNT_DIR\" > /dev/null 2>&1 || handle_error \"Failed to unmount $MOUNT_DIR\"\nfi\n\n# Remove the mount directory\nif [ -d \"$MOUNT_DIR\" ]; then\n    sudo rm -rf \"$MOUNT_DIR\" > /dev/null 2>&1 || handle_error \"Failed to remove $MOUNT_DIR\"\nfi\n\n# Remove NGINX configuration files\n[ -f \"$VHOST_MAIN_FILE\" ] && sudo rm -f \"$VHOST_MAIN_FILE\" || handle_error \"Warning: $VHOST_MAIN_FILE not found.\"\n[ -f \"$VHOST_MAIN_LOCATION_FILE\" ] && sudo rm -f \"$VHOST_MAIN_LOCATION_FILE\" || handle_error \"Warning: $VHOST_MAIN_LOCATION_FILE not found.\"\n[ -f \"$VHOST_CONSOLE_FILE\" ] && sudo rm -f \"$VHOST_CONSOLE_FILE\" || handle_error \"Warning: $VHOST_CONSOLE_FILE not found.\"\n[ -f \"$VHOST_CONSOLE_LOCATION_FILE\" ] && sudo rm -f \"$VHOST_CONSOLE_LOCATION_FILE\" || handle_error \"Warning: $VHOST_CONSOLE_LOCATION_FILE not found.\"\n\n# Update status\necho \"suspended\" | sudo tee \"$STATUS_FILE\" > /dev/null\n\n# Success\necho \"success\"\nexit 0\n"
            }
          ]
        }
      },
      "typeVersion": 3.4,
      "alwaysOutputData": true
    },
    {
      "id": "87b7f7c2-7f7e-49e5-846c-3f92d436b5b6",
      "name": "Terminated",
      "type": "n8n-nodes-base.set",
      "onError": "continueRegularOutput",
      "position": [
        -220,
        -620
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "21f4453e-c136-4388-be90-1411ae78e8a5",
              "name": "sh",
              "type": "string",
              "value": "=#!/bin/bash\n\nDOMAIN=\"{{ $('API').item.json.body.domain }}\"\nCOMPOSE_DIR=\"{{ $('Parametrs').item.json.clients_dir }}/$DOMAIN\"\nCOMPOSE_FILE=\"$COMPOSE_DIR/docker-compose.yml\"\nSTATUS_FILE=\"$COMPOSE_DIR/status\"\nIMG_FILE=\"$COMPOSE_DIR/data.img\"\nNGINX_DIR=\"$COMPOSE_DIR/nginx\"\nVHOST_DIR=\"/opt/docker/nginx-proxy/nginx/vhost.d\"\n\nVHOST_MAIN_FILE=\"$VHOST_DIR/$DOMAIN\"\nVHOST_MAIN_LOCATION_FILE=\"$VHOST_DIR/$DOMAIN\"_location\nVHOST_CONSOLE_FILE=\"$VHOST_DIR/console.$DOMAIN\"\nVHOST_CONSOLE_LOCATION_FILE=\"$VHOST_DIR/console.$DOMAIN\"_location\nMOUNT_DIR=\"{{ $('Parametrs').item.json.mount_dir }}/$DOMAIN\"\n\n# Function to log an error, write to status file, and print to console\nhandle_error() {\n    STATUS_JSON=\"{\\\"status\\\": \\\"error\\\", \\\"message\\\": \\\"$1\\\"}\"\n    echo \"error: $1\"\n    exit 1\n}\n\n# Stop and remove the Docker containers\nif [ -f \"$COMPOSE_FILE\" ]; then\n    sudo docker-compose -f \"$COMPOSE_FILE\" down > /dev/null 2>&1\nfi\n\n# Remove the mount entry from /etc/fstab if it exists\nif grep -q \"$IMG_FILE\" /etc/fstab; then\n    sudo sed -i \"\\|$(printf '%s\\n' \"$IMG_FILE\" | sed 's/[.[\\*^$]/\\\\&/g')|d\" /etc/fstab\nfi\n\n# Unmount the image if it is still mounted\nif mount | grep -q \"$MOUNT_DIR\"; then\n    sudo umount \"$MOUNT_DIR\" > /dev/null 2>&1 || handle_error \"Failed to unmount $MOUNT_DIR\"\nfi\n\n# Remove all related directories and files\nfor item in \"$COMPOSE_DIR\" \"$VHOST_MAIN_FILE\" \"$VHOST_MAIN_LOCATION_FILE\" \"$VHOST_CONSOLE_FILE\" \"$VHOST_CONSOLE_LOCATION_FILE\"; do\n    if [ -e \"$item\" ]; then\n        sudo rm -rf \"$item\" || handle_error \"Failed to remove $item\"\n    fi\ndone\n\necho \"success\"\nexit 0\n"
            }
          ]
        }
      },
      "typeVersion": 3.4,
      "alwaysOutputData": true
    },
    {
      "id": "610dc730-9a2f-4fbf-bbbe-ce31d1494422",
      "name": "Unsuspend",
      "type": "n8n-nodes-base.set",
      "onError": "continueRegularOutput",
      "position": [
        -220,
        -800
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "21f4453e-c136-4388-be90-1411ae78e8a5",
              "name": "sh",
              "type": "string",
              "value": "=#!/bin/bash\n\nDOMAIN=\"{{ $('API').item.json.body.domain }}\"\nCOMPOSE_DIR=\"{{ $('Parametrs').item.json.clients_dir }}/$DOMAIN\"\nCOMPOSE_FILE=\"$COMPOSE_DIR/docker-compose.yml\"\nSTATUS_FILE=\"$COMPOSE_DIR/status\"\nIMG_FILE=\"$COMPOSE_DIR/data.img\"\nNGINX_DIR=\"$COMPOSE_DIR/nginx\"\nVHOST_DIR=\"/opt/docker/nginx-proxy/nginx/vhost.d\"\nMOUNT_DIR=\"{{ $('Parametrs').item.json.mount_dir }}/$DOMAIN\"\nDOCKER_COMPOSE_TEXT='{{ $('Deploy-docker-compose').item.json[\"docker-compose\"] }}'\n\nNGINX_MAIN_ACL_FILE=\"$NGINX_DIR/$DOMAIN\"_acl\n\nNGINX_MAIN_TEXT='{{ $('nginx').item.json['main'] }}'\nNGINX_MAIN_FILE=\"$NGINX_DIR/$DOMAIN\"\nVHOST_MAIN_FILE=\"$VHOST_DIR/$DOMAIN\"\n\nNGINX_MAIN_LOCATION_TEXT='{{ $('nginx').item.json['main_location'] }}'\nNGINX_MAIN_LOCATION_FILE=\"$NGINX_DIR/$DOMAIN\"_location\nVHOST_MAIN_LOCATION_FILE=\"$VHOST_DIR/$DOMAIN\"_location\n\nNGINX_CONSOLE_ACL_FILE=\"$NGINX_DIR/console.$DOMAIN\"_acl\n\nNGINX_CONSOLE_TEXT='{{ $('nginx').item.json['console'] }}'\nNGINX_CONSOLE_FILE=\"$NGINX_DIR/console.$DOMAIN\"\nVHOST_CONSOLE_FILE=\"$VHOST_DIR/console.$DOMAIN\"\n\nNGINX_CONSOLE_LOCATION_TEXT='{{ $('nginx').item.json['console_location'] }}'\nNGINX_CONSOLE_LOCATION_FILE=\"$NGINX_DIR/console.$DOMAIN\"_location\nVHOST_CONSOLE_LOCATION_FILE=\"$VHOST_DIR/console.$DOMAIN\"_location\n\nDISK_SIZE=\"{{ $('API').item.json.body.disk }}\"\n\n# Function to log an error, write to status file, and print to console\nhandle_error() {\n    STATUS_JSON=\"{\\\"status\\\": \\\"error\\\", \\\"message\\\": \\\"$1\\\"}\"\n    echo \"$STATUS_JSON\" | sudo tee \"$STATUS_FILE\" > /dev/null\n    echo \"error: $1\"\n    exit 1\n}\n\nupdate_nginx_acl() {\n    ACL_FILE=$1\n    LOCATION_FILE=$2\n    \n    if [ -s \"$ACL_FILE\" ]; then  # Проверяем, что файл существует и не пустой\n        VALID_LINES=$(grep -vE '^\\s*$' \"$ACL_FILE\")  # Убираем пустые строки\n        if [ -n \"$VALID_LINES\" ]; then  # Если есть непустые строки\n            while IFS= read -r line; do\n                echo \"allow $line;\" | sudo tee -a \"$LOCATION_FILE\" > /dev/null || handle_error \"Failed to update $LOCATION_FILE\"\n            done <<< \"$VALID_LINES\"\n            echo \"deny all;\" | sudo tee -a \"$LOCATION_FILE\" > /dev/null || handle_error \"Failed to update $LOCATION_FILE\"\n        fi\n    fi\n}\n\n# Create necessary directories with permissions\nfor dir in \"$COMPOSE_DIR\" \"$NGINX_DIR\" \"$MOUNT_DIR\"; do\n    sudo mkdir -p \"$dir\" || handle_error \"Failed to create $dir\"\n    sudo chmod -R 777 \"$dir\" || handle_error \"Failed to set permissions on $dir\"\ndone\n\n# Check if the image is already mounted using fstab\nif ! grep -q \"$IMG_FILE\" /etc/fstab; then\n    echo \"$IMG_FILE $MOUNT_DIR ext4 loop 0 0\" | sudo tee -a /etc/fstab > /dev/null || handle_error \"Failed to add fstab entry for $IMG_FILE\"\nfi\n\n# Apply the fstab changes and mount the image\nif ! mount | grep -q \"$MOUNT_DIR\"; then\n    sudo mount -a || handle_error \"Failed to mount image using fstab\"\nfi\n\n# Create docker-compose.yml file\necho \"$DOCKER_COMPOSE_TEXT\" | sudo tee \"$COMPOSE_FILE\" > /dev/null 2>&1 || handle_error \"Failed to create $COMPOSE_FILE\"\n\n# Create NGINX configuration files\necho \"$NGINX_MAIN_TEXT\" | sudo tee \"$NGINX_MAIN_FILE\" > /dev/null 2>&1 || handle_error \"Failed to create $NGINX_MAIN_FILE\"\necho \"$NGINX_MAIN_LOCATION_TEXT\" | sudo tee \"$NGINX_MAIN_LOCATION_FILE\" > /dev/null 2>&1 || handle_error \"Failed to create $NGINX_MAIN_FILE\"\n\necho \"$NGINX_CONSOLE_TEXT\" | sudo tee \"$NGINX_CONSOLE_FILE\" > /dev/null 2>&1 || handle_error \"Failed to create $NGINX_CONSOLE_FILE\"\necho \"$NGINX_CONSOLE_LOCATION_TEXT\" | sudo tee \"$NGINX_CONSOLE_LOCATION_FILE\" > /dev/null 2>&1 || handle_error \"Failed to create $NGINX_CONSOLE_LOCATION_FILE\"\n\n# Copy NGINX configuration files instead of creating symbolic links\nsudo cp -f \"$NGINX_MAIN_FILE\" \"$VHOST_MAIN_FILE\" || handle_error \"Failed to copy $NGINX_MAIN_FILE to $VHOST_MAIN_FILE\"\nsudo chmod 777 \"$VHOST_MAIN_FILE\" || handle_error \"Failed to set permissions on $VHOST_MAIN_FILE\"\n\nsudo cp -f \"$NGINX_MAIN_LOCATION_FILE\" \"$VHOST_MAIN_LOCATION_FILE\" || handle_error \"Failed to copy $NGINX_MAIN_LOCATION_FILE to $VHOST_MAIN_LOCATION_FILE\"\nsudo chmod 777 \"$VHOST_MAIN_LOCATION_FILE\" || handle_error \"Failed to set permissions on $VHOST_MAIN_LOCATION_FILE\"\n\nsudo cp -f \"$NGINX_CONSOLE_FILE\" \"$VHOST_CONSOLE_FILE\" || handle_error \"Failed to copy $NGINX_CONSOLE_FILE to $VHOST_CONSOLE_FILE\"\nsudo chmod 777 \"$VHOST_CONSOLE_FILE\" || handle_error \"Failed to set permissions on $VHOST_CONSOLE_FILE\"\n\nsudo cp -f \"$NGINX_CONSOLE_LOCATION_FILE\" \"$VHOST_CONSOLE_LOCATION_FILE\" || handle_error \"Failed to copy $NGINX_CONSOLE_LOCATION_FILE to $VHOST_CONSOLE_LOCATION_FILE\"\nsudo chmod 777 \"$VHOST_CONSOLE_LOCATION_FILE\" || handle_error \"Failed to set permissions on $VHOST_CONSOLE_LOCATION_FILE\"\n\nupdate_nginx_acl \"$NGINX_MAIN_ACL_FILE\" \"$VHOST_MAIN_LOCATION_FILE\"\nupdate_nginx_acl \"$NGINX_CONSOLE_ACL_FILE\" \"$VHOST_CONSOLE_LOCATION_FILE\"\n\n# Change to the compose directory\ncd \"$COMPOSE_DIR\" || handle_error \"Failed to change directory to $COMPOSE_DIR\"\n\n# Start Docker containers using docker-compose\n> error.log\nif ! sudo docker-compose up -d > error.log 2>&1; then\n    ERROR_MSG=$(tail -n 10 error.log)  # Read the last 10 lines from error.log\n    handle_error \"Docker-compose failed: $ERROR_MSG\"\nfi\n\n# If everything is successful, update the status file and print success message\necho \"active\" | sudo tee \"$STATUS_FILE\" > /dev/null\necho \"success\"\nexit 0\n"
            }
          ]
        }
      },
      "typeVersion": 3.4,
      "alwaysOutputData": true
    },
    {
      "id": "8d6893c3-9597-43fe-bbec-ba3c55d2c220",
      "name": "Mount Disk",
      "type": "n8n-nodes-base.set",
      "onError": "continueRegularOutput",
      "position": [
        -1180,
        360
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "21f4453e-c136-4388-be90-1411ae78e8a5",
              "name": "sh",
              "type": "string",
              "value": "=#!/bin/bash\n\nCOMPOSE_DIR=\"{{ $('Parametrs').item.json.clients_dir }}/{{ $('API').item.json.body.domain }}\"\nIMG_FILE=\"$COMPOSE_DIR/data.img\"\nMOUNT_DIR=\"{{ $('Parametrs').item.json.mount_dir }}/{{ $('API').item.json.body.domain }}\"\n\n# Function to log an error, write to status file, and print to console\nhandle_error() {\n    echo \"error: $1\"\n    exit 1\n}\n\n# Create necessary directories with permissions\nsudo mkdir -p \"$MOUNT_DIR\" > /dev/null 2>&1 || handle_error \"Failed to create $MOUNT_DIR\"\nsudo chmod 777 \"$MOUNT_DIR\" > /dev/null 2>&1 || handle_error \"Failed to set permissions on $MOUNT_DIR\"\n\nif df -h | grep -q \"$MOUNT_DIR\"; then\n    handle_error \"The file $IMG_FILE is mounted to $MOUNT_DIR\"\nfi\n\nif ! grep -q \"$IMG_FILE\" /etc/fstab; then\n    echo \"$IMG_FILE $MOUNT_DIR ext4 loop 0 0\" | sudo tee -a /etc/fstab > /dev/null || handle_error \"Failed to add entry to /etc/fstab\"\nfi\n\nsudo mount -a || handle_error \"Failed to mount entries from /etc/fstab\"\n\necho \"success\"\n\nexit 0\n"
            }
          ]
        }
      },
      "typeVersion": 3.4,
      "alwaysOutputData": true
    },
    {
      "id": "1b2182c6-7080-4b09-9699-2ba7c3292913",
      "name": "Unmount Disk",
      "type": "n8n-nodes-base.set",
      "onError": "continueRegularOutput",
      "position": [
        -1060,
        460
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "21f4453e-c136-4388-be90-1411ae78e8a5",
              "name": "sh",
              "type": "string",
              "value": "=#!/bin/bash\n\nCOMPOSE_DIR=\"{{ $('Parametrs').item.json.clients_dir }}/{{ $('API').item.json.body.domain }}\"\nIMG_FILE=\"$COMPOSE_DIR/data.img\"\nMOUNT_DIR=\"{{ $('Parametrs').item.json.mount_dir }}/{{ $('API').item.json.body.domain }}\"\n\n# Function to log an error, write to status file, and print to console\nhandle_error() {\n    echo \"error: $1\"\n    exit 1\n}\n\nif ! df -h | grep -q \"$MOUNT_DIR\"; then\n    handle_error \"The file $IMG_FILE is not mounted to $MOUNT_DIR\"\nfi\n\n# Remove the mount entry from /etc/fstab if it exists\nif grep -q \"$IMG_FILE\" /etc/fstab; then\n    sudo sed -i \"\\|$(printf '%s\\n' \"$IMG_FILE\" | sed 's/[.[\\*^$]/\\\\&/g')|d\" /etc/fstab\nfi\n\n# Unmount the image if it is mounted (using fstab)\nif mount | grep -q \"$MOUNT_DIR\"; then\n    sudo umount \"$MOUNT_DIR\" > /dev/null 2>&1 || handle_error \"Failed to unmount $MOUNT_DIR\"\nfi\n\n# Remove the mount directory (if needed)\nif ! sudo rm -rf \"$MOUNT_DIR\" > /dev/null 2>&1; then\n    handle_error \"Failed to remove $MOUNT_DIR\"\nfi\n\necho \"success\"\n\nexit 0\n"
            }
          ]
        }
      },
      "typeVersion": 3.4,
      "alwaysOutputData": true
    },
    {
      "id": "dd0cd3d9-876e-485c-94ed-f69e6f26c62b",
      "name": "Log",
      "type": "n8n-nodes-base.set",
      "onError": "continueRegularOutput",
      "position": [
        -1180,
        -100
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "21f4453e-c136-4388-be90-1411ae78e8a5",
              "name": "sh",
              "type": "string",
              "value": "=#!/bin/bash\n\nCONTAINER_NAME=\"{{ $('API').item.json.body.domain }}\"\nLOGS_JSON=\"{}\"\n\n# Function to return error in JSON format\nhandle_error() {\n    echo \"{\\\"status\\\": \\\"error\\\", \\\"message\\\": \\\"$1\\\"}\"\n    exit 1\n}\n\n# Check if the container exists\nif ! sudo docker ps -a | grep -q \"$CONTAINER_NAME\" > /dev/null 2>&1; then\n    handle_error \"Container $CONTAINER_NAME not found\"\nfi\n\n# Get logs of the container\nLOGS=$(sudo docker logs --tail 1000 \"$CONTAINER_NAME\" 2>&1)\nif [ $? -ne 0 ]; then\n    handle_error \"Failed to retrieve logs for $CONTAINER_NAME\"\nfi\n\n# Escape double quotes in logs for valid JSON\nLOGS_ESCAPED=$(echo \"$LOGS\" | sed 's/\"/\\\\\"/g' | sed ':a;N;$!ba;s/\\n/\\\\n/g')\n\n# Format logs as JSON\nLOGS_JSON=\"{\\\"logs\\\": \\\"$LOGS_ESCAPED\\\"}\"\n\necho \"$LOGS_JSON\"\nexit 0"
            }
          ]
        }
      },
      "typeVersion": 3.4,
      "alwaysOutputData": true
    },
    {
      "id": "64e41e91-62b3-4346-874b-e952201fecb5",
      "name": "ChangePackage",
      "type": "n8n-nodes-base.set",
      "onError": "continueRegularOutput",
      "position": [
        -220,
        -440
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "21f4453e-c136-4388-be90-1411ae78e8a5",
              "name": "sh",
              "type": "string",
              "value": "=#!/bin/bash\n\n# Get values for variables from templates\nDOMAIN=\"{{ $('API').item.json.body.domain }}\"\nCOMPOSE_DIR=\"{{ $('Parametrs').item.json.clients_dir }}/$DOMAIN\"\nCOMPOSE_FILE=\"$COMPOSE_DIR/docker-compose.yml\"\nSTATUS_FILE=\"$COMPOSE_DIR/status\"\nIMG_FILE=\"$COMPOSE_DIR/data.img\"\nNGINX_DIR=\"$COMPOSE_DIR/nginx\"\nVHOST_DIR=\"/opt/docker/nginx-proxy/nginx/vhost.d\"\nMOUNT_DIR=\"{{ $('Parametrs').item.json.mount_dir }}/$DOMAIN\"\nDOCKER_COMPOSE_TEXT='{{ $('Deploy-docker-compose').item.json[\"docker-compose\"] }}'\n\nNGINX_MAIN_TEXT='{{ $('nginx').item.json['main'] }}'\nNGINX_MAIN_FILE=\"$NGINX_DIR/$DOMAIN\"\nVHOST_MAIN_FILE=\"$VHOST_DIR/$DOMAIN\"\n\nNGINX_MAIN_LOCATION_TEXT='{{ $('nginx').item.json['main_location'] }}'\nNGINX_MAIN_LOCATION_FILE=\"$NGINX_DIR/$DOMAIN\"_location\nVHOST_MAIN_LOCATION_FILE=\"$VHOST_DIR/$DOMAIN\"_location\n\nNGINX_CONSOLE_TEXT='{{ $('nginx').item.json['console'] }}'\nNGINX_CONSOLE_FILE=\"$NGINX_DIR/console.$DOMAIN\"\nVHOST_CONSOLE_FILE=\"$VHOST_DIR/console.$DOMAIN\"\n\nNGINX_CONSOLE_LOCATION_TEXT='{{ $('nginx').item.json['console_location'] }}'\nNGINX_CONSOLE_LOCATION_FILE=\"$NGINX_DIR/console.$DOMAIN\"_location\nVHOST_CONSOLE_LOCATION_FILE=\"$VHOST_DIR/console.$DOMAIN\"_location\n\nDISK_SIZE=\"{{ $('API').item.json.body.disk }}\"\n\n# Function to log an error, write to status file, and print to console\nhandle_error() {\n    STATUS_JSON=\"{\\\"status\\\": \\\"error\\\", \\\"message\\\": \\\"$1\\\"}\"\n    echo \"$STATUS_JSON\" | sudo tee \"$STATUS_FILE\" > /dev/null\n    echo \"error: $1\"\n    exit 1\n}\n\n# Check if the compose file exists before stopping the container\nif [ -f \"$COMPOSE_FILE\" ]; then\n    sudo docker-compose -f \"$COMPOSE_FILE\" down > /dev/null 2>&1 || handle_error \"Failed to stop containers\"\nelse\n    handle_error \"docker-compose.yml not found\"\nfi\n\n# Unmount the image if it is currently mounted\nif mount | grep -q \"$MOUNT_DIR\"; then\n    sudo umount \"$MOUNT_DIR\" > /dev/null 2>&1 || handle_error \"Failed to unmount $MOUNT_DIR\"\nfi\n\n# Create docker-compose.yml file\necho \"$DOCKER_COMPOSE_TEXT\" | sudo tee \"$COMPOSE_FILE\" > /dev/null 2>&1 || handle_error \"Failed to create $COMPOSE_FILE\"\n\n# Create NGINX configuration files\necho \"$NGINX_MAIN_TEXT\" | sudo tee \"$NGINX_MAIN_FILE\" > /dev/null 2>&1 || handle_error \"Failed to create $NGINX_MAIN_FILE\"\necho \"$NGINX_MAIN_LOCATION_TEXT\" | sudo tee \"$NGINX_MAIN_LOCATION_FILE\" > /dev/null 2>&1 || handle_error \"Failed to create $NGINX_MAIN_LOCATION_FILE\"\n\necho \"$NGINX_CONSOLE_TEXT\" | sudo tee \"$NGINX_CONSOLE_FILE\" > /dev/null 2>&1 || handle_error \"Failed to create $NGINX_CONSOLE_FILE\"\necho \"$NGINX_CONSOLE_LOCATION_TEXT\" | sudo tee \"$NGINX_CONSOLE_LOCATION_FILE\" > /dev/null 2>&1 || handle_error \"Failed to create $NGINX_CONSOLE_LOCATION_FILE\"\n\n# Resize the disk image if it exists\nif [ -f \"$IMG_FILE\" ]; then\n    sudo truncate -s \"$DISK_SIZE\"G \"$IMG_FILE\" > /dev/null 2>&1 || handle_error \"Failed to resize $IMG_FILE (truncate)\"\n    sudo e2fsck -fy \"$IMG_FILE\" > /dev/null 2>&1 || handle_error \"Filesystem check failed on $IMG_FILE\"\n    sudo resize2fs \"$IMG_FILE\" > /dev/null 2>&1 || handle_error \"Failed to resize filesystem on $IMG_FILE\"\nelse\n    handle_error \"Disk image $IMG_FILE does not exist\"\nfi\n\n# Mount the disk only if it is not already mounted\nif ! mount | grep -q \"$MOUNT_DIR\"; then\n    sudo mount -a || handle_error \"Failed to mount entries from /etc/fstab\"\nfi\n\n# Change to the compose directory\ncd \"$COMPOSE_DIR\" > /dev/null 2>&1 || handle_error \"Failed to change directory to $COMPOSE_DIR\"\n\n# Copy NGINX configuration files instead of creating symbolic links\nsudo cp -f \"$NGINX_MAIN_FILE\" \"$VHOST_MAIN_FILE\" || handle_error \"Failed to copy $NGINX_MAIN_FILE to $VHOST_MAIN_FILE\"\nsudo chmod 777 \"$VHOST_MAIN_FILE\" || handle_error \"Failed to set permissions on $VHOST_MAIN_FILE\"\n\nsudo cp -f \"$NGINX_MAIN_LOCATION_FILE\" \"$VHOST_MAIN_LOCATION_FILE\" || handle_error \"Failed to copy $NGINX_MAIN_LOCATION_FILE to $VHOST_MAIN_LOCATION_FILE\"\nsudo chmod 777 \"$VHOST_MAIN_LOCATION_FILE\" || handle_error \"Failed to set permissions on $VHOST_MAIN_LOCATION_FILE\"\n\nsudo cp -f \"$NGINX_CONSOLE_FILE\" \"$VHOST_CONSOLE_FILE\" || handle_error \"Failed to copy $NGINX_CONSOLE_FILE to $VHOST_CONSOLE_FILE\"\nsudo chmod 777 \"$VHOST_CONSOLE_FILE\" || handle_error \"Failed to set permissions on $VHOST_CONSOLE_FILE\"\n\nsudo cp -f \"$NGINX_CONSOLE_LOCATION_FILE\" \"$VHOST_CONSOLE_LOCATION_FILE\" || handle_error \"Failed to copy $NGINX_CONSOLE_LOCATION_FILE to $VHOST_CONSOLE_LOCATION_FILE\"\nsudo chmod 777 \"$VHOST_CONSOLE_LOCATION_FILE\" || handle_error \"Failed to set permissions on $VHOST_CONSOLE_LOCATION_FILE\"\n\n# Start Docker containers using docker-compose\nif ! sudo docker-compose up -d > /dev/null 2>error.log; then\n    ERROR_MSG=$(tail -n 10 error.log)  # Read the last 10 lines from error.log\n    handle_error \"Docker-compose failed: $ERROR_MSG\"\nfi\n\n# Update status file\necho \"active\" | sudo tee \"$STATUS_FILE\" > /dev/null\n\necho \"success\"\n\nexit 0\n"
            }
          ]
        }
      },
      "typeVersion": 3.4,
      "alwaysOutputData": true
    },
    {
      "id": "d7688118-55bb-4934-aac7-507bd3a3e956",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -2640,
        -1280
      ],
      "parameters": {
        "color": 6,
        "width": 639,
        "height": 909,
        "content": "## 👋 Welcome to PUQ Docker MinIO deploy!\n## Template for MinIO: API Backend for WHMCS/WISECP by PUQcloud\n\nv.1\n\nThis is an n8n template that creates an API backend for the WHMCS/WISECP module developed by PUQcloud.\n\n## Setup Instructions\n\n### 1. Configure API Webhook and SSH Access\n- Create a Credential (Basic Auth) for the **Webhook API Block** in n8n.\n- Create a Credential for **SSH access** to a server with Docker installed (**SSH Block**).\n\n### 2. Modify Template Parameters\nIn the **Parameters** block of the template, update the following settings:\n\n- `server_domain` – must match the domain of the WHMCS/WISECP Docker server.\n- `clients_dir` – directory where user data related to Docker and disks will be stored.\n- `mount_dir` – default mount point for the container disk (recommended not to change).\n\n**Do not modify** the following technical parameters:\n\n- `screen_left`\n- `screen_right`\n\n## Additional Resources\n- Full documentation: [https://doc.puq.info/books/docker-minio-whmcs-module](https://doc.puq.info/books/docker-minio-whmcs-module)\n- WHMCS module: [https://puqcloud.com/whmcs-module-docker-minio.php](https://puqcloud.com/whmcs-module-docker-minio.php)\n\n"
      },
      "typeVersion": 1
    },
    {
      "id": "e8b68657-ae60-4558-8ea0-768dba92fcba",
      "name": "Deploy-docker-compose",
      "type": "n8n-nodes-base.set",
      "position": [
        -1200,
        -1360
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "21f4453e-c136-4388-be90-1411ae78e8a5",
              "name": "docker-compose",
              "type": "string",
              "value": "=version: \"3\"\n\nservices:\n  {{ $('API').item.json.body.domain }}:\n    image: minio/minio\n    restart: unless-stopped\n    container_name: {{ $('API').item.json.body.domain }}\n    command: server /data --console-address \":9001\"\n    environment:\n      MINIO_ROOT_USER: {{ $('API').item.json.body.username }}\n      MINIO_ROOT_PASSWORD: {{ $('API').item.json.body.password }}\n      MINIO_BROWSER_REDIRECT_URL: https://console.{{ $('API').item.json.body.domain }}\n      LETSENCRYPT_HOST: {{ $('API').item.json.body.domain }},console.{{ $('API').item.json.body.domain }}\n      VIRTUAL_HOST_MULTIPORTS: |-\n          {{ $('API').item.json.body.domain }}:\n            \"/\":\n              port: 9000\n          console.{{ $('API').item.json.body.domain }}:\n            \"/\":\n              port: 9001\n    volumes:\n      - \"{{ $('Parametrs').item.json.mount_dir }}/{{ $('API').item.json.body.domain }}/data:/data\"\n    networks:\n      - nginx-proxy_web\n    mem_limit: \"{{ $('API').item.json.body.ram }}G\"\n    cpus: \"{{ $('API').item.json.body.cpu }}\"\n\nnetworks:\n  nginx-proxy_web:\n    external: true\n"
            }
          ]
        }
      },
      "typeVersion": 3.4,
      "alwaysOutputData": true
    },
    {
      "id": "938520b1-aae6-4fe7-ac8e-e888f0793c8a",
      "name": "Version",
      "type": "n8n-nodes-base.set",
      "onError": "continueRegularOutput",
      "position": [
        -1080,
        1300
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "21f4453e-c136-4388-be90-1411ae78e8a5",
              "name": "sh",
              "type": "string",
              "value": "=#!/bin/bash\n\nCONTAINER_NAME=\"{{ $('API').item.json.body.domain }}\"\nVERSION_JSON=\"{}\"\n\n# Function to return error in JSON format\nhandle_error() {\n    echo \"{\\\"status\\\": \\\"error\\\", \\\"message\\\": \\\"$1\\\"}\"\n    exit 1\n}\n\n# Check if the container exists\nif ! sudo docker ps -a | grep -q \"$CONTAINER_NAME\" > /dev/null 2>&1; then\n    handle_error \"Container $CONTAINER_NAME not found\"\nfi\n\n# Get the MinIO version from the container (first line only)\nVERSION=$(sudo docker exec \"$CONTAINER_NAME\" minio -v | head -n 1)\n\n# Extract just the version string\nVERSION_CLEAN=$(echo \"$VERSION\" | awk '{print $3}')\n\n# Format version as JSON\nVERSION_JSON=\"{\\\"version\\\": \\\"$VERSION_CLEAN\\\"}\"\n\necho \"$VERSION_JSON\"\nexit 0\n"
            }
          ]
        }
      },
      "typeVersion": 3.4,
      "alwaysOutputData": true
    },
    {
      "id": "d83a8249-9ad9-4772-bb1b-5484ebeb4b81",
      "name": "Users",
      "type": "n8n-nodes-base.set",
      "onError": "continueRegularOutput",
      "position": [
        -1140,
        1460
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "21f4453e-c136-4388-be90-1411ae78e8a5",
              "name": "sh",
              "type": "string",
              "value": "=#!/bin/bash\n\nCONTAINER_NAME=\"{{ $('API').item.json.body.domain }}\"\nMINIO_USERNAME=\"{{ $('API').item.json.body.username }}\"\nMINIO_PASSWORD=\"{{ $('API').item.json.body.password }}\"\n\n# Function to return error in JSON format\nhandle_error() {\n    echo \"{\\\"status\\\": \\\"error\\\", \\\"message\\\": \\\"$1\\\"}\"\n    exit 1\n}\n\n# Check if the container exists\nif ! sudo docker ps -a | grep -q \"$CONTAINER_NAME\" > /dev/null 2>&1; then\n    handle_error \"Container $CONTAINER_NAME not found\"\nfi\n\n# Set alias for MinIO client\nsudo docker exec \"$CONTAINER_NAME\" mc alias set local http://localhost:9000 \"$MINIO_USERNAME\" \"$MINIO_PASSWORD\" > /dev/null 2>&1\n\n# Get user list and format it correctly as JSON array\nUSERS_JSON=$(sudo docker exec \"$CONTAINER_NAME\" mc admin user list local --json | jq -s '.')\n\n# Check if USERS_JSON is empty\nif [ -z \"$USERS_JSON\" ]; then\n    handle_error \"Failed to retrieve user list for $CONTAINER_NAME\"\nfi\n\n# Wrap in a JSON object\nJSON=\"{\\\"users\\\": $USERS_JSON}\"\n\necho \"$JSON\"\nexit 0\n"
            }
          ]
        }
      },
      "typeVersion": 3.4,
      "alwaysOutputData": true
    },
    {
      "id": "ba9b26be-31b6-47c9-85c1-719f346abc1a",
      "name": "If1",
      "type": "n8n-nodes-base.if",
      "position": [
        -1780,
        -1260
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
              "id": "8602bd4c-9693-4d5f-9e7d-5ee62210baca",
              "operator": {
                "name": "filter.operator.equals",
                "type": "string",
                "operation": "equals"
              },
              "leftValue": "={{ $('API').item.json.body.command }}",
              "rightValue": "create"
            },
            {
              "id": "1c630b59-0e5a-441d-8aa5-70b31338d897",
              "operator": {
                "name": "filter.operator.equals",
                "type": "string",
                "operation": "equals"
              },
              "leftValue": "={{ $('API').item.json.body.command }}",
              "rightValue": "change_package"
            },
            {
              "id": "b3eb7052-a70f-438e-befd-8c5240df32c7",
              "operator": {
                "name": "filter.operator.equals",
                "type": "string",
                "operation": "equals"
              },
              "leftValue": "={{ $('API').item.json.body.command }}",
              "rightValue": "unsuspend"
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "c08cfbd4-ef9a-4430-8a03-41ae209a3c92",
      "name": "MinIO",
      "type": "n8n-nodes-base.switch",
      "position": [
        -1680,
        1380
      ],
      "parameters": {
        "rules": {
          "values": [
            {
              "outputKey": "version",
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
                    "id": "66ad264d-5393-410c-bfa3-011ab8eb234a",
                    "operator": {
                      "name": "filter.operator.equals",
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $('API').item.json.body.command }}",
                    "rightValue": "app_version"
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "users",
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
                    "id": "b48957a0-22c0-4ac0-82ef-abd9e7ab0207",
                    "operator": {
                      "name": "filter.operator.equals",
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $('API').item.json.body.command }}",
                    "rightValue": "app_users"
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
      "id": "d75c83ca-c106-4b96-9db7-9f3ef1e20453",
      "name": "nginx",
      "type": "n8n-nodes-base.set",
      "position": [
        -1420,
        -1360
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "21f4453e-c136-4388-be90-1411ae78e8a5",
              "name": "main",
              "type": "string",
              "value": "=ignore_invalid_headers off;\nclient_max_body_size 0;\nproxy_buffering off;\nproxy_request_buffering off;"
            },
            {
              "id": "6507763a-21d4-4ff0-84d2-5dc9d21b7430",
              "name": "main_location",
              "type": "string",
              "value": "=# Custom header\nproxy_set_header Host $http_host;\nproxy_set_header X-Real-IP $remote_addr;\nproxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;\nproxy_set_header X-Forwarded-Proto $scheme;\n\nproxy_connect_timeout 300;\n# Default is HTTP/1, keepalive is only enabled in HTTP/1.1\nproxy_http_version 1.1;\nproxy_set_header Connection \"\";\nchunked_transfer_encoding off;\n"
            },
            {
              "id": "d00aa07a-0641-43ef-8fd2-5fb9ef62e313",
              "name": "console",
              "type": "string",
              "value": "=ignore_invalid_headers off;\nclient_max_body_size 0;\nproxy_buffering off;\nproxy_request_buffering off;"
            },
            {
              "id": "c00fb803-8b9f-4aca-a1b1-2e3da42fc8d1",
              "name": "console_location",
              "type": "string",
              "value": "=# Custom header\nproxy_set_header Host $http_host;\nproxy_set_header X-Real-IP $remote_addr;\nproxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;\nproxy_set_header X-Forwarded-Proto $scheme;\nproxy_set_header X-NginX-Proxy true;\n\nreal_ip_header X-Real-IP;\nproxy_connect_timeout 300;\nproxy_http_version 1.1;\nproxy_set_header Upgrade $http_upgrade;\nproxy_set_header Connection \"upgrade\";\n  \nchunked_transfer_encoding off;"
            }
          ]
        }
      },
      "typeVersion": 3.4,
      "alwaysOutputData": true
    },
    {
      "id": "70c2cb4d-af9d-4003-8aaf-e5800580552b",
      "name": "Container Stat",
      "type": "n8n-nodes-base.switch",
      "position": [
        -1680,
        -240
      ],
      "parameters": {
        "rules": {
          "values": [
            {
              "outputKey": "inspect",
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
                    "id": "66ad264d-5393-410c-bfa3-011ab8eb234a",
                    "operator": {
                      "name": "filter.operator.equals",
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $('API').item.json.body.command }}",
                    "rightValue": "container_information_inspect"
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "stats",
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
                    "id": "b48957a0-22c0-4ac0-82ef-abd9e7ab0207",
                    "operator": {
                      "name": "filter.operator.equals",
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $('API').item.json.body.command }}",
                    "rightValue": "container_information_stats"
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "log",
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
                    "id": "50ede522-af22-4b7a-b1fd-34b27fd3fadd",
                    "operator": {
                      "name": "filter.operator.equals",
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $('API').item.json.body.command }}",
                    "rightValue": "container_log"
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
      "id": "0bb2aeeb-8279-4f13-827f-a6559ef805b1",
      "name": "GET ACL",
      "type": "n8n-nodes-base.set",
      "onError": "continueRegularOutput",
      "position": [
        -1180,
        560
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "21f4453e-c136-4388-be90-1411ae78e8a5",
              "name": "sh",
              "type": "string",
              "value": "=#!/bin/bash\n\n# Get values for variables from templates\nDOMAIN=\"{{ $('API').item.json.body.domain }}\"\nCOMPOSE_DIR=\"{{ $('Parametrs').item.json.clients_dir }}/$DOMAIN\"\nNGINX_DIR=\"$COMPOSE_DIR/nginx\"\n\nNGINX_MAIN_ACL_FILE=\"$NGINX_DIR/$DOMAIN\"_acl\nNGINX_CONSOLE_ACL_FILE=\"$NGINX_DIR/console.$DOMAIN\"_acl\n\n# Function to log an error and exit\nhandle_error() {\n    echo \"error: $1\"\n    exit 1\n}\n\n# Read files if they exist, else assign empty array\nif [[ -f \"$NGINX_CONSOLE_ACL_FILE\" ]]; then\n    WEB_CONSOLE_IPS=$(cat \"$NGINX_CONSOLE_ACL_FILE\" | jq -R -s 'split(\"\\n\") | map(select(length > 0))')\nelse\n    WEB_CONSOLE_IPS=\"[]\"\nfi\n\nif [[ -f \"$NGINX_MAIN_ACL_FILE\" ]]; then\n    REST_API_IPS=$(cat \"$NGINX_MAIN_ACL_FILE\" | jq -R -s 'split(\"\\n\") | map(select(length > 0))')\nelse\n    REST_API_IPS=\"[]\"\nfi\n\n# Output JSON\necho \"{ \\\"web_console_ips\\\": $WEB_CONSOLE_IPS, \\\"rest_api_ips\\\": $REST_API_IPS }\"\n\nexit 0\n"
            }
          ]
        }
      },
      "typeVersion": 3.4,
      "alwaysOutputData": true
    },
    {
      "id": "9603bee0-de6f-46bf-97d4-f7a2a4d27514",
      "name": "SET ACL",
      "type": "n8n-nodes-base.set",
      "onError": "continueRegularOutput",
      "position": [
        -1060,
        700
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "21f4453e-c136-4388-be90-1411ae78e8a5",
              "name": "sh",
              "type": "string",
              "value": "=#!/bin/bash\n\n# Get values for variables from templates\nDOMAIN=\"{{ $('API').item.json.body.domain }}\"\nCOMPOSE_DIR=\"{{ $('Parametrs').item.json.clients_dir }}/$DOMAIN\"\nNGINX_DIR=\"$COMPOSE_DIR/nginx\"\nVHOST_DIR=\"/opt/docker/nginx-proxy/nginx/vhost.d\"\n\nNGINX_MAIN_ACL_FILE=\"$NGINX_DIR/$DOMAIN\"_acl\nNGINX_MAIN_ACL_TEXT=\"{{ $('API').item.json.body.rest_api_ips }}\"\nVHOST_MAIN_LOCATION_FILE=\"$VHOST_DIR/$DOMAIN\"_location\nNGINX_MAIN_LOCATION_FILE=\"$NGINX_DIR/$DOMAIN\"_location\n\nNGINX_CONSOLE_ACL_FILE=\"$NGINX_DIR/console.$DOMAIN\"_acl\nNGINX_CONSOLE_ACL_TEXT=\"{{ $('API').item.json.body.web_console_ips }}\"\nVHOST_CONSOLE_LOCATION_FILE=\"$VHOST_DIR/console.$DOMAIN\"_location\nNGINX_CONSOLE_LOCATION_FILE=\"$NGINX_DIR/console.$DOMAIN\"_location\n\n# Function to log an error and exit\nhandle_error() {\n    echo \"error: $1\"\n    exit 1\n}\n\nupdate_nginx_acl() {\n    ACL_FILE=$1\n    LOCATION_FILE=$2\n    \n    if [ -s \"$ACL_FILE\" ]; then\n        VALID_LINES=$(grep -vE '^\\s*$' \"$ACL_FILE\")\n        if [ -n \"$VALID_LINES\" ]; then\n            while IFS= read -r line; do\n                echo \"allow $line;\" | sudo tee -a \"$LOCATION_FILE\" > /dev/null || handle_error \"Failed to update $LOCATION_FILE\"\n            done <<< \"$VALID_LINES\"\n            echo \"deny all;\" | sudo tee -a \"$LOCATION_FILE\" > /dev/null || handle_error \"Failed to update $LOCATION_FILE\"\n        fi\n    fi\n}\n\n# Create or overwrite the file with the content from variables\necho \"$NGINX_MAIN_ACL_TEXT\" | sudo tee \"$NGINX_MAIN_ACL_FILE\" > /dev/null\necho \"$NGINX_CONSOLE_ACL_TEXT\" | sudo tee \"$NGINX_CONSOLE_ACL_FILE\" > /dev/null\n\nsudo cp -f \"$NGINX_MAIN_LOCATION_FILE\" \"$VHOST_MAIN_LOCATION_FILE\" || handle_error \"Failed to copy $NGINX_MAIN_LOCATION_FILE to $VHOST_MAIN_LOCATION_FILE\"\nsudo chmod 777 \"$VHOST_MAIN_LOCATION_FILE\" || handle_error \"Failed to set permissions on $VHOST_MAIN_LOCATION_FILE\"\n\nsudo cp -f \"$NGINX_CONSOLE_LOCATION_FILE\" \"$VHOST_CONSOLE_LOCATION_FILE\" || handle_error \"Failed to copy $NGINX_CONSOLE_LOCATION_FILE to $VHOST_CONSOLE_LOCATION_FILE\"\nsudo chmod 777 \"$VHOST_CONSOLE_LOCATION_FILE\" || handle_error \"Failed to set permissions on $VHOST_CONSOLE_LOCATION_FILE\"\n\nupdate_nginx_acl \"$NGINX_MAIN_ACL_FILE\" \"$VHOST_MAIN_LOCATION_FILE\"\nupdate_nginx_acl \"$NGINX_CONSOLE_ACL_FILE\" \"$VHOST_CONSOLE_LOCATION_FILE\"\n\n# Reload Nginx with sudo\nif sudo docker exec nginx-proxy nginx -s reload; then\n    echo \"success\"\nelse\n    handle_error \"Failed to reload Nginx.\"\nfi\n\nexit 0\n"
            }
          ]
        }
      },
      "typeVersion": 3.4,
      "alwaysOutputData": true
    },
    {
      "id": "325e6cfc-f28e-490e-84a0-d8153e1c9fc9",
      "name": "GET NET",
      "type": "n8n-nodes-base.set",
      "onError": "continueRegularOutput",
      "position": [
        -1180,
        840
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "21f4453e-c136-4388-be90-1411ae78e8a5",
              "name": "sh",
              "type": "string",
              "value": "=#!/bin/bash\n\n# Get values for variables from templates\nDOMAIN=\"{{ $('API').item.json.body.domain }}\"\nCOMPOSE_DIR=\"{{ $('Parametrs').item.json.clients_dir }}/$DOMAIN\"\nNGINX_DIR=\"$COMPOSE_DIR/nginx\"\nNET_IN_FILE=\"$COMPOSE_DIR/net_in\"\nNET_OUT_FILE=\"$COMPOSE_DIR/net_out\"\n\n# Function to log an error and exit\nhandle_error() {\n    echo \"error: $1\"\n    exit 1\n}\n\n# Get current network statistics from container\nSTATS=$(sudo docker exec \"$DOMAIN\" cat /proc/net/dev | grep eth0) || handle_error \"Failed to get network stats\"\nNET_IN_NEW=$(echo \"$STATS\" | awk '{print $2}')  # RX bytes (received)\nNET_OUT_NEW=$(echo \"$STATS\" | awk '{print $10}') # TX bytes (transmitted)\n\n# Ensure directory exists\nmkdir -p \"$COMPOSE_DIR\"\n\n# Read old values, create files if they don't exist\nif [[ -f \"$NET_IN_FILE\" ]]; then\n    NET_IN_OLD=$(sudo cat \"$NET_IN_FILE\")\nelse\n    NET_IN_OLD=0\nfi\n\nif [[ -f \"$NET_OUT_FILE\" ]]; then\n    NET_OUT_OLD=$(sudo cat \"$NET_OUT_FILE\")\nelse\n    NET_OUT_OLD=0\nfi\n\n# Save new values\necho \"$NET_IN_NEW\" | sudo tee \"$NET_IN_FILE\" > /dev/null\necho \"$NET_OUT_NEW\" | sudo tee \"$NET_OUT_FILE\" > /dev/null\n\n# Output JSON\necho \"{ \\\"net_in_new\\\": $NET_IN_NEW, \\\"net_out_new\\\": $NET_OUT_NEW, \\\"net_in_old\\\": $NET_IN_OLD, \\\"net_out_old\\\": $NET_OUT_OLD }\"\n\nexit 0\n"
            }
          ]
        }
      },
      "typeVersion": 3.4,
      "alwaysOutputData": true
    }
  ],
  "active": true,
  "pinData": {},
  "settings": {
    "timezone": "America/Winnipeg",
    "executionOrder": "v1"
  },
  "versionId": "930dd393-6eff-43d5-8446-30ba19fce16d",
  "connections": {
    "If": {
      "main": [
        [
          {
            "node": "Container Stat",
            "type": "main",
            "index": 0
          },
          {
            "node": "Container Actions",
            "type": "main",
            "index": 0
          },
          {
            "node": "MinIO",
            "type": "main",
            "index": 0
          },
          {
            "node": "If1",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "422-Invalid server domain",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "API": {
      "main": [
        [
          {
            "node": "Parametrs",
            "type": "main",
            "index": 0
          }
        ],
        []
      ]
    },
    "If1": {
      "main": [
        [
          {
            "node": "nginx",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Service Actions",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Log": {
      "main": [
        [
          {
            "node": "SSH",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "SSH": {
      "main": [
        [
          {
            "node": "Code1",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Code1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Stat": {
      "main": [
        [
          {
            "node": "SSH",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Stop": {
      "main": [
        [
          {
            "node": "SSH",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Code1": {
      "main": [
        [
          {
            "node": "API answer",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "MinIO": {
      "main": [
        [
          {
            "node": "Version",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Users",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Start": {
      "main": [
        [
          {
            "node": "SSH",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Users": {
      "main": [
        [
          {
            "node": "SSH",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "nginx": {
      "main": [
        [
          {
            "node": "Deploy-docker-compose",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Deploy": {
      "main": [
        [
          {
            "node": "SSH",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "GET ACL": {
      "main": [
        [
          {
            "node": "SSH",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "GET NET": {
      "main": [
        [
          {
            "node": "SSH",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Inspect": {
      "main": [
        [
          {
            "node": "SSH",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "SET ACL": {
      "main": [
        [
          {
            "node": "SSH",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Suspend": {
      "main": [
        [
          {
            "node": "SSH",
            "type": "main",
            "index": 0
          }
        ],
        []
      ]
    },
    "Version": {
      "main": [
        [
          {
            "node": "SSH",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Parametrs": {
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
    "Unsuspend": {
      "main": [
        [
          {
            "node": "SSH",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Mount Disk": {
      "main": [
        [
          {
            "node": "SSH",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Terminated": {
      "main": [
        [
          {
            "node": "SSH",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Unmount Disk": {
      "main": [
        [
          {
            "node": "SSH",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "ChangePackage": {
      "main": [
        [
          {
            "node": "SSH",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Container Stat": {
      "main": [
        [
          {
            "node": "Inspect",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Stat",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Log",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Service Actions": {
      "main": [
        [
          {
            "node": "Test Connection1",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Deploy",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Suspend",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Unsuspend",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Terminated",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "ChangePackage",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Test Connection1": {
      "main": [
        [
          {
            "node": "SSH",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Container Actions": {
      "main": [
        [
          {
            "node": "Start",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Stop",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Mount Disk",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Unmount Disk",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "GET ACL",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "SET ACL",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "GET NET",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Deploy-docker-compose": {
      "main": [
        [
          {
            "node": "Service Actions",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-263"></a>

## Template 263 - Notificação diária do tempo

- **Nome:** Notificação diária do tempo
- **Descrição:** Envia uma notificação push diária com a temperatura atual de Berlim, informando o valor em °C.
- **Funcionalidade:** • Agendamento diário: Executa o fluxo automaticamente todos os dias às 09:00.
• Consulta de clima: Obtém a temperatura atual da cidade de Berlim a partir de um serviço de dados meteorológicos.
• Envio de notificação push: Envia uma mensagem personalizada contendo a temperatura em °C e um título para o destinatário via serviço de notificações.
- **Ferramentas:** • OpenWeatherMap: Serviço de dados meteorológicos que fornece informações como temperatura, umidade e condições atuais por cidade.
• Pushover: Serviço de notificações push que permite enviar mensagens e alertas para dispositivos e contas de usuário.

## Fluxo visual

```mermaid
flowchart LR
    N1["Pushover"]
    N2["Cron"]
    N3["OpenWeatherMap"]

    N2 --> N3
    N3 --> N1
```

## Fluxo (.json) :

```json
{
  "id": "91",
  "name": "Send daily weather updates via a push notification",
  "nodes": [
    {
      "name": "Pushover",
      "type": "n8n-nodes-base.pushover",
      "position": [
        970,
        300
      ],
      "parameters": {
        "message": "=Hey! The temperature outside is {{$node[\"OpenWeatherMap\"].json[\"main\"][\"temp\"]}}°C.",
        "userKey": "",
        "priority": 0,
        "additionalFields": {
          "title": "Today's Weather"
        }
      },
      "credentials": {
        "pushoverApi": "pushover"
      },
      "typeVersion": 1
    },
    {
      "name": "Cron",
      "type": "n8n-nodes-base.cron",
      "position": [
        570,
        300
      ],
      "parameters": {
        "triggerTimes": {
          "item": [
            {
              "hour": 9
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "OpenWeatherMap",
      "type": "n8n-nodes-base.openWeatherMap",
      "position": [
        770,
        300
      ],
      "parameters": {
        "cityName": "berlin"
      },
      "credentials": {
        "openWeatherMapApi": "owm"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "Cron": {
      "main": [
        [
          {
            "node": "OpenWeatherMap",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenWeatherMap": {
      "main": [
        [
          {
            "node": "Pushover",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-264"></a>

## Template 264 - Envio de certificados por e-mail em lotes

- **Nome:** Envio de certificados por e-mail em lotes
- **Descrição:** Lê um arquivo CSV com nomes e e-mails, busca certificados PNG correspondentes e envia cada certificado por e-mail em lotes.
- **Funcionalidade:** • Gatilho manual: inicia o fluxo quando executado manualmente.
• Leitura do arquivo CSV: carrega um arquivo CSV da máquina local e converte em registros.
• Processamento em lotes: divide os registros em lotes de 5 para controlar a taxa de envio.
• Leitura dinâmica de arquivos binários: para cada registro, lê o arquivo PNG de certificado cujo nome é construído a partir do campo "name".
• Envio de e-mail com anexo: envia um e-mail por registro com assunto fixo e anexa o PNG correspondente.
• Suporte a certificados TLS não autorizados: permite conexões a servidores SMTP com certificados não verificados.
- **Ferramentas:** • Servidor SMTP: serviço externo usado para enviar os e-mails, exige credenciais de acesso.
• Sistema de arquivos local: armazenamento onde estão o CSV de entrada e os arquivos PNG dos certificados.

## Fluxo visual

```mermaid
flowchart LR
    N1["On clicking 'execute'"]
    N2["Send Email"]
    N3["Read Binary File"]
    N4["Spreadsheet File"]
    N5["SplitInBatches"]
    N6["Read Binary File1"]

    N5 --> N6
    N3 --> N4
    N4 --> N5
    N6 --> N2
    N1 --> N3
```

## Fluxo (.json) :

```json
{
  "id": 1,
  "name": "My workflow",
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        320,
        300
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Send Email",
      "type": "n8n-nodes-base.emailSend",
      "position": [
        1520,
        300
      ],
      "parameters": {
        "options": {
          "allowUnauthorizedCerts": true
        },
        "subject": "Certificate For Course",
        "toEmail": "={{$node[\"SplitInBatches\"].json[\"email\"]}}",
        "fromEmail": "bhavabhuthi@riseup.net",
        "attachments": "data"
      },
      "credentials": {
        "smtp": {
          "id": "1",
          "name": "SMTP account"
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Read Binary File",
      "type": "n8n-nodes-base.readBinaryFile",
      "position": [
        560,
        300
      ],
      "parameters": {
        "filePath": "/home/shashikanth/Documents/Cert-Gen-Test/data.csv",
        "dataPropertyName": "csv"
      },
      "typeVersion": 1,
      "alwaysOutputData": false
    },
    {
      "name": "Spreadsheet File",
      "type": "n8n-nodes-base.spreadsheetFile",
      "position": [
        840,
        300
      ],
      "parameters": {
        "options": {
          "headerRow": true
        },
        "binaryPropertyName": "csv"
      },
      "typeVersion": 1
    },
    {
      "name": "SplitInBatches",
      "type": "n8n-nodes-base.splitInBatches",
      "position": [
        1080,
        300
      ],
      "parameters": {
        "options": {
          "reset": false
        },
        "batchSize": 5
      },
      "typeVersion": 1
    },
    {
      "name": "Read Binary File1",
      "type": "n8n-nodes-base.readBinaryFile",
      "position": [
        1300,
        300
      ],
      "parameters": {
        "filePath": "=/home/shashikanth/Documents/Cert-Gen-Test/generator-output/{{$json[\"name\"]}}.png"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "SplitInBatches": {
      "main": [
        [
          {
            "node": "Read Binary File1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Read Binary File": {
      "main": [
        [
          {
            "node": "Spreadsheet File",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Spreadsheet File": {
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
    "Read Binary File1": {
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
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "Read Binary File",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-265"></a>

## Template 265 - Conversa multi-agente escalável

- **Nome:** Conversa multi-agente escalável
- **Descrição:** Orquestra interações com múltiplos assistentes de IA configuráveis, permitindo direcionar respostas por menções ou chamar todos os assistentes de forma sequencial.
- **Funcionalidade:** • Detecção de menções @: identifica menções a assistentes na mensagem do usuário e preserva a ordem de aparição.
• Chamada condicional de assistentes: se houver menções, chama somente os assistentes mencionados; se não, chama todos em ordem aleatória.
• Agentes configuráveis individualmente: cada assistente tem nome, modelo e instruções de sistema próprias.
• Seleção dinâmica de modelo por agente: usa o modelo associado a cada assistente ao gerar respostas.
• Loop sequencial por agente: processa cada agente em sequência, passando contexto entre iterações.
• Memória por sessão: mantém um histórico (janela de contexto) por sessão para conversas multi-turno.
• Composição e formatação de respostas: combina as respostas de todos os assistentes em um único resultado formatado.
• Entrada dinâmica: permite usar a mensagem do usuário ou a última resposta de um assistente como entrada para a rodada atual.
• Configuração centralizada: informações do usuário, mensagens globais e definição dos assistentes são mantidas em um lugar para fácil ajuste.
- **Ferramentas:** • OpenRouter: serviço de API usado para enviar prompts e obter respostas de modelos de linguagem.
• Modelos de LLM (ex.: openai/gpt-4o, anthropic/claude-3.7-sonnet, google/gemini-2.0-flash-lite-001): diferentes modelos de linguagem configuráveis para cada agente, responsáveis por gerar as respostas.

## Fluxo visual

```mermaid
flowchart LR
    N1["When chat message received"]
    N2["AI Agent"]
    N3["Loop Over Items"]
    N4["Extract mentions"]
    N5["Simple Memory"]
    N6["Set last Assistant message as input"]
    N7["Set user message as input"]
    N8["First loop?"]
    N9["Set lastAssistantMessage"]
    N10["Combine and format responses"]
    N11["Define Global Settings"]
    N12["Define Agent Settings"]
    N13["Sticky Note"]
    N14["Sticky Note1"]
    N15["Sticky Note2"]
    N16["Sticky Note3"]
    N17["Sticky Note4"]
    N18["OpenRouter Chat Model"]

    N2 --> N9
    N8 --> N7
    N8 --> N6
    N3 --> N10
    N3 --> N8
    N4 --> N3
    N12 --> N4
    N11 --> N12
    N9 --> N3
    N7 --> N2
    N1 --> N11
    N6 --> N2
```

## Fluxo (.json) :

```json
{
  "id": "0QQxgdQABUbbDJ0G",
  "meta": {
    "instanceId": "c98909b50b05c4069bd93ee5a4753d07322c9680e81da8568e96de2c713adb5c"
  },
  "name": "Multi-Agent Conversation",
  "tags": [],
  "nodes": [
    {
      "id": "218308e2-dc68-43ee-ae84-d931ad7a4ac5",
      "name": "When chat message received",
      "type": "@n8n/n8n-nodes-langchain.chatTrigger",
      "position": [
        -1880,
        -3280
      ],
      "webhookId": "a74752f3-419a-4510-856f-3efeaceec019",
      "parameters": {
        "options": {}
      },
      "typeVersion": 1.1
    },
    {
      "id": "a519fe1e-8739-46e0-9770-deb256ab96cf",
      "name": "AI Agent",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        -340,
        -3280
      ],
      "parameters": {
        "text": "={{ $json.chatInput }}",
        "options": {
          "systemMessage": "=Current date is {{ $now.format('yyyy-MM-dd') }}. The current time is {{ $now.format('HH:MM:ss') }}.\n\nThe user is {{ $('Define Global Settings').item.json.user.name }}, based in {{ $('Define Global Settings').item.json.user.location }}. {{ $('Define Global Settings').item.json.user.notes }}\n\nYou are part of a conversation with a user and multiple AI Assistants: {{ $('Define Agent Settings').item.json.keys() }}\n\nYou are {{ $('First loop?').item.json.name }}.\n\n{{ $('Loop Over Items').item.json.systemMessage }}\n\n{{ $('Define Global Settings').item.json.global.systemMessage }}"
        },
        "promptType": "define"
      },
      "typeVersion": 1.8
    },
    {
      "id": "2e00f0ff-e7af-45d5-99bc-23031b5d7892",
      "name": "Loop Over Items",
      "type": "n8n-nodes-base.splitInBatches",
      "position": [
        -1000,
        -3280
      ],
      "parameters": {
        "options": {}
      },
      "typeVersion": 3
    },
    {
      "id": "1c979a20-46a5-4591-92da-82c1c96277c6",
      "name": "Extract mentions",
      "type": "n8n-nodes-base.code",
      "position": [
        -1220,
        -3280
      ],
      "parameters": {
        "jsCode": "// Analyzes the user message and extracts @mentions in the order they appear. If there are none, all Assistants will be called in random order.\n// --- Configuration: Adjust these lines ---\nconst chatMessageNodeName = 'When chat message received'; // <-- Replace with your Chat Message node name\nconst agentSetupNodeName = 'Define Agent Settings';         // <-- Replace with your Agent Setup node name\nconst chatTextPath = 'json.chatInput';               // <-- Replace with path to text in Chat node output (e.g., 'json.message')\n// --- End Configuration ---\n\n// Helper function for safe nested property access (alternative to _.get)\nfunction getSafe(obj, path, defaultValue = undefined) {\n    const pathParts = path.split('.');\n    let current = obj;\n    for (const part of pathParts) {\n        if (current === null || current === undefined || typeof current !== 'object' || !Object.prototype.hasOwnProperty.call(current, part)) {\n            return defaultValue;\n        }\n        current = current[part];\n    }\n    return current ?? defaultValue;\n}\n\n// 1. Get Chat Text\nconst chatMessageNode = $(chatMessageNodeName);\nconst chatText = getSafe(chatMessageNode.item, chatTextPath, '');\n\n// 2. Get Agent Data and Names\nconst agentSetupNode = $(agentSetupNodeName);\nconst agentData = getSafe(agentSetupNode.item, 'json', {}); // e.g., { Chad: {...}, Gemma: {...}, Claude: {...} }\nconst agentNames = Object.keys(agentData);\n\n// 3. Find all mentions, their names, and their positions in the text\nconst foundMentions = [];\nif (chatText && agentNames.length > 0) {\n    const escapeRegex = (s) => s.replace(/[-/\\\\^$*+?.()|[\\]{}]/g, '\\\\$&');\n    const agentPatternPart = agentNames.map(escapeRegex).join('|');\n\n    if (agentPatternPart) {\n        const mentionPattern = new RegExp(`\\\\B@(${agentPatternPart})\\\\b`, 'gi');\n        const matches = chatText.matchAll(mentionPattern);\n\n        for (const match of matches) {\n            const matchedNameCaseInsensitive = match[1];\n            const matchIndex = match.index;\n            const canonicalName = agentNames.find(name => name.toLowerCase() === matchedNameCaseInsensitive.toLowerCase());\n            if (canonicalName) {\n                foundMentions.push({ name: canonicalName, index: matchIndex });\n            }\n        }\n    }\n}\n\n// 4. Sort the found mentions by their index (order of appearance)\nfoundMentions.sort((a, b) => a.index - b.index);\n\n// 5. Map the sorted mentions to the desired output format (array of agent detail objects)\nlet outputArray = foundMentions.map(mention => {\n    const agentDetails = agentData[mention.name];\n    if (!agentDetails) {\n        console.warn(`Could not find details for agent: ${mention.name}`);\n        return null;\n    }\n    return {\n        name: agentDetails.name,\n        model: agentDetails.model,\n        systemMessage: agentDetails.systemMessage\n    };\n}).filter(item => item !== null);\n\n// 6. Check if any mentions were specifically found. If not, populate outputArray with ALL agents in RANDOM order.\nif (outputArray.length === 0 && foundMentions.length === 0) { // Check if NO mentions were found initially\n    // --- NO MENTIONS FOUND ---\n    // Populate outputArray with ALL agents from agentData\n    const allAgentDetailsArray = Object.values(agentData);\n\n    // --- Simple Randomization ---\n    // Shuffle the array in place using sort with a random comparator\n    allAgentDetailsArray.sort(() => 0.5 - Math.random());\n    // --- End Randomization ---\n\n    // Map all agents (now in random order) to the output structure\n    outputArray = allAgentDetailsArray.map(agentObject => ({\n        name: agentObject.name,\n        model: agentObject.model,\n        systemMessage: agentObject.systemMessage\n    }));\n} // Intentionally no 'else' here, if outputArray already had items from mentions, we use that.\n\n// 7. Final Output Formatting (Handles both cases: specific mentions OR all agents)\n// Check if, after everything, the outputArray is *still* empty (e.g., if agentData was empty initially)\nif (outputArray.length === 0) {\n    // If still empty, return a status or error as a fallback\n     return [{ json: { status: \"no_agents_available\", message: \"No mentions found and no agents defined.\" } }];\n} else {\n    // Return the array of agent objects formatted for n8n (multiple items)\n    return outputArray.map(agentObject => ({ json: agentObject }));\n}"
      },
      "typeVersion": 2
    },
    {
      "id": "45f635ca-f4fa-4f6c-a32a-9722906255fd",
      "name": "Simple Memory",
      "type": "@n8n/n8n-nodes-langchain.memoryBufferWindow",
      "position": [
        -192,
        -3060
      ],
      "parameters": {
        "sessionKey": "={{ $('When chat message received').first().json.sessionId }}",
        "sessionIdType": "customKey",
        "contextWindowLength": 99
      },
      "typeVersion": 1.3
    },
    {
      "id": "5c903044-bce2-4aa8-b168-a460a4999c54",
      "name": "Set last Assistant message as input",
      "type": "n8n-nodes-base.set",
      "position": [
        -560,
        -3180
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "38aa959a-e1e5-4c84-a7bd-ff5e0f61b62d",
              "name": "=chatInput",
              "type": "string",
              "value": "={{ $('Set lastAssistantMessage').first().json.lastAssistantMessage }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "7b389b9f-1751-4bc1-9c6f-bf6a04a1e09f",
      "name": "Set user message as input",
      "type": "n8n-nodes-base.set",
      "position": [
        -560,
        -3380
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "75b61275-7526-4431-b624-f8e098aa812d",
              "name": "chatInput",
              "type": "string",
              "value": "={{ $('When chat message received').item.json.chatInput }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "a238817f-0d10-4cd4-9760-53f69bb179f7",
      "name": "First loop?",
      "type": "n8n-nodes-base.if",
      "position": [
        -780,
        -3280
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
              "id": "51c41fdf-f4d3-4c7a-ac18-06815a59a958",
              "operator": {
                "type": "number",
                "operation": "equals"
              },
              "leftValue": "={{ $runIndex}}",
              "rightValue": 0
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "415927d7-b1a4-42b2-9607-c6ff707a528b",
      "name": "Set lastAssistantMessage",
      "type": "n8n-nodes-base.set",
      "position": [
        36,
        -3155
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "b93025b2-f5a7-476b-bd09-b5b4af050e73",
              "name": "lastAssistantMessage",
              "type": "string",
              "value": "=**{{ $('Loop Over Items').item.json.name }}**:\n\n{{ $json.output }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "77861e4b-a1d2-4c35-bf50-15914602a8b5",
      "name": "Combine and format responses",
      "type": "n8n-nodes-base.code",
      "position": [
        -780,
        -3480
      ],
      "parameters": {
        "jsCode": "// Get the array of items from the input (output of the loop)\nconst inputItems = items;\n\n// Extract the 'lastAssistantMessage' from each item's JSON data.\n// If the field is missing or not a string, use an empty string to avoid errors.\nconst messages = inputItems.map(item => {\n  const message = item.json.lastAssistantMessage;\n  return typeof message === 'string' ? message : '';\n});\n\n// Join the extracted messages together with a horizontal rule separator\nconst combinedText = messages.join('\\n\\n---\\n\\n');\n\n// Return a new single item containing the combined text.\n// You can rename 'output' if you like.\nreturn [{ json: { output: combinedText } }];"
      },
      "typeVersion": 2
    },
    {
      "id": "4da2f95d-bce4-4844-a23c-63ca777efbfd",
      "name": "Define Global Settings",
      "type": "n8n-nodes-base.code",
      "position": [
        -1660,
        -3280
      ],
      "parameters": {
        "jsCode": "// Configure Global settings. This includes information about you - the user - and a section of the System Message that all Assistants will see. (Assistant-specific System Message sections can be set in the 'Define Agent Settings' node.)\nreturn [\n  {\n    json: {\n      \"user\": {\n        \"name\": \"Jon\",\n        \"location\": \"Melbourne, Australia\",\n        \"notes\": \"Jon likes a casual, informal conversation style.\"\n      },\n      \"global\": {\n        \"systemMessage\": \"Don't overdo the helpful, agreeable approach.\"\n      }\n    }\n  }\n];\n"
      },
      "typeVersion": 2
    },
    {
      "id": "6639a554-9e5f-40ac-b68e-b8eaa777252d",
      "name": "Define Agent Settings",
      "type": "n8n-nodes-base.code",
      "position": [
        -1440,
        -3280
      ],
      "parameters": {
        "jsCode": "// Configure Assistants. The number of Assistants can be changed by adding or removing JSON objects. Use the OpenRouter model naming convention.\nreturn [\n  {\n    json: {\n      \"Chad\": {\n        \"name\": \"Chad\",\n        \"model\": \"openai/gpt-4o\",\n        \"systemMessage\": \"You are a helpful Assistant. You are eccentric and creative, and try to take discussions into unexpected territory.\"\n      },\n      \"Claude\": {\n        \"name\": \"Claude\",\n        \"model\": \"anthropic/claude-3.7-sonnet\",\n        \"systemMessage\": \"You are logical and practical.\"\n      },\n      \"Gemma\": {\n        \"name\": \"Gemma\",\n        \"model\": \"google/gemini-2.0-flash-lite-001\",\n        \"systemMessage\": \"You are super friendly and love to debate.\"\n      }\n    }\n  }\n];\n"
      },
      "typeVersion": 2
    },
    {
      "id": "d55a7e02-3574-4d78-a141-db8d3657857b",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -1750,
        -3620
      ],
      "parameters": {
        "color": 4,
        "width": 500,
        "height": 500,
        "content": "## Step 1: Configure Settings Nodes\n\nEdit the JSON in these nodes to:\n\n- Configure details about you (the user)\n- Define content that will appear in all system messages\n- Define Agents.\n\nFor Agents, you can configure:\n- How many you create\n- Their names\n- The LLM model they use (choose any that are available via OpenRouter)\n- Agent-specific system prompt content"
      },
      "typeVersion": 1
    },
    {
      "id": "d3eb2797-4008-4bdb-a588-b2412ed5ffa7",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -400,
        -3620
      ],
      "parameters": {
        "color": 4,
        "width": 360,
        "height": 720,
        "content": "## Step 2: Connect Agent to OpenRouter\n\nSet your OpenRouter credentials, and all other parameters including system messages and model selection are dynamically populated."
      },
      "typeVersion": 1
    },
    {
      "id": "a6085a55-db36-42d8-8c57-c9123490581f",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -1940,
        -3900
      ],
      "parameters": {
        "color": 5,
        "width": 2180,
        "height": 1100,
        "content": "# Scalable Multi-Agent Conversations\n\n"
      },
      "typeVersion": 1
    },
    {
      "id": "d2ee6317-3a9c-4df8-8fce-87daa3530233",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -1200,
        -3860
      ],
      "parameters": {
        "width": 380,
        "height": 360,
        "content": "## About this workflow\n\n**What does this workflow do?**\nEnables you to initiate a conversation with multiple AI agents at once. Each agent can be configured with a unique name, system instructions, a different model.\n\n**How do I use it?**\n1. Configure the settings nodes to create the Agents you need.\n2. Call one or more individual agents using @Name mentions in your messages. If your message does not have @mentions, all agents will be called, in random order."
      },
      "typeVersion": 1
    },
    {
      "id": "a190a268-7f90-4c4e-aceb-482545d0b72b",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -820,
        -3860
      ],
      "parameters": {
        "width": 380,
        "height": 360,
        "content": "**How does it work?**\nSettings are configured in the first two nodes after the chat trigger. Then @mentions in your message are extracted and fed into a loop. With each loop, the agent's system message and model are dynamically populated, avoiding the need to create multiple agent nodes and complex routing logic.\n\nWhen all agents have had their say, their responses are combined and formatted. The use of a shared memory node enables multi-round conversations.\n\n**What are the limitations?**\nAgents cannot call each other or respond in parallel. Agents' responses are not visible to the user until all agents have responded.\n\n"
      },
      "typeVersion": 1
    },
    {
      "id": "30d8c207-9a7a-46c5-be89-0deafc6c183f",
      "name": "OpenRouter Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenRouter",
      "position": [
        -312,
        -3060
      ],
      "parameters": {
        "model": "={{ $('Extract mentions').item.json.model }}",
        "options": {}
      },
      "credentials": {
        "openRouterApi": {
          "id": "jB56IT6KRdHSBbkw",
          "name": "OpenRouter account"
        }
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "6c0312e7-7a81-41cd-9403-8ad947100b80",
  "connections": {
    "AI Agent": {
      "main": [
        [
          {
            "node": "Set lastAssistantMessage",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "First loop?": {
      "main": [
        [
          {
            "node": "Set user message as input",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Set last Assistant message as input",
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
    "Loop Over Items": {
      "main": [
        [
          {
            "node": "Combine and format responses",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "First loop?",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract mentions": {
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
    "Define Agent Settings": {
      "main": [
        [
          {
            "node": "Extract mentions",
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
            "node": "AI Agent",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Define Global Settings": {
      "main": [
        [
          {
            "node": "Define Agent Settings",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set lastAssistantMessage": {
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
    "Set user message as input": {
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
    "When chat message received": {
      "main": [
        [
          {
            "node": "Define Global Settings",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Combine and format responses": {
      "main": [
        []
      ]
    },
    "Set last Assistant message as input": {
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

<a id="template-266"></a>

## Template 266 - Registrar transferências Wise → Airtable

- **Nome:** Registrar transferências Wise → Airtable
- **Descrição:** Este fluxo captura alterações no estado de transferências do Wise, obtém os dados completos da transferência e registra os detalhes em uma tabela do Airtable.
- **Funcionalidade:** • Detecção de mudança de estado de transferência: Inicia o fluxo ao receber um evento de alteração de estado de transferência para um perfil específico.
• Recuperação de detalhes da transferência: Busca os dados completos da transferência usando o ID recebido no evento.
• Mapeamento e formatação de campos: Extrai e organiza campos relevantes como ID da transferência, data, referência e valor.
• Inserção na base de dados: Adiciona um novo registro à tabela do Airtable com os dados formatados.
- **Ferramentas:** • Wise: Serviço de pagamentos que emite webhooks de eventos de transferência e fornece API para recuperar detalhes das transferências.
• Airtable: Plataforma de base de dados/planilha onde os registros das transferências são armazenados em uma tabela.

## Fluxo visual

```mermaid
flowchart LR
    N1["Wise Trigger"]
    N2["Wise"]
    N3["Set"]
    N4["Airtable"]

    N3 --> N4
    N2 --> N3
    N1 --> N2
```

## Fluxo (.json) :

```json
{
  "nodes": [
    {
      "name": "Wise Trigger",
      "type": "n8n-nodes-base.wiseTrigger",
      "position": [
        450,
        280
      ],
      "webhookId": "df8c0c06-7d40-4e57-aaff-60f458e6997c",
      "parameters": {
        "event": "tranferStateChange",
        "profileId": 16138858
      },
      "credentials": {
        "wiseApi": "Wise API Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Wise",
      "type": "n8n-nodes-base.wise",
      "position": [
        650,
        280
      ],
      "parameters": {
        "resource": "transfer",
        "transferId": "={{$json[\"data\"][\"resource\"][\"id\"]}}"
      },
      "credentials": {
        "wiseApi": "Wise API Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Set",
      "type": "n8n-nodes-base.set",
      "position": [
        850,
        280
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "Transfer ID",
              "value": "={{$json[\"id\"]}}"
            },
            {
              "name": "Date",
              "value": "={{$json[\"created\"]}}"
            },
            {
              "name": "Reference",
              "value": "={{$json[\"reference\"]}}"
            },
            {
              "name": "Amount",
              "value": "={{$json[\"sourceValue\"]}}"
            }
          ]
        },
        "options": {},
        "keepOnlySet": true
      },
      "typeVersion": 1
    },
    {
      "name": "Airtable",
      "type": "n8n-nodes-base.airtable",
      "position": [
        1050,
        280
      ],
      "parameters": {
        "table": "Table 1",
        "options": {},
        "operation": "append",
        "application": ""
      },
      "credentials": {
        "airtableApi": "Airtable Credentials n8n"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Set": {
      "main": [
        [
          {
            "node": "Airtable",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Wise": {
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
    "Wise Trigger": {
      "main": [
        [
          {
            "node": "Wise",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-267"></a>

## Template 267 - Análise de redes sociais e email personalizado

- **Nome:** Análise de redes sociais e email personalizado
- **Descrição:** Fluxo que coleta dados de LinkedIn e Twitter de um lead a partir de uma planilha, extrai posts, usa IA para criar um assunto e uma carta de apresentação em HTML, envia o email com cópia para o remetente e atualiza o status na planilha.
- **Funcionalidade:** • Coleta de dados do lead a partir de Google Sheets e triggers: lê LinkedIn URL, nome, Twitter, email e estado de conclusão.
• Consulta a APIs de redes sociais: obtém dados de LinkedIn e Tweets via RapidAPI.
• Extração e limitação de conteúdo: filtra posts/tweets, limitando a até 10 itens.
• Geração de conteúdo com IA: produz assunto e carta de apresentação em HTML com base nos dados coletados.
• Envio de email automatizado: envia o email ao lead com o conteúdo gerado e CC para o remetente.
• Atualização de progresso: marca o lead como processado na planilha.
- **Ferramentas:** • Google Sheets: armazenamento e leitura de leads e estado de conclusão.
• RapidAPI: acesso a dados de LinkedIn e Twitter.
• OpenAI: geração de tópico e carta de apresentação baseada em IA.
• SMTP: envio automático de emails com o conteúdo gerado.

## Fluxo visual

```mermaid
flowchart LR
    N1["Set your company's variables"]
    N2["Get linkedin Posts"]
    N3["Get twitter ID"]
    N4["Get tweets"]
    N5["Extract and limit Linkedin"]
    N6["Exract and limit X"]
    N7["OpenAI Chat Model"]
    N8["Structured Output Parser"]
    N9["Generate Subject and cover letter based on match"]
    N10["Send Cover letter and CC me"]
    N11["Sticky Note"]
    N12["Google Sheets Trigger"]
    N13["Google Sheets"]
    N14["If"]
    N15["Sticky Note1"]
    N16["Sticky Note2"]
    N17["Sticky Note3"]
    N18["Sticky Note4"]
    N19["Sticky Note5"]

    N14 --> N1
    N4 --> N6
    N3 --> N4
    N6 --> N2
    N2 --> N5
    N12 --> N14
    N5 --> N9
    N10 --> N13
    N1 --> N3
    N9 --> N10
```

## Fluxo (.json) :

```json
{
  "nodes": [
    {
      "id": "a768bce6-ae26-464c-95fc-009edea4f94d",
      "name": "Set your company's variables",
      "type": "n8n-nodes-base.set",
      "position": [
        440,
        0
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "6a8063b6-1fd8-429a-9f13-b7512066c702",
              "name": "your_company_name",
              "type": "string",
              "value": "Pollup Data Services"
            },
            {
              "id": "3e6780d6-86d0-4353-aa17-8470a91f63a8",
              "name": "your_company_activity",
              "type": "string",
              "value": "Whether it’s automating recurring tasks, analysing data faster, or personalising customer interactions, we build bespoke AI agents to help your workforce work smarter."
            },
            {
              "id": "1b42f1b3-20ed-4278-952d-f28fe0f03fa3",
              "name": "your_email",
              "type": "string",
              "value": "thomas@pollup.net"
            },
            {
              "id": "7c109ba2-d855-49d5-8700-624b01a05bc1",
              "name": "your_name",
              "type": "string",
              "value": "Justin"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "ca729f8d-cab8-4221-addb-aa23813d80b4",
      "name": "Get linkedin Posts",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1300,
        0
      ],
      "parameters": {
        "url": "https://fresh-linkedin-profile-data.p.rapidapi.com/get-profile-posts",
        "options": {},
        "sendQuery": true,
        "sendHeaders": true,
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "queryParameters": {
          "parameters": [
            {
              "name": "linkedin_url",
              "value": "={{ $('Google Sheets Trigger').item.json.linkedin_url }}"
            },
            {
              "name": "type",
              "value": "posts"
            }
          ]
        },
        "headerParameters": {
          "parameters": [
            {
              "name": "x-rapidapi-host",
              "value": "fresh-linkedin-profile-data.p.rapidapi.com"
            }
          ]
        }
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "nhoVFnkO31mejJrI",
          "name": "RapidAPI Key"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "b9559958-f8ac-4ab6-93c6-50eb04113808",
      "name": "Get twitter ID",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        680,
        0
      ],
      "parameters": {
        "url": "https://twitter-api47.p.rapidapi.com/v2/user/by-username",
        "options": {},
        "sendQuery": true,
        "sendHeaders": true,
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "queryParameters": {
          "parameters": [
            {
              "name": "username",
              "value": "={{ $('Google Sheets Trigger').item.json.twitter_handler }}"
            }
          ]
        },
        "headerParameters": {
          "parameters": [
            {
              "name": "x-rapidapi-host",
              "value": "twitter-api47.p.rapidapi.com"
            }
          ]
        }
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "nhoVFnkO31mejJrI",
          "name": "RapidAPI Key"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "3e85565f-ebfa-4568-9391-869961c5b3ed",
      "name": "Get tweets",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        880,
        0
      ],
      "parameters": {
        "url": "https://twitter-api47.p.rapidapi.com/v2/user/tweets",
        "options": {},
        "sendQuery": true,
        "sendHeaders": true,
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "queryParameters": {
          "parameters": [
            {
              "name": "userId",
              "value": "={{ $json.rest_id }}"
            }
          ]
        },
        "headerParameters": {
          "parameters": [
            {
              "name": "x-rapidapi-host",
              "value": "twitter-api47.p.rapidapi.com"
            }
          ]
        }
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "nhoVFnkO31mejJrI",
          "name": "RapidAPI Key"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "6e060b21-9eaf-49e6-9665-c051b3f2397e",
      "name": "Extract and limit Linkedin",
      "type": "n8n-nodes-base.code",
      "position": [
        1520,
        0
      ],
      "parameters": {
        "jsCode": "// Loop over input items and add a new field called 'myNewField' to the JSON of each one\noutput = []\nmax_posts = 10\nlet counter = 0\nfor (const item of $input.all()[0].json.data) {\n let post = {\n title: item.article_title,\n text: item.text\n }\n output.push(post)\n if(counter++ >= max_posts) break;\n}\n\nreturn {\"linkedIn posts\": output};"
      },
      "typeVersion": 2
    },
    {
      "id": "e65bc472-e7c6-43c5-8e84-fe8c4512e92f",
      "name": "Exract and limit X",
      "type": "n8n-nodes-base.code",
      "position": [
        1100,
        0
      ],
      "parameters": {
        "jsCode": "// Loop over input items and add a new field called 'myNewField' to the JSON of each one\noutput = []\nmax_posts = 10\nlet counter = 0\nfor (const item of $input.all()[0].json.tweets) {\n if(!item.content.hasOwnProperty('itemContent')) continue\n let post = {\n text: item.content.itemContent?.tweet_results?.result.legacy?.full_text\n }\n console.log(post)\n output.push(post)\n if(counter++ >= max_posts) break;\n}\n\nreturn {\"Twitter tweets\": output};"
      },
      "typeVersion": 2
    },
    {
      "id": "10f088a0-0479-428e-96cf-fe0df9b37877",
      "name": "OpenAI Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        1740,
        200
      ],
      "parameters": {
        "model": "gpt-4o",
        "options": {}
      },
      "credentials": {
        "openAiApi": {
          "id": "yepsCCAriRlCkICW",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "9adfd648-8348-4a0a-8b9b-d54dc3b715bb",
      "name": "Structured Output Parser",
      "type": "@n8n/n8n-nodes-langchain.outputParserStructured",
      "position": [
        1920,
        220
      ],
      "parameters": {
        "jsonSchemaExample": "{\n \"subject\": \"\",\n \"cover_letter\": \"\"\n}"
      },
      "typeVersion": 1.2
    },
    {
      "id": "af96003c-539d-4728-832c-4819d85bbbcc",
      "name": "Generate Subject and cover letter based on match",
      "type": "@n8n/n8n-nodes-langchain.chainLlm",
      "position": [
        1720,
        0
      ],
      "parameters": {
        "text": "=## Me\n- My company name is: {{ $('Set your company\\'s variables').item.json.your_company_name }}\n- My company's activity is: {{ $('Set your company\\'s variables').item.json.your_company_activity }}\n- My name is: {{ $('Set your company\\'s variables').item.json.your_name }}\n- My email is: {{ $('Set your company\\'s variables').item.json.your_email }}\n\n## My lead:\nHis name: {{ $('Google Sheets Trigger').item.json.name }}\n\n## What I want you to do\n- According to the info about me, and the linkedin posts an twitter post of a user given below, I want you to find a common activity that I could propose to this person and generate a cover letter about it\n- Return ONLY the cover letter and the subject as a json like this:\n{\n \"subject\": \"\",\n \"cover_letter\": \"\"\n}\n\nTHe cover letter should be in HTML format\n\n## The Linkedin Posts:\n{{ JSON.stringify($json[\"linkedIn posts\"])}}\n\n## THe Twitter posts:\n{{ JSON.stringify($('Exract and limit X').item.json['Twitter tweets']) }}\n",
        "messages": {
          "messageValues": [
            {
              "message": "You are a helpful Marketing assistant"
            }
          ]
        },
        "promptType": "define",
        "hasOutputParser": true
      },
      "typeVersion": 1.5
    },
    {
      "id": "6954285f-7ea5-4e3d-8be2-03051d716d03",
      "name": "Send Cover letter and CC me",
      "type": "n8n-nodes-base.emailSend",
      "position": [
        2080,
        0
      ],
      "parameters": {
        "html": "={{ $json.output.cover_letter }}",
        "options": {},
        "subject": "={{ $json.output.subject }}",
        "toEmail": "={{ $('Google Sheets Trigger').item.json.email }}, {{ $('Set your company\\'s variables').item.json.your_email }}",
        "fromEmail": "thomas@pollup.net"
      },
      "credentials": {
        "smtp": {
          "id": "yrsGGdbYvSB8u7sx",
          "name": "SMTP account"
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "357477a8-98c3-48a5-8c88-965f90a4beb2",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        360,
        -280
      ],
      "parameters": {
        "color": 4,
        "height": 480,
        "content": "## Personalize here\n\n### Set: \n- your name\n- your company name\n- your company activity, used to find a match with your leads\n- your email, used as the sender"
      },
      "typeVersion": 1
    },
    {
      "id": "0c26383c-c8f1-44b1-995e-2c88118061bb",
      "name": "Google Sheets Trigger",
      "type": "n8n-nodes-base.googleSheetsTrigger",
      "position": [
        -40,
        20
      ],
      "parameters": {
        "options": {
          "dataLocationOnSheet": {
            "values": {
              "rangeDefinition": "specifyRange"
            }
          }
        },
        "pollTimes": {
          "item": [
            {
              "mode": "everyMinute"
            }
          ]
        },
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": "gid=0",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1IcvbbG_WScVNyutXhzqyE9NxdxNbY90Dd63R8Y1UrAw/edit#gid=0",
          "cachedResultName": "Sheet1"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "1IcvbbG_WScVNyutXhzqyE9NxdxNbY90Dd63R8Y1UrAw",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1IcvbbG_WScVNyutXhzqyE9NxdxNbY90Dd63R8Y1UrAw/edit?usp=drivesdk",
          "cachedResultName": "Analyze social media of a lead"
        }
      },
      "credentials": {
        "googleSheetsTriggerOAuth2Api": {
          "id": "LBJHhfLqklwl9les",
          "name": "Google Sheets Trigger account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "923cca3d-69a9-4d26-80a3-e9062d42d8a8",
      "name": "Google Sheets",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        2280,
        0
      ],
      "parameters": {
        "columns": {
          "value": {
            "done": "X",
            "linkedin_url": "={{ $('Google Sheets Trigger').item.json.linkedin_url }}"
          },
          "schema": [
            {
              "id": "linkedin_url",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "linkedin_url",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "name",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "name",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "twitter_handler",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "twitter_handler",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "email",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "email",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "done",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "done",
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
            "linkedin_url"
          ]
        },
        "options": {},
        "operation": "update",
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": "gid=0",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1IcvbbG_WScVNyutXhzqyE9NxdxNbY90Dd63R8Y1UrAw/edit#gid=0",
          "cachedResultName": "Sheet1"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "1IcvbbG_WScVNyutXhzqyE9NxdxNbY90Dd63R8Y1UrAw",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1IcvbbG_WScVNyutXhzqyE9NxdxNbY90Dd63R8Y1UrAw/edit?usp=drivesdk",
          "cachedResultName": "Analyze social media of a lead"
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
      "id": "6df02119-09db-4d87-b435-7753693b27aa",
      "name": "If",
      "type": "n8n-nodes-base.if",
      "position": [
        180,
        20
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
              "id": "3839b337-6c33-4907-ba75-8ef04cefc14c",
              "operator": {
                "type": "string",
                "operation": "empty",
                "singleValue": true
              },
              "leftValue": "={{ $json.done }}",
              "rightValue": ""
            }
          ]
        },
        "looseTypeValidation": true
      },
      "executeOnce": false,
      "typeVersion": 2.2,
      "alwaysOutputData": true
    },
    {
      "id": "2edaa85e-ef69-490c-9835-cf8779cada6d",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -120,
        -320
      ],
      "parameters": {
        "color": 4,
        "width": 260,
        "height": 500,
        "content": "## Create a Gooogle sheet with the following columns:\n- linkedin_url\n- name\n- twitter_handler \n- email\n- done\n\nAnd put some data in it except in \"done\" that should remain empty."
      },
      "typeVersion": 1
    },
    {
      "id": "19210bba-1db1-4568-b34e-4e9de002b0eb",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1680,
        -160
      ],
      "parameters": {
        "color": 5,
        "width": 340,
        "height": 300,
        "content": "## Here you can modify the prompt\n- make it better by adding some examples\n- Follow a known framework\netc."
      },
      "typeVersion": 1
    },
    {
      "id": "bebab4e5-35fa-49b7-bb85-a85231c44389",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        660,
        -280
      ],
      "parameters": {
        "color": 4,
        "width": 340,
        "height": 480,
        "content": "## Call RapidAPI Twitter API Profile Data\nYou have to create an account in [RapidAPI](https://rapidapi.com/restocked-gAGxip8a_/api/twitter-api47) and subscribe to Twiiter API. With a free account you will be able to scrape 500 tweets / month.\nAfter your subscription you will have to choose as Generic Auth Type: Header Auth and then put as header name: \"x-rapidapi-key\" and the value given in the RapidAPI interface\n"
      },
      "typeVersion": 1
    },
    {
      "id": "42df4665-2d46-4020-938c-f082db6f09d0",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1220,
        -300
      ],
      "parameters": {
        "color": 4,
        "width": 280,
        "height": 480,
        "content": "## Call RapidAPI Fresh Linkedin Profile Data\nYou have to create an account in [RapidAPI](https://rapidapi.com) and subscribe to Fresh LinkedIn Profile Data. With a free account you will be able to scrape 100 profile / month.\nAfter your subscription you will have to choose as Generic Auth Type: Header Auth and then put as header name: \"x-rapidapi-key\" and the value given in the RapidAPI interface\n"
      },
      "typeVersion": 1
    },
    {
      "id": "4a14febd-bd82-428c-8c97-15f1ba724b02",
      "name": "Sticky Note5",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -840,
        -620
      ],
      "parameters": {
        "width": 700,
        "height": 1180,
        "content": "## Social Media Analysis and Automated Email Generation\n\n> by Thomas Vie [Thomas@pollup.net](mailto:thomas@pollup.net)\n\n### **Who is this for?**\nThis template is ideal for marketers, lead generation specialists, and business professionals seeking to analyze social media profiles of potential leads and automate personalized email outreach efficiently.\n\n\n### **What problem is this workflow solving?**\nManually analyzing social media profiles and crafting personalized emails can be time-consuming and prone to errors. This workflow streamlines the process by integrating social media APIs with AI to generate tailored communication, saving time and increasing outreach effectiveness.\n\n### **What this workflow does:**\n1. **Google Sheets Integration:** Start with a Google Sheet containing lead information such as LinkedIn URL, Twitter handle, name, and email.\n2. **Social Media Data Extraction:** Automatically fetch profile and activity data from Twitter and LinkedIn using RapidAPI integrations.\n3. **AI-Powered Content Generation:** Use OpenAI's Chat Model to analyze the extracted data and generate personalized email subject lines and cover letters.\n4. **Automated Email Dispatch:** Send the generated email directly to the lead, with a copy sent to yourself for tracking purposes.\n5. **Progress Tracking:** Update the Google Sheet to indicate completed actions.\n\n#### **Setup:**\n1. **Google Sheets:**\n - Create a sheet with the columns: LinkedIn URL, name, Twitter handle, email, and a \"done\" column for tracking.\n - Populate the sheet with your leads.\n\n2. **RapidAPI Accounts:**\n - Sign up for RapidAPI and subscribe to the Twitter and LinkedIn API plans.\n - Configure API authentication keys in the workflow.\n\n3. **AI Configuration:**\n - Connect OpenAI Chat Model with your API key for text generation.\n\n4. **Email Integration:**\n - Add your email credentials or service (SMTP or third-party service like Gmail) for sending automated emails.\n\n#### **How to customize this workflow to your needs:**\n- **Modify the AI Prompt:** Adapt the prompt in the AI node to better align with your tone, style, or specific messaging framework.\n- **Expand Data Fields:** Add additional data fields in Google Sheets if you require further personalization.\n- **API Limits:** Adjust API configurations to fit your usage limits or upgrade to higher tiers for increased data scraping capabilities.\n- **Personalize Email Templates:** Tweak email formats to suit different audiences or use cases.\n- **Extend Functionality:** Integrate additional social media platforms or CRM tools as needed.\n\nBy implementing this workflow, you’ll save time on repetitive tasks and create more effective lead generation strategies."
      },
      "typeVersion": 1
    }
  ],
  "pinData": {},
  "connections": {
    "If": {
      "main": [
        [
          {
            "node": "Set your company's variables",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get tweets": {
      "main": [
        [
          {
            "node": "Exract and limit X",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Sheets": {
      "main": [
        []
      ]
    },
    "Get twitter ID": {
      "main": [
        [
          {
            "node": "Get tweets",
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
            "node": "Generate Subject and cover letter based on match",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Exract and limit X": {
      "main": [
        [
          {
            "node": "Get linkedin Posts",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get linkedin Posts": {
      "main": [
        [
          {
            "node": "Extract and limit Linkedin",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Sheets Trigger": {
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
    "Structured Output Parser": {
      "ai_outputParser": [
        [
          {
            "node": "Generate Subject and cover letter based on match",
            "type": "ai_outputParser",
            "index": 0
          }
        ]
      ]
    },
    "Extract and limit Linkedin": {
      "main": [
        [
          {
            "node": "Generate Subject and cover letter based on match",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Send Cover letter and CC me": {
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
    "Set your company's variables": {
      "main": [
        [
          {
            "node": "Get twitter ID",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Generate Subject and cover letter based on match": {
      "main": [
        [
          {
            "node": "Send Cover letter and CC me",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-268"></a>

## Template 268 - Publicar no X usando perfil Airtop

- **Nome:** Publicar no X usando perfil Airtop
- **Descrição:** Automatiza a publicação de um texto em x.com usando um perfil Airtop fornecido via formulário ou por outro fluxo.
- **Funcionalidade:** • Receber dados por formulário: aceita o nome do perfil Airtop e o texto a publicar.
• Aceitar execução por outro fluxo: permite receber os mesmos parâmetros quando invocado por outro fluxo.
• Iniciar sessão com perfil Airtop: abre uma sessão usando o perfil informado para navegar já autenticado.
• Abrir página do X: carrega x.com em uma janela do navegador para realizar a publicação.
• Inserir e publicar o texto: digita o conteúdo na caixa de composição e executa a ação de postagem (enter e clique em Post).
• Encerrar sessão: termina a sessão ativa e pode salvar o perfil ao finalizar.
• Retornar confirmação ao usuário: envia uma mensagem de sucesso ao usuário após o envio do formulário.
- **Ferramentas:** • Airtop: plataforma de automação de navegador que permite iniciar sessões com perfis salvos e executar interações web.
• X (x.com): rede social onde o conteúdo será publicado.

## Fluxo visual

```mermaid
flowchart LR
    N1["Create session"]
    N2["Create window"]
    N3["Type text"]
    N4["Click on Post"]
    N5["End session"]
    N6["When Executed by Another Workflow"]
    N7["Sticky Note"]
    N8["On form submission"]
    N9["Parameters"]

    N3 --> N4
    N9 --> N1
    N4 --> N5
    N2 --> N3
    N1 --> N2
    N8 --> N9
    N6 --> N9
```

## Fluxo (.json) :

```json
{
  "id": "plzObaqgoEvV4UU0",
  "meta": {
    "instanceId": "28a947b92b197fc2524eaba16e57560338657b2b0b5796300b2f1cedc1d0d355",
    "templateCredsSetupCompleted": true
  },
  "name": "Post on X",
  "tags": [
    {
      "id": "gNiDOCnjqCXR7phD",
      "name": "Marketing",
      "createdAt": "2025-04-15T01:08:25.516Z",
      "updatedAt": "2025-04-15T01:08:25.516Z"
    },
    {
      "id": "zKNO4Omjzfu6J25M",
      "name": "Demo",
      "createdAt": "2025-04-15T18:59:57.364Z",
      "updatedAt": "2025-04-15T18:59:57.364Z"
    }
  ],
  "nodes": [
    {
      "id": "203a06a1-2e25-46df-9465-4d5740177249",
      "name": "Create session",
      "type": "n8n-nodes-base.airtop",
      "position": [
        60,
        180
      ],
      "parameters": {
        "profileName": "={{ $json.airtop_profile }}",
        "timeoutMinutes": 5,
        "saveProfileOnTermination": true
      },
      "credentials": {
        "airtopApi": {
          "id": "Yi4YPNnovLVUjFn5",
          "name": "Airtop API"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "18c8ade3-8492-4e75-8310-3be4d7815ab6",
      "name": "Create window",
      "type": "n8n-nodes-base.airtop",
      "position": [
        280,
        180
      ],
      "parameters": {
        "url": "https://x.com/",
        "resource": "window",
        "additionalFields": {}
      },
      "credentials": {
        "airtopApi": {
          "id": "Yi4YPNnovLVUjFn5",
          "name": "Airtop API"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "c46baeac-5d91-4656-a30f-0ca932e8042c",
      "name": "Type text",
      "type": "n8n-nodes-base.airtop",
      "position": [
        500,
        180
      ],
      "parameters": {
        "text": "={{ $('Parameters').item.json.post_text }}",
        "resource": "interaction",
        "operation": "type",
        "pressEnterKey": true,
        "additionalFields": {},
        "elementDescription": "\"What's happening?\" text box on top"
      },
      "credentials": {
        "airtopApi": {
          "id": "Yi4YPNnovLVUjFn5",
          "name": "Airtop API"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "cfc19d89-8fb2-49c5-97a3-38ad03dffe31",
      "name": "Click on Post",
      "type": "n8n-nodes-base.airtop",
      "position": [
        720,
        180
      ],
      "parameters": {
        "resource": "interaction",
        "additionalFields": {
          "visualScope": "viewport"
        },
        "elementDescription": "Click on the Post button "
      },
      "credentials": {
        "airtopApi": {
          "id": "Yi4YPNnovLVUjFn5",
          "name": "Airtop API"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "1b2a4d37-1fcd-4b6a-8db7-a7056c569ad4",
      "name": "End session",
      "type": "n8n-nodes-base.airtop",
      "position": [
        940,
        180
      ],
      "parameters": {
        "operation": "terminate"
      },
      "credentials": {
        "airtopApi": {
          "id": "Yi4YPNnovLVUjFn5",
          "name": "Airtop API"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "2fdae018-aaca-4101-acdc-42d799463880",
      "name": "When Executed by Another Workflow",
      "type": "n8n-nodes-base.executeWorkflowTrigger",
      "position": [
        -380,
        280
      ],
      "parameters": {
        "workflowInputs": {
          "values": [
            {
              "name": "airtop_profile"
            },
            {
              "name": "post_text"
            }
          ]
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "2a2125ff-6acd-4aca-bc69-d148b6cbb678",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        0,
        20
      ],
      "parameters": {
        "color": 5,
        "width": 220,
        "height": 320,
        "content": "### Heads up!\nTo make sure everything works smoothly, use an [Airtop Profile](https://docs.airtop.ai/guides/how-to/saving-a-profile) signed into x.com for the \"Create session\" node"
      },
      "typeVersion": 1
    },
    {
      "id": "ca75bf36-55c4-4496-9a77-3870d078bec2",
      "name": "On form submission",
      "type": "n8n-nodes-base.formTrigger",
      "position": [
        -380,
        80
      ],
      "webhookId": "bf22d894-7313-40b1-aefa-98bc518473bf",
      "parameters": {
        "options": {
          "buttonLabel": "Post on X",
          "appendAttribution": false,
          "respondWithOptions": {
            "values": {
              "formSubmittedText": "✅ Your post has been published!"
            }
          }
        },
        "formTitle": "Post on X",
        "formFields": {
          "values": [
            {
              "fieldLabel": "Airtop profile name",
              "placeholder": "e.g. my-x-profile",
              "requiredField": true
            },
            {
              "fieldLabel": "Text to post",
              "placeholder": "e.g. This X post was made with Airtop and n8n",
              "requiredField": true
            }
          ]
        },
        "responseMode": "lastNode",
        "formDescription": "Enter the <a href=\"https://docs.airtop.ai/guides/how-to/saving-a-profile\" target=\"_blank\">Airtop Profile</a> and the content you would like to post on x.com"
      },
      "typeVersion": 2.2
    },
    {
      "id": "d56e067b-9825-4a81-88a4-c65dac5a919c",
      "name": "Parameters",
      "type": "n8n-nodes-base.set",
      "position": [
        -160,
        180
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "e612bf63-72bd-4b61-82c9-786a90b58b7b",
              "name": "airtop_profile",
              "type": "string",
              "value": "={{ $json[\"Airtop profile name\"] || $json.airtop_profile }}"
            },
            {
              "id": "567e5e7d-4efd-4d0a-a93c-6c7aed02c305",
              "name": "post_text",
              "type": "string",
              "value": "={{ $json[\"Text to post\"] || $json.post_text }}"
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
  "versionId": "9129144f-d078-48f8-825a-7f8bbda4570b",
  "connections": {
    "Type text": {
      "main": [
        [
          {
            "node": "Click on Post",
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
            "node": "Create session",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Click on Post": {
      "main": [
        [
          {
            "node": "End session",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Create window": {
      "main": [
        [
          {
            "node": "Type text",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Create session": {
      "main": [
        [
          {
            "node": "Create window",
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
            "node": "Parameters",
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

<a id="template-269"></a>

## Template 269 - Pesquisa web inteligente com reordenação semântica

- **Nome:** Pesquisa web inteligente com reordenação semântica
- **Descrição:** Fluxo que recebe uma pergunta via webhook, cria uma query de busca otimizada, consulta um motor de busca, reordena os resultados por relevância usando modelos de linguagem e retorna os principais links e informações extraídas em JSON.
- **Funcionalidade:** • Recepção de consulta via webhook: aceita a "Research Question" como entrada e inicia o processo.
• Registro de data e hora: anexa a data atual ao contexto para avaliar a atualidade das fontes.
• Geração automática de query de pesquisa: LLM elabora uma query concisa e otimizada a partir da pergunta do usuário.
• Consulta à API de busca web: executa a busca usando a query gerada e obtém títulos, URLs e descrições.
• Agregação de resultados: consolida títulos, links e descrições retornadas pela busca em texto estruturado.
• Re-ranqueamento semântico: modelos de linguagem avaliam e ordenam os resultados por relevância, credibilidade e adequação ao objetivo do usuário.
• Extração de informação: identifica e extrai trechos relevantes das descrições ou sinaliza "N/A" quando não há conteúdo útil.
• Geração de query de follow-up: propõe refinamentos de busca se os resultados forem insuficientes ou pouco promissores.
• Resposta formatada ao solicitante: devolve um JSON com até os 10 links mais bem ranqueados e o conteúdo extraído.
• Suporte a múltiplos modelos e parsing automático: permite usar diferentes modelos de linguagem e parsers de saída para robustez e correção.
• Instruções e configuração de API: inclui orientações para inserir a chave da API de busca e usar a chamada de webhook de teste.
- **Ferramentas:** • Brave Web Search API: serviço de busca web utilizado para recuperar resultados (títulos, URLs e descrições).
• Anthropic Claude: modelo de linguagem usado para re-ranqueamento semântico e análise crítica dos resultados.
• OpenAI (GPT): alternativa de modelo de linguagem empregada para geração e refinamento de queries e análise.
• Google Gemini / PaLM: modelo usado como parser/agent para processamento, correção e formatação de saídas.
• Endpoint HTTP externo (ex.: up.railway.app): URL de teste usada para enviar chamadas de webhook ao fluxo.



## Fluxo visual

```mermaid
flowchart LR
    N1["Sticky Note4"]
    N2["Sticky Note"]
    N3["Date & Time"]
    N4["Webhook"]
    N5["Auto-fixing Output Parser6"]
    N6["Auto-fixing Output Parser"]
    N7["Structured Output Parser1"]
    N8["Query-1 Combined"]
    N9["Respond to Webhook"]
    N10["Semantic Search - Result Re-Ranker"]
    N11["Query"]
    N12["Webhook Call"]
    N13["Sticky Note6"]
    N14["Semantic Search -Query Maker"]
    N15["Anthropic Chat Model"]
    N16["OpenAI Chat Model"]
    N17["Structured Output Parser2"]
    N18["Parser Model"]
    N19["Agent Model"]
    N20["Sticky Note5"]

    N11 --> N8
    N4 --> N3
    N3 --> N14
    N8 --> N10
    N14 --> N11
    N10 --> N9
```

## Fluxo (.json) :

```json
{
  "id": "wa2uEnSIowqSrHoY",
  "meta": {
    "instanceId": "cca06617664f52c5a019ea575691fdbce675dd95dc0452af5f13dbe76d615b69"
  },
  "name": "Intelligent Web Query and Semantic Re-Ranking Flow",
  "tags": [],
  "nodes": [
    {
      "id": "8e7dc5cb-6822-4ef6-9e5a-2b350a1526bf",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -640,
        -620
      ],
      "parameters": {
        "color": 5,
        "width": 1172,
        "height": 970,
        "content": "\n## Step 1. Set Up a Free Brave Web Search Query API Key\n\nTo attain the free web search API tier from Brave, follow these steps:\n\n1. Visit api.search.brave.com\n2. Create an account\n3. Subscribe to the free plan (no charge)\n4. Navigate to the API Keys section\n5. Generate an API key. For the subscription type, choose \"Free\".\n6. Go to the \"Query\" Nodes and change the \"X-Subscription-Token\" value to your API Key.\n"
      },
      "typeVersion": 1
    },
    {
      "id": "5bb3e68f-7693-4d4b-b794-843f2c3535e0",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -1580,
        -420
      ],
      "parameters": {
        "color": 4,
        "width": 680,
        "height": 360,
        "content": "## If you require to change this Node to Webhook Or any Other Item:\n\n- In case you want to change the input type from Webhook to any other item, Make sure to go to the Query 1 and Query 1 Ranker and replace the Webhook Input to your Node's input."
      },
      "typeVersion": 1
    },
    {
      "id": "f2fc02f9-a78a-4e87-be85-0032492a9f3f",
      "name": "Date & Time",
      "type": "n8n-nodes-base.dateTime",
      "position": [
        -820,
        -240
      ],
      "parameters": {
        "options": {}
      },
      "typeVersion": 2
    },
    {
      "id": "6f18ebbd-83db-4900-bc2e-0a9f23d6e8c8",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "position": [
        -1340,
        -240
      ],
      "webhookId": "962f1468-c80f-4c0c-8555-a0acf648ede4",
      "parameters": {
        "path": "962f1468-c80f-4c0c-8555-a0acf648ede4",
        "options": {},
        "responseMode": "responseNode"
      },
      "typeVersion": 2
    },
    {
      "id": "ba5ea83e-1b47-475b-863f-269ae293729a",
      "name": "Auto-fixing Output Parser6",
      "type": "@n8n/n8n-nodes-langchain.outputParserAutofixing",
      "position": [
        180,
        -140
      ],
      "parameters": {
        "options": {}
      },
      "typeVersion": 1
    },
    {
      "id": "ca426b6d-5412-4c5b-a55c-009a47c59a81",
      "name": "Auto-fixing Output Parser",
      "type": "@n8n/n8n-nodes-langchain.outputParserAutofixing",
      "position": [
        -580,
        -140
      ],
      "parameters": {
        "options": {}
      },
      "typeVersion": 1
    },
    {
      "id": "501d5390-5317-4973-a3e9-b0f502399c2b",
      "name": "Structured Output Parser1",
      "type": "@n8n/n8n-nodes-langchain.outputParserStructured",
      "position": [
        -460,
        -60
      ],
      "parameters": {
        "jsonSchemaExample": "{\n  \"reasoning_summary\": \"Detailed explanation of each analytical chain’s purpose and insights, including key terms and considerations for query formulation.\",\n  \"final_search_query\": \"The single, best-fit search query derived from the meta-reasoning and multi-chain analysis, optimized to answer the research question.\"\n}"
      },
      "typeVersion": 1.2
    },
    {
      "id": "a27e75c7-0307-4d71-9266-5a56b297a6e3",
      "name": "Query-1 Combined",
      "type": "n8n-nodes-base.code",
      "position": [
        -80,
        -240
      ],
      "parameters": {
        "jsCode": "// Initialize an empty string to store all title, url, and description pairs\nlet aggregatedOutputText = \"\";\n\n// Loop through all items passed to this Function node\nfor (let item of items) {\n  // Access the JSON data from \"Query 1\" node for the current item\n  const queryData = item.json;\n\n  // Ensure there is a \"web.results\" array to process\n  if (queryData.web?.results && Array.isArray(queryData.web.results)) {\n    // Loop through all results in the \"web.results\" array\n    for (let result of queryData.web.results) {\n      // Extract the title, url, and description for each result\n      const title = result.title || \"No Title\";\n      const url = result.url || \"No URL\";\n      const description = result.description || \"No Description\";\n\n      // Append the values to the aggregated string\n      aggregatedOutputText += `Title: ${title}\\nURL: ${url}\\nDescription: ${description}\\n\\n`;\n    }\n  } else {\n    // If no results array, handle gracefully\n    aggregatedOutputText += \"No results found for this item.\\n\\n\";\n  }\n}\n\n// Trim the final string to remove any trailing newline and whitespace\naggregatedOutputText = aggregatedOutputText.trim();\n\n// Return a single item containing the aggregated output as a string\nreturn [\n  {\n    json: {\n      aggregated_text: aggregatedOutputText\n    }\n  }\n];\n"
      },
      "typeVersion": 2
    },
    {
      "id": "acbdbe94-b5a7-4ec9-9fc8-c3ab147f42fa",
      "name": "Respond to Webhook",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        640,
        -240
      ],
      "parameters": {
        "options": {},
        "respondWith": "text",
        "responseBody": "={\n    \"Highest_RANKEDURL_1\": {\n        \"title\": \"{{ $item('0').$node['Semantic Search - Result Re-Ranker'].json['output']['Highest_RANKEDURL_1']['title'] }}\",\n        \"link\": \"{{ $item('0').$node['Semantic Search - Result Re-Ranker'].json['output']['Highest_RANKEDURL_1']['link'] }}\",\n        \"description\": \"{{ $item('0').$node['Semantic Search - Result Re-Ranker'].json['output']['Highest_RANKEDURL_1']['description'] }}\"\n    },\n    \"Highest_RANKEDURL_2\": {\n        \"title\": \"{{ $item('0').$node['Semantic Search - Result Re-Ranker'].json['output']['Highest_RANKEDURL_2']['title'] }}\",\n        \"link\": \"{{ $item('0').$node['Semantic Search - Result Re-Ranker'].json['output']['Highest_RANKEDURL_2']['link'] }}\",\n        \"description\": \"{{ $item('0').$node['Semantic Search - Result Re-Ranker'].json['output']['Highest_RANKEDURL_2']['description'] }}\"\n    },\n    \"Highest_RANKEDURL_3\": {\n        \"title\": \"{{ $item('0').$node['Semantic Search - Result Re-Ranker'].json['output']['Highest_RANKEDURL_3']['title'] }}\",\n        \"link\": \"{{ $item('0').$node['Semantic Search - Result Re-Ranker'].json['output']['Highest_RANKEDURL_3']['link'] }}\",\n        \"description\": \"{{ $item('0').$node['Semantic Search - Result Re-Ranker'].json['output']['Highest_RANKEDURL_3']['description'] }}\"\n    },\n    \"Highest_RANKEDURL_4\": {\n        \"title\": \"{{ $item('0').$node['Semantic Search - Result Re-Ranker'].json['output']['Highest_RANKEDURL_4']['title'] }}\",\n        \"link\": \"{{ $item('0').$node['Semantic Search - Result Re-Ranker'].json['output']['Highest_RANKEDURL_4']['link'] }}\",\n        \"description\": \"{{ $item('0').$node['Semantic Search - Result Re-Ranker'].json['output']['Highest_RANKEDURL_4']['description'] }}\"\n    },\n    \"Highest_RANKEDURL_5\": {\n        \"title\": \"{{ $item('0').$node['Semantic Search - Result Re-Ranker'].json['output']['Highest_RANKEDURL_5']['title'] }}\",\n        \"link\": \"{{ $item('0').$node['Semantic Search - Result Re-Ranker'].json['output']['Highest_RANKEDURL_5']['link'] }}\",\n        \"description\": \"{{ $item('0').$node['Semantic Search - Result Re-Ranker'].json['output']['Highest_RANKEDURL_5']['description'] }}\"\n    },\n    \"Highest_RANKEDURL_6\": {\n        \"title\": \"{{ $item('0').$node['Semantic Search - Result Re-Ranker'].json['output']['Highest_RANKEDURL_6']['title'] }}\",\n        \"link\": \"{{ $item('0').$node['Semantic Search - Result Re-Ranker'].json['output']['Highest_RANKEDURL_6']['link'] }}\",\n        \"description\": \"{{ $item('0').$node['Semantic Search - Result Re-Ranker'].json['output']['Highest_RANKEDURL_6']['description'] }}\"\n    },\n    \"Highest_RANKEDURL_7\": {\n        \"title\": \"{{ $item('0').$node['Semantic Search - Result Re-Ranker'].json['output']['Highest_RANKEDURL_7']['title'] }}\",\n        \"link\": \"{{ $item('0').$node['Semantic Search - Result Re-Ranker'].json['output']['Highest_RANKEDURL_7']['link'] }}\",\n        \"description\": \"{{ $item('0').$node['Semantic Search - Result Re-Ranker'].json['output']['Highest_RANKEDURL_7']['description'] }}\"\n    },\n    \"Highest_RANKEDURL_8\": {\n        \"title\": \"{{ $item('0').$node['Semantic Search - Result Re-Ranker'].json['output']['Highest_RANKEDURL_8']['title'] }}\",\n        \"link\": \"{{ $item('0').$node['Semantic Search - Result Re-Ranker'].json['output']['Highest_RANKEDURL_8']['link'] }}\",\n        \"description\": \"{{ $item('0').$node['Semantic Search - Result Re-Ranker'].json['output']['Highest_RANKEDURL_8']['description'] }}\"\n    },\n    \"Highest_RANKEDURL_9\": {\n        \"title\": \"{{ $item('0').$node['Semantic Search - Result Re-Ranker'].json['output']['Highest_RANKEDURL_9']['title'] }}\",\n        \"link\": \"{{ $item('0').$node['Semantic Search - Result Re-Ranker'].json['output']['Highest_RANKEDURL_9']['link'] }}\",\n        \"description\": \"{{ $item('0').$node['Semantic Search - Result Re-Ranker'].json['output']['Highest_RANKEDURL_9']['description'] }}\"\n    },\n    \"Highest_RANKEDURL_10\": {\n        \"title\": \"{{ $item('0').$node['Semantic Search - Result Re-Ranker'].json['output']['Highest_RANKEDURL_10']['title'] }}\",\n        \"link\": \"{{ $item('0').$node['Semantic Search - Result Re-Ranker'].json['output']['Highest_RANKEDURL_10']['link'] }}\",\n        \"description\": \"{{ $item('0').$node['Semantic Search - Result Re-Ranker'].json['output']['Highest_RANKEDURL_10']['description'] }}\"\n    },\n    \"Information_extracted\": \"{{ $item('0').$node['Semantic Search - Result Re-Ranker'].json['output']['Information_extracted'] }}\"\n}\n"
      },
      "typeVersion": 1.1
    },
    {
      "id": "b8b6ae73-586a-406f-9641-57e2625f800c",
      "name": "Semantic Search - Result Re-Ranker",
      "type": "@n8n/n8n-nodes-langchain.chainLlm",
      "onError": "continueRegularOutput",
      "position": [
        100,
        -240
      ],
      "parameters": {
        "text": "=\n**Objective:**\n\nFor the user's query, web search results are provided. Your tasks are:\n\n1. **Rank the links** based on how well they match the user's query.\n2. **Extract relevant information** from the descriptions provided. If no relevant information is found, return \"N/A\".\n\n---\n\n**Task:**\n\n**Step 1: Understand the User's Intent**\n\n- Determine what the user is truly and technically looking for.\n- The user's request query is: \"{{ $('Webhook').item.json.query['Research Question'] }}\"\n- The serach results below, however their  performance seem, have been based on this query \"{{ $item(\"0\").$node[\"Semantic Search -Query Maker\"].json[\"output\"][\"final_search_query\"] }}\". If the result are not satisfactory or missing due to bad query making, you should note that as well for the neww query making.\n- To nesure being time aware , realize todays date is: \"{{ $item(\"0\").$node[\"Date & Time\"].json[\"currentDate\"] }}\"\n\n- Follow a three-step chain of thought to comprehend the user's needs. Think out loud.\n\n---\n\n**Step 2: Rank the Links**\n\n- From the URLs and description snippets provided, **rank the top 10 websites** that are most likely to contain the required information.\n- Use the titles, descriptions, and sources to inform your ranking.\n\n**Links, Titles, and Descriptions:**\n\n{{ $json.aggregated_text }}\n\n---\n\nThis list completes the structure up to 20 results as you requested. Let me know if there’s anything more you need!\n\n---\n\n**Step 3: Analyze and Create a Follow-up Query**\n\n- Recognize that for the user's request:\n\n  `\"{{ $('Webhook').item.json.query['Research Question'] }}\"`\n\n  The results provided are based on the assistant's generated search query:\n\n  `\"{{ $item(\"0\").$node[\"Semantic Search -Query Maker\"].json[\"output\"][\"final_search_query\"] }}\"`\n\n- Analyze and revise any issues or new insights through multi-step thinking to create a follow-up query.\n\n**Indications and Priorities:**\n\n1. **No Results Received:** If no search items are shared, the search query may have been ineffective (e.g., too specific, incorrect parameters).\n2. **Insufficient or Unpromising Results:** If fewer than 20 but more than 5 results are provided, and none seem promising, the search query may need refinement.\n3. **Successful Results with Potential Follow-up:** If none of the above issues occurred and the search results provide answers or suggest a follow-up, create a new query. This could be a new topic, a deep dive, or a parallel factor that offers additional benefits.\n\n- Provide your chain of thought that connects the user's request to the actual information.\n\n- Deliver precise, detailed, and value-oriented information relevant to the user's query.\n\n**Step 4: Query making notes and examples**: \n\nThe queries must not be long tails , as they result in 0 websearch reutrns. We give you some examples of good web search queries:\nExamples:\n\nUser Question: \"What is the current state of the U.S. economy in 2024?\"\nEffective Search Query: \"U.S. Economy Analysis Report 2024\"\n\nUser Question: \"What are the recent advancements in artificial intelligence?\"\nEffective Search Query: \"2024 Artificial Intelligence Developments\"\n\nUser Question: \"How is climate change affecting agriculture globally?\"\nEffective Search Query: \"Global Impact of Climate Change on Agriculture 2024\"\n\nUser Question: \"What are the latest trends in cybersecurity threats?\"\nEffective Search Query: \"Cybersecurity Threats and Trends 2024\"\n\nUser Question: \"What is the outlook for renewable energy investments?\"\nEffective Search Query: \"Renewable Energy Investment Outlook 2024\"\n\n**Step 5: Query making*: \nor query making remember as we said:\n   - **Today's Date:** \"{{ $item(\"0\").$node[\"Date & Time\"].json[\"currentDate\"] }}\"\n **Search Inquiry:** \n   - **Search Topic to create the query upon it:**{{ $item(\"0\").$node[\"Webhook\"].json[\"query\"][\"Research Question\"] }}\"\"\n\n\n---\n\n**Step 6: Output Format**\n\nEnsure the response is in the following JSON format:\n\n{\n    \"chain_of_thought\": \"Insert your step-by-step reasoning here.\",\n    \"Highest_RANKEDURL_1\": {\n        \"title\": \"Insert the First Ranked URL's Title here.\",\n        \"link\": \"Insert the First Ranked URL here.\",\n        \"description\": \"Insert the First Ranked URL's Description here.\"\n    },\n    \"Highest_RANKEDURL_2\": {\n        \"title\": \"Insert the Second Ranked URL's Title here.\",\n        \"link\": \"Insert the Second Ranked URL here.\",\n        \"description\": \"Insert the Second Ranked URL's Description here.\"\n    },\n    \"Highest_RANKEDURL_3\": {\n        \"title\": \"Insert the Third Ranked URL's Title here.\",\n        \"link\": \"Insert the Third Ranked URL here.\",\n        \"description\": \"Insert the Third Ranked URL's Description here.\"\n    },\n    \"Highest_RANKEDURL_4\": {\n        \"title\": \"Insert the Fourth Ranked URL's Title here.\",\n        \"link\": \"Insert the Fourth Ranked URL here.\",\n        \"description\": \"Insert the Fourth Ranked URL's Description here.\"\n    },\n    \"Highest_RANKEDURL_5\": {\n        \"title\": \"Insert the Fifth Ranked URL's Title here.\",\n        \"link\": \"Insert the Fifth Ranked URL here.\",\n        \"description\": \"Insert the Fifth Ranked URL's Description here.\"\n    },\n    \"Highest_RANKEDURL_6\": {\n        \"title\": \"Insert the Sixth Ranked URL's Title here.\",\n        \"link\": \"Insert the Sixth Ranked URL here.\",\n        \"description\": \"Insert the Sixth Ranked URL's Description here.\"\n    },\n    \"Highest_RANKEDURL_7\": {\n        \"title\": \"Insert the Seventh Ranked URL's Title here.\",\n        \"link\": \"Insert the Seventh Ranked URL here.\",\n        \"description\": \"Insert the Seventh Ranked URL's Description here.\"\n    },\n    \"Highest_RANKEDURL_8\": {\n        \"title\": \"Insert the Eighth Ranked URL's Title here.\",\n        \"link\": \"Insert the Eighth Ranked URL here.\",\n        \"description\": \"Insert the Eighth Ranked URL's Description here.\"\n    },\n    \"Highest_RANKEDURL_9\": {\n        \"title\": \"Insert the Ninth Ranked URL's Title here.\",\n        \"link\": \"Insert the Ninth Ranked URL here.\",\n        \"description\": \"Insert the Ninth Ranked URL's Description here.\"\n    },\n    \"Highest_RANKEDURL_10\": {\n        \"title\": \"Insert the Tenth Ranked URL's Title here.\",\n        \"link\": \"Insert the Tenth Ranked URL here.\",\n        \"description\": \"Insert the Tenth Ranked URL's Description here.\"\n    },\n    \"Information_extracted\": \"Insert all extracted information relevant to the user's query or 'N/A' if none.\"\n}\n",
        "messages": {
          "messageValues": [
            {
              "message": "=\nYou are an expert information retrieval and critical evaluation assistant designed to process, rank, and extract high-relevance content from web search results for complex user queries. You must provide value-oriented insights while refining searches based on relevance and context sensitivity. \n\n**Your Process and Priorities:**\n\n#### 1. **Determine the User's Technical Intent**\n   - Interpret the user's core question provided as `{{ $item(\"0\").$node[\"Webhook\"].json[\"query\"][\"Research Question\"] }}`, discerning underlying objectives and specialized needs.\n   - Recognize that the search results may have been generated from a **secondary query**: `{{ $item(\"0\").$node[\"Semantic Search -Query Maker\"].json[\"output\"][\"final_search_query\"] }}`. \n   - Judge the adequacy of this generated query. If it does not meet the user’s objectives, highlight the need for query refinement and prepare to adapt the approach.\n   - Stay mindful of the date context, using `{{ $item(\"0\").$node[\"Date & Time\"].json[\"currentDate\"] }}` to assess the freshness of content or time-sensitive relevance.\n\n#### 2. **Rank Results Based on Analytical Relevance**\n   - From the search results provided, **rank the top 3 URLs** that most closely align with the user’s intent and technical needs.\n     - Use multi-dimensional analysis to assess how each link’s title, description, and source match the user’s objective.\n     - Prioritize results based on credibility, relevance, and their potential to add depth to the user’s inquiry.\n   - Your goal is to select the highest-value links, disregarding results that offer superficial, off-topic, or outdated information.\n\n#### 3. **Extract Key Information**\n   - For each of the top 3 ranked results, extract insights and details from the description snippets that directly address the user’s query.\n   - If no pertinent information is available in a description, record `\"N/A\"` to indicate its lack of relevance.\n\n#### 4. **Evaluate for Potential Query Improvement**\n   - Evaluate the relevance and coverage of search results:\n     - If fewer than 5 relevant results are present, consider that the initial query may be too narrow, specific, or otherwise misaligned.\n     - Generate a **refined query** that is adjusted to better match the user’s likely needs and produce higher-quality results.\n   - Use advanced language modifications, new keyword suggestions, or rephrasing to formulate a search query that enhances alignment with the user’s goals.\n"
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
      "id": "a1ca671d-0b0c-4717-9def-93fdb965de8d",
      "name": "Query",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        -240,
        -240
      ],
      "parameters": {
        "url": "https://api.search.brave.com/res/v1/web/search",
        "options": {},
        "sendQuery": true,
        "sendHeaders": true,
        "queryParameters": {
          "parameters": [
            {
              "name": "q",
              "value": "={{ $json.output.final_search_query }}"
            }
          ]
        },
        "headerParameters": {
          "parameters": [
            {
              "name": "Accept",
              "value": "application/json"
            },
            {
              "name": "Accept-Encoding",
              "value": "gzip"
            },
            {
              "name": "X-Subscription-Token",
              "value": "<Insert Your API Key Here>"
            }
          ]
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "d3cc4e7c-3ead-4d38-9b51-a11cd9d7faeb",
      "name": "Webhook Call",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        -180,
        1040
      ],
      "parameters": {
        "url": "https://primary-production-8aa4.up.railway.app/webhook-test/962f1468-c80f-4c0c-8555-a0acf648ede4",
        "options": {},
        "sendQuery": true,
        "queryParameters": {
          "parameters": [
            {
              "name": "Research Question",
              "value": "what is the latest news in global world in politics and economy?"
            }
          ]
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "6931404b-94d6-4b9d-9f0a-124012212eb5",
      "name": "Sticky Note6",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -640,
        420
      ],
      "parameters": {
        "color": 3,
        "width": 1180,
        "height": 840,
        "content": "## Step 2. Setup the Webhook Call Node\n\n**Instructions for Setting Up the Webhook Call and Using It in Your Workflow**\n\nThis node is designed to send a **web search query** to the workflow (partly built in this chart) and return the results. Follow these steps to correctly configure and use it:\n\n1. **Locate the \"Webhook\" Node in the Workflow**:\n   - Navigate to the workflow above, the first item, the \"Webhook\" node.\n   - In the \"Webhook\" node, change the **Webhook URL option** from \"Test URL\" to \"Production URL.\"\n   - Copy the generated **Production URL**.\n\n2. **Paste the Webhook URL in the HTTP Node**:\n   - In your target workflow, locate the **HTTP Request** node.\n   - Paste the copied **Production URL** into the URL field of the HTTP Request node. This connects the two workflows.\n\n3. **Send the Research Request**:\n   - When sending the request to this workflow, make sure to include your web search query in the **\"Research Question\" parameter** of the HTTP Request node.\n\n4. **Move the Webhook Call Node**:\n   - Move this **Webhook Call Node** into the workflow where you need the research results. Ensure that it’s correctly connected and configured to send the data to the main workflow.\n"
      },
      "typeVersion": 1
    },
    {
      "id": "01d73f91-1dd6-4b80-951c-9f944ea9d992",
      "name": "Semantic Search -Query Maker",
      "type": "@n8n/n8n-nodes-langchain.chainLlm",
      "position": [
        -560,
        -240
      ],
      "parameters": {
        "text": "=1. **Task:** `\"Your task is to develop a web search query that most effectively answers the research question given. Use meta-reasoning and multi-chain analysis to ensure a comprehensive approach.\"`\n\n2. **Structured Guidance for Chains of Thought:**  \n    a. **Chain 1:** Break down the research question, identifying keywords and relevant terms.  \n    b. **Chain 2:** Explore the context and potential sources, determining the types of results that would be most relevant.  \n    c. **Chain 3:** Refine the query for specificity and completeness, considering how to capture nuances of the question.\n\n3. **Final Query Generation:** Based on the insights from the three chains, generate a single, refined search query.\n\n\n4. Note, the queries must not be long tails , as they result in 0 websearch reutrns. We give you some examples of good web search queries:\nExamples:\n\nUser Question: \"What is the current state of the U.S. economy in 2024?\"\n\nEffective Search Query: \"U.S. Economy Analysis Report 2024\"\nUser Question: \"What are the recent advancements in artificial intelligence?\"\n\nEffective Search Query: \"2024 Artificial Intelligence Developments\"\nUser Question: \"How is climate change affecting agriculture globally?\"\n\nEffective Search Query: \"Global Impact of Climate Change on Agriculture 2024\"\nUser Question: \"What are the latest trends in cybersecurity threats?\"\n\nEffective Search Query: \"Cybersecurity Threats and Trends 2024\"\nUser Question: \"What is the outlook for renewable energy investments?\"\n\nEffective Search Query: \"Renewable Energy Investment Outlook 2024\"\n\n5. Data Input:\n   - **Today's Date:** \"{{ $item(\"0\").$node[\"Date & Time\"].json[\"currentDate\"] }}\"\n **Search Inquiry:** \n   - **Search Topic to create the query upon it:**{{ $item(\"0\").$node[\"Webhook\"].json[\"query\"][\"Research Question\"] }}\"\"\n\n6. Now develop the best fit web search query given the user request above under number 5\n---\n\n**Output Requirements:**  \nThe Assistant’s output should be in JSON format, structured as follows:\n\n{\n  \"reasoning_summary\": \"Detailed explanation of each analytical chain’s purpose and insights, including key terms and considerations for query formulation.\",\n  \"final_search_query\": \"The single, best-fit search query derived from the meta-reasoning and multi-chain analysis, optimized to answer the research question.\"\n}\n```\n\n---\n",
        "messages": {
          "messageValues": [
            {
              "message": "You are an advanced data and research retrieval through smart search queires via Bing and Brave websearch APIs. "
            },
            {
              "type": "HumanMessagePromptTemplate",
              "message": "1. **Task:** `\"Your task is to develop a web search query that most effectively answers the research question given. Use meta-reasoning and multi-chain analysis to ensure a comprehensive approach.\"`\n\n2. **Structured Guidance for Chains of Thought:**  \n    a. **Chain 1:** Break down the research question, identifying keywords and relevant terms.  \n    b. **Chain 2:** Explore the context and potential sources, determining the types of results that would be most relevant.  \n    c. **Chain 3:** Refine the query for specificity and completeness, considering how to capture nuances of the question.\n\n3. **Final Query Generation:** Based on the insights from the three chains, generate a single, refined search query.\n\n4. Data Input:\n   - **Today's Date:** \"2024-11-12T10:21:33.764-05:00\"\n2. **Search Inquiry:** \n   - **Search Topic to create the query upon it:** \"What is the latest stock Market Analysis in mid-term?\"\n\n\n---\n\n**Output Requirements:**  \nThe Assistant’s output should be in JSON format, structured as follows:\n\n{\n  \"reasoning_summary\": \"Detailed explanation of each analytical chain’s purpose and insights, including key terms and considerations for query formulation.\",\n  \"final_search_query\": \"The single, best-fit search query derived from the meta-reasoning and multi-chain analysis, optimized to answer the research question.\"\n}\n```\n\n---\n"
            },
            {
              "type": "AIMessagePromptTemplate",
              "message": "Assessing query functionality\n\nI’m evaluating the viability of the assistant's proposed search query. The user questions if it would yield meaningful results on different search engines.\n\nClarifying the query\n\nOK, let me see. The task involves clarifying the user's needs, ensuring the response aligns with OpenAI's policies, and possibly re-evaluating and correcting any errors in the previous response.\n\nRefining search specifics\n\nI'm working through refining the search query to focus on specific terms like 'S&P 500', integrating dates such as 'November 2024', and emphasizing phrases for precision.\n\nSelf-reflecting on search queries\n\nToday, I’m thinking about how to validate search queries for accuracy and realism, ensuring they are practical and likely to yield productive results.\n\nAcknowledging insights\n\nI’m recognizing and correcting a search query to ensure it’s optimal and effectively aligned with advanced user needs, leading to a more precise output.\n\nCrafting a search query\n\nI’m crafting a search query to pinpoint the most pertinent recent mid-term stock market analyses. Starting with relevant terms and then exploring potential sources for context and relevance.\n\nPinpointing sources and specifics\n\nI'm gathering info from financial news, investment reports, and economic research institutions. I’m refining search terms like \"mid-term stock market analysis\" and \"market forecast\" to keep results current and nuanced.\n\nCrafting the query\n\nI’m finalizing the query by merging terms like 'latest' and 'stock market analysis' with 'mid-term', and considering synonyms such as 'market forecast' to refine the search for 2024.\n\nTweaking the search\n\nI adjusted the search terms to 'latest stock market mid-term outlook 2024,' removing excessive quotes for better clarity and relevance.\n\n\n{\n  \"reasoning_summary\": \"Chain 1: Broke down the research question to identify key terms such as 'latest', 'stock market analysis', and 'mid-term'. Considered synonyms like 'mid-term outlook', 'market forecast', and included the current year '2024' for recency.\\n\\nChain 2: Explored the context where the user seeks recent analyses of the stock market with a mid-term perspective. Relevant sources would be financial news outlets, investment banks, and economic research firms. The most useful results would be up-to-date articles or reports offering mid-term forecasts.\\n\\nChain 3: Refined the query by removing unnecessary quotation marks and simplifying it to reflect how an advanced user might search. Included terms like 'latest', 'mid-term outlook', and '2024' to enhance specificity without limiting the search results unnecessarily.\",\n  \"final_search_query\": \"latest stock market mid-term outlook 2024\"\n}"
            }
          ]
        },
        "promptType": "define",
        "hasOutputParser": true
      },
      "typeVersion": 1.4
    },
    {
      "id": "696b4f97-ad29-406b-9157-44ad9d05c9cd",
      "name": "Anthropic Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatAnthropic",
      "position": [
        740,
        180
      ],
      "parameters": {
        "model": "claude-3-5-haiku-20241022",
        "options": {
          "topP": 0.8,
          "temperature": 0.4,
          "maxTokensToSample": 4096
        }
      },
      "credentials": {
        "anthropicApi": {
          "id": "mVKB2CryW6bMm9Qo",
          "name": "Anthropic account"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "82f25610-8b70-4aee-ad90-2616d3389f15",
      "name": "OpenAI Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        900,
        180
      ],
      "parameters": {
        "options": {
          "topP": 0.7,
          "maxTokens": 4096,
          "maxRetries": 1,
          "temperature": 0.5
        }
      },
      "credentials": {
        "openAiApi": {
          "id": "wQQZLwJO9A5nFu8h",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "f230bdf0-4a22-4abf-96cd-47f309f0c514",
      "name": "Structured Output Parser2",
      "type": "@n8n/n8n-nodes-langchain.outputParserStructured",
      "position": [
        260,
        -60
      ],
      "parameters": {
        "jsonSchemaExample": "{\n    \"chain_of_thought\": \"Insert your step-by-step reasoning here.\",\n    \"Highest_RANKEDURL_1\": {\n        \"title\": \"Insert the First Ranked URL's Title here.\",\n        \"link\": \"Insert the First Ranked URL here.\",\n        \"description\": \"Insert the First Ranked URL's Description here.\"\n    },\n    \"Highest_RANKEDURL_2\": {\n        \"title\": \"Insert the Second Ranked URL's Title here.\",\n        \"link\": \"Insert the Second Ranked URL here.\",\n        \"description\": \"Insert the Second Ranked URL's Description here.\"\n    },\n    \"Highest_RANKEDURL_3\": {\n        \"title\": \"Insert the Third Ranked URL's Title here.\",\n        \"link\": \"Insert the Third Ranked URL here.\",\n        \"description\": \"Insert the Third Ranked URL's Description here.\"\n    },\n    \"Highest_RANKEDURL_4\": {\n        \"title\": \"Insert the Fourth Ranked URL's Title here.\",\n        \"link\": \"Insert the Fourth Ranked URL here.\",\n        \"description\": \"Insert the Fourth Ranked URL's Description here.\"\n    },\n    \"Highest_RANKEDURL_5\": {\n        \"title\": \"Insert the Fifth Ranked URL's Title here.\",\n        \"link\": \"Insert the Fifth Ranked URL here.\",\n        \"description\": \"Insert the Fifth Ranked URL's Description here.\"\n    },\n    \"Highest_RANKEDURL_6\": {\n        \"title\": \"Insert the Sixth Ranked URL's Title here.\",\n        \"link\": \"Insert the Sixth Ranked URL here.\",\n        \"description\": \"Insert the Sixth Ranked URL's Description here.\"\n    },\n    \"Highest_RANKEDURL_7\": {\n        \"title\": \"Insert the Seventh Ranked URL's Title here.\",\n        \"link\": \"Insert the Seventh Ranked URL here.\",\n        \"description\": \"Insert the Seventh Ranked URL's Description here.\"\n    },\n    \"Highest_RANKEDURL_8\": {\n        \"title\": \"Insert the Eighth Ranked URL's Title here.\",\n        \"link\": \"Insert the Eighth Ranked URL here.\",\n        \"description\": \"Insert the Eighth Ranked URL's Description here.\"\n    },\n    \"Highest_RANKEDURL_9\": {\n        \"title\": \"Insert the Ninth Ranked URL's Title here.\",\n        \"link\": \"Insert the Ninth Ranked URL here.\",\n        \"description\": \"Insert the Ninth Ranked URL's Description here.\"\n    },\n    \"Highest_RANKEDURL_10\": {\n        \"title\": \"Insert the Tenth Ranked URL's Title here.\",\n        \"link\": \"Insert the Tenth Ranked URL here.\",\n        \"description\": \"Insert the Tenth Ranked URL's Description here.\"\n    },\n    \"Information_extracted\": \"Insert all extracted information relevant to the user's query or 'N/A' if none.\"\n}\n"
      },
      "typeVersion": 1.2
    },
    {
      "id": "3421ebe5-6a86-435e-b9c6-e3dcf6dd7833",
      "name": "Parser Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatGoogleGemini",
      "position": [
        -180,
        180
      ],
      "parameters": {
        "options": {
          "topP": 0.6,
          "temperature": 0.4,
          "maxOutputTokens": 4096
        },
        "modelName": "models/gemini-1.5-flash-002"
      },
      "credentials": {
        "googlePalmApi": {
          "id": "rTbWGMQGwWtjhNaA",
          "name": "Google Gemini(PaLM) Api account 4"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "fd19e9f6-d8c7-45df-93d9-ecf7956b461f",
      "name": "Agent Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatGoogleGemini",
      "position": [
        -180,
        -20
      ],
      "parameters": {
        "options": {
          "topP": 0.6,
          "temperature": 0.4,
          "safetySettings": {
            "values": [
              {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_NONE"
              },
              {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_NONE"
              },
              {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_NONE"
              },
              {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_NONE"
              }
            ]
          },
          "maxOutputTokens": 4086
        },
        "modelName": "models/gemini-1.5-flash-002"
      },
      "credentials": {
        "googlePalmApi": {
          "id": "rTbWGMQGwWtjhNaA",
          "name": "Google Gemini(PaLM) Api account 4"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "156e83ff-928a-4aca-af8b-0c0fa51acd56",
      "name": "Sticky Note5",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        560,
        -20
      ],
      "parameters": {
        "color": 6,
        "width": 712,
        "height": 370,
        "content": "\n## Customized Models to Replace\n\nIn case you rather to use another LLM Model to Perform the Semantic Search and Re-Ranking, These nodes below are Optimized based on the LLM Structure of OpenAI GPT4o & Anthropic Claude.\n"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "b824ca9d-5676-4ca5-b97d-e5113d955de2",
  "connections": {
    "Query": {
      "main": [
        [
          {
            "node": "Query-1 Combined",
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
            "node": "Date & Time",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Agent Model": {
      "ai_languageModel": [
        [
          {
            "node": "Semantic Search - Result Re-Ranker",
            "type": "ai_languageModel",
            "index": 0
          },
          {
            "node": "Semantic Search -Query Maker",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Date & Time": {
      "main": [
        [
          {
            "node": "Semantic Search -Query Maker",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Parser Model": {
      "ai_languageModel": [
        [
          {
            "node": "Auto-fixing Output Parser6",
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
    "Query-1 Combined": {
      "main": [
        [
          {
            "node": "Semantic Search - Result Re-Ranker",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Chat Model": {
      "ai_languageModel": [
        []
      ]
    },
    "Anthropic Chat Model": {
      "ai_languageModel": [
        []
      ]
    },
    "Auto-fixing Output Parser": {
      "ai_outputParser": [
        [
          {
            "node": "Semantic Search -Query Maker",
            "type": "ai_outputParser",
            "index": 0
          }
        ]
      ]
    },
    "Structured Output Parser1": {
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
    "Structured Output Parser2": {
      "ai_outputParser": [
        [
          {
            "node": "Auto-fixing Output Parser6",
            "type": "ai_outputParser",
            "index": 0
          }
        ]
      ]
    },
    "Auto-fixing Output Parser6": {
      "ai_outputParser": [
        [
          {
            "node": "Semantic Search - Result Re-Ranker",
            "type": "ai_outputParser",
            "index": 0
          }
        ]
      ]
    },
    "Semantic Search -Query Maker": {
      "main": [
        [
          {
            "node": "Query",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Semantic Search - Result Re-Ranker": {
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

<a id="template-270"></a>

## Template 270 - Servidor MCP para calendário e funções

- **Nome:** Servidor MCP para calendário e funções
- **Descrição:** Fluxo que implementa um servidor MCP para expor ferramentas acessíveis por IA, permitindo operações em calendário e chamadas a funções utilitárias como conversão de texto, geração de dados aleatórios e obtenção de piadas.
- **Funcionalidade:** • Exposição de ferramentas via MCP: disponibiliza endpoints SSE para que clientes possam descobrir e invocar ferramentas remotas.
• Orquestração por modelo de linguagem: recebe mensagens de chat e usa um modelo de linguagem para interpretar solicitações e decidir quais ferramentas chamar.
• Ferramentas de calendário: permite buscar, criar, atualizar e excluir eventos em um calendário conectado.
• Ferramentas de funções reutilizáveis: fornece sub-workflows acionáveis para conversão de texto (maiúsculas/minúsculas), geração de dados de usuários aleatórios e obtenção de piadas.
• Chamadas por outros fluxos: permite ser acionado por outro fluxo enviando nome da função e payload, com roteamento baseado no nome da função.
• Memória de contexto: mantém um buffer de conversação para preservar contexto entre interações.
• Filtragem e formatação de saída: processa respostas das ferramentas para retornar apenas os campos relevantes ao solicitante.
• Integração com APIs externas: consulta APIs públicas quando necessário (por exemplo, para obter piadas).
- **Ferramentas:** • OpenAI (gpt-4o): modelo de linguagem usado para interpretar comandos, gerar respostas e orquestrar chamadas às ferramentas.
• Google Calendar: serviço de calendário usado para buscar, criar, atualizar e excluir eventos do usuário via credenciais OAuth2.
• Official Joke API: API pública usada para obter piadas aleatórias quando solicitado.



## Fluxo visual

```mermaid
flowchart LR
    N1["AI Agent"]
    N2["SearchEvent"]
    N3["CreateEvent"]
    N4["UpdateEvent"]
    N5["DeleteEvent"]
    N6["Google Calendar MCP"]
    N7["When Executed by Another Workflow"]
    N8["Switch"]
    N9["Convert Text to Upper Case"]
    N10["Convert Text to Lower Case"]
    N11["Convert Text"]
    N12["When chat message received"]
    N13["Simple Memory"]
    N14["Calendar MCP"]
    N15["My Functions"]
    N16["Sticky Note"]
    N17["My Functions Server"]
    N18["Sticky Note1"]
    N19["Random user data"]
    N20["Sticky Note2"]
    N21["Generate random user data"]
    N22["Return only some fields"]
    N23["Joke Request"]
    N24["Random Jokes"]
    N25["Sticky Note3"]
    N26["Sticky Note4"]
    N27["Sticky Note5"]
    N28["Sticky Note6"]
    N29["OpenAI 4o"]
    N30["Sticky Note7"]
    N31["Sticky Note8"]
    N32["Sticky Note9"]

    N8 --> N9
    N8 --> N10
    N8 --> N19
    N8 --> N23
    N19 --> N22
    N12 --> N1
    N7 --> N8
```

## Fluxo (.json) :

```json
{
  "id": "8n0VYmvJgISwezyz",
  "meta": {
    "instanceId": "cf0c5836fa3beacaef0de12624775e6f153c527586d6a910f5e2be3bb2e519a3",
    "templateCredsSetupCompleted": true
  },
  "name": "Build your first AI MCP Server",
  "tags": [],
  "nodes": [
    {
      "id": "f734e72b-1954-44e8-8633-47b6fa69bfc7",
      "name": "AI Agent",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        -440,
        -160
      ],
      "parameters": {
        "options": {
          "systemMessage": "=You are a helpful assistant.\nCurrent datetime is {{ $now.toString() }}"
        }
      },
      "typeVersion": 1.8
    },
    {
      "id": "02c66e36-63e6-48f5-a26a-2c7b1eaf2400",
      "name": "SearchEvent",
      "type": "n8n-nodes-base.googleCalendarTool",
      "position": [
        1180,
        200
      ],
      "parameters": {
        "limit": "={{ /*n8n-auto-generated-fromAI-override*/ $fromAI('Limit', ``, 'number') }}",
        "options": {},
        "timeMax": "={{ /*n8n-auto-generated-fromAI-override*/ $fromAI('Before', ``, 'string') }}",
        "timeMin": "={{ /*n8n-auto-generated-fromAI-override*/ $fromAI('After', ``, 'string') }}",
        "calendar": {
          "__rl": true,
          "mode": "list",
          "value": "gmsalomao2@gmail.com",
          "cachedResultName": "gmsalomao2@gmail.com"
        },
        "operation": "getAll"
      },
      "credentials": {
        "googleCalendarOAuth2Api": {
          "id": "imp2lyvMg9IpuCwC",
          "name": "Google Calendar account"
        }
      },
      "typeVersion": 1.3
    },
    {
      "id": "5956abba-4458-480c-997f-416126dc8c10",
      "name": "CreateEvent",
      "type": "n8n-nodes-base.googleCalendarTool",
      "position": [
        1300,
        200
      ],
      "parameters": {
        "end": "={{ /*n8n-auto-generated-fromAI-override*/ $fromAI('End', ``, 'string') }}",
        "start": "={{ /*n8n-auto-generated-fromAI-override*/ $fromAI('Start', ``, 'string') }}",
        "calendar": {
          "__rl": true,
          "mode": "list",
          "value": "gmsalomao2@gmail.com",
          "cachedResultName": "gmsalomao2@gmail.com"
        },
        "additionalFields": {
          "summary": "={{ $fromAI(\"event_title\", \"The event title\", \"string\") }}",
          "description": "={{ $fromAI(\"event_description\", \"The event description\", \"string\") }}"
        }
      },
      "credentials": {
        "googleCalendarOAuth2Api": {
          "id": "imp2lyvMg9IpuCwC",
          "name": "Google Calendar account"
        }
      },
      "typeVersion": 1.3
    },
    {
      "id": "f12fd8d6-1600-4516-bbb0-a0a893e2ff25",
      "name": "UpdateEvent",
      "type": "n8n-nodes-base.googleCalendarTool",
      "position": [
        1420,
        200
      ],
      "parameters": {
        "eventId": "={{ /*n8n-auto-generated-fromAI-override*/ $fromAI('Event_ID', ``, 'string') }}",
        "calendar": {
          "__rl": true,
          "mode": "list",
          "value": "gmsalomao2@gmail.com",
          "cachedResultName": "gmsalomao2@gmail.com"
        },
        "operation": "update",
        "updateFields": {
          "end": "={{ /*n8n-auto-generated-fromAI-override*/ $fromAI('End', ``, 'string') }}",
          "start": "={{ /*n8n-auto-generated-fromAI-override*/ $fromAI('Start', ``, 'string') }}",
          "summary": "={{ $fromAI(\"event_title\", \"The event title\", \"string\") }}",
          "description": "={{ $fromAI(\"event_description\", \"The event description\", \"string\") }}"
        }
      },
      "credentials": {
        "googleCalendarOAuth2Api": {
          "id": "imp2lyvMg9IpuCwC",
          "name": "Google Calendar account"
        }
      },
      "typeVersion": 1.3
    },
    {
      "id": "b9c6d019-cf0a-4192-b063-e94322f12dae",
      "name": "DeleteEvent",
      "type": "n8n-nodes-base.googleCalendarTool",
      "position": [
        1540,
        200
      ],
      "parameters": {
        "eventId": "={{ /*n8n-auto-generated-fromAI-override*/ $fromAI('Event_ID', ``, 'string') }}",
        "options": {},
        "calendar": {
          "__rl": true,
          "mode": "list",
          "value": "gmsalomao2@gmail.com",
          "cachedResultName": "gmsalomao2@gmail.com"
        },
        "operation": "delete"
      },
      "credentials": {
        "googleCalendarOAuth2Api": {
          "id": "imp2lyvMg9IpuCwC",
          "name": "Google Calendar account"
        }
      },
      "typeVersion": 1.3
    },
    {
      "id": "48e028c3-392f-429c-9e71-a3cbdb342a99",
      "name": "Google Calendar MCP",
      "type": "@n8n/n8n-nodes-langchain.mcpTrigger",
      "position": [
        1180,
        0
      ],
      "webhookId": "f9d9d5ea-6f83-42c8-ae50-ee6c71789bca",
      "parameters": {
        "path": "my-calendar"
      },
      "typeVersion": 1
    },
    {
      "id": "fede10f5-e75b-4851-834f-f248f07a5559",
      "name": "When Executed by Another Workflow",
      "type": "n8n-nodes-base.executeWorkflowTrigger",
      "position": [
        560,
        900
      ],
      "parameters": {
        "workflowInputs": {
          "values": [
            {
              "name": "function_name"
            },
            {
              "name": "payload",
              "type": "object"
            }
          ]
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "bc77345e-e6e0-4529-97f0-872eb96d1631",
      "name": "Switch",
      "type": "n8n-nodes-base.switch",
      "position": [
        780,
        880
      ],
      "parameters": {
        "rules": {
          "values": [
            {
              "outputKey": "UPPERCASE",
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
                    "id": "ab18304c-4f73-430f-b9fa-2ce4d098e1fa",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $json.function_name }}",
                    "rightValue": "uppercase"
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "LOWERCASE",
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
                    "id": "606bda79-f401-4de2-be9d-51368c794479",
                    "operator": {
                      "name": "filter.operator.equals",
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $json.function_name }}",
                    "rightValue": "lowercase"
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "RANDOM DATA",
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
                    "id": "4b22e689-e652-47d2-b737-7be00da9f185",
                    "operator": {
                      "name": "filter.operator.equals",
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $json.function_name }}",
                    "rightValue": "random_user_data"
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "JOKE",
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
                    "id": "27a75a2c-8058-4a7c-85c1-898cabeac4a1",
                    "operator": {
                      "name": "filter.operator.equals",
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $json.function_name }}",
                    "rightValue": "joke"
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
      "id": "abc580fa-3293-443d-a3a3-5d12c0655be2",
      "name": "Convert Text to Upper Case",
      "type": "n8n-nodes-base.set",
      "position": [
        1120,
        540
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "42333f26-8e14-438a-9965-eec31bf4b6a3",
              "name": "converted_text",
              "type": "string",
              "value": "={{ $json.payload.text.toUpperCase() }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "37d2337c-3ccf-4c34-8284-5acc6cbb89fe",
      "name": "Convert Text to Lower Case",
      "type": "n8n-nodes-base.set",
      "position": [
        1120,
        740
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "42333f26-8e14-438a-9965-eec31bf4b6a3",
              "name": "converted_text",
              "type": "string",
              "value": "={{ $json.payload.text.toLowerCase() }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "138d2f10-deca-41c7-bec0-8a7727993d44",
      "name": "Convert Text",
      "type": "@n8n/n8n-nodes-langchain.toolWorkflow",
      "position": [
        560,
        200
      ],
      "parameters": {
        "name": "convert_text_case",
        "workflowId": {
          "__rl": true,
          "mode": "id",
          "value": "={{ $workflow.id }}"
        },
        "description": "Call this tool to convert text to lower case or upper case.",
        "workflowInputs": {
          "value": {
            "payload": "={\n  \"text\": \"{{ $fromAI(\"text_to_convert\", \"The text to convert\", \"string\") }}\"\n}\n",
            "function_name": "={{ $fromAI(\"function_name\", \"Either lowercase or uppercase\", \"string\") }}"
          },
          "schema": [
            {
              "id": "function_name",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "function_name",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "payload",
              "type": "object",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "payload",
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
      "id": "bf198087-b571-4de3-a174-c53b769c1326",
      "name": "When chat message received",
      "type": "@n8n/n8n-nodes-langchain.chatTrigger",
      "position": [
        -640,
        -160
      ],
      "webhookId": "7b02318f-1c6b-4f2a-9a4f-b17fa69ea680",
      "parameters": {
        "options": {}
      },
      "typeVersion": 1.1
    },
    {
      "id": "df4435ad-0512-4a50-9eaf-2aef566c5fdb",
      "name": "Simple Memory",
      "type": "@n8n/n8n-nodes-langchain.memoryBufferWindow",
      "position": [
        -340,
        60
      ],
      "parameters": {},
      "typeVersion": 1.3
    },
    {
      "id": "60745d31-1892-45c1-82b2-bb67386f4384",
      "name": "Calendar MCP",
      "type": "@n8n/n8n-nodes-langchain.mcpClientTool",
      "position": [
        200,
        80
      ],
      "parameters": {
        "sseEndpoint": "https://n8n.yourdomain/mcp/my-calendar/sse"
      },
      "typeVersion": 1
    },
    {
      "id": "17bef416-fd54-47da-87c7-afd7e6fa5345",
      "name": "My Functions",
      "type": "@n8n/n8n-nodes-langchain.mcpClientTool",
      "position": [
        40,
        80
      ],
      "parameters": {
        "sseEndpoint": "https://n8n.yourdomain/mcp/my-functions/sse"
      },
      "typeVersion": 1
    },
    {
      "id": "d883db20-c3d9-47bf-b19b-85098067054a",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        440,
        -160
      ],
      "parameters": {
        "color": 3,
        "width": 620,
        "height": 520,
        "content": "## Activate the workflow to make the MCP Trigger work\nIn order to make the MCP server available, you need to activate the workflow.\n\nThen copy the Production URL of the MCP Trigger and paste it in the corresponding MCP Client tool."
      },
      "typeVersion": 1
    },
    {
      "id": "83b21003-eced-444c-ae5c-2fe77ed31fa9",
      "name": "My Functions Server",
      "type": "@n8n/n8n-nodes-langchain.mcpTrigger",
      "position": [
        560,
        0
      ],
      "webhookId": "83f72547-18b7-4f02-846b-27bf39d1efff",
      "parameters": {
        "path": "my-functions"
      },
      "typeVersion": 1
    },
    {
      "id": "4bc297bc-8ded-4e6e-aa2d-de2f41659864",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -60,
        -160
      ],
      "parameters": {
        "color": 7,
        "width": 440,
        "height": 520,
        "content": "## MCP Clients\nFor every tool here you need to obtain he corresponding Production URL from the MCP Triggers on the right 👉"
      },
      "typeVersion": 1
    },
    {
      "id": "2ad20ab6-b8a6-4427-af03-fbc512f0aa3c",
      "name": "Random user data",
      "type": "n8n-nodes-base.debugHelper",
      "position": [
        1120,
        1040
      ],
      "parameters": {
        "category": "randomData",
        "randomDataCount": "={{ $json.payload.number }}"
      },
      "typeVersion": 1
    },
    {
      "id": "84435164-94c8-4093-8578-81d5a870bef5",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -1360,
        -160
      ],
      "parameters": {
        "color": 7,
        "width": 620,
        "height": 640,
        "content": "# Try these example requests with the AI Agent\n\n### My Functions MCP\n1. Use your tools to convert this text to lower case: `EXAMPLE TeXt`\n\n2. Use your tools to convert this text to upper case: `example TeXt`\n\n3. Generate 5 random user data, please.\n\n4. Please obtain 3 jokes.\n\n\n\n\n### Calendar MCP\n5. What is my schedule for next week?\n\n6. I have a meeting with John tomorrow at 2pm. Please add it to my Calendar.\n\n7. Adjust the time of my meeting with John tomorrow from 2pm to 4pm, please.\n\n8. Cancel my meeting with John, tomorrow."
      },
      "typeVersion": 1
    },
    {
      "id": "d678dc07-1c44-4bdb-9707-dc544cd813b2",
      "name": "Generate random user data",
      "type": "@n8n/n8n-nodes-langchain.toolWorkflow",
      "position": [
        720,
        200
      ],
      "parameters": {
        "name": "random_user_data",
        "workflowId": {
          "__rl": true,
          "mode": "id",
          "value": "={{ $workflow.id }}"
        },
        "description": "Generate random user data",
        "workflowInputs": {
          "value": {
            "payload": "={\n  \"number\": {{ $fromAI(\"amount\", \"The amount of user data to generate in integer format\", \"number\") }}\n}",
            "function_name": "random_user_data"
          },
          "schema": [
            {
              "id": "function_name",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "function_name",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "payload",
              "type": "object",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "payload",
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
      "id": "38f22f69-c6e0-49d8-837c-64e72743ffbf",
      "name": "Return only some fields",
      "type": "n8n-nodes-base.set",
      "position": [
        1340,
        1040
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "b4548cbe-f3fc-4911-901a-d73182d710a9",
              "name": "First name",
              "type": "string",
              "value": "={{ $json.firstname }}"
            },
            {
              "id": "6e573a27-ef03-4254-8f9b-2c471e1540c2",
              "name": "Last name",
              "type": "string",
              "value": "={{ $json.lastname }}"
            },
            {
              "id": "ac5b5806-bf8e-4e1a-a47d-e7180d31e98a",
              "name": "Email",
              "type": "string",
              "value": "={{ $json.email }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "a66e8f27-ebf5-460b-898f-b91017d37883",
      "name": "Joke Request",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1120,
        1240
      ],
      "parameters": {
        "url": "=https://official-joke-api.appspot.com/jokes/random/{{ $json.payload.number }}",
        "options": {}
      },
      "typeVersion": 4.2
    },
    {
      "id": "98205665-4b35-4850-9f37-df1688edde85",
      "name": "Random Jokes",
      "type": "@n8n/n8n-nodes-langchain.toolWorkflow",
      "position": [
        880,
        200
      ],
      "parameters": {
        "name": "obtain_jokes",
        "workflowId": {
          "__rl": true,
          "mode": "id",
          "value": "={{ $workflow.id }}"
        },
        "description": "Call this tool to obtain random jokes",
        "workflowInputs": {
          "value": {
            "payload": "={\n  \"number\": {{ $fromAI(\"amount\", \"The amount of jokes to request\", \"number\") }}\n}",
            "function_name": "joke"
          },
          "schema": [
            {
              "id": "function_name",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "function_name",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "payload",
              "type": "object",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "payload",
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
      "id": "643221de-4ec5-45c2-818d-e754e2b76377",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        440,
        380
      ],
      "parameters": {
        "color": 7,
        "width": 1260,
        "height": 1060,
        "content": "## The My Functions MCP calls this sub-workflow every time.\nA subworkflow is a separate workflow that can be called by other workflows and is able to receive parameters.\nLearn more about sub-workflows **[here](https://docs.n8n.io/flow-logic/subworkflows/)**"
      },
      "typeVersion": 1
    },
    {
      "id": "ff5dafdc-02f2-4a40-a803-044e18f6d680",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1080,
        -160
      ],
      "parameters": {
        "color": 5,
        "width": 620,
        "height": 520,
        "content": "## Google Calendar tools require credentials\nIf you don't have your Google Credentials set up in n8n yet, watch [this](https://www.youtube.com/watch?v=3Ai1EPznlAc) video to learn how to do it.\n\nIf you are using n8n Cloud plans, it's very intuitive to setup and you may not even need the tutorial."
      },
      "typeVersion": 1
    },
    {
      "id": "cb113628-48c3-4be7-8306-c60e92bbd295",
      "name": "Sticky Note5",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -1360,
        500
      ],
      "parameters": {
        "color": 7,
        "width": 620,
        "height": 580,
        "content": "# Author\n![Solomon](https://gravatar.com/avatar/79aa147f090807fe0f618fb47a1de932669e385bb0c84bf3a7f891ae7d174256?r=pg&d=retro&size=200)\n### Solomon\nFreelance consultant from Brazil, specializing in automations and data analysis. I work with select clients, addressing their toughest projects.\n\nCurrently running the [Scrapes community](https://www.skool.com/scrapes/about?ref=21f10ad99f4d46ba9b8aaea8c9f58c34) with Simon 💪\n\nFor business inquiries, email me at automations.solomon@gmail.com\nOr message me on [Telegram](https://t.me/salomaoguilherme) for a faster response.\n\n## Check out my other templates\n### 👉 https://n8n.io/creators/solomon/\n"
      },
      "typeVersion": 1
    },
    {
      "id": "83f39d92-73a8-480f-bf66-0996a54c39b9",
      "name": "Sticky Note6",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -1360,
        1100
      ],
      "parameters": {
        "width": 620,
        "height": 180,
        "content": "# Need help?\nFor getting help with this workflow, please create a topic on the community forums here:\nhttps://community.n8n.io/c/questions/"
      },
      "typeVersion": 1
    },
    {
      "id": "d6dfab2b-3c55-40b1-ac84-2a30650089f2",
      "name": "OpenAI 4o",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        -480,
        60
      ],
      "parameters": {
        "model": {
          "__rl": true,
          "mode": "list",
          "value": "gpt-4o",
          "cachedResultName": "gpt-4o"
        },
        "options": {}
      },
      "credentials": {
        "openAiApi": {
          "id": "1OcDEFHmAarBeW0G",
          "name": "n8n-testing2"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "7452095e-d893-40c0-a099-302572dcc513",
      "name": "Sticky Note7",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -640,
        180
      ],
      "parameters": {
        "color": 7,
        "height": 240,
        "content": "## Why model 4o? 👆\nAfter testing 4o-mini it had some difficulties handling the calendar requests, while the 4o model handled it with ease.\n\nDepending on your prompt and tools, 4o-mini might be able to work well too, but it requires further testing."
      },
      "typeVersion": 1
    },
    {
      "id": "33687586-79d7-4a59-bec0-09fd09bc0a7d",
      "name": "Sticky Note8",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -1360,
        -320
      ],
      "parameters": {
        "color": 4,
        "width": 3060,
        "height": 140,
        "content": ""
      },
      "typeVersion": 1
    },
    {
      "id": "02d2a399-36ca-4580-8442-59a7752e3808",
      "name": "Sticky Note9",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -240,
        -280
      ],
      "parameters": {
        "color": 4,
        "width": 800,
        "height": 80,
        "content": "# Learn How to Build an MCP Server and Client"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {
    "When Executed by Another Workflow": [
      {
        "json": {
          "payload": {
            "number": 5
          },
          "function_name": "joke"
        }
      }
    ]
  },
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "1da3b8d6-0a3e-472d-84f3-06771229901f",
  "connections": {
    "Switch": {
      "main": [
        [
          {
            "node": "Convert Text to Upper Case",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Convert Text to Lower Case",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Random user data",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Joke Request",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI 4o": {
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
    "CreateEvent": {
      "ai_tool": [
        [
          {
            "node": "Google Calendar MCP",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "DeleteEvent": {
      "ai_tool": [
        [
          {
            "node": "Google Calendar MCP",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "SearchEvent": {
      "ai_tool": [
        [
          {
            "node": "Google Calendar MCP",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "UpdateEvent": {
      "ai_tool": [
        [
          {
            "node": "Google Calendar MCP",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Calendar MCP": {
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
    "Convert Text": {
      "ai_tool": [
        [
          {
            "node": "My Functions Server",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "My Functions": {
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
    "Random Jokes": {
      "ai_tool": [
        [
          {
            "node": "My Functions Server",
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
            "node": "AI Agent",
            "type": "ai_memory",
            "index": 0
          }
        ]
      ]
    },
    "Random user data": {
      "main": [
        [
          {
            "node": "Return only some fields",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Generate random user data": {
      "ai_tool": [
        [
          {
            "node": "My Functions Server",
            "type": "ai_tool",
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
    "When Executed by Another Workflow": {
      "main": [
        [
          {
            "node": "Switch",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-271"></a>

## Template 271 - Detecção de Bounding Boxes com Gemini 2.0

- **Nome:** Detecção de Bounding Boxes com Gemini 2.0
- **Descrição:** Fluxo que baixa uma imagem de teste, usa Gemini 2.0 para detectar caixas delimitadoras de coelhos, ajusta as coordenadas para a imagem original e desenha as caixas sobre a imagem.
- **Funcionalidade:** • Baixar imagem de teste: o fluxo baixa a imagem de teste para processamento.
• Detectar bounding boxes com prompt: envia a imagem para o modelo Gemini 2.0 com um prompt para retornar as caixas delimitadoras.
• Converter coordenadas para pixels: transforma as coordenadas normalizadas (0-1000) em posições de pixel usando a largura e altura da imagem.
• Desenhar bounding boxes na imagem: desenha as caixas sobre a imagem original.
• Gerar saída visual com caixas: prepara a imagem final com caixas para visualização.
- **Ferramentas:** • Gemini 2.0 API: API de detecção de objetos baseada em prompt que retorna bounding boxes.
• Imagem de teste online: URL de uma imagem pública usada como entrada para o fluxo.



## Fluxo visual

```mermaid
flowchart LR
    N1["When clicking ‘Test workflow’"]
    N2["Get Variables"]
    N3["Get Test Image"]
    N4["Gemini 2.0 Object Detection"]
    N5["Scale Normalised Coords"]
    N6["Draw Bounding Boxes"]
    N7["Get Image Info"]
    N8["Sticky Note"]
    N9["Sticky Note1"]
    N10["Sticky Note2"]
    N11["Sticky Note3"]
    N12["Sticky Note4"]
    N13["Sticky Note5"]
    N14["Sticky Note6"]

    N2 --> N5
    N7 --> N4
    N3 --> N7
    N5 --> N6
    N4 --> N2
    N1 --> N3
```

## Fluxo (.json) :

```json
{
  "nodes": [
    {
      "id": "bae5d407-9210-4bd0-99a3-3637ee893065",
      "name": "When clicking ‘Test workflow’",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        -1440,
        -280
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "c5a14c8e-4aeb-4a4e-b202-f88e837b6efb",
      "name": "Get Variables",
      "type": "n8n-nodes-base.set",
      "position": [
        -200,
        -180
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "b455afe0-2311-4d3f-8751-269624d76cf1",
              "name": "coords",
              "type": "array",
              "value": "={{ $json.candidates[0].content.parts[0].text.parseJson() }}"
            },
            {
              "id": "92f09465-9a0b-443c-aa72-6d208e4df39c",
              "name": "width",
              "type": "string",
              "value": "={{ $('Get Image Info').item.json.size.width }}"
            },
            {
              "id": "da98ce2a-4600-46a6-b4cb-159ea515cb50",
              "name": "height",
              "type": "string",
              "value": "={{ $('Get Image Info').item.json.size.height }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "f24017c9-05bc-4f75-a18c-29efe99bfe0e",
      "name": "Get Test Image",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        -1260,
        -280
      ],
      "parameters": {
        "url": "https://www.stonhambarns.co.uk/wp-content/uploads/jennys-ark-petting-zoo-for-website-6.jpg",
        "options": {}
      },
      "typeVersion": 4.2
    },
    {
      "id": "c0f6a9f7-ba65-48a3-8752-ce5d80fe33cf",
      "name": "Gemini 2.0 Object Detection",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        -680,
        -180
      ],
      "parameters": {
        "url": "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent",
        "method": "POST",
        "options": {},
        "jsonBody": "={{\n{\n \"contents\": [{\n \"parts\":[\n {\"text\": \"I want to see all bounding boxes of rabbits in this image.\"},\n {\n \"inline_data\": {\n \"mime_type\":\"image/jpeg\",\n \"data\": $input.item.binary.data.data\n }\n }\n ]\n }],\n \"generationConfig\": {\n \"response_mime_type\": \"application/json\",\n \"response_schema\": {\n \"type\": \"ARRAY\",\n \"items\": {\n \"type\": \"OBJECT\",\n \"properties\": {\n \"box_2d\": {\"type\":\"ARRAY\", \"items\": { \"type\": \"NUMBER\" } },\n \"label\": { \"type\": \"STRING\"}\n }\n }\n }\n }\n}\n}}",
        "sendBody": true,
        "specifyBody": "json",
        "authentication": "predefinedCredentialType",
        "nodeCredentialType": "googlePalmApi"
      },
      "credentials": {
        "googlePalmApi": {
          "id": "dSxo6ns5wn658r8N",
          "name": "Google Gemini(PaLM) Api account"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "edbc1152-4642-4656-9a3a-308dae42bac6",
      "name": "Scale Normalised Coords",
      "type": "n8n-nodes-base.code",
      "position": [
        -20,
        -180
      ],
      "parameters": {
        "jsCode": "const { coords, width, height } = $input.first().json;\n\nconst scale = 1000;\nconst scaleCoordX = (val) => (val * width) / scale;\nconst scaleCoordY = (val) => (val * height) / scale;\n \nconst normalisedOutput = coords\n .filter(coord => coord.box_2d.length === 4)\n .map(coord => {\n return {\n xmin: coord.box_2d[1] ? scaleCoordX(coord.box_2d[1]) : coord.box_2d[1],\n xmax: coord.box_2d[3] ? scaleCoordX(coord.box_2d[3]) : coord.box_2d[3],\n ymin: coord.box_2d[0] ? scaleCoordY(coord.box_2d[0]) : coord.box_2d[0],\n ymax: coord.box_2d[2] ? scaleCoordY(coord.box_2d[2]) : coord.box_2d[2],\n }\n });\n\nreturn {\n json: {\n coords: normalisedOutput\n },\n binary: $('Get Test Image').first().binary\n}"
      },
      "typeVersion": 2
    },
    {
      "id": "e0380611-ac7d-48d8-8eeb-35de35dbe56a",
      "name": "Draw Bounding Boxes",
      "type": "n8n-nodes-base.editImage",
      "position": [
        400,
        -180
      ],
      "parameters": {
        "options": {},
        "operation": "multiStep",
        "operations": {
          "operations": [
            {
              "color": "#ff00f277",
              "operation": "draw",
              "endPositionX": "={{ $json.coords[0].xmax }}",
              "endPositionY": "={{ $json.coords[0].ymax }}",
              "startPositionX": "={{ $json.coords[0].xmin }}",
              "startPositionY": "={{ $json.coords[0].ymin }}"
            },
            {
              "color": "#ff00f277",
              "operation": "draw",
              "endPositionX": "={{ $json.coords[1].xmax }}",
              "endPositionY": "={{ $json.coords[1].ymax }}",
              "startPositionX": "={{ $json.coords[1].xmin }}",
              "startPositionY": "={{ $json.coords[1].ymin }}"
            },
            {
              "color": "#ff00f277",
              "operation": "draw",
              "endPositionX": "={{ $json.coords[2].xmax }}",
              "endPositionY": "={{ $json.coords[2].ymax }}",
              "startPositionX": "={{ $json.coords[2].xmin }}",
              "startPositionY": "={{ $json.coords[2].ymin }}"
            },
            {
              "color": "#ff00f277",
              "operation": "draw",
              "endPositionX": "={{ $json.coords[3].xmax }}",
              "endPositionY": "={{ $json.coords[3].ymax }}",
              "startPositionX": "={{ $json.coords[3].xmin }}",
              "startPositionY": "={{ $json.coords[3].ymin }}"
            },
            {
              "color": "#ff00f277",
              "operation": "draw",
              "endPositionX": "={{ $json.coords[4].xmax }}",
              "endPositionY": "={{ $json.coords[4].ymax }}",
              "startPositionX": "={{ $json.coords[4].xmin }}",
              "startPositionY": "={{ $json.coords[4].ymin }}"
            },
            {
              "color": "#ff00f277",
              "operation": "draw",
              "cornerRadius": "=0",
              "endPositionX": "={{ $json.coords[5].xmax }}",
              "endPositionY": "={{ $json.coords[5].ymax }}",
              "startPositionX": "={{ $json.coords[5].xmin }}",
              "startPositionY": "={{ $json.coords[5].ymin }}"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "id": "52daac1b-5ba3-4302-b47b-df3f410b40fc",
      "name": "Get Image Info",
      "type": "n8n-nodes-base.editImage",
      "position": [
        -1080,
        -280
      ],
      "parameters": {
        "operation": "information"
      },
      "typeVersion": 1
    },
    {
      "id": "0d2ab96a-3323-472d-82ff-2af5e7d815a1",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        740,
        -460
      ],
      "parameters": {
        "width": 440,
        "height": 380,
        "content": "Fig 1. Output of Object Detection\n![](https://res.cloudinary.com/daglih2g8/image/upload/f_auto,q_auto/v1/n8n-workflows/download_1_qmqyyo#full-width)"
      },
      "typeVersion": 1
    },
    {
      "id": "c1806400-57da-4ef2-a50d-6ed211d5df29",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -1520,
        -480
      ],
      "parameters": {
        "color": 7,
        "width": 600,
        "height": 420,
        "content": "## 1. Download Test Image\n[Read more about the HTTP node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)\n\nAny compatible image will do ([see docs](https://ai.google.dev/gemini-api/docs/vision?lang=rest#technical-details-image)) but best if it isn't too busy or the subjects too obscure. Most importantly, you are able to retrieve the width and height as this is required for a later step."
      },
      "typeVersion": 1
    },
    {
      "id": "3ae12a7c-a20f-4087-868e-b118cc09fa9a",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -900,
        -480
      ],
      "parameters": {
        "color": 7,
        "width": 560,
        "height": 540,
        "content": "## 2. Use Prompt-Based Object Detection\n[Read more about the HTTP node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)\n\nWe've had generalised object detection before ([see my other template using ResNet](https://n8n.io/workflows/2331-build-your-own-image-search-using-ai-object-detection-cdn-and-elasticsearch/)) but being able to prompt for what you're looking for is a very exciting proposition! Not only could this reduce the effort in post-detection filtering but also introduce contextual use-cases such as searching by \"emotion\", \"locality\", \"anomolies\" and many more!\n\nI found the the output json schema of `{ \"box_2d\": { \"type\": \"array\", ... } }` works best for Gemini to return coordinates. "
      },
      "typeVersion": 1
    },
    {
      "id": "35673272-7207-41d1-985e-08032355846e",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -320,
        -400
      ],
      "parameters": {
        "color": 7,
        "width": 520,
        "height": 440,
        "content": "## 3. Scale Coords to Fit Original Image\n[Read more about the Code node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.code/)\n\nAccording to the Gemini 2.0 overview on [how it calculates bounding boxes](https://ai.google.dev/gemini-api/docs/models/gemini-v2?_gl=1*187cb6v*_up*MQ..*_ga*MTU1ODkzMDc0Mi4xNzM0NDM0NDg2*_ga_P1DBVKWT6V*MTczNDQzNDQ4Ni4xLjAuMTczNDQzNDQ4Ni4wLjAuMjEzNzc5MjU0Ng..#bounding-box), we'll have to rescale the coordinate values as they are normalised to a 0-1000 range. Nothing a little code node can't help with!"
      },
      "typeVersion": 1
    },
    {
      "id": "d3d4470d-0fe1-47fd-a892-10a19b6a6ecc",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -660,
        80
      ],
      "parameters": {
        "color": 5,
        "width": 340,
        "height": 100,
        "content": "### Q. Why not use the Basic LLM node?\nAt time of writing, Langchain version does not recognise Gemini 2.0 to be a multimodal model."
      },
      "typeVersion": 1
    },
    {
      "id": "5b2c1eff-6329-4d9a-9d3d-3a48fb3bd753",
      "name": "Sticky Note5",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        220,
        -400
      ],
      "parameters": {
        "color": 7,
        "width": 500,
        "height": 440,
        "content": "## 4. Draw!\n[Read more about the Edit Image node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.editimage/)\n\nFinally for this demonstration, we can use the \"Edit Image\" node to draw the bounding boxes on top of the original image. In my test run, I can see Gemini did miss out one of the bunnies but seeing how this is the experimental version we're playing with, it's pretty good to see it doesn't do too bad of a job."
      },
      "typeVersion": 1
    },
    {
      "id": "965d791b-a183-46b0-b2a6-dd961d630c13",
      "name": "Sticky Note6",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -1960,
        -740
      ],
      "parameters": {
        "width": 420,
        "height": 680,
        "content": "## Try it out!\n### This n8n template demonstrates how to use Gemini 2.0's new Bounding Box detection capabilities your workflows.\n\nThe key difference being this enables prompt-based object detection for images which is pretty powerful for things like contextual search over an image. eg. \"Put a bounding box around all adults with children in this image\" or \"Put a bounding box around cars parked out of bounds of a parking space\".\n\n## How it works\n* An image is downloaded via the HTTP node and an \"Edit Image\" node is used to extract the file's width and height.\n* The image is then given to the Gemini 2.0 API to parse and return coordinates of the bounding box of the requested subjects. In this demo, we've asked for the AI to identify all bunnies.\n* The coordinates are then rescaled with the original image's width and height to correctl align them.\n* Finally to measure the accuracy of the object detection, we use the \"Edit Image\" node to draw the bounding boxes onto the original image.\n\n\n### Need Help?\nJoin the [Discord](https://discord.com/invite/XPKeKXeB7d) or ask in the [Forum](https://community.n8n.io/)!\n\nHappy Hacking!"
      },
      "typeVersion": 1
    }
  ],
  "pinData": {},
  "connections": {
    "Get Variables": {
      "main": [
        [
          {
            "node": "Scale Normalised Coords",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Image Info": {
      "main": [
        [
          {
            "node": "Gemini 2.0 Object Detection",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Test Image": {
      "main": [
        [
          {
            "node": "Get Image Info",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Draw Bounding Boxes": {
      "main": [
        []
      ]
    },
    "Scale Normalised Coords": {
      "main": [
        [
          {
            "node": "Draw Bounding Boxes",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Gemini 2.0 Object Detection": {
      "main": [
        [
          {
            "node": "Get Variables",
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
            "node": "Get Test Image",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-272"></a>

## Template 272 - Geração automática de relatórios de pesquisa

- **Nome:** Geração automática de relatórios de pesquisa
- **Descrição:** Automatiza a coleta, síntese e publicação de relatórios de pesquisa a partir de solicitações recebidas via Telegram ou webhook, incluindo busca na web, extração de conteúdo, redação e postagem no Notion.
- **Funcionalidade:** • Entrada via Telegram ou Webhook: Recebe solicitações de pesquisa diretamente de mensagens ou chamadas HTTP.
• Diálogo estratégico e clarificação: Conversa com o usuário para definir o tema e faz perguntas de follow-up para refinar a direção da pesquisa.
• Memória de sessão: Mantém contexto limitado por sessão para conversas sequenciais e acompanhamento do usuário.
• Geração de consultas SERP: Cria queries otimizadas e curtas para pesquisa na web com base no briefing do usuário.
• Busca e extração de conteúdo: Executa buscas web e extrai o conteúdo mais relevante de URLs selecionadas.
• Seleção de fonte via modelo: Usa modelos de linguagem para escolher a URL mais relevante entre os resultados obtidos.
• Agregação de resultados: Junta resultados e conteúdos extraídos para compor o material bruto de pesquisa.
• Redação de relatório em Markdown: Gera um relatório detalhado, organizado em seções, consolidando e reescrevendo as informações das fontes.
• Geração de título e descrição: Cria título e descrição do relatório a partir do rascunho para uso como metadados.
• Conversão para HTML e blocos do Notion: Converte o Markdown final em HTML e transforma trechos (tabelas, listas, headings) em blocos compatíveis com Notion.
• Publicação e atualização no Notion: Cria/atualiza página no banco de dados do Notion, com status de progresso e marcação de conclusão.
• Notificação externa: Envia aviso para um endpoint externo quando o relatório estiver pronto, incluindo título, URL e status.
• Identificação e rastreamento: Gera um ID aleatório para cada requisição para rastrear e relacionar registros e páginas.
- **Ferramentas:** • Telegram: Canal de entrada de mensagens do usuário para iniciar pedidos de pesquisa.
• Webhook personalizado: Endpoint HTTP para receber solicitações e sessão_id de clientes externos.
• Tavily (search & extract API): Serviço usado para executar buscas na web e extrair conteúdo detalhado de URLs.
• OpenAI: Modelos usados para selecionar URLs relevantes e gerar metadados (título/descrição) e partes do conteúdo.
• OpenRouter / Anthropic (Claude): Modelos conversacionais usados para agente de estratégia e geração de rascunhos/planejamento.
• Google Gemini: Modelo utilizado para ajudar na conversão de HTML para blocos compatíveis com Notion.
• Notion: Armazenamento final do relatório em banco de dados e publicação dos blocos convertidos.
• Endpoint de notificação (ex.: Replit app): Serviço externo que recebe POST quando o relatório fica pronto para notificar o usuário ou sistema integrador.



## Fluxo (.json) :

```json
{}
```

<a id="template-273"></a>

## Template 273 - Orquestrador Master Multi‑Agente Pyragogy

- **Nome:** Orquestrador Master Multi‑Agente Pyragogy
- **Descrição:** Fluxo que orquestra múltiplos agentes de IA para processar entradas, avaliar qualidade via um painel de revisão (automático + humano) e arquivar conteúdos aprovados com versionamento e notificações.
- **Funcionalidade:** • Recepção via webhook: Inicia o fluxo ao receber requisições HTTP com o conteúdo a processar.
• Verificação de conexão ao banco: Confirma disponibilidade do banco de dados antes de prosseguir.
• Meta‑orquestração por IA: Decide automaticamente a sequência ideal de agentes a executar com base no input.
• Roteamento para agentes especializados: Encaminha o conteúdo para agentes como Summarizer, Synthesizer, Peer Reviewer, Sensemaking, Prompt Engineer, Onboarding/Explainer e Archivist.
• Processamento iterativo e controle de fluxo: Mantém índice de agentes, coleta contribuições e permite loops controlados para rielaboração (até limites definidos).
• Avaliação de consenso do painel: Agrega outputs de revisores automáticos para decidir se é necessário redraft com votação majoritária.
• Mecanismo de rielaboração: Redireciona para o Synthesizer quando o painel exige revisões, incluindo feedback consolidado.
• Preparação de conteúdo para revisão humana: Gera front‑matter, markdown e metadados para revisão do handbook.
• Revisão humana com aprovação/rejeição: Envia pedido de revisão por e‑mail com links de aprovação ou rejeição e espera resposta do revisor.
• Persistência e registro: Ao aprovar, salva entrada no banco de dados, registra contribuições dos agentes e gera caminho de arquivo para versionamento.
• Integração com repositório: Realiza commit do conteúdo aprovado em repositório remoto quando configurado.
• Notificações e resposta final: Envia notificação (opcional) e retorna resposta JSON final com saída e histórico de contribuições.
- **Ferramentas:** • PostgreSQL: Banco de dados relacional para verificar conexão, armazenar handbook_entries e registrar agent_contributions.
• OpenAI (modelo gpt‑4o): Plataforma de modelos de linguagem usada para Meta‑Orchestrator e todos os agentes de processamento e revisão automática.
• Serviço de e‑mail (SMTP ou provedor compatível): Envio de solicitações de revisão humana com links de aprovação/rejeição.
• GitHub: Repositório para commitar e versionar o conteúdo aprovado (opcional, ativado por token).
• Slack (webhook): Canal de notificação para avisar sobre completude do fluxo e resultados.
• Endpoints HTTP (webhook público): Recepção das solicitações iniciais e callbacks de feedback de revisão humana.



## Fluxo (.json) :

```json
{}
```

<a id="template-274"></a>

## Template 274 - Agente conversacional para consultas em Supabase

- **Nome:** Agente conversacional para consultas em Supabase
- **Descrição:** Fluxo que permite conversar com um banco de dados Supabase (PostgreSQL) usando um agente de IA que gera e executa consultas SQL conforme as solicitações do usuário.
- **Funcionalidade:** • Recepção de mensagem de chat: Inicia o processo a partir da mensagem enviada pelo usuário.
• Interpretação de intenção e geração de SQL: Utiliza um modelo de linguagem para entender o pedido do usuário e compor consultas SQL apropriadas.
• Execução de consultas personalizadas: Executa consultas SQL geradas dinamicamente no banco de dados PostgreSQL hospedado no Supabase.
• Descoberta do esquema do banco: Recupera a lista de tabelas e definitions (colunas, tipos e referências) para orientar a geração de consultas.
• Extração e análise de dados JSON: Suporta extração de campos JSON armazenados em colunas para análise e agregação.
• Resposta ao usuário com resultados formatados: Retorna ao usuário os resultados ou resumos baseados nas consultas executadas.
- **Ferramentas:** • Supabase (PostgreSQL): Serviço de banco de dados hospedado que armazena os dados e executa consultas SQL.
• OpenAI: API de modelo de linguagem usada para interpretar mensagens do usuário, gerar consultas SQL e formatar respostas.



## Fluxo visual

```mermaid
flowchart LR
    N1["Sticky Note3"]
    N2["Sticky Note5"]
    N3["Sticky Note6"]
    N4["Sticky Note7"]
    N5["When chat message received"]
    N6["OpenAI Chat Model"]
    N7["DB Schema"]
    N8["Get table definition"]
    N9["Sticky Note"]
    N10["AI Agent"]
    N11["Run SQL Query"]

    N5 --> N10
```

## Fluxo (.json) :

```json
{
  "nodes": [
    {
      "id": "0a4e65b7-39be-44eb-8c66-913ebfe8a87a",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1140,
        840
      ],
      "parameters": {
        "color": 3,
        "width": 215,
        "height": 80,
        "content": "**Replace password and username for Supabase**"
      },
      "typeVersion": 1
    },
    {
      "id": "2cea21fc-f3fe-47b7-a7b6-12acb0bc03ac",
      "name": "Sticky Note5",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -160,
        320
      ],
      "parameters": {
        "color": 7,
        "width": 280.2462120317618,
        "height": 545.9087885077763,
        "content": "### Set up steps\n\n#### Preparation\n1. **Create Accounts**:\n   - [N8N](https://n8n.partnerlinks.io/2hr10zpkki6a): For workflow automation.\n   - [Supabase](https://supabase.com/): For database hosting and management.\n   - [OpenAI](https://openai.com/): For building the conversational AI agent.\n2. **Configure Database Connection**:\n   - Set up a PostgreSQL database in Supabase.\n   - Use appropriate credentials (`username`, `password`, `host`, and `database` name) in your workflow.\n\n#### N8N Workflow\n\nAI agent with tools:\n\n1. **Code Tool**:\n   - Execute SQL queries based on user input.\n2. **Database Schema Tool**:\n   - Retrieve a list of all tables in the database.\n   - Use a predefined SQL query to fetch table definitions, including column names, types, and references.\n3. **Table Definition**:\n   - Retrieve a list of columns with types for one table."
      },
      "typeVersion": 1
    },
    {
      "id": "eacc0c8c-11d5-44fb-8ff1-10533a233693",
      "name": "Sticky Note6",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -160,
        -200
      ],
      "parameters": {
        "color": 7,
        "width": 636.2128494576581,
        "height": 497.1532689930921,
        "content": "![5min Logo](https://res.cloudinary.com/de9jgixzm/image/upload/v1739773200/Skool%20Assets/ejm3hqnvhgwpnu2fv92s.png)\n## AI Agent to chat with Supabase/PostgreSQL DB\n**Made by [Mark Shcherbakov](https://www.linkedin.com/in/marklowcoding/) from community [5minAI](https://www.skool.com/5minai-2861)**\n\nAccessing and analyzing database data often requires SQL expertise or dedicated reports, which can be time-consuming. This workflow empowers users to interact with a database conversationally through an AI-powered agent. It dynamically generates SQL queries based on user requests, streamlining data retrieval and analysis.\n\nThis workflow integrates OpenAI with a Supabase database, enabling users to interact with their data via an AI agent. The agent can:\n- Retrieve records from the database.\n- Extract and analyze JSON data stored in tables.\n- Provide summaries, aggregations, or specific data points based on user queries.\n\n"
      },
      "typeVersion": 1
    },
    {
      "id": "be1559ea-1f75-4e7c-9bdd-3add8d8be70b",
      "name": "Sticky Note7",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        140,
        320
      ],
      "parameters": {
        "color": 7,
        "width": 330.5152611046425,
        "height": 239.5888196628349,
        "content": "### ... or watch set up video [20 min]\n[![Youtube Thumbnail](https://res.cloudinary.com/de9jgixzm/image/upload/v1739773279/Youtube%20Thumbs/Chat%20With%20DB.png)](https://www.youtube.com/watch?v=-GgKzhCNxjk)\n"
      },
      "typeVersion": 1
    },
    {
      "id": "4ea87754-dead-49ea-848c-ed86c98e217b",
      "name": "When chat message received",
      "type": "@n8n/n8n-nodes-langchain.chatTrigger",
      "position": [
        720,
        400
      ],
      "webhookId": "6e95bc27-99a6-417c-8bf7-2831d7f7a4be",
      "parameters": {
        "options": {}
      },
      "typeVersion": 1.1
    },
    {
      "id": "c20d6e57-eb41-4682-a7f5-5bb4323df476",
      "name": "OpenAI Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        760,
        680
      ],
      "parameters": {
        "options": {}
      },
      "credentials": {
        "openAiApi": {
          "id": "zJhr5piyEwVnWtaI",
          "name": "OpenAi club"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "8d3b1faf-643c-4070-996d-a59cb06e1827",
      "name": "DB Schema",
      "type": "n8n-nodes-base.postgresTool",
      "position": [
        1180,
        660
      ],
      "parameters": {
        "query": "SELECT table_schema, table_name\nFROM information_schema.tables\nWHERE table_type = 'BASE TABLE' AND table_schema = 'public';",
        "options": {},
        "operation": "executeQuery",
        "descriptionType": "manual",
        "toolDescription": "Get list of all tables in database"
      },
      "credentials": {
        "postgres": {
          "id": "AO9cER6p8uX7V07T",
          "name": "Postgres 5minai"
        }
      },
      "typeVersion": 2.5
    },
    {
      "id": "d9346ade-79d1-44c2-8fa6-b337ad8b0544",
      "name": "Get table definition",
      "type": "n8n-nodes-base.postgresTool",
      "position": [
        1340,
        660
      ],
      "parameters": {
        "query": "SELECT \n    c.column_name,\n    c.data_type,\n    c.is_nullable,\n    c.column_default,\n    tc.constraint_type,\n    ccu.table_name AS referenced_table,\n    ccu.column_name AS referenced_column\nFROM \n    information_schema.columns c\nLEFT JOIN \n    information_schema.key_column_usage kcu \n    ON c.table_name = kcu.table_name \n    AND c.column_name = kcu.column_name\nLEFT JOIN \n    information_schema.table_constraints tc \n    ON kcu.constraint_name = tc.constraint_name\n    AND tc.constraint_type = 'FOREIGN KEY'\nLEFT JOIN\n    information_schema.constraint_column_usage ccu\n    ON tc.constraint_name = ccu.constraint_name\nWHERE \n    c.table_name = '{{ $fromAI(\"table_name\") }}' -- Your table name\n    AND c.table_schema = 'public' -- Ensure it's in the right schema\nORDER BY \n    c.ordinal_position;\n",
        "options": {},
        "operation": "executeQuery",
        "descriptionType": "manual",
        "toolDescription": "Get table definition to find all columns and types."
      },
      "credentials": {
        "postgres": {
          "id": "AO9cER6p8uX7V07T",
          "name": "Postgres 5minai"
        }
      },
      "typeVersion": 2.5
    },
    {
      "id": "b88a21e0-d2ff-4431-bd84-dfd43edeb5c4",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        960,
        280
      ],
      "parameters": {
        "width": 215,
        "height": 80,
        "content": "**Finetune the prompt of assistant**"
      },
      "typeVersion": 1
    },
    {
      "id": "fbe9eb68-5990-485c-820f-08234ea33194",
      "name": "AI Agent",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        940,
        400
      ],
      "parameters": {
        "text": "={{ $('When chat message received').item.json.chatInput }}",
        "agent": "openAiFunctionsAgent",
        "options": {
          "systemMessage": "You are DB assistant. You need to run queries in DB aligned with user requests.\n\nRun custom SQL query to aggregate data and response to user.\n\nFetch all data to analyse it for response if needed.\n"
        },
        "promptType": "define"
      },
      "typeVersion": 1.6
    },
    {
      "id": "7f82d6d9-d7d6-4443-bbaa-c9b276a376e3",
      "name": "Run SQL Query",
      "type": "n8n-nodes-base.postgresTool",
      "position": [
        1040,
        660
      ],
      "parameters": {
        "query": "{{ $fromAI(\"query\",\"SQL query for PostgreSQL DB in Supabase\") }}",
        "options": {},
        "operation": "executeQuery",
        "descriptionType": "manual",
        "toolDescription": "Run custom SQL queries using knowledge about Output structure to provide needed response for user request.\nUse ->> operator to extract JSON data."
      },
      "credentials": {
        "postgres": {
          "id": "AO9cER6p8uX7V07T",
          "name": "Postgres 5minai"
        }
      },
      "typeVersion": 2.5
    }
  ],
  "pinData": {},
  "connections": {
    "DB Schema": {
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
    "Run SQL Query": {
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
    "Get table definition": {
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
    }
  }
}
```

<a id="template-275"></a>

## Template 275 - Gerar e enviar screenshots por e-mail

- **Nome:** Gerar e enviar screenshots por e-mail
- **Descrição:** Gera screenshots (simples e fullpage) de um site, armazena-as em Dropbox e envia um e-mail com as imagens para um destinatário especificado.
- **Funcionalidade:** • Gatilho manual: Inicia o fluxo quando executado manualmente.
• Criação de item com dados: Define a URL do site e o e-mail de destino.
• Geração de screenshot fullpage: Solicita captura de tela completa do site.
• Geração de screenshot simples: Solicita captura de tela apenas da área visível.
• Download dos arquivos gerados: Baixa as imagens resultantes da geração de screenshots.
• Upload para armazenamento em nuvem: Envia ambas as imagens para pastas definidas no armazenamento.
• Envio de e-mail com imagens: Envia um e-mail HTML ao destinatário contendo as screenshots incorporadas via URL.
- **Ferramentas:** • Uproc: Serviço/API para gerar screenshots a partir de uma URL (suporta fullpage e viewport).
• Dropbox: Armazenamento em nuvem usado para salvar os arquivos de imagem gerados.
• AWS SES (Amazon Simple Email Service): Serviço usado para enviar o e-mail com as imagens.

## Fluxo visual

```mermaid
flowchart LR
    N1["On clicking 'execute'"]
    N2["Create Web + Email Item"]
    N3["Send Email"]
    N4["Generate FullPage"]
    N5["Generate Screenshot"]
    N6["Get File"]
    N7["Get File1"]
    N8["Merge"]
    N9["Upload Screenshot"]
    N10["Upload fullpage"]

    N8 --> N3
    N6 --> N10
    N7 --> N9
    N10 --> N8
    N4 --> N6
    N9 --> N8
    N5 --> N7
    N1 --> N2
    N2 --> N4
    N2 --> N5
```

## Fluxo (.json) :

```json
{
  "id": "105",
  "name": "screenshot",
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        440,
        580
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Create Web + Email Item",
      "type": "n8n-nodes-base.functionItem",
      "position": [
        630,
        580
      ],
      "parameters": {
        "functionCode": "item.website = \"https://uproc.io\";\nitem.email = \"miquel@uproc.io\";\n\nreturn item;"
      },
      "typeVersion": 1
    },
    {
      "name": "Send Email",
      "type": "n8n-nodes-base.awsSes",
      "position": [
        1660,
        600
      ],
      "parameters": {
        "body": "=Hi,\n<br><br>\nThese are your screenshots:<br>\n<table border=\"0\">\n<tr>\n<th>Simple screenshot</th><th>Fullpage screenshot</th>\n<tr>\n<td style=\"vertical-align: top; text-align: center\"><img src=\"{{$node[\"Generate Screenshot\"].json[\"message\"][\"result\"]}}\" width=\"320\"></td>\n<td style=\"vertical-align: top; text-align: center\"><img src=\"{{$node[\"Generate FullPage\"].json[\"message\"][\"result\"]}}\" width=\"320\"></td>\n</tr>\n</table>\n<br><br>\nThank you!",
        "subject": "Your screenshots!",
        "fromEmail": "miquel@uproc.io",
        "isBodyHtml": true,
        "toAddresses": [
          "={{$node[\"Create Web + Email Item\"].json[\"email\"]}}"
        ],
        "additionalFields": {}
      },
      "credentials": {
        "aws": "ses"
      },
      "typeVersion": 1
    },
    {
      "name": "Generate FullPage",
      "type": "n8n-nodes-base.uproc",
      "position": [
        850,
        510
      ],
      "parameters": {
        "url": "={{$node[\"Create Web + Email Item\"].json[\"website\"]}}",
        "tool": "getUrlScreenshot",
        "group": "image",
        "width": "640",
        "fullpage": "yes",
        "additionalOptions": {}
      },
      "credentials": {
        "uprocApi": "miquel-uproc"
      },
      "typeVersion": 1
    },
    {
      "name": "Generate Screenshot",
      "type": "n8n-nodes-base.uproc",
      "position": [
        840,
        680
      ],
      "parameters": {
        "url": "={{$node[\"Create Web + Email Item\"].json[\"website\"]}}",
        "tool": "getUrlScreenshot",
        "group": "image",
        "width": "640",
        "fullpage": "no",
        "additionalOptions": {}
      },
      "credentials": {
        "uprocApi": "miquel-uproc"
      },
      "typeVersion": 1
    },
    {
      "name": "Get File",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1050,
        510
      ],
      "parameters": {
        "url": "={{$node[\"Generate FullPage\"].json[\"message\"][\"result\"]}}",
        "options": {},
        "responseFormat": "file",
        "allowUnauthorizedCerts": true
      },
      "typeVersion": 1
    },
    {
      "name": "Get File1",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1050,
        680
      ],
      "parameters": {
        "url": "={{$node[\"Generate Screenshot\"].json[\"message\"][\"result\"]}}",
        "options": {},
        "responseFormat": "file",
        "allowUnauthorizedCerts": true
      },
      "typeVersion": 1
    },
    {
      "name": "Merge",
      "type": "n8n-nodes-base.merge",
      "position": [
        1460,
        600
      ],
      "parameters": {
        "mode": "passThrough"
      },
      "typeVersion": 1
    },
    {
      "name": "Upload Screenshot",
      "type": "n8n-nodes-base.dropbox",
      "position": [
        1270,
        680
      ],
      "parameters": {
        "path": "/screenshots/sample.png",
        "binaryData": true
      },
      "credentials": {
        "dropboxApi": "dropbox-miquel"
      },
      "typeVersion": 1
    },
    {
      "name": "Upload fullpage",
      "type": "n8n-nodes-base.dropbox",
      "position": [
        1270,
        510
      ],
      "parameters": {
        "path": "/screenshots/sample_fullpage.png",
        "binaryData": true
      },
      "credentials": {
        "dropboxApi": "dropbox-miquel"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "Merge": {
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
    "Get File": {
      "main": [
        [
          {
            "node": "Upload fullpage",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get File1": {
      "main": [
        [
          {
            "node": "Upload Screenshot",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Upload fullpage": {
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
    "Generate FullPage": {
      "main": [
        [
          {
            "node": "Get File",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Upload Screenshot": {
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
    "Generate Screenshot": {
      "main": [
        [
          {
            "node": "Get File1",
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
            "node": "Create Web + Email Item",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Create Web + Email Item": {
      "main": [
        [
          {
            "node": "Generate FullPage",
            "type": "main",
            "index": 0
          },
          {
            "node": "Generate Screenshot",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-276"></a>

## Template 276 - Leitura manual de JPGs de pasta

- **Nome:** Leitura manual de JPGs de pasta
- **Descrição:** Este fluxo inicia manualmente a leitura de todos os arquivos JPG em um diretório especificado e fornece seus conteúdos binários para uso posterior.
- **Funcionalidade:** • Inicio manual: O fluxo é acionado manualmente pelo usuário ao clicar em executar.
• Leitura em lote de arquivos JPG: Localiza e lê todos os arquivos com extensão .jpg no diretório /data/lol usando um padrão curinga.
• Disponibilização do conteúdo binário: Carrega o conteúdo binário das imagens para processamento ou integração posterior.
- **Ferramentas:** • Sistema de arquivos local: Fonte dos arquivos JPG, acessando o diretório /data/lol e retornando os arquivos correspondentes ao padrão *.jpg.

## Fluxo visual

```mermaid
flowchart LR
    N1["On clicking 'execute'"]
    N2["Read Binary Files"]

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
        270,
        320
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Read Binary Files",
      "type": "n8n-nodes-base.readBinaryFiles",
      "position": [
        470,
        320
      ],
      "parameters": {
        "fileSelector": "/data/lol/*.jpg"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "Read Binary Files",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-277"></a>

## Template 277 - Criar tickets únicos no Jira a partir de alertas Splunk

- **Nome:** Criar tickets únicos no Jira a partir de alertas Splunk
- **Descrição:** Recebe alertas via webhook e cria ou atualiza tickets no Jira garantindo que não haja duplicação por host.
- **Funcionalidade:** • Recepção de alertas via webhook: inicia o processo ao receber o payload do alerta (dados de host, métrica, descrição e timestamp).
• Normalização do nome do host: remove caracteres especiais do host recebido para gerar um identificador consistente.
• Busca de ticket existente: pesquisa no Jira por tickets associados ao host normalizado para detectar duplicados.
• Decisão condicional: determina se deve criar um novo ticket ou atualizar um existente com base na presença de um ticket correspondente.
• Criação de ticket único: quando não há ticket correspondente, cria um novo com resumo, descrição completa e salva o host no campo personalizado.
• Atualização de ticket existente: quando já existe um ticket, adiciona um comentário com timestamp e descrição do alerta para agregar informações sem duplicar issues.
- **Ferramentas:** • Splunk Observability (SignalFx): envia alertas via webhook contendo detalhes do evento, host, métrica, descrição e timestamp.
• Jira Cloud: plataforma para criar novos tickets, pesquisar por tickets existentes e adicionar comentários; armazena o host como campo personalizado para correlação.

## Fluxo visual

```mermaid
flowchart LR
    N1["Webhook"]
    N2["Add Ticket Comment"]
    N3["Search Ticket"]
    N4["Set Host Name"]
    N5["IF Ticket Not Exists"]
    N6["Sticky Note"]
    N7["Create Ticket"]
    N8["Sticky Note1"]
    N9["Sticky Note2"]
    N10["Sticky Note3"]
    N11["Sticky Note4"]

    N1 --> N4
    N3 --> N5
    N4 --> N3
    N5 --> N7
    N5 --> N2
```

## Fluxo (.json) :

```json
{
  "id": "uD31xU0VYjogxWoY",
  "meta": {
    "instanceId": "03e9d14e9196363fe7191ce21dc0bb17387a6e755dcc9acc4f5904752919dca8"
  },
  "name": "Create_Unique_Jira_tickets_from_Splunk_alerts",
  "tags": [
    {
      "id": "GCHVocImoXoEVnzP",
      "name": "🛠️ In progress",
      "createdAt": "2023-10-31T02:17:21.618Z",
      "updatedAt": "2023-10-31T02:17:21.618Z"
    },
    {
      "id": "QPJKatvLSxxtrE8U",
      "name": "Secops",
      "createdAt": "2023-10-31T02:15:11.396Z",
      "updatedAt": "2023-10-31T02:15:11.396Z"
    }
  ],
  "nodes": [
    {
      "id": "3f9fa220-1966-4478-b7db-c39056564c9d",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "position": [
        -640,
        320
      ],
      "webhookId": "f2a52578-2fef-40a6-a7ff-e03f6b751a02",
      "parameters": {
        "path": "f2a52578-2fef-40a6-a7ff-e03f6b751a02",
        "options": {},
        "httpMethod": "POST"
      },
      "typeVersion": 1
    },
    {
      "id": "375ac47e-7975-45cb-b7c1-cef1c7fca701",
      "name": "Add Ticket Comment",
      "type": "n8n-nodes-base.jira",
      "position": [
        240,
        520
      ],
      "parameters": {
        "comment": "=Timestamp: {{ $('Set Host Name').item.json.body.timestamp }}\nDescription: {{ $('Set Host Name').item.json.body.description }}",
        "options": {},
        "issueKey": "={{ $json.key }}",
        "resource": "issueComment"
      },
      "credentials": {
        "jiraSoftwareCloudApi": {
          "id": "OYvpDV2Q42eY6iyA",
          "name": "Alex Jira Cloud"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "a5dea875-6adf-4d18-aeb9-5fe31a0ebfae",
      "name": "Search Ticket",
      "type": "n8n-nodes-base.jira",
      "position": [
        -200,
        320
      ],
      "parameters": {
        "options": {
          "jql": "=splunkhostname ~ \"{{ $json['splunk-host-name'] }}\" "
        },
        "operation": "getAll"
      },
      "credentials": {
        "jiraSoftwareCloudApi": {
          "id": "OYvpDV2Q42eY6iyA",
          "name": "Alex Jira Cloud"
        }
      },
      "typeVersion": 1,
      "alwaysOutputData": true
    },
    {
      "id": "3dac410e-1e37-463d-9aba-bc6abf3889f7",
      "name": "Set Host Name",
      "type": "n8n-nodes-base.set",
      "position": [
        -420,
        320
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "splunk-host-name",
              "value": "={{ $json.body.inputs.A.key['host.name'].replace(/[^a-zA-Z0-9 ]/g, '') }}"
            }
          ]
        },
        "options": {}
      },
      "typeVersion": 2
    },
    {
      "id": "465ec3b0-dd16-482e-b4b6-f8ed91fbb11b",
      "name": "IF Ticket Not Exists",
      "type": "n8n-nodes-base.if",
      "position": [
        20,
        320
      ],
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{ $json.key }}",
              "operation": "isEmpty"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "id": "1315b76b-39fc-4fd3-9a45-a91e5e873874",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -1120,
        -26.960531840248223
      ],
      "parameters": {
        "width": 643.8620281403546,
        "height": 537.944771288002,
        "content": "![VirusTotal](https://i.imgur.com/spMd6AQ.png)\n## Webhook Node \nTo setup your webhook integration for Splunk, first ensure that splunk is setup to send alerts to a webhook by visiting the [Setup Guide here](https://docs.splunk.com/observability/en/admin/notif-services/webhook.html). You will copy the n8n webhook url opening the webhook node below. \n- **Form Access URLs**:\n  - **Execute Mode**: `https://n8n.domain.com/webhook/test/webhookpath` - Use this to execute the workflow interactively within the n8n canvas. Hit the 'Execute Workflow' button to see real-time execution results. We have pinned data in the webhook node to make testing easier. \n  - **Silent Mode**: `https://n8n.domain.com/webhook/webhookpath` - Use this for background execution without canvas updates. Results will be logged silently and can be reviewed in the 'Executions' tab."
      },
      "typeVersion": 1
    },
    {
      "id": "636425b9-a11f-4891-aa00-2f3c42956c01",
      "name": "Create Ticket",
      "type": "n8n-nodes-base.jira",
      "position": [
        240,
        160
      ],
      "parameters": {
        "project": {
          "__rl": true,
          "mode": "list",
          "value": "10001",
          "cachedResultName": "Service Desk"
        },
        "summary": "=Splunk Alert for host {{ $('Set Host Name').item.json.body.inputs.A.key[\"host.name\"] }}:  {{ $('Set Host Name').item.json.body.description }}",
        "issueType": {
          "__rl": true,
          "mode": "list",
          "value": "10004",
          "cachedResultName": "[System] Incident"
        },
        "additionalFields": {
          "description": "={{ $('Set Host Name').item.json.body.description }}\n\n{{ $('Set Host Name').item.json.body.messageBody }}",
          "customFieldsUi": {
            "customFieldsValues": [
              {
                "fieldId": {
                  "__rl": true,
                  "mode": "id",
                  "value": "customfield_10063"
                },
                "fieldValue": "={{ $('Webhook').item.json[\"body\"][\"inputs\"][\"A\"][\"key\"][\"host.name\"].replace(/[^a-zA-Z0-9 ]/g, '') }}"
              }
            ]
          }
        }
      },
      "credentials": {
        "jiraSoftwareCloudApi": {
          "id": "OYvpDV2Q42eY6iyA",
          "name": "Alex Jira Cloud"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "47af8bdb-e0da-4923-8f0a-05deb86ac1b3",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -460,
        98.72468966845895
      ],
      "parameters": {
        "width": 401.99970102055784,
        "height": 413.43480804607805,
        "content": "![VirusTotal](https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Jira_%28Software%29_logo.svg/320px-Jira_%28Software%29_logo.svg.png)\n## Normalize Hostname \nTo ensure no special characters are passed into jira and create issues, this set node removes special characters from the `splunk-host-name` and uses that to search and create tickets. This host name is saved as a custom field. "
      },
      "typeVersion": 1
    },
    {
      "id": "c0bf09e6-ca08-4db6-aff0-a6528a8fb03b",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        180,
        -21.934709587377256
      ],
      "parameters": {
        "width": 401.99970102055784,
        "height": 348.38243930996134,
        "content": "![VirusTotal](https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Jira_%28Software%29_logo.svg/320px-Jira_%28Software%29_logo.svg.png)\n## Create a new ticket\nThis creates a new ticket in your Prjoect and issue type. Ensure to update these values to ensure it works correctly. "
      },
      "typeVersion": 1
    },
    {
      "id": "a175e343-83ed-4442-94df-7e7027b8c687",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        180,
        340
      ],
      "parameters": {
        "width": 401.99970102055784,
        "height": 341.08777742613927,
        "content": "![VirusTotal](https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Jira_%28Software%29_logo.svg/320px-Jira_%28Software%29_logo.svg.png)\n## Add Ticket Comment\nThis adds the alert as a comment in the existing ticket, to ensure the data is not duplicated. "
      },
      "typeVersion": 1
    },
    {
      "id": "09143b8c-a4ce-4791-8937-3333d24b6e01",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -40,
        100.50445897107033
      ],
      "parameters": {
        "width": 193.6032856277124,
        "height": 415.27445353029793,
        "content": "## Check if ticket found\nThis checks `$json.key` to see if the value was found, and route accordingly."
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {
    "Webhook": [
      {
        "json": {
          "body": {
            "tip": null,
            "rule": "n8n-test",
            "inputs": {
              "A": {
                "key": {
                  "os.type": "linux",
                  "host.name": "n8n-enterprise-demo",
                  "sf_metric": "cpu.utilization"
                },
                "value": "0.1670342357065173",
                "fragment": "data('cpu.utilization').publish(label='A')"
              },
              "_S2": {
                "value": "0.2",
                "fragment": "threshold(0.2)"
              }
            },
            "status": "ok",
            "detector": "n8n-test",
            "imageUrl": "https://static.eu0.signalfx.com/signed/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJjb20uc2lnbmFsZnguYXBwIiwiZXhwIjoxNjk0NjE0NjI2LCJpSWQiOiJGNVZBcTEwQUVBQSIsIm9JZCI6IkY1V0JKZ2lBSUFBIiwiYlQiOiJlbmQifQ.udzyF5-HqKyV_EMRmT51EtgECK9g-wanl8nx_MH0i9Q/async",
            "severity": "Critical",
            "eventType": "F5Vx1EuAAKc__F5V-TcTAEJ8__n8n-test",
            "sf_schema": 2,
            "timestamp": "2023-09-06T14:17:00Z",
            "detectorId": "F5V-TcTAEJ8",
            "incidentId": "F5VAq10AEAA",
            "runbookUrl": null,
            "description": "The value of cpu.utilization is above 0.2.",
            "detectorUrl": "https://app.eu0.signalfx.com/#/detector/F5V-TcTAEJ8/edit?incidentId=F5VAq10AEAA&is=ok",
            "messageBody": "Rule \"n8n-test\" in detector \"n8n-test\" cleared at Wed, 6 Sep 2023 14:17:00 GMT.\n\nCurrent signal value for n8n.test: 0.1670342357065173\n\nSignal details:\n{sf_metric=cpu.utilization, host.name=n8n-enterprise-demo, os.type=linux}",
            "messageTitle": "Back to normal: n8n-test (n8n-test)",
            "statusExtended": "ok",
            "detectOnCondition": "when(A > threshold(0.2))",
            "originatingMetric": "cpu.utilization",
            "triggeredWhileMuted": false
          },
          "query": {},
          "params": {},
          "headers": {
            "host": "internal.users.n8n.cloud",
            "x-real-ip": "10.255.0.2",
            "user-agent": "Apache-HttpClient/4.5.14 (Java/1.8.0_372)",
            "content-type": "application/json; charset=utf-8",
            "content-length": "1366",
            "accept-encoding": "gzip,deflate",
            "x-forwarded-for": "10.255.0.2",
            "x-forwarded-host": "internal.users.n8n.cloud",
            "x-forwarded-port": "443",
            "x-forwarded-proto": "https",
            "x-forwarded-server": "e591fa1c2d01"
          }
        }
      }
    ]
  },
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "3985cac2-7f23-4d27-b826-0edfb0544b58",
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Set Host Name",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Search Ticket": {
      "main": [
        [
          {
            "node": "IF Ticket Not Exists",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set Host Name": {
      "main": [
        [
          {
            "node": "Search Ticket",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "IF Ticket Not Exists": {
      "main": [
        [
          {
            "node": "Create Ticket",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Add Ticket Comment",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-278"></a>

## Template 278 - Busca de torrent por título e adição ao Transmission

- **Nome:** Busca de torrent por título e adição ao Transmission
- **Descrição:** Recebe um título via webhook, busca torrents em provedores, adiciona o primeiro resultado ao Transmission tratando autenticação de sessão e notifica via Telegram sobre sucesso ou falha.
- **Funcionalidade:** • Recepção de requisição: Aceita POST com o título do filme para iniciar o fluxo.
• Busca de torrents: Procura até 5 resultados usando os provedores configurados.
• Verificação de resultado: Determina se foram encontrados torrents e marca o estado apropriado.
• Adição ao Transmission: Envia o magnet do primeiro resultado para o Transmission com diretório e autenticação.
• Tratamento de sessão (X-Transmission-Session-Id): Detecta resposta 409 e reenvia a requisição usando o token de sessão retornado.
• Notificações via Telegram: Informa sobre início do download com o título do torrent ou avisa quando nenhum torrent foi encontrado.
- **Ferramentas:** • Webhook endpoint: Ponto de entrada que recebe o título via requisição HTTP POST.
• TorrentSearchApi: Biblioteca/serviço usado para procurar torrents em múltiplos provedores.
• KickassTorrents: Provedor de torrents usado como fonte de resultados.
• Rarbg: Provedor de torrents usado como fonte de resultados.
• Transmission RPC: Serviço de torrent que recebe comandos para adicionar downloads via API (requisição POST, autenticação básica e header de sessão).
• Telegram Bot API: Serviço usado para enviar notificações ao usuário sobre sucesso ou erro.

## Fluxo visual

```mermaid
flowchart LR
    N1["Webhook"]
    N2["SearchTorrent"]
    N3["Start download"]
    N4["IF"]
    N5["Torrent not found"]
    N6["Telegram1"]
    N7["IF2"]
    N8["Start download new token"]

    N4 --> N3
    N4 --> N5
    N7 --> N8
    N7 --> N6
    N1 --> N2
    N2 --> N4
    N3 --> N7
    N8 --> N6
```

## Fluxo (.json) :

```json
{
  "nodes": [
    {
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "position": [
        310,
        300
      ],
      "webhookId": "6be952e8-e30f-4dd7-90b3-bc202ae9f174",
      "parameters": {
        "path": "6be952e8-e30f-4dd7-90b3-bc202ae9f174",
        "options": {
          "rawBody": true
        },
        "httpMethod": "POST"
      },
      "typeVersion": 1
    },
    {
      "name": "SearchTorrent",
      "type": "n8n-nodes-base.functionItem",
      "position": [
        530,
        300
      ],
      "parameters": {
        "functionCode": "const TorrentSearchApi = require('torrent-search-api');\n\nTorrentSearchApi.enableProvider('KickassTorrents');\nTorrentSearchApi.enableProvider('Rarbg');\n\nitem.title = $node[\"Webhook\"].json[\"body\"].title.trim();\n\nconst torrents = await TorrentSearchApi.search(item.title, 'All', 5);\n\nitem.torrents = torrents;\nitem.found = true;\n\nif(!torrents.length)\n  item.found = false;\n  \nconsole.log('Done!');\n\nreturn item;"
      },
      "typeVersion": 1
    },
    {
      "name": "Start download",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        960,
        280
      ],
      "parameters": {
        "url": "http://localhost:9091/transmission/rpc",
        "options": {},
        "requestMethod": "POST",
        "authentication": "basicAuth",
        "jsonParameters": true,
        "bodyParametersJson": "={\"method\":\"torrent-add\",\"arguments\":{\"paused\":false,\"download-dir\":\"/media/FILM/TORRENT\",\"filename\":\"{{$node[\"SearchTorrent\"].json[\"torrents\"][0][\"magnet\"]}}\"}}",
        "headerParametersJson": "{\"X-Transmission-Session-Id\":\"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\"}"
      },
      "credentials": {
        "httpBasicAuth": "Transmission-basic-auth"
      },
      "typeVersion": 1,
      "continueOnFail": true
    },
    {
      "name": "IF",
      "type": "n8n-nodes-base.if",
      "position": [
        740,
        300
      ],
      "parameters": {
        "conditions": {
          "boolean": [
            {
              "value1": "={{$json[\"found\"]}}",
              "value2": true
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Torrent not found",
      "type": "n8n-nodes-base.telegram",
      "position": [
        960,
        470
      ],
      "parameters": {
        "text": "=Film {{$node[\"Webhook\"].json[\"body\"].title}} non trovato.",
        "chatId": "00000000",
        "additionalFields": {}
      },
      "credentials": {
        "telegramApi": "your_bot_credential"
      },
      "typeVersion": 1
    },
    {
      "name": "Telegram1",
      "type": "n8n-nodes-base.telegram",
      "position": [
        1500,
        490
      ],
      "parameters": {
        "text": "=Scarico {{$node[\"Webhook\"].json[\"body\"].title}}!\nTitolo: {{$node[\"SearchTorrent\"].json[\"torrents\"][0][\"title\"]}}",
        "chatId": "0000000",
        "additionalFields": {}
      },
      "credentials": {
        "telegramApi": "your_bot_credential"
      },
      "typeVersion": 1
    },
    {
      "name": "IF2",
      "type": "n8n-nodes-base.if",
      "position": [
        1150,
        280
      ],
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "=\"{{$json[\"error\"][\"statusCode\"]}}\"",
              "value2": "=\"409\""
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Start download new token",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1340,
        260
      ],
      "parameters": {
        "url": "http://localhost:9091/transmission/rpc",
        "options": {},
        "requestMethod": "POST",
        "authentication": "basicAuth",
        "jsonParameters": true,
        "bodyParametersJson": "={\"method\":\"torrent-add\",\"arguments\":{\"paused\":false,\"download-dir\":\"/media/FILM/TORRENT\",\"filename\":\"{{$node[\"SearchTorrent\"].json[\"torrents\"][0][\"magnet\"]}}\"}}",
        "headerParametersJson": "={\"X-Transmission-Session-Id\":\"{{$node[\"Start download\"].json[\"error\"][\"response\"][\"headers\"][\"x-transmission-session-id\"]}}\"}"
      },
      "credentials": {
        "httpBasicAuth": "Transmission-basic-auth"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "IF": {
      "main": [
        [
          {
            "node": "Start download",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Torrent not found",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "IF2": {
      "main": [
        [
          {
            "node": "Start download new token",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Telegram1",
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
            "node": "SearchTorrent",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "SearchTorrent": {
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
    "Start download": {
      "main": [
        [
          {
            "node": "IF2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Start download new token": {
      "main": [
        [
          {
            "node": "Telegram1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-279"></a>

## Template 279 - Salvar anexos de faturas por remetente e data

- **Nome:** Salvar anexos de faturas por remetente e data
- **Descrição:** Lê e-mails da caixa 'Invoices', extrai e sanitiza cada anexo e metadados, e envia cada arquivo para um caminho organizado no Nextcloud.
- **Funcionalidade:** • Leitura de e-mails: Conecta-se à caixa de entrada 'Invoices' para obter mensagens e seus anexos.
• Extração de anexos: Separa cada anexo em itens individuais para processamento independente.
• Sanitização de nomes: Limpa e limita caracteres dos nomes dos arquivos, do remetente e da data para evitar caracteres inválidos.
• Renomeação e organização: Gera nomes padronizados combinando data, remetente e nome do arquivo para facilitar organização.
• Upload para armazenamento remoto: Envia os arquivos binários para um caminho estruturado em um servidor de arquivos remoto.
- **Ferramentas:** • Servidor IMAP: Fonte dos e-mails e anexos, usando a caixa de correio 'Invoices'.
• Nextcloud: Armazenamento remoto onde os anexos são salvos em um caminho organizado.

## Fluxo visual

```mermaid
flowchart LR
    N1["IMAP Email"]
    N2["Nextcloud"]
    N3["Map each attachment"]

    N1 --> N3
    N3 --> N2
```

## Fluxo (.json) :

```json
{
  "nodes": [
    {
      "name": "IMAP Email",
      "type": "n8n-nodes-base.emailReadImap",
      "position": [
        240,
        420
      ],
      "parameters": {
        "format": "resolved",
        "mailbox": "Invoices",
        "options": {
          "customEmailConfig": "[\"ALL\"]"
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Nextcloud",
      "type": "n8n-nodes-base.nextCloud",
      "position": [
        940,
        420
      ],
      "parameters": {
        "path": "=Documents/Invoices/{{$json[\"date\"]}}_{{$json[\"from\"]}}_{{$binary.file.fileName}}",
        "binaryDataUpload": true,
        "binaryPropertyName": "file"
      },
      "typeVersion": 1
    },
    {
      "name": "Map each attachment",
      "type": "n8n-nodes-base.function",
      "position": [
        620,
        420
      ],
      "parameters": {
        "functionCode": "const _ = require('lodash')\n\nconst sanitize = str => _.chain(str)\n  .replace(/[^A-Za-z0-9&.-]/g, '-') // sanitise via whitelist of characters\n  .replace(/-(?=-)/g, '') // remove repeated dashes - https://regexr.com/6ag8h\n  .trim('-') // trim any leading/trailing dashes\n  .truncate({\n    length: 60,\n    omission: '-' // when the string ends with '-', you'll know it was truncated\n  })\n  .value()\n\nconst result = _.flatMap(items.map(item => {\n  //console.log({item})\n\n  // Maps each attachment to a separate item\n  return _.values(item.binary).map(file => {\n    console.log(\"Saving attachement:\", file.fileName, 'from:', ...item.json.from.value)\n    \n    // sanitize filename but exclude extension\n    const filename_parts = file.fileName.split('.')\n    const ext = _.slice(filename_parts, filename_parts.length-1)\n    const filename_main = _.join(_.dropRight(filename_parts), '.')\n    file.fileName = sanitize(filename_main) + '.' + ext\n    \n    return {\n      json: {\n        from: sanitize(item.json.from.value[0].name),\n        date: sanitize(new Date(item.json.date).toISOString().split(\"T\")[0]) // get date part \"2020-01-01\"\n      }, \n      binary: { file }\n    }\n  })\n}))\n\n//console.log(result)\nreturn result"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "IMAP Email": {
      "main": [
        [
          {
            "node": "Map each attachment",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Map each attachment": {
      "main": [
        [
          {
            "node": "Nextcloud",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-280"></a>

## Template 280 - Resposta automática por IA a emails de informação

- **Nome:** Resposta automática por IA a emails de informação
- **Descrição:** Automatiza a leitura, resumo, classificação e resposta a emails de richiesta informazioni aziendali, usando modelos de linguagem e uma base de conhecimento vetorial para compor respostas curtas e profissionais.
- **Funcionalidade:** • Detecção de emails recebidos: Monitora uma caixa de entrada e inicia o fluxo quando chega um novo email.
• Conversão para formato legível: Converte o corpo do email (HTML) para formato texto/markdown para melhor análise pelo modelo de linguagem.
• Resumo automático: Gera um resumo conciso do conteúdo do email (limite de palavras configurado).
• Classificação do email: Classifica o email para decidir se é uma solicitação de informações sobre a empresa e direcionar o fluxo.
• Recuperação de conhecimento: Consulta uma base de conhecimento vetorial para extrair informações relevantes ao responder (quando aplicável).
• Composição da resposta: Usa modelos de linguagem para escrever uma resposta profissional e concisa baseada no contexto e no conhecimento disponível.
• Revisão e formatação: Revisa e formata a resposta em HTML (máximo de palavras definido) antes do envio.
• Envio automático: Envia a resposta ao remetente usando configurações SMTP apropriadas.
• Gestão da base de conhecimento: Permite criar/atualizar coleções vetoriais e indexar documentos provenientes do Google Drive para manter o conhecimento atualizado.
• Ramo de segurança: Possui caminho que não envia resposta para emails fora do escopo definido (ex.: não relacionados a informações da empresa).
- **Ferramentas:** • Servidor IMAP: Recebe e monitora emails de entrada para iniciar a automação.
• Servidor SMTP: Envia as respostas geradas para os remetentes.
• OpenAI / OpenRouter: Modelos de linguagem para sumarização, classificação, redação e geração de embeddings.
• Qdrant (base vetorial): Armazena e recupera vetores de documentos para fornecer contexto e respostas baseadas no conhecimento da empresa.
• Google Drive: Fonte de documentos que podem ser baixados e vetorizados para alimentar a base de conhecimento.
• API Qdrant (hospedagem Hetzner ou similar): Endpoints para criar, limpar e gerenciar coleções vetoriais remotamente.

## Fluxo visual

```mermaid
flowchart LR
    N1["Email Trigger (IMAP)"]
    N2["Markdown"]
    N3["DeepSeek R1"]
    N4["Send Email"]
    N5["Qdrant Vector Store"]
    N6["Embeddings OpenAI"]
    N7["Email Classifier"]
    N8["Email Summarization Chain"]
    N9["Write email"]
    N10["Review email"]
    N11["When clicking ‘Test workflow’"]
    N12["Create collection"]
    N13["Refresh collection"]
    N14["Get folder"]
    N15["Download Files"]
    N16["Default Data Loader"]
    N17["Token Splitter"]
    N18["Sticky Note3"]
    N19["Qdrant Vector Store1"]
    N20["Embeddings OpenAI1"]
    N21["Sticky Note5"]
    N22["Do nothing"]
    N23["OpenAI"]
    N24["DeepSeek"]
    N25["Sticky Note"]
    N26["OpenAI 4-o-mini"]

    N2 --> N8
    N14 --> N15
    N9 --> N10
    N10 --> N4
    N15 --> N19
    N7 --> N9
    N7 --> N22
    N13 --> N14
    N1 --> N2
    N8 --> N7
    N11 --> N12
    N11 --> N13
```

## Fluxo (.json) :

```json
{
  "id": "q8IFGLeOCGSfoWZu",
  "meta": {
    "instanceId": "a4bfc93e975ca233ac45ed7c9227d84cf5a2329310525917adaf3312e10d5462",
    "templateCredsSetupCompleted": true
  },
  "name": "Email AI Auto-responder. Summerize and send email",
  "tags": [],
  "nodes": [
    {
      "id": "59885699-0f6c-4522-acff-9e28b2a07b82",
      "name": "Email Trigger (IMAP)",
      "type": "n8n-nodes-base.emailReadImap",
      "position": [
        -440,
        -20
      ],
      "parameters": {
        "options": {}
      },
      "credentials": {
        "imap": {
          "id": "k31W9oGddl9pMDy4",
          "name": "IMAP info@n3witalia.com"
        }
      },
      "typeVersion": 2
    },
    {
      "id": "b268ab9d-b2e3-46e6-b7ae-70aff0b5484d",
      "name": "Markdown",
      "type": "n8n-nodes-base.markdown",
      "position": [
        -220,
        -20
      ],
      "parameters": {
        "html": "={{ $json.textHtml }}",
        "options": {}
      },
      "typeVersion": 1
    },
    {
      "id": "13c2d151-6f59-4e1f-a174-02d4d0bcaefd",
      "name": "DeepSeek R1",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        -20,
        160
      ],
      "parameters": {
        "model": {
          "__rl": true,
          "mode": "list",
          "value": "deepseek/deepseek-r1:free",
          "cachedResultName": "deepseek/deepseek-r1:free"
        },
        "options": {}
      },
      "credentials": {
        "openAiApi": {
          "id": "XJTqRiKFJpFs5MuX",
          "name": "OpenRouter account"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "8149e40d-64e6-4fb9-aebc-2a2483961f07",
      "name": "Send Email",
      "type": "n8n-nodes-base.emailSend",
      "position": [
        500,
        340
      ],
      "parameters": {
        "html": "={{ $json.text }}",
        "options": {},
        "subject": "=Re: {{ $('Email Trigger (IMAP)').item.json.subject }}",
        "toEmail": "={{ $('Email Trigger (IMAP)').item.json.from }}",
        "fromEmail": "={{ $('Email Trigger (IMAP)').item.json.to }}"
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
      "id": "633f0ce9-04ff-4653-8bbc-7457ba0d18bd",
      "name": "Qdrant Vector Store",
      "type": "@n8n/n8n-nodes-langchain.vectorStoreQdrant",
      "position": [
        -320,
        600
      ],
      "parameters": {
        "mode": "retrieve-as-tool",
        "options": {},
        "toolName": "company_knowladge_base",
        "toolDescription": "Extracts information regarding the request made.",
        "qdrantCollection": {
          "__rl": true,
          "mode": "id",
          "value": "=COLLECTION"
        },
        "includeDocumentMetadata": false
      },
      "credentials": {
        "qdrantApi": {
          "id": "iyQ6MQiVaF3VMBmt",
          "name": "QdrantApi account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "20daf5d3-dc9c-4fad-9f2f-98d86bc1660c",
      "name": "Embeddings OpenAI",
      "type": "@n8n/n8n-nodes-langchain.embeddingsOpenAi",
      "position": [
        -340,
        760
      ],
      "parameters": {
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
      "id": "67699bca-4096-4259-bbd4-51a879539aca",
      "name": "Email Classifier",
      "type": "@n8n/n8n-nodes-langchain.textClassifier",
      "position": [
        360,
        -20
      ],
      "parameters": {
        "options": {
          "fallback": "other",
          "multiClass": false,
          "enableAutoFixing": true,
          "systemPromptTemplate": "Please classify the text provided by the user into one of the following categories: {categories}, and use the provided formatting instructions below. Don't explain, and only output the json.\n"
        },
        "inputText": "=You must classify the following email::\n\n{{ $json.response.text }}",
        "categories": {
          "categories": [
            {
              "category": "Company info request",
              "description": "Company info request"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "id": "9f7742e9-87d5-40b9-9129-0777d8a37933",
      "name": "Email Summarization Chain",
      "type": "@n8n/n8n-nodes-langchain.chainSummarization",
      "position": [
        0,
        -20
      ],
      "parameters": {
        "options": {
          "binaryDataKey": "={{ $json.data }}",
          "summarizationMethodAndPrompts": {
            "values": {
              "prompt": "=Write a concise summary of the following in max 100 words:\n\n\"{{ $json.data }}\"\n\nDo not enter the total number of words used.",
              "combineMapPrompt": "=Write a concise summary of the following in max 100 words:\n\n\"{{ $json.data }}\"\n"
            }
          }
        },
        "operationMode": "nodeInputBinary"
      },
      "typeVersion": 2
    },
    {
      "id": "e2d404c0-2aad-407d-b75e-5ef0c5105c0e",
      "name": "Write email",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        -440,
        340
      ],
      "parameters": {
        "text": "=Write the text to reply to the following email:\n\n{{ $json.response.text }}",
        "options": {
          "systemMessage": "You are an expert at answering emails. You need to answer them professionally based on the information you have. This is a business email. Be concise and never exceed 100 words."
        },
        "promptType": "define"
      },
      "typeVersion": 1.7
    },
    {
      "id": "3786c2de-c5cb-4233-826e-7265f2bccbdb",
      "name": "Review email",
      "type": "@n8n/n8n-nodes-langchain.chainLlm",
      "position": [
        40,
        340
      ],
      "parameters": {
        "text": "=Review at the following email:\n\n{{ $json.output }}",
        "messages": {
          "messageValues": [
            {
              "message": "=If you are an expert in reviewing emails before sending them. You need to review and structure them in such a way that you can send them. It must be in HTML format and you can insert (if you think it is appropriate) only HTML characters such as <br>, <b>, <i>, <p> where necessary.\n\nNon superare le 100 parole."
            }
          ]
        },
        "promptType": "define",
        "hasOutputParser": true
      },
      "typeVersion": 1.5
    },
    {
      "id": "baf60eba-5e7b-467f-b27e-1388a91622d0",
      "name": "When clicking ‘Test workflow’",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        -500,
        -980
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "77e6160f-20a7-4a75-9fef-bc875b953a16",
      "name": "Create collection",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        -200,
        -1120
      ],
      "parameters": {
        "url": "https://QDRANTURL/collections/COLLECTION",
        "method": "POST",
        "options": {},
        "jsonBody": "{\n \"filter\": {}\n}",
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
          "id": "qhny6r5ql9wwotpn",
          "name": "Qdrant API (Hetzner)"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "ab7764d1-531c-4281-8b89-015fb3f5e780",
      "name": "Refresh collection",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        -200,
        -860
      ],
      "parameters": {
        "url": "https://QDRANTURL/collections/COLLECTION/points/delete",
        "method": "POST",
        "options": {},
        "jsonBody": "{\n \"filter\": {}\n}",
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
          "id": "qhny6r5ql9wwotpn",
          "name": "Qdrant API (Hetzner)"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "cd3eaa81-0f94-484b-b0c2-ecf0ca4541dc",
      "name": "Get folder",
      "type": "n8n-nodes-base.googleDrive",
      "position": [
        20,
        -860
      ],
      "parameters": {
        "filter": {
          "driveId": {
            "__rl": true,
            "mode": "list",
            "value": "My Drive",
            "cachedResultUrl": "https://drive.google.com/drive/my-drive",
            "cachedResultName": "My Drive"
          },
          "folderId": {
            "__rl": true,
            "mode": "id",
            "value": "=test-whatsapp"
          }
        },
        "options": {},
        "resource": "fileFolder"
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
      "id": "b39ecd2d-4d5b-4885-86a9-2cfe9f6074ef",
      "name": "Download Files",
      "type": "n8n-nodes-base.googleDrive",
      "position": [
        240,
        -860
      ],
      "parameters": {
        "fileId": {
          "__rl": true,
          "mode": "id",
          "value": "={{ $json.id }}"
        },
        "options": {
          "googleFileConversion": {
            "conversion": {
              "docsToFormat": "text/plain"
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
      "id": "8171b8f2-998d-4d72-ac28-524daae4a2d7",
      "name": "Default Data Loader",
      "type": "@n8n/n8n-nodes-langchain.documentDefaultDataLoader",
      "position": [
        620,
        -660
      ],
      "parameters": {
        "options": {},
        "dataType": "binary"
      },
      "typeVersion": 1
    },
    {
      "id": "ec6737ad-3fbe-4864-9df8-44f82d6f2c5c",
      "name": "Token Splitter",
      "type": "@n8n/n8n-nodes-langchain.textSplitterTokenSplitter",
      "position": [
        600,
        -500
      ],
      "parameters": {
        "chunkSize": 300,
        "chunkOverlap": 30
      },
      "typeVersion": 1
    },
    {
      "id": "57b6a4f3-e935-4058-bfdf-309d606c0ca9",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        0,
        -1180
      ],
      "parameters": {
        "color": 6,
        "width": 880,
        "height": 220,
        "content": "# STEP 1\n\n## Create Qdrant Collection\nChange:\n- QDRANTURL\n- COLLECTION"
      },
      "typeVersion": 1
    },
    {
      "id": "21e2326a-138d-46f3-a849-a80aa7917da9",
      "name": "Qdrant Vector Store1",
      "type": "@n8n/n8n-nodes-langchain.vectorStoreQdrant",
      "position": [
        480,
        -860
      ],
      "parameters": {
        "mode": "insert",
        "options": {},
        "qdrantCollection": {
          "__rl": true,
          "mode": "id",
          "value": "=COLLECTION"
        }
      },
      "credentials": {
        "qdrantApi": {
          "id": "iyQ6MQiVaF3VMBmt",
          "name": "QdrantApi account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "0818fb6a-2adf-4725-90a4-11cdd7d14036",
      "name": "Embeddings OpenAI1",
      "type": "@n8n/n8n-nodes-langchain.embeddingsOpenAi",
      "position": [
        500,
        -620
      ],
      "parameters": {
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
      "id": "8949d938-2743-45d6-b2ad-ce4ac139e0a3",
      "name": "Sticky Note5",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -220,
        -920
      ],
      "parameters": {
        "color": 4,
        "width": 620,
        "height": 400,
        "content": "# STEP 2\n\n\n\n\n\n\n\n\n\n\n\n\n## Documents vectorization with Qdrant and Google Drive\nChange:\n- QDRANTURL\n- COLLECTION"
      },
      "typeVersion": 1
    },
    {
      "id": "36d384be-3e11-43b1-b8c3-f63df600a6a6",
      "name": "Do nothing",
      "type": "n8n-nodes-base.noOp",
      "position": [
        820,
        0
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "386c27cb-6e69-4d96-a8ab-8cfd43e6b171",
      "name": "OpenAI",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        -520,
        580
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
          "id": "CDX6QM4gLYanh0P4",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "0bd17bef-e205-464e-9b36-dcda75254e06",
      "name": "DeepSeek",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        40,
        540
      ],
      "parameters": {
        "model": {
          "__rl": true,
          "mode": "list",
          "value": "deepseek/deepseek-r1:free",
          "cachedResultName": "deepseek/deepseek-r1:free"
        },
        "options": {}
      },
      "credentials": {
        "openAiApi": {
          "id": "XJTqRiKFJpFs5MuX",
          "name": "OpenRouter account"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "3e68a65f-af29-432f-8159-4a599e8a0866",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -540,
        -320
      ],
      "parameters": {
        "width": 1620,
        "height": 240,
        "content": "# STEP 3 - MAIN FLOW\n\n- Transform the email into Markdown format for optimal reading by the LLM model\n- Email Summarization through DeepSeek R1 (any model can be used)\n- I classify the email in such a way as to continue only with emails regarding general information about the company. In this way I can respond independently through the information obtained from the vector database\n- I create a chain where I entrust the review of the email to a high-performance model designed for this purpose\n- I send the response email\n\n\n"
      },
      "typeVersion": 1
    },
    {
      "id": "3b6ae6aa-75a8-4038-bbc2-248ab533b3ab",
      "name": "OpenAI 4-o-mini",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        360,
        160
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
          "id": "CDX6QM4gLYanh0P4",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1.2
    }
  ],
  "active": false,
  "pinData": {
    "Email Trigger (IMAP)": [
      {
        "json": {
          "to": "info@n3witalia.com",
          "date": "Wed, 5 Feb 2025 13:38:51 +0100",
          "from": "n3w Italia <info@n3w.it>",
          "subject": "Richiesta di informazioni aziendali",
          "metadata": {
            "x-gm-gg": "ASbGncsq6D/oyHjmnpbG4gCUuC0rZNUR8WW4c+LmGMSdGJ1lHkRnKn7b3ngCdndp8NB\tkyDG3unga3kPebzAv1LO7DS6rDMHTWb8F7kZoLijJUGlAy6wqmfX/n4z2DH1uSxp7EsnIP9K9",
            "arc-seal": "i=1; s=arc-2022; d=mailchannels.net; t=1738759167; a=rsa-sha256;\tcv=none;\tb=Fdjl0FQlp2JxGTUy9B6U3UVZDgw2xRK0M9ge2H7QXFuX8Jhy2/eDktsWwyDOuAnebq+pZB\tZmt9/ZWM+VqpfvPc9j4+cpX1HnXkRnyV9HMp0KK1Srpkuc7iimLDX1puMEQP08mC8fBI9n\tYW9JAMVmy55D2xtcOgqQPe6HUsAM8vFfk0y7dv7aV/MMc4tW+lyBddf4BHedDPabmHtog9\tlI9qQB8f5o78KJoJHi9jUfoibHrw7ePCi/XNi1KzfLhkkcvaEhOIg82JgyaTOVuLX4TTpy\t713VrUVQKemdE8AJBgxrUyI8AM/XZDRxF92tDNRD5k+rFxVwZnNg1KzovEUFiw==",
            "received": "from postfix-inbound-v2-3.inbound.mailchannels.net (inbound-egress-7.mailchannels.net [23.83.220.5])\t(using TLSv1.3 with cipher TLS_AES_256_GCM_SHA384 (256/256 bits)\t key-exchange X25519 server-signature RSA-PSS (2048 bits) server-digest SHA256)\t(No client certificate requested)\tby pdx1-sub0-mail-mx201.dreamhost.com (Postfix) with ESMTPS id 4Yp0DP2WKvz6n5V\tfor <info@n3witalia.com>; Wed, 5 Feb 2025 04:39:33 -0800 (PST)",
            "message-id": "<CACo-EPti-vvs3198N-KKhAMnm70ppkmGJPkUz3Y483wxAv_z3g@mail.gmail.com>",
            "x-received": "by 2002:a05:6820:4ccb:b0:5fa:7e37:e42e with SMTP id 006d021491bc7-5fc479d7b7dmr1800193eaf.3.1738759166233; Wed, 05 Feb 2025 04:39:26 -0800 (PST)",
            "return-path": "<info@n3w.it>",
            "content-type": "multipart/alternative; boundary=\"000000000000742c2a062d646a8f\"",
            "delivered-to": "x21967472@pdx1-sub0-mail-mx201.dreamhost.com",
            "mime-version": "1.0",
            "received-spf": "none (dmarc-service-75b56dd9b6-qz8tf: n3w.it does not provide an SPF record) client-ip=209.85.161.50; envelope-from=info@n3w.it; helo=mail-oo1-f50.google.com;",
            "x-message-id": "YDPlyzG1R2Ky6usgMxqEJvf1",
            "x-gm-features": "AWEUYZl838uJdYn-9fUMGZvOqArNBONSW_VOkpWSkn1OYyR-HUtJL8UAJf2I33g",
            "x-original-to": "info@n3witalia.com",
            "dkim-signature": "v=1; a=rsa-sha256; c=relaxed/relaxed; d=n3w-it.20230601.gappssmtp.com; s=20230601; t=1738759166; x=1739363966; darn=n3witalia.com; h=to:subject:message-id:date:from:mime-version:from:to:cc:subject :date:message-id:reply-to; bh=2N6Y8wbn3yS/TpkJr2ZQZ3rEEFMq1gc4mSHvPNXonAg=; b=eH1Dg2CwoWEuiif+VkxoPH8PcgiveMtY7urkbJAXXAEnpmkknbrSX7fLQ/pdfnV2YF RaDEVEFBYeYde7pra1NhNmQXQfamV6dxTZSoNOVj0DtdOuSZVYC4BQMMQiIk7emERgdx keDGBtYe2SifOK9QDK4deKKFPaswC7vATsPmBIAnN0MDahaOlsDPbm6aFSR39aK0qEpx MTylUSCNFx52cTYegrpzMGCRTrCxcHwvpq0gGZo1ol0mlq5WC4sa260qsVEQq566N1wh ICipbEhLdoX0nryrR67fJ+mq05kfg39gv++0p1aZl3/ahTdLTijPJswPs4phiTUj6fUH Z3Fg==",
            "x-gm-message-state": "AOJu0YwNwfJ1yYtAsu71S9Oy+BVSQqPDS1EJCni+CLWs7aDwxkFYjxsP\tX0A935B/tHpnOhgJuR8W5FwuKnXSFMZ/xP8TFQz8zBVGw7DYInyaC0lKAxPSbBsLDIFyVj2LYki\tR4sfj6a9YJDaWKE/HYPwbidCOfOV/mZvqJ2ESL5uJgSL0W4FrMJKmondc",
            "x-google-smtp-source": "AGHT+IFsZ2bQKEg+M9ddjCSDXjf2Okz49s6pteuNGyJAkFpjMLwhH4mshXYItB/GVj4r8fUIiAiACRT+QDfae1MMj48=",
            "arc-message-signature": "i=1; a=rsa-sha256; c=relaxed/relaxed; d=mailchannels.net;\ts=arc-2022; t=1738759167;\th=from:from:reply-to:subject:subject:date:date:message-id:message-id:\t to:to:cc:mime-version:mime-version:content-type:content-type:\t dkim-signature; bh=2N6Y8wbn3yS/TpkJr2ZQZ3rEEFMq1gc4mSHvPNXonAg=;\tb=xytHIe/PVvcfCsSYAhcVE9VlTvmbJcVbkpq0oKRt4H0M1VOfZZlsg5ILysJvwLAzrRO7SZ\tDUrh4bw57jqMpcE+Sk5AAcbgBMc6x1G+Wf/2nqnjy0hRCyqtajuUwtFOS3kDM7TKvFOU+/\tMFChI5mg97hb/0loj8DWQ+J24bu4a6YixGDglupW3JYJoDsPWje2oA+mYyiI5tsnRXFEwe\tpku9KlXkPburbm/ASqKbbi1Y9bEOa2vlRwLL3fFontmC+3kgogunW2fjf4YJlFlSaAj/Xb\tZXQiytNgKOJtkBQMvb0AmYMLgBbYdOBVzUkOUTQCP3Wzbuu0zslvl7cS3HkFIg==",
            "authentication-results": "inbound.mailchannels.net; spf=none smtp.mailfrom=info@n3w.it; dkim=temperror header.d=n3w-it.20230601.gappssmtp.com; dmarc=none; arc=none",
            "x-google-dkim-signature": "v=1; a=rsa-sha256; c=relaxed/relaxed; d=1e100.net; s=20230601; t=1738759166; x=1739363966; h=to:subject:message-id:date:from:mime-version:x-gm-message-state :from:to:cc:subject:date:message-id:reply-to; bh=2N6Y8wbn3yS/TpkJr2ZQZ3rEEFMq1gc4mSHvPNXonAg=; b=h+GPFjY1knf3xPd+R62zD7JNhs37K+F1qx+6EA3codzYY+yTXSJyTuETXOGVW5r2VK GOcntvGBdeijxte5RLmN6ZwLjvzePLlJLQVOnY8FICowUbwClQbDW1vXvucD+WaGpnBg O95TH/8jKWRBU34EZ9kAY5EqtauKSt675WyhVCmmT864BPbVV335d0t9RgJwV86rM9zy /miMTqpWeDJxDcX4thRlIk19GDc2Wh+5bqFD9kacOAur46RWdwqWaU7T8+5bQmbrKUg5 hqeO8ZDefVV6AyOjSnuLItHcHhlk1PaQ9uOumkRnFQfLUjS08bvLEnJyMA1YrEdo7mCi tD2Q==",
            "arc-authentication-results": "i=1;\tinbound-rspamd-8684fd6f95-jsctp;\tnone"
          },
          "textHtml": "<div dir=\"ltr\">mi chiamo Davide e sto scrivendo per richiedere alcune informazioni riguardanti il vostro negozio di tecnologia. Sto valutando diverse opzioni per [motivo della richiesta, ad esempio: acquistare un nuovo dispositivo, richiedere assistenza tecnica, o esplorare servizi aziendali] e sarei grato se poteste fornirmi alcuni dettagli utili.<br><br>In particolare, avrei bisogno di sapere:<br><br>Gli orari di apertura del vostro negozio, inclusi eventuali giorni di chiusura o orari ridotti durante i festivi.<br><br>Se offrite servizi di assistenza tecnica per dispositivi elettronici e, in caso affermativo, quali tipologie di dispositivi supportate (es. smartphone, computer, tablet).<br><br>Se disponete di un catalogo prodotti aggiornato o un sito web dove posso consultare lâofferta disponibile.<br><br>Se effettuate consegne a domicilio o se Ã¨ possibile prenotare prodotti online per il ritiro in negozio.<br><br>Se offrite sconti o promozioni per studenti, aziende o clienti abituali.<br><br>Se organizzate eventi o workshop legati alla tecnologia, come corsi di formazione o presentazioni di nuovi prodotti.<br><br>Inoltre, sarei interessato a sapere se il vostro negozio aderisce a programmi di riciclo di dispositivi elettronici o se offrite servizi di smaltimento ecologico per apparecchiature obsolete.<br><br>Se possibile, gradirei ricevere anche informazioni sui metodi di pagamento accettati (es. carte di credito, PayPal, finanziamenti) e se Ã¨ possibile richiedere un preventivo personalizzato per acquisti di grandi dimensioni.<br><br>Resto a disposizione per eventuali chiarimenti o per fornire ulteriori dettagli sulle mie esigenze. Vi ringrazio in anticipo per il tempo dedicato alla mia richiesta e attendo con interesse una vostra risposta.<br><br>Cordiali saluti,</div>\r\n",
          "textPlain": "mi chiamo Davide e sto scrivendo per richiedere alcune informazioni\r\nriguardanti il vostro negozio di tecnologia. Sto valutando diverse opzioni\r\nper [motivo della richiesta, ad esempio: acquistare un nuovo dispositivo,\r\nrichiedere assistenza tecnica, o esplorare servizi aziendali] e sarei grato\r\nse poteste fornirmi alcuni dettagli utili.\r\n\r\nIn particolare, avrei bisogno di sapere:\r\n\r\nGli orari di apertura del vostro negozio, inclusi eventuali giorni di\r\nchiusura o orari ridotti durante i festivi.\r\n\r\nSe offrite servizi di assistenza tecnica per dispositivi elettronici e, in\r\ncaso affermativo, quali tipologie di dispositivi supportate (es.\r\nsmartphone, computer, tablet).\r\n\r\nSe disponete di un catalogo prodotti aggiornato o un sito web dove posso\r\nconsultare lâofferta disponibile.\r\n\r\nSe effettuate consegne a domicilio o se Ã¨ possibile prenotare prodotti\r\nonline per il ritiro in negozio.\r\n\r\nSe offrite sconti o promozioni per studenti, aziende o clienti abituali.\r\n\r\nSe organizzate eventi o workshop legati alla tecnologia, come corsi di\r\nformazione o presentazioni di nuovi prodotti.\r\n\r\nInoltre, sarei interessato a sapere se il vostro negozio aderisce a\r\nprogrammi di riciclo di dispositivi elettronici o se offrite servizi di\r\nsmaltimento ecologico per apparecchiature obsolete.\r\n\r\nSe possibile, gradirei ricevere anche informazioni sui metodi di pagamento\r\naccettati (es. carte di credito, PayPal, finanziamenti) e se Ã¨ possibile\r\nrichiedere un preventivo personalizzato per acquisti di grandi dimensioni.\r\n\r\nResto a disposizione per eventuali chiarimenti o per fornire ulteriori\r\ndettagli sulle mie esigenze. Vi ringrazio in anticipo per il tempo dedicato\r\nalla mia richiesta e attendo con interesse una vostra risposta.\r\n\r\nCordiali saluti,\r\n"
        }
      }
    ],
    "Email Summarization Chain": [
      {
        "json": {
          "response": {
            "text": "Davide contatta il negozio di tecnologia per richiedere informazioni in merito a: orari di apertura (compresi festivi e chiusure), assistenza tecnica (specificando dispositivi supportati come smartphone, computer, tablet), disponibilità di catalogo aggiornato/sito web, opzioni di consegna a domicilio o ritiro in negozio, sconti per studenti/aziende/clienti abituali, eventi/workshop tematici, programmi di riciclo/smaltimento ecologico, metodi di pagamento accettati (carte, PayPal, finanziamenti) e preventivi personalizzati per acquisti consistenti. Si rende disponibile per ulteriori chiarimenti e ringrazia per la risposta. (99 parole)"
          }
        }
      }
    ]
  },
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "eee08614-3096-477a-b462-859782a74188",
  "connections": {
    "OpenAI": {
      "ai_languageModel": [
        [
          {
            "node": "Write email",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "DeepSeek": {
      "ai_languageModel": [
        [
          {
            "node": "Review email",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Markdown": {
      "main": [
        [
          {
            "node": "Email Summarization Chain",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get folder": {
      "main": [
        [
          {
            "node": "Download Files",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "DeepSeek R1": {
      "ai_languageModel": [
        [
          {
            "node": "Email Summarization Chain",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Write email": {
      "main": [
        [
          {
            "node": "Review email",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Review email": {
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
    "Download Files": {
      "main": [
        [
          {
            "node": "Qdrant Vector Store1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Token Splitter": {
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
    "OpenAI 4-o-mini": {
      "ai_languageModel": [
        [
          {
            "node": "Email Classifier",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Email Classifier": {
      "main": [
        [
          {
            "node": "Write email",
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
    "Embeddings OpenAI1": {
      "ai_embedding": [
        [
          {
            "node": "Qdrant Vector Store1",
            "type": "ai_embedding",
            "index": 0
          }
        ]
      ]
    },
    "Refresh collection": {
      "main": [
        [
          {
            "node": "Get folder",
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
            "node": "Qdrant Vector Store1",
            "type": "ai_document",
            "index": 0
          }
        ]
      ]
    },
    "Qdrant Vector Store": {
      "ai_tool": [
        [
          {
            "node": "Write email",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Email Trigger (IMAP)": {
      "main": [
        [
          {
            "node": "Markdown",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Email Summarization Chain": {
      "main": [
        [
          {
            "node": "Email Classifier",
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
            "node": "Create collection",
            "type": "main",
            "index": 0
          },
          {
            "node": "Refresh collection",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-281"></a>

## Template 281 - Notificar novo produto WooCommerce no Slack

- **Nome:** Notificar novo produto WooCommerce no Slack
- **Descrição:** Quando um novo produto é criado no WooCommerce, o fluxo envia uma notificação formatada para um canal do Slack com os principais detalhes do produto.
- **Funcionalidade:** • Detecção de novo produto: inicia a automação ao identificar a criação de um produto na loja.
• Coleta de dados do produto: obtém nome, preço regular, preço promocional, link permanente e data de criação do item.
• Envio de notificação ao Slack: publica uma mensagem no canal configurado anunciando o novo produto.
• Montagem de anexo formatado: inclui um anexo com cor, campos detalhados (Nome, Price, Sale Price, Link) e um rodapé com a data de adição.
- **Ferramentas:** • WooCommerce: plataforma de comércio eletrônico usada para detectar a criação de produtos e fornecer seus dados.
• Slack: serviço de comunicação usado para enviar notificações ao canal designado.

## Fluxo visual

```mermaid
flowchart LR
    N1["Product Created"]
    N2["Send to Slack"]

    N1 --> N2
```

## Fluxo (.json) :

```json
{
  "id": 80,
  "name": "New WooCommerce product to Slack",
  "nodes": [
    {
      "name": "Product Created",
      "type": "n8n-nodes-base.wooCommerceTrigger",
      "position": [
        320,
        500
      ],
      "webhookId": "267c4855-6227-4d33-867e-74600097473e",
      "parameters": {
        "event": "product.created"
      },
      "credentials": {
        "wooCommerceApi": {
          "id": "48",
          "name": "WooCommerce account"
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Send to Slack",
      "type": "n8n-nodes-base.slack",
      "position": [
        540,
        500
      ],
      "parameters": {
        "text": ":new: A new product has been added! :new:",
        "channel": "woo-commerce",
        "blocksUi": {
          "blocksValues": []
        },
        "attachments": [
          {
            "color": "#66FF00",
            "fields": {
              "item": [
                {
                  "short": false,
                  "title": "Name",
                  "value": "={{$json[\"name\"]}}"
                },
                {
                  "short": true,
                  "title": "Price",
                  "value": "={{$json[\"regular_price\"]}}"
                },
                {
                  "short": true,
                  "title": "Sale Price",
                  "value": "={{$json[\"sale_price\"]}}"
                },
                {
                  "short": false,
                  "title": "Link",
                  "value": "={{$json[\"permalink\"]}}"
                }
              ]
            },
            "footer": "=Added: {{$json[\"date_created\"]}}"
          }
        ],
        "otherOptions": {}
      },
      "credentials": {
        "slackApi": {
          "id": "53",
          "name": "Slack Access Token"
        }
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "Product Created": {
      "main": [
        [
          {
            "node": "Send to Slack",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
