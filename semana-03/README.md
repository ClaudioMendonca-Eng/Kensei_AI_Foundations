# SEMANA 3

# DADOS COM PANDAS

Analisando o mundo real com Python.

Datasets reais + Pandas + Matplotlib + Ecossistema - tudo via Vibe Coding.

Kensei AI Foundations | Quartas as 19h | Mao na Massa!

Kensei CyberSec Lab | AI Foundations 2026 | Semana 3 Vibe Coding.

---

## O Que Sao Dados? (E Por Que Importam)

Tudo e dado. Planilhas de vendas, logs de servidor, posts de rede social, sensores IoT, registros de ataques ciberneticos.

Quem sabe ler e transformar dados em informacao util tem superpoder no mercado.

### Tipos de dados

### Estruturados

Tabelas, planilhas, CSV, bancos de dados.

Linhas e colunas organizadas.

Exemplos: planilha de clientes, logs de firewall.

### Semi-estruturados

JSON, XML, APIs. Alguma estrutura mais flexivel.

Exemplos: respostas de API, dados de IoT.

### Nao-estruturados

Texto livre, imagens, audio, video. Sem formato fixo.

Exemplos: emails, PDFs, capturas de tela.

---

## Datasets: De Onde Vem os Dados?

Dataset = conjunto de dados organizado, pronto pra analise.

### Kaggle

`kaggle.com/datasets`

A maior plataforma de datasets do mundo. Milhares gratuitos.

Exemplos: logs de ataques, dados COVID, precos de casas.

### dados.gov.br

`dados.gov.br`

Portal de dados abertos do governo brasileiro. Dados oficiais.

Exemplos: criminalidade, educacao, saude publica.

### GitHub Awesome Data

`github.com/awesomedata`

Colecao curada de datasets organizados por tema.

Exemplos: redes sociais, clima, seguranca.

### APIs publicas (VirusTotal, Shodan...)

Servicos que oferecem dados via API em tempo real.

Exemplos: threat intel, clima, cambio.

---

## Pandas: Sua Ferramenta de Dados

Pandas e uma biblioteca Python para trabalhar com dados em formato de tabela.

Pense nele como um Excel superpotente dentro do Python.

Voce carrega um arquivo, filtra, agrupa, calcula, tudo com poucas linhas (que a IA pode escrever com voce).

### Conceitos-chave

- DataFrame: a tabela (linhas = registros, colunas = informacoes)
- Series: uma unica coluna
- CSV: arquivo texto com dados separados por virgula
- Index: numero da linha (comeca em 0)

---

## Matplotlib: Transformando Dados em Graficos

Matplotlib e a biblioteca padrao do Python para criar graficos e visualizacoes.

Se Pandas e o Excel dos dados, Matplotlib e o PowerPoint dos graficos.

### O que da pra fazer

- Barras (`kind="bar"`): comparar valores entre categorias
- Linhas (`kind="line"`): mostrar tendencias ao longo do tempo
- Pizza (`kind="pie"`): mostrar proporcoes
- Histograma (`kind="hist"`): distribuicao de valores

---

## O Ecossistema de Dados em Python

Pandas e Matplotlib sao a base, mas existe um universo de bibliotecas que complementam:

- NumPy (CALCULO): operacoes com arrays e base matematica do Pandas
- Seaborn (VISUAL): graficos estatisticos bonitos com poucas linhas
- Plotly (INTERATIVO): graficos interativos com zoom, hover e filtros
- Streamlit (APPS): transforma scripts em apps web em minutos
- Scikit-learn (ML): machine learning para classificacao, regressao e clustering
- Jupyter Notebook: ambiente interativo para codigo, resultados e graficos

---

## Projeto 1: Carregando e Explorando Dados

Voce pede:

"Instala pandas e matplotlib. Carrega CSV de ataques ciberneticos, mostra primeiras linhas, info e estatisticas."

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cybersecurity_attacks.csv")
print(df.head())
print(df.shape)
print(df.info())
print(df.describe())
print(df.columns)
print(df.isnull().sum())
```

### O que voce aprende

- `import pandas as pd`
- `import matplotlib`
- `pd.read_csv()`
- `df.head()`
- `df.shape`
- `df.info()`
- `df.describe()`
- `df.isnull().sum()`

---

## Projeto 2: Limpando Dados Sujos

Dados reais sempre vem sujos. Limpar e grande parte do trabalho.

Voce pede:

"Limpa o dataset: remove duplicados, preenche nulos, converte datas, remove dados invalidos."

```python
print(df.isnull().sum())
print(df.duplicated().sum())

