# SEMANA 4

# APIs DE IA

Conectando Python com Inteligência Artificial

Seus scripts ganham cérebro — tudo via Vibe Coding

Kensei AI Foundations | Quartas as 19h | Mão na Massa!

---

## O Que É uma API? (Simples!)

**API = um garçom entre você e a cozinha.**

Seu script faz um pedido → A API leva para o servidor da IA → O servidor processa → A API traz a resposta

**Você não precisa saber cozinhar. Só precisa saber pedir.**

Na prática: até agora você usava IA pelo site. Agora seu **CÓDIGO conversa com a IA**. Automação, apps, bots, ferramentas personalizadas!

```
Seu Script (Python) → API (Garçom) → Servidor IA (Cozinha)
```

---

## API Key: Sua Chave de Acesso

Para usar a API você precisa de uma chave (**API Key**). É como uma senha.

### Provedores de IA

| Provedor | Link | Crédito |
|---|---|---|
| **OpenAI (ChatGPT)** | [platform.openai.com/api-keys](https://platform.openai.com/api-keys) | US$5 grátis |
| **Anthropic (Claude)** | [console.anthropic.com](https://console.anthropic.com) | US$5 grátis |
| **Google (Gemini)** | [aistudio.google.com/apikey](https://aistudio.google.com/apikey) | Grátis com limites |

### ⚠️ REGRA DE OURO: Nunca coloque API Key no código!

Use `.env` + `python-dotenv`. Se subir a key pro GitHub **qualquer pessoa gasta sua conta!**

---

## Configurando o Projeto

### 1. Instalar dependências

```bash
pip install -r requirements.txt
```

### 2. Criar `.env` (PRIVADO)

Copie [.env.example](.env.example) e renomeie para `.env`:

```env
OPENAI_API_KEY=sk-sua-chave-aqui
ANTHROPIC_API_KEY=sk-ant-sua-chave-aqui
GOOGLE_API_KEY=sua-chave-aqui
```

### 3. `.gitignore` protege sua chave

```
.env
__pycache__/
*.pyc
.DS_Store
```

Já configurado! ✅

---

## Projeto 1: Primeira Conversa com a API

Arquivo: [01_hello_api.py](01_hello_api.py)

Versão multi-provider: [01_hello_api_multi.py](01_hello_api_multi.py)

**O que faz:**
- Carrega API key de `.env`
- Cria cliente OpenAI
- Envia pergunta para a IA
- Imprime resposta
- Permite entrada do usuário

**Conceitos:**
- `load_dotenv()` — carrega `.env`
- `OpenAI()` — cliente da API
- `.chat.completions.create()` — endpoint de chat
- `model=` — qual modelo usar
- `messages=[]` — conversa
- `.choices[0].message.content` — pega resposta

**Rodar:**
```bash
python 01_hello_api.py
python 01_hello_api_multi.py
```

---

## Projeto 2: Assistente de Terminal

Arquivo: [02_assistente.py](02_assistente.py)

**O que faz:**
- Loop infinito: usuário digita, IA responde
- **Mantém histórico** da conversa (memória)
- System prompt personaliza a IA (cybersecurity)
- Mostra tokens gastos

**Conceitos:**
- `role: system` — personalidade da IA
- `role: user` — sua mensagem
- `role: assistant` — resposta da IA
- `historico` — lista que cresce (memória)
- `.append()` — adiciona mensagem

**Variações sugeridas:**
- Adicionar cores: IA em verde, usuário em branco
- Salvar histórico em arquivo
- Contar tokens totais da sessão

**Rodar:**
```bash
python 02_assistente.py
```

---

## Projeto 3: Analisador de Texto

Arquivo: [03_analisador.py](03_analisador.py)

**O que faz:**
- Recebe texto
- Pede pra IA: resumo (3 frases), sentimento, 5 palavras-chave
- Retorna JSON estruturado
- Salva em arquivo `analise.json`

**Conceitos:**
- Prompt estruturado (engineering)
- Parsing JSON da resposta
- Processamento automatizado

**O prompt está no código!**

Você programa a IA. Não é mais manual.

1000 textos? Roda 1000 vezes → **Isso é automação de verdade.**

**Variações:**
- Processar pasta inteira de `.txt`
- Criar dashboard com resultados
- Integrar com banco de dados

**Rodar:**
```bash
python 03_analisador.py
```

---

## Projeto 4: Tradutor Inteligente

Arquivo: [04_tradutor.py](04_tradutor.py)

**O que faz:**
- Detecta idioma original
- Traduz para português (ou outro idioma)
- **Glossário de termos técnicos** que NÃO devem ser traduzidos (phishing, malware, etc.)
- Processa arquivo `.txt` e salva com sufixo `_pt`

**Por que melhor que Google Translate?**
- LLM entende contexto, gírias, termos técnicos
- Você controla tudo: tom, formato, glossário
- **Ferramenta real pro dia a dia!**

**Variações:**
- Processar pasta inteira de `.txt`
- Adicionar glossário customizável
- Detecção automática de idioma

**Rodar:**
```bash
python 04_tradutor.py
```

---

## Projeto 5: Relatório com Dados + IA

Arquivo: [05_gerador_relatorios.py](05_gerador_relatorios.py)

**O que faz:**
- Carrega CSV com **Pandas**
- Calcula estatísticas
- Envia resumo para a API
- **IA gera relatório executivo em Markdown**
- Salva em `relatorio_gerado.md`

**Aqui combina TUDO:**
- S2: Python
- S3: Pandas + dados
- S4: API de IA

**Dados + análise + relatório = ferramenta profissional.**

Empresas pagam consultores pra isso! 💰

**Variações:**
- Adicionar gráficos Matplotlib
- Gerar relatório automaticamente diariamente
- Enviar por email

**Rodar:**
```bash
# Primeiro copie um CSV para a pasta (ex: vendas.csv)
python 05_gerador_relatorios.py
```

---

## ⚠️ Cuidados com APIs

### NUNCA suba API Key pro GitHub
Use `.env` + `.gitignore`. Se vazar, **revogue imediatamente!**

### Monitore custos
APIs cobram por tokens.
- Use `gpt-4o-mini` (barato)
- Veja painel de uso na console

### Não envie dados sensíveis
CPF, senhas, dados de clientes — **nunca mande pra API**.

### Rate limits
APIs têm limites por minuto.
- Erro 429 = espere e tente de novo
- Implemente retry logic

---

## Estrutura do Projeto

```text
semana-04/
  ├── .env                      # Suas chaves (PRIVADO — não sobe)
  ├── .env.example              # Template (sube no repo)
  ├── .dockerignore             # Protege arquivos no build Docker
  ├── .gitignore                # Protege .env
  ├── Dockerfile                # Ambiente Docker da semana 4
  ├── requirements.txt          # Dependências Python
  ├── api_provider.py           # Camada única para OpenAI/Google/Anthropic
  ├── 00_demo.py                # Teste Docker sem API key
  ├── 00_test_google.py         # Teste Google Gemini
  ├── 01_hello_api.py           # Primeira chamada à API
  ├── 01_hello_api_multi.py     # OpenAI/Anthropic/Google (auto-detect)
  ├── 01_hello_api_v2.py        # Versão melhorada do projeto 1
  ├── 02_assistente.py          # Chatbot com memória
  ├── 02_assistente_v2.py       # Assistente com comandos (/stats, /salvar)
  ├── 03_analisador.py          # Análise de texto → JSON
  ├── 03_analisador_v2.py       # Parser JSON robusto + fallback
  ├── 04_tradutor.py            # Detecta idioma + traduz
  ├── 04_tradutor_v2.py         # Tradução com glossário e arquivo .txt
  ├── 05_gerador_relatorios.py  # Versão base do relatório
  ├── 05_relatorio_automatico_v2.py  # CSV + API = relatório automático
  ├── 06_ferramenta_soc_api_v2.py    # Ferramenta própria: triagem SOC
  ├── historico/                # Cópia dos projetos antigos (preservados)
  ├── analise.json              # Saída do analisador
  ├── relatorio_gerado.md       # Saída do gerador
  └── README.md                 # Este arquivo
```

---

## Rodando com Docker

Arquivos adicionados:
- `semana-04/Dockerfile`
- `semana-04/.dockerignore`

### 1. Build da imagem

Na raiz do repositório:

```bash
docker build -f semana-04/Dockerfile -t kensei-semana04 .
```

### 2. Demo (teste sem API key)

```bash
docker run --rm kensei-semana04 python 00_demo.py
```

Mostra que tudo foi instalado corretamente! ✅

### 3. Testar Google Gemini

Se você já cadastrou a chave do Google:

```bash
docker run --rm \
  -e GOOGLE_API_KEY=AIza... \
  kensei-semana04 python 00_test_google.py
```

### 3.1 Testar OpenAI

Se você já cadastrou a OPENAI_API_KEY:

```bash
docker run --rm \
  -v $(pwd)/semana-04/.env:/app/semana-04/.env \
  kensei-semana04 python -c "import os;from dotenv import load_dotenv;load_dotenv();from openai import OpenAI;client=OpenAI(api_key=os.getenv('OPENAI_API_KEY'));r=client.chat.completions.create(model='gpt-4o-mini',messages=[{'role':'user','content':'Responda apenas: OK'}],max_tokens=5);print(r.choices[0].message.content.strip())"
```

Windows CMD (uma linha):

```bat
docker run --rm -v "%cd%\semana-04\.env:/app/semana-04/.env" kensei-semana04 python -c "import os;from dotenv import load_dotenv;load_dotenv();from openai import OpenAI;client=OpenAI(api_key=os.getenv('OPENAI_API_KEY'));r=client.chat.completions.create(model='gpt-4o-mini',messages=[{'role':'user','content':'Responda apenas: OK'}],max_tokens=5);print(r.choices[0].message.content.strip())"
```

### 4. Executar scripts no container

Opção A (recomendada): variável de ambiente

```bash
# OpenAI (script original)
docker run --rm \
  -e OPENAI_API_KEY=sk-sua-chave \
  kensei-semana04 python 01_hello_api.py

# Google Gemini (script de teste)
docker run --rm \
  -e GOOGLE_API_KEY=AIza... \
  kensei-semana04 python 00_test_google.py

# Script multi-provider (auto-detecta OpenAI / Google / Anthropic)
docker run --rm \
  -e GOOGLE_API_KEY=AIza... \
  kensei-semana04 python 01_hello_api_multi.py
```

Exemplo em uma linha para Windows CMD:

```bat
docker run --rm -e OPENAI_API_KEY=sk-sua-chave kensei-semana04 python 01_hello_api.py
```

### 5. Rodar usando arquivo `.env`

Windows CMD:

```bat
docker run --rm ^
  -v "%cd%\semana-04\.env:/app/semana-04/.env" ^
  kensei-semana04 python 01_hello_api_multi.py
```

Linux/Mac:

```bash
docker run --rm \
  -v $(pwd)/semana-04/.env:/app/semana-04/.env \
  kensei-semana04 python 01_hello_api_multi.py
```

### 6. Scripts disponíveis no container

```bash
docker run --rm -e OPENAI_API_KEY=sk-xxx kensei-semana04 python 01_hello_api.py
docker run --rm -e OPENAI_API_KEY=sk-xxx kensei-semana04 python 02_assistente.py
docker run --rm -e OPENAI_API_KEY=sk-xxx kensei-semana04 python 03_analisador.py
docker run --rm -e OPENAI_API_KEY=sk-xxx kensei-semana04 python 04_tradutor.py
docker run --rm -e OPENAI_API_KEY=sk-xxx kensei-semana04 python 05_gerador_relatorios.py
docker run --rm -e GOOGLE_API_KEY=AIza... kensei-semana04 python 00_test_google.py
docker run --rm -e GOOGLE_API_KEY=AIza... kensei-semana04 python 01_hello_api_multi.py
```

### 7. Salvar outputs (JSON, MD)

Para salvar arquivos gerados no host:

```bat
mkdir semana-04\outputs
docker run --rm -e OPENAI_API_KEY=sk-xxx -v "%cd%\semana-04\outputs:/app/semana-04/outputs" kensei-semana04 python 05_gerador_relatorios.py
```

---

## Fluxo de Trabalho

### 1. Configuração (uma vez)

```bash
pip install -r requirements.txt
# Copie .env.example para .env e preencha as chaves
```

### 2. Rodar scripts locais

```bash
python 00_demo.py
python 00_test_google.py
python 01_hello_api.py
python 01_hello_api_multi.py
python 01_hello_api_v2.py
python 02_assistente.py
python 02_assistente_v2.py
python 03_analisador.py
python 03_analisador_v2.py
python 04_tradutor.py
python 04_tradutor_v2.py
python 05_gerador_relatorios.py
python 05_relatorio_automatico_v2.py
python 06_ferramenta_soc_api_v2.py
```

---

## Exercícios Concluídos

### 1) Criar ferramenta própria com API

Implementado em `06_ferramenta_soc_api_v2.py`.

O script:
- carrega alertas de cibersegurança (`cybersecurity_attacks.csv`)
- prioriza eventos por `Anomaly Scores`
- pede para a IA gerar plano SOC acionável
- salva saída em `outputs/plano_triagem_soc_v2.md`

Rodar:

```bash
docker run --rm -e GOOGLE_API_KEY=AIza... kensei-semana04 python 06_ferramenta_soc_api_v2.py
```

### 2) Dados CSV + API = relatório automático

Implementado em `05_relatorio_automatico_v2.py`.

O script:
- varre todos os `.csv` da pasta atual
- gera análise automática com IA
- cria arquivos versionados por timestamp em `outputs/`

Rodar:

```bash
docker run --rm -e OPENAI_API_KEY=sk-xxx kensei-semana04 python 05_relatorio_automatico_v2.py
```

### 3) Melhorar cada projeto e manter antigos como histórico

Feito com versões `v2` e cópia de segurança dos antigos.

- Projetos antigos preservados em `historico/`
- Melhorias entregues: `01_hello_api_v2.py` até `06_ferramenta_soc_api_v2.py`
- Camada reutilizável adicionada: `api_provider.py`

---

## Observação de Validação (Docker)

Validação executada em container da semana 4:

- Build da imagem: OK
- Compilação dos scripts com `py_compile` no container: OK
- Chave OpenAI carregada no container: OK
- Chamada real para OpenAI: retornou `429 insufficient_quota`

Isso indica que a integração está funcional, mas a conta/projeto está sem cota disponível no momento.

### Troubleshooting de quota 429

OpenAI:
- Verifique billing e uso em: https://platform.openai.com/usage
- Verifique limites em: https://platform.openai.com/settings/organization/limits

Google Gemini:
- Verifique limites em: https://ai.google.dev/gemini-api/docs/rate-limits

Quando a cota for liberada, rode novamente os comandos de teste acima.

### 3. Customizar

Cada script é um template. Customize conforme sua necessidade!

### 4. Salvando no GitHub

```bash
# Stage & Commit (sem .env!)
git add .
git commit -m "semana 04 - apis de ia"

# Confira que .env NÃO está na lista de staged files
git status

# Push
git push
```

---

## Recap + Para Casa

### ✅ O Que Fizemos

- Entendemos APIs (garçom!)
- Configuramos API key segura com `.env`
- Primeira chamada a IA via código
- Assistente de terminal com memória
- Analisador + Tradutor automático
- Relatório: dados + IA combinados

### 💼 Para Casa

- Completar 5 projetos e fazer push
- Criar ferramenta própria com API
- Testar API do Claude também
- Dados CSV + API = relatório automático
- Pedir IA melhorar cada projeto

