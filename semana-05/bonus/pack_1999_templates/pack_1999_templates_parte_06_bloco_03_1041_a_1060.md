# PACK 1999 TEMPLATES PARTE 06 - Bloco 3

Templates neste bloco: 20

## Sumário

- [Template 1041 - Agendamento de Entrevista via IA](#template-1041)
- [Template 1042 - Resumo de emails e envio para Messenger](#template-1042)
- [Template 1043 - Monitorar lançamentos relevantes no Product Hunt](#template-1043)
- [Template 1044 - Enriquecimento de perfis LinkedIn e geração de ice breakers](#template-1044)
- [Template 1045 - Auditoria de Segurança de Website](#template-1045)
- [Template 1046 - Enriquecimento de leads imobiliários](#template-1046)
- [Template 1047 - Criar campanha Emelia e adicionar contato](#template-1047)
- [Template 1048 - Bot Telegram integrado com NeurochainAI (texto e imagem)](#template-1048)
- [Template 1049 - Deduplicação automática de arquivos no Google Drive](#template-1049)
- [Template 1050 - Pedido de compra Outlook: XLSX para saída estruturada](#template-1050)
- [Template 1051 - Bot Telegram com memória em Supabase](#template-1051)
- [Template 1052 - Atualizar taxas de câmbio USD e registrar dados](#template-1052)
- [Template 1053 - Anunciar novo produto nas redes](#template-1053)
- [Template 1054 - Obter página web e retornar Markdown](#template-1054)
- [Template 1055 - Coleta diária do Product Hunt para Sheets](#template-1055)
- [Template 1056 - Criar ticket Zendesk para pedidos novos](#template-1056)
- [Template 1057 - Criar pastas no Drive por caminho](#template-1057)
- [Template 1058 - Notificação de erro via Telegram](#template-1058)
- [Template 1059 - Previsão do tempo via Slack](#template-1059)
- [Template 1060 - Obter informações e filtrar servidores Scaleway](#template-1060)

---

<a id="template-1041"></a>

## Template 1041 - Agendamento de Entrevista via IA

- **Nome:** Agendamento de Entrevista via IA
- **Descrição:** Fluxo que permite aos candidatos agendar entrevistas por conversa com IA. Ele verifica a disponibilidade, gera slots de 30 minutos durante o horário comercial em fuso horário Eastern, cruza as opções disponíveis, e agenda a entrevista no Google Calendar, fornecendo confirmação ao usuário.
- **Funcionalidade:** • Detecção de input do usuário: inicia o agendamento quando o chat recebe uma mensagem.
• Verificação de disponibilidade: consulta a agenda para saber horários livres.
• Geração de slots de 30 minutos: cria blocos entre 9h e 17h, de segunda a sexta, em Eastern Time.
• Combinação de slots com disponibilidade: identifica horários viáveis sem sobreposição.
• Retorno de horários disponíveis: apresenta opções ao usuário em formato legível.
• Confirmação e agendamento: agenda a entrevista no calendário e prepara a confirmação.
- **Ferramentas:** • Google Calendar: verificação de disponibilidade e criação de eventos de entrevista.
• OpenAI: processamento de linguagem natural para conduzir a conversa e gerar respostas.

## Fluxo visual

```mermaid
flowchart LR
    N1["OpenAI Chat Model2"]
    N2["Window Buffer Memory2"]
    N3["OpenAI Chat Model4"]
    N4["Run Get Availability"]
    N5["Sticky Note1"]
    N6["check day names"]
    N7["Sticky Note"]
    N8["Convert Output to JSON"]
    N9["Interview Scheduler"]
    N10["If Final Output"]
    N11["Respond for More Info"]
    N12["Parse to JSON"]
    N13["Set Meeting with Google"]
    N14["Final Response to User"]
    N15["Generate Interview Times"]
    N16["Check My Calendar"]
    N17["Split Events into 30 min blocks"]
    N18["Add Blocked Field"]
    N19["Generate 30 Minute Timeslots"]
    N20["Combine My Calendar with All Slots"]
    N21["Check if Calendar Blocked"]
    N22["Return string of all available times"]
    N23["Get Availability"]
    N24["Sticky Note2"]
    N25["When chat message received"]

    N10 --> N8
    N10 --> N11
    N23 --> N16
    N23 --> N19
    N18 --> N20
    N16 --> N17
    N9 --> N10
    N8 --> N13
    N13 --> N14
    N21 --> N22
    N25 --> N9
    N19 --> N20
    N17 --> N18
    N20 --> N21
```

## Fluxo (.json) :

```json
{
  "id": "bh3H2b654RSYgIm9",
  "meta": {
    "instanceId": "efb474b59b0341d7791932605bd9ff04a6c7ed9941fdd53dc4a2e4b99a6f9439",
    "templateCredsSetupCompleted": true
  },
  "name": "Inverview Scheduler",
  "tags": [],
  "nodes": [
    {
      "id": "cd5664f9-0b6b-491a-a0a0-1d8b3b2f2461",
      "name": "OpenAI Chat Model2",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        320,
        1480
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
          "id": "ghJTvay8CvwXDsXz",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "e8ca4a14-ee58-4be0-838b-5cbf8a802b6e",
      "name": "Window Buffer Memory2",
      "type": "@n8n/n8n-nodes-langchain.memoryBufferWindow",
      "position": [
        520,
        1480
      ],
      "parameters": {
        "sessionKey": "={{ $json.sessionId }}",
        "sessionIdType": "customKey",
        "contextWindowLength": 10
      },
      "typeVersion": 1.3
    },
    {
      "id": "d2957530-acd1-4875-a75b-69b890f08065",
      "name": "OpenAI Chat Model4",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        1220,
        1440
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
          "id": "ghJTvay8CvwXDsXz",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "897c8189-aaa9-45c7-99c6-95378a7a13f2",
      "name": "Run Get Availability",
      "type": "@n8n/n8n-nodes-langchain.toolWorkflow",
      "position": [
        720,
        1520
      ],
      "parameters": {
        "name": "get_availability",
        "source": "parameter",
        "description": "Call this tool to get my availability",
        "workflowJson": "{\n  \"nodes\": [\n    {\n      \"parameters\": {\n        \"operation\": \"getAll\",\n        \"calendar\": {\n          \"__rl\": true,\n          \"value\": \"rbreen.ynteractive@gmail.com\",\n          \"mode\": \"list\",\n          \"cachedResultName\": \"rbreen.ynteractive@gmail.com\"\n        },\n        \"returnAll\": true,\n        \"options\": {\n          \"fields\": \"\"\n        }\n      },\n      \"type\": \"n8n-nodes-base.googleCalendar\",\n      \"typeVersion\": 1.3,\n      \"position\": [\n        -500,\n        220\n      ],\n      \"id\": \"a1017705-8866-469f-83e0-9f5d5f37af53\",\n      \"name\": \"Check My Calendar\",\n      \"credentials\": {\n        \"googleCalendarOAuth2Api\": {\n          \"id\": \"nc5M45R7LyFadByw\",\n          \"name\": \"Google Calendar account\"\n        }\n      }\n    },\n    {\n      \"parameters\": {\n        \"jsCode\": \"const events = items.map(item => item.json);\\nconst intervalMinutes = 30;\\nconst timeZone = 'America/New_York';\\n\\nfunction formatToEastern(date) {\\n  const tzDate = new Intl.DateTimeFormat('en-US', {\\n    timeZone,\\n    year: 'numeric',\\n    month: '2-digit',\\n    day: '2-digit',\\n    hour: '2-digit',\\n    minute: '2-digit',\\n    second: '2-digit',\\n    hour12: false\\n  }).formatToParts(date).reduce((acc, part) => {\\n    if (part.type !== 'literal') acc[part.type] = part.value;\\n    return acc;\\n  }, {});\\n\\n  const offset = getEasternOffset(date);\\n  return `${tzDate.year}-${tzDate.month}-${tzDate.day}T${tzDate.hour}:${tzDate.minute}:${tzDate.second}${offset}`;\\n}\\n\\nfunction getEasternOffset(date) {\\n  const options = { timeZone, timeZoneName: 'short' };\\n  const parts = new Intl.DateTimeFormat('en-US', options).formatToParts(date);\\n  const tzName = parts.find(p => p.type === 'timeZoneName').value;\\n  return tzName.includes('EDT') ? '-04:00' : '-05:00';\\n}\\n\\nfunction alignToPreviousSlot(date) {\\n  const aligned = new Date(date);\\n  const minutes = aligned.getMinutes();\\n  aligned.setMinutes(minutes < 30 ? 0 : 30, 0, 0);\\n  return aligned;\\n}\\n\\nfunction alignToNextSlot(date) {\\n  const aligned = new Date(date);\\n  const minutes = aligned.getMinutes();\\n  if (minutes > 0 && minutes <= 30) {\\n    aligned.setMinutes(30, 0, 0);\\n  } else if (minutes > 30) {\\n    aligned.setHours(aligned.getHours() + 1);\\n    aligned.setMinutes(0, 0, 0);\\n  } else {\\n    aligned.setMinutes(0, 0, 0);\\n  }\\n  return aligned;\\n}\\n\\nconst splitEventIntoETBlocks = (event) => {\\n  const blocks = [];\\n\\n  let current = alignToPreviousSlot(new Date(event.start.dateTime));\\n  const eventEnd = alignToNextSlot(new Date(event.end.dateTime));\\n\\n  while (current < eventEnd) {\\n    const blockEnd = new Date(current);\\n    blockEnd.setMinutes(current.getMinutes() + intervalMinutes);\\n\\n    blocks.push({\\n      start: formatToEastern(current),\\n      end: formatToEastern(blockEnd)\\n    });\\n\\n    current = blockEnd;\\n  }\\n\\n  return blocks;\\n};\\n\\nlet allBlocks = [];\\nfor (const event of events) {\\n  if (event.start?.dateTime && event.end?.dateTime) {\\n    const blocks = splitEventIntoETBlocks(event);\\n    allBlocks = allBlocks.concat(blocks);\\n  }\\n}\\n\\nreturn allBlocks.map(block => ({ json: block }));\\n\"\n      },\n      \"type\": \"n8n-nodes-base.code\",\n      \"typeVersion\": 2,\n      \"position\": [\n        -280,\n        240\n      ],\n      \"id\": \"fb9063c2-de6b-4513-8901-d12625f5d772\",\n      \"name\": \"Split Events into 30 min blocks\"\n    },\n    {\n      \"parameters\": {\n        \"assignments\": {\n          \"assignments\": [\n            {\n              \"id\": \"f1270be8-1d11-4086-8bc0-ae53c99507c1\",\n              \"name\": \"start\",\n              \"value\": \"={{ $json.start }}\",\n              \"type\": \"string\"\n            },\n            {\n              \"id\": \"1a5f24ff-7d0c-436d-bb0b-015fc0c85cb7\",\n              \"name\": \"end\",\n              \"value\": \"={{ $json.end }}\",\n              \"type\": \"string\"\n            },\n            {\n              \"id\": \"befe6645-c0c1-40eb-9ba6-eccf2a762247\",\n              \"name\": \"Blocked\",\n              \"value\": \"Blocked\",\n              \"type\": \"string\"\n            }\n          ]\n        },\n        \"options\": {}\n      },\n      \"type\": \"n8n-nodes-base.set\",\n      \"typeVersion\": 3.4,\n      \"position\": [\n        -80,\n        240\n      ],\n      \"id\": \"23d8ed50-131f-49ea-9ce8-72a0067fe828\",\n      \"name\": \"Add Blocked Field\"\n    },\n    {\n      \"parameters\": {\n        \"jsCode\": \"const slots = [];\\nconst slotMinutes = 30;\\nconst timeZone = 'America/New_York';\\nconst businessStartHour = 9;\\nconst businessEndHour = 17;\\n\\n// Get offset like -04:00 or -05:00\\nfunction getEasternOffset(date) {\\n  const options = { timeZone, timeZoneName: 'short' };\\n  const parts = new Intl.DateTimeFormat('en-US', options).formatToParts(date);\\n  const tz = parts.find(p => p.type === 'timeZoneName')?.value || 'EST';\\n  return tz.includes('EDT') ? '-04:00' : '-05:00';\\n}\\n\\n// Format Date as ISO with Eastern offset\\nfunction formatToEasternISO(date) {\\n  const formatter = new Intl.DateTimeFormat('en-CA', {\\n    timeZone,\\n    year: 'numeric',\\n    month: '2-digit',\\n    day: '2-digit',\\n    hour: '2-digit',\\n    minute: '2-digit',\\n    second: '2-digit',\\n    hour12: false,\\n  });\\n\\n  const parts = formatter.formatToParts(date).reduce((acc, part) => {\\n    if (part.type !== 'literal') acc[part.type] = part.value;\\n    return acc;\\n  }, {});\\n\\n  const offset = getEasternOffset(date);\\n  return `${parts.year}-${parts.month}-${parts.day}T${parts.hour}:${parts.minute}:${parts.second}${offset}`;\\n}\\n\\n// Convert a Date to the hour/minute of its Eastern time\\nfunction getEasternTimeParts(date) {\\n  const formatter = new Intl.DateTimeFormat('en-US', {\\n    timeZone,\\n    hour: '2-digit',\\n    minute: '2-digit',\\n    hour12: false,\\n  });\\n  const [hourStr, minStr] = formatter.format(date).split(':');\\n  return { hour: parseInt(hourStr), minute: parseInt(minStr) };\\n}\\n\\nconst now = new Date();\\nconst endDate = new Date(now);\\nendDate.setDate(now.getDate() + 7);\\n\\n// Set current time to 24 hours in the future\\nconst current = new Date(now);\\ncurrent.setHours(current.getHours() + 24);\\n\\n// Round to the next 30-minute block in Eastern time\\nconst { minute } = getEasternTimeParts(current);\\nif (minute < 30) {\\n  current.setMinutes(30, 0, 0);\\n} else {\\n  current.setHours(current.getHours() + 1);\\n  current.setMinutes(0, 0, 0);\\n}\\n\\n// Generate 30-minute blocks only during business hours & weekdays\\nwhile (current < endDate) {\\n  const dayOfWeek = current.getDay(); // 0 = Sunday, 6 = Saturday\\n\\n  // Skip weekends\\n  if (dayOfWeek !== 0 && dayOfWeek !== 6) {\\n    const { hour } = getEasternTimeParts(current);\\n\\n    if (hour >= businessStartHour && hour < businessEndHour) {\\n      const start = new Date(current);\\n      const end = new Date(start);\\n      end.setMinutes(start.getMinutes() + slotMinutes);\\n\\n      slots.push({\\n        start: formatToEasternISO(start),\\n        end: formatToEasternISO(end),\\n      });\\n    }\\n  }\\n\\n  current.setMinutes(current.getMinutes() + slotMinutes);\\n}\\n\\nreturn slots.map(slot => ({ json: slot }));\\n\"\n      },\n      \"type\": \"n8n-nodes-base.code\",\n      \"typeVersion\": 2,\n      \"position\": [\n        -400,\n        460\n      ],\n      \"id\": \"01597a94-d94b-47e7-9488-adea3abb741c\",\n      \"name\": \"Generate 30 Minute Timeslots\"\n    },\n    {\n      \"parameters\": {\n        \"mode\": \"combine\",\n        \"fieldsToMatchString\": \"start, end\",\n        \"joinMode\": \"enrichInput2\",\n        \"options\": {}\n      },\n      \"type\": \"n8n-nodes-base.merge\",\n      \"typeVersion\": 3,\n      \"position\": [\n        180,\n        300\n      ],\n      \"id\": \"2d9f98a1-02ac-4332-a288-635a48ea3ee8\",\n      \"name\": \"Combine My Calendar with All Slots\"\n    },\n    {\n      \"parameters\": {\n        \"conditions\": {\n          \"options\": {\n            \"caseSensitive\": true,\n            \"leftValue\": \"\",\n            \"typeValidation\": \"strict\",\n            \"version\": 2\n          },\n          \"conditions\": [\n            {\n              \"id\": \"af65c6c8-31c7-4f27-a073-cf7f72079882\",\n              \"leftValue\": \"={{ $json.Blocked }}\",\n              \"rightValue\": \"Blocked\",\n              \"operator\": {\n                \"type\": \"string\",\n                \"operation\": \"notEquals\"\n              }\n            }\n          ],\n          \"combinator\": \"and\"\n        },\n        \"options\": {}\n      },\n      \"type\": \"n8n-nodes-base.if\",\n      \"typeVersion\": 2.2,\n      \"position\": [\n        420,\n        280\n      ],\n      \"id\": \"0438b5be-b3c4-4645-9604-303ace7bfead\",\n      \"name\": \"Check if Calendar Blocked\"\n    },\n    {\n      \"parameters\": {\n        \"jsCode\": \"const formatted = items.map(item => {\\n  const start = item.json.start;\\n  const end = item.json.end;\\n  return `${start} - ${end}`;\\n});\\n\\nconst combined = formatted.join(', ');\\n\\nreturn [\\n  {\\n    json: {\\n      availableSlots: combined\\n    }\\n  }\\n];\\n\"\n      },\n      \"type\": \"n8n-nodes-base.code\",\n      \"typeVersion\": 2,\n      \"position\": [\n        660,\n        300\n      ],\n      \"id\": \"4a6bfde4-7d9f-4837-bc6c-66bf968e782a\",\n      \"name\": \"Return string of all available times\"\n    },\n    {\n      \"parameters\": {\n        \"inputSource\": \"passthrough\"\n      },\n      \"type\": \"n8n-nodes-base.executeWorkflowTrigger\",\n      \"typeVersion\": 1.1,\n      \"position\": [\n        -760,\n        340\n      ],\n      \"id\": \"8bde95cb-7239-4b7d-aca1-0adacf2ea257\",\n      \"name\": \"Get Availability\"\n    }\n  ],\n  \"connections\": {\n    \"Check My Calendar\": {\n      \"main\": [\n        [\n          {\n            \"node\": \"Split Events into 30 min blocks\",\n            \"type\": \"main\",\n            \"index\": 0\n          }\n        ]\n      ]\n    },\n    \"Split Events into 30 min blocks\": {\n      \"main\": [\n        [\n          {\n            \"node\": \"Add Blocked Field\",\n            \"type\": \"main\",\n            \"index\": 0\n          }\n        ]\n      ]\n    },\n    \"Add Blocked Field\": {\n      \"main\": [\n        [\n          {\n            \"node\": \"Combine My Calendar with All Slots\",\n            \"type\": \"main\",\n            \"index\": 0\n          }\n        ]\n      ]\n    },\n    \"Generate 30 Minute Timeslots\": {\n      \"main\": [\n        [\n          {\n            \"node\": \"Combine My Calendar with All Slots\",\n            \"type\": \"main\",\n            \"index\": 1\n          }\n        ]\n      ]\n    },\n    \"Combine My Calendar with All Slots\": {\n      \"main\": [\n        [\n          {\n            \"node\": \"Check if Calendar Blocked\",\n            \"type\": \"main\",\n            \"index\": 0\n          }\n        ]\n      ]\n    },\n    \"Check if Calendar Blocked\": {\n      \"main\": [\n        [\n          {\n            \"node\": \"Return string of all available times\",\n            \"type\": \"main\",\n            \"index\": 0\n          }\n        ]\n      ]\n    },\n    \"Get Availability\": {\n      \"main\": [\n        [\n          {\n            \"node\": \"Check My Calendar\",\n            \"type\": \"main\",\n            \"index\": 0\n          },\n          {\n            \"node\": \"Generate 30 Minute Timeslots\",\n            \"type\": \"main\",\n            \"index\": 0\n          }\n        ]\n      ]\n    }\n  },\n  \"pinData\": {},\n  \"meta\": {\n    \"instanceId\": \"efb474b59b0341d7791932605bd9ff04a6c7ed9941fdd53dc4a2e4b99a6f9439\"\n  }\n}"
      },
      "typeVersion": 2.1
    },
    {
      "id": "8892f883-aaae-4616-bb50-bbe0f9dacb23",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1440,
        1660
      ],
      "parameters": {
        "color": 3,
        "width": 520,
        "height": 480,
        "content": "Check Day Names Tool\n\n\n1. This part of the flow is just a copy of what is embedded in the \"Check Day Names Tool\". It does not run. \n\n2. If you update this part of the flow, copy it with ctrl-c and paste it into another workbook. Add a sub-workflow execution. Set the workflow to accept all data. Copy the flow. Paste the Workflow JSON field in the \"Check Day Names Tool\" tool node\n"
      },
      "typeVersion": 1
    },
    {
      "id": "234b89da-9003-43d5-842a-4ecf92522b51",
      "name": "check day names",
      "type": "@n8n/n8n-nodes-langchain.toolWorkflow",
      "position": [
        880,
        1480
      ],
      "parameters": {
        "name": "check_days",
        "source": "parameter",
        "workflowJson": "{\n  \"nodes\": [\n    {\n      \"parameters\": {\n        \"inputSource\": \"passthrough\"\n      },\n      \"type\": \"n8n-nodes-base.executeWorkflowTrigger\",\n      \"typeVersion\": 1.1,\n      \"position\": [\n        -400,\n        -120\n      ],\n      \"id\": \"dec37e15-3695-4911-91a6-1f97018ab982\",\n      \"name\": \"When Executed by Another Workflow\"\n    },\n    {\n      \"parameters\": {\n        \"jsCode\": \"function getWeekdaysNextTwoWeeks() {\\n  const items = [];\\n  const longDayNames = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];\\n\\n  const today = new Date();\\n  const endDate = new Date();\\n  endDate.setDate(today.getDate() + 14); // 2 weeks ahead\\n\\n  const current = new Date(today);\\n\\n  while (current <= endDate) {\\n    const dayOfWeek = current.getDay(); // 0 = Sunday, 6 = Saturday\\n\\n    // Only weekdays (Mon–Fri)\\n    if (dayOfWeek >= 1 && dayOfWeek <= 5) {\\n      const dateStr = current.toISOString().split('T')[0]; // YYYY-MM-DD\\n      const output = `${longDayNames[dayOfWeek]} - ${dateStr}`;\\n\\n      items.push({\\n        json: {\\n          day: output\\n        }\\n      });\\n    }\\n\\n    current.setDate(current.getDate() + 1); // Go to next day\\n  }\\n\\n  return items;\\n}\\n\\n// Example usage:\\nreturn getWeekdaysNextTwoWeeks();\\n\"\n      },\n      \"type\": \"n8n-nodes-base.code\",\n      \"typeVersion\": 2,\n      \"position\": [\n        -180,\n        -120\n      ],\n      \"id\": \"cbbe4248-d1cc-48e3-9ea8-67a844f3de29\",\n      \"name\": \"Check Day Names\"\n    }\n  ],\n  \"connections\": {\n    \"When Executed by Another Workflow\": {\n      \"main\": [\n        [\n          {\n            \"node\": \"Check Day Names\",\n            \"type\": \"main\",\n            \"index\": 0\n          }\n        ]\n      ]\n    }\n  },\n  \"pinData\": {},\n  \"meta\": {\n    \"instanceId\": \"efb474b59b0341d7791932605bd9ff04a6c7ed9941fdd53dc4a2e4b99a6f9439\"\n  }\n}"
      },
      "typeVersion": 2.1
    },
    {
      "id": "c052c7e4-1587-4c7e-9a8e-043c8571338d",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        180,
        1660
      ],
      "parameters": {
        "width": 1200,
        "height": 500,
        "content": "Get Availability Execution. \n\n1. This part of the flow is just a copy of what is embedded in the \"Run Get Availability Tool\". It does not run. \n\n2. If you update this part of the flow, copy it with ctrl-c and paste it into another workbook. Add a sub-workflow execution. Set the workflow to accept all data. Copy the flow. Paste the Workflow JSON field in the \"Run Get Availability\" tool node"
      },
      "typeVersion": 1
    },
    {
      "id": "b7c71153-fbd1-45ac-8dbf-d4beb241daaf",
      "name": "Convert Output to JSON",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        1240,
        1260
      ],
      "parameters": {
        "text": "={{ $json.output }}",
        "options": {
          "systemMessage": "=take in this message and output json"
        },
        "promptType": "define",
        "hasOutputParser": true
      },
      "typeVersion": 1.7
    },
    {
      "id": "1f902158-5885-46d6-8d7e-26ccf116ed0a",
      "name": "Interview Scheduler",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        520,
        1220
      ],
      "parameters": {
        "text": "={{ $json.chatInput }}",
        "options": {
          "systemMessage": "=You are a friendly AI chatbot helping users schedule meetings. Ask for Phone, email, preferred date, and time. Confirm details before booking. Time zone: Eastern.\n\nToday's date is {{ $now }}\n\n1. Use the get_availability tool to find when I am available. it will return comma separated timeslots the interviewer can meet. check the proposed time against the results. Times are in 24 hour clock times in this format.  2025-03-31T09:00:00-04:00\n3. If I am not available, look at get_availability tool again and propose a similar time where I am available\n2. use the check_days tool if the user mentions something like next tuesday so you know what date they are talking about\n3. Once a time is aggreed upon, output json in this format \n2025-03-28T13:00:00-04:00. \n4. once you have the email, phone start and end time, output only the json and nothing else\n\n{\n  \"interview\": {\n    \"email\": \"applicant@example.com\",\n    \"phone\": \"814-882-1293\",\n    \"start_datetime\": \"2025-03-28T10:00:00\",\n    \"end_datetime\": \"2025-03-28T11:00:00\"\n  }\n}\n\n## Rules\n- If the calendar is not available at the time requested, do not double book. Send a new time.\n- Interviews are all 30 minutes long\n- Do not book over another meeting\n- do not give details about what is on the interviewers calendar\n- do not converse with the user about anything else",
          "returnIntermediateSteps": true
        },
        "promptType": "define"
      },
      "typeVersion": 1.7
    },
    {
      "id": "ba0fb82e-a280-4392-833e-04f00a47170c",
      "name": "If Final Output",
      "type": "n8n-nodes-base.if",
      "position": [
        960,
        1160
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
              "id": "e75b6a50-680f-4f5b-8dd3-fc93be1bc7f1",
              "operator": {
                "type": "string",
                "operation": "contains"
              },
              "leftValue": "={{ $json.output }}",
              "rightValue": "start_datetime"
            },
            {
              "id": "cadd4bff-8d53-446c-8ad0-14b3fb9ab335",
              "operator": {
                "type": "string",
                "operation": "contains"
              },
              "leftValue": "={{ $json.output }}",
              "rightValue": "end_datetime"
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "c56bcba9-ac39-474b-a186-ceb67fa4008d",
      "name": "Respond for More Info",
      "type": "n8n-nodes-base.noOp",
      "position": [
        1040,
        1400
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "efd03308-0da1-4797-b899-3d4446eba722",
      "name": "Parse to JSON",
      "type": "@n8n/n8n-nodes-langchain.outputParserStructured",
      "position": [
        1400,
        1500
      ],
      "parameters": {
        "jsonSchemaExample": "{\n  \"interview\": {\n    \"email\": \"applicant@example.com\",\n    \"phone\": \"814-882-1293\",\n    \"start_datetime\": \"2025-03-28T10:00:00\",\n    \"end_datetime\": \"2025-03-28T11:00:00\"\n  }\n}"
      },
      "typeVersion": 1.2
    },
    {
      "id": "11abd142-d509-4459-bdf5-861dcf4263bf",
      "name": "Set Meeting with Google",
      "type": "n8n-nodes-base.googleCalendar",
      "position": [
        1640,
        1280
      ],
      "parameters": {
        "end": "={{ $json.output.interview.end_datetime }}",
        "start": "={{ $json.output.interview.start_datetime }}",
        "calendar": {
          "__rl": true,
          "mode": "list",
          "value": "rbreen.ynteractive@gmail.com",
          "cachedResultName": "rbreen.ynteractive@gmail.com"
        },
        "additionalFields": {
          "summary": "Interview",
          "attendees": [
            "={{ $json.output.interview.email }}"
          ],
          "description": "=I will call you at  {{ $json.output.interview.phone }}"
        }
      },
      "credentials": {
        "googleCalendarOAuth2Api": {
          "id": "nc5M45R7LyFadByw",
          "name": "Google Calendar account"
        }
      },
      "typeVersion": 1.3
    },
    {
      "id": "fef5ba53-4386-4e88-9f28-8a9b5d9c928f",
      "name": "Final Response to User",
      "type": "n8n-nodes-base.code",
      "position": [
        1640,
        1500
      ],
      "parameters": {
        "jsCode": "const email = $('Convert Output to JSON').first().json.output.interview.email;\nconst phone = $('Convert Output to JSON').first().json.output.interview.phone;\nconst start_datetime = $('Convert Output to JSON').first().json.output.interview.start_datetime;\nconst end_datetime = $('Convert Output to JSON').first().json.output.interview.end_datetime;\n\nlet text = `✅ Interview Confirmed!\\n\\n📧 Email: ${email}\\n📞 Phone: ${phone}\\n🕒 Start: ${start_datetime}\\n🕕 End: ${end_datetime}`;\n\nreturn { text };\n"
      },
      "typeVersion": 2
    },
    {
      "id": "a06664e2-d5d2-40a7-98a5-a3de2d775b7c",
      "name": "Generate Interview Times",
      "type": "n8n-nodes-base.code",
      "position": [
        1620,
        1920
      ],
      "parameters": {
        "jsCode": "function getWeekdaysNextTwoWeeks() {\n  const items = [];\n  const longDayNames = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];\n\n  const today = new Date();\n  const endDate = new Date();\n  endDate.setDate(today.getDate() + 14); // 2 weeks ahead\n\n  const current = new Date(today);\n\n  while (current <= endDate) {\n    const dayOfWeek = current.getDay(); // 0 = Sunday, 6 = Saturday\n\n    // Only weekdays (Mon–Fri)\n    if (dayOfWeek >= 1 && dayOfWeek <= 5) {\n      const dateStr = current.toISOString().split('T')[0]; // YYYY-MM-DD\n      const output = `${longDayNames[dayOfWeek]} - ${dateStr}`;\n\n      items.push({\n        json: {\n          day: output\n        }\n      });\n    }\n\n    current.setDate(current.getDate() + 1); // Go to next day\n  }\n\n  return items;\n}\n\n// Example usage:\nreturn getWeekdaysNextTwoWeeks();\n"
      },
      "typeVersion": 2
    },
    {
      "id": "f35d595e-6834-4898-bbcb-b17599d769b4",
      "name": "Check My Calendar",
      "type": "n8n-nodes-base.googleCalendar",
      "position": [
        420,
        1820
      ],
      "parameters": {
        "options": {
          "fields": ""
        },
        "calendar": {
          "__rl": true,
          "mode": "list",
          "value": "rbreen.ynteractive@gmail.com",
          "cachedResultName": "rbreen.ynteractive@gmail.com"
        },
        "operation": "getAll",
        "returnAll": true
      },
      "credentials": {
        "googleCalendarOAuth2Api": {
          "id": "nc5M45R7LyFadByw",
          "name": "Google Calendar account"
        }
      },
      "typeVersion": 1.3
    },
    {
      "id": "29e3a097-b6f1-4a54-b943-d9ad9177b03b",
      "name": "Split Events into 30 min blocks",
      "type": "n8n-nodes-base.code",
      "position": [
        620,
        1820
      ],
      "parameters": {
        "jsCode": "const events = items.map(item => item.json);\nconst intervalMinutes = 30;\nconst timeZone = 'America/New_York';\n\nfunction formatToEastern(date) {\n  const tzDate = new Intl.DateTimeFormat('en-US', {\n    timeZone,\n    year: 'numeric',\n    month: '2-digit',\n    day: '2-digit',\n    hour: '2-digit',\n    minute: '2-digit',\n    second: '2-digit',\n    hour12: false\n  }).formatToParts(date).reduce((acc, part) => {\n    if (part.type !== 'literal') acc[part.type] = part.value;\n    return acc;\n  }, {});\n\n  const offset = getEasternOffset(date);\n  return `${tzDate.year}-${tzDate.month}-${tzDate.day}T${tzDate.hour}:${tzDate.minute}:${tzDate.second}${offset}`;\n}\n\nfunction getEasternOffset(date) {\n  const options = { timeZone, timeZoneName: 'short' };\n  const parts = new Intl.DateTimeFormat('en-US', options).formatToParts(date);\n  const tzName = parts.find(p => p.type === 'timeZoneName').value;\n  return tzName.includes('EDT') ? '-04:00' : '-05:00';\n}\n\nfunction alignToPreviousSlot(date) {\n  const aligned = new Date(date);\n  const minutes = aligned.getMinutes();\n  aligned.setMinutes(minutes < 30 ? 0 : 30, 0, 0);\n  return aligned;\n}\n\nfunction alignToNextSlot(date) {\n  const aligned = new Date(date);\n  const minutes = aligned.getMinutes();\n  if (minutes > 0 && minutes <= 30) {\n    aligned.setMinutes(30, 0, 0);\n  } else if (minutes > 30) {\n    aligned.setHours(aligned.getHours() + 1);\n    aligned.setMinutes(0, 0, 0);\n  } else {\n    aligned.setMinutes(0, 0, 0);\n  }\n  return aligned;\n}\n\nconst splitEventIntoETBlocks = (event) => {\n  const blocks = [];\n\n  let current = alignToPreviousSlot(new Date(event.start.dateTime));\n  const eventEnd = alignToNextSlot(new Date(event.end.dateTime));\n\n  while (current < eventEnd) {\n    const blockEnd = new Date(current);\n    blockEnd.setMinutes(current.getMinutes() + intervalMinutes);\n\n    blocks.push({\n      start: formatToEastern(current),\n      end: formatToEastern(blockEnd)\n    });\n\n    current = blockEnd;\n  }\n\n  return blocks;\n};\n\nlet allBlocks = [];\nfor (const event of events) {\n  if (event.start?.dateTime && event.end?.dateTime) {\n    const blocks = splitEventIntoETBlocks(event);\n    allBlocks = allBlocks.concat(blocks);\n  }\n}\n\nreturn allBlocks.map(block => ({ json: block }));\n"
      },
      "typeVersion": 2
    },
    {
      "id": "f9297e8a-75dd-4f12-b0e1-d3fa372a7631",
      "name": "Add Blocked Field",
      "type": "n8n-nodes-base.set",
      "position": [
        800,
        1840
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "f1270be8-1d11-4086-8bc0-ae53c99507c1",
              "name": "start",
              "type": "string",
              "value": "={{ $json.start }}"
            },
            {
              "id": "1a5f24ff-7d0c-436d-bb0b-015fc0c85cb7",
              "name": "end",
              "type": "string",
              "value": "={{ $json.end }}"
            },
            {
              "id": "befe6645-c0c1-40eb-9ba6-eccf2a762247",
              "name": "Blocked",
              "type": "string",
              "value": "Blocked"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "8ba70f94-e9e6-44aa-b0e7-9a5294634e0e",
      "name": "Generate 30 Minute Timeslots",
      "type": "n8n-nodes-base.code",
      "position": [
        440,
        2020
      ],
      "parameters": {
        "jsCode": "const slots = [];\nconst slotMinutes = 30;\nconst timeZone = 'America/New_York';\nconst businessStartHour = 9;\nconst businessEndHour = 17;\n\n// Get offset like -04:00 or -05:00\nfunction getEasternOffset(date) {\n  const options = { timeZone, timeZoneName: 'short' };\n  const parts = new Intl.DateTimeFormat('en-US', options).formatToParts(date);\n  const tz = parts.find(p => p.type === 'timeZoneName')?.value || 'EST';\n  return tz.includes('EDT') ? '-04:00' : '-05:00';\n}\n\n// Format Date as ISO with Eastern offset\nfunction formatToEasternISO(date) {\n  const formatter = new Intl.DateTimeFormat('en-CA', {\n    timeZone,\n    year: 'numeric',\n    month: '2-digit',\n    day: '2-digit',\n    hour: '2-digit',\n    minute: '2-digit',\n    second: '2-digit',\n    hour12: false,\n  });\n\n  const parts = formatter.formatToParts(date).reduce((acc, part) => {\n    if (part.type !== 'literal') acc[part.type] = part.value;\n    return acc;\n  }, {});\n\n  const offset = getEasternOffset(date);\n  return `${parts.year}-${parts.month}-${parts.day}T${parts.hour}:${parts.minute}:${parts.second}${offset}`;\n}\n\n// Convert a Date to the hour/minute of its Eastern time\nfunction getEasternTimeParts(date) {\n  const formatter = new Intl.DateTimeFormat('en-US', {\n    timeZone,\n    hour: '2-digit',\n    minute: '2-digit',\n    hour12: false,\n  });\n  const [hourStr, minStr] = formatter.format(date).split(':');\n  return { hour: parseInt(hourStr), minute: parseInt(minStr) };\n}\n\nconst now = new Date();\nconst endDate = new Date(now);\nendDate.setDate(now.getDate() + 7);\n\n// Set current time to 24 hours in the future\nconst current = new Date(now);\ncurrent.setHours(current.getHours() + 24);\n\n// Round to the next 30-minute block in Eastern time\nconst { minute } = getEasternTimeParts(current);\nif (minute < 30) {\n  current.setMinutes(30, 0, 0);\n} else {\n  current.setHours(current.getHours() + 1);\n  current.setMinutes(0, 0, 0);\n}\n\n// Generate 30-minute blocks only during business hours & weekdays\nwhile (current < endDate) {\n  const dayOfWeek = current.getDay(); // 0 = Sunday, 6 = Saturday\n\n  // Skip weekends\n  if (dayOfWeek !== 0 && dayOfWeek !== 6) {\n    const { hour } = getEasternTimeParts(current);\n\n    if (hour >= businessStartHour && hour < businessEndHour) {\n      const start = new Date(current);\n      const end = new Date(start);\n      end.setMinutes(start.getMinutes() + slotMinutes);\n\n      slots.push({\n        start: formatToEasternISO(start),\n        end: formatToEasternISO(end),\n      });\n    }\n  }\n\n  current.setMinutes(current.getMinutes() + slotMinutes);\n}\n\nreturn slots.map(slot => ({ json: slot }));\n"
      },
      "typeVersion": 2
    },
    {
      "id": "3ea13a0a-d496-40b8-9321-6bc3df415191",
      "name": "Combine My Calendar with All Slots",
      "type": "n8n-nodes-base.merge",
      "position": [
        780,
        2020
      ],
      "parameters": {
        "mode": "combine",
        "options": {},
        "joinMode": "enrichInput2",
        "fieldsToMatchString": "start, end"
      },
      "typeVersion": 3
    },
    {
      "id": "ad57e0b4-43d0-4991-adc3-e325e2405e93",
      "name": "Check if Calendar Blocked",
      "type": "n8n-nodes-base.if",
      "position": [
        1100,
        1820
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
              "id": "af65c6c8-31c7-4f27-a073-cf7f72079882",
              "operator": {
                "type": "string",
                "operation": "notEquals"
              },
              "leftValue": "={{ $json.Blocked }}",
              "rightValue": "Blocked"
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "6e427266-1f64-4492-b4c0-30d03d6a20de",
      "name": "Return string of all available times",
      "type": "n8n-nodes-base.code",
      "position": [
        1160,
        2000
      ],
      "parameters": {
        "jsCode": "const formatted = items.map(item => {\n  const start = item.json.start;\n  const end = item.json.end;\n  return `${start} - ${end}`;\n});\n\nconst combined = formatted.join(', ');\n\nreturn [\n  {\n    json: {\n      availableSlots: combined\n    }\n  }\n];\n"
      },
      "typeVersion": 2
    },
    {
      "id": "3f26c921-2d4c-4e8a-a551-801c2a94086a",
      "name": "Get Availability",
      "type": "n8n-nodes-base.executeWorkflowTrigger",
      "position": [
        220,
        1920
      ],
      "parameters": {
        "inputSource": "passthrough"
      },
      "typeVersion": 1.1
    },
    {
      "id": "6d34f9e2-4c43-4e0b-a54d-2c8076ee6fe0",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -420,
        1160
      ],
      "parameters": {
        "color": 5,
        "width": 520,
        "height": 1000,
        "content": "How to Use the Interview Scheduler Workflow in n8n\n________________________________________\n✨ Overview\nThis workflow allows candidates to schedule interviews by chatting with an AI assistant. It checks your Google Calendar availability, identifies free 30-minute weekday slots between 9am-5pm EST, and automatically books a meeting once details are confirmed.\n________________________________________\n⚡ Prerequisites\n1.\tOpenAI Account\no\tAPI Key with GPT-4o model access\n2.\tGoogle Account with Calendar Access\no\tYour calendar must be accessible via Google Calendar\n3.\tOAuth2 Credentials for Google Calendar API configured in n8n\n4.\tOpenAI Credentials configured in n8n\n________________________________________\n🔐 API Credentials Setup\nGoogle Calendar OAuth2:\n•\tCreate a project called n8n in google cloud console\n•\tGo to n8n > Credentials\n•\tCreate new Google Calendar OAuth2 API credentials\n•\tAuthorize your Google account (e.g., yourname@gmail.com)\nOpenAI:\n•\tGo to Credentials\n•\tCreate new OpenAI API credentials\n•\tEnter your OpenAI API key and give it a label (e.g., \"My OpenAI Key\")\n________________________________________\n🔧 How to Make It Yours\n✅ Update These Workflow Fields:\n1.\tGoogle Calendar Email\no\tReplace all instances of rbreen.ynteractive@gmail.com with your own Google Calendar email.\no\tThis appears in:\n\tGoogle Calendar Nodes\n\tToolWorkflow JSON for \"Run Get Availability\"\n2.\tGoogle Calendar OAuth2 Credential Name\no\tReplace credential name Google Calendar account with your own credential name.\n3.\tOpenAI Credential Name\no\tReplace OpenAi account with your own OpenAI credential name.\n4.\tWebhook URL / Chat Interface\no\tGo to the Candidate Chat node\no\tCopy the webhook URL\no\tShare this public link with users to start the chatbot\n5.\tSystem Message Instructions (Optional)\no\tYou can tweak the system message in the Interview Scheduler agent node to change tone, questions, or rules.\n6.\tCustom Branding (Optional)\no\tUpdate the title and subtitle in the Candidate Chat node under options\no\tYou can also replace the final message in Final Response to User with your own branding/tone\n________________________________________\n\n\n"
      },
      "typeVersion": 1
    },
    {
      "id": "07ef21ee-c02a-4145-a0fb-3ecc260ff585",
      "name": "When chat message received",
      "type": "@n8n/n8n-nodes-langchain.chatTrigger",
      "position": [
        280,
        1220
      ],
      "webhookId": "0c8f9f17-f5f3-4b5d-85e7-071ced0213ae",
      "parameters": {
        "public": true,
        "options": {}
      },
      "typeVersion": 1.1
    }
  ],
  "active": true,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "69e8aa1b-e404-44ed-aedc-7d8480e2383e",
  "connections": {
    "Parse to JSON": {
      "ai_outputParser": [
        [
          {
            "node": "Convert Output to JSON",
            "type": "ai_outputParser",
            "index": 0
          }
        ]
      ]
    },
    "If Final Output": {
      "main": [
        [
          {
            "node": "Convert Output to JSON",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Respond for More Info",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "check day names": {
      "ai_tool": [
        [
          {
            "node": "Interview Scheduler",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Get Availability": {
      "main": [
        [
          {
            "node": "Check My Calendar",
            "type": "main",
            "index": 0
          },
          {
            "node": "Generate 30 Minute Timeslots",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Add Blocked Field": {
      "main": [
        [
          {
            "node": "Combine My Calendar with All Slots",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Check My Calendar": {
      "main": [
        [
          {
            "node": "Split Events into 30 min blocks",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Chat Model2": {
      "ai_languageModel": [
        [
          {
            "node": "Interview Scheduler",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Chat Model4": {
      "ai_languageModel": [
        [
          {
            "node": "Convert Output to JSON",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Interview Scheduler": {
      "main": [
        [
          {
            "node": "If Final Output",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Run Get Availability": {
      "ai_tool": [
        [
          {
            "node": "Interview Scheduler",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Respond for More Info": {
      "main": [
        []
      ]
    },
    "Window Buffer Memory2": {
      "ai_memory": [
        [
          {
            "node": "Interview Scheduler",
            "type": "ai_memory",
            "index": 0
          }
        ]
      ]
    },
    "Convert Output to JSON": {
      "main": [
        [
          {
            "node": "Set Meeting with Google",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Final Response to User": {
      "main": [
        []
      ]
    },
    "Set Meeting with Google": {
      "main": [
        [
          {
            "node": "Final Response to User",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Check if Calendar Blocked": {
      "main": [
        [
          {
            "node": "Return string of all available times",
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
            "node": "Interview Scheduler",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Generate 30 Minute Timeslots": {
      "main": [
        [
          {
            "node": "Combine My Calendar with All Slots",
            "type": "main",
            "index": 1
          }
        ]
      ]
    },
    "Split Events into 30 min blocks": {
      "main": [
        [
          {
            "node": "Add Blocked Field",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Combine My Calendar with All Slots": {
      "main": [
        [
          {
            "node": "Check if Calendar Blocked",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-1042"></a>

## Template 1042 - Resumo de emails e envio para Messenger

- **Nome:** Resumo de emails e envio para Messenger
- **Descrição:** Lê emails de uma conta IMAP, envia o conteúdo para um serviço de A.I. que gera resumos seguindo regras específicas e envia o resultado para um destinatário no Messenger (LINE).
- **Funcionalidade:** • Leitura de emails via IMAP: Conecta-se ao servidor de email e busca mensagens para processamento.
• Envio do conteúdo para A.I.: Transmite o remetente, assunto e corpo do email a um modelo de linguagem para gerar um resumo.
• Regras de formatação do resumo: Solicita destaque de prazos (em negrito), identificação de itens de ação e marcação de urgência com emoji; resumos curtos para emails não importantes.
• Encaminhamento do resumo para Messenger: Envia o texto gerado pelo A.I. para um usuário/ID usando a API de mensagens.
• Uso de autenticação por cabeçalho: Utiliza tokens no cabeçalho HTTP para autenticar requisições aos serviços externos.
- **Ferramentas:** • Servidor de email (IMAP): Fornece acesso às mensagens para leitura e extração de conteúdo.
• OpenRouter.ai (modelo meta-llama/llama-3.1-70b-instruct:free): Serviço de A.I. usado para interpretar o conteúdo do email e gerar resumos conforme o prompt fornecido.
• LINE Messaging API: Endpoint para enviar mensagens push ao destinatário usando um token de canal (Bearer token).

## Fluxo visual

```mermaid
flowchart LR
    N1["Read emails (IMAP)"]
    N2["Send email to A.I. to summarize"]
    N3["Send summarized content to messenger"]
    N4["Sticky Note"]
    N5["Sticky Note1"]
    N6["Sticky Note2"]
    N7["Sticky Note3"]

    N1 --> N2
    N2 --> N3
```

## Fluxo (.json) :

```json
{
  "id": "QnVdtKiTf3nbrNkh",
  "meta": {
    "instanceId": "558d88703fb65b2d0e44613bc35916258b0f0bf983c5d4730c00c424b77ca36a",
    "templateCredsSetupCompleted": true
  },
  "name": "Summarize emails with A.I. then send to messenger",
  "tags": [],
  "nodes": [
    {
      "id": "50e12e63-df28-45ac-9208-48cbf5116d09",
      "name": "Read emails (IMAP)",
      "type": "n8n-nodes-base.emailReadImap",
      "position": [
        340,
        260
      ],
      "parameters": {
        "options": {},
        "postProcessAction": "nothing"
      },
      "credentials": {
        "imap": {
          "id": "gXtdakU9M02LBQc3",
          "name": "IMAP account"
        }
      },
      "typeVersion": 2
    },
    {
      "id": "6565350b-2269-44e3-8f36-8797f32d3e09",
      "name": "Send email to A.I. to summarize",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        700,
        260
      ],
      "parameters": {
        "url": "https://openrouter.ai/api/v1/chat/completions",
        "method": "POST",
        "options": {},
        "jsonBody": "={\n \"model\": \"meta-llama/llama-3.1-70b-instruct:free\",\n \"messages\": [\n {\n \"role\": \"user\",\n \"content\": \"I want you to read and summarize all the emails. If it's not rimportant, just give me a short summary with less than 10 words.\\n\\nHighlight as important if it is, add an emoji to indicate it is urgent:\\nFor the relevant content, find any action items and deadlines. Sometimes I need to sign up before a certain date or pay before a certain date, please highlight that in the summary for me.\\n\\nPut the deadline in BOLD at the top. If the email is not important, keep the summary short to 1 sentence only.\\n\\nHere's the email content for you to read:\\nSender email address: {{ encodeURIComponent($json.from) }}\\nSubject: {{ encodeURIComponent($json.subject) }}\\n{{ encodeURIComponent($json.textHtml) }}\"\n }\n ]\n}",
        "sendBody": true,
        "specifyBody": "json",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth"
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "WY7UkF14ksPKq3S8",
          "name": "Header Auth account 2"
        }
      },
      "typeVersion": 4.2,
      "alwaysOutputData": false
    },
    {
      "id": "d04c422a-c000-4e48-82d0-0bf44bcd9fff",
      "name": "Send summarized content to messenger",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1100,
        260
      ],
      "parameters": {
        "url": "https://api.line.me/v2/bot/message/push",
        "method": "POST",
        "options": {},
        "jsonBody": "={\n \"to\": \"U3ec262c49811f30cdc2d2f2b0a0df99a\",\n \"messages\": [\n {\n \"type\": \"text\",\n \"text\": \"{{ $json.choices[0].message.content.replace(/\\n/g, \"\\\\n\") }}\"\n }\n ]\n}\n\n\n ",
        "sendBody": true,
        "specifyBody": "json",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth"
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "SzcKjO9Nn9vZPL2H",
          "name": "Header Auth account 5"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "57a1219c-4f40-407c-855b-86c4c7c468bb",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        180,
        0
      ],
      "parameters": {
        "width": 361,
        "height": 90,
        "content": "## Summarize emails with A.I.\nYou can find out more about the [use case](https://rumjahn.com/how-a-i-saved-my-kids-school-life-and-my-marriage/)"
      },
      "typeVersion": 1
    },
    {
      "id": "17686264-56ac-419e-a32b-dc5c75f15f1f",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        283,
        141
      ],
      "parameters": {
        "color": 5,
        "width": 229,
        "height": 280,
        "content": "Find your email server's IMAP Settings. \n- Link for [gmail](https://www.getmailspring.com/setup/access-gmail-via-imap-smtp)"
      },
      "typeVersion": 1
    },
    {
      "id": "1862abd6-7dca-4c66-90d6-110d4fcf4d99",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        580,
        0
      ],
      "parameters": {
        "color": 6,
        "width": 365,
        "height": 442,
        "content": "For the A.I. you can use Openrouter.ai. \n- Set up a free account\n- The A.I. model selected is FREE to use.\n## Credentials\n- Use header auth\n- Username: Authorization\n- Password: Bearer {insert your API key}.\n- The password is \"Bearer\" space plus your API key."
      },
      "typeVersion": 1
    },
    {
      "id": "c4a3a76f-539d-4bbf-8f95-d7aaebf39a55",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1000,
        0
      ],
      "parameters": {
        "color": 4,
        "width": 307,
        "height": 439,
        "content": "Don't use the official Line node. It's outdated.\n## Credentials\n- Use header auth\n- Username: Authorization\n- Password: Bearer {channel access token}\n\nYou can find your channel access token at the [Line API console](https://developers.line.biz/console/). Go to Messaging API and scroll to the bottom."
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "81216e6a-2bd8-4215-8a96-376ee520469d",
  "connections": {
    "Read emails (IMAP)": {
      "main": [
        [
          {
            "node": "Send email to A.I. to summarize",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Send email to A.I. to summarize": {
      "main": [
        [
          {
            "node": "Send summarized content to messenger",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-1043"></a>

## Template 1043 - Monitorar lançamentos relevantes no Product Hunt

- **Nome:** Monitorar lançamentos relevantes no Product Hunt
- **Descrição:** Monitora diariamente lançamentos no Product Hunt sobre um tema definido e envia os resultados para um canal do Slack.
- **Funcionalidade:** • Definição do tema relevante: Define o assunto a ser monitorado (ex.: "AI Agents").
• Consulta e extração de lançamentos: Acessa o Product Hunt e extrai até 5 lançamentos relevantes, retornando título e URL.
• Trigger diário: Executa automaticamente o processo todos os dias às 06:00.
• Validação de resultados: Verifica se foram encontrados produtos e trata o caso em que não há resultados (retorno [NA]).
• Notificação no Slack: Envia a resposta formatada para um canal Slack específico.
- **Ferramentas:** • Product Hunt: Fonte de lançamentos de produtos usada para buscar novos projetos relevantes.
• Airtop: Serviço de extração/consulta que acessa páginas e retorna informações estruturadas com base em um prompt.
• Slack: Plataforma de comunicação usada para entregar as notificações com os resultados.

## Fluxo visual

```mermaid
flowchart LR
    N1["Define relevant products"]
    N2["Found products?"]
    N3["Look up products"]
    N4["Send slack message"]
    N5["Trigger daily"]

    N5 --> N1
    N2 --> N4
    N3 --> N2
    N1 --> N3
```

## Fluxo (.json) :

```json
{
  "id": "fvYgcG9s1pqP5cQ6",
  "meta": {
    "instanceId": "660cf2c29eb19fa42319afac3bd2a4a74c6354b7c006403f6cba388968b63f5d",
    "templateCredsSetupCompleted": true
  },
  "name": "Monitor ProductHunt",
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
      "id": "3cf0b7e0-ec9f-4173-bc85-1b4daef5aa22",
      "name": "Define relevant products",
      "type": "n8n-nodes-base.set",
      "position": [
        220,
        -100
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "a83156e0-1782-4d0a-a15c-1ff889ff915d",
              "name": "Relevant Products",
              "type": "string",
              "value": "AI Agents"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "a316f080-0fd8-4723-a65c-bce2c2a13cf8",
      "name": "Found products?",
      "type": "n8n-nodes-base.if",
      "position": [
        660,
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
              "id": "552c61c2-1ec0-40b5-b473-2423b646418b",
              "operator": {
                "type": "string",
                "operation": "notContains"
              },
              "leftValue": "={{ $json.data.modelResponse }}",
              "rightValue": "[NA]"
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "ffb0289e-9341-4641-bfcd-41b25f0b1379",
      "name": "Look up products",
      "type": "n8n-nodes-base.airtop",
      "position": [
        440,
        -100
      ],
      "parameters": {
        "url": "https://www.producthunt.com/",
        "prompt": "=Extract up to 5 product launches that are {{ $json[\"Relevant Products\"] }} for each product extract the title and URL (if exists).\n\nReturn format:\nToday's [{{ $json[\"Relevant Products\"] }}] on Producthunt\n1. Title 1 (URL 1)\n2. Title 2 (URL 2)\nand so on\n\nIf you cannot find any relevant products, return [NA]",
        "resource": "extraction",
        "operation": "query",
        "sessionMode": "new",
        "additionalFields": {}
      },
      "credentials": {
        "airtopApi": {
          "id": "byhouJF8RLH5DkmY",
          "name": "[PROD] Airtop"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "4d1f0668-d5d5-4440-8608-3cfe3d61d0c0",
      "name": "Send slack message",
      "type": "n8n-nodes-base.slack",
      "position": [
        880,
        -100
      ],
      "webhookId": "9887477b-9680-4701-a2a1-583d47f1fb5d",
      "parameters": {
        "text": "={{ $json.data.modelResponse }}",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "mode": "list",
          "value": "C087FK3J0MC",
          "cachedResultName": "make-debug"
        },
        "otherOptions": {}
      },
      "credentials": {
        "slackApi": {
          "id": "NgjAmOgS9xRg1RlU",
          "name": "Slack account"
        }
      },
      "typeVersion": 2.3
    },
    {
      "id": "921d283e-6d67-4aaa-a344-687bb23b8710",
      "name": "Trigger daily",
      "type": "n8n-nodes-base.scheduleTrigger",
      "position": [
        0,
        -100
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
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "e51e2bd0-43f0-4601-a0ad-f553f419a827",
  "connections": {
    "Trigger daily": {
      "main": [
        [
          {
            "node": "Define relevant products",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Found products?": {
      "main": [
        [
          {
            "node": "Send slack message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Look up products": {
      "main": [
        [
          {
            "node": "Found products?",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Define relevant products": {
      "main": [
        [
          {
            "node": "Look up products",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-1044"></a>

## Template 1044 - Enriquecimento de perfis LinkedIn e geração de ice breakers

- **Nome:** Enriquecimento de perfis LinkedIn e geração de ice breakers
- **Descrição:** Automatiza o enriquecimento de perfis LinkedIn via Bright Data, gera ice breakers personalizados com um modelo LLM e registra os resultados em uma planilha Google.
- **Funcionalidade:** • Leitura de linhas da planilha: Busca os perfis a serem enriquecidos a partir de um Google Sheet.
• Loop por itens: Processa cada URL de LinkedIn individualmente em lotes.
• Disparo de captura no Bright Data: Envia requisições para iniciar a coleta/enriquecimento do perfil.
• Espera e polling do progresso: Aguarda e verifica periodicamente o status do snapshot até estar pronto.
• Recuperação dos dados enriquecidos: Faz chamada para obter o JSON do snapshot com campos como nome, cidade, about, posts e empresa atual.
• Atualização da planilha com dados pessoais: Grava os campos de enriquecimento de volta no Google Sheet, mapeando pelo número da linha.
• Geração de ice breaker com LLM: Usa um modelo de linguagem para criar uma mensagem curta e personalizada baseada nos posts e no about do perfil.
• Escrita do ice breaker na planilha: Salva o texto gerado de volta na linha correspondente do Google Sheet.
• Agendamento e teste manual: Permite executar manualmente ou rodar em agenda programada.
• Tratamento de atrasos e erros: Inclui espera, retries e recomendações para fallback caso snapshot falhe ou exceda limites de taxa.
- **Ferramentas:** • Bright Data: Serviço de coleta/enriquecimento de dados via API (datasets/snapshots) para extrair informações públicas de perfis.
• Anthropic Claude (Haiku): Modelo de linguagem para gerar textos e ice breakers personalizados.
• Google Sheets: Armazenamento de entrada (URLs) e saída (dados enriquecidos e ice breakers).

## Fluxo visual

```mermaid
flowchart LR
    N1["When clicking 'Test workflow'"]
    N2["Sticky Note"]
    N3["Get rows to enrich"]
    N4["Sticky Note3"]
    N5["Sticky Note5"]
    N6["Sticky Note7"]
    N7["Sticky Note9"]
    N8["Anthropic Chat Model"]
    N9["Sticky Note4"]
    N10["Sticky Note1"]
    N11["Basic LLM Chain- Ice Breaker"]
    N12["BrightData_Get_Linkedin"]
    N13["Adjust_input_for_loop"]
    N14["HTTP_Request_Post_Request_BrightData"]
    N15["Wait_For_API_Call_Results"]
    N16["API_Call_Snapshot_Progress"]
    N17["IF-Checking_Status_API_Call"]
    N18["Google Sheets - Update Row with data From API"]
    N19["Google Sheets - Update Row with Ice Breaker"]
    N20["Run Workflow on a certain Schedule"]
    N21["Loop Over Items- All Prospects"]

    N3 --> N13
    N13 --> N21
    N12 --> N18
    N15 --> N16
    N16 --> N17
    N17 --> N15
    N17 --> N12
    N11 --> N19
    N1 --> N3
    N21 --> N14
    N20 --> N3
    N14 --> N15
    N19 --> N21
    N18 --> N11
```

## Fluxo (.json) :

```json
{
  "meta": {
    "instanceId": "5aaf4236c70e34e423fbdb2c7b754d19253a933bb1476d548f75848a01e473cf",
    "templateId": "3561"
  },
  "nodes": [
    {
      "id": "f3641141-a880-4400-bad7-909558848c20",
      "name": "When clicking \"Test workflow\"",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        2260,
        820
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "7b1ddbd1-f918-4ef9-a05e-2c02e6de75df",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        380,
        580
      ],
      "parameters": {
        "color": 4,
        "width": 1289,
        "height": 2698,
        "content": "=======================================\n         WORKFLOW DETAILS & GUIDELINES\n=======================================\nName:\n    LinkedIn Enrichment & Ice Breaker Generator\n\nPurpose:\n    Automate the process of enriching LinkedIn profiles using Bright Data,\n    generate personalized ice breakers with an LLM, and update Google Sheets.\n\nTools Needed:\n    - n8n Nodes:\n        • Manual Trigger or Schedule Trigger\n        • Set\n        • SplitInBatches\n        • HTTP Request\n        • If\n        • Wait\n        • Google Sheets\n        • LangChain LLM (Claude via Anthropic)\n    - External Services:\n        • Bright Data (Dataset API)\n        • Anthropic Claude (Haiku)\n        • Google Sheets API\n\nAPI Keys & Authentication Required:\n    • Bright Data API Key\n        → Used in HTTP Request headers as:\n           `Authorization: Bearer YOUR_BRIGHTDATA_API_KEY`\n    • Google Sheets OAuth2 Credentials\n        → Connects n8n to your Google account for reading/writing to Sheets.\n    • Anthropic API Key\n        → Used for generating ice breakers via Claude models.\n        → Must be set in the Anthropic credential section in n8n.\n\nGeneral Guidelines:\n    • Use descriptive and consistent naming for all nodes.\n    • Add retry limits to polling loops to avoid infinite cycles.\n    • Ensure each LinkedIn URL maps to a unique `row_number`.\n    • Obfuscate any keys before sharing the workflow publicly.\n\nThings to be Aware Of:\n    • Bright Data may require some delay (via Wait node) before snapshot is ready.\n    • Retry logic should not exceed API rate limits.\n    • If snapshot fails or times out, ensure fallback logging is in place.\n    • Claude model IDs and prompt formats may change — validate before updates.\n\nAdditional Notes:\n    • Make a copy of the Google Sheet template before use.\n    • Replace placeholders in `Authorization` headers and credentials section.\n    • Use test data first to avoid exhausting API quotas during setup.\n\n=======================================\n\nThis workflow allows you to enrich LinkedIn profiles using Bright Data,\ngenerate AI-written ice breakers with Claude, and log everything into Google Sheets.\n"
      },
      "typeVersion": 1
    },
    {
      "id": "215cd515-149b-41b1-adbe-fa203cbc9b5d",
      "name": "Get rows to enrich",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        2540,
        820
      ],
      "parameters": {
        "options": {},
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": "gid=0",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1g8Dum0tfZ1nQdd3b6sLhZX2aMu6FzwoVvD0EAXMpPx8/edit#gid=0",
          "cachedResultName": "input"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "1g8Dum0tfZ1nQdd3b6sLhZX2aMu6FzwoVvD0EAXMpPx8",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1g8Dum0tfZ1nQdd3b6sLhZX2aMu6FzwoVvD0EAXMpPx8/edit?usp=drivesdk",
          "cachedResultName": "NoFluff-N8N-Sheet-Template-Hyper Personalization"
        }
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "gq9mwBL5a74eYjfd",
          "name": "Google Sheets account"
        }
      },
      "typeVersion": 4.3
    },
    {
      "id": "f140e851-6409-4169-b5af-28ab6f16d99c",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        3220,
        680
      ],
      "parameters": {
        "width": 1420,
        "height": 460,
        "content": "Personal Data"
      },
      "typeVersion": 1
    },
    {
      "id": "8878ae56-0772-498a-b153-b628222f6688",
      "name": "Sticky Note5",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2220,
        680
      ],
      "parameters": {
        "width": 266.12865147126786,
        "height": 627.5654650079845,
        "content": "Run the workflow manually or activate it to run on schedule\n"
      },
      "typeVersion": 1
    },
    {
      "id": "df3f1f83-1092-40fe-bc5d-301e9a118601",
      "name": "Sticky Note7",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2500,
        460
      ],
      "parameters": {
        "width": 194.6864335083109,
        "height": 525.6560478822986,
        "content": "In this workflow, I use Google Sheets to store the results. \n\nYou can use my template to get started faster:\n\n1. [Click on this link to get the template](https://docs.google.com/spreadsheets/d/1_jbr5zBllTy_pGbogfGSvyv1_0a77I8tU-Ai7BjTAw4/edit?usp=sharing)\n2. Make a copy of the Sheets\n3. Add the URL to this node and the node **\"Google Sheets - Update Row with data\"**\n\n\n"
      },
      "typeVersion": 1
    },
    {
      "id": "1c294196-206a-4add-8d47-8558ba99515d",
      "name": "Sticky Note9",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        380,
        240
      ],
      "parameters": {
        "color": 4,
        "width": 1280,
        "height": 320,
        "content": "=======================================\n            WORKFLOW ASSISTANCE\n=======================================\nFor any questions or support, please contact:\n    Yaron@nofluff.online\n\nExplore more tips and tutorials here:\n   - YouTube: https://www.youtube.com/@YaronBeen/videos\n   - LinkedIn: https://www.linkedin.com/in/yaronbeen/\n=======================================\n"
      },
      "typeVersion": 1
    },
    {
      "id": "3491b2bf-83a0-4966-9ff5-9c7c55f316e0",
      "name": "Anthropic Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatAnthropic",
      "position": [
        4800,
        1240
      ],
      "parameters": {
        "model": {
          "__rl": true,
          "mode": "list",
          "value": "claude-3-5-haiku-20241022",
          "cachedResultName": "Claude 3.5 Haiku"
        },
        "options": {}
      },
      "typeVersion": 1.3
    },
    {
      "id": "66b79bfc-3447-4b42-9617-308e490079bb",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        4720,
        880
      ],
      "parameters": {
        "width": 1120,
        "height": 580,
        "content": "ICE BREAKER\n"
      },
      "typeVersion": 1
    },
    {
      "id": "7557e53f-b898-4831-a52e-be9eeb0f4964",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2940,
        560
      ],
      "parameters": {
        "color": 4,
        "width": 2980,
        "height": 1000,
        "content": "LOOP"
      },
      "typeVersion": 1
    },
    {
      "id": "0119ee4c-bc70-4aef-84e0-881cdea57aa9",
      "name": "Basic LLM Chain- Ice Breaker",
      "type": "@n8n/n8n-nodes-langchain.chainLlm",
      "position": [
        4920,
        900
      ],
      "parameters": {
        "text": "=Help me with writing a witty Ice breaker to try to persuade  {{ $json.name }} from{{ $('BrightData_Get_Linkedin').item.json.city }}. His About section in his Linkedin profile says:{{ $('BrightData_Get_Linkedin').item.json.about }}. \nHe also had a recent post about:{{ $('BrightData_Get_Linkedin').item.json.posts[0].title }}\n\nMake it 4 lines maximum. Focus more on his recent post, not the about. Just to make it feel personalized yet respectful and not creepy.\n\nWRITE THE ICE BREAKER Straight away. Dont write \"here's a draft\" or any other text before your actual response.",
        "promptType": "define"
      },
      "retryOnFail": true,
      "typeVersion": 1.6
    },
    {
      "id": "e3965132-4d21-4252-ab26-525128d79d29",
      "name": "BrightData_Get_Linkedin",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        4120,
        740
      ],
      "parameters": {
        "url": "=https://api.brightdata.com/datasets/v3/snapshot/{{ $json.snapshot_id }}",
        "options": {},
        "sendQuery": true,
        "sendHeaders": true,
        "queryParameters": {
          "parameters": [
            {
              "name": "format",
              "value": "json"
            }
          ]
        },
        "headerParameters": {
          "parameters": [
            {
              "name": "Authorization",
              "value": "Bearer <BRIGHT_DATA_API_KEY>"
            }
          ]
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "0e55b67e-7ddb-4431-8250-59be59c6c557",
      "name": "Adjust_input_for_loop",
      "type": "n8n-nodes-base.set",
      "position": [
        2740,
        820
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "fcc97354-b9f6-4459-a004-46e87902c77c",
              "name": "person_input",
              "type": "string",
              "value": "={{ $json.Linkedin_URL_Person }}"
            },
            {
              "id": "e5415c49-5204-45b1-a0e9-814157127b12",
              "name": "row_number",
              "type": "number",
              "value": "={{ $json.row_number }}"
            }
          ]
        }
      },
      "typeVersion": 3.3
    },
    {
      "id": "0cc85426-64f7-41f8-bd9a-215aaaad3299",
      "name": "HTTP_Request_Post_Request_BrightData",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        3300,
        740
      ],
      "parameters": {
        "url": "https://api.brightdata.com/datasets/v3/trigger",
        "method": "POST",
        "options": {},
        "jsonBody": "=[\n  {\n    \"url\": \"{{ $json.person_input }}\"\n  }\n]",
        "sendBody": true,
        "sendQuery": true,
        "sendHeaders": true,
        "specifyBody": "json",
        "queryParameters": {
          "parameters": [
            {
              "name": "dataset_id",
              "value": "gd_l1viktl72bvl7bjuj0"
            },
            {
              "name": "include_errors",
              "value": "true"
            }
          ]
        },
        "headerParameters": {
          "parameters": [
            {
              "name": "Authorization",
              "value": "Bearer <BRIGHT_DATA_API_KEY>"
            }
          ]
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "851b23e0-6a1b-4a47-95e9-d2f769243a57",
      "name": "Wait_For_API_Call_Results",
      "type": "n8n-nodes-base.wait",
      "position": [
        3500,
        740
      ],
      "webhookId": "8005a2b3-2195-479e-badb-d90e4240e699",
      "parameters": {
        "amount": 10
      },
      "executeOnce": false,
      "typeVersion": 1.1
    },
    {
      "id": "294a7c03-2268-4d7a-b4e7-a52faa78d929",
      "name": "API_Call_Snapshot_Progress",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        3660,
        840
      ],
      "parameters": {
        "url": "=https://api.brightdata.com/datasets/v3/progress/{{ $json.snapshot_id }}",
        "options": {},
        "sendHeaders": true,
        "headerParameters": {
          "parameters": [
            {
              "name": "Authorization",
              "value": "Bearer <Bright_Data_API_KEY>"
            }
          ]
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "d568403b-c323-4798-b7e5-e4a89dfe7830",
      "name": "IF-Checking_Status_API_Call",
      "type": "n8n-nodes-base.if",
      "position": [
        3860,
        900
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
              "id": "7932282b-71bb-4bbb-ab73-4978e554de7e",
              "operator": {
                "name": "filter.operator.equals",
                "type": "string",
                "operation": "equals"
              },
              "leftValue": "={{ $json.status }}",
              "rightValue": "running"
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "b44b5f4b-8aef-4ea3-bbd7-1e72548dda64",
      "name": "Google Sheets - Update Row with data From API",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        4500,
        940
      ],
      "parameters": {
        "columns": {
          "value": {
            "city": "={{ $json.city }}",
            "name": "={{ $json.name }}",
            "about": "={{ $json.about }}",
            "row_number": "={{ $('Loop Over Items- All Prospects').item.json.row_number }}",
            "country_code": "={{ $json.country_code }}",
            "Linkedin_URL_Person": "={{ $json.input.url }}",
            "current_company.name": "={{ $json.current_company.name }}"
          },
          "schema": [
            {
              "id": "Linkedin_URL_Person",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "Linkedin_URL_Person",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
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
              "id": "city",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "city",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "country_code",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "country_code",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Position",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "Position",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "about",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "about",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "current_company.name",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "current_company.name",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Post 1",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "Post 1",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Post 2",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "Post 2",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Post 3",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "Post 3",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Ice Breaker 1",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "Ice Breaker 1",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Ice Breaker 2",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "Ice Breaker 2",
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
          "value": "gid=0",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1_jbr5zBllTy_pGbogfGSvyv1_0a77I8tU-Ai7BjTAw4/edit#gid=0",
          "cachedResultName": "input"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "1_jbr5zBllTy_pGbogfGSvyv1_0a77I8tU-Ai7BjTAw4",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1_jbr5zBllTy_pGbogfGSvyv1_0a77I8tU-Ai7BjTAw4/edit?usp=drivesdk",
          "cachedResultName": "NoFluff-N8N-Sheet-Template"
        }
      },
      "typeVersion": 4.3,
      "alwaysOutputData": true
    },
    {
      "id": "081f9e1d-6325-4645-bb0c-368a8ac3be99",
      "name": "Google Sheets - Update Row with Ice Breaker",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        5400,
        1340
      ],
      "parameters": {
        "columns": {
          "value": {
            "row_number": "={{ $('Loop Over Items- All Prospects').item.json.row_number }}",
            "Ice Breaker 1": "={{ $json.text }}"
          },
          "schema": [
            {
              "id": "Linkedin_URL_Person",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "Linkedin_URL_Person",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "name",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "name",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "city",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "city",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "country_code",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "country_code",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Position",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "Position",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "about",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "about",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "current_company.name",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "current_company.name",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Post 1",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "Post 1",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Post 2",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "Post 2",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Post 3",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "Post 3",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Ice Breaker 1",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "Ice Breaker 1",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Ice Breaker 2",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "Ice Breaker 2",
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
          "value": "gid=0",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1_jbr5zBllTy_pGbogfGSvyv1_0a77I8tU-Ai7BjTAw4/edit#gid=0",
          "cachedResultName": "input"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "1_jbr5zBllTy_pGbogfGSvyv1_0a77I8tU-Ai7BjTAw4",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1_jbr5zBllTy_pGbogfGSvyv1_0a77I8tU-Ai7BjTAw4/edit?usp=drivesdk",
          "cachedResultName": "NoFluff-N8N-Sheet-Template"
        }
      },
      "typeVersion": 4.3,
      "alwaysOutputData": true
    },
    {
      "id": "7709c869-5283-4760-b929-fde27167f040",
      "name": "Run Workflow on a certain Schedule",
      "type": "n8n-nodes-base.scheduleTrigger",
      "position": [
        2260,
        1000
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
      "id": "84e08531-b548-43f2-a17a-b2809f833d32",
      "name": "Loop Over Items- All Prospects",
      "type": "n8n-nodes-base.splitInBatches",
      "position": [
        2980,
        720
      ],
      "parameters": {
        "options": {}
      },
      "typeVersion": 3
    }
  ],
  "pinData": {},
  "connections": {
    "Get rows to enrich": {
      "main": [
        [
          {
            "node": "Adjust_input_for_loop",
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
            "node": "Basic LLM Chain- Ice Breaker",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Adjust_input_for_loop": {
      "main": [
        [
          {
            "node": "Loop Over Items- All Prospects",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "BrightData_Get_Linkedin": {
      "main": [
        [
          {
            "node": "Google Sheets - Update Row with data From API",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Wait_For_API_Call_Results": {
      "main": [
        [
          {
            "node": "API_Call_Snapshot_Progress",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "API_Call_Snapshot_Progress": {
      "main": [
        [
          {
            "node": "IF-Checking_Status_API_Call",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "IF-Checking_Status_API_Call": {
      "main": [
        [
          {
            "node": "Wait_For_API_Call_Results",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "BrightData_Get_Linkedin",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Basic LLM Chain- Ice Breaker": {
      "main": [
        [
          {
            "node": "Google Sheets - Update Row with Ice Breaker",
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
            "node": "Get rows to enrich",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Loop Over Items- All Prospects": {
      "main": [
        [],
        [
          {
            "node": "HTTP_Request_Post_Request_BrightData",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Run Workflow on a certain Schedule": {
      "main": [
        [
          {
            "node": "Get rows to enrich",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "HTTP_Request_Post_Request_BrightData": {
      "main": [
        [
          {
            "node": "Wait_For_API_Call_Results",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Sheets - Update Row with Ice Breaker": {
      "main": [
        [
          {
            "node": "Loop Over Items- All Prospects",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Sheets - Update Row with data From API": {
      "main": [
        [
          {
            "node": "Basic LLM Chain- Ice Breaker",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-1045"></a>

## Template 1045 - Auditoria de Segurança de Website

- **Nome:** Auditoria de Segurança de Website
- **Descrição:** Este fluxo coleta a URL de uma página, analisa os cabeçalhos de segurança e o conteúdo da página e gera um relatório de auditoria de segurança com recomendações enviando-o por e-mail.
- **Funcionalidade:** • Captação da URL de entrada: recebe a URL fornecida pelo usuário via formulário para iniciar a análise.
• Recuperação do conteúdo da página: realiza uma requisição HTTP para obter o HTML/texto da página.
• Análise de cabeçalhos de segurança: avalia cabeçalhos HTTP de segurança e políticas configuradas.
• Análise de conteúdo da página: avalia o HTML/JavaScript para vulnerabilidades do lado do cliente.
• Auditoria de configuração de segurança: verifica cookies, CSP e outras configurações visíveis no lado do cliente.
• Mesclagem de resultados: combina saídas das análises para um relatório consolidado.
• Geração de relatório HTML: formata as descobertas em um relatório HTML com seções bem organizadas.
• Envio do relatório por e-mail: envia o relatório HTML ao destinatário informado.
- **Ferramentas:** • OpenAI API (GPT-4o mini): modelo de linguagem utilizado para analisar conteúdo da página e cabeçalhos de segurança e gerar recomendações.
• Gmail (OAuth2): envio do relatório por e-mail.

## Fluxo visual

```mermaid
flowchart LR
    N1["Landing Page Url"]
    N2["Scrape Website"]
    N3["OpenAI Headers Analysis"]
    N4["OpenAI Content Analysis"]
    N5["Security Vulnerabilities Audit"]
    N6["Security Configuration Audit"]
    N7["Merge Security Results"]
    N8["Aggregate Audit Results"]
    N9["Process Audit Results"]
    N10["Send Security Report"]
    N11["Sticky Note - Setup Instructions"]
    N12["Sticky Note - OpenAI Analysis"]
    N13["Sticky Note - Email Configuration"]
    N14["Sticky Note - Audit Process"]
    N15["Sticky Note - How To Use"]
    N16["Sticky Note - Report Formatting"]
    N17["Sticky Note - Results Processing"]
    N18["Extract Headers for Debug"]
    N19["convert to HTML"]

    N2 --> N5
    N2 --> N18
    N19 --> N10
    N1 --> N2
    N9 --> N19
    N7 --> N8
    N8 --> N9
    N18 --> N6
    N6 --> N7
    N5 --> N7
```

## Fluxo (.json) :

```json
{
  "meta": {
    "instanceId": "c2589fa234defe76e8a1321c3a7d0a73579d0120d64d927e88f5e3be584ae8d4"
  },
  "nodes": [
    {
      "id": "634f2fc5-0ba7-42ad-bdf5-ade3415dd288",
      "name": "Landing Page Url",
      "type": "n8n-nodes-base.formTrigger",
      "position": [
        -200,
        580
      ],
      "webhookId": "afe067a5-4878-4c9d-b746-691f77190f54",
      "parameters": {
        "options": {},
        "formTitle": "Website Security Scanner",
        "formFields": {
          "values": [
            {
              "fieldLabel": "Landing Page Url",
              "placeholder": "https://example.com",
              "requiredField": true
            }
          ]
        },
        "formDescription": "Check your website for security vulnerabilities and get a detailed report"
      },
      "typeVersion": 2.2
    },
    {
      "id": "6cee63ca-d0f6-444a-b882-22da1a9fd70c",
      "name": "Scrape Website",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        0,
        580
      ],
      "parameters": {
        "url": "={{ $json['Landing Page Url'] }}",
        "options": {
          "redirect": {
            "redirect": {
              "maxRedirects": 5
            }
          },
          "response": {
            "response": {
              "fullResponse": true,
              "responseFormat": "text"
            }
          }
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "0d5d1e76-e627-4565-a1ee-6a610f4b2028",
      "name": "OpenAI Headers Analysis",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        340,
        600
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
          "id": "yZ0AIg9abV8HJadB",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "04427ef7-515d-4a1a-88d2-ade10aeefc87",
      "name": "OpenAI Content Analysis",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        340,
        980
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
          "id": "yZ0AIg9abV8HJadB",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "d4ee4db8-aa04-4068-9b97-d16acf98c027",
      "name": "Security Vulnerabilities Audit",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        360,
        780
      ],
      "parameters": {
        "text": "=You are an elite cybersecurity expert specializing in web application security.\n\nIn this task, you will analyze the HTML and visible content of the webpage to identify potential security vulnerabilities.\n\nAudit Structure\nYou will review all client-side security aspects of the page and present your findings in three sections:\n- Critical Vulnerabilities – Issues that could lead to immediate compromise\n- Information Leakage – Sensitive data exposed in page source\n- Client-Side Weaknesses – JavaScript vulnerabilities, XSS opportunities, etc.\n\nFor each issue found, provide:\n1. A clear description of the vulnerability\n2. The potential impact\n3. A specific recommendation to fix it\n\nIf you find no issues in a particular section, explicitly state that no issues were found in that category.\n\nEnsure the output is properly formatted, clean, and highly readable. Focus only on issues that can be detected from the client-side code.\n\nHere is the content of the webpage: {{ $json.data }}",
        "options": {},
        "promptType": "define"
      },
      "typeVersion": 1.7
    },
    {
      "id": "c9702f2b-845b-464d-9c32-3d5be308ef77",
      "name": "Security Configuration Audit",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        360,
        380
      ],
      "parameters": {
        "text": "=You are an elite web security expert specializing in secure configurations.\n\nIn this task, you will analyze the HTTP headers, cookies, and overall configuration of a webpage to identify security misconfigurations.\n\nAudit Structure\nYou will begin by listing ALL security headers that ARE present and properly configured.\n\nBe very clear and explicit about which headers are present and which are missing. For each header, clearly state whether it is present or missing, and if present, what its value is.\n\nThen, present your findings in three sections:\n- Header Security – Missing or misconfigured security headers\n- Cookie Security – Insecure cookie configurations\n- Content Security – CSP issues, mixed content, etc.\n\nFor each finding, provide:\n1. A clear description of the misconfiguration\n2. The security implications\n3. The recommended secure configuration with example code\n\nIf you find no issues in a particular section, explicitly state that no issues were found.\n\nUse proper formatting with code blocks for configuration examples. Only include issues that can be detected from client-side inspection.\nHere are the response headers: {{ $json.formattedHeaders }}\n\nPlease Respond like this\n\n### [any section heading that includes \"Headers]\n\n1. **[Header Title]**\n   - **Present?** Yes/No\n   - **Value:** `actual-header-value`\n",
        "options": {},
        "promptType": "define"
      },
      "typeVersion": 1.7
    },
    {
      "id": "3b43be75-c35c-44e4-8ecc-a29c48e3625c",
      "name": "Merge Security Results",
      "type": "n8n-nodes-base.merge",
      "position": [
        860,
        580
      ],
      "parameters": {},
      "typeVersion": 3,
      "alwaysOutputData": true
    },
    {
      "id": "da134256-d7fa-4a3f-ba24-acc320a944a2",
      "name": "Aggregate Audit Results",
      "type": "n8n-nodes-base.aggregate",
      "position": [
        1060,
        580
      ],
      "parameters": {
        "options": {},
        "fieldsToAggregate": {
          "fieldToAggregate": [
            {
              "fieldToAggregate": "output"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "id": "aef1da93-0b01-4a7f-9439-1f74c2af12d6",
      "name": "Process Audit Results",
      "type": "n8n-nodes-base.code",
      "position": [
        1240,
        580
      ],
      "parameters": {
        "jsCode": "// ✅ Updated extractSecurityHeaders and related logic remains unchanged\n\nfunction extractSecurityHeaders(rawHeaders = {}, configOutput = '') {\n  const securityHeaders = [\n    'Content-Security-Policy',\n    'Strict-Transport-Security',\n    'X-Content-Type-Options',\n    'X-Frame-Options',\n    'Referrer-Policy',\n    'Permissions-Policy',\n    'X-XSS-Protection',\n    'Cross-Origin-Embedder-Policy',\n    'Cross-Origin-Opener-Policy',\n    'X-Permitted-Cross-Domain-Policies'\n  ];\n\n  const headerStatus = {};\n  for (const header of securityHeaders) {\n    headerStatus[header] = { present: false, value: '' };\n  }\n\n  for (const header in rawHeaders) {\n    const norm = header.trim().toLowerCase();\n    for (const standard of securityHeaders) {\n      if (norm === standard.toLowerCase()) {\n        headerStatus[standard].present = true;\n        headerStatus[standard].value = rawHeaders[header];\n      }\n    }\n  }\n\n  const presentSection = configOutput.match(/(?:###|##|\\*\\*)[^\\n]*?\\bheaders?\\b[\\s\\S]*?(?=###|##|\\*\\*|$)/i);\n  if (presentSection) {\n    const section = presentSection[0];\n    for (const header of securityHeaders) {\n      const title = header.replace(/-/g, ' ').replace(/\\b\\w/g, c => c.toUpperCase());\n      const regex = new RegExp(`\\\\*\\\\*${title}\\\\*\\\\*[^\\\\n]*?\\\\*\\\\*Present\\\\?\\\\*\\\\*\\\\s*Yes[^\\\\n]*?\\\\*\\\\*Value:\\\\*\\\\*\\\\s*\\`([^\\\\\\`]+)\\``, 'is');\n      const match = section.match(regex);\n      if (match && match[1]) {\n        headerStatus[header].present = true;\n        headerStatus[header].value = match[1].trim();\n      }\n    }\n  }\n\n  return headerStatus;\n}\n\nfunction hasUnsafeInline(value) {\n  return value && value.includes('unsafe-inline');\n}\n\nfunction determineGrade(headerStatus) {\n  const critical = [\n    'Content-Security-Policy',\n    'Strict-Transport-Security',\n    'X-Content-Type-Options',\n    'X-Frame-Options'\n  ];\n  const important = ['Referrer-Policy', 'Permissions-Policy'];\n  const additional = [\n    'X-XSS-Protection',\n    'Cross-Origin-Embedder-Policy',\n    'Cross-Origin-Opener-Policy',\n    'X-Permitted-Cross-Domain-Policies'\n  ];\n\n  let criticalCount = 0;\n  let importantCount = 0;\n  let hasCSPIssue = false;\n\n  for (const h of critical) {\n    if (headerStatus[h]?.present) {\n      criticalCount++;\n      if (h === 'Content-Security-Policy' && hasUnsafeInline(headerStatus[h].value)) {\n        hasCSPIssue = true;\n      }\n    }\n  }\n\n  for (const h of important) {\n    if (headerStatus[h]?.present) importantCount++;\n  }\n\n  if (criticalCount === critical.length) {\n    if (importantCount === important.length) return hasCSPIssue ? 'A-' : 'A+';\n    if (importantCount >= 1) return hasCSPIssue ? 'B+' : 'A-';\n    return hasCSPIssue ? 'B' : 'B+';\n  } else if (criticalCount >= critical.length - 1) {\n    return importantCount >= 1 ? 'B' : 'C+';\n  } else if (criticalCount >= 2) {\n    return 'C';\n  } else if (criticalCount >= 1) {\n    return 'D';\n  } else {\n    return 'F';\n  }\n}\n\nfunction formatHeadersForDisplay(headerStatus) {\n  const present = Object.keys(headerStatus).filter(h => headerStatus[h].present);\n  return present.length > 0 ? present.join(', ') : 'No security headers detected';\n}\n\nfunction processSecurityHeaders(items) {\n  try {\n    const json = items[0].json || items[0];\n\n    // ⛏️ Try to grab from originalHeaders if available\n    const rawHeaders =\n      json?.originalHeaders ||\n      $('Extract Headers for Debug')?.first()?.json?.originalHeaders ||\n      json?.headers ||\n      {};\n\n    const configOutput = json.configOutput || json.output?.[0] || '';\n    const vulnOutput = json.vulnOutput || json.output?.[1] || '';\n\n    const headerStatus = extractSecurityHeaders(rawHeaders, configOutput);\n    const presentHeaders = formatHeadersForDisplay(headerStatus);\n    const grade = determineGrade(headerStatus);\n\n    const timestamp = new Date().toLocaleString('en-US', {\n      year: 'numeric',\n      month: 'long',\n      day: 'numeric',\n      hour: '2-digit',\n      minute: '2-digit'\n    });\n\n    const url =\n      json?.formValues?.url ||\n      json?.['Landing Page Url'] ||\n      $('Landing Page Url')?.first()?.json?.['Landing Page Url'] ||\n      json?.Landing_Page_Url ||\n      json?.landingPageUrl ||\n      json?.url ||\n      'https://example.com';\n\n    return [\n      {\n        json: {\n          ...json,\n          auditData: {\n            url,\n            timestamp,\n            grade,\n            criticalCount:\n              headerStatus['Content-Security-Policy'].present &&\n              hasUnsafeInline(headerStatus['Content-Security-Policy'].value)\n                ? 1\n                : 0,\n            warningCount: Object.keys(headerStatus).filter(\n              h =>\n                !headerStatus[h].present &&\n                !['Strict-Transport-Security', 'Content-Security-Policy'].includes(h)\n            ).length,\n            presentHeaders,\n            configOutput,\n            vulnOutput,\n            headerStatus,\n            originalHeaders: rawHeaders\n          }\n        }\n      }\n    ];\n  } catch (err) {\n    return [{ json: { ...items[0].json, error: err.message } }];\n  }\n}\n\nreturn processSecurityHeaders(items);\n"
      },
      "typeVersion": 2
    },
    {
      "id": "ced29b26-474c-4d62-808a-3284103c9d60",
      "name": "Send Security Report",
      "type": "n8n-nodes-base.gmail",
      "position": [
        1580,
        580
      ],
      "webhookId": "2979e4dc-1689-447e-8cd4-eb907b4eedf4",
      "parameters": {
        "sendTo": "=example@here.com",
        "message": "={{ $json.emailHtml }}",
        "options": {},
        "subject": "=Website Security Audit - {{ $json.auditData.url }}"
      },
      "credentials": {
        "gmailOAuth2": {
          "id": "9CEpbF4jIWb2OETv",
          "name": "Gmail account"
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "918c0fc4-2f02-4594-bfc9-e36035f2d802",
      "name": "Sticky Note - Setup Instructions",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -820,
        400
      ],
      "parameters": {
        "width": 500,
        "height": 440,
        "content": "## Quick Setup Guide\n\n1. **Add OpenAI API Credentials**\n   - Go to Settings → Credentials → New → OpenAI API\n   - Enter your API key from platform.openai.com\n\n2. **Add Gmail Credentials**\n   - Go to Settings → Credentials → New → Gmail OAuth2 API\n   - Complete the OAuth setup process\n\n3. **Update Email Configuration**\n   - Open the 'Send Security Report' node\n   - Change the recipient email address from the default\n\n4. **Activate and Deploy Workflow**\n   - Click 'Active' toggle in the top right\n   - Copy the form URL to share with others or use yourself"
      },
      "typeVersion": 1
    },
    {
      "id": "6e31b9b8-ae02-4da4-a75e-5d784b210c64",
      "name": "Sticky Note - OpenAI Analysis",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        300,
        120
      ],
      "parameters": {
        "color": 3,
        "width": 420,
        "height": 240,
        "content": "## OpenAI Security Analysis\n\n- Add your OpenAI credentials (required)\n- Using GPT-4o models provides more detailed security analysis\n- Analyzes for XSS, information disclosure, CSRF, and more\n- Each agent scans different aspects of website security\n- Consider upgrading to GPT-4o (not mini) for production use"
      },
      "typeVersion": 1
    },
    {
      "id": "590b1f1c-024d-4002-a8eb-d9dc81528f89",
      "name": "Sticky Note - Email Configuration",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1480,
        220
      ],
      "parameters": {
        "color": 3,
        "width": 360,
        "height": 200,
        "content": "## Send Security Report\n\n- Connects securely to Gmail for sending detailed reports\n- Report is sent as HTML formatted email\n- Subject line includes the scanned URL\n- Requires Gmail OAuth credentials to be set up"
      },
      "typeVersion": 1
    },
    {
      "id": "dc6223f8-a98c-497a-97c9-af39e80e6d66",
      "name": "Sticky Note - Audit Process",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -200,
        780
      ],
      "parameters": {
        "color": 2,
        "width": 420,
        "height": 300,
        "content": "## Security Audit Process\n\n- This workflow performs two parallel security analyses\n- Top path: Checks headers, cookies, and security configurations\n- Bottom path: Analyzes HTML/JavaScript for client-side vulnerabilities\n- Results are merged and formatted into a comprehensive report\n- Analysis is non-invasive and only examines client-side content"
      },
      "typeVersion": 1
    },
    {
      "id": "cbda16d4-f1f4-491c-b38c-43d7544e129b",
      "name": "Sticky Note - How To Use",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -240,
        240
      ],
      "parameters": {
        "color": 4,
        "width": 400,
        "height": 280,
        "content": "## How To Use This Workflow\n\n1. **Deploy the workflow** and activate it\n2. **Access the form** via the provided URL\n3. **Enter any website URL** to scan (must include http:// or https://)\n4. **Submit the form** to trigger the analysis\n5. **Check your email** for the detailed security report\n6. **Share the results** with your development team to implement fixes"
      },
      "typeVersion": 1
    },
    {
      "id": "4859416f-4de3-43ea-9461-3ead8a38db6e",
      "name": "Sticky Note - Report Formatting",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1160,
        220
      ],
      "parameters": {
        "color": 5,
        "width": 300,
        "height": 280,
        "content": "## Report Formatting\n\n- Creates beautiful, professional HTML email report\n- Visual grade indicator (A-F) based on findings\n- Includes count of critical issues and warnings\n- Color-coded sections for easy readability\n- Mobile-friendly responsive design"
      },
      "typeVersion": 1
    },
    {
      "id": "a02db4c7-2cad-41ff-b5ad-e1b19604a699",
      "name": "Sticky Note - Results Processing",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        840,
        240
      ],
      "parameters": {
        "width": 300,
        "height": 240,
        "content": "## Results Processing\n\n- Analyzes AI output to determine security grade\n- Counts critical issues and warnings\n- Extracts present security headers\n- Prepares data for the email report template\n- Generates timestamp for the report"
      },
      "typeVersion": 1
    },
    {
      "id": "41b834c8-62f7-47e7-9d9d-e0e1244faecb",
      "name": "Extract Headers for Debug",
      "type": "n8n-nodes-base.code",
      "position": [
        200,
        460
      ],
      "parameters": {
        "jsCode": "// Format headers into a readable string\nlet formattedHeaders = '';\nif (items[0].json.headers) {\n  for (const key in items[0].json.headers) {\n    formattedHeaders += `${key}: ${items[0].json.headers[key]}\\n`;\n  }\n}\n\n// Return both the original data and the formatted headers\nreturn [{\n  json: {\n    ...items[0].json,\n    formattedHeaders: formattedHeaders,\n    originalHeaders: items[0].json.headers // Keep the original headers too\n  }\n}];"
      },
      "typeVersion": 2
    },
    {
      "id": "0b76b396-fc96-41fc-a095-30971dd88271",
      "name": "convert to HTML",
      "type": "n8n-nodes-base.code",
      "position": [
        1400,
        580
      ],
      "parameters": {
        "jsCode": "// Create a direct HTML template with improved styling\nconst auditData = items[0].json.auditData;\n\nfunction formatConfigurationIssues() {\n  if (!auditData.configOutput || auditData.configOutput.trim() === '') {\n    return '<p>No specific configuration issues detected.</p>';\n  }\n\n  try {\n    const config = auditData.configOutput.trim();\n    let html = '';\n    const renderedKeys = new Set();\n\n    const renderBlock = (title, description, impact, recommendation) => `\n      <div style=\"border-left: 4px solid #3498DB; padding: 10px; margin-bottom: 15px;\">\n        <div style=\"font-weight: bold; color: #3498DB;\">${title}</div>\n        ${description ? `<div style=\"margin-top: 5px;\">${description}</div>` : ''}\n        ${impact ? `<div style=\"margin-top: 5px; font-style: italic; color: #7F8C8D;\">Impact: ${impact}</div>` : ''}\n        ${recommendation ? `<div style=\"margin-top: 5px;\"><strong>Recommendation:</strong></div>\n          <pre style=\"background-color: #f8f9fa; padding: 10px; border-radius: 5px; overflow-x: auto; font-family: monospace;\">${recommendation}</pre>` : ''}\n      </div>`;\n\n    const sections = config.split(/(?=^###\\s+)/gm).filter(Boolean);\n\n    for (const section of sections) {\n      const sectionTitleMatch = section.match(/^###\\s+(.*)/);\n      const sectionTitle = sectionTitleMatch?.[1]?.trim() || 'Unnamed Section';\n      const sectionKey = sectionTitle.toLowerCase();\n\n      // Skip \"no issues found\" sections\n      if (/no issues? (found|were found)/i.test(section)) continue;\n\n      const lines = section.split(/\\n+/).filter(line => line.trim() !== '');\n\n      let currentTitle = '';\n      let description = '';\n      let impact = '';\n      let recommendation = '';\n\n      for (let i = 0; i < lines.length; i++) {\n        const line = lines[i].trim();\n\n        // Start of a new numbered or bolded issue\n        const numberedTitle = line.match(/^\\d+\\.\\s+\\*\\*(.*?)\\*\\*/);\n        const bulletTitle = line.match(/^\\*\\*(.*?)\\*\\*/);\n\n        if (numberedTitle || (!currentTitle && bulletTitle)) {\n          // Flush last block\n          if (currentTitle && !renderedKeys.has(`${sectionKey}::${currentTitle.toLowerCase()}`)) {\n            html += renderBlock(currentTitle, description, impact, recommendation);\n            renderedKeys.add(`${sectionKey}::${currentTitle.toLowerCase()}`);\n          }\n\n          currentTitle = (numberedTitle || bulletTitle)[1].trim();\n          description = '';\n          impact = '';\n          recommendation = '';\n          continue;\n        }\n\n        const valueMatch = line.match(/- \\*\\*Value:\\*\\*\\s*`?(.*?)`?$/i);\n        const presentMatch = line.match(/- \\*\\*Present\\?\\*\\*.*?(Yes|No)/i);\n        const descMatch = line.match(/- \\*\\*Description:\\*\\*\\s*(.*)/i);\n        const impactMatch = line.match(/- \\*\\*(?:Impact|Security Implication|Potential Impact):\\*\\*\\s*(.*)/i);\n        const recMatch = line.match(/```(?:\\w*)?\\n([\\s\\S]*?)```/i);\n\n        if (descMatch) {\n          description = descMatch[1].trim();\n        } else if (valueMatch || presentMatch) {\n          const present = presentMatch?.[1]?.trim() || 'Unknown';\n          const value = valueMatch?.[1]?.trim() || '[Not provided]';\n          description = `This header is ${present.toLowerCase()}. Value: ${value}.`;\n        }\n\n        if (impactMatch) {\n          impact = impactMatch[1].trim();\n        }\n\n        if (recMatch) {\n          recommendation = recMatch[1].trim();\n        }\n      }\n\n      // Final block in section\n      if (currentTitle && !renderedKeys.has(`${sectionKey}::${currentTitle.toLowerCase()}`)) {\n        html += renderBlock(currentTitle, description, impact, recommendation);\n        renderedKeys.add(`${sectionKey}::${currentTitle.toLowerCase()}`);\n      }\n    }\n\n    return html || '<p>No configuration issues detected.</p>';\n  } catch (e) {\n    console.error('Error in formatConfigurationIssues:', e);\n    return `<p>Error processing configuration issues: ${e.message}</p>`;\n  }\n}\n\n\n\n// Create header badge HTML\nfunction createHeaderBadge(headerName, isWarning = false) {\n  const isPresent = auditData.headerStatus && \n                   auditData.headerStatus[headerName] && \n                   auditData.headerStatus[headerName].present;\n  \n  const color = isWarning && isPresent ? \"#F39C12\" : (isPresent ? \"#27AE60\" : \"#E74C3C\");\n  const icon = isPresent ? \"✓\" : \"✗\";\n  \n  return `<span style=\"display: inline-block; margin: 2px; padding: 4px 8px; background-color: ${color}; color: white; border-radius: 4px; font-size: 12px;\">${icon} ${headerName}</span>`;\n}\n\n// Format warnings section\nfunction formatWarningsSection() {\n  if (!auditData.warningCount || auditData.warningCount === 0 || !auditData.headerStatus) {\n    return '<p>No warnings detected.</p>';\n  }\n\n  const csp = Object.entries(auditData.headerStatus).find(([k]) => k.toLowerCase() === 'content-security-policy');\n  const hsts = Object.entries(auditData.headerStatus).find(([k]) => k.toLowerCase() === 'strict-transport-security');\n  const xss = Object.entries(auditData.headerStatus).find(([k]) => k.toLowerCase() === 'x-xss-protection');\n\n  let warnings = '';\n\n  if (csp && csp[1].value && csp[1].value.includes('unsafe-inline')) {\n    warnings += `\n      <div style=\"margin-top: 15px;\">\n        <div style=\"border-left: 4px solid #F39C12; padding: 10px;\">\n          <strong style=\"color: #F39C12;\">Content-Security-Policy: unsafe-inline</strong>\n          <p>The use of 'unsafe-inline' allows potentially malicious scripts to execute.</p>\n        </div>\n      </div>`;\n  }\n\n  if (hsts && hsts[1].value) {\n    const match = hsts[1].value.match(/max-age=(\\d+)/);\n    const age = match ? parseInt(match[1]) : 0;\n    if (age < 2592000) {\n      warnings += `\n        <div style=\"margin-top: 15px;\">\n          <div style=\"border-left: 4px solid #F39C12; padding: 10px;\">\n            <strong style=\"color: #F39C12;\">Strict-Transport-Security</strong>\n            <p>max-age is too low (${age}). Should be at least 2592000 (30 days).</p>\n          </div>\n        </div>`;\n    }\n  }\n\n  if (xss && !xss[1].present) {\n    warnings += `\n      <div style=\"margin-top: 15px;\">\n        <div style=\"border-left: 4px solid #F39C12; padding: 10px;\">\n          <strong style=\"color: #F39C12;\">Missing X-XSS-Protection</strong>\n          <p>This header enables the browser's XSS filter. Lack of it increases XSS risks.</p>\n        </div>\n      </div>`;\n  }\n\n  if (!warnings) {\n    warnings = `\n      <div style=\"margin-top: 15px;\">\n        <div style=\"border-left: 4px solid #F39C12; padding: 10px;\">\n          <strong style=\"color: #F39C12;\">${auditData.warningCount} warnings detected</strong>\n          <p>See the Configuration Issues section below for more info.</p>\n        </div>\n      </div>`;\n  }\n\n  return warnings;\n}\n\nfunction formatLongValue(value) {\n  if (!value || typeof value !== 'string') return '[empty]';\n\n  // Convert URLs into clickable links\n  value = value.replace(/(https?://[^\\s]+)/g, '<a href=\"$1\" style=\"color: #3498DB; text-decoration: none;\" target=\"_blank\">$1</a>');\n\n  // Add line breaks after commas or semicolons for readability\n  if (value.length > 100) {\n    value = value.replace(/([,;])\\s*/g, '$1<br>');\n  }\n\n  return value;\n}\n\nfunction formatDetailedRawHeaders() {\n  const allHeaders = [];\n  const seen = new Set();\n\n  const addHeader = (name, value) => {\n    const key = name.toLowerCase();\n    if (seen.has(key)) return;\n    seen.add(key);\n\n    const status = Object.entries(auditData.headerStatus || {}).find(\n      ([k]) => k.toLowerCase() === name.toLowerCase()\n    );\n    const present = status ? status[1].present : !!value;\n\n    allHeaders.push({\n      name: name.trim(),\n      present,\n      value: value || '[empty]'\n    });\n  };\n\n  Object.entries(auditData.originalHeaders || {}).forEach(([key, value]) => {\n    if (key) addHeader(key, value);\n  });\n\n  const securityHeaders = [\n    'content-security-policy',\n    'strict-transport-security',\n    'x-content-type-options',\n    'x-frame-options',\n    'referrer-policy',\n    'permissions-policy',\n    'x-xss-protection'\n  ];\n\n  const isWarningHeader = (name, value) => {\n    const lower = name.toLowerCase();\n    if (lower === 'strict-transport-security') {\n      const match = value.match(/max-age=(\\d+)/);\n      return match && parseInt(match[1]) < 2592000;\n    }\n    if (lower === 'content-security-policy') return value.includes(\"'unsafe-inline'\");\n    return false;\n  };\n\n  const tableRows = allHeaders.map(header => {\n    const isSecurity = securityHeaders.includes(header.name.toLowerCase());\n    const warning = isSecurity && isWarningHeader(header.name, header.value);\n    const missing = isSecurity && !header.present;\n\n    let bgColor = '#F8F9FA';\n    let textColor = '#333';\n\n    if (isSecurity) {\n      if (missing) {\n        bgColor = '#FFEBEE';\n        textColor = '#C62828';\n      } else if (warning) {\n        bgColor = '#FFF9C4';\n        textColor = '#F57F17';\n      } else {\n        bgColor = '#E8F5E9';\n        textColor = '#2E7D32';\n      }\n    }\n\n    return `\n      <tr style=\"background-color: ${bgColor}; color: ${textColor};\">\n        <td title=\"${isSecurity ? (missing ? 'Missing' : (warning ? 'Needs review' : 'Secure')) : 'Informational'}\" style=\"padding: 8px; font-weight: bold;\">${header.name}</td>\n        <td style=\"padding: 8px; text-align: center;\">${header.present ? 'present' : 'absent'}</td>\n        <td style=\"padding: 8px; word-break: break-word; font-family: monospace;\">${formatLongValue(header.value)}</td>\n      </tr>`;\n  }).join('');\n\n  return `\n    <table style=\"width: 100%; border-collapse: collapse; margin-top: 10px;\">\n      <thead>\n        <tr style=\"background-color: #E0E0E0;\">\n          <th style=\"padding: 10px;\">Header</th>\n          <th style=\"padding: 10px;\">Status</th>\n          <th style=\"padding: 10px;\">Value</th>\n        </tr>\n      </thead>\n      <tbody>\n        ${tableRows}\n      </tbody>\n    </table>`;\n}\n\n// Format additional information section\nfunction formatAdditionalInfo() {\n  const headers = [\n    {\n      name: 'access-control-allow-origin',\n      description: 'This is a very lax CORS policy. Such a policy should only be used on a public CDN.'\n    },\n    {\n      name: 'strict-transport-security',\n      description: 'HTTP Strict Transport Security is an excellent feature to support on your site and strengthens your implementation of TLS by getting the User Agent to enforce the use of HTTPS.'\n    },\n    {\n      name: 'content-security-policy',\n      description: 'Content Security Policy is an effective measure to protect your site from XSS attacks. By whitelisting sources of approved content, you can prevent the browser from loading malicious assets. Analyse this policy in more detail. You can sign up for a free account on Report URI to collect reports about problems on your site.'\n    },\n    {\n      name: 'permissions-policy',\n      description: 'Permissions Policy is a new header that allows a site to control which features and APIs can be used in the browser.'\n    },\n    {\n      name: 'referrer-policy',\n      description: 'Referrer Policy is a new header that allows a site to control how much information the browser includes with navigations away from a document and should be set by all sites.'\n    },\n    {\n      name: 'x-content-type-options',\n      description: 'X-Content-Type-Options stops a browser from trying to MIME-sniff the content type and forces it to stick with the declared content-type. The only valid value for this header is \"X-Content-Type-Options: nosniff\".'\n    },\n    {\n      name: 'x-frame-options',\n      description: 'X-Frame-Options tells the browser whether you want to allow your site to be framed or not. By preventing a browser from framing your site you can defend against attacks like clickjacking.'\n    },\n    {\n      name: 'report-to',\n      description: 'Report-To enables the Reporting API. This allows a website to collect reports from the browser about various errors that may occur. You can sign up for a free account on Report URI to collect these reports.'\n    },\n    {\n      name: 'nel',\n      description: 'Network Error Logging is a new header that instructs the browser to send reports during various network or application errors. You can sign up for a free account on Report URI to collect these reports.'\n    },\n    {\n      name: 'server',\n      description: 'Server value has been changed. Typically you will see values like \"Microsoft-IIS/8.0\" or \"nginx 1.7.2\".'\n    }\n  ];\n  \n  let rows = '';\n  \n  for (const header of headers) {\n    const isSecurityHeader = ['content-security-policy', 'strict-transport-security', 'x-content-type-options', 'x-frame-options', 'referrer-policy', 'permissions-policy'].includes(header.name);\n    const headerColor = isSecurityHeader ? '#27AE60' : '#3498DB';\n    \n    rows += `\n      <tr>\n        <td style=\"padding: 8px; border-bottom: 1px solid #eee; color: ${headerColor}; font-weight: bold;\">${header.name}</td>\n        <td style=\"padding: 8px; border-bottom: 1px solid #eee;\">${header.description}</td>\n      </tr>\n    `;\n  }\n  \n  return `\n    <table style=\"width: 100%; border-collapse: collapse; margin-top: 10px;\">\n      <tbody>\n        ${rows}\n      </tbody>\n    </table>\n  `;\n}\n\nfunction formatSecurityGrade() {\n  const gradeColors = {\n    'A+': '#27AE60',\n    'A': '#27AE60',\n    'A-': '#27AE60',\n    'B+': '#3498DB',\n    'B': '#3498DB',\n    'B-': '#3498DB',\n    'C+': '#F39C12',\n    'C': '#F39C12',\n    'C-': '#F39C12',\n    'D+': '#E74C3C',\n    'D': '#E74C3C',\n    'D-': '#E74C3C',\n    'F': '#E74C3C'\n  };\n  \n  return `<div class=\"grade\" style=\"font-size: 64px; font-weight: bold; width: 100px; height: 100px; line-height: 100px; text-align: center; background-color: ${gradeColors[auditData.grade] || '#E74C3C'}; color: white; border-radius: 5px; margin: 0 auto;\">${auditData.grade}</div>`;\n}\n\nfunction formatCriticalVulnerabilities() {\n  if (!auditData.vulnOutput || auditData.vulnOutput.trim() === '') {\n    return '<p>No vulnerabilities detected.</p>';\n  }\n\n  try {\n    const vuln = auditData.vulnOutput.trim();\n    let html = '';\n    const renderedTitles = new Set();\n\n    // Match sections like ## Category (e.g., ## Critical Vulnerabilities)\n    const categories = vuln.split(/(?=^##\\s+)/gm).filter(Boolean);\n\n    for (const categoryBlock of categories) {\n      const categoryMatch = categoryBlock.match(/^##\\s+(.*)/);\n      const categoryTitle = categoryMatch?.[1]?.trim() || 'Uncategorized';\n\n      // Find numbered items: 1. **Title**\n      const vulns = categoryBlock.split(/(?=^\\d+\\.\\s+\\*\\*)/gm).filter(Boolean);\n\n      for (const vulnBlock of vulns) {\n        const titleMatch = vulnBlock.match(/^\\d+\\.\\s+\\*\\*(.*?)\\*\\*/);\n        const title = titleMatch?.[1]?.trim() || 'Unnamed Vulnerability';\n        const key = `${categoryTitle}::${title}`.toLowerCase();\n        if (renderedTitles.has(key)) continue;\n\n        const descriptionMatch = vulnBlock.match(/\\*\\*Description\\*\\*:?\\s*([\\s\\S]*?)(?=\\n\\*\\*|\\n$)/i);\n        const impactMatch = vulnBlock.match(/\\*\\*(?:Impact|Potential Impact)\\*\\*:?\\s*([\\s\\S]*?)(?=\\n\\*\\*|\\n$)/i);\n        const recommendationMatch = vulnBlock.match(/\\*\\*(?:Recommendation|Mitigation|Fix)\\*\\*:?\\s*([\\s\\S]*?)(?=\\n\\*\\*|\\n$)/i);\n\n        const description = descriptionMatch?.[1]?.trim() || '';\n        const impact = impactMatch?.[1]?.trim() || '';\n        const recommendation = recommendationMatch?.[1]?.trim() || '';\n\n        if (description || impact || recommendation) {\n          html += `\n            <div style=\"border-left: 4px solid #E74C3C; padding: 10px; margin-bottom: 15px;\">\n              <div style=\"font-weight: bold; color: #E74C3C;\">${title}</div>\n              ${description ? `<div style=\"margin-top: 5px;\">${description}</div>` : ''}\n              ${impact ? `<div style=\"margin-top: 5px; font-style: italic; color: #7F8C8D;\">Impact: ${impact}</div>` : ''}\n              ${recommendation ? `<div style=\"margin-top: 5px;\"><strong>Recommendation:</strong> ${recommendation}</div>` : ''}\n            </div>`;\n          renderedTitles.add(key);\n        }\n      }\n    }\n\n    return html || '<p>No vulnerabilities parsed from output.</p>';\n  } catch (e) {\n    console.error('Error in formatCriticalVulnerabilities:', e);\n    return `<p>Error processing vulnerabilities: ${e.message}</p>`;\n  }\n}\n\n\n// Generate all security header badges\nfunction generateAllHeaderBadges() {\n  // Only include the necessary security headers\n  const securityHeaders = [\n    'Content-Security-Policy',\n    'Strict-Transport-Security',\n    'X-Content-Type-Options',\n    'X-Frame-Options',\n    'Referrer-Policy',\n    'Permissions-Policy'\n  ];\n  \n  let badges = '';\n  securityHeaders.forEach(header => {\n                      \n    const isWarning = header === 'Strict-Transport-Security' &&\n                  auditData.headerStatus?.[header]?.value &&\n                  parseInt(auditData.headerStatus[header].value.match(/max-age=(\\d+)/)?.[1] || 0) < 2592000;\n    \n    badges += createHeaderBadge(header, isWarning);\n  });\n  \n  return badges;\n}\n\n<!-- Modify the HTML to directly access auditData.originalHeaders or allHeaders -->\nconst html = `<!DOCTYPE html>\n<html>\n<head>\n    <meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n    <title>Website Security Audit Report</title>\n    <style>\n        body { font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f9f9f9; }\n        .container { max-width: 950px; margin: 0 auto; }\n        .header { background-color: #2c3e50; color: white; padding: 25px 20px; text-align: center; }\n        .header h1 { color: white; font-size: 28px; margin: 0; text-shadow: 1px 1px 2px rgba(0,0,0,0.5); }\n        .content { padding: 20px; }\n        .summary-box { background-color: #EBF5FB; padding: 15px; margin-bottom: 20px; border-radius: 5px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }\n        .warning-box { background-color: #FEF5E7; padding: 15px; margin-bottom: 20px; border-radius: 5px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }\n        .headers-box { background-color: #F5F7FA; padding: 15px; margin-bottom: 20px; border-radius: 5px; }\n        .findings-box { background-color: white; padding: 15px; margin-bottom: 20px; border-radius: 5px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }\n        .raw-headers-box { background-color: #F5F7FA; padding: 15px; margin-bottom: 20px; border-radius: 5px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }\n        .additional-info-box { background-color: #F5F7FA; padding: 15px; margin-bottom: 20px; border-radius: 5px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }\n        .details-table { width: 100%; border-collapse: collapse; }\n        .details-table th { text-align: left; padding: 8px; background-color: #f2f2f2; }\n        .details-table td { padding: 8px; border-bottom: 1px solid #eee; }\n        .header-badges { margin-top: 10px; }\n        h1, h2, h3 { color: #2c3e50; }\n        .critical-item { border-left: 4px solid #E74C3C; padding: 10px; margin-bottom: 15px; }\n        .critical-title { font-weight: bold; color: #E74C3C; }\n        .config-item { border-left: 4px solid #3498DB; padding: 10px; margin-bottom: 15px; }\n        .config-title { font-weight: bold; color: #3498DB; }\n        pre { background-color: #f8f9fa; padding: 10px; border-radius: 5px; overflow-x: auto; font-family: monospace; margin-top: 5px; }\n    </style>\n</head>\n<body>\n    <div class=\"container\">\n        <!-- Report Header -->\n        <div class=\"header\">\n            <h1 style=\"color: white; text-shadow: 1px 1px 2px rgba(0,0,0,0.5);\">Website Security Audit Report</h1>\n        </div>\n        \n        <div class=\"content\">\n            <!-- Security Report Summary -->\n            <div class=\"summary-box\">\n                <h2>Security Report Summary</h2>\n                <table style=\"width: 100%;\">\n                    <tr>\n                        <td style=\"width: 120px;\" valign=\"top\">\n                            ${formatSecurityGrade()}\n                        </td>\n                        <td valign=\"top\">\n                            <table style=\"width: 100%;\">\n                                <tr>\n                                    <td><strong>Site:</strong></td>\n                                    <td><a href=\"${auditData.url}\" style=\"color: #3498db;\">${auditData.url}</a></td>\n                                </tr>\n                                <tr>\n                                    <td><strong>Report Time:</strong></td>\n                                    <td>${auditData.timestamp}</td>\n                                </tr>\n                                <tr>\n                                    <td valign=\"top\"><strong>Headers:</strong></td>\n                                    <td>\n                                        <div class=\"header-badges\">\n                                            ${generateAllHeaderBadges()}\n                                        </div>\n                                    </td>\n                                </tr>\n                                <tr>\n                                    <td><strong>Critical Issues:</strong></td>\n                                    <td>${auditData.criticalCount || 0}</td>\n                                </tr>\n                                <tr>\n                                    <td><strong>Warnings:</strong></td>\n                                    <td>${auditData.warningCount || 0}</td>\n                                </tr>\n                            </table>\n                        </td>\n                    </tr>\n                </table>\n            </div>\n\n            <!-- Warnings Section -->\n            <div class=\"warning-box\">\n                <h2>Warnings</h2>\n                ${formatWarningsSection()}\n            </div>\n\n            <!-- Raw Headers Section -->\n            <div class=\"raw-headers-box\">\n                <h2>Raw Headers</h2>\n                ${formatDetailedRawHeaders()}\n            </div>\n\n            <!-- Security Findings -->\n            <div class=\"findings-box\">\n                <h2>Security Findings</h2>\n                \n                <!-- Vulnerabilities -->\n                <h3>Vulnerabilities</h3>\n                ${formatCriticalVulnerabilities()}\n                \n                <!-- Configuration Issues -->\n                <h3>Configuration Issues</h3>\n                ${formatConfigurationIssues()}\n            </div>\n            \n            <div class=\"additional-info-box\">\n              <h2>Additional Information</h2>\n              ${formatAdditionalInfo()}\n            </div>\n            \n            <!-- Implementation Guide -->\n            <div class=\"findings-box\">\n                <h2>Implementation Guide</h2>\n                <p>This report highlights security issues detected through client-side analysis. For a comprehensive security assessment, consider engaging a professional penetration tester.</p>\n                \n                <div style=\"background-color: #eafaf1; padding: 15px; margin-top: 15px; border-left: 4px solid #2ecc71; border-radius: 3px;\">\n                    <p><strong>To implement the fixes above:</strong></p>\n                    <ol style=\"padding-left: 20px; margin-top: 10px;\">\n                        <li>Work with your development team to address each issue in order of criticality</li>\n                        <li>Retest after implementing each fix</li>\n                        <li>Consider implementing a web application firewall for additional protection</li>\n                    </ol>\n                </div>\n            </div>\n            \n            <!-- Footer -->\n            <div style=\"text-align: center; padding: 20px; font-size: 12px; color: #777;\">\n                <p>This report was automatically generated and represents an automated assessment of publicly accessible aspects of your website. For a more comprehensive security assessment, consider engaging with a professional security consultant.</p>\n                <p>&copy; 2025 Website Security Scanner | Generated on ${auditData.timestamp}</p>\n            </div>\n        </div>\n    </div>\n</body>\n</html>`;\n\nreturn [{\n  json: {\n    ...items[0].json,\n    emailHtml: html\n  }\n}];"
      },
      "typeVersion": 2
    }
  ],
  "pinData": {},
  "connections": {
    "Scrape Website": {
      "main": [
        [
          {
            "node": "Security Vulnerabilities Audit",
            "type": "main",
            "index": 0
          },
          {
            "node": "Extract Headers for Debug",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "convert to HTML": {
      "main": [
        [
          {
            "node": "Send Security Report",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Landing Page Url": {
      "main": [
        [
          {
            "node": "Scrape Website",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Process Audit Results": {
      "main": [
        [
          {
            "node": "convert to HTML",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Merge Security Results": {
      "main": [
        [
          {
            "node": "Aggregate Audit Results",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Aggregate Audit Results": {
      "main": [
        [
          {
            "node": "Process Audit Results",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Content Analysis": {
      "ai_languageModel": [
        [
          {
            "node": "Security Vulnerabilities Audit",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Headers Analysis": {
      "ai_languageModel": [
        [
          {
            "node": "Security Configuration Audit",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Extract Headers for Debug": {
      "main": [
        [
          {
            "node": "Security Configuration Audit",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Security Configuration Audit": {
      "main": [
        [
          {
            "node": "Merge Security Results",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Security Vulnerabilities Audit": {
      "main": [
        [
          {
            "node": "Merge Security Results",
            "type": "main",
            "index": 1
          }
        ]
      ]
    }
  }
}
```

<a id="template-1046"></a>

## Template 1046 - Enriquecimento de leads imobiliários

- **Nome:** Enriquecimento de leads imobiliários
- **Descrição:** Automatiza a busca, filtragem e enriquecimento de leads imobiliários, obtendo contatos de proprietários e exportando os resultados para CRM e relatório em Excel.
- **Funcionalidade:** • Gatilhos agendado e manual: Permite execução diária automática ou disparo manual sob demanda.
• Configuração de parâmetros de busca: Define critérios de pesquisa (local, tipo de propriedade, faixa de valor, percentual de equity, status, limite).
• Consulta à API de propriedades: Realiza requisição para obter propriedades que atendam aos critérios configurados.
• Filtragem e pontuação de propriedades: Aplica filtros adicionais (proprietário ausente, tempo de posse, sem vendas recentes) e calcula pontuação de lead com base em equity, tempo de posse e inadimplência fiscal.
• Skip trace de contatos do proprietário: Executa consulta para enriquecer cada propriedade com e-mail e telefones de proprietário.
• Formatação dos dados de lead: Normaliza e estrutura dados de propriedade e contato para CRM e relatórios, incluindo informações adicionais e data de inclusão.
• Exportação para Excel: Gera arquivo .xlsx com os leads e detalhes, nomeado com a data de execução.
• Inserção no CRM: Envia leads formatados para o sistema CRM configurado.
• Notificação por e-mail: Envia um e-mail resumo com o relatório anexado.
• Sumário de resultados: Calcula e registra métricas básicas da execução (total de leads, maior pontuação, data).
- **Ferramentas:** • BatchData API: Serviço externo utilizado para buscar propriedades e executar skip-trace para obter informações de proprietários.
• HubSpot: CRM usado para inserir e gerenciar os leads enriquecidos.
• Serviço de envio de e-mail/SMTP: Responsável por enviar notificações e entregar o relatório por e-mail.
• Geração de planilhas Excel (.xlsx): Biblioteca/serviço que cria o arquivo de relatório em formato Excel.

## Fluxo visual

```mermaid
flowchart LR
    N1["When clicking 'Execute Workflow'"]
    N2["Daily Schedule"]
    N3["Search Properties API"]
    N4["Configure Search Parameters"]
    N5["Filter Property Results"]
    N6["Get Owner Contact Info"]
    N7["Format Lead Data"]
    N8["Create Excel Spreadsheet"]
    N9["Push to CRM"]
    N10["Email Notification"]
    N11["Summarize Results"]
    N12["Sticky Note - Workflow Overview"]
    N13["Sticky Note - Triggers"]
    N14["Sticky Note - Property Search"]
    N15["Sticky Note - Data Processing"]
    N16["Sticky Note - Output"]

    N2 --> N4
    N7 --> N8
    N7 --> N9
    N7 --> N11
    N11 --> N10
    N3 --> N5
    N6 --> N7
    N5 --> N6
    N8 --> N10
    N4 --> N3
    N1 --> N4
```

## Fluxo (.json) :

```json
{
  "id": "RGVS0tHJV7Wh6aX4",
  "meta": {
    "instanceId": "bb9853d4d7d87207561a30bc6fe4ece20b295264f7d27d4a62215de2f3846a56"
  },
  "name": "Property Lead Contact Enrichment from CRM",
  "tags": [],
  "nodes": [
    {
      "id": "518b14de-23b9-4821-930c-8fa55eb4cfb4",
      "name": "When clicking \"Execute Workflow\"",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        -340,
        280
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "939df2a3-f6dd-40c9-a01a-460923a332a6",
      "name": "Daily Schedule",
      "type": "n8n-nodes-base.scheduleTrigger",
      "position": [
        -340,
        100
      ],
      "parameters": {
        "rule": {
          "interval": [
            {}
          ]
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "3228372f-ac40-4898-8bf5-09a4f37fde85",
      "name": "Search Properties API",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        320,
        260
      ],
      "parameters": {
        "url": "https://api.batchdata.com/api/v1/properties/search",
        "method": "POST",
        "options": {},
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth"
      },
      "typeVersion": 4.1
    },
    {
      "id": "0aa1fb95-66c8-4b61-81f5-04b37e5c1185",
      "name": "Configure Search Parameters",
      "type": "n8n-nodes-base.set",
      "position": [
        40,
        240
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "search_parameters",
              "value": "={ \"location\": { \"city\": \"Austin\", \"state\": \"TX\" }, \"propertyType\": \"single_family\", \"value\": { \"min\": 200000, \"max\": 500000 }, \"status\": \"distressed\", \"equity\": { \"min\": 30 }, \"limit\": 50 }"
            }
          ]
        },
        "options": {}
      },
      "typeVersion": 2
    },
    {
      "id": "052b357b-a374-4e0c-ab98-67e79ed8cf2b",
      "name": "Filter Property Results",
      "type": "n8n-nodes-base.code",
      "position": [
        540,
        260
      ],
      "parameters": {
        "jsCode": "// Process batch property results and filter according to criteria\nconst results = $input.all()[0].json.results || [];\n\n// Filter to find matching properties\nconst filteredProperties = results.filter(property => {\n  // Example filtering criteria - customize as needed\n  // Only include properties where:\n  // 1. Owner doesn't live at the property (absentee)\n  // 2. Property has been owned for 5+ years\n  // 3. No sales in the last 3 years\n  \n  const isAbsentee = property.owner_occupied === false;\n  \n  // Calculate years of ownership if purchase date exists\n  let yearsOwned = 0;\n  if (property.last_sale_date) {\n    const purchaseDate = new Date(property.last_sale_date);\n    const currentDate = new Date();\n    yearsOwned = currentDate.getFullYear() - purchaseDate.getFullYear();\n  }\n  \n  // Check if no recent sales (last 3 years)\n  let noRecentSales = true;\n  if (property.last_sale_date) {\n    const lastSale = new Date(property.last_sale_date);\n    const threeYearsAgo = new Date();\n    threeYearsAgo.setFullYear(threeYearsAgo.getFullYear() - 3);\n    noRecentSales = lastSale < threeYearsAgo;\n  }\n  \n  return isAbsentee && yearsOwned >= 5 && noRecentSales;\n});\n\n// Add relevant score to each property\nconst scoredProperties = filteredProperties.map(property => {\n  // Create a simple scoring system from 0-100\n  // This helps prioritize the best leads\n  let score = 50; // Base score\n  \n  // Increase score for properties with more equity\n  if (property.equity_percentage) {\n    score += Math.min(property.equity_percentage / 2, 25);\n  }\n  \n  // Increase score for longer ownership\n  if (property.last_sale_date) {\n    const purchaseDate = new Date(property.last_sale_date);\n    const currentDate = new Date();\n    const yearsOwned = currentDate.getFullYear() - purchaseDate.getFullYear();\n    score += Math.min(yearsOwned, 15);\n  }\n  \n  // Increase score for tax delinquency\n  if (property.tax_delinquent) {\n    score += 10;\n  }\n  \n  return { ...property, lead_score: Math.round(score) };\n});\n\n// Sort by score descending\nscoredProperties.sort((a, b) => b.lead_score - a.lead_score);\n\n// Return the filtered and scored properties\nreturn scoredProperties.map(property => {\n  return {\n    json: property\n  };\n});"
      },
      "typeVersion": 2
    },
    {
      "id": "2c183cc1-06a1-4528-82c3-df2585df58eb",
      "name": "Get Owner Contact Info",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        760,
        260
      ],
      "parameters": {
        "url": "https://api.batchdata.com/api/v1/property/skip-trace",
        "method": "POST",
        "options": {},
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth"
      },
      "typeVersion": 4.1
    },
    {
      "id": "2fe0aef9-30d2-4c30-9029-571f3b4c8ca9",
      "name": "Format Lead Data",
      "type": "n8n-nodes-base.code",
      "position": [
        960,
        260
      ],
      "parameters": {
        "jsCode": "// Process and format the property data with owner contact info\nreturn $input.all().map(item => {\n  const property = item.json;\n  const skipTraceData = property.skip_trace_data || {};\n  const ownerInfo = property.owner_info || {};\n  \n  return {\n    json: {\n      // Property Information\n      property_id: property.property_id,\n      address: property.address,\n      city: property.city,\n      state: property.state,\n      zip: property.zip,\n      property_type: property.property_type,\n      beds: property.beds,\n      baths: property.baths,\n      sqft: property.building_sqft,\n      lot_size: property.lot_size,\n      year_built: property.year_built,\n      last_sale_date: property.last_sale_date,\n      last_sale_price: property.last_sale_price,\n      estimated_value: property.estimated_value,\n      estimated_equity: property.estimated_equity,\n      equity_percentage: property.equity_percentage,\n      lead_score: property.lead_score,\n      \n      // Owner Information\n      owner_name: ownerInfo.full_name || `${ownerInfo.first_name || ''} ${ownerInfo.last_name || ''}`.trim(),\n      owner_mailing_address: ownerInfo.mailing_address,\n      owner_mailing_city: ownerInfo.mailing_city,\n      owner_mailing_state: ownerInfo.mailing_state,\n      owner_mailing_zip: ownerInfo.mailing_zip,\n      \n      // Contact Info from Skip Trace\n      email: skipTraceData.email,\n      phone: skipTraceData.phone_number,\n      mobile: skipTraceData.mobile_number,\n      alternate_phone: skipTraceData.alternate_phone,\n      \n      // Additional Details\n      absentee_owner: property.owner_occupied === false ? 'Yes' : 'No',\n      tax_delinquent: property.tax_delinquent ? 'Yes' : 'No',\n      years_owned: property.years_owned,\n      lead_source: 'BatchData Property Search',\n      date_added: new Date().toISOString().split('T')[0]\n    }\n  };\n});"
      },
      "typeVersion": 2
    },
    {
      "id": "013469c2-1e83-44e0-b078-c0b3d052a2c5",
      "name": "Create Excel Spreadsheet",
      "type": "n8n-nodes-base.spreadsheetFile",
      "position": [
        1280,
        160
      ],
      "parameters": {
        "options": {
          "fileName": "Property_Leads_{{ $now.format('YYYY-MM-DD') }}.xlsx",
          "headerRow": true
        },
        "operation": "toFile",
        "fileFormat": "xlsx"
      },
      "typeVersion": 2
    },
    {
      "id": "954c492a-7da2-4902-99ab-318d4ea6e333",
      "name": "Push to CRM",
      "type": "n8n-nodes-base.hubspot",
      "position": [
        1280,
        540
      ],
      "parameters": {
        "options": {},
        "additionalFields": {}
      },
      "typeVersion": 2
    },
    {
      "id": "61bfd72b-8971-4298-8d2a-09baea403956",
      "name": "Email Notification",
      "type": "n8n-nodes-base.emailSend",
      "position": [
        1520,
        300
      ],
      "webhookId": "e9459278-1cd9-47bb-bffd-88380d297217",
      "parameters": {
        "options": {},
        "subject": "Property Lead Report - {{ $now.format('YYYY-MM-DD') }}",
        "toEmail": "your-email@yourdomain.com",
        "fromEmail": "no-reply@yourdomain.com"
      },
      "typeVersion": 2.1
    },
    {
      "id": "a79a0618-ac63-4aaf-8337-b9ccc5940eef",
      "name": "Summarize Results",
      "type": "n8n-nodes-base.code",
      "position": [
        1280,
        360
      ],
      "parameters": {
        "jsCode": "// Summarize the results of the property lead search\nconst leads = $input.all();\nconst totalLeads = leads.length;\n\n// Calculate the highest lead score\nlet highestScore = 0;\nif (totalLeads > 0) {\n  highestScore = Math.max(...leads.map(item => item.json.lead_score || 0));\n}\n\n// Return a summary object\nreturn {\n  json: {\n    total_leads: totalLeads,\n    highest_score: highestScore,\n    execution_date: new Date().toISOString(),\n    success: true\n  }\n};"
      },
      "typeVersion": 2
    },
    {
      "id": "cf6bbc2b-4892-4612-aee9-7f255f627a67",
      "name": "Sticky Note - Workflow Overview",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -420,
        -520
      ],
      "parameters": {
        "width": 800,
        "height": 280,
        "content": "# Property Lead Automation Workflow\n\nThis workflow automatically searches for potential real estate leads based on configured criteria, obtains owner contact information through skip tracing, and pushes the leads to your CRM. It can be run manually or scheduled to run daily.\n\n## Steps: Property Search → Filter Results → Skip Trace → Format Data → Export (Excel & CRM)"
      },
      "typeVersion": 1
    },
    {
      "id": "ff155460-3f4e-44e8-aac7-4b84dff2dceb",
      "name": "Sticky Note - Triggers",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -420,
        -160
      ],
      "parameters": {
        "color": 2,
        "width": 320,
        "height": 620,
        "content": "## Workflow Triggers\n\nThis workflow can be triggered in two ways:\n\n1. **Scheduled Trigger** - Runs automatically every day at the specified time\n\n2. **Manual Trigger** - Run the workflow on-demand by clicking Execute"
      },
      "typeVersion": 1
    },
    {
      "id": "8c127497-0dc4-428d-a946-14c10b9572cb",
      "name": "Sticky Note - Property Search",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -80,
        -180
      ],
      "parameters": {
        "color": 4,
        "width": 320,
        "height": 650,
        "content": "## Search Configuration\n\nConfigure your property search criteria including:\n\n- Location (city, state, zip)\n- Property type\n- Value range\n- Equity percentage\n- Owner status\n- And more\n\nEdit the 'search_parameters' in the Set node to customize your search criteria."
      },
      "typeVersion": 1
    },
    {
      "id": "20ad7c5e-5d73-4b43-b5b0-6c9eaae18400",
      "name": "Sticky Note - Data Processing",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        260,
        -180
      ],
      "parameters": {
        "color": 5,
        "width": 880,
        "height": 660,
        "content": "## Property Data Processing\n\n1. **Search Properties API** - Connect to BatchData to search for properties\n\n2. **Filter Property Results** - Apply additional filtering logic and calculate lead scores based on factors like:\n   - Equity percentage\n   - Years of ownership\n   - Owner occupancy status\n   - Tax delinquency\n   - Recent sales activity\n\n3. **Get Owner Contact Info** - Skip trace each property to find owner contact details\n\n4. **Format Lead Data** - Structure the data for CRM and reporting"
      },
      "typeVersion": 1
    },
    {
      "id": "a0254233-a0af-43b2-8258-0820d8fdd49d",
      "name": "Sticky Note - Output",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1180,
        -180
      ],
      "parameters": {
        "color": 6,
        "width": 560,
        "height": 920,
        "content": "## Lead Output Options\n\n1. **Create Excel Spreadsheet** - Generates an Excel file with all property leads and details\n\n2. **Push to CRM** - Adds leads to your CRM system (HubSpot in this example, but can be changed to Salesforce, Zoho, etc.)\n\n3. **Email Notification** - Sends a summary email with the Excel file attached\n\n4. **Summarize Results** - Provides a summary of the execution results"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "ff401fba-f56d-4d22-b259-d23a4e141a98",
  "connections": {
    "Daily Schedule": {
      "main": [
        [
          {
            "node": "Configure Search Parameters",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Format Lead Data": {
      "main": [
        [
          {
            "node": "Create Excel Spreadsheet",
            "type": "main",
            "index": 0
          },
          {
            "node": "Push to CRM",
            "type": "main",
            "index": 0
          },
          {
            "node": "Summarize Results",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Summarize Results": {
      "main": [
        [
          {
            "node": "Email Notification",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Search Properties API": {
      "main": [
        [
          {
            "node": "Filter Property Results",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Owner Contact Info": {
      "main": [
        [
          {
            "node": "Format Lead Data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Filter Property Results": {
      "main": [
        [
          {
            "node": "Get Owner Contact Info",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Create Excel Spreadsheet": {
      "main": [
        [
          {
            "node": "Email Notification",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Configure Search Parameters": {
      "main": [
        [
          {
            "node": "Search Properties API",
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
            "node": "Configure Search Parameters",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-1047"></a>

## Template 1047 - Criar campanha Emelia e adicionar contato

- **Nome:** Criar campanha Emelia e adicionar contato
- **Descrição:** Cria uma campanha e adiciona um contato, encadeando o ID da campanha criada para operações subsequentes.
- **Funcionalidade:** • Criação de campanha: Cria uma nova campanha com o nome "n8n-docs".
• Adição de contato: Adiciona um contato com email e nome a uma campanha específica.
• Encadeamento de dados: Utiliza o ID da campanha recém-criada para alimentar etapas seguintes do fluxo.
- **Ferramentas:** • Emelia: Serviço/API para criação e gerenciamento de campanhas de email e contatos.

## Fluxo visual

```mermaid
flowchart LR
    N1["Emelia"]
    N2["Emelia1"]
    N3["Emelia2"]

    N1 --> N2
    N2 --> N3
```

## Fluxo (.json) :

```json
{
  "nodes": [
    {
      "name": "Emelia",
      "type": "n8n-nodes-base.emelia",
      "position": [
        530,
        310
      ],
      "parameters": {
        "operation": "create",
        "campaignName": "n8n-docs"
      },
      "credentials": {
        "emeliaApi": "Emelia API Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Emelia1",
      "type": "n8n-nodes-base.emelia",
      "position": [
        730,
        310
      ],
      "parameters": {
        "operation": "addContact",
        "campaignId": "603dfd70cbe34c3c9730fd09",
        "contactEmail": "email@example.com",
        "additionalFields": {
          "firstName": "NAME"
        }
      },
      "credentials": {
        "emeliaApi": "Emelia API Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Emelia2",
      "type": "n8n-nodes-base.emelia",
      "position": [
        930,
        310
      ],
      "parameters": {
        "campaignId": "={{$node[\"Emelia\"].json[\"_id\"]}}"
      },
      "credentials": {
        "emeliaApi": "Emelia API Credentials"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Emelia": {
      "main": [
        [
          {
            "node": "Emelia1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Emelia1": {
      "main": [
        [
          {
            "node": "Emelia2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-1048"></a>

## Template 1048 - Bot Telegram integrado com NeurochainAI (texto e imagem)

- **Nome:** Bot Telegram integrado com NeurochainAI (texto e imagem)
- **Descrição:** Fluxo que recebe mensagens de um bot Telegram, envia prompts à API da NeurochainAI para geração de texto ou imagens e retorna as respostas ao usuário, com tratamento de erros e indicações de processamento.
- **Funcionalidade:** • Detecção de entrada: Captura mensagens enviadas ao bot e identifica comandos, menções ou mensagens diretas.
• Roteamento por tipo de entrada: Diferencia comandos com prefixo (/flux), menções ao bot e DMs para acionar fluxos apropriados.
• Limpeza do prompt: Remove o prefixo '/flux' e espaços extras para obter o prompt limpo.
• Indicação de processamento: Envia ação de "digitando" para informar que o pedido está sendo processado.
• Geração de texto via API: Envia o prompt para a API de texto da NeurochainAI (modelos configuráveis) e retorna a resposta ao chat.
• Geração de imagem via API: Envia prompts para o endpoint de geração de imagens da NeurochainAI (com parâmetros como tamanho, qualidade, seed aleatório) e recupera a imagem gerada.
• Envio de mídia ao usuário: Faz o download da imagem gerada e envia como foto ao chat com legenda contendo o prompt.
• Gerenciamento de mensagens temporárias: Publica mensagens de status e as deleta após receber o resultado para manter o chat limpo.
• Tratamento de erros e re-tentativas: Detecta respostas de erro da API, notifica o usuário, oferece botão de retry e exibe mensagens específicas para prompts inválidos ou curtos.
• Mensagens de fallback: Informa o usuário quando não há resposta do worker ou quando o prompt é considerado curto demais.
- **Ferramentas:** • Telegram Bot API: Plataforma para receber mensagens dos usuários, enviar ações de chat (typing), enviar/editar/excluir mensagens e enviar mídias (fotos).
• NeurochainAI Inference API: Serviço de inferência para geração de texto e imagens (endpoints para tarefas de texto e TTI), que aceita modelos configuráveis (ex.: Meta-Llama, Mistral, flux1) e retorna respostas ou URLs de imagens geradas.

## Fluxo visual

```mermaid
flowchart LR
    N1["Telegram Trigger"]
    N2["Code"]
    N3["HTTP Request3"]
    N4["Telegram2"]
    N5["Telegram1"]
    N6["Telegram4"]
    N7["Telegram3"]
    N8["Telegram5"]
    N9["Telegram6"]
    N10["Telegram7"]
    N11["NeurochainAI - REST API"]
    N12["TYPING - ACTION"]
    N13["AI Response"]
    N14["No response"]
    N15["Prompt too short"]
    N16["Sticky Note"]
    N17["Switch2"]
    N18["Sticky Note1"]
    N19["Sticky Note2"]
    N20["Sticky Note3"]
    N21["Sticky Note4"]
    N22["Sticky Note5"]
    N23["Code1"]
    N24["Sticky Note6"]
    N25["Sticky Note7"]
    N26["Switch"]
    N27["Sticky Note8"]
    N28["NeurochainAI - Flux"]
    N29["Switch1"]

    N2 --> N3
    N23 --> N4
    N26 --> N23
    N26 --> N12
    N29 --> N9
    N29 --> N7
    N17 --> N14
    N17 --> N15
    N5 --> N6
    N4 --> N28
    N7 --> N8
    N9 --> N10
    N3 --> N5
    N12 --> N11
    N1 --> N26
    N28 --> N2
    N28 --> N29
    N11 --> N13
    N11 --> N17
```

## Fluxo (.json) :

```json
{
  "id": "RLWjEhY8L4TORAIj",
  "meta": {
    "instanceId": "36399efc72267ed21ee0d3747f5abdd0ee139cb67749ff919ff09fcd65230079",
    "templateCredsSetupCompleted": true
  },
  "name": "NeurochainAI Basic API Integration",
  "tags": [],
  "nodes": [
    {
      "id": "da34bd1a-4e4e-4133-acad-939d0cc96596",
      "name": "Telegram Trigger",
      "type": "n8n-nodes-base.telegramTrigger",
      "position": [
        -1740,
        880
      ],
      "webhookId": "05885608-5344-4dcf-81ad-4550b9a01241",
      "parameters": {
        "updates": [
          "*"
        ],
        "additionalFields": {}
      },
      "credentials": {
        "telegramApi": {
          "id": "VPtf3hBnwGucAQtu",
          "name": "TEMPLATE"
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "3b3f4b00-6b3b-4346-8fcc-7ab75bcfe838",
      "name": "Code",
      "type": "n8n-nodes-base.code",
      "notes": "Extract the URL from the previous node",
      "position": [
        80,
        260
      ],
      "parameters": {
        "jsCode": "// O valor vem como um array com uma string, então precisamos pegar o primeiro item do array\nconst rawUrl = $json.choices[0].text;\n\n// Remover colchetes e aspas (se existirem) e pegar o primeiro elemento do array\nconst imageUrl = JSON.parse(rawUrl)[0];\n\nreturn {\n json: {\n imageUrl: imageUrl\n }\n};"
      },
      "notesInFlow": true,
      "typeVersion": 2
    },
    {
      "id": "ccb91a15-96b5-42aa-a6ae-ff7ae79d1e8f",
      "name": "HTTP Request3",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        240,
        260
      ],
      "parameters": {
        "url": "={{ $json.imageUrl }}",
        "options": {}
      },
      "typeVersion": 4.2
    },
    {
      "id": "588899b6-a68e-407e-b12f-f05c205674c5",
      "name": "Telegram2",
      "type": "n8n-nodes-base.telegram",
      "position": [
        -520,
        500
      ],
      "parameters": {
        "text": "⌛",
        "chatId": "={{ $('Telegram Trigger').item.json.message.chat.id }}",
        "replyMarkup": "inlineKeyboard",
        "additionalFields": {
          "appendAttribution": false,
          "reply_to_message_id": "={{ $('Telegram Trigger').item.json.message.message_id }}"
        }
      },
      "credentials": {
        "telegramApi": {
          "id": "VPtf3hBnwGucAQtu",
          "name": "TEMPLATE"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "e1534b69-d93d-4e8b-a3c4-adbc17c1dacd",
      "name": "Telegram1",
      "type": "n8n-nodes-base.telegram",
      "position": [
        440,
        260
      ],
      "parameters": {
        "chatId": "={{ $('Telegram Trigger').item.json.message.chat.id }}",
        "operation": "sendPhoto",
        "binaryData": true,
        "additionalFields": {
          "caption": "=*Prompt:* `{{ $('Code1').item.json.cleanMessage }}`",
          "parse_mode": "Markdown",
          "reply_to_message_id": "={{ $('Telegram Trigger').item.json.message.message_id }}"
        }
      },
      "credentials": {
        "telegramApi": {
          "id": "VPtf3hBnwGucAQtu",
          "name": "TEMPLATE"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "88ba4ced-bdd0-408e-94e1-9e54ed4d1b5d",
      "name": "Telegram4",
      "type": "n8n-nodes-base.telegram",
      "position": [
        620,
        260
      ],
      "parameters": {
        "chatId": "={{ $('Telegram2').item.json.result.chat.id }}",
        "messageId": "={{ $('Telegram2').item.json.result.message_id }}",
        "operation": "deleteMessage"
      },
      "credentials": {
        "telegramApi": {
          "id": "VPtf3hBnwGucAQtu",
          "name": "TEMPLATE"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "251a026e-ebfa-44f5-9c80-f30e5c142e23",
      "name": "Telegram3",
      "type": "n8n-nodes-base.telegram",
      "position": [
        260,
        700
      ],
      "parameters": {
        "text": "={{ $json.error.message }}",
        "chatId": "={{ $('Telegram Trigger').item.json.message.chat.id }}",
        "replyMarkup": "inlineKeyboard",
        "inlineKeyboard": {
          "rows": [
            {
              "row": {
                "buttons": [
                  {
                    "text": "🔄 Retry",
                    "additionalFields": {
                      "callback_data": "=response= Fluxretry: {{ $('Code1').item.json.cleanMessage }}"
                    }
                  }
                ]
              }
            }
          ]
        },
        "additionalFields": {
          "appendAttribution": false,
          "reply_to_message_id": "={{ $('Telegram Trigger').item.json.message.message_id }}"
        }
      },
      "credentials": {
        "telegramApi": {
          "id": "VPtf3hBnwGucAQtu",
          "name": "TEMPLATE"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "fb71a62a-9cf8-4abf-baa4-885ae4b1a290",
      "name": "Telegram5",
      "type": "n8n-nodes-base.telegram",
      "position": [
        480,
        700
      ],
      "parameters": {
        "chatId": "={{ $('Telegram2').item.json.result.chat.id }}",
        "messageId": "={{ $('Telegram2').item.json.result.message_id }}",
        "operation": "deleteMessage"
      },
      "credentials": {
        "telegramApi": {
          "id": "VPtf3hBnwGucAQtu",
          "name": "TEMPLATE"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "0f9bcdf0-0008-447a-900c-6afe5b9d53fe",
      "name": "Telegram6",
      "type": "n8n-nodes-base.telegram",
      "position": [
        260,
        520
      ],
      "parameters": {
        "text": "=*Prompt too short*",
        "chatId": "={{ $('Telegram Trigger').item.json.message.chat.id }}",
        "replyMarkup": "inlineKeyboard",
        "additionalFields": {
          "parse_mode": "Markdown",
          "appendAttribution": false,
          "reply_to_message_id": "={{ $('Telegram Trigger').item.json.message.message_id }}"
        }
      },
      "credentials": {
        "telegramApi": {
          "id": "VPtf3hBnwGucAQtu",
          "name": "TEMPLATE"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "d805548a-7379-456c-9bc3-f5fafeb86aed",
      "name": "Telegram7",
      "type": "n8n-nodes-base.telegram",
      "position": [
        480,
        520
      ],
      "parameters": {
        "chatId": "={{ $('Telegram2').item.json.result.chat.id }}",
        "messageId": "={{ $('Telegram2').item.json.result.message_id }}",
        "operation": "deleteMessage"
      },
      "credentials": {
        "telegramApi": {
          "id": "VPtf3hBnwGucAQtu",
          "name": "TEMPLATE"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "a3e521a3-aff0-4d31-9a69-626f70f86ae2",
      "name": "NeurochainAI - REST API",
      "type": "n8n-nodes-base.httpRequest",
      "onError": "continueErrorOutput",
      "position": [
        -680,
        1280
      ],
      "parameters": {
        "url": "https://ncmb.neurochain.io/tasks/message",
        "method": "POST",
        "options": {},
        "jsonBody": "={\n \"model\": \"Meta-Llama-3.1-8B-Instruct-Q6_K.gguf\",\n \"prompt\": \"You must respond directly to the user's message, and the message the user sent you is the following message: {{ $('Telegram Trigger').item.json.message.text }}\",\n \"max_tokens\": 1024,\n \"temperature\": 0.6,\n \"top_p\": 0.95,\n \"frequency_penalty\": 0,\n \"presence_penalty\": 1.1\n}",
        "sendBody": true,
        "sendHeaders": true,
        "specifyBody": "json",
        "headerParameters": {
          "parameters": [
            {
              "name": "Authorization",
              "value": "=Bearer YOUR-API-KEY-HERE"
            },
            {
              "name": "Content-Type",
              "value": "application/json"
            }
          ]
        }
      },
      "typeVersion": 4.2,
      "alwaysOutputData": false
    },
    {
      "id": "5fea3a8b-3e1b-4c69-b734-3f9dc7647e4b",
      "name": "TYPING - ACTION",
      "type": "n8n-nodes-base.telegram",
      "position": [
        -1100,
        1280
      ],
      "parameters": {
        "chatId": "={{ $('Telegram Trigger').item.json.message.chat.id }}",
        "operation": "sendChatAction"
      },
      "credentials": {
        "telegramApi": {
          "id": "VPtf3hBnwGucAQtu",
          "name": "TEMPLATE"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "ca183e3d-2bef-4d80-bbb7-c712a0290b2b",
      "name": "AI Response",
      "type": "n8n-nodes-base.telegram",
      "position": [
        -360,
        1000
      ],
      "parameters": {
        "text": "={{ $json.choices[0].text }}",
        "chatId": "={{ $('Telegram Trigger').item.json.message.chat.id }}",
        "additionalFields": {
          "parse_mode": "Markdown",
          "appendAttribution": false,
          "reply_to_message_id": "={{ $('Telegram Trigger').item.json.message.message_id }}"
        }
      },
      "credentials": {
        "telegramApi": {
          "id": "VPtf3hBnwGucAQtu",
          "name": "TEMPLATE"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "27e65f30-e58e-457d-b3b7-2b74267554e1",
      "name": "No response",
      "type": "n8n-nodes-base.telegram",
      "position": [
        -140,
        1240
      ],
      "parameters": {
        "text": "=*No response from worker*",
        "chatId": "={{ $('Telegram Trigger').item.json.message.chat.id }}",
        "additionalFields": {
          "parse_mode": "Markdown",
          "appendAttribution": false,
          "reply_to_message_id": "={{ $('Telegram Trigger').item.json.message.message_id }}"
        }
      },
      "credentials": {
        "telegramApi": {
          "id": "VPtf3hBnwGucAQtu",
          "name": "TEMPLATE"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "02cf4dfa-558f-4968-ad09-19f1e40735b0",
      "name": "Prompt too short",
      "type": "n8n-nodes-base.telegram",
      "position": [
        -140,
        1400
      ],
      "parameters": {
        "text": "=*Prompt too short*",
        "chatId": "={{ $('Telegram Trigger').item.json.message.chat.id }}",
        "replyMarkup": "inlineKeyboard",
        "additionalFields": {
          "parse_mode": "Markdown",
          "appendAttribution": false,
          "reply_to_message_id": "={{ $('Telegram Trigger').item.json.message.message_id }}"
        }
      },
      "credentials": {
        "telegramApi": {
          "id": "VPtf3hBnwGucAQtu",
          "name": "TEMPLATE"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "943d31e4-3745-49ea-9669-8a560a486cc4",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -400,
        1220
      ],
      "parameters": {
        "color": 3,
        "width": 460.4333621829785,
        "height": 347.9769162173868,
        "content": "## ERROR"
      },
      "typeVersion": 1
    },
    {
      "id": "6b5d142f-8d8c-493f-81e7-cedb4e95cd31",
      "name": "Switch2",
      "type": "n8n-nodes-base.switch",
      "position": [
        -380,
        1380
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
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $json.error.message }}",
                    "rightValue": "=500 - \"{\\\"error\\\":true,\\\"msg\\\":\\\"No response from worker\\\"}\""
                  }
                ]
              }
            },
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
                    "id": "ef851d57-0618-4fe7-8469-a30971a05ee5",
                    "operator": {
                      "type": "string",
                      "operation": "notEquals"
                    },
                    "leftValue": "{{ $json.error.message }}",
                    "rightValue": "400 - \"{\\\"error\\\":true,\\\"msg\\\":\\\"Prompt string is invalid\\\"}\""
                  }
                ]
              }
            }
          ]
        },
        "options": {}
      },
      "typeVersion": 3.2
    },
    {
      "id": "77651cb7-2530-46b2-89eb-7ac07f39a3ba",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -400,
        860
      ],
      "parameters": {
        "color": 4,
        "width": 459.0810102677459,
        "height": 350.68162004785273,
        "content": "## SUCCESS\nThis node will send the AI ​​response directly to the Telegram chat."
      },
      "typeVersion": 1
    },
    {
      "id": "5dce8414-fe7a-450a-a414-553d3e5e01cd",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -830.8527430805248,
        861.5987888475245
      ],
      "parameters": {
        "color": 5,
        "width": 411.78262099325127,
        "height": 705.0354263931183,
        "content": "## HTTP REQUEST\n\nReplace **MODEL** with the desired AI model from the NeurochainAI dashboard.\n\nReplace YOUR-API-KEY-HERE with your actual NeurochainAI API key.\n\n**Models:**\nMeta-Llama-3.1-8B-Instruct-Q8_0.gguf\nMeta-Llama-3.1-8B-Instruct-Q6_K.gguf\nMistral-7B-Instruct-v0.2-GPTQ-Neurochain-custom-io\nMistral-7B-Instruct-v0.2-GPTQ-Neurochain-custom\nMistral-7B-OpenOrca-GPTQ\nMistral-7B-Instruct-v0.1-gguf-q8_0.gguf\nMistral-7B-Instruct-v0.2-GPTQ\ningredient-extractor-mistral-7b-instruct-v0.1-gguf-q8_0.gguf"
      },
      "typeVersion": 1
    },
    {
      "id": "3540e1fa-01f8-4b5e-ad7a-1b1c5cd90d08",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -840,
        220
      ],
      "parameters": {
        "color": 6,
        "width": 236.80242230495116,
        "height": 535.7153791682382,
        "content": "## This node removes the /flux prefix."
      },
      "typeVersion": 1
    },
    {
      "id": "6720b734-c0ae-4c88-adb6-3931467c780d",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        220,
        444
      ],
      "parameters": {
        "color": 3,
        "width": 593.1328365275054,
        "height": 403.9345258807414,
        "content": "## ERROR"
      },
      "typeVersion": 1
    },
    {
      "id": "30332278-399d-4c8f-8470-dfb967764455",
      "name": "Sticky Note5",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -320,
        220
      ],
      "parameters": {
        "color": 5,
        "width": 384.60321058533617,
        "height": 538.7613862505775,
        "content": "## HTTP REQUEST\n\nReplace **MODEL** with the desired AI model from the NeurochainAI dashboard.\n\nReplace YOUR-API-KEY-HERE with your actual NeurochainAI API key.\n\n**Models:**\nsuper-flux1-schnell-gguf\nflux1-schnell-gguf"
      },
      "typeVersion": 1
    },
    {
      "id": "09f17d6a-6229-49ad-b77b-243712552f2b",
      "name": "Code1",
      "type": "n8n-nodes-base.code",
      "position": [
        -780,
        480
      ],
      "parameters": {
        "jsCode": "// Acessa a mensagem original que está em $json.message.text\nconst userMessage = $json.message.text;\n\n// Remover o prefixo '/flux' e qualquer espaço extra após o comando\nconst cleanMessage = userMessage.replace(/^/flux\\s*/, '');\n\n// Retornar a mensagem limpa\nreturn {\n json: {\n cleanMessage: cleanMessage\n }\n};"
      },
      "typeVersion": 2
    },
    {
      "id": "0c809796-9776-4238-94b8-0779ad390bc6",
      "name": "Sticky Note6",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -580,
        220
      ],
      "parameters": {
        "height": 535.7153791682384,
        "content": "## This node sends an emoji to indicate that the prompt is being processed."
      },
      "typeVersion": 1
    },
    {
      "id": "19043710-a61a-46d0-9ab9-bcdf9c94f800",
      "name": "Sticky Note7",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        220,
        80
      ],
      "parameters": {
        "color": 4,
        "width": 596.5768511548468,
        "height": 350.68162004785273,
        "content": "## SUCCESS\nThis node will send the AI ​​response directly to the Telegram chat."
      },
      "typeVersion": 1
    },
    {
      "id": "e5715001-75a3-4da3-84bb-9aad193fe680",
      "name": "Switch",
      "type": "n8n-nodes-base.switch",
      "position": [
        -1420,
        880
      ],
      "parameters": {
        "rules": {
          "values": [
            {
              "outputKey": "Flux",
              "conditions": {
                "options": {
                  "version": 2,
                  "leftValue": "",
                  "caseSensitive": false,
                  "typeValidation": "loose"
                },
                "combinator": "and",
                "conditions": [
                  {
                    "id": "f5df9de6-0650-42e4-9a6e-8d1becf16c51",
                    "operator": {
                      "type": "string",
                      "operation": "startsWith"
                    },
                    "leftValue": "={{ $json.message.text }}",
                    "rightValue": "/flux"
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
                  "caseSensitive": false,
                  "typeValidation": "loose"
                },
                "combinator": "and",
                "conditions": [
                  {
                    "id": "a49ecf63-3f68-4e21-a015-d0cbc227c230",
                    "operator": {
                      "type": "string",
                      "operation": "contains"
                    },
                    "leftValue": "={{ $json.message.text }}",
                    "rightValue": "@NCNAI_BOT"
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "DM Text",
              "conditions": {
                "options": {
                  "version": 2,
                  "leftValue": "",
                  "caseSensitive": false,
                  "typeValidation": "loose"
                },
                "combinator": "and",
                "conditions": [
                  {
                    "id": "d5ac0c9f-858a-4040-b72e-ae7b522ff60e",
                    "operator": {
                      "name": "filter.operator.equals",
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $json.message.chat.type }}",
                    "rightValue": "private"
                  }
                ]
              },
              "renameOutput": true
            }
          ]
        },
        "options": {
          "ignoreCase": true
        },
        "looseTypeValidation": true
      },
      "typeVersion": 3.2
    },
    {
      "id": "0ebdea59-8518-4078-b07a-9aa24c5e79b5",
      "name": "Sticky Note8",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -1840,
        200
      ],
      "parameters": {
        "width": 623.6530631885605,
        "height": 648.96526541807,
        "content": "## Instructions for Using the Template\nFollow these steps to set up and use this template:\n\n**Create a Telegram Bot**:\n- Open Telegram and search for BotFather.\n- Use the ``/newbot`` command to create your bot.\n- Follow the prompts and copy the Token provided at the end.\n-------------\n**Obtain a NeurochainAI API Key:**\n\n- Log in to the NeurochainAI Dashboard.\n- Generate an **API Key** under the Inference As Service section.\n- Ensure your account has sufficient credits for usage.\n-------------\n **Configure Telegram Nodes:**\n- Locate all Telegram nodes in the workflow and add your Telegram Bot Token to each node's credentials.\n-------------\n**Configure HTTP Request Nodes:**\n\n- Identify the NeurochainAI - Rest API and NeurochainAI - Flux nodes in the workflow.\nIn each node:\n- Enter your desired model in the Model field.\n- Replace ``YOUR-API-KEY-HERE`` with your API Key in the headers or configuration section.\n-------------\n**Save and Test:**\n- Save the workflow in N8N.\n- Test the workflow by interacting with your Telegram bot to trigger text and image generation tasks."
      },
      "typeVersion": 1
    },
    {
      "id": "06642d6b-f8e2-48b6-87e3-5f51af75d357",
      "name": "NeurochainAI - Flux",
      "type": "n8n-nodes-base.httpRequest",
      "onError": "continueErrorOutput",
      "position": [
        -180,
        540
      ],
      "parameters": {
        "url": "https://ncmb.neurochain.io/tasks/tti",
        "method": "POST",
        "options": {},
        "jsonBody": "={\n \"model\": \"flux1-schnell-gguf\",\n \"prompt\": \"Generate an image that matches exactly this: {{ $('Code1').item.json.cleanMessage }}\",\n \"size\": \"1024x1024\",\n \"quality\": \"standard\",\n \"n\": 1,\n \"seed\": {{ Math.floor(Math.random() * 999) + 1 }}\n}",
        "sendBody": true,
        "sendHeaders": true,
        "specifyBody": "json",
        "headerParameters": {
          "parameters": [
            {
              "name": "Authorization",
              "value": "=Bearer YOUR-API-KEY-HERE"
            },
            {
              "name": "Content-Type",
              "value": "application/json"
            }
          ]
        }
      },
      "typeVersion": 4.2,
      "alwaysOutputData": false
    },
    {
      "id": "92820069-3e65-4385-8b79-9b04dd1d3b03",
      "name": "Switch1",
      "type": "n8n-nodes-base.switch",
      "position": [
        100,
        600
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
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $json.error.message }}",
                    "rightValue": "400 - \"{\\\"error\\\":true,\\\"msg\\\":\\\"Prompt string is invalid\\\"}\""
                  }
                ]
              }
            },
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
                    "id": "ef851d57-0618-4fe7-8469-a30971a05ee5",
                    "operator": {
                      "type": "string",
                      "operation": "notEquals"
                    },
                    "leftValue": "{{ $json.error.message }}",
                    "rightValue": "400 - \"{\\\"error\\\":true,\\\"msg\\\":\\\"Prompt string is invalid\\\"}\""
                  }
                ]
              }
            }
          ]
        },
        "options": {}
      },
      "typeVersion": 3.2
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "ef6d73c3-5256-4bc0-9e10-1daf674c083e",
  "connections": {
    "Code": {
      "main": [
        [
          {
            "node": "HTTP Request3",
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
            "node": "Telegram2",
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
            "node": "Code1",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "TYPING - ACTION",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "TYPING - ACTION",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch1": {
      "main": [
        [
          {
            "node": "Telegram6",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Telegram3",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch2": {
      "main": [
        [
          {
            "node": "No response",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Prompt too short",
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
            "node": "Telegram4",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Telegram2": {
      "main": [
        [
          {
            "node": "NeurochainAI - Flux",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Telegram3": {
      "main": [
        [
          {
            "node": "Telegram5",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Telegram6": {
      "main": [
        [
          {
            "node": "Telegram7",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "HTTP Request3": {
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
    "TYPING - ACTION": {
      "main": [
        [
          {
            "node": "NeurochainAI - REST API",
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
            "node": "Switch",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "NeurochainAI - Flux": {
      "main": [
        [
          {
            "node": "Code",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Switch1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "NeurochainAI - REST API": {
      "main": [
        [
          {
            "node": "AI Response",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Switch2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-1049"></a>

## Template 1049 - Deduplicação automática de arquivos no Google Drive

- **Nome:** Deduplicação automática de arquivos no Google Drive
- **Descrição:** Fluxo que identifica duplicatas entre arquivos em uma pasta específica do Drive, mantendo apenas o primeiro ou o último conforme configuração, e atua em duplicatas renomeando-as ou enviando-as para a lixeira.
- **Funcionalidade:** • Detecção de duplicatas: identifica duplicatas usando md5Checksum e tempo de criação para marcar itens repetidos.
• Ordenação conforme configuração keep first/last: dependendo da opção, o fluxo decide manter o primeiro ou o último arquivo duplicado.
• Marcação de duplicatas: define a propriedade isDuplicate em cada item para posterior filtragem.
• Filtragem de arquivos relevantes: ignora documentos do tipo Google Apps para não processar itens não binários.
• Trigger e pasta de trabalho: monitora uma pasta específica e coleta arquivos pertencentes ao proprietário definido.
• Agrupamento para ação: duplicatas são encaminhadas para ações de trash ou renomeação conforme configuração.
• Ação sobre duplicatas: enviar para lixeira ou renomear com prefixo DUPLICATE- para sinalizar duplicatas.
• Evitar reflagging: itens já com prefixo DUPLICATE- não são marcados de novo.
• Atualização de nomes: duplicatas são renomeadas com o prefixo DUPLICATE- para facilitar identificação.
- **Ferramentas:** • Google Drive: serviço de armazenamento na nuvem utilizado para monitorar, renomear e excluir arquivos.

## Fluxo visual

```mermaid
flowchart LR
    N1["Config"]
    N2["Edit Fields"]
    N3["Filter"]
    N4["Deduplicate Keep First"]
    N5["Deduplicate Keep Last"]
    N6["Sticky Note5"]
    N7["Sticky Note6"]
    N8["Send Duplicates to Trash"]
    N9["No Operation, do nothing"]
    N10["Is Flagged"]
    N11["Google Drive Trigger"]
    N12["Drop Google Apps files"]
    N13["Sticky Note"]
    N14["Sticky Note7"]
    N15["Working Folder"]
    N16["Sticky Note1"]
    N17["Sticky Note2"]
    N18["Google Drive"]
    N19["Keep First/Last"]
    N20["Trash/Flag Duplicates"]

    N1 --> N15
    N3 --> N20
    N10 --> N9
    N10 --> N18
    N2 --> N3
    N15 --> N12
    N19 --> N5
    N19 --> N4
    N11 --> N1
    N5 --> N2
    N20 --> N8
    N20 --> N10
    N4 --> N2
    N12 --> N19
```

## Fluxo (.json) :

```json
{
  "meta": {
    "instanceId": "5e2cdd86a9e1ca2fc82cc63db38d1710d5d6a5c6fe352258a6f7112815bcd512",
    "templateCredsSetupCompleted": true
  },
  "nodes": [
    {
      "id": "c4dca8f0-98fa-4b06-a806-1ab271f024a2",
      "name": "Config",
      "type": "n8n-nodes-base.set",
      "position": [
        120,
        460
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "a916dcbd-d681-4e09-9ce9-0f50a1b4290b",
              "name": "keep",
              "type": "string",
              "value": "=last"
            },
            {
              "id": "949a2f76-5981-4fd2-9665-b10db26e2f48",
              "name": "action",
              "type": "string",
              "value": "=flag"
            },
            {
              "id": "7f4502b4-c330-4c9c-ab89-ba53874aafbb",
              "name": "owner",
              "type": "string",
              "value": "={{ $json.owner || $json.owners[0].emailAddress }}"
            },
            {
              "id": "592eb79e-28db-4470-8347-36b2a661cb03",
              "name": "folder",
              "type": "string",
              "value": "={{ $json.folder || $json.parents[0]}}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "2562ed4a-8ecd-4a32-ae51-bc85daa9817b",
      "name": "Edit Fields",
      "type": "n8n-nodes-base.set",
      "position": [
        1800,
        440
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "1d28f976-2467-4d18-8698-556d29a5f8c0",
              "name": "isDuplicate",
              "type": "boolean",
              "value": "={{ $json.isDuplicate }}"
            },
            {
              "id": "e9d8eb20-7668-4287-bfb4-d4f66c019f73",
              "name": "id",
              "type": "string",
              "value": "={{ $json.id }}"
            },
            {
              "id": "587e5f8e-bd94-4ec5-80f2-066c99922135",
              "name": "name",
              "type": "string",
              "value": "={{ $json.name }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "e7f0482c-77c7-46a0-8a36-e61bb624c422",
      "name": "Filter",
      "type": "n8n-nodes-base.filter",
      "position": [
        2020,
        440
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
              "id": "bd33247c-4c88-4c0b-bdfe-6f9dca0205e3",
              "operator": {
                "type": "boolean",
                "operation": "true",
                "singleValue": true
              },
              "leftValue": "={{ $json.isDuplicate }}",
              "rightValue": ""
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "28768732-29a4-4446-8b12-dda187976bf9",
      "name": "Deduplicate Keep First",
      "type": "n8n-nodes-base.code",
      "position": [
        1580,
        560
      ],
      "parameters": {
        "jsCode": "// Sort files by creation time (oldest first)\nconst sorted = items.sort((a, b) => \n  new Date(a.json.createdTime) - new Date(b.json.createdTime));\n\nconst seen = {};\nfor (const item of sorted) {\n  const md5 = item.json.md5Checksum;\n\n  // Failsafe: Skip if md5Checksum is missing or empty\n  if (!md5) {\n    item.json.isDuplicate = false; // Mark as not duplicate to avoid issues\n    continue; // Skip to the next item\n  }\n\n  item.json.isDuplicate = md5 in seen;\n  if (!item.json.isDuplicate) seen[md5] = true;\n}\nreturn items;"
      },
      "executeOnce": false,
      "typeVersion": 2
    },
    {
      "id": "1f6f9529-2283-4806-ad5a-b0425f9f68e2",
      "name": "Deduplicate Keep Last",
      "type": "n8n-nodes-base.code",
      "position": [
        1580,
        360
      ],
      "parameters": {
        "jsCode": "// Sort files by creation time (latest first)\nconst sorted = items.sort((a, b) => \n  new Date(b.json.createdTime) - new Date(a.json.createdTime));\n\nconst seen = {};\nfor (const item of sorted) {\n  const md5 = item.json.md5Checksum;\n\n  // Failsafe: Skip if md5Checksum is missing or empty\n  if (!md5) {\n    item.json.isDuplicate = false; // Mark as not duplicate to avoid issues\n    continue; // Skip to the next item\n  }\n\n  if (md5 in seen) {\n    item.json.isDuplicate = true;\n  } else {\n    item.json.isDuplicate = false;\n    seen[md5] = true;\n  }\n}\nreturn items;"
      },
      "executeOnce": false,
      "typeVersion": 2
    },
    {
      "id": "c5250dd1-6eeb-4b89-b2e7-e44a8d88212c",
      "name": "Sticky Note5",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -40,
        -120
      ],
      "parameters": {
        "color": 5,
        "width": 440,
        "height": 800,
        "content": "# 2. Configuration\nChoose the **keep** and **action** behavior of the workflow\n\n1. The **keep** parameter let's you decide whether to keep the first or last received file when duplicates are detected. (possible values: `first`, `last`. Default: `last`)\n2. The **action** parameter let's you decide what to do with the detected duplicates. Send them to the trash or flag them by renaming them with prefix DUPLICATE- (possible values: `trash`, `flag`. Default: `flag`) flag already prexied by DUPLICATE- are not flagged again.\n\n\nThe parameters `owner` and `folder` are taken from the trigger and will probably never need to be changed:\n- The **folder** points to the folder to work with. By default it is taken from the trigger.\n- The **owner** parameter needs to match the owner of the files. The workflow only works with files owned by this user. It is specified with the user email and is taken from the first file owner of the trigger."
      },
      "typeVersion": 1
    },
    {
      "id": "67c4d02f-b170-4504-9bae-7bf14db7abd3",
      "name": "Sticky Note6",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        460,
        180
      ],
      "parameters": {
        "color": 7,
        "width": 320,
        "height": 500,
        "content": "## Working Folder\nThe \"Working Folder\" node let's you choose Files to deduplicate.\n\nThis workflow includes a filter to work on just 1 folder at depth level 1. It doesn't work with files in nested folders\n\nYou can remove the Folder filter to work on the entire drive instead or add different filters."
      },
      "typeVersion": 1
    },
    {
      "id": "9ed26ef0-da89-43c5-9e12-2ec97b2e51f6",
      "name": "Send Duplicates to Trash",
      "type": "n8n-nodes-base.googleDrive",
      "position": [
        2760,
        320
      ],
      "parameters": {
        "fileId": {
          "__rl": true,
          "mode": "id",
          "value": "={{ $json.id }}"
        },
        "options": {},
        "operation": "deleteFile"
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
      "id": "fcfd08fa-7a19-4974-b3bb-6ed27a2030cf",
      "name": "No Operation, do nothing",
      "type": "n8n-nodes-base.noOp",
      "position": [
        2800,
        600
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "de7967e7-eb3b-456c-b12e-6de3165ad29a",
      "name": "Is Flagged",
      "type": "n8n-nodes-base.if",
      "position": [
        2540,
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
              "id": "c8d8eac5-e03a-4673-bcf9-a8acaa95cb8e",
              "operator": {
                "type": "string",
                "operation": "startsWith"
              },
              "leftValue": "={{ $('Trash/Flag Duplicates').item.json.name }}",
              "rightValue": "DUPLICATE-"
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "d227d6ee-97e7-4b4d-b1a2-4cd402be99d5",
      "name": "Google Drive Trigger",
      "type": "n8n-nodes-base.googleDriveTrigger",
      "position": [
        -360,
        460
      ],
      "parameters": {
        "event": "fileCreated",
        "options": {},
        "pollTimes": {
          "item": [
            {
              "mode": "everyX",
              "unit": "minutes",
              "value": 15
            }
          ]
        },
        "triggerOn": "specificFolder",
        "folderToWatch": {
          "__rl": true,
          "mode": "list",
          "value": "1-tjf96Ooj0SL8qaE04BGIeCGnd-O1R8c",
          "cachedResultUrl": "https://drive.google.com/drive/folders/1-tjf96Ooj0SL8qaE04BGIeCGnd-O1R8c",
          "cachedResultName": "2025/04\n"
        }
      },
      "credentials": {
        "googleDriveOAuth2Api": {
          "id": "VypmUgEf64twpmiZ",
          "name": "Google Drive account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "22e1638e-5c2e-41bc-b66e-fcee6af05762",
      "name": "Drop Google Apps files",
      "type": "n8n-nodes-base.filter",
      "position": [
        940,
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
              "id": "1e7d9666-fba0-4fe7-b03a-1a4e5c07b389",
              "operator": {
                "type": "string",
                "operation": "notStartsWith"
              },
              "leftValue": "={{ $json.mimeType }}",
              "rightValue": "application/vnd.google-apps"
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "ec80f4de-5dff-4693-bff4-2509fd581d70",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        840,
        180
      ],
      "parameters": {
        "color": 7,
        "width": 320,
        "height": 500,
        "content": "# Discard found Google Apps documents\nDocs, Sheets, Forms, Slides, Drawins etc. are discarded because they are not actual binary files and their content can't be directly checked."
      },
      "typeVersion": 1
    },
    {
      "id": "66ee766a-3dea-449f-827c-1922c6e053f3",
      "name": "Sticky Note7",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -520,
        -120
      ],
      "parameters": {
        "color": 5,
        "width": 440,
        "height": 800,
        "content": "# 1. Trigger Settings and Working Folder\n\nWhen using Google Drive Trigger configure the **Poll times** and the **Folder** to work with.\n\nBy Default the trigger is configured to check for *file uploads* every 15 minutes.\n\nWhen configured with a specific folder in the drive the workflow works only with files directly in the folder (It will not check/modify files in sub-folders).\n\nWhen configured with the root (/) folder of the drive it will check all files in all folders and sub-folders so **USE THIS WITH CAUTION** since it might lead to trashing/renaming of important files. "
      },
      "typeVersion": 1
    },
    {
      "id": "6f8a7855-2ee3-426d-879f-afb303d5aa20",
      "name": "Working Folder",
      "type": "n8n-nodes-base.googleDrive",
      "position": [
        560,
        460
      ],
      "parameters": {
        "filter": {
          "folderId": {
            "__rl": true,
            "mode": "id",
            "value": "={{ $('Config').item.json.folder }}"
          },
          "whatToSearch": "files"
        },
        "options": {
          "fields": [
            "*"
          ]
        },
        "resource": "fileFolder",
        "returnAll": true,
        "queryString": "='{{$('Config').item.json.owner}}' in owners",
        "searchMethod": "query"
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
      "id": "6f69e6d3-96ca-4411-9a48-160ebdb2a273",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2500,
        540
      ],
      "parameters": {
        "color": 7,
        "width": 540,
        "height": 220,
        "content": "### Files that already start with *DUPLICATE-* are not flagged again."
      },
      "typeVersion": 1
    },
    {
      "id": "65b4ba42-89ce-437c-a3e8-bf3f9b01cc21",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2500,
        780
      ],
      "parameters": {
        "color": 7,
        "width": 360,
        "height": 240,
        "content": "### In Google Drive Trashed files are kept for 30 days before being permanently deleted. \nThey can be reviewed and restored during that 30 day interval."
      },
      "typeVersion": 1
    },
    {
      "id": "99374aa8-e597-4919-8b64-c376b246621a",
      "name": "Google Drive",
      "type": "n8n-nodes-base.googleDrive",
      "position": [
        2880,
        800
      ],
      "parameters": {
        "fileId": {
          "__rl": true,
          "mode": "id",
          "value": "={{ $json.id }}"
        },
        "options": {},
        "operation": "update",
        "newUpdatedFileName": "=DUPLICATE-{{ $json.name }}"
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
      "id": "6ae62c31-4cf0-48e7-aa42-19fc259c5981",
      "name": "Keep First/Last",
      "type": "n8n-nodes-base.switch",
      "position": [
        1300,
        460
      ],
      "parameters": {
        "rules": {
          "values": [
            {
              "outputKey": "last",
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
                    "id": "7f5ba21d-8f3d-4736-9c34-ac7ebd6a9699",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $('Config').item.json.keep }}",
                    "rightValue": "last"
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "first",
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
                    "id": "93a013f6-6c59-47ad-bce3-8b34cc8f026c",
                    "operator": {
                      "name": "filter.operator.equals",
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $('Config').item.json.keep }}",
                    "rightValue": "first"
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
      "id": "9cb84da7-3cd9-4a53-af09-8b63f1cf8a34",
      "name": "Trash/Flag Duplicates",
      "type": "n8n-nodes-base.switch",
      "position": [
        2240,
        440
      ],
      "parameters": {
        "rules": {
          "values": [
            {
              "outputKey": "send to trash",
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
                    "id": "0314ac48-e7b7-406b-abcd-8cd1ab872c79",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $('Config').item.json.action }}",
                    "rightValue": "trash"
                  }
                ]
              },
              "renameOutput": true
            },
            {
              "outputKey": "flag as duplicate",
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
                    "id": "70d8e5f1-16a6-4921-ad9c-ab00049e507d",
                    "operator": {
                      "name": "filter.operator.equals",
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $('Config').item.json.action }}",
                    "rightValue": "flag"
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
    }
  ],
  "pinData": {},
  "connections": {
    "Config": {
      "main": [
        [
          {
            "node": "Working Folder",
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
            "node": "Trash/Flag Duplicates",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Is Flagged": {
      "main": [
        [
          {
            "node": "No Operation, do nothing",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Google Drive",
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
            "node": "Filter",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Working Folder": {
      "main": [
        [
          {
            "node": "Drop Google Apps files",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Keep First/Last": {
      "main": [
        [
          {
            "node": "Deduplicate Keep Last",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Deduplicate Keep First",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Drive Trigger": {
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
    "Deduplicate Keep Last": {
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
    "Trash/Flag Duplicates": {
      "main": [
        [
          {
            "node": "Send Duplicates to Trash",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Is Flagged",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Deduplicate Keep First": {
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
    "Drop Google Apps files": {
      "main": [
        [
          {
            "node": "Keep First/Last",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-1050"></a>

## Template 1050 - Pedido de compra Outlook: XLSX para saída estruturada

- **Nome:** Pedido de compra Outlook: XLSX para saída estruturada
- **Descrição:** Este fluxo automatiza o recebimento de pedidos de compra por email, converte anexos XLSX em um formato legível, usa IA para extrair dados e valida o conteúdo, gerando uma saída estruturada e respostas automáticas ao remetente conforme o resultado.
- **Funcionalidade:** • Detecção de novos pedidos via Outlook: Monitora recebimentos de pedidos de compra por email.
• Conversão de XLSX para Markdown: Converte anexos XLSX em uma tabela Markdown para facilitar leitura pela IA.
• Extração de dados com IA: Extrai dados-chave do pedido usando IA em formato estruturado.
• Validação automática: Verifica presença do PO, data válida, itens e correção do total.
• Correção de datas de Excel: Ajusta datas vindas do Excel para o formato correto.
• Geração de saída estruturada e resposta: Gera saída estruturada e envia respostas ao remetente conforme o resultado.
• Preparação para integração: Prepara a saída para integração com ERP ou outros sistemas de backend.
- **Ferramentas:** • Microsoft Outlook: Serviço de email utilizado para receber pedidos de compra.
• IA de Processamento de Linguagem: Extrai informações do pedido e gera saída estruturada.

## Fluxo visual

```mermaid
flowchart LR
    N1["Sticky Note"]
    N2["Sticky Note1"]
    N3["Sticky Note5"]
    N4["Extract Purchase Order Details"]
    N5["Is Excel Document?"]
    N6["Sticky Note7"]
    N7["Run Checks"]
    N8["Is Valid Purchase Order?"]
    N9["Extract from File"]
    N10["XLSX to Markdown Table"]
    N11["OpenAI Chat Model"]
    N12["Sticky Note2"]
    N13["Reply Invalid Format"]
    N14["Outlook Trigger"]
    N15["Reply Rejection"]
    N16["Reply Accepted"]
    N17["Do Something with Purchase Order"]
    N18["Fix Excel Dates"]
    N19["Sticky Note3"]
    N20["Is Submitting a Purchase Order?"]
    N21["Do Nothing"]
    N22["OpenAI Chat Model1"]

    N7 --> N8
    N16 --> N17
    N18 --> N7
    N14 --> N20
    N9 --> N10
    N5 --> N9
    N5 --> N13
    N10 --> N4
    N8 --> N16
    N8 --> N15
    N4 --> N18
    N20 --> N5
    N20 --> N21
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
      "id": "b87cc222-82ec-4b46-9573-68f41d096969",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        640,
        620
      ],
      "parameters": {
        "color": 7,
        "width": 740,
        "height": 680,
        "content": "## 2. Manually Convert XLSX to Markdown\n[Learn more about the Extract From File node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.extractfromfile/)\n\nToday's LLMs cannot parse Excel files directly so the best we can do is to convert the spreadsheet into a format that they can, namely markdown. This conversion is also a good solution for excels which aren't really datasheets - the cells are used like layout elements - which is still common for invoices and purchase orders.\n\nTo perform the conversion, we can use the 'Extract from File' node to get the each row from the xlsx and then iterate and concatenate to form our markdown table using the code node."
      },
      "typeVersion": 1
    },
    {
      "id": "c4c55042-02c8-4364-ae7e-d1ec5a75437a",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1400,
        620
      ],
      "parameters": {
        "color": 7,
        "width": 640,
        "height": 680,
        "content": "## 3. Extract Purchase Order Details using AI\n[Learn more about the Information Extractor](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.information-extractor)\n\nData entry is probably the number one reason as to why we need AI/LLMs. This time consuming and menial task can be completed in seconds and with a high degree of accuracy. Here, we ask the AI to extract each event with the term dates to a list of events using structured output."
      },
      "typeVersion": 1
    },
    {
      "id": "b9530f93-464b-4116-add7-da218fe8eb12",
      "name": "Sticky Note5",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -700,
        -80
      ],
      "parameters": {
        "width": 460,
        "height": 1400,
        "content": "## Try it out!\n### This n8n template imports purchase order submissions from Outlook and converts attached purchase order form in XLSX format into structured output.\n\nData entry jobs with user-submitted XLSX forms is a time consuming, incredibly mundane but necessary tasks which in likelihood are inherited and critical to business operation.\n\nWhile we could dream of system overhauls and modernisation, the fact is that change is hard. There is another way however -  using n8n and AI!\n\n### How it works\n* An Outlook trigger is used to watch for incoming purchase order forms submitted via a shared inbox.\n* The email attachment for the submission is a form in xlsx format - like this one https://1drv.ms/x/c/8f1f7dda12b7a145/ETWH8dKwgZ1OiVz7ISUWYf8BwiyihBjXPXEbCYkVi8XDyw?e=WWU2eR - which is imported into the workflow.\n* The 'Extract from File' node is used with the 'code' node to convert the xlsx file to markdown. This is so our LLM can understand it.\n* The Information Extractor node is used to read and extract the relevant purchase order details and line items from the form.\n* A simple validation step is used to check for common errors such as missing PO number or the amounts not matching up. A notification is automated to reply to the buyer if so.\n* Once validation passes, a confirmation is sent to the buyer and the purchase order structured output can be sent along to internal systems.\n\n### How to use\n* This template only works if you're expecting and receiving forms in XLSX format. These can be invoices, request forms as well as purchase order forms.\n* Update the Outlook nodes with your email or other emails as required.\n* What's next? I've omitted the last steps to send to an ERP or accounting system as this is dependent on your org.\n\n### Requirements\n* Outlook for Emails\n  * Check out how to setup credentials here: https://docs.n8n.io/integrations/builtin/credentials/microsoft/\n* OpenAI for LLM document understanding and extraction.\n\n### Customising the workflow\n* This template should work for other Excel files. Some will be more complicated than others so experiment with different parsers and extraction tools and strategies.\n* Customise the Information Extractor Schema to pull out the specific data you need. For example, capture any notes or comments given by the buyer.\n\n### Need Help?\nJoin the [Discord](https://discord.com/invite/XPKeKXeB7d) or ask in the [Forum](https://community.n8n.io/)!\n\nHappy Hacking!"
      },
      "typeVersion": 1
    },
    {
      "id": "f5a2d1e7-f73b-4bfa-8e02-f30db275bbcc",
      "name": "Extract Purchase Order Details",
      "type": "@n8n/n8n-nodes-langchain.informationExtractor",
      "position": [
        1500,
        920
      ],
      "parameters": {
        "text": "={{ $json.table }}",
        "options": {
          "systemPromptTemplate": "Capture the values as seen. Do not convert dates."
        },
        "schemaType": "manual",
        "inputSchema": "{\n  \"type\": \"object\",\n  \"properties\": {\n    \"purchase_order_number\": { \"type\": \"string\" },\n    \"purchase_order_date\": { \"type\": \"string\" },\n    \"purchase_order_total\": { \"type\": \"number\" },\n    \"vendor_name\": { \"type\": \"string\" },\n    \"vendor_address\": { \"type\": \"string\" },\n    \"vendor_contact\": { \"type\": \"string\" },\n    \"delivery_contact\": { \"type\": \"string\" },\n    \"delivery_address\": { \"type\": \"string\" },\n    \"delivery_method\": { \"type\": \"string\" },\n    \"items\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"description\": { \"type\": \"string\" },\n          \"part_number\": { \"type\": \"string\" },\n          \"quantity\": { \"type\": \"number\" },\n          \"unit\": { \"type\": \"number\" },\n          \"unit_price\": { \"type\": \"number\" }\n        }\n      }\n    }\n  }\n}"
      },
      "typeVersion": 1
    },
    {
      "id": "0ce545f0-8147-4ad2-bb9e-14ef0b0c26ef",
      "name": "Is Excel Document?",
      "type": "n8n-nodes-base.if",
      "position": [
        760,
        1020
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
              "id": "f723ab0a-8f2d-4501-8273-fd6455c57cdd",
              "operator": {
                "name": "filter.operator.equals",
                "type": "string",
                "operation": "equals"
              },
              "leftValue": "={{ $binary.data.mimeType }}",
              "rightValue": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "ccbd9531-66be-4e07-8b73-faf996622f9f",
      "name": "Sticky Note7",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -220,
        460
      ],
      "parameters": {
        "color": 5,
        "width": 340,
        "height": 140,
        "content": "### PURCHASE ORDER EXAMPLE\nThis is the purchase order XLSX which is used an example for this template.\nhttps://1drv.ms/x/c/8f1f7dda12b7a145/ETWH8dKwgZ1OiVz7ISUWYf8BwiyihBjXPXEbCYkVi8XDyw?e=WWU2eR"
      },
      "typeVersion": 1
    },
    {
      "id": "ef8b00eb-dba6-47dd-a825-1aa5c85ee215",
      "name": "Run Checks",
      "type": "n8n-nodes-base.set",
      "position": [
        2160,
        940
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "049c7aca-7663-4eed-93b4-9eec3760c058",
              "name": "has_po_number",
              "type": "boolean",
              "value": "={{ Boolean($json.output.purchase_order_number) }}"
            },
            {
              "id": "94d2224a-cf81-4a42-acd0-de5276a5e493",
              "name": "has_valid_po_date",
              "type": "boolean",
              "value": "={{ $json.output.purchase_order_date.toDateTime() < $now.plus({ 'day': 1 }) }}"
            },
            {
              "id": "a8f69605-dad6-4ec2-a22f-d13ff99e27cd",
              "name": "has_items",
              "type": "boolean",
              "value": "={{ $json.output.items.length > 0 }}"
            },
            {
              "id": "c11db99e-9cc2-40b7-b3a5-f3c65f88dc13",
              "name": "is_math_correct",
              "type": "boolean",
              "value": "={{\n$json.output.items.map(item => item.unit_price * item.quantity).sum().round(2) === $json.output.purchase_order_total.round(2) }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "801848cc-558c-4a30-aab5-eb403564b68f",
      "name": "Is Valid Purchase Order?",
      "type": "n8n-nodes-base.if",
      "position": [
        2360,
        940
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
              "id": "11fa8087-7809-4bc9-9fbe-32bfd35821a6",
              "operator": {
                "type": "boolean",
                "operation": "true",
                "singleValue": true
              },
              "leftValue": "={{ $json.has_po_number }}",
              "rightValue": ""
            },
            {
              "id": "c45ae85a-e060-4416-aa2c-daf58db8ba0e",
              "operator": {
                "type": "boolean",
                "operation": "true",
                "singleValue": true
              },
              "leftValue": "={{ $json.has_valid_po_date }}",
              "rightValue": ""
            },
            {
              "id": "d0ae9518-2f4b-43fb-87b1-7108a6a75424",
              "operator": {
                "type": "boolean",
                "operation": "true",
                "singleValue": true
              },
              "leftValue": "={{ $json.has_items }}",
              "rightValue": ""
            },
            {
              "id": "eed09f78-ce1a-4e09-8940-febcf7e41078",
              "operator": {
                "type": "boolean",
                "operation": "true",
                "singleValue": true
              },
              "leftValue": "={{ $json.is_math_correct }}",
              "rightValue": ""
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "7c7dd7a0-45fe-4549-8341-3b3fd18e1725",
      "name": "Extract from File",
      "type": "n8n-nodes-base.extractFromFile",
      "position": [
        980,
        920
      ],
      "parameters": {
        "options": {
          "rawData": true,
          "headerRow": false,
          "includeEmptyCells": true
        },
        "operation": "xlsx"
      },
      "typeVersion": 1
    },
    {
      "id": "dfb6b00f-fe50-42d6-8597-8fdcb562714b",
      "name": "XLSX to Markdown Table",
      "type": "n8n-nodes-base.code",
      "position": [
        1180,
        920
      ],
      "parameters": {
        "jsCode": "const rows = $input.all().map(item => item.json.row);\nconst maxLength = Math.max(...rows.map(row => row.length));\n\nconst table = [\n  '|' + rows[0].join('|') + '|',\n  '|' + Array(maxLength).fill(0).map(_ => '-').join('|') + '|',\n  rows.slice(1, rows.length)\n    .filter(row => row.some(Boolean))\n    .map(row =>\n      '|' + row.join('|') + '|'\n    ).join('\\n')\n].join('\\n')\n\nreturn { table }"
      },
      "typeVersion": 2
    },
    {
      "id": "1a3de516-1d21-4664-b2e3-8c8d6ec90ef2",
      "name": "OpenAI Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        1600,
        1080
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
      "id": "1a29236f-5eaa-4a38-a0a1-6e19abd77d2c",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2060,
        620
      ],
      "parameters": {
        "color": 7,
        "width": 940,
        "height": 680,
        "content": "## 4. Use Simple Validation to Save Time and Effort\n[Learn more about the Edit Fields node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.set)\n\nWith our extracted output, we can run simple validation checks to save on admin time. Common errors such as missing purchase order numbers or miscalculated cost amounts are easy to detect and a quick response can be given. Once validation passes, it's up to you how you use the extracted output next."
      },
      "typeVersion": 1
    },
    {
      "id": "79a39a03-5f71-4021-bcfd-06edbc285e8a",
      "name": "Reply Invalid Format",
      "type": "n8n-nodes-base.microsoftOutlook",
      "position": [
        980,
        1120
      ],
      "webhookId": "9464583e-9505-49ec-865e-58aa1ab3c2ed",
      "parameters": {
        "message": "PO rejected due to invalid file format. Please try again with XLSX.",
        "options": {},
        "messageId": {
          "__rl": true,
          "mode": "id",
          "value": "={{ $('Outlook Trigger').first().json.id }}"
        },
        "operation": "reply",
        "additionalFields": {},
        "replyToSenderOnly": true
      },
      "credentials": {
        "microsoftOutlookOAuth2Api": {
          "id": "EWg6sbhPKcM5y3Mr",
          "name": "Microsoft Outlook account"
        }
      },
      "typeVersion": 2
    },
    {
      "id": "ec973438-4d6c-4d2e-8702-1d195f514528",
      "name": "Outlook Trigger",
      "type": "n8n-nodes-base.microsoftOutlookTrigger",
      "position": [
        -120,
        920
      ],
      "parameters": {
        "fields": [
          "body",
          "categories",
          "conversationId",
          "from",
          "hasAttachments",
          "internetMessageId",
          "sender",
          "subject",
          "toRecipients",
          "receivedDateTime",
          "webLink"
        ],
        "output": "fields",
        "filters": {
          "hasAttachments": true,
          "foldersToInclude": []
        },
        "options": {
          "downloadAttachments": true
        },
        "pollTimes": {
          "item": [
            {
              "mode": "everyHour"
            }
          ]
        }
      },
      "credentials": {
        "microsoftOutlookOAuth2Api": {
          "id": "EWg6sbhPKcM5y3Mr",
          "name": "Microsoft Outlook account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "fcb173ce-7dad-497a-9376-9650c2a24a84",
      "name": "Reply Rejection",
      "type": "n8n-nodes-base.microsoftOutlook",
      "position": [
        2580,
        1040
      ],
      "webhookId": "9464583e-9505-49ec-865e-58aa1ab3c2ed",
      "parameters": {
        "message": "=PO Rejected due to the following errors:\n{{\n[\n  !$json.has_po_number ? '* PO number was not provided' : '',\n  !$json.has_valid_po_date ? '* PO date was missing or invalid' : '',\n  !$json.has_items ? '* No line items detected' : '',\n  !$json.is_math_correct ? '* Line items prices do not match up to PO total' : ''\n]\n  .compact()\n  .join('\\n')\n}}",
        "options": {},
        "messageId": {
          "__rl": true,
          "mode": "id",
          "value": "={{ $('Outlook Trigger').first().json.id }}"
        },
        "operation": "reply",
        "additionalFields": {},
        "replyToSenderOnly": true
      },
      "credentials": {
        "microsoftOutlookOAuth2Api": {
          "id": "EWg6sbhPKcM5y3Mr",
          "name": "Microsoft Outlook account"
        }
      },
      "typeVersion": 2
    },
    {
      "id": "64ced193-6b12-4ee9-b1e2-735040648051",
      "name": "Reply Accepted",
      "type": "n8n-nodes-base.microsoftOutlook",
      "position": [
        2580,
        820
      ],
      "webhookId": "9464583e-9505-49ec-865e-58aa1ab3c2ed",
      "parameters": {
        "message": "=Thank you for the purchase order.\nThis is an automated reply.",
        "options": {},
        "messageId": {
          "__rl": true,
          "mode": "id",
          "value": "={{ $('Outlook Trigger').first().json.id }}"
        },
        "operation": "reply",
        "additionalFields": {},
        "replyToSenderOnly": true
      },
      "credentials": {
        "microsoftOutlookOAuth2Api": {
          "id": "EWg6sbhPKcM5y3Mr",
          "name": "Microsoft Outlook account"
        }
      },
      "typeVersion": 2
    },
    {
      "id": "7bfe0e44-cd5d-4290-ba2e-0064c95bc4e2",
      "name": "Do Something with Purchase Order",
      "type": "n8n-nodes-base.noOp",
      "position": [
        2800,
        940
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "6f517f2f-6072-46a2-8a9d-cca4e958d601",
      "name": "Fix Excel Dates",
      "type": "n8n-nodes-base.set",
      "position": [
        1840,
        920
      ],
      "parameters": {
        "mode": "raw",
        "options": {},
        "jsonOutput": "={{\n{\n  output: {\n    ...$json.output,\n    purchase_order_date: $json.output.purchase_order_date\n      ? new Date((new Date(1900, 0, 1)).getTime() + (Number($json.output.purchase_order_date) - 2) * (24 * 60 * 60 * 1000))\n      : $json.output.purchase_order_date\n  }\n}\n}}"
      },
      "typeVersion": 3.4
    },
    {
      "id": "f3a31b63-ebcb-4d93-8c5a-f626897b7d68",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -220,
        620
      ],
      "parameters": {
        "color": 7,
        "width": 840,
        "height": 680,
        "content": "## 1. Wait For Incoming Purchase Orders\n[Read more about the Outlook trigger](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftoutlooktrigger)\n\nOur template starts by watching for new emails to a shared inbox (eg. \"purchase-orders@example.com\") using the Outlook Trigger node. Our goal is to identify and capture buyer purchase orders so that we can automating validate and use AI to reduce the data entry time and cost at scale.\n\nWe can also use the Text Classifier node to validate intent. This ensures we catch valid submissions are not just queries about purchase-orders or replies."
      },
      "typeVersion": 1
    },
    {
      "id": "bb395dfc-2831-4e57-90c9-62f13f84302e",
      "name": "Is Submitting a Purchase Order?",
      "type": "@n8n/n8n-nodes-langchain.textClassifier",
      "position": [
        80,
        920
      ],
      "parameters": {
        "options": {
          "fallback": "other"
        },
        "inputText": "=from: {{ $json.from.emailAddress.name }} <{{ $json.from.emailAddress.address }}>\nsubject: {{ $json.subject }}\nmessage:\n{{ $json.body.content }}",
        "categories": {
          "categories": [
            {
              "category": "is_purchase_order",
              "description": "The message's intent is to submit a purchase order"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "id": "e52ec2e2-8be5-40ab-b1f8-8d7c0b161e1a",
      "name": "Do Nothing",
      "type": "n8n-nodes-base.noOp",
      "position": [
        420,
        1040
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "5ca6be4e-bc33-42d7-91bc-d30f7ccfdd25",
      "name": "OpenAI Chat Model1",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        180,
        1080
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
          "id": "8gccIjcuf3gvaoEr",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1.2
    }
  ],
  "pinData": {},
  "connections": {
    "Run Checks": {
      "main": [
        [
          {
            "node": "Is Valid Purchase Order?",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Reply Accepted": {
      "main": [
        [
          {
            "node": "Do Something with Purchase Order",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Fix Excel Dates": {
      "main": [
        [
          {
            "node": "Run Checks",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Outlook Trigger": {
      "main": [
        [
          {
            "node": "Is Submitting a Purchase Order?",
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
            "node": "XLSX to Markdown Table",
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
            "node": "Extract Purchase Order Details",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Is Excel Document?": {
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
            "node": "Reply Invalid Format",
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
            "node": "Is Submitting a Purchase Order?",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "XLSX to Markdown Table": {
      "main": [
        [
          {
            "node": "Extract Purchase Order Details",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Is Valid Purchase Order?": {
      "main": [
        [
          {
            "node": "Reply Accepted",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Reply Rejection",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract Purchase Order Details": {
      "main": [
        [
          {
            "node": "Fix Excel Dates",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Is Submitting a Purchase Order?": {
      "main": [
        [
          {
            "node": "Is Excel Document?",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Do Nothing",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-1051"></a>

## Template 1051 - Bot Telegram com memória em Supabase

- **Nome:** Bot Telegram com memória em Supabase
- **Descrição:** Fluxo que recebe mensagens do Telegram, mantém a sessão do usuário em Supabase vinculando-a a um thread do OpenAI e retorna respostas geradas por um assistente OpenAI.
- **Funcionalidade:** • Recepção de mensagens do Telegram: Aciona o fluxo ao receber novas mensagens de usuários.
• Verificação de usuário existente: Consulta o banco para verificar se o usuário já tem um thread associado.
• Criação de thread OpenAI para novos usuários: Gera um novo thread no OpenAI quando não há thread associado ao usuário.
• Armazenamento de mapeamento de sessão: Salva telegram_id e openai_thread_id no Supabase para persistência de sessão e contexto.
• Envio de mensagens do usuário ao OpenAI: Encaminha o texto recebido ao thread correspondente no OpenAI.
• Execução do assistente (com streaming): Dispara a execução do assistente configurado, recebendo atualizações parciais (deltas) e o resultado final.
• Recuperação e encaminhamento da resposta: Busca as mensagens do thread OpenAI e envia a resposta final de volta ao usuário no Telegram.
- **Ferramentas:** • Telegram: Plataforma de mensageria usada para receber mensagens dos usuários e enviar respostas.
• OpenAI (Assistants / Threads API): Serviço de modelo de linguagem que cria threads, recebe mensagens do usuário, executa o assistente e gera respostas (suporta streaming de deltas).
• Supabase: Banco de dados em nuvem usado para armazenar e recuperar o mapeamento entre telegram_id e openai_thread_id, preservando o contexto do usuário.

## Fluxo visual

```mermaid
flowchart LR
    N1["Get New Message"]
    N2["OPENAI - Create thread"]
    N3["Create User"]
    N4["Merge"]
    N5["OPENAI - Send message"]
    N6["OPENAI - Run assistant"]
    N7["OPENAI - Get messages"]
    N8["Send Message to User"]
    N9["If User exists"]
    N10["Find User"]
    N11["Sticky Note1"]
    N12["Sticky Note2"]
    N13["Sticky Note3"]
    N14["Sticky Note4"]
    N15["Sticky Note5"]
    N16["Sticky Note6"]
    N17["Sticky Note7"]

    N4 --> N5
    N10 --> N9
    N3 --> N4
    N9 --> N4
    N9 --> N2
    N1 --> N10
    N7 --> N8
    N5 --> N6
    N2 --> N3
    N6 --> N7
```

## Fluxo (.json) :

```json
{
  "nodes": [
    {
      "id": "9cc26a42-eb43-40c4-b507-cbaf187a5e15",
      "name": "Get New Message",
      "type": "n8n-nodes-base.telegramTrigger",
      "position": [
        1120,
        500
      ],
      "webhookId": "464f0a75-56d1-402f-8b12-b358452e9736",
      "parameters": {
        "updates": [
          "message"
        ],
        "additionalFields": {}
      },
      "credentials": {
        "telegramApi": {
          "id": "rI0zyfIYVIyXt2fL",
          "name": "Telegram Club"
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "098b6fcf-7cb6-4730-8892-949fedc946b3",
      "name": "OPENAI - Create thread",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1740,
        640
      ],
      "parameters": {
        "url": "https://api.openai.com/v1/threads",
        "method": "POST",
        "options": {},
        "sendHeaders": true,
        "authentication": "predefinedCredentialType",
        "headerParameters": {
          "parameters": [
            {
              "name": "OpenAI-Beta",
              "value": "assistants=v2"
            }
          ]
        },
        "nodeCredentialType": "openAiApi"
      },
      "credentials": {
        "openAiApi": {
          "id": "zJhr5piyEwVnWtaI",
          "name": "OpenAi club"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "fa157f8c-b776-4b20-bfaf-c17460383505",
      "name": "Create User",
      "type": "n8n-nodes-base.supabase",
      "position": [
        1900,
        640
      ],
      "parameters": {
        "tableId": "telegram_users",
        "fieldsUi": {
          "fieldValues": [
            {
              "fieldId": "telegram_id",
              "fieldValue": "={{ $('Get New Message').item.json.message.chat.id }}"
            },
            {
              "fieldId": "openai_thread_id",
              "fieldValue": "={{ $('OPENAI - Create thread').item.json.id }}"
            }
          ]
        }
      },
      "credentials": {
        "supabaseApi": {
          "id": "QBhcokohbJHfQZ9A",
          "name": "Supabase club"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "115e417f-5962-409b-8adf-ff236eb9ce2e",
      "name": "Merge",
      "type": "n8n-nodes-base.merge",
      "position": [
        2080,
        500
      ],
      "parameters": {},
      "typeVersion": 3
    },
    {
      "id": "ba5c7385-8c80-43c8-9de2-430175bda70b",
      "name": "OPENAI - Send message",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        2240,
        500
      ],
      "parameters": {
        "url": "=https://api.openai.com/v1/threads/{{ $('Merge').item.json.openai_thread_id }}/messages ",
        "method": "POST",
        "options": {},
        "sendBody": true,
        "sendHeaders": true,
        "authentication": "predefinedCredentialType",
        "bodyParameters": {
          "parameters": [
            {
              "name": "role",
              "value": "user"
            },
            {
              "name": "content",
              "value": "={{ $('Get New Message').item.json.message.text }}"
            }
          ]
        },
        "headerParameters": {
          "parameters": [
            {
              "name": "OpenAI-Beta",
              "value": "assistants=v2"
            }
          ]
        },
        "nodeCredentialType": "openAiApi"
      },
      "credentials": {
        "openAiApi": {
          "id": "fLfRtaXbR0EVD0pl",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "024832bc-3d42-4879-a57f-b23e962b4c69",
      "name": "OPENAI - Run assistant",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        2440,
        500
      ],
      "parameters": {
        "url": "=https://api.openai.com/v1/threads/{{ $('Merge').item.json.openai_thread_id }}/runs",
        "method": "POST",
        "options": {},
        "sendBody": true,
        "sendHeaders": true,
        "authentication": "predefinedCredentialType",
        "bodyParameters": {
          "parameters": [
            {
              "name": "assistant_id",
              "value": "asst_b0QhuzySG6jofHFdzPZD7WEz"
            },
            {
              "name": "stream",
              "value": "={{true}}"
            }
          ]
        },
        "headerParameters": {
          "parameters": [
            {
              "name": "OpenAI-Beta",
              "value": "assistants=v2"
            }
          ]
        },
        "nodeCredentialType": "openAiApi"
      },
      "credentials": {
        "openAiApi": {
          "id": "fLfRtaXbR0EVD0pl",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "bc191e2b-15f4-45b7-af2e-19ed1639b7f5",
      "name": "OPENAI - Get messages",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        2640,
        500
      ],
      "parameters": {
        "url": "=https://api.openai.com/v1/threads/{{ $('Merge').item.json.openai_thread_id }}/messages",
        "options": {},
        "sendHeaders": true,
        "authentication": "predefinedCredentialType",
        "headerParameters": {
          "parameters": [
            {
              "name": "OpenAI-Beta",
              "value": "assistants=v2"
            }
          ]
        },
        "nodeCredentialType": "openAiApi"
      },
      "credentials": {
        "openAiApi": {
          "id": "zJhr5piyEwVnWtaI",
          "name": "OpenAi club"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "c22e05e5-f0a7-4a09-a864-acfc58469b30",
      "name": "Send Message to User",
      "type": "n8n-nodes-base.telegram",
      "position": [
        2840,
        500
      ],
      "parameters": {
        "text": "={{ $('OPENAI - Get messages').item.json.data[0].content[0].text.value }}",
        "chatId": "={{ $('Get New Message').item.json.message.chat.id }}",
        "additionalFields": {
          "appendAttribution": false
        }
      },
      "credentials": {
        "telegramApi": {
          "id": "rI0zyfIYVIyXt2fL",
          "name": "Telegram Club"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "0673be1f-3cae-42a0-9c62-1ed570859043",
      "name": "If User exists",
      "type": "n8n-nodes-base.if",
      "position": [
        1560,
        500
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
              "id": "b6e69a1f-eb42-4ef6-b80c-3167f1b8c830",
              "operator": {
                "type": "string",
                "operation": "exists",
                "singleValue": true
              },
              "leftValue": "={{ $json.id }}",
              "rightValue": ""
            }
          ]
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "a4916f54-ae6b-495d-979b-92dca965e3bb",
      "name": "Find User",
      "type": "n8n-nodes-base.supabase",
      "position": [
        1360,
        500
      ],
      "parameters": {
        "filters": {
          "conditions": [
            {
              "keyName": "telegram_id",
              "keyValue": "={{ $json.message.chat.id }}",
              "condition": "eq"
            }
          ]
        },
        "tableId": "telegram_users",
        "operation": "getAll"
      },
      "credentials": {
        "supabaseApi": {
          "id": "QBhcokohbJHfQZ9A",
          "name": "Supabase club"
        }
      },
      "typeVersion": 1,
      "alwaysOutputData": true
    },
    {
      "id": "6d01d7ed-e96b-47cf-9a5f-46608031baa2",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1300,
        800
      ],
      "parameters": {
        "color": 7,
        "width": 600.723278204605,
        "height": 213.15921994594194,
        "content": "SQL query to create table in Supabase:\n\n```\ncreate table\n public.telegram_users (\n id uuid not null default gen_random_uuid (),\n date_created timestamp with time zone not null default (now() at time zone 'utc'::text),\n telegram_id bigint null,\n openai_thread_id text null,\n constraint telegram_users_pkey primary key (id)\n ) tablespace pg_default;\n```"
      },
      "typeVersion": 1
    },
    {
      "id": "1a996da0-6022-48d7-ba40-1d137547a3d7",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2340,
        360
      ],
      "parameters": {
        "color": 3,
        "width": 282.075050779723,
        "height": 80,
        "content": "Create assistant in [OpenAI](https://platform.openai.com/assistants).\n\n**Specify own assistant id here**\n"
      },
      "typeVersion": 1
    },
    {
      "id": "b24d2008-7950-41f0-a7fa-50360c0c6854",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1040,
        380
      ],
      "parameters": {
        "color": 3,
        "width": 235.09282368774151,
        "height": 80,
        "content": "Create own Telegram bot in [Botfather bot](https://t.me/botfather)"
      },
      "typeVersion": 1
    },
    {
      "id": "9eb2491e-5ad9-4015-8ed9-611e72924503",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1300,
        680
      ],
      "parameters": {
        "color": 3,
        "height": 80,
        "content": "Create table in [Supabase](https://supabase.com) with SQL query"
      },
      "typeVersion": 1
    },
    {
      "id": "884b5a1b-007c-4752-becc-46c8fc58db92",
      "name": "Sticky Note5",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        200,
        120
      ],
      "parameters": {
        "color": 7,
        "width": 280.2462120317618,
        "height": 438.5821431288714,
        "content": "### Set up steps\n1. **Create a Telegram Bot** using the [Botfather](https://t.me/botfather) and obtain the bot token.\n2. **Set up Supabase:**\n\t1. Create a new project and generate a ```SUPABASE_URL``` and ```SUPABASE_KEY```.\n\t2. Create a new table named ```telegram_users``` with the following SQL query:\n```\ncreate table\n public.telegram_users (\n id uuid not null default gen_random_uuid (),\n date_created timestamp with time zone not null default (now() at time zone 'utc'::text),\n telegram_id bigint null,\n openai_thread_id text null,\n constraint telegram_users_pkey primary key (id)\n ) tablespace pg_default;\n```\n3. **OpenAI Setup:**\n\t1. Create an OpenAI assistant and obtain the ```OPENAI_API_KEY```.\n\t2. Customize your assistant’s personality or use cases according to your requirements.\n4. **Environment Configuration in n8n:**\n\t1. Configure the Telegram, Supabase, and OpenAI nodes with the appropriate credentials.\n\t2. Set up triggers for receiving messages and handling conversation logic.\n\t3. Set up OpenAI assistant ID in \"++OPENAI - Run assistant++\" node."
      },
      "typeVersion": 1
    },
    {
      "id": "02db77ac-4909-4a56-a558-03c86d8b8552",
      "name": "Sticky Note6",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        200,
        -400
      ],
      "parameters": {
        "color": 7,
        "width": 636.2128494576581,
        "height": 494.9629292914819,
        "content": "![5min Logo](https://cflobdhpqwnoisuctsoc.supabase.co/storage/v1/object/public/my_storage/Untitled%20(1500%20x%20300%20px).png)\n## AI Telegram Bot with Supabase memory\n**Made by [Mark Shcherbakov](https://www.linkedin.com/in/marklowcoding/) from community [5minAI](https://www.skool.com/5minai-2861)**\n\nMany simple chatbots lack context awareness and user memory. This workflow solves that by integrating Supabase to keep track of user sessions (via ```telegram_id``` and ```openai_thread_id```), allowing the bot to maintain continuity and context in conversations, leading to a more human-like and engaging experience.\n\nThis Telegram bot template connects with OpenAI to answer user queries while storing and retrieving user information from a Supabase database. The memory component ensures that the bot can reference past interactions, making it suitable for use cases such as customer support, virtual assistants, or any application where context retention is crucial.\n\n"
      },
      "typeVersion": 1
    },
    {
      "id": "a991a7c9-ea5f-4a25-aa92-6dc2fce11b05",
      "name": "Sticky Note7",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        500,
        120
      ],
      "parameters": {
        "color": 7,
        "width": 330.5152611046425,
        "height": 240.6839895136402,
        "content": "### ... or watch set up video [5 min]\n[![Youtube Thumbnail](https://cflobdhpqwnoisuctsoc.supabase.co/storage/v1/object/public/my_storage/Youtube%20thumb%20(3).png)](https://www.youtube.com/watch?v=kS41gut8l0g)\n"
      },
      "typeVersion": 1
    }
  ],
  "pinData": {
    "Merge": [
      {
        "id": "4a5d71a4-a2f7-43e2-936f-37ee5bf5cc9e",
        "telegram_id": 1468754364,
        "date_created": "2024-10-04T08:29:07.458869+00:00",
        "openai_thread_id": null
      }
    ],
    "Find User": [
      {
        "id": "4a5d71a4-a2f7-43e2-936f-37ee5bf5cc9e",
        "telegram_id": 1468754364,
        "date_created": "2024-10-04T08:29:07.458869+00:00",
        "openai_thread_id": null
      }
    ],
    "Get New Message": [
      {
        "message": {
          "chat": {
            "id": 1468754364,
            "type": "private",
            "username": "low_code",
            "first_name": "Mark"
          },
          "date": 1727961249,
          "from": {
            "id": 1468754364,
            "is_bot": false,
            "username": "low_code",
            "first_name": "Mark",
            "language_code": "en"
          },
          "text": "Hello, how are you?",
          "entities": [
            {
              "type": "bot_command",
              "length": 6,
              "offset": 0
            }
          ],
          "message_id": 3
        },
        "update_id": 412281353
      }
    ],
    "Send Message to User": [
      {
        "ok": true,
        "result": {
          "chat": {
            "id": 1468754364,
            "type": "private",
            "username": "low_code",
            "first_name": "Mark"
          },
          "date": 1727971919,
          "from": {
            "id": 7999029315,
            "is_bot": true,
            "username": "test241234_bot",
            "first_name": "Test bot"
          },
          "text": "Hello! I'm just a program, but I'm here and ready to help you. How can I assist you today?",
          "message_id": 7
        }
      }
    ],
    "OPENAI - Get messages": [
      {
        "data": [
          {
            "id": "msg_C7aXbSotAl6xCxjR9avi4wUz",
            "role": "assistant",
            "object": "thread.message",
            "run_id": "run_9avgP4lZ1FRSsL3y9UO8HPa1",
            "content": [
              {
                "text": {
                  "value": "Hello! I'm just a program, but I'm here and ready to help you. How can I assist you today?",
                  "annotations": []
                },
                "type": "text"
              }
            ],
            "metadata": {},
            "thread_id": "thread_laO8JLPW6L1upYHW6fSRj8Bt",
            "created_at": 1727971739,
            "attachments": [],
            "assistant_id": "asst_b0QhuzySG6jofHFdzPZD7WEz"
          },
          {
            "id": "msg_fVGPVHR03QKheHXh54SFpmpm",
            "role": "user",
            "object": "thread.message",
            "run_id": null,
            "content": [
              {
                "text": {
                  "value": "Hello, how are you?",
                  "annotations": []
                },
                "type": "text"
              }
            ],
            "metadata": {},
            "thread_id": "thread_laO8JLPW6L1upYHW6fSRj8Bt",
            "created_at": 1727971467,
            "attachments": [],
            "assistant_id": null
          }
        ],
        "object": "list",
        "last_id": "msg_fVGPVHR03QKheHXh54SFpmpm",
        "first_id": "msg_C7aXbSotAl6xCxjR9avi4wUz",
        "has_more": false
      }
    ],
    "OPENAI - Send message": [
      {
        "id": "msg_fVGPVHR03QKheHXh54SFpmpm",
        "role": "user",
        "object": "thread.message",
        "run_id": null,
        "content": [
          {
            "text": {
              "value": "Hello, how are you?",
              "annotations": []
            },
            "type": "text"
          }
        ],
        "metadata": {},
        "thread_id": "thread_laO8JLPW6L1upYHW6fSRj8Bt",
        "created_at": 1727971467,
        "attachments": [],
        "assistant_id": null
      }
    ],
    "OPENAI - Create thread": [
      {
        "id": "thread_laO8JLPW6L1upYHW6fSRj8Bt",
        "object": "thread",
        "metadata": {},
        "created_at": 1727971362,
        "tool_resources": {}
      }
    ],
    "OPENAI - Run assistant": [
      {
        "data": "event: thread.run.created\ndata: {\"id\":\"run_9avgP4lZ1FRSsL3y9UO8HPa1\",\"object\":\"thread.run\",\"created_at\":1727971737,\"assistant_id\":\"asst_b0QhuzySG6jofHFdzPZD7WEz\",\"thread_id\":\"thread_laO8JLPW6L1upYHW6fSRj8Bt\",\"status\":\"queued\",\"started_at\":null,\"expires_at\":1727972337,\"cancelled_at\":null,\"failed_at\":null,\"completed_at\":null,\"required_action\":null,\"last_error\":null,\"model\":\"gpt-4o-mini\",\"instructions\":\"You are ChatGPT\",\"tools\":[],\"tool_resources\":{\"code_interpreter\":{\"file_ids\":[]}},\"metadata\":{},\"temperature\":1.0,\"top_p\":1.0,\"max_completion_tokens\":null,\"max_prompt_tokens\":null,\"truncation_strategy\":{\"type\":\"auto\",\"last_messages\":null},\"incomplete_details\":null,\"usage\":null,\"response_format\":\"auto\",\"tool_choice\":\"auto\",\"parallel_tool_calls\":true}\n\nevent: thread.run.queued\ndata: {\"id\":\"run_9avgP4lZ1FRSsL3y9UO8HPa1\",\"object\":\"thread.run\",\"created_at\":1727971737,\"assistant_id\":\"asst_b0QhuzySG6jofHFdzPZD7WEz\",\"thread_id\":\"thread_laO8JLPW6L1upYHW6fSRj8Bt\",\"status\":\"queued\",\"started_at\":null,\"expires_at\":1727972337,\"cancelled_at\":null,\"failed_at\":null,\"completed_at\":null,\"required_action\":null,\"last_error\":null,\"model\":\"gpt-4o-mini\",\"instructions\":\"You are ChatGPT\",\"tools\":[],\"tool_resources\":{\"code_interpreter\":{\"file_ids\":[]}},\"metadata\":{},\"temperature\":1.0,\"top_p\":1.0,\"max_completion_tokens\":null,\"max_prompt_tokens\":null,\"truncation_strategy\":{\"type\":\"auto\",\"last_messages\":null},\"incomplete_details\":null,\"usage\":null,\"response_format\":\"auto\",\"tool_choice\":\"auto\",\"parallel_tool_calls\":true}\n\nevent: thread.run.in_progress\ndata: {\"id\":\"run_9avgP4lZ1FRSsL3y9UO8HPa1\",\"object\":\"thread.run\",\"created_at\":1727971737,\"assistant_id\":\"asst_b0QhuzySG6jofHFdzPZD7WEz\",\"thread_id\":\"thread_laO8JLPW6L1upYHW6fSRj8Bt\",\"status\":\"in_progress\",\"started_at\":1727971738,\"expires_at\":1727972337,\"cancelled_at\":null,\"failed_at\":null,\"completed_at\":null,\"required_action\":null,\"last_error\":null,\"model\":\"gpt-4o-mini\",\"instructions\":\"You are ChatGPT\",\"tools\":[],\"tool_resources\":{\"code_interpreter\":{\"file_ids\":[]}},\"metadata\":{},\"temperature\":1.0,\"top_p\":1.0,\"max_completion_tokens\":null,\"max_prompt_tokens\":null,\"truncation_strategy\":{\"type\":\"auto\",\"last_messages\":null},\"incomplete_details\":null,\"usage\":null,\"response_format\":\"auto\",\"tool_choice\":\"auto\",\"parallel_tool_calls\":true}\n\nevent: thread.run.step.created\ndata: {\"id\":\"step_b0iFvL1q1UEZDfBRbbNTiulO\",\"object\":\"thread.run.step\",\"created_at\":1727971739,\"run_id\":\"run_9avgP4lZ1FRSsL3y9UO8HPa1\",\"assistant_id\":\"asst_b0QhuzySG6jofHFdzPZD7WEz\",\"thread_id\":\"thread_laO8JLPW6L1upYHW6fSRj8Bt\",\"type\":\"message_creation\",\"status\":\"in_progress\",\"cancelled_at\":null,\"completed_at\":null,\"expires_at\":1727972337,\"failed_at\":null,\"last_error\":null,\"step_details\":{\"type\":\"message_creation\",\"message_creation\":{\"message_id\":\"msg_C7aXbSotAl6xCxjR9avi4wUz\"}},\"usage\":null}\n\nevent: thread.run.step.in_progress\ndata: {\"id\":\"step_b0iFvL1q1UEZDfBRbbNTiulO\",\"object\":\"thread.run.step\",\"created_at\":1727971739,\"run_id\":\"run_9avgP4lZ1FRSsL3y9UO8HPa1\",\"assistant_id\":\"asst_b0QhuzySG6jofHFdzPZD7WEz\",\"thread_id\":\"thread_laO8JLPW6L1upYHW6fSRj8Bt\",\"type\":\"message_creation\",\"status\":\"in_progress\",\"cancelled_at\":null,\"completed_at\":null,\"expires_at\":1727972337,\"failed_at\":null,\"last_error\":null,\"step_details\":{\"type\":\"message_creation\",\"message_creation\":{\"message_id\":\"msg_C7aXbSotAl6xCxjR9avi4wUz\"}},\"usage\":null}\n\nevent: thread.message.created\ndata: {\"id\":\"msg_C7aXbSotAl6xCxjR9avi4wUz\",\"object\":\"thread.message\",\"created_at\":1727971739,\"assistant_id\":\"asst_b0QhuzySG6jofHFdzPZD7WEz\",\"thread_id\":\"thread_laO8JLPW6L1upYHW6fSRj8Bt\",\"run_id\":\"run_9avgP4lZ1FRSsL3y9UO8HPa1\",\"status\":\"in_progress\",\"incomplete_details\":null,\"incomplete_at\":null,\"completed_at\":null,\"role\":\"assistant\",\"content\":[],\"attachments\":[],\"metadata\":{}}\n\nevent: thread.message.in_progress\ndata: {\"id\":\"msg_C7aXbSotAl6xCxjR9avi4wUz\",\"object\":\"thread.message\",\"created_at\":1727971739,\"assistant_id\":\"asst_b0QhuzySG6jofHFdzPZD7WEz\",\"thread_id\":\"thread_laO8JLPW6L1upYHW6fSRj8Bt\",\"run_id\":\"run_9avgP4lZ1FRSsL3y9UO8HPa1\",\"status\":\"in_progress\",\"incomplete_details\":null,\"incomplete_at\":null,\"completed_at\":null,\"role\":\"assistant\",\"content\":[],\"attachments\":[],\"metadata\":{}}\n\nevent: thread.message.delta\ndata: {\"id\":\"msg_C7aXbSotAl6xCxjR9avi4wUz\",\"object\":\"thread.message.delta\",\"delta\":{\"content\":[{\"index\":0,\"type\":\"text\",\"text\":{\"value\":\"Hello\",\"annotations\":[]}}]}}\n\nevent: thread.message.delta\ndata: {\"id\":\"msg_C7aXbSotAl6xCxjR9avi4wUz\",\"object\":\"thread.message.delta\",\"delta\":{\"content\":[{\"index\":0,\"type\":\"text\",\"text\":{\"value\":\"!\"}}]}}\n\nevent: thread.message.delta\ndata: {\"id\":\"msg_C7aXbSotAl6xCxjR9avi4wUz\",\"object\":\"thread.message.delta\",\"delta\":{\"content\":[{\"index\":0,\"type\":\"text\",\"text\":{\"value\":\" I'm\"}}]}}\n\nevent: thread.message.delta\ndata: {\"id\":\"msg_C7aXbSotAl6xCxjR9avi4wUz\",\"object\":\"thread.message.delta\",\"delta\":{\"content\":[{\"index\":0,\"type\":\"text\",\"text\":{\"value\":\" just\"}}]}}\n\nevent: thread.message.delta\ndata: {\"id\":\"msg_C7aXbSotAl6xCxjR9avi4wUz\",\"object\":\"thread.message.delta\",\"delta\":{\"content\":[{\"index\":0,\"type\":\"text\",\"text\":{\"value\":\" a\"}}]}}\n\nevent: thread.message.delta\ndata: {\"id\":\"msg_C7aXbSotAl6xCxjR9avi4wUz\",\"object\":\"thread.message.delta\",\"delta\":{\"content\":[{\"index\":0,\"type\":\"text\",\"text\":{\"value\":\" program\"}}]}}\n\nevent: thread.message.delta\ndata: {\"id\":\"msg_C7aXbSotAl6xCxjR9avi4wUz\",\"object\":\"thread.message.delta\",\"delta\":{\"content\":[{\"index\":0,\"type\":\"text\",\"text\":{\"value\":\",\"}}]}}\n\nevent: thread.message.delta\ndata: {\"id\":\"msg_C7aXbSotAl6xCxjR9avi4wUz\",\"object\":\"thread.message.delta\",\"delta\":{\"content\":[{\"index\":0,\"type\":\"text\",\"text\":{\"value\":\" but\"}}]}}\n\nevent: thread.message.delta\ndata: {\"id\":\"msg_C7aXbSotAl6xCxjR9avi4wUz\",\"object\":\"thread.message.delta\",\"delta\":{\"content\":[{\"index\":0,\"type\":\"text\",\"text\":{\"value\":\" I'm\"}}]}}\n\nevent: thread.message.delta\ndata: {\"id\":\"msg_C7aXbSotAl6xCxjR9avi4wUz\",\"object\":\"thread.message.delta\",\"delta\":{\"content\":[{\"index\":0,\"type\":\"text\",\"text\":{\"value\":\" here\"}}]}}\n\nevent: thread.message.delta\ndata: {\"id\":\"msg_C7aXbSotAl6xCxjR9avi4wUz\",\"object\":\"thread.message.delta\",\"delta\":{\"content\":[{\"index\":0,\"type\":\"text\",\"text\":{\"value\":\" and\"}}]}}\n\nevent: thread.message.delta\ndata: {\"id\":\"msg_C7aXbSotAl6xCxjR9avi4wUz\",\"object\":\"thread.message.delta\",\"delta\":{\"content\":[{\"index\":0,\"type\":\"text\",\"text\":{\"value\":\" ready\"}}]}}\n\nevent: thread.message.delta\ndata: {\"id\":\"msg_C7aXbSotAl6xCxjR9avi4wUz\",\"object\":\"thread.message.delta\",\"delta\":{\"content\":[{\"index\":0,\"type\":\"text\",\"text\":{\"value\":\" to\"}}]}}\n\nevent: thread.message.delta\ndata: {\"id\":\"msg_C7aXbSotAl6xCxjR9avi4wUz\",\"object\":\"thread.message.delta\",\"delta\":{\"content\":[{\"index\":0,\"type\":\"text\",\"text\":{\"value\":\" help\"}}]}}\n\nevent: thread.message.delta\ndata: {\"id\":\"msg_C7aXbSotAl6xCxjR9avi4wUz\",\"object\":\"thread.message.delta\",\"delta\":{\"content\":[{\"index\":0,\"type\":\"text\",\"text\":{\"value\":\" you\"}}]}}\n\nevent: thread.message.delta\ndata: {\"id\":\"msg_C7aXbSotAl6xCxjR9avi4wUz\",\"object\":\"thread.message.delta\",\"delta\":{\"content\":[{\"index\":0,\"type\":\"text\",\"text\":{\"value\":\".\"}}]}}\n\nevent: thread.message.delta\ndata: {\"id\":\"msg_C7aXbSotAl6xCxjR9avi4wUz\",\"object\":\"thread.message.delta\",\"delta\":{\"content\":[{\"index\":0,\"type\":\"text\",\"text\":{\"value\":\" How\"}}]}}\n\nevent: thread.message.delta\ndata: {\"id\":\"msg_C7aXbSotAl6xCxjR9avi4wUz\",\"object\":\"thread.message.delta\",\"delta\":{\"content\":[{\"index\":0,\"type\":\"text\",\"text\":{\"value\":\" can\"}}]}}\n\nevent: thread.message.delta\ndata: {\"id\":\"msg_C7aXbSotAl6xCxjR9avi4wUz\",\"object\":\"thread.message.delta\",\"delta\":{\"content\":[{\"index\":0,\"type\":\"text\",\"text\":{\"value\":\" I\"}}]}}\n\nevent: thread.message.delta\ndata: {\"id\":\"msg_C7aXbSotAl6xCxjR9avi4wUz\",\"object\":\"thread.message.delta\",\"delta\":{\"content\":[{\"index\":0,\"type\":\"text\",\"text\":{\"value\":\" assist\"}}]}}\n\nevent: thread.message.delta\ndata: {\"id\":\"msg_C7aXbSotAl6xCxjR9avi4wUz\",\"object\":\"thread.message.delta\",\"delta\":{\"content\":[{\"index\":0,\"type\":\"text\",\"text\":{\"value\":\" you\"}}]}}\n\nevent: thread.message.delta\ndata: {\"id\":\"msg_C7aXbSotAl6xCxjR9avi4wUz\",\"object\":\"thread.message.delta\",\"delta\":{\"content\":[{\"index\":0,\"type\":\"text\",\"text\":{\"value\":\" today\"}}]}}\n\nevent: thread.message.delta\ndata: {\"id\":\"msg_C7aXbSotAl6xCxjR9avi4wUz\",\"object\":\"thread.message.delta\",\"delta\":{\"content\":[{\"index\":0,\"type\":\"text\",\"text\":{\"value\":\"?\"}}]}}\n\nevent: thread.message.completed\ndata: {\"id\":\"msg_C7aXbSotAl6xCxjR9avi4wUz\",\"object\":\"thread.message\",\"created_at\":1727971739,\"assistant_id\":\"asst_b0QhuzySG6jofHFdzPZD7WEz\",\"thread_id\":\"thread_laO8JLPW6L1upYHW6fSRj8Bt\",\"run_id\":\"run_9avgP4lZ1FRSsL3y9UO8HPa1\",\"status\":\"completed\",\"incomplete_details\":null,\"incomplete_at\":null,\"completed_at\":1727971740,\"role\":\"assistant\",\"content\":[{\"type\":\"text\",\"text\":{\"value\":\"Hello! I'm just a program, but I'm here and ready to help you. How can I assist you today?\",\"annotations\":[]}}],\"attachments\":[],\"metadata\":{}}\n\nevent: thread.run.step.completed\ndata: {\"id\":\"step_b0iFvL1q1UEZDfBRbbNTiulO\",\"object\":\"thread.run.step\",\"created_at\":1727971739,\"run_id\":\"run_9avgP4lZ1FRSsL3y9UO8HPa1\",\"assistant_id\":\"asst_b0QhuzySG6jofHFdzPZD7WEz\",\"thread_id\":\"thread_laO8JLPW6L1upYHW6fSRj8Bt\",\"type\":\"message_creation\",\"status\":\"completed\",\"cancelled_at\":null,\"completed_at\":1727971740,\"expires_at\":1727972337,\"failed_at\":null,\"last_error\":null,\"step_details\":{\"type\":\"message_creation\",\"message_creation\":{\"message_id\":\"msg_C7aXbSotAl6xCxjR9avi4wUz\"}},\"usage\":{\"prompt_tokens\":39,\"completion_tokens\":25,\"total_tokens\":64}}\n\nevent: thread.run.completed\ndata: {\"id\":\"run_9avgP4lZ1FRSsL3y9UO8HPa1\",\"object\":\"thread.run\",\"created_at\":1727971737,\"assistant_id\":\"asst_b0QhuzySG6jofHFdzPZD7WEz\",\"thread_id\":\"thread_laO8JLPW6L1upYHW6fSRj8Bt\",\"status\":\"completed\",\"started_at\":1727971738,\"expires_at\":null,\"cancelled_at\":null,\"failed_at\":null,\"completed_at\":1727971740,\"required_action\":null,\"last_error\":null,\"model\":\"gpt-4o-mini\",\"instructions\":\"You are ChatGPT\",\"tools\":[],\"tool_resources\":{\"code_interpreter\":{\"file_ids\":[]}},\"metadata\":{},\"temperature\":1.0,\"top_p\":1.0,\"max_completion_tokens\":null,\"max_prompt_tokens\":null,\"truncation_strategy\":{\"type\":\"auto\",\"last_messages\":null},\"incomplete_details\":null,\"usage\":{\"prompt_tokens\":39,\"completion_tokens\":25,\"total_tokens\":64},\"response_format\":\"auto\",\"tool_choice\":\"auto\",\"parallel_tool_calls\":true}\n\nevent: done\ndata: [DONE]\n\n"
      }
    ]
  },
  "connections": {
    "Merge": {
      "main": [
        [
          {
            "node": "OPENAI - Send message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Find User": {
      "main": [
        [
          {
            "node": "If User exists",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Create User": {
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
    "If User exists": {
      "main": [
        [
          {
            "node": "Merge",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "OPENAI - Create thread",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get New Message": {
      "main": [
        [
          {
            "node": "Find User",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OPENAI - Get messages": {
      "main": [
        [
          {
            "node": "Send Message to User",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OPENAI - Send message": {
      "main": [
        [
          {
            "node": "OPENAI - Run assistant",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OPENAI - Create thread": {
      "main": [
        [
          {
            "node": "Create User",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OPENAI - Run assistant": {
      "main": [
        [
          {
            "node": "OPENAI - Get messages",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-1052"></a>

## Template 1052 - Atualizar taxas de câmbio USD e registrar dados

- **Nome:** Atualizar taxas de câmbio USD e registrar dados
- **Descrição:** Este fluxo agenda a coleta diária de taxas de câmbio do USD para várias moedas, atualiza uma planilha de taxas com os valores atuais e registra o histórico de cotações em uma planilha de Arquivos.
- **Funcionalidade:** • Agendamento diário: inicia a automação no horário definido.
• Coleta de taxas do USD: faz uma chamada de API para obter as taxas de várias moedas em relação ao USD.
• Formatação de dados: transforma a resposta em um formato pronto para uso nas planilhas.
• Atualização de planilha de taxas: atualiza a planilha principal com as novas taxas e a data de atualização.
• Arquivamento de taxas: adiciona as taxas históricas a uma planilha de Arquivos para registro contínuo.
• Notas de configuração: inclui observações e instruções para configurar o fluxo.
- **Ferramentas:** • Exchangerate API: serviço de API HTTP utilizado para obter as taxas de câmbio do USD para várias moedas.
• Planilhas Google: serviço para ler e escrever dados em planilhas, usado para atualizar as taxas e arquivar o histórico.

## Fluxo visual

```mermaid
flowchart LR
    N1["Filter Fields"]
    N2["Final Outputs"]
    N3["USD Query"]
    N4["Update Rate Sheet"]
    N5["Archive Rates"]
    N6["Sticky Note4"]
    N7["Format Output to JSON"]
    N8["Sticky Note"]
    N9["Trigger - 08:00 am"]
    N10["Sticky Note3"]

    N3 --> N7
    N3 --> N1
    N1 --> N2
    N2 --> N4
    N2 --> N5
    N9 --> N3
    N7 --> N2
```

## Fluxo (.json) :

```json
{
  "meta": {
    "instanceId": ""
  },
  "nodes": [
    {
      "id": "9ede57d1-57de-44d5-bf64-38632e54dd73",
      "name": "Filter Fields",
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
              "id": "d492ffce-8ece-443d-9fc3-caa9a7a90744",
              "name": "base_currency",
              "type": "string",
              "value": "={{ $json.base_code }}"
            },
            {
              "id": "33e67974-8cee-4d1f-b144-c4c07b149bab",
              "name": "time_last_update_utc",
              "type": "string",
              "value": "={{ new Date($json[\"time_last_update_utc\"]).toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric', timeZone: 'UTC' }) + ' at ' + new Date($json[\"time_last_update_utc\"]).toISOString().substring(11, 16) + ' UTC' }}\n"
            }
          ]
        }
      },
      "notesInFlow": true,
      "retryOnFail": true,
      "typeVersion": 3.4
    },
    {
      "id": "7bb820ce-b6aa-46b6-9546-0a3d7f30fa54",
      "name": "Final Outputs",
      "type": "n8n-nodes-base.merge",
      "position": [
        860,
        180
      ],
      "parameters": {
        "mode": "combineBySql"
      },
      "notesInFlow": true,
      "typeVersion": 3
    },
    {
      "id": "4eb99392-7b5c-4ec8-8eeb-56b01d5778f6",
      "name": "USD Query",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        300,
        180
      ],
      "parameters": {
        "url": "https://v6.exchangerate-api.com/v6/<YOUR_API_KEY>/latest/USD",
        "options": {}
      },
      "notesInFlow": true,
      "retryOnFail": true,
      "typeVersion": 4.2
    },
    {
      "id": "bc33414a-36db-41d3-881f-870d40bb929e",
      "name": "Update Rate Sheet",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        1080,
        240
      ],
      "parameters": {
        "columns": {
          "value": {},
          "schema": [
            {
              "id": "base_currency",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "base_currency",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "time_last_update_utc",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "time_last_update_utc",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "USD",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "USD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "AED",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "AED",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "AFN",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "AFN",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "ALL",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "ALL",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "AMD",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "AMD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "ANG",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "ANG",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "AOA",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "AOA",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "ARS",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "ARS",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "AUD",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "AUD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "AWG",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "AWG",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "AZN",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "AZN",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "BAM",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "BAM",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "BBD",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "BBD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "BDT",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "BDT",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "BGN",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "BGN",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "BHD",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "BHD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "BIF",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "BIF",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "BMD",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "BMD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "BND",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "BND",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "BOB",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "BOB",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "BRL",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "BRL",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "BSD",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "BSD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "BTN",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "BTN",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "BWP",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "BWP",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "BYN",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "BYN",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "BZD",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "BZD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "CAD",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "CAD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "CDF",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "CDF",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "CHF",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "CHF",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "CLP",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "CLP",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "CNY",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "CNY",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "COP",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "COP",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "CRC",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "CRC",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "CUP",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "CUP",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "CVE",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "CVE",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "CZK",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "CZK",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "DJF",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "DJF",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "DKK",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "DKK",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "DOP",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "DOP",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "DZD",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "DZD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "EGP",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "EGP",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "ERN",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "ERN",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "ETB",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "ETB",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "EUR",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "EUR",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "FJD",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "FJD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "FKP",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "FKP",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "FOK",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "FOK",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "GBP",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "GBP",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "GEL",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "GEL",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "GGP",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "GGP",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "GHS",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "GHS",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "GIP",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "GIP",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "GMD",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "GMD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "GNF",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "GNF",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "GTQ",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "GTQ",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "GYD",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "GYD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "HKD",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "HKD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "HNL",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "HNL",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "HRK",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "HRK",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "HTG",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "HTG",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "HUF",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "HUF",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "IDR",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "IDR",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "ILS",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "ILS",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "IMP",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "IMP",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "INR",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "INR",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "IQD",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "IQD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "IRR",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "IRR",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "ISK",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "ISK",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "JEP",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "JEP",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "JMD",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "JMD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "JOD",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "JOD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "JPY",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "JPY",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "KES",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "KES",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "KGS",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "KGS",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "KHR",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "KHR",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "KID",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "KID",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "KMF",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "KMF",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "KRW",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "KRW",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "KWD",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "KWD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "KYD",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "KYD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "KZT",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "KZT",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "LAK",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "LAK",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "LBP",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "LBP",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "LKR",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "LKR",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "LRD",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "LRD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "LSL",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "LSL",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "LYD",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "LYD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "MAD",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "MAD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "MDL",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "MDL",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "MGA",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "MGA",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "MKD",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "MKD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "MMK",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "MMK",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "MNT",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "MNT",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "MOP",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "MOP",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "MRU",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "MRU",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "MUR",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "MUR",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "MVR",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "MVR",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "MWK",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "MWK",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "MXN",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "MXN",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "MYR",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "MYR",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "MZN",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "MZN",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "NAD",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "NAD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "NGN",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "NGN",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "NIO",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "NIO",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "NOK",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "NOK",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "NPR",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "NPR",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "NZD",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "NZD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "OMR",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "OMR",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "PAB",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "PAB",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "PEN",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "PEN",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "PGK",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "PGK",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "PHP",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "PHP",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "PKR",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "PKR",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "PLN",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "PLN",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "PYG",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "PYG",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "QAR",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "QAR",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "RON",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "RON",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "RSD",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "RSD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "RUB",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "RUB",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "RWF",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "RWF",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "SAR",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "SAR",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "SBD",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "SBD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "SCR",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "SCR",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "SDG",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "SDG",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "SEK",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "SEK",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "SGD",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "SGD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "SHP",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "SHP",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "SLE",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "SLE",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "SLL",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "SLL",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "SOS",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "SOS",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "SRD",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "SRD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "SSP",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "SSP",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "STN",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "STN",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "SYP",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "SYP",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "SZL",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "SZL",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "THB",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "THB",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "TJS",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "TJS",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "TMT",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "TMT",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "TND",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "TND",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "TOP",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "TOP",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "TRY",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "TRY",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "TTD",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "TTD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "TVD",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "TVD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "TWD",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "TWD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "TZS",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "TZS",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "UAH",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "UAH",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "UGX",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "UGX",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "UYU",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "UYU",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "UZS",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "UZS",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "VES",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "VES",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "VND",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "VND",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "VUV",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "VUV",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "WST",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "WST",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "XAF",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "XAF",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "XCD",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "XCD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "XCG",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "XCG",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "XDR",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "XDR",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "XOF",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "XOF",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "XPF",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "XPF",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "YER",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "YER",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "ZAR",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "ZAR",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "ZMW",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "ZMW",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "ZWL",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "ZWL",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            }
          ],
          "mappingMode": "autoMapInputData",
          "matchingColumns": [
            "base_currency"
          ],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {},
        "operation": "update",
        "sheetName": {
          "__rl": true,
          "mode": "=",
          "value": "gid=0",
          "cachedResultUrl": "=",
          "cachedResultName": "="
        },
        "documentId": {
          "__rl": true,
          "mode": "=",
          "value": "=",
          "cachedResultUrl": "=",
          "cachedResultName": "="
        }
      },
      "notesInFlow": true,
      "typeVersion": 4.5
    },
    {
      "id": "51c05637-b9c0-4fa5-9942-42b5abb870db",
      "name": "Archive Rates",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        1080,
        100
      ],
      "parameters": {
        "columns": {
          "value": {},
          "schema": [
            {
              "id": "base_currency",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "base_currency",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "time_last_update_utc",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "time_last_update_utc",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "USD",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "USD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "AED",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "AED",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "AFN",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "AFN",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "ALL",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "ALL",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "AMD",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "AMD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "ANG",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "ANG",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "AOA",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "AOA",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "ARS",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "ARS",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "AUD",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "AUD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "AWG",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "AWG",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "AZN",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "AZN",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "BAM",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "BAM",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "BBD",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "BBD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "BDT",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "BDT",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "BGN",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "BGN",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "BHD",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "BHD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "BIF",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "BIF",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "BMD",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "BMD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "BND",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "BND",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "BOB",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "BOB",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "BRL",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "BRL",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "BSD",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "BSD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "BTN",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "BTN",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "BWP",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "BWP",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "BYN",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "BYN",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "BZD",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "BZD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "CAD",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "CAD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "CDF",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "CDF",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "CHF",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "CHF",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "CLP",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "CLP",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "CNY",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "CNY",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "COP",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "COP",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "CRC",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "CRC",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "CUP",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "CUP",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "CVE",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "CVE",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "CZK",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "CZK",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "DJF",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "DJF",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "DKK",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "DKK",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "DOP",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "DOP",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "DZD",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "DZD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "EGP",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "EGP",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "ERN",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "ERN",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "ETB",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "ETB",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "EUR",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "EUR",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "FJD",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "FJD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "FKP",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "FKP",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "FOK",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "FOK",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "GBP",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "GBP",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "GEL",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "GEL",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "GGP",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "GGP",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "GHS",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "GHS",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "GIP",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "GIP",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "GMD",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "GMD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "GNF",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "GNF",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "GTQ",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "GTQ",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "GYD",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "GYD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "HKD",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "HKD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "HNL",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "HNL",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "HRK",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "HRK",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "HTG",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "HTG",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "HUF",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "HUF",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "IDR",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "IDR",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "ILS",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "ILS",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "IMP",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "IMP",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "INR",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "INR",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "IQD",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "IQD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "IRR",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "IRR",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "ISK",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "ISK",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "JEP",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "JEP",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "JMD",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "JMD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "JOD",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "JOD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "JPY",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "JPY",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "KES",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "KES",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "KGS",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "KGS",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "KHR",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "KHR",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "KID",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "KID",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "KMF",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "KMF",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "KRW",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "KRW",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "KWD",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "KWD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "KYD",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "KYD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "KZT",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "KZT",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "LAK",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "LAK",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "LBP",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "LBP",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "LKR",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "LKR",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "LRD",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "LRD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "LSL",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "LSL",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "LYD",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "LYD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "MAD",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "MAD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "MDL",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "MDL",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "MGA",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "MGA",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "MKD",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "MKD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "MMK",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "MMK",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "MNT",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "MNT",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "MOP",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "MOP",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "MRU",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "MRU",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "MUR",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "MUR",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "MVR",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "MVR",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "MWK",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "MWK",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "MXN",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "MXN",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "MYR",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "MYR",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "MZN",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "MZN",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "NAD",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "NAD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "NGN",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "NGN",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "NIO",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "NIO",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "NOK",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "NOK",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "NPR",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "NPR",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "NZD",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "NZD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "OMR",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "OMR",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "PAB",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "PAB",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "PEN",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "PEN",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "PGK",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "PGK",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "PHP",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "PHP",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "PKR",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "PKR",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "PLN",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "PLN",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "PYG",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "PYG",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "QAR",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "QAR",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "RON",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "RON",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "RSD",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "RSD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "RUB",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "RUB",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "RWF",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "RWF",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "SAR",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "SAR",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "SBD",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "SBD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "SCR",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "SCR",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "SDG",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "SDG",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "SEK",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "SEK",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "SGD",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "SGD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "SHP",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "SHP",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "SLE",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "SLE",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "SLL",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "SLL",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "SOS",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "SOS",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "SRD",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "SRD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "SSP",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "SSP",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "STN",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "STN",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "SYP",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "SYP",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "SZL",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "SZL",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "THB",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "THB",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "TJS",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "TJS",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "TMT",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "TMT",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "TND",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "TND",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "TOP",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "TOP",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "TRY",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "TRY",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "TTD",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "TTD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "TVD",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "TVD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "TWD",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "TWD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "TZS",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "TZS",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "UAH",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "UAH",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "UGX",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "UGX",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "UYU",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "UYU",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "UZS",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "UZS",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "VES",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "VES",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "VND",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "VND",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "VUV",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "VUV",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "WST",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "WST",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "XAF",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "XAF",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "XCD",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "XCD",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "XCG",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "XCG",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "XDR",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "XDR",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "XOF",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "XOF",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "XPF",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "XPF",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "YER",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "YER",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "ZAR",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "ZAR",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "ZMW",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "ZMW",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "ZWL",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "ZWL",
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
          "value": 249536536,
          "cachedResultUrl": "=",
          "cachedResultName": "Archives"
        },
        "documentId": {
          "__rl": true,
          "mode": "=",
          "value": "=",
          "cachedResultUrl": "=",
          "cachedResultName": "="
        }
      },
      "notesInFlow": true,
      "typeVersion": 4.5
    },
    {
      "id": "7e27ded4-f201-4c45-9221-23a4dbdaada1",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        740,
        -280
      ],
      "parameters": {
        "color": 7,
        "width": 540,
        "height": 680,
        "content": "### 2. Update Rates and Record Data\nThe results are recorded in two sheets\n- The invoice template sheet with the exchange rate and the update date\n- A record sheet that includes all the conversions from the base currency to any target currency\n\n#### How to setup?\n- **Update Results in Google Sheets**:\n 0. Copy and paste the template of Google Sheet: [Template Sheet](https://docs.google.com/spreadsheets/d/1SjzMb2q-6-byx9qmHbkrLseBWj9jEGduinH_5xi-c7g/edit?usp=sharing)\n   1. Add your Google Sheet API credentials to access the Google Sheet file\n   2. Select the file using the list, an URL or an ID\n   3. Select the sheet in which the vocabulary list is stored\n  [Learn more about the Google Sheet Node](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets)"
      },
      "typeVersion": 1
    },
    {
      "id": "062fc991-7c1d-4aee-a85a-7b961e310c33",
      "name": "Format Output to JSON",
      "type": "n8n-nodes-base.code",
      "position": [
        580,
        280
      ],
      "parameters": {
        "jsCode": "const rates = items[0].json.conversion_rates;\n\nreturn [\n  {\n    json: rates\n  }\n];\n"
      },
      "typeVersion": 2
    },
    {
      "id": "2379c1ca-2348-4d19-b47e-8cbe5955e759",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        20,
        -280
      ],
      "parameters": {
        "color": 7,
        "width": 480,
        "height": 640,
        "content": "### 1. Setup the Trigger and Exchange API Call\nThe scheduler will trigger the workflow every morning at 08:00. It starts with an API call to collect the exchange rate of USD to all currency.\n\n#### How to setup?\n- **Put your API Key for exchange rate**:\n   1. Sign up for a free tier and get your API key: [API Documentation](https://www.exchangerate-api.com/docs/overview)\n   2. Replace the placeholder in the HTTP request node <YOUR_API_KEY> with your key"
      },
      "typeVersion": 1
    },
    {
      "id": "f383eca8-bc1f-40f7-a450-7dbbbcec4c49",
      "name": "Trigger - 08:00 am",
      "type": "n8n-nodes-base.scheduleTrigger",
      "position": [
        100,
        180
      ],
      "parameters": {
        "rule": {
          "interval": [
            {
              "triggerAtHour": 7
            }
          ]
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "64cd2e3b-2ca3-4df5-b855-b4d37912d643",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1300,
        -280
      ],
      "parameters": {
        "width": 780,
        "height": 540,
        "content": "### 3. Do you need more details?\nFind a step-by-step guide in this tutorial\n![Guide](https://www.samirsaci.com/content/images/2025/04/temp-6.png)\n[🎥 Watch My Tutorial](https://www.youtube.com/watch?v=T8UFxu8Y9zA)"
      },
      "typeVersion": 1
    }
  ],
  "pinData": {},
  "connections": {
    "USD Query": {
      "main": [
        [
          {
            "node": "Format Output to JSON",
            "type": "main",
            "index": 0
          },
          {
            "node": "Filter Fields",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Filter Fields": {
      "main": [
        [
          {
            "node": "Final Outputs",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Final Outputs": {
      "main": [
        [
          {
            "node": "Update Rate Sheet",
            "type": "main",
            "index": 0
          },
          {
            "node": "Archive Rates",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Trigger - 08:00 am": {
      "main": [
        [
          {
            "node": "USD Query",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Format Output to JSON": {
      "main": [
        [
          {
            "node": "Final Outputs",
            "type": "main",
            "index": 1
          }
        ]
      ]
    }
  }
}
```

<a id="template-1053"></a>

## Template 1053 - Anunciar novo produto nas redes

- **Nome:** Anunciar novo produto nas redes
- **Descrição:** Ao detectar a criação de um novo produto na loja, o fluxo publica um anúncio no Twitter e envia uma mensagem para um chat no Telegram com informações do produto.
- **Funcionalidade:** • Detecção de criação de produto: inicia o fluxo quando um novo produto é criado na loja.
• Publicação no Twitter: publica um tweet com um texto templado que inclui vendor, title e product_type do produto.
• Envio de mensagem no Telegram: envia uma mensagem para o chat configurado (chatId) com o mesmo conteúdo do anúncio.
• Inserção de dados dinâmicos: utiliza campos do produto (vendor, title, product_type) como placeholders nas mensagens.
- **Ferramentas:** • Shopify: plataforma de comércio eletrônico que envia o evento de criação do produto.
• Twitter: plataforma de microblogging usada para publicar o anúncio publicamente.
• Telegram: aplicativo de mensagens usado para enviar o anúncio a um chat/ canal configurado.

## Fluxo visual

```mermaid
flowchart LR
    N1["Twitter"]
    N2["Telegram"]
    N3["product created"]

    N3 --> N1
    N3 --> N2
```

## Fluxo (.json) :

```json
{
  "nodes": [
    {
      "name": "Twitter",
      "type": "n8n-nodes-base.twitter",
      "position": [
        720,
        -220
      ],
      "parameters": {
        "text": "=Hey there, my design is now on a new product ✨\nVisit my {{$json[\"vendor\"]}} shop to get this cool{{$json[\"title\"]}} (and check out more {{$json[\"product_type\"]}}) 🛍️",
        "additionalFields": {}
      },
      "credentials": {
        "twitterOAuth1Api": "twitter"
      },
      "typeVersion": 1
    },
    {
      "name": "Telegram",
      "type": "n8n-nodes-base.telegram",
      "position": [
        720,
        -20
      ],
      "parameters": {
        "text": "=Hey there, my design is now on a new product!\nVisit my {{$json[\"vendor\"]}} shop to get this cool{{$json[\"title\"]}} (and check out more {{$json[\"product_type\"]}})",
        "chatId": "123456",
        "additionalFields": {}
      },
      "credentials": {
        "telegramApi": "telegram_habot"
      },
      "typeVersion": 1
    },
    {
      "name": "product created",
      "type": "n8n-nodes-base.shopifyTrigger",
      "position": [
        540,
        -110
      ],
      "webhookId": "2a7e0e50-8f09-4a2b-bf54-a849a6ac4fe0",
      "parameters": {
        "topic": "products/create"
      },
      "credentials": {
        "shopifyApi": "shopify_nodeqa"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "product created": {
      "main": [
        [
          {
            "node": "Twitter",
            "type": "main",
            "index": 0
          },
          {
            "node": "Telegram",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-1054"></a>

## Template 1054 - Obter página web e retornar Markdown

- **Nome:** Obter página web e retornar Markdown
- **Descrição:** Recebe uma URL, solicita o conteúdo ao serviço de scraping e devolve o texto da página no formato Markdown.
- **Funcionalidade:** • Receber URL de entrada: Aceita um objeto de entrada contendo o campo query.url com a URL a ser processada.
• Enviar requisição de scraping: Constrói e envia um POST para um serviço de scraping contendo a URL e solicitando o formato Markdown.
• Autenticação por cabeçalho: Utiliza credenciais configuradas via cabeçalho HTTP para autorizar a chamada à API de scraping.
• Extrair e normalizar resposta: Captura o campo de retorno com o Markdown (data.markdown) e o mapeia para o campo response para uso posterior.
• Reutilização por agentes/workspaces: Documentado para que outros agentes ou workspaces possam chamar este fluxo enviando apenas a URL.
- **Ferramentas:** • FireCrawl API: Serviço de scraping que recebe uma URL via API e retorna o conteúdo da página em formatos estruturados (neste fluxo, Markdown).



## Fluxo visual

```mermaid
flowchart LR
    N1["Execute Workflow Trigger"]
    N2["FireCrawl"]
    N3["Edit Fields"]
    N4["Sticky Note"]

    N2 --> N3
    N1 --> N2
```

## Fluxo (.json) :

```json
{
  "id": "7DPLpEkww5Uctcml",
  "meta": {
    "instanceId": "75d76ac1fb686d403c2294ca007b62282f34c3e15dc3528cc1dbe36a827c0c6e"
  },
  "name": "get_a_web_page",
  "tags": [
    {
      "id": "7v5QbLiQYkQ7zGTK",
      "name": "tools",
      "createdAt": "2025-01-08T16:33:21.887Z",
      "updatedAt": "2025-01-08T16:33:21.887Z"
    }
  ],
  "nodes": [
    {
      "id": "290cc9b8-e4b1-4124-ab0e-afbb02a9072b",
      "name": "Execute Workflow Trigger",
      "type": "n8n-nodes-base.executeWorkflowTrigger",
      "position": [
        -460,
        -100
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "f256ed59-ba61-4912-9a75-4e7703547de5",
      "name": "FireCrawl",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        -220,
        -100
      ],
      "parameters": {
        "url": "https://api.firecrawl.dev/v1/scrape",
        "method": "POST",
        "options": {},
        "jsonBody": "={\n \"url\": \"{{ $json.query.url }}\",\n \"formats\": [\n \"markdown\"\n ]\n} ",
        "sendBody": true,
        "sendHeaders": true,
        "specifyBody": "json",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "headerParameters": {
          "parameters": [
            {}
          ]
        }
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "RoJ6k6pWBzSVp9JK",
          "name": "Firecrawl"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "a28bdbe6-fa59-4bf1-b0ab-c34ebb10cf0f",
      "name": "Edit Fields",
      "type": "n8n-nodes-base.set",
      "position": [
        -20,
        -100
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "1af62ef9-7385-411a-8aba-e4087f09c3a9",
              "name": "response",
              "type": "string",
              "value": "={{ $json.data.markdown }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "fcd26213-038a-453f-80e5-a3936e4c2d06",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -480,
        -340
      ],
      "parameters": {
        "width": 620,
        "height": 200,
        "content": "## Send URL got Crawl\nThis can be reused by Ai Agents and any Workspace to crawl a site. All that Workspace has to do is send a request:\n\n```json\n {\n \"url\": \"Some URL to Get\"\n }\n```"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {
    "Execute Workflow Trigger": [
      {
        "json": {
          "query": {
            "url": "https://en.wikipedia.org/wiki/Linux"
          }
        }
      }
    ]
  },
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "396f46a7-3120-42f9-b3d5-2021e6e995b8",
  "connections": {
    "FireCrawl": {
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
    "Execute Workflow Trigger": {
      "main": [
        [
          {
            "node": "FireCrawl",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-1055"></a>

## Template 1055 - Coleta diária do Product Hunt para Sheets

- **Nome:** Coleta diária do Product Hunt para Sheets
- **Descrição:** Fluxo automatizado que busca diariamente posts do Product Hunt, extrai informações do produto, resolve o URL final de cada site e grava os dados em uma planilha.
- **Funcionalidade:** • Detecção automática diária: o fluxo é acionado a cada dia para iniciar a coleta.
• Definição de data atual: obtém a data de hoje no formato yyyy-mm-dd para filtrar os posts.
• Busca de posts do Product Hunt: consulta GraphQL para obter os posts do dia.
• Extração de informações do produto: extrai nome, tagline, descrição e website de cada post.
• Resolução de URL de website: resolve redirecionamentos para obter o URL final do site.
• Mesclagem de dados: combina informações do produto com o URL final para cada item.
• Gravação na planilha: adiciona ou atualiza linhas com nome, tagline, descrição e next_url na planilha alvo.
- **Ferramentas:** • Product Hunt GraphQL API: API para consultar posts diários do Product Hunt, com autenticação por token.
• Google Sheets: Planilha para armazenar os dados coletados (nome, tagline, descrição, next_url).



## Fluxo visual

```mermaid
flowchart LR
    N1["Daily Trigger1"]
    N2["Set Date1"]
    N3["Sticky Note16"]
    N4["Sticky Note17"]
    N5["Fetches today’s Product Hunt posts via API."]
    N6["Extracts Product Info"]
    N7["Resolve Website Redirection"]
    N8["Data  2 (website url)"]
    N9["Data 1 (product info)"]
    N10["Merge Data"]
    N11["Appends all details"]
    N12["Sticky Note18"]

    N2 --> N5
    N10 --> N11
    N1 --> N2
    N8 --> N10
    N9 --> N10
    N6 --> N7
    N6 --> N9
    N7 --> N8
    N5 --> N6
```

## Fluxo (.json) :

```json
{
  "meta": {
    "instanceId": "431926ace0ab32761b92304a05ffb4819a2a2a8ee5de45404953945769b5412a"
  },
  "nodes": [
    {
      "id": "53bf4cb6-8f55-4d8d-b4af-48345f75cdd5",
      "name": "Daily Trigger1",
      "type": "n8n-nodes-base.scheduleTrigger",
      "position": [
        -660,
        6580
      ],
      "parameters": {
        "rule": {
          "interval": [
            {}
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "id": "774624c1-cb4d-4355-9ed7-448d393c5f3b",
      "name": "Set Date1",
      "type": "n8n-nodes-base.set",
      "position": [
        -440,
        6580
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "today",
              "value": "={{ new Date().toISOString().split('T')[0] }}"
            }
          ]
        },
        "options": {}
      },
      "typeVersion": 1
    },
    {
      "id": "951eb189-8143-48d7-88c9-3ce235de83f6",
      "name": "Sticky Note16",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -260,
        6400
      ],
      "parameters": {
        "content": "### 🔐 How to Get Your Product Hunt Token\n\nTo get your Product Hunt token, follow the official guide here:  \n👉 [Product Hunt OAuth Token Guide](https://api.producthunt.com/v2/docs/oauth_user_authentication/oauth_authorize_ask_for_access_grant_code_on_behalf_of_the_user)\n"
      },
      "typeVersion": 1
    },
    {
      "id": "ae83bb19-a981-4b28-8dcd-ecd9501bd3d0",
      "name": "Sticky Note17",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        820,
        6280
      ],
      "parameters": {
        "width": 360,
        "height": 280,
        "content": "### 📄 How to Connect Google Sheets in n8n\n\nTo connect your Google Sheets to n8n:\n\n1. Go to your n8n Credentials page.\n2. Select **Google Sheets** and add new credentials.\n3. Authenticate your Google account and give the required permissions.\n\nFollow the full guide here:  \n👉 https://www.youtube.com/watch?v=pWGXlZBGu4k\n"
      },
      "typeVersion": 1
    },
    {
      "id": "4a0c04d4-3ce2-4ebb-94a3-2a0441e25e23",
      "name": "Fetches today’s Product Hunt posts via API.",
      "type": "n8n-nodes-base.httpRequest",
      "notes": "### 🔐 How to Get Your Product Hunt Token\n\nTo get your Product Hunt token, follow the official guide here:  \n👉 [Product Hunt OAuth Token Guide](https://api.producthunt.com/v2/docs/oauth_user_authentication/oauth_authorize_ask_for_access_grant_code_on_behalf_of_the_user)\n",
      "position": [
        -220,
        6580
      ],
      "parameters": {
        "url": "https://api.producthunt.com/v2/api/graphql",
        "method": "POST",
        "options": {},
        "sendBody": true,
        "sendHeaders": true,
        "bodyParameters": {
          "parameters": [
            {
              "name": "query",
              "value": "query {   posts(first: 10, postedAfter: \"{{ $node[\\\"Set Date1\\\"].json[\\\"today\\\"] }}T00:00:00Z\", postedBefore: \"{{ $node[\\\"Set Date1\\\"].json[\\\"today\\\"] }}T23:59:59Z\") {     edges {       node {         name         tagline         description         website       }       cursor     }     pageInfo {       hasNextPage       endCursor     }   } }"
            }
          ]
        },
        "headerParameters": {
          "parameters": [
            {
              "name": "Authorization",
              "value": "=Bearer YOUR_PRODUCT_HUNT_API_KEY"
            },
            {
              "name": "User-Agent",
              "value": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            }
          ]
        }
      },
      "notesInFlow": false,
      "typeVersion": 4.2
    },
    {
      "id": "994c8a22-ce3a-42cf-95e1-9512f1525fd7",
      "name": "Extracts Product Info",
      "type": "n8n-nodes-base.code",
      "position": [
        0,
        6580
      ],
      "parameters": {
        "jsCode": "return $json.data.posts.edges.map(edge => {\n  return {\n    json: {\n      name: edge.node.name,\n      tagline: edge.node.tagline,\n      description: edge.node.description,\n      website: edge.node.website\n    }\n  };\n});\n"
      },
      "typeVersion": 2
    },
    {
      "id": "f7846147-cd50-4b5e-bb79-0f17ff7d5900",
      "name": "Resolve Website Redirection",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        220,
        6680
      ],
      "parameters": {
        "url": "={{ $json.website }}\n",
        "options": {
          "fullResponse": true,
          "followRedirect": false,
          "followAllRedirects": false,
          "ignoreResponseCode": true
        },
        "responseFormat": "string",
        "dataPropertyName": "body",
        "allowUnauthorizedCerts": true
      },
      "typeVersion": 1
    },
    {
      "id": "11f5df7a-bc46-4ae6-b97d-0ce8c15d804d",
      "name": "Data  2 (website url)",
      "type": "n8n-nodes-base.set",
      "position": [
        440,
        6680
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "next_url",
              "value": "={{$json[\"headers\"][\"location\"]}}"
            }
          ]
        },
        "options": {},
        "keepOnlySet": true
      },
      "typeVersion": 1
    },
    {
      "id": "3fd9b50e-c30b-44dd-ac53-83b0a597db2e",
      "name": "Data 1 (product info)",
      "type": "n8n-nodes-base.set",
      "position": [
        440,
        6480
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "name",
              "value": "={{ $json.name }}"
            },
            {
              "name": "tagline",
              "value": "={{ $json.tagline }}"
            },
            {
              "name": "description",
              "value": "={{ $json.description }}"
            }
          ]
        },
        "options": {},
        "keepOnlySet": true
      },
      "typeVersion": 1
    },
    {
      "id": "68acc44b-10cd-4bae-bf01-b304cd753f15",
      "name": "Merge Data",
      "type": "n8n-nodes-base.function",
      "position": [
        660,
        6580
      ],
      "parameters": {
        "functionCode": "// Initialize empty arrays for both data sources\nlet productData = [];\nlet redirectData = [];\n\ntry {\n  productData = $items(\"Data to Keep4\");\n} catch (error) {\n  console.log(\"Error fetching product data:\", error.message);\n}\n\ntry {\n  redirectData = $items(\"Data to Keep3\");\n} catch (error) {\n  console.log(\"Error fetching redirect data:\", error.message);\n}\n\nconst mergedItems = [];\n\nfor (let i = 0; i < productData.length; i++) {\n  const product = productData[i].json;\n  \n  const mergedItem = {\n    name: product.name,\n    tagline: product.tagline,\n    description: product.description,\n    next_url: null\n  };\n  \n  if (i < redirectData.length && redirectData[i] && redirectData[i].json) {\n    let url = redirectData[i].json.next_url;\n    // Remove ?ref=producthunt from the URL\n    if (url && url.includes('?ref=producthunt')) {\n      url = url.replace('?ref=producthunt', '');\n    }\n    mergedItem.next_url = url;\n  }\n  \n  mergedItems.push({ json: mergedItem });\n}\n\nconsole.log(`Product data items: ${productData.length}`);\nconsole.log(`Redirect data items: ${redirectData.length}`);\nconsole.log(`Merged items: ${mergedItems.length}`);\n\nreturn mergedItems;"
      },
      "typeVersion": 1
    },
    {
      "id": "39429f34-19d1-488a-9603-7b25f6042fa6",
      "name": "Appends all details",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        880,
        6580
      ],
      "parameters": {
        "columns": {
          "value": {
            "name": "={{ $json.name }}",
            "tagline": "={{ $json.tagline }}",
            "description": "={{ $json.description }}"
          },
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
              "id": "tagline",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "tagline",
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
              "id": "next_url",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "next_url",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            }
          ],
          "mappingMode": "autoMapInputData",
          "matchingColumns": [
            "name"
          ],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {},
        "operation": "appendOrUpdate",
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": "gid=0",
          "cachedResultUrl": "demo",
          "cachedResultName": "Sheet1"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "demo",
          "cachedResultUrl": "demo",
          "cachedResultName": "Get product hunt products"
        },
        "authentication": "serviceAccount"
      },
      "typeVersion": 4.5
    },
    {
      "id": "6be5f1a1-c6e9-4dea-9199-523cd7f4b659",
      "name": "Sticky Note18",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -980,
        6380
      ],
      "parameters": {
        "width": 280,
        "height": 260,
        "content": "### About Me  \n\nHey there! I’m **Ajetomobi Ifeoluwa** – the brains (and vibe) behind this template. When I’m not crafting cool workflows, I’m busy making the web more beautiful and functional as a **UI/UX Designer** and **Vibe Coder**. Want your project to stand out? Let’s chat! Check out my [portfolio](https://ifeoluwaajetomobi.framer.website/) and my work on [Behance](https://www.behance.net/ajetomoifeoluw). Let’s create something awesome together! 🎨✨\n\n"
      },
      "typeVersion": 1
    }
  ],
  "pinData": {},
  "connections": {
    "Set Date1": {
      "main": [
        [
          {
            "node": "Fetches today’s Product Hunt posts via API.",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Merge Data": {
      "main": [
        [
          {
            "node": "Appends all details",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Daily Trigger1": {
      "main": [
        [
          {
            "node": "Set Date1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Data  2 (website url)": {
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
    "Data 1 (product info)": {
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
    "Extracts Product Info": {
      "main": [
        [
          {
            "node": "Resolve Website Redirection",
            "type": "main",
            "index": 0
          },
          {
            "node": "Data 1 (product info)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Resolve Website Redirection": {
      "main": [
        [
          {
            "node": "Data  2 (website url)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Fetches today’s Product Hunt posts via API.": {
      "main": [
        [
          {
            "node": "Extracts Product Info",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-1056"></a>

## Template 1056 - Criar ticket Zendesk para pedidos novos

- **Nome:** Criar ticket Zendesk para pedidos novos
- **Descrição:** Ao receber uma atualização de pedido, verifica se já existe um ticket correspondente no suporte; se não existir, cria um ticket em Zendesk com os detalhes do pedido.
- **Funcionalidade:** • Detecção de atualização de pedido: Inicia o fluxo quando um pedido é atualizado na loja.
• Busca de ticket existente: Pesquisa tickets no sistema de suporte usando o identificador externo (número do pedido) e status aberto.
• Extração de informações do ticket: Mantém apenas o ID e o external_id do ticket encontrado para uso posterior.
• Enriquecimento dos dados do pedido: Une as informações do pedido com os dados do ticket encontrado, relacionando pelo número do pedido.
• Verificação condicional: Se um ticket já existir para o pedido, não realiza nenhuma ação adicional.
• Criação de ticket novo: Se não houver ticket existente, cria um novo ticket no sistema de suporte com assunto, descrição e external_id associados ao pedido.
- **Ferramentas:** • Shopify: Plataforma de comércio eletrônico usada como fonte de eventos quando um pedido é atualizado.
• Zendesk: Plataforma de suporte ao cliente utilizada para pesquisar tickets existentes e criar novos tickets.



## Fluxo visual

```mermaid
flowchart LR
    N1["On order updated"]
    N2["Order exists in Zendesk"]
    N3["NoOp"]
    N4["Find if order already has a ticket in Zendesk"]
    N5["Keep only ticket Id"]
    N6["Add ticket info to order data"]
    N7["Create new ticket for new orders"]

    N1 --> N4
    N1 --> N6
    N5 --> N6
    N2 --> N3
    N2 --> N7
    N6 --> N2
    N4 --> N5
```

## Fluxo (.json) :

```json
{
  "meta": {
    "instanceId": "237600ca44303ce91fa31ee72babcdc8493f55ee2c0e8aa2b78b3b4ce6f70bd9"
  },
  "nodes": [
    {
      "id": "1b1fd43f-5acb-45e7-bd98-e4774754cdfe",
      "name": "On order updated",
      "type": "n8n-nodes-base.shopifyTrigger",
      "position": [
        180,
        520
      ],
      "webhookId": "0972ce92-d800-4049-ab60-7c71898ecbfa",
      "parameters": {
        "topic": "orders/updated"
      },
      "credentials": {
        "shopifyApi": {
          "id": "10",
          "name": "Shopify account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "d96cde15-f810-4302-aa45-554f6675b505",
      "name": "Order exists in Zendesk",
      "type": "n8n-nodes-base.if",
      "position": [
        1220,
        540
      ],
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{ $json[\"ZendeskTicketId\"] }}",
              "operation": "isNotEmpty"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "id": "62c09ef2-55c8-4269-9869-c15e8a955169",
      "name": "NoOp",
      "type": "n8n-nodes-base.noOp",
      "position": [
        1500,
        460
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "68f867c3-842c-478a-8afd-c7299e12b98d",
      "name": "Find if order already has a ticket in Zendesk",
      "type": "n8n-nodes-base.zendesk",
      "position": [
        480,
        660
      ],
      "parameters": {
        "options": {
          "query": "external_id:1027",
          "status": "open"
        },
        "operation": "getAll"
      },
      "credentials": {
        "zendeskApi": {
          "id": "5",
          "name": "Zendesk account"
        }
      },
      "typeVersion": 1,
      "alwaysOutputData": true
    },
    {
      "id": "01d4acba-8641-43e8-b333-e4494a2594d1",
      "name": "Keep only ticket Id",
      "type": "n8n-nodes-base.set",
      "position": [
        720,
        660
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "external_Id",
              "value": "={{ $json[\"external_id\"] }}"
            },
            {
              "name": "ZendeskTicketId",
              "value": "={{ $json[\"id\"] }}"
            }
          ]
        },
        "options": {},
        "keepOnlySet": true
      },
      "typeVersion": 1
    },
    {
      "id": "63099ec6-7ae5-4d88-881b-a6a8ae3a64b8",
      "name": "Add ticket info to order data",
      "type": "n8n-nodes-base.merge",
      "position": [
        960,
        540
      ],
      "parameters": {
        "mode": "mergeByKey",
        "propertyName1": "order_number",
        "propertyName2": "external_Id"
      },
      "typeVersion": 1
    },
    {
      "id": "79bf059e-d3b9-4323-88e5-7887deae74f7",
      "name": "Create new ticket for new orders",
      "type": "n8n-nodes-base.zendesk",
      "position": [
        1500,
        640
      ],
      "parameters": {
        "description": "=Order #{{ $json[\"order_number\"] }} - {{$json[\"line_items\"].length}} item(s)\n\nOrder:\nCustomer: {{$json[\"customer\"][\"first_name\"]}} {{$json[\"customer\"][\"last_name\"]}} \nemail: {{$json[\"customer\"][\"email\"]}}\nStatus: New order",
        "additionalFields": {
          "status": "open",
          "subject": "=Order #{{ $json[\"order_number\"] }} - {{$json[\"line_items\"].length}} item(s)",
          "externalId": "={{ $json[\"order_number\"] }}"
        }
      },
      "credentials": {
        "zendeskApi": {
          "id": "5",
          "name": "Zendesk account"
        }
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "On order updated": {
      "main": [
        [
          {
            "node": "Find if order already has a ticket in Zendesk",
            "type": "main",
            "index": 0
          },
          {
            "node": "Add ticket info to order data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Keep only ticket Id": {
      "main": [
        [
          {
            "node": "Add ticket info to order data",
            "type": "main",
            "index": 1
          }
        ]
      ]
    },
    "Order exists in Zendesk": {
      "main": [
        [
          {
            "node": "NoOp",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Create new ticket for new orders",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Add ticket info to order data": {
      "main": [
        [
          {
            "node": "Order exists in Zendesk",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Find if order already has a ticket in Zendesk": {
      "main": [
        [
          {
            "node": "Keep only ticket Id",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-1057"></a>

## Template 1057 - Criar pastas no Drive por caminho

- **Nome:** Criar pastas no Drive por caminho
- **Descrição:** Este fluxo cria pastas aninhadas no Google Drive a partir de um caminho informado, começando pela pasta de destino indicada, e retorna o ID da última pasta criada para uso imediato.
- **Funcionalidade:** • Gatilho de entrada: pode ser iniciado manualmente ou por um fluxo que o invoca.
• Processamento do caminho: divide o caminho em partes (pastas) para criar a hierarquia.
• Verificação da pasta superior: verifica se a pasta topo existe antes de criar subpastas.
• Criação de subpastas: cria a pasta no nível apropriado quando não existe.
• Loop de criação: repete a verificação/criação para cada nível do caminho.
• Retorno do ID final: retorna o ID da última pasta criada para uso posterior.
- **Ferramentas:** • Google Drive: Serviço de armazenamento em nuvem utilizado para criar, localizar e estruturar pastas no caminho especificado.
• Google Drive API: Interface de integração utilizada para realizar operações de criação e verificação de pastas durante o fluxo.



## Fluxo visual

```mermaid
flowchart LR
    N1["When clicking ‘Test workflow’"]
    N2["Set parameters for next run"]
    N3["Execute Workflow Trigger"]
    N4["Dummy input data"]
    N5["Split the desired path"]
    N6["Create desired path"]
    N7["Check if top folder exists"]
    N8["If top folder doesn't exist"]
    N9["Create new subfolder"]
    N10["If path has been completely created"]
    N11["Return the ID of the last folder"]
    N12["Sticky Note"]
    N13["Sticky Note1"]
    N14["Sticky Note2"]
    N15["Sticky Note3"]
    N16["Sticky Note4"]

    N4 --> N5
    N6 --> N7
    N9 --> N2
    N5 --> N6
    N3 --> N5
    N7 --> N8
    N8 --> N9
    N8 --> N2
    N2 --> N10
    N1 --> N4
    N10 --> N11
    N10 --> N6
```

## Fluxo (.json) :

```json
{
  "meta": {
    "instanceId": "4de3652773c3e67f6210deb1e1d390d75b23715f2e2cca0340008f99419607e6"
  },
  "nodes": [
    {
      "id": "4c9256c8-8dd7-4e81-8aef-0789e6808808",
      "name": "When clicking ‘Test workflow’",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        -260,
        80
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "1935ad6a-ade4-4073-9205-0c3dd1091c0f",
      "name": "Set parameters for next run",
      "type": "n8n-nodes-base.code",
      "position": [
        1520,
        460
      ],
      "parameters": {
        "mode": "runOnceForEachItem",
        "jsCode": "const desired_path = $('Create desired path').item.json.desired_path;\ndesired_path.shift();\n\nreturn {\n  desired_path: desired_path,\n  google_drive_folder_id: $json.id,\n}"
      },
      "typeVersion": 2
    },
    {
      "id": "5d99a9c4-57c6-4052-b093-fb0c32d9ff56",
      "name": "Execute Workflow Trigger",
      "type": "n8n-nodes-base.executeWorkflowTrigger",
      "position": [
        -40,
        460
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "879b92ae-edab-4d73-96d0-4df36d12fbb2",
      "name": "Dummy input data",
      "type": "n8n-nodes-base.set",
      "position": [
        -40,
        80
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "041e1077-f4dc-476f-b75a-6d60d9c8d0b9",
              "name": "google_drive_folder_id",
              "type": "string",
              "value": "root"
            },
            {
              "id": "843e3a7f-c59e-48c1-80f8-c9995515e340",
              "name": "desired_path",
              "type": "string",
              "value": "testXavier/2024/Q4/03 Documenten"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "822d45f1-149d-430c-8daf-183998c01166",
      "name": "Split the desired path",
      "type": "n8n-nodes-base.code",
      "position": [
        340,
        260
      ],
      "parameters": {
        "mode": "runOnceForEachItem",
        "jsCode": "// Add a new field called 'myNewField' to the JSON of the item\n$input.item.json.desired_path = $input.item.json.desired_path.split('/');\n\nreturn $input.item;"
      },
      "typeVersion": 2
    },
    {
      "id": "e2aba13a-fec6-4d1e-aa1c-af95d3f957ad",
      "name": "Create desired path",
      "type": "n8n-nodes-base.code",
      "position": [
        580,
        260
      ],
      "parameters": {
        "mode": "runOnceForEachItem",
        "jsCode": "return {\n  google_drive_folder_id: $json.google_drive_folder_id,\n  desired_path: $json.desired_path,\n};"
      },
      "typeVersion": 2
    },
    {
      "id": "aa3f9b95-3197-4b89-bcb2-9e723b8496a0",
      "name": "Check if top folder exists",
      "type": "n8n-nodes-base.googleDrive",
      "position": [
        800,
        260
      ],
      "parameters": {
        "filter": {
          "folderId": {
            "__rl": true,
            "mode": "id",
            "value": "={{ $json.google_drive_folder_id }}"
          },
          "whatToSearch": "folders"
        },
        "options": {},
        "resource": "fileFolder",
        "queryString": "={{ $json.desired_path[0] }}"
      },
      "credentials": {
        "googleDriveOAuth2Api": {
          "id": "Xk1mfDiQRaqwWUaU",
          "name": "Google Drive account 2"
        }
      },
      "typeVersion": 3,
      "alwaysOutputData": true
    },
    {
      "id": "969b7823-2720-45c5-b98c-1cc659fe62df",
      "name": "If top folder doesn't exist",
      "type": "n8n-nodes-base.if",
      "position": [
        1040,
        260
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
              "id": "59e55ba1-5db4-455e-95a1-bb8e4c1d0d31",
              "operator": {
                "type": "object",
                "operation": "empty",
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
      "id": "2cd3932d-b066-438a-b968-4078dfc9dbe7",
      "name": "Create new subfolder",
      "type": "n8n-nodes-base.googleDrive",
      "position": [
        1340,
        240
      ],
      "parameters": {
        "name": "={{ $('Create desired path').item.json.desired_path[0] }}",
        "driveId": {
          "__rl": true,
          "mode": "list",
          "value": "My Drive"
        },
        "options": {},
        "folderId": {
          "__rl": true,
          "mode": "id",
          "value": "={{ $('Create desired path').item.json.google_drive_folder_id }}"
        },
        "resource": "folder"
      },
      "credentials": {
        "googleDriveOAuth2Api": {
          "id": "Xk1mfDiQRaqwWUaU",
          "name": "Google Drive account 2"
        }
      },
      "typeVersion": 3
    },
    {
      "id": "f9322682-b77f-4bad-8bbc-13868c126063",
      "name": "If path has been completely created",
      "type": "n8n-nodes-base.if",
      "position": [
        1740,
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
              "id": "d95b4b2e-68c5-4d82-84af-a46fbb84035c",
              "operator": {
                "type": "array",
                "operation": "empty",
                "singleValue": true
              },
              "leftValue": "={{ $json.desired_path }}",
              "rightValue": ""
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "94c4694b-0a32-4681-b977-c01e3232d9e8",
      "name": "Return the ID of the last folder",
      "type": "n8n-nodes-base.set",
      "position": [
        2040,
        440
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "692a23db-71c8-4154-af87-a0177045b63d",
              "name": "google_drive_folder_id",
              "type": "string",
              "value": "={{ $('Set parameters for next run').item.json.google_drive_folder_id }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "5e9f327d-61bb-46af-b16b-21499f5c22e0",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -820,
        -80
      ],
      "parameters": {
        "width": 480,
        "height": 880,
        "content": "# Create Google Drive Folders by Path\nThis workflow created nested Google Drive folder from a path string and returns the ID of the final folder for immediate use.\n\nUse this workflow in your other flows by calling it directly with the following data:\n- `google_drive_folder_id` -> The ID of the folder where you want to create additional folders in. You can use \"root\" if you want to begin at root level of your Drive.\n- `desired_path` -> The folder structure you'd like to create in Google Drive. Each folder is separated by a slash, eg: `Projects/Clients/Reports`"
      },
      "typeVersion": 1
    },
    {
      "id": "35b3741f-465a-4846-9f62-4dedc40ca884",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -280,
        -20
      ],
      "parameters": {
        "color": 5,
        "width": 500,
        "height": 80,
        "content": "## Test data for the workflow\nUse this in case you want to test the workflow."
      },
      "typeVersion": 1
    },
    {
      "id": "3b7fe210-d966-4988-aaf4-5e07567b3054",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -280,
        320
      ],
      "parameters": {
        "color": 5,
        "width": 500,
        "height": 120,
        "content": "## Triggered from another workflow\nThis workflow is intended to be triggered by other workflows. Don't copy/paste this workflow as it will be more difficult to maintain and keep up-to-date."
      },
      "typeVersion": 1
    },
    {
      "id": "16477e77-656e-4bff-914f-633d61477d38",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        560,
        80
      ],
      "parameters": {
        "color": 5,
        "width": 1320,
        "height": 120,
        "content": "## Main loop\nTake the desired_path and split it into parts. Eg: `Projects/Clients/Reports` will turn into 3 parts: Projects, Clients, Reports.\nWe then check if the top folder exists and create it if not. We repeat this process until all subfolders have been created and correctly nested."
      },
      "typeVersion": 1
    },
    {
      "id": "57404f59-28b8-4969-b483-fb8a3320a592",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1980,
        80
      ],
      "parameters": {
        "color": 5,
        "width": 280,
        "height": 120,
        "content": "## Rerturn data\nHere we return the ID of the last folder in the path, so you can start uploading new files to it."
      },
      "typeVersion": 1
    }
  ],
  "pinData": {},
  "connections": {
    "Dummy input data": {
      "main": [
        [
          {
            "node": "Split the desired path",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Create desired path": {
      "main": [
        [
          {
            "node": "Check if top folder exists",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Create new subfolder": {
      "main": [
        [
          {
            "node": "Set parameters for next run",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Split the desired path": {
      "main": [
        [
          {
            "node": "Create desired path",
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
            "node": "Split the desired path",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Check if top folder exists": {
      "main": [
        [
          {
            "node": "If top folder doesn't exist",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "If top folder doesn't exist": {
      "main": [
        [
          {
            "node": "Create new subfolder",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Set parameters for next run",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set parameters for next run": {
      "main": [
        [
          {
            "node": "If path has been completely created",
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
            "node": "Dummy input data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "If path has been completely created": {
      "main": [
        [
          {
            "node": "Return the ID of the last folder",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Create desired path",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-1058"></a>

## Template 1058 - Notificação de erro via Telegram

- **Nome:** Notificação de erro via Telegram
- **Descrição:** Envia uma notificação no Telegram quando uma execução falha, informando o nome do fluxo e o link da execução.
- **Funcionalidade:** • Detecção de erro: Aciona automaticamente ao ocorrer uma falha em uma execução.
• Formatação de mensagem: Gera uma mensagem contendo o nome do fluxo e o link da execução para facilitar investigação.
• Envio de notificação via Telegram: Envia a mensagem para um chat configurado usando credenciais de bot.
• Configuração de destinatário e credenciais: Permite definir o chat id e o token do bot para direcionar a notificação.
- **Ferramentas:** • Telegram: Plataforma de mensagens utilizada para enviar notificações por meio de um bot para um chat específico.



## Fluxo visual

```mermaid
flowchart LR
    N1["On Error"]
    N2["Set message"]
    N3["Sticky Note3"]
    N4["Telegram"]
    N5["Sticky Note"]

    N1 --> N2
    N2 --> N4
```

## Fluxo (.json) :

```json
{
  "nodes": [
    {
      "id": "aa84d631-c14f-45c2-a659-454605e83c30",
      "name": "On Error",
      "type": "n8n-nodes-base.errorTrigger",
      "position": [
        880,
        900
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "abffce17-cc93-4c6a-8955-de2d0f4cc885",
      "name": "Set message",
      "type": "n8n-nodes-base.set",
      "position": [
        1140,
        900
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "message",
              "value": "=⚠️ Workflow `{{$json[\"workflow\"][\"name\"]}}` failed to run! [execution]({{ $json.execution.url }})"
            }
          ]
        },
        "options": {},
        "keepOnlySet": true
      },
      "typeVersion": 1
    },
    {
      "id": "1e5c4af6-30ae-45b8-bca7-048a656ce9bd",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        800,
        700
      ],
      "parameters": {
        "color": 5,
        "width": 424.4907862645661,
        "height": 154.7766688696994,
        "content": "### 👨‍🎤 Setup\n1. Add Telegram creds\n2. Set chat id in **Telegram** node\n2. Add this error workflow to other workflows\nhttps://docs.n8n.io/flow-logic/error-handling/#create-and-set-an-error-workflow"
      },
      "typeVersion": 1
    },
    {
      "id": "845ddf26-2d40-4cc6-843b-ccb3b365fbfb",
      "name": "Telegram",
      "type": "n8n-nodes-base.telegram",
      "position": [
        1360,
        900
      ],
      "parameters": {
        "text": "={{ $json.message }}",
        "chatId": "1688282582",
        "additionalFields": {
          "appendAttribution": false
        }
      },
      "credentials": {
        "telegramApi": {
          "id": "6",
          "name": "mymontsbot token"
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "90db96b8-0e43-4977-b455-3e6813211640",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1380,
        1080
      ],
      "parameters": {
        "width": 241,
        "height": 80,
        "content": "### 👆🏽 Set chat id here"
      },
      "typeVersion": 1
    }
  ],
  "pinData": {},
  "connections": {
    "On Error": {
      "main": [
        [
          {
            "node": "Set message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set message": {
      "main": [
        [
          {
            "node": "Telegram",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-1059"></a>

## Template 1059 - Previsão do tempo via Slack

- **Nome:** Previsão do tempo via Slack
- **Descrição:** Recebe uma localização por webhook, obtém a previsão meteorológica para essa posição e publica o resultado em um canal do Slack.
- **Funcionalidade:** • Recepção de comandos via webhook: Aceita texto com a localização enviada ao webhook.
• Geocodificação: Converte o texto da localização em coordenadas (latitude/longitude) usando um serviço de busca.
• Obtenção de pontos meteorológicos: Consulta a API meteorológica para obter gridId, gridX e gridY a partir das coordenadas.
• Recuperação da previsão: Solicita a previsão de tempo para o grid identificado e extrai os períodos de previsão.
• Formatação da mensagem: Monta uma mensagem com nome do período, temperatura, direção e velocidade do vento e resumo curto do tempo.
• Publicação no Slack com OAuth2: Envia a previsão formatada para um canal do Slack utilizando autenticação OAuth2.
• Inclusão de cabeçalhos personalizados: Adiciona cabeçalho User-Agent nas requisições externas para identificação.
- **Ferramentas:** • Slack: Plataforma de mensagens usada para receber comandos e publicar a previsão em um canal.
• OpenStreetMap (Nominatim): Serviço de geocodificação usado para transformar o texto da localização em coordenadas.
• National Weather Service (api.weather.gov): API oficial usada para obter os pontos de grade e a previsão meteorológica.



## Fluxo visual

```mermaid
flowchart LR
    N1["Webhook"]
    N2["Slack"]
    N3["OpenStreetMap"]
    N4["NWS"]
    N5["NWS1"]

    N4 --> N5
    N5 --> N2
    N1 --> N3
    N3 --> N4
```

## Fluxo (.json) :

```json
{
  "id": "B6UHILmjPWa7ViQ4",
  "meta": {
    "instanceId": "ecc960f484e18b0e09045fd93acf0d47f4cfff25cc212ea348a08ac3aae81850",
    "templateCredsSetupCompleted": true
  },
  "name": "Weather via Slack",
  "tags": [
    {
      "id": "2KlkHxhULPP42BS6",
      "name": "App 72",
      "createdAt": "2025-02-19T21:15:27.390Z",
      "updatedAt": "2025-02-19T21:15:27.390Z"
    },
    {
      "id": "aw8suPYTKfXDtMZl",
      "name": "Utility",
      "createdAt": "2025-02-10T14:41:49.045Z",
      "updatedAt": "2025-02-10T14:41:49.045Z"
    }
  ],
  "nodes": [
    {
      "id": "9aea370b-7eb9-4742-9663-6628513e4de3",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "position": [
        -340,
        -300
      ],
      "webhookId": "41a60a4f-66d0-433b-aa43-b225dffa6761",
      "parameters": {
        "path": "slack1",
        "options": {},
        "httpMethod": "POST"
      },
      "typeVersion": 2
    },
    {
      "id": "c982487f-076a-48e8-9a35-78e8fbfb8936",
      "name": "Slack",
      "type": "n8n-nodes-base.slack",
      "position": [
        560,
        -300
      ],
      "webhookId": "4840f197-e116-4ef5-9372-0abd063e4aad",
      "parameters": {
        "text": "={{\n  JSON.parse($node[\"NWS1\"].json.data).properties.periods\n  .map(period => \n    `*${period.name}*\\n` +\n    `Temp: ${period.temperature}°${period.temperatureUnit}\\n` +\n    `Wind: ${period.windSpeed} ${period.windDirection}\\n` +\n    `Forecast: ${period.shortForecast}`\n  )\n  .join(\"\\n\\n\")\n}}\n",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "mode": "list",
          "value": "C0889718P8S",
          "cachedResultName": "n8n"
        },
        "otherOptions": {},
        "authentication": "oAuth2"
      },
      "credentials": {
        "slackOAuth2Api": {
          "id": "GSiEiuKBz8GR5qiD",
          "name": "AlexK Slack account"
        }
      },
      "typeVersion": 2.3
    },
    {
      "id": "7d42112a-0590-4a09-ba0e-dbdf1eddccf2",
      "name": "OpenStreetMap",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        -100,
        -300
      ],
      "parameters": {
        "url": "https://nominatim.openstreetmap.org/search",
        "options": {
          "response": {
            "response": {
              "fullResponse": true
            }
          }
        },
        "sendQuery": true,
        "sendHeaders": true,
        "queryParameters": {
          "parameters": [
            {
              "name": "q",
              "value": "={{ $('Webhook').item.json.body.text }}"
            },
            {
              "name": "format",
              "value": "json"
            }
          ]
        },
        "headerParameters": {
          "parameters": [
            {
              "name": "User-Agent",
              "value": "alexk1919 (alex@alexk1919.com)"
            }
          ]
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "565a0123-9059-4e6e-be97-96e0875c1b84",
      "name": "NWS",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        120,
        -300
      ],
      "parameters": {
        "url": "=https://api.weather.gov/points/{{ $json.body[0].lat }},{{ $json.body[0].lon }}",
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
              "name": "User-Agent",
              "value": "alexk1919 (alex@alexk1919.com)"
            }
          ]
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "3505e6c2-6e66-4abd-a1bb-75a1d8fc9a08",
      "name": "NWS1",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        340,
        -300
      ],
      "parameters": {
        "url": "=https://api.weather.gov/gridpoints/{{$json[\"data\"] ? JSON.parse($json[\"data\"]).properties.gridId : \"\"}}\n/{{$json[\"data\"] ? JSON.parse($json[\"data\"]).properties.gridX : \"\"}}\n,{{$json[\"data\"] ? JSON.parse($json[\"data\"]).properties.gridY : \"\"}}\n/forecast",
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
              "name": "User-Agent",
              "value": "alexk1919 (alex@alexk1919.com)"
            }
          ]
        }
      },
      "typeVersion": 4.2
    }
  ],
  "active": true,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "4244c90f-02e9-42fc-9873-3f8074f6ecf4",
  "connections": {
    "NWS": {
      "main": [
        [
          {
            "node": "NWS1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "NWS1": {
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
    "Slack": {
      "main": [
        []
      ]
    },
    "Webhook": {
      "main": [
        [
          {
            "node": "OpenStreetMap",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenStreetMap": {
      "main": [
        [
          {
            "node": "NWS",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

<a id="template-1060"></a>

## Template 1060 - Obter informações e filtrar servidores Scaleway

- **Nome:** Obter informações e filtrar servidores Scaleway
- **Descrição:** Recupera e consolida informações de servidores (instâncias e baremetal) de várias zonas do Scaleway e permite filtrar os resultados por critérios como tags, nome, IP público ou zona, retornando-os via webhook autenticado.
- **Funcionalidade:** • Recuperação por zona: realiza chamadas às APIs do Scaleway para obter servidores de zonas configuradas.
• Suporte a instâncias e baremetal: identifica zonas configuradas para baremetal e utiliza o endpoint apropriado.
• Normalização e agregação de dados: extrai e unifica campos essenciais (nome, tags, IP público, tipo, estado, zona, usuário) em um único dataset.
• Filtragem dinâmica: permite filtrar os servidores por tags, nome, IP público ou zona com base em parâmetros recebidos.
• Entrada via webhook autenticado: recebe requisições externas (POST) com autenticação básica contendo os parâmetros de busca (search_by e search).
• Tratamento de erros: retorna uma resposta clara quando o critério de busca é inválido, listando as opções válidas.
• Configuração centralizada: usa campos configuráveis para definir listas de zonas e o token de autenticação do Scaleway.
- **Ferramentas:** • Scaleway API: API pública usada para consultar instâncias e servidores baremetal por zona.
• Consola Scaleway (API Tokens): interface para criar e obter o token de API necessário para autenticação.
• Serviço HTTP/Webhook: endpoint externo para receber requisições de entrada e enviar as respostas (ex.: webhook HTTP usado para integração com sistemas externos).



## Fluxo visual

```mermaid
flowchart LR
    N1["Code"]
    N2["Edit Fields"]
    N3["Switch"]
    N4["Code search Tags"]
    N5["Code search Name"]
    N6["Code search public_ip"]
    N7["Code search zone"]
    N8["Webhook"]
    N9["Respond Error"]
    N10["Respond to Webhook1"]
    N11["Respond to Webhook2"]
    N12["Respond to Webhook3"]
    N13["Respond to Webhook"]
    N14["Sticky Note"]
    N15["Sticky Note1"]
    N16["Get Scalway Machines"]
    N17["Loop Over Items"]
    N18["Respond to Webhook4"]
    N19["Get scw instance by zone"]
    N20["Loop Over Zone Instance"]
    N21["Get scw baremetal by zone"]
    N22["Split Out ZONE_INSTANCE"]
    N23["If ZONE_BAREMETAL in ZONE_INSTANCE"]
    N24["Sticky Note2"]

    N1 --> N3
    N3 --> N4
    N3 --> N5
    N3 --> N6
    N3 --> N7
    N3 --> N18
    N3 --> N9
    N8 --> N2
    N2 --> N22
    N5 --> N10
    N4 --> N13
    N7 --> N12
    N16 --> N17
    N6 --> N11
    N20 --> N1
    N20 --> N19
    N22 --> N20
    N19 --> N23
    N21 --> N20
    N23 --> N21
    N23 --> N20
```

## Fluxo (.json) :

```json
{
  "id": "olDVR3wuxbUsTvuW",
  "meta": {
    "instanceId": "598c730c3a95b29c8be35b1b34a362ffa595154754b692ab1bb4baa1db7b1f33",
    "templateCredsSetupCompleted": true
  },
  "name": "Get all scaleway server info copy",
  "tags": [],
  "nodes": [
    {
      "id": "9da28130-ed83-4129-b65c-82969fe3126d",
      "name": "Code",
      "type": "n8n-nodes-base.code",
      "position": [
        2000,
        -60
      ],
      "parameters": {
        "jsCode": "// Function to extract essential information from servers\nfunction extractServers(serversArray) {\n    let servers = [];\n\n    if (!Array.isArray(serversArray)) {\n        console.log(\"⚠️ Invalid data received:\", JSON.stringify(serversArray, null, 2));\n        return servers; // Returns an empty array if the data is not valid\n    }\n\n    serversArray.forEach(server => {\n        servers.push({\n            name: server.name || \"Unknown\",\n            tags: server.tags && server.tags.length > 0 ? server.tags.join(\", \") : \"No tags\",\n            public_ip: getPublicIPs(server),\n            type: server.commercial_type || server.offer_name || \"Unknown\", // Baremetal does not have commercial_type, but offer_name\n            state: server.state || server.status || \"Unknown\", // Baremetal uses status instead of state\n            zone: server.zone || \"Unknown\",\n            user: getUser(server) // User management\n        });\n    });\n\n    return servers;\n}\n\n// Function to extract the public IP (IPv4 prioritized, otherwise IPv6)\nfunction getPublicIPs(server) {\n    let ipv4 = null;\n    let ipv6 = null;\n\n    // Case for Compute instances (public_ips is an array)\n    if (server.public_ips && Array.isArray(server.public_ips)) {\n        server.public_ips.forEach(ip => {\n            if (ip.family === \"inet\" && !ipv4) ipv4 = ip.address;\n            if (ip.family === \"inet6\" && !ipv6) ipv6 = ip.address;\n        });\n    }\n\n    // Some instances have public_ip as a single object\n    if (server.public_ip && server.public_ip.address) {\n        if (server.public_ip.family === \"inet\" && !ipv4) ipv4 = server.public_ip.address;\n        if (server.public_ip.family === \"inet6\" && !ipv6) ipv6 = server.public_ip.address;\n    }\n\n    // Case for Baremetal servers (ips is an array)\n    if (server.ips && Array.isArray(server.ips)) {\n        server.ips.forEach(ip => {\n            if (ip.version === \"IPv4\" && !ipv4) ipv4 = ip.address;\n            if (ip.version === \"IPv6\" && !ipv6) ipv6 = ip.address;\n        });\n    }\n\n    // Returns IPv4 if available, otherwise IPv6, otherwise \"No IP\"\n    return ipv4 || ipv6 || \"No IP\";\n}\n\n// Function to retrieve the user\nfunction getUser(server) {\n    // For Compute instances, the \"user\" field sometimes exists\n    if (server.user) return server.user;\n\n    // For Baremetal servers, user info is often found in install.user\n    if (server.install && server.install.user) return server.install.user;\n\n    // Default value\n    return \"root\";\n}\n\n// Retrieve all input items (from Loop Over Zone Instance)\nlet inputItems = $input.all();\nlet allServers = [];\n\n// Iterate over each item and extract servers if they are contained in a \"servers\" property\ninputItems.forEach(item => {\n    if (item.json.servers && Array.isArray(item.json.servers)) {\n        allServers = allServers.concat(extractServers(item.json.servers));\n    } else {\n        // If the item does not have a \"servers\" property, attempt to process the object itself as a server\n        allServers = allServers.concat(extractServers([item.json]));\n    }\n});\n\n// Return the final result as items (JSON object per server)\nreturn allServers.map(server => ({ json: server }));\n"
      },
      "typeVersion": 2,
      "alwaysOutputData": true
    },
    {
      "id": "12e10b9e-99ca-4ab8-b90d-be318ba2f9ff",
      "name": "Edit Fields",
      "type": "n8n-nodes-base.set",
      "position": [
        880,
        0
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "e6764348-1fa6-439e-9279-3b423c7c73af",
              "name": "search_by",
              "type": "string",
              "value": "={{ $json.body.search_by }}"
            },
            {
              "id": "5535e47b-c187-47eb-80af-bccb3972f4a5",
              "name": "search",
              "type": "string",
              "value": "={{ $json.body.search }}"
            },
            {
              "id": "b69ff3d1-885e-4145-a277-074b8e517aaf",
              "name": "Scaleway-X-Auth-Token",
              "type": "string",
              "value": "<Your personal Scaleway X Auth Token>"
            },
            {
              "id": "65ee376e-093f-4a8b-abe8-5d9173d26427",
              "name": "ZONE_INSTANCE",
              "type": "array",
              "value": "[\"fr-par-1\", \"fr-par-2\", \"fr-par-3\", \"nl-ams-1\", \"nl-ams-2\", \"nl-ams-3\", \"pl-waw-1\", \"pl-waw-2\", \"pl-waw-3\"]"
            },
            {
              "id": "9a9fff0b-f812-4bb1-800e-2376b39381ed",
              "name": "ZONE_BAREMETAL",
              "type": "string",
              "value": "[\"fr-par-1\", \"fr-par-2\", \"nl-ams-1\", \"nl-ams-2\", \"pl-waw-2\", \"pl-waw-3\"]"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "20398633-d856-4700-98a9-1f722f3d2a8f",
      "name": "Switch",
      "type": "n8n-nodes-base.switch",
      "position": [
        2260,
        -80
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
                    "id": "7ee5d5ae-3a88-4bef-820d-979c26499cbd",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $('Edit Fields').first().json.search_by }}",
                    "rightValue": "tags"
                  }
                ]
              }
            },
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
                    "id": "eb879619-5b97-4402-b3de-3f98e0a7d0d3",
                    "operator": {
                      "name": "filter.operator.equals",
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $('Edit Fields').first().json.search_by }}",
                    "rightValue": "name"
                  }
                ]
              }
            },
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
                    "id": "2d0b6397-e46d-484a-84a0-7af8d7345dea",
                    "operator": {
                      "name": "filter.operator.equals",
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $('Edit Fields').first().json.search_by }}",
                    "rightValue": "public_ip"
                  }
                ]
              }
            },
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
                    "id": "0ee8fb2d-cf38-4994-a49a-88c7482b46ab",
                    "operator": {
                      "name": "filter.operator.equals",
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $('Edit Fields').first().json.search_by }}",
                    "rightValue": "zone"
                  }
                ]
              }
            },
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
                    "id": "04a298b2-2a22-433a-a8db-3902dcff0425",
                    "operator": {
                      "name": "filter.operator.equals",
                      "type": "string",
                      "operation": "equals"
                    },
                    "leftValue": "={{ $('Edit Fields').first().json.search_by }}",
                    "rightValue": "null"
                  }
                ]
              }
            }
          ]
        },
        "options": {
          "ignoreCase": false,
          "fallbackOutput": "extra"
        }
      },
      "typeVersion": 3.2
    },
    {
      "id": "f480f721-d2b3-49a4-9211-266af3e8fd42",
      "name": "Code search Tags",
      "type": "n8n-nodes-base.code",
      "position": [
        2680,
        -500
      ],
      "parameters": {
        "jsCode": "// Retrieve all input items\nlet servers = $input.all();\n\n// Filter only servers with the tag \"STAGING\"\nlet filteredServers = servers.filter(server =>\n    server.json.tags && server.json.tags.includes($('Edit Fields').first().json.search)\n);\n\n// Return only servers that have \"search\" in the tags\nreturn filteredServers;\n"
      },
      "typeVersion": 2,
      "alwaysOutputData": true
    },
    {
      "id": "44ee26b2-1320-44a6-a705-ff102e789a9c",
      "name": "Code search Name",
      "type": "n8n-nodes-base.code",
      "position": [
        2680,
        -340
      ],
      "parameters": {
        "jsCode": "// Retrieve all input items\nlet servers = $input.all();\n\n// Filter only servers with the tag \"STAGING\"\nlet filteredServers = servers.filter(server =>\n    server.json.name && server.json.name.includes($('Edit Fields').first().json.search)\n);\n\n// Return only servers that have \"search\" in the name\nreturn filteredServers;\n"
      },
      "typeVersion": 2,
      "alwaysOutputData": true
    },
    {
      "id": "b8e5f1b5-09a0-42f8-a5d6-a10989cb9f81",
      "name": "Code search public_ip",
      "type": "n8n-nodes-base.code",
      "position": [
        2680,
        -180
      ],
      "parameters": {
        "jsCode": "// Retrieve all input items\nlet servers = $input.all();\n\n// Filter only servers with the tag \"STAGING\"\nlet filteredServers = servers.filter(server =>\n    server.json.public_ip && server.json.public_ip.includes($('Edit Fields').first().json.search)\n);\n\n// Return only servers that have \"search\" in the public_ip\nreturn filteredServers;\n"
      },
      "typeVersion": 2,
      "alwaysOutputData": true
    },
    {
      "id": "1029d9bc-8d42-4038-9dfe-f8957e9115b6",
      "name": "Code search zone",
      "type": "n8n-nodes-base.code",
      "position": [
        2680,
        -20
      ],
      "parameters": {
        "jsCode": "// Retrieve all input items\nlet servers = $input.all();\n\n// Filter only servers with the tag \"STAGING\"\nlet filteredServers = servers.filter(server =>\n    server.json.public_ip && server.json.public_ip.includes($('Edit Fields').first().json.search)\n);\n\n// Return only servers that have \"search\" in the public_ip\nreturn filteredServers;\n"
      },
      "typeVersion": 2,
      "alwaysOutputData": true
    },
    {
      "id": "3dae20ba-07b2-4948-a58c-8b803f672dcb",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "position": [
        660,
        0
      ],
      "webhookId": "a6767312-3a4c-4819-b4fe-a03c9e0ade5c",
      "parameters": {
        "path": "a6767312-3a4c-4819-b4fe-a03c9e0ade5c",
        "options": {},
        "httpMethod": "POST",
        "responseMode": "responseNode",
        "authentication": "basicAuth"
      },
      "credentials": {
        "httpBasicAuth": {
          "id": "YzpBkNOC0UnKboCn",
          "name": "Endpoint Get server scalway info"
        }
      },
      "typeVersion": 2
    },
    {
      "id": "65f62d8f-aead-47cb-a9df-105054d8b666",
      "name": "Respond Error",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        2680,
        300
      ],
      "parameters": {
        "options": {},
        "respondWith": "json",
        "responseBody": "={\n  \"error\": \"no search by {{ $('Edit Fields').item.json.search_by }} available. You can search by : tags, name, public_ip, zone\"\n}"
      },
      "typeVersion": 1.1
    },
    {
      "id": "9d8db89d-c318-4078-9a3d-8bc10022d059",
      "name": "Respond to Webhook1",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        2900,
        -340
      ],
      "parameters": {
        "options": {},
        "respondWith": "allIncomingItems"
      },
      "typeVersion": 1.1
    },
    {
      "id": "3009a593-8a23-448c-b8fd-58c6fc4b77b3",
      "name": "Respond to Webhook2",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        2900,
        -180
      ],
      "parameters": {
        "options": {},
        "respondWith": "allIncomingItems"
      },
      "typeVersion": 1.1
    },
    {
      "id": "27e1f543-c57c-4772-944b-d2207526dd9d",
      "name": "Respond to Webhook3",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        2900,
        -20
      ],
      "parameters": {
        "options": {},
        "respondWith": "allIncomingItems"
      },
      "typeVersion": 1.1
    },
    {
      "id": "90e51c36-9888-4942-ad13-28fa90235d13",
      "name": "Respond to Webhook",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        2900,
        -500
      ],
      "parameters": {
        "options": {},
        "respondWith": "allIncomingItems"
      },
      "typeVersion": 1.1
    },
    {
      "id": "92ad3cf2-c3b3-4c42-9d1b-7d55f3e5ad56",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1000,
        -1240
      ],
      "parameters": {
        "color": 4,
        "width": 1000,
        "height": 1080,
        "content": "# Technical Documentation\n\n## Description\n\nThis n8n workflow retrieves information about Scaleway servers—both instances and baremetal—from dynamically defined zones. It collects server details from the Scaleway API, aggregates them into a single dataset, and allows filtering of the results based on user-defined criteria (such as name, tags, public IP address, or zone) before returning the data via a webhook.\n\n## Operation\n\n### 1. Workflow Trigger\n\n- **Webhook Activation:**\n  The workflow is triggered by a Webhook node that listens for an HTTP POST request. This request uses basic authentication (basicAuth) and includes the search parameters:\n  - `search_by`: The filter type (e.g., \"tags\", \"name\", \"public_ip\", or \"zone\").\n  - `search`: The keyword to filter the server data.\n\n### 2. Retrieving Server Information\n\n- **HTTP Requests to Scaleway API:**\n  The workflow makes HTTP GET requests to two main Scaleway API endpoints:\n  - **Instances Endpoint:** Retrieves server instances from zones specified under the `ZONE_INSTANCE` variable.\n  - **Baremetal Endpoint:** Retrieves baremetal server information from zones defined in the `ZONE_BAREMETAL` variable.\n  - **Headers and Authentication:**\n    Each request sends the `X-Auth-Token` header along with a `Content-Type: application/json` header and expects a JSON response from the API.\n\n### 3. Data Processing\n\n- **Zone Splitting and Iteration:**\n  - A `Split Out ZONE_INSTANCE` node divides the list of predefined zones so each zone is processed separately.\n  - The `Loop Over Zone Instance` node iterates over the zones. An `If ZONE_BAREMETAL in ZONE_INSTANCE` node checks whether the current zone is configured for baremetal servers; if so, it directs the flow to the corresponding baremetal API request, otherwise to the instance request.\n  - **Aggregating and Structuring Data:**\n    The `Code` node aggregates all responses from each zone. It:\n    - Iterates over the incoming items.\n    - Uses helper functions (`extractServers`, `getPublicIPs`, `getUser`) to extract and normalize key information (name, tags, public IP, server type, state, zone, user).\n    - Consolidates the structured server information into a unified array for further processing.\n\n### 4. Dynamic Filtering\n\n- **Defining Search Criteria:**\n  A `Set` node captures the incoming search parameters (`search_by` and `search`) along with configuration details, such as the Scaleway authentication token and the lists of applicable zones.\n  - **Routing Based on Filter Type:**\n    The `Switch` node analyzes the value of `search_by` and routes the aggregated server data to one of four dedicated `Code` nodes that filter the data according to:\n    - `tags`\n    - `name`\n    - `public_ip`\n    - `zone`\n  - **Error Handling:**\n    If the `search_by` value does not match any of the valid filters, an error response is generated via a dedicated node that returns a JSON error message listing the available filter options.\n\n### 5. Response via Webhook\n\n- **Returning the Filtered Data:**\n  The filtered server data is sent back to the requester via one of several `Respond to Webhook` nodes assigned to handle the output from each filter type.\n  - **Error Response:**\n    In cases where no valid search criteria are provided, the workflow sends an error JSON response indicating that the valid filters are: `tags`, `name`, `public_ip`, and `zone`.\n\n## Example Usage\n\nTo use the workflow from an application or another workflow, send a POST request to the webhook endpoint with a JSON payload similar to this:\n\n```json\n{\n  \"search_by\": \"tags\",\n  \"search\": \"Apiv1\"\n}\n```\n\nIf executed successfully, the workflow will return a JSON array with server objects. Each object includes properties such as:\n- `name`\n- `tags`\n- `public_ip`\n- `type`\n- `state`\n- `zone`\n- `user`"
      },
      "typeVersion": 1
    },
    {
      "id": "0fc94a1e-2cb3-47d7-a198-a053b2bed8e4",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1060,
        520
      ],
      "parameters": {
        "width": 960,
        "height": 660,
        "content": "# Usage in an External App or Another Workflow\n\nTo integrate this part of the workflow into your application or another workflow:\n\n1. **Send a POST Request:**\n   Use the Get Scalway Machines node’s endpoint (displayed under the node) to send a POST request containing the search criteria. For example:\n\n   ```json\n   {\n     \"search_by\": \"tags\",\n     \"search\": \"Apiv1\"\n   }\n   ```\n\n2. **Process the Results:**\n   The Loop Over Items node will iterate over each response item, allowing you to handle multiple servers or records in one run.\n\n3. **Receive the Filtered Data:**\n   The returned data (each item representing a server) can then be processed further in your application or workflow, giving you a quick, automated way to retrieve and filter Scaleway server information."
      },
      "typeVersion": 1
    },
    {
      "id": "d54772b2-40e7-43ff-9c4c-d4bbf176c3c2",
      "name": "Get Scalway Machines",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1400,
        1020
      ],
      "parameters": {
        "url": "https://sup-n8n.unipile.com/webhook/209dd6cb-76cf-4841-8c79-cea45a742b39",
        "method": "POST",
        "options": {},
        "sendBody": true,
        "authentication": "genericCredentialType",
        "bodyParameters": {
          "parameters": [
            {
              "name": "search_by",
              "value": "Available filters (name, tags, public_ip, zone) or null if you don't want to apply a filter"
            },
            {
              "name": "search",
              "value": "Your search keyword"
            }
          ]
        },
        "genericAuthType": "httpBasicAuth"
      },
      "credentials": {
        "httpBasicAuth": {
          "id": "YzpBkNOC0UnKboCn",
          "name": "Endpoint Get server scalway info"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "710b2503-ccb9-42d2-877a-034082a6fef8",
      "name": "Loop Over Items",
      "type": "n8n-nodes-base.splitInBatches",
      "position": [
        1600,
        1020
      ],
      "parameters": {
        "options": {}
      },
      "typeVersion": 3
    },
    {
      "id": "387d2a3d-8f2c-47be-a4c6-73ac110b03d0",
      "name": "Respond to Webhook4",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        2680,
        140
      ],
      "parameters": {
        "options": {},
        "respondWith": "allIncomingItems"
      },
      "typeVersion": 1.1
    },
    {
      "id": "09f05bba-5fe3-4e3f-b5e6-b6f75eb9400d",
      "name": "Get scw instance by zone",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1560,
        80
      ],
      "parameters": {
        "url": "=https://api.scaleway.com/instance/v1/zones/{{ $('Split Out ZONE_INSTANCE').item.json.ZONE_INSTANCE }}/servers",
        "options": {},
        "sendHeaders": true,
        "headerParameters": {
          "parameters": [
            {
              "name": "X-Auth-Token",
              "value": "={{ $('Edit Fields').item.json['Scalway-X-Auth-Token'] }}"
            },
            {
              "name": "Content-Type",
              "value": "application/json"
            }
          ]
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "541d8cd6-f7db-49a1-b527-235813b82737",
      "name": "Loop Over Zone Instance",
      "type": "n8n-nodes-base.splitInBatches",
      "position": [
        1360,
        0
      ],
      "parameters": {
        "options": {}
      },
      "typeVersion": 3
    },
    {
      "id": "be293c2d-bd39-46f5-8c09-766cc145f8b7",
      "name": "Get scw baremetal by zone",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        2000,
        80
      ],
      "parameters": {
        "url": "=https://api.scaleway.com/baremetal/v1/zones/{{ $('Split Out ZONE_INSTANCE').item.json.ZONE_INSTANCE }}/servers",
        "options": {},
        "sendHeaders": true,
        "headerParameters": {
          "parameters": [
            {
              "name": "X-Auth-Token",
              "value": "={{ $('Edit Fields').item.json['Scalway-X-Auth-Token'] }}"
            },
            {
              "name": "Content-Type",
              "value": "application/json"
            }
          ]
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "b12396b5-8fd6-4b06-8c41-0a14d2382937",
      "name": "Split Out ZONE_INSTANCE",
      "type": "n8n-nodes-base.splitOut",
      "position": [
        1100,
        0
      ],
      "parameters": {
        "options": {},
        "fieldToSplitOut": "ZONE_INSTANCE"
      },
      "typeVersion": 1
    },
    {
      "id": "b96d5ee0-db41-4ea8-a23f-2db3cea63a3c",
      "name": "If ZONE_BAREMETAL in ZONE_INSTANCE",
      "type": "n8n-nodes-base.if",
      "position": [
        1780,
        80
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
              "id": "874626f1-ecf5-42c4-86fe-01a9c68cbb1a",
              "operator": {
                "type": "array",
                "operation": "contains",
                "rightType": "any"
              },
              "leftValue": "={{ $('Edit Fields').item.json.ZONE_BAREMETAL }}",
              "rightValue": "={{ $('Loop Over Zone Instance').item.json.ZONE_INSTANCE }}"
            }
          ]
        },
        "looseTypeValidation": true
      },
      "typeVersion": 2.2
    },
    {
      "id": "30234c35-1788-4857-bc58-c1a581be318f",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -20,
        -140
      ],
      "parameters": {
        "color": 3,
        "width": 580,
        "height": 380,
        "content": "# Replace the Scaleway-X-Auth-Token Field\n\nTo ensure the workflow functions correctly, you must:\n\n1. Open the Edit Fields node in your workflow.\n2. Locate the Scaleway-X-Auth-Token field and enter your personal Scaleway token (replacing the default value).\n3. If you do not have a token yet:\n   - Log in to your Scaleway console.\n   - Create a new API Token by following the [Scaleway documentation](https://www.scaleway.com/en/developers/api/).\n   - Copy the generated token and paste it into the Scaleway-X-Auth-Token field."
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "b38207e8-da63-462c-ac51-925d029d5a1f",
  "connections": {
    "Code": {
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
    "Switch": {
      "main": [
        [
          {
            "node": "Code search Tags",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Code search Name",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Code search public_ip",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Code search zone",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Respond to Webhook4",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Respond Error",
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
            "node": "Edit Fields",
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
            "node": "Split Out ZONE_INSTANCE",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Code search Name": {
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
    "Code search Tags": {
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
    "Code search zone": {
      "main": [
        [
          {
            "node": "Respond to Webhook3",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Scalway Machines": {
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
    "Code search public_ip": {
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
    "Loop Over Zone Instance": {
      "main": [
        [
          {
            "node": "Code",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Get scw instance by zone",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Split Out ZONE_INSTANCE": {
      "main": [
        [
          {
            "node": "Loop Over Zone Instance",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get scw instance by zone": {
      "main": [
        [
          {
            "node": "If ZONE_BAREMETAL in ZONE_INSTANCE",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get scw baremetal by zone": {
      "main": [
        [
          {
            "node": "Loop Over Zone Instance",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "If ZONE_BAREMETAL in ZONE_INSTANCE": {
      "main": [
        [
          {
            "node": "Get scw baremetal by zone",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Loop Over Zone Instance",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