df = df.drop_duplicates()
df["tipo"].fillna("desconhecido", inplace=True)
df["data"] = pd.to_datetime(df["data"])
df = df.dropna(subset=["ip_origem"])
```

### Conceitos

- `.isnull().sum()`
- `.duplicated()`
- `.drop_duplicates()`
- `.fillna()`
- `pd.to_datetime()`
- `.dropna()`

---

## Projeto 3: Filtrando e Agrupando

Voce pede:

"Filtra ataques DDoS do ultimo mes, agrupa por pais e mostra top 10 com mais ataques."

```python
ddos = df[df["tipo"] == "DDoS"]
recentes = ddos[ddos["data"] > "2024-01-01"]
por_pais = recentes.groupby("pais_origem")
contagem = por_pais.size()
top10 = contagem.sort_values(ascending=False).head(10)
print(top10)
```

### Conceitos

- `df[condicao]`
- `.groupby()`
- `.size()`
- `.sort_values()`
- `.head(10)`

Iteracao sugerida:

"Agora mostra media de duracao dos ataques por pais"

---

## Projeto 4: Graficos com Matplotlib

Agora transformamos dados em visualizacoes.

Voce pede:

"Cria 3 graficos: barras top 10 paises, linha ataques por mes, pizza tipos de ataque. Salva PNG."

```python
import matplotlib.pyplot as plt

top10.plot(kind="bar", color="#16C79A")
plt.title("Top 10 Paises - DDoS")
plt.xlabel("Pais")
plt.ylabel("Ataques")
plt.tight_layout()
plt.savefig("top10_ddos.png")
plt.show()
```

Dica pro:

- Quer graficos mais bonitos? Peca Seaborn.
- Quer graficos interativos? Peca Plotly.

---

## Projeto 5: Analise Completa

Pipeline completo (com IA):

1. Escolher dataset (Kaggle, dados.gov.br ou outra fonte)
2. Carregar e explorar (`read_csv`, `head`, `shape`, `info`, `describe`)
3. Limpar (nulos, duplicados, formatos)
4. Analisar (filtros, grupos, contagens, medias)
5. Visualizar (3+ graficos salvos em PNG)
6. Documentar (README com conclusoes e aprendizados)

Datasets sugeridos:

- Cyber Attack (Kaggle, ~50K)
- Data Breaches (Kaggle, ~500)
- Seguranca BR (dados.gov.br)
- COVID-19 Brasil (github/wcota, ~5M)
- World Happiness (Kaggle, ~150 paises)

---

## Análise de Cibersegurança (Pasta cyber/)

Além dos 5 scripts base com dados de vendas, criamos uma análise completa do dataset **cybersecurity_attacks.csv** em subpasta dedicada.

### Scripts da Pasta cyber/

| Script | Descrição |
|---|---|
| `01_explorar_ataques.py` | Carrega CSV, mostra `head()`, `shape`, `info()`, `describe()`, tipos de ataque, severidade |
| `02_limpeza_ataques.py` | Remove duplicados, converte Timestamp, preenche nulos (IoC, Proxy, Alerts), normaliza Severity |
| `03_filtros_ataques.py` | Filtra alta severidade, DDoS bloqueados, eventos com IoC; agrupa por tipo, ação, protocolo |
| `04_kpis_ataques.py` | 9 KPIs: taxa bloqueio (33.8%), IoC (50%), eventos por ano, protocolo mais atacado |
| `05_visualizacao_ataques.py` | 4 PNGs: barras tipo ataque, barras ação×severidade, pizza tráfego, dashboard consolidado |

### Executar no Docker

```bash
# Explorar dataset
docker run --rm kensei-semana03 python cyber/01_explorar_ataques.py

# Limpeza
docker run --rm kensei-semana03 python cyber/02_limpeza_ataques.py

# Filtros e grupos
docker run --rm kensei-semana03 python cyber/03_filtros_ataques.py

# KPIs de segurança
docker run --rm kensei-semana03 python cyber/04_kpis_ataques.py

