| O **Kensei AI Foundations** e uma jornada pratica para quem quer entrar no universo de **IA, dados, programacao e automacao**, mesmo comecando do zero. Aqui, o foco nao e so teoria: voce aprende construindo projetos reais, usando IA como copiloto e desenvolvendo as competencias que o mercado ja exige. Ao longo de 8 semanas, voce evolui com desafios mao na massa, apoio da comunidade e um portfolio que prova sua capacidade de resolver problemas reais. Se o objetivo e construir uma carreira **AI-first** com base solida e visao aplicada para tecnologia e cybersecurity, este curso e o ponto de partida. |
|:---:|
| |
|  <a href="https://kensei.seg.br/lab" target="_blank"><img style="margin: 10px" height="100" width="300" src="../../img/logo_kensei.png" alt="Logos Kensei"/></a> |

---

<p align="center">
    <img src="../../img/02-Kensei_AI_Foundations_S02_Vibe_Coding.png" alt="Semana 2 - Vibe Coding" width="1100">
</p>

---

# Semana 2 - Vibe Coding

Python com IA escrevendo pra voce.

Voce dirige, a IA executa. Voce entende, a IA acelera.

Kensei AI Foundations | Quartas as 19h | Mao na Massa!

Kensei CyberSec Lab | AI Foundations 2026 | Semana 2 | Vibe Coding.

## O que e Vibe Coding?

Vibe Coding e o fluxo em que voce descreve o que quer e a IA gera o codigo inicial.

Seu trabalho nao e decorar toda a sintaxe. Seu trabalho e:

1. Saber pedir com clareza
2. Saber ler o codigo gerado
3. Saber iterar e refinar

Em outras palavras: pedir, entender, testar, ajustar e repetir.

## O fluxo da aula

1. Pedir
2. Ler
3. Rodar
4. Iterar

Exemplo simples:

```python
nome = input("Qual seu nome? ")
nome_maiusculo = nome.upper()
print(f"Ola, {nome_maiusculo}!")
```

O que isso ensina:

- input() para ler do usuario
- .upper() para transformar texto em maiusculo
- f-string para formatar saidas

## Projetos desta pasta

```text
vibe_coding/
├── README.md
├── 01_conversor.py
├── 02_lista_compras.py
├── 03_quiz_cyber.py
├── 04_gerador_senhas.py
└── 05_organizador.py
```

## Projeto 1 - Conversor de temperatura

Arquivo: 01_conversor.py

Converte:

- Celsius para Fahrenheit
- Fahrenheit para Celsius

Conceitos:

- input()
- float()
- operacoes matematicas
- if/elif/else
- f-string

Melhoria implementada: o slide mostrava apenas a conversao de Celsius para Fahrenheit. O script foi iterado para ter um menu que permite escolher as duas direcoes antes de digitar a temperatura.

## Projeto 2 - Lista de compras

Arquivo: 02_lista_compras.py

Funcionalidades:

- adicionar item
- ver lista
- remover item
- sair
- salvar em arquivo .txt ao encerrar

Conceitos:

- lista vazia
- while True
- append()
- pop()
- break

Melhoria implementada: o slide pedia como proxima iteracao salvar a lista em .txt ao sair. Isso foi incluido junto com remocao por numero de posicao e validacao de item vazio antes de adicionar.

## Projeto 3 - Quiz de cybersecurity

Arquivo: 03_quiz_cyber.py

Funcionalidades:

- 5 perguntas sobre cyber
- 3 opcoes por pergunta
- pontuacao final
- informa se passou com 3 ou mais acertos
- timer de 10 segundos por pergunta

Conceitos:

- lista de dicionarios
- for
- contador
- funcao
- validacao de resposta

Melhoria implementada: o slide pedia como proxima iteracao adicionar um timer de 10 segundos por pergunta. Foi implementado com threading e queue: uma thread captura a resposta do usuario enquanto o contador corre em paralelo. Se o tempo esgotar, a resposta e considerada errada automaticamente.

## Projeto 4 - Gerador de senhas

Arquivo: 04_gerador_senhas.py

Funcionalidades:

- escolher tamanho
- escolher maiusculas
- escolher numeros
- escolher simbolos
- gerar 5 senhas de uma vez
- salvar em senhas.txt com data e hora

Conceitos:

- import
- funcoes
- random
- string
- booleanos

Melhoria implementada: o slide pedia como proxima iteracao gerar 5 senhas de uma vez e salvar em senhas.txt com data. O script gera as 5 senhas em loop, exibe cada uma numerada e grava tudo em senhas.txt no modo append, com timestamp no formato YYYY-MM-DD HH:MM:SS antes de cada lote.

## Projeto 5 - Organizador de arquivos

Arquivo: 05_organizador.py

Funcionalidades:

- organiza arquivos por extensao
- cria subpastas automaticamente
- move arquivos
- mostra log por categoria

Conceitos:

- os
- shutil
- dicionario
- laco for
- automacao util no dia a dia

Melhoria implementada: o slide pedia como proxima iteracao adicionar um log mostrando quantos arquivos foram movidos por categoria. O script exibe esse resumo ao final, inclui a categoria "outros" para extensoes nao mapeadas e trata colisao de nomes: se ja existir um arquivo com o mesmo nome no destino, renomeia automaticamente com sufixo numerico.

## Quando der erro

Erros fazem parte do processo.

Fluxo recomendado:

1. Leia a ultima linha do erro
2. Cole o erro na IA
3. Peca: corrige e me explica
4. Rode de novo

## Como executar

No terminal, a partir da raiz do repositorio:

```bash
python semana-02/vibe_coding/01_conversor.py
python semana-02/vibe_coding/02_lista_compras.py
python semana-02/vibe_coding/03_quiz_cyber.py
python semana-02/vibe_coding/04_gerador_senhas.py
python semana-02/vibe_coding/05_organizador.py
```

## GitHub

Fluxo sugerido:

1. Salvar tudo
2. Stage All
3. Commit com a mensagem: semana 02 vibe coding
4. Sync Changes

Dica: um commit por projeto e melhor do que deixar tudo para o final.

## Para casa

- Terminar e revisar os 5 projetos
- Fazer push no GitHub
- Adicionar pelo menos 1 melhoria em cada projeto
- Criar um sexto projeto inventado por voce
- Pedir para a IA explicar trechos do codigo
- Pesquisar o que e Pandas

## Proxima aula

Semana 3 - Dados com Pandas.

Dados reais, limpeza, analise e graficos via vibe coding.

```python
voce = "vibe coder"
print(f"{voce} em construcao")
```
