# Exercicio IA Gratuita - Ollama Local + Streamlit

Este exercicio implementa uma validacao real de IA gratuita com Ollama local e Streamlit para executar testes em Python.

Observacao importante: se voce estiver em dev container, normalmente nao existe Docker dentro do Docker. Nesse caso, rode o Ollama no host e acesse pela URL `http://host.docker.internal:11434`.

## O que voce vai validar

- Conexao com Ollama local
- Geracao de resposta por prompt livre
- Bateria de 3 testes padrao com latencia e status

## Estrutura

- `docker-compose.yml`: opcional, para subir Ollama no host via Docker
- `requirements.txt`: dependencias Python
- `app_streamlit_ollama.py`: app Streamlit para executar os testes

## Passo a passo

1. Inicie o Ollama no host (fora do dev container):

Opcao A - Docker no host:

```bash
docker compose up -d
```

Opcao B - Ollama instalado no host:

```bash
ollama serve
```

2. Baixe um modelo:

```bash
ollama pull llama3.2:3b
```

3. Instale as dependencias Python:

```bash
pip install -r requirements.txt
```

4. Rode o app Streamlit:

```bash
streamlit run app_streamlit_ollama.py
```

5. No app:
- Clique em **Checar Ollama**
- Se necessario, ajuste o campo **Ollama host** para `http://host.docker.internal:11434`
- Teste um prompt livre
- Clique em **Rodar bateria** para os 3 testes padrao

## Troubleshooting rapido

Se aparecer timeout em host.docker.internal:

1. Confirme no host se o Ollama esta ativo:

```bash
ollama list
```

2. No app, use o botao **Auto detectar host** na barra lateral.

3. Se ainda falhar, teste manualmente no campo Ollama host, nesta ordem:

- http://host.docker.internal:11434
- http://172.17.0.1:11434
- http://172.18.0.1:11434

4. Se nenhum host responder, o Ollama nao esta exposto para o container. Nesse caso, reinicie o Ollama no host e rode o app novamente.

## Entrega sugerida

- Print da tela com status do ollama conectado

<p align="center">
    <img src="./img/01-teste_conexao.png" alt="Semana 8 - IA Gratuita e Projeto Final" width="1100">
</p>


- Prompt livre e resposta gerada

<p align="center">
    <img src="./img/02-teste_prompt_livre.png" alt="Semana 8 - IA Gratuita e Projeto Final" width="1100">
</p>

- Latencia  e status da bateria de testes

<p align="center">
    <img src="./img/03-bateria_testes_exercicio.png" alt="Semana 8 - IA Gratuita e Projeto Final" width="1100" >
</p>


## Resultados obtidos

Os testes foram executados com sucesso usando o modelo `llama3.2:3b` no Ollama local.

Resumo da bateria:

| Teste | Status | Latencia (s) |
| --- | --- | ---: |
| T1 | ok | 12.99 |
| T2 | ok | 14.84 |
| T3 | ok | 18.60 |

Latencia media: 15.48 s

### Observacoes

- O endpoint local respondeu corretamente aos 3 testes.
- As respostas foram coerentes e adequadas para um MVP educacional.
- A latencia ficou aceitavel para uso local, mas ainda pode melhorar com modelo menor ou hardware mais forte.

### Evidencias

- O arquivo CSV com os resultados foi salvo em [doc/resultado_2026-06-01T22-28_export.csv](doc/resultado_2026-06-01T22-28_export.csv).
- Os prints da execucao foram gerados durante a validacao visual do app.

### Resumo final: o exercicio de IA gratuita com Ollama local foi validado com sucesso, demonstrando a viabilidade de usar IA local gratuita para casos de uso simples, com latencia aceitavel e respostas coerentes.