# Gerar gráficos PNG
docker run --rm -v "%cd%\semana-03\graficos:/app/semana-03/graficos" kensei-semana03 python cyber/05_visualizacao_ataques.py
```

### Gráficos Gerados

Salvos em `semana-03/graficos/`:
- `cyber_ataques_por_tipo.png` — Barras: DDoS, Malware, Intrusion
- `cyber_acoes_por_severidade.png` — Agrupado: ações tomadas × severidade
- `cyber_trafego_pizza.png` — Pizza: HTTP, DNS, FTP
- `cyber_dashboard.png` — Dashboard com 3 gráficos consolidados

---

## Dashboard Interativo

Arquivo: `semana-03/dashboard.html`

**Abra direto no navegador** — não precisa de servidor.

### Funcionalidades

- **Toggle Cibersegurança ↔ Vendas**: alterna datasets no header
- **Tema dinâmico**: cores mudam (verde-teal para cyber, laranja-vermelho para vendas)
- **5 Painéis de KPIs** por dataset
- **Gráficos interativos** com Chart.js:

**Cibersegurança (5 gráficos):**
- Barras: Ataques por tipo (DDoS, Malware, Intrusion)
- Rosca: Distribuição por severidade (High, Medium, Low)
- Barras: Ações tomadas (Blocked, Logged, Ignored)
- Pizza: Tipo de tráfego (HTTP, DNS, FTP)
- Linha: Eventos por ano (2020–2023)

**Vendas (4 gráficos):**
- Barras: Faturamento por categoria (Hardware, Periférico, Software, Móveis)
- Barras: Pedidos por cidade (São Paulo, Rio, Curitiba, etc.)
- Rosca: Status dos pedidos (Concluída, Pendente, Cancelada)
- Barras horizontais: Top 5 produtos por faturamento

---

## Rodando com Docker

Arquivos adicionados para container:

- `semana-03/Dockerfile`
- `semana-03/requirements.txt`
- `semana-03/.dockerignore`

### 1. Build da imagem

Rode na raiz do repositorio:

```bash
docker build -f semana-03/Dockerfile -t kensei-semana03 .
```

### 2. Executar scripts no container

Script padrao (exploracao inicial):

```bash
docker run --rm kensei-semana03
```

Executar scripts especificos:

```bash
docker run --rm kensei-semana03 python 02_limpeza_dados.py
docker run --rm kensei-semana03 python 03_filtros_consultas.py
docker run --rm kensei-semana03 python 04_analise_kpis.py
docker run --rm kensei-semana03 python 05_visualizacao.py
```

### 3. Gerar graficos PNG no host

Para salvar os PNGs em `semana-03/graficos` no seu computador:

```bash
docker run --rm -v ${PWD}/semana-03/graficos:/app/semana-03/graficos kensei-semana03 python 05_visualizacao.py
```

No Windows cmd, use:

```bat
docker run --rm -v "%cd%\semana-03\graficos:/app/semana-03/graficos" kensei-semana03 python 05_visualizacao.py
```

---

## Salvando no GitHub

Estrutura atual:

```text
kensei-ai-foundations/
  semana-01/ ...
  semana-02/ ...
  semana-03/
    ├── 01_pandas_primeiros_passos.py      # Vendas: carrega e explora
    ├── 02_limpeza_dados.py                # Vendas: limpa nulos, converte datas
    ├── 03_filtros_consultas.py            # Vendas: filtra e agrupa
    ├── 04_analise_kpis.py                 # Vendas: calcula KPIs
    ├── 05_visualizacao.py                 # Vendas: gera 3 PNGs
    ├── cyber/
    │   ├── 01_explorar_ataques.py         # Cyber: explora cybersecurity_attacks.csv
    │   ├── 02_limpeza_ataques.py          # Cyber: limpa dataset
    │   ├── 03_filtros_ataques.py          # Cyber: filtros e agrupamentos
    │   ├── 04_kpis_ataques.py             # Cyber: 9 KPIs de segurança
    │   └── 05_visualizacao_ataques.py     # Cyber: 4 gráficos PNG
    ├── data/
    │   ├── vendas.csv                     # 12 pedidos — Março 2026
    │   └── cybersecurity_attacks.csv      # 40 000 eventos — 2020–2023
    ├── graficos/                          # PNGs dos gráficos
    │   ├── dashboard_semana03.png         # Vendas
    │   ├── faturamento_por_categoria.png  # Vendas
    │   ├── pedidos_por_cidade.png         # Vendas
    │   ├── cyber_ataques_por_tipo.png     # Cyber
    │   ├── cyber_acoes_por_severidade.png # Cyber
    │   ├── cyber_trafego_pizza.png        # Cyber
    │   └── cyber_dashboard.png            # Cyber
    ├── dashboard.html                     # Dashboard interativo (abrir no navegador)
    ├── Dockerfile                         # Container com pandas + matplotlib
    ├── requirements.txt                   # pandas==2.2.2, matplotlib==3.9.0
    ├── .dockerignore
    └── README.md                          # Este arquivo
```

### Fluxo de Trabalho

1. Salve tudo (Ctrl+S)
2. Stage All > Commit
3. "semana 03 - dados pandas + cyber + dashboard"
4. Sync Changes (push)
5. Inclua os PNGs dos gráficos

---

## Salvando no GitHub

Estrutura sugerida:

```text
kensei-ai-foundations/
  semana-01/ ...
  semana-02/ ...
  semana-03/
    01_explorar_dados.py
    02_limpar_dados.py
    03_filtrar_agrupar.py
    04_graficos.py
    05_analise_completa.py
    graficos/ (PNGs)
    README.md
```

Fluxo:

1. Salve tudo (Ctrl+S)
2. Stage All > Commit
3. "semana 03 - dados pandas"
4. Sync Changes (push)
5. Inclua os PNGs dos graficos

---

## Recap + Para Casa

### O que fizemos

- Entendemos dados e datasets
- Conhecemos Pandas e Matplotlib
- Vimos o ecossistema (Seaborn, Plotly...)
- Carregamos, limpamos e filtramos dados
- Criamos graficos profissionais
- Estruturamos uma analise completa

### Para casa

- Completar analise de um dataset
- Gerar 3+ graficos salvos como PNG
- Escrever README com conclusoes
- Fazer push de tudo no GitHub
- Experimentar Seaborn ou Plotly
