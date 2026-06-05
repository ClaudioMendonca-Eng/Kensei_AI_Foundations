# Projeto Final - Red Team vs Blue Team // Card Arena

Projeto final da Semana 8 em formato de card game educacional sobre estrategia cibernetica.

A proposta do app e ensinar conceitos de ataque e defesa (Red Team vs Blue Team) com uma experiencia visual estilo trading card game, usando IA para enriquecer explicacoes, contexto e interacao.

## Objetivo do projeto

- Transformar estudo de ciberseguranca em uma experiencia pratica e interativa
- Mostrar aplicacao real de IA em produto educacional
- Entregar um MVP funcional publicavel no GitHub

## Funcionalidades principais

- Interface em Streamlit com visual de card game
- Fluxo de aprendizado Red Team vs Blue Team
- Conteudo explicativo com suporte de IA
- Modo com provedores locais ou em nuvem
- Estrutura pronta para evolucao com novas cartas, modos e desafios

## Estrutura da pasta

- `RedTeam_BlueTeam_OSI_IA_card.py`: aplicacao principal
- `img/`: imagens e assets visuais do jogo
- `README.md`: documentacao do projeto final

## Requisitos

- Python 3.10+
- Streamlit instalado
- Dependencias do projeto instaladas via `requirements.txt`
- (Opcional) credenciais de API para provedores externos
- (Opcional) endpoint local compativel com OpenAI (Ollama, LM Studio, vLLM)

## Como executar

No terminal, dentro desta pasta:

```bash
pip install -r requirements.txt
```

Depois execute o app:

```bash
streamlit run RedTeam_BlueTeam_OSI_IA_card.py
```

Depois, abra a URL local exibida pelo Streamlit.

## Provedores de IA suportados

- Local Offline
- Ollama
- LM Studio
- vLLM
- OpenAI
- Gemini
- OpenAI Compatible

## Configuracao de IA (visao geral)

1. Escolha o provedor no app.
2. Se for provedor externo, informe chave de API e modelo.
3. Se for local, configure endpoint/base URL compativel com OpenAI.
4. Execute uma interacao de teste para validar resposta.

### Exemplo rapido de endpoint local (Ollama)

- Base URL: `http://localhost:11434/v1`
- Modelo (exemplo): `llama3.2:3b`

Observacao: em dev container, pode ser necessario usar `http://host.docker.internal:11434/v1`.

## Fluxo recomendado de uso

1. Iniciar o app no Streamlit.
2. Selecionar provedor e validar conexao.
3. Explorar os cards de ataque e defesa.
4. Usar a IA para apoiar explicacoes e comparacoes.
5. Registrar aprendizados para o relatorio final da Semana 8.

## Entrega esperada no GitHub

- Codigo funcional do app
- README com instrucoes claras (este arquivo)
- Arquivo de dependencias (`requirements.txt`)
- Assets visuais necessarios em `img/`
- Evidencias de funcionamento (prints ou GIFs)
- Relatorio final do curso (arquivo separado)

## Limites atuais do MVP

- Dependencia de configuracao manual de provedor/modelo
- Conteudo inicial de cartas pode ser expandido
- Falta de testes automatizados dedicados

## Roadmap sugerido

- Adicionar mais cartas e cenarios reais de SOC
- Criar modo quiz com pontuacao
- Salvar historico de partidas
- Exportar resumo da sessao em Markdown/PDF
- Publicar versao online para demonstracao

## Observacoes importantes

- O app foi desenhado para funcionar tanto com IA local quanto com APIs externas.
- Mantenha os arquivos de imagem dentro de `img/` para evitar quebra na interface.
- Para demonstração rapida, prefira comecar pelo modo local/offline.

## Pipeline de criacao de imagens

Para fechar o visual do Card Arena, as imagens do jogo foram criadas fora do app, usando o Nano Banana. A IA foi instruida com prompts especificos para manter consistencia visual no estilo trading card cyberpunk.

Tambem foram organizadas duas tabelas de prompts:

- Tabela 1: imagens das cartas do deck
- Tabela 2: imagens gerais do jogo e personagens

### Tabela 1 - TEAM e COMUM (cartas do deck)

| TEAM e COMUM | Carta | Tamanho | Prompt |
|---|---|---|---|
| RED TEAM | Script Kiddie | 768 x 312 | Jovem hacker impulsivo em sala escura neon, multiplas telas com exploit simples, energia caotica, faiscas vermelhas, postura agressiva, arte de criatura cyberpunk estilo trading card Magic, sem texto, sem logo, sem watermark |
| COMUM | Nodo Fisico | 768 x 312 | Nodo fisico cyberpunk em datacenter industrial, cabos de energia brilhando, conectores metalicos gigantes, neon branco-azulado, atmosfera tensa de batalha digital, arte detalhada de trading card fantasy sci-fi estilo Magic, iluminacao dramatica, sem texto, sem logo, sem watermark |
| COMUM | Hub de Enlace | 768 x 312 | Hub de enlace cyberpunk como nucleo de rede flutuante, pecas modulares e links luminosos conectando multiplos canais, tons azul eletrico, sensacao de controle tatico, arte detalhada de card game estilo Magic cyberpunk, sem texto, sem logo, sem watermark |
| COMUM | Gateway de Rede | 768 x 312 | Gateway de rede como portal hexagonal de dados, trafego digital em feixes vermelhos e ciano atravessando a estrutura, cidade noturna ao fundo, estilo card art Magic cyberpunk, alto contraste, sem texto, sem logo, sem watermark |
| COMUM | Servidor TCP | 768 x 312 | Servidor TCP monumental com racks futuristas e streams de pacotes como trilhas de luz verde, ambiente de guerra cibernetica, fumaca leve e brilhos neon, pintura digital epica estilo card game Magic, sem texto, sem logo, sem watermark |
| COMUM | Broker de Sessao | 768 x 312 | Broker de sessao representado por mascara digital e tokens de autenticacao orbitando em um salao escuro neon roxo e azul, clima furtivo e estrategico, arte cyberpunk estilo Magic card, sem texto, sem logo, sem watermark |
| COMUM | Modulo TLS | 768 x 312 | Modulo TLS como cofre criptografico translucido com cadeados holograficos, runas matematicas de criptografia brilhando, paleta azul gelo e branco, arte fantasy-tech estilo card Magic cyberpunk, sem texto, sem logo, sem watermark |
| COMUM | Endpoint App | 768 x 312 | Endpoint App como terminal avancado com interface neural, silhueta humana conectada a multiplas janelas holograficas, tons vermelho e magenta, atmosfera de risco humano, arte de carta estilo Magic cyberpunk, sem texto, sem logo, sem watermark |
| RED TEAM | Phishing Maestro | 768 x 312 | Golpista digital elegante controlando anzois de luz e e-mails holograficos, expressao manipuladora, tons violeta e ciano, cenario urbano noturno, arte de card estilo Magic cyberpunk, sem texto, sem logo, sem watermark |
| RED TEAM | Zero Day Hunter | 768 x 312 | Cacador de zero-day com visor tatico rastreando falhas em mural de codigo rachado, aura vermelha intensa, composicao dinamica de ataque, pintura digital detalhada estilo card game Magic cyberpunk, sem texto, sem logo, sem watermark |
| RED TEAM | APT Operative | 768 x 312 | Operativo APT furtivo com capa tatica e laminas de dados, infiltrando rede corporativa em silencio, paleta escura com brilho ambar e ciano, arte sofisticada de carta estilo Magic cyberpunk, sem texto, sem logo, sem watermark |
| RED TEAM | Botnet Commander | 768 x 312 | Comandante de botnet no topo de torre neon, enxame de drones/robos conectados por linhas de comando luminosas, sensacao de dominio massivo, arte epica estilo card Magic cyberpunk, sem texto, sem logo, sem watermark |
| RED TEAM | SQL Injection | 768 x 312 | Serpente de codigo injetando comando malicioso em banco de dados holografico, colunas SQL quebrando em fragmentos de luz, paleta vermelho e preto, arte de feitico cyberpunk estilo Magic, sem texto, sem logo, sem watermark |
| RED TEAM | CVE Critical | 768 x 312 | Vulnerabilidade critica explodindo como selo digital quebrado com alerta vermelho maximo, fragmentos de firmware voando, clima urgente de colapso de seguranca, arte impactante estilo Magic cyberpunk, sem texto, sem logo, sem watermark |
| RED TEAM | ARP Poison | 768 x 312 | Rede local distorcida com pacotes falsos envenenando rotas, nevoa toxica neon verde e amarelo, switches fantasmas e caminhos enganados, arte de magia tecnica estilo card Magic cyberpunk, sem texto, sem logo, sem watermark |
| RED TEAM | Rootkit | 768 x 312 | Entidade rootkit sombria escondida sob camadas de kernel holografico, olhos brilhantes no escuro, presenca silenciosa e ameacadora, tons preto, vinho e ciano, arte de malware estilo Magic cyberpunk, sem texto, sem logo, sem watermark |
| BLUE TEAM | SOC Analyst | 768 x 312 | Analista SOC em centro de operacoes futurista, multiplos paineis de alerta e telemetria, postura defensiva firme, paleta azul de monitoramento, arte de personagem estilo card Magic cyberpunk, sem texto, sem logo, sem watermark |
| BLUE TEAM | SIEM Monitor | 768 x 312 | Torre SIEM holografica agregando logs como constelacoes de dados, radar digital pulsando, tons azul e prata, sensacao de vigilancia total, arte de carta estilo Magic cyberpunk, sem texto, sem logo, sem watermark |
| BLUE TEAM | Threat Hunter | 768 x 312 | Cacador de ameacas com drone orbital e scanner avancado rastreando malware oculto, ambiente urbano chuvoso neon, clima tatico e preciso, arte heroica estilo card Magic cyberpunk, sem texto, sem logo, sem watermark |
| BLUE TEAM | WAF Guardian | 768 x 312 | Guardiao WAF como muralha energetica com escudo hexagonal bloqueando rajada de ataques web, luz branca e azul, presenca imponente, arte de defensor estilo card game Magic cyberpunk, sem texto, sem logo, sem watermark |
| BLUE TEAM | Incident Responder | 768 x 312 | Especialista de resposta a incidentes em acao, isolando sistemas com barreiras digitais e kits de recuperacao, atmosfera urgente porem controlada, tons azul e ambar, arte de carta estilo Magic cyberpunk, sem texto, sem logo, sem watermark |
| BLUE TEAM | Patch Deployed | 768 x 312 | Patch de seguranca sendo aplicado como selo luminoso cicatrizando rachaduras de codigo, brilho azul-esverdeado de estabilizacao, metafora visual de correcao rapida, arte de magia tecnica estilo Magic cyberpunk, sem texto, sem logo, sem watermark |
| BLUE TEAM | Firewall Rule | 768 x 312 | Parede de firewall com runas digitais barrando enxurrada de trafego hostil, chamas frias neon e grade de filtragem, composicao defensiva forte, arte de card spell estilo Magic cyberpunk, sem texto, sem logo, sem watermark |
| BLUE TEAM | Honeypot Network | 768 x 312 | Rede honeypot como colmeia tecnologica dourada atraindo ameacas para armadilha luminosa, fios e nos brilhando em azul, clima inteligente e estrategico, arte de card estilo Magic cyberpunk, sem texto, sem logo, sem watermark |
| BLUE TEAM | MFA Enforcement | 768 x 312 | Multiplos fatores de autenticacao representados por camadas de chaves biometricas e tokens holograficos, barreira de acesso elegante, paleta branco-azul com acentos dourados, arte de suporte estilo Magic cyberpunk, sem texto, sem logo, sem watermark |
| RED TEAM | Lateral Movement | 768 x 312 | Invasor se movendo lateralmente por segmentos de rede iluminados, trilhas de acesso em neon vermelho e laranja, sensacao de avanco tatico silencioso, arte cyberpunk estilo card game Magic, sem texto, sem logo, sem watermark |
| RED TEAM | Credential Dumper | 768 x 312 | Malware extraindo credenciais como chaves digitais arrancadas de cofres de memoria, ambiente escuro com brilho rubro e violeta, atmosfera de roubo furtivo, arte estilo Magic cyberpunk, sem texto, sem logo, sem watermark |
| RED TEAM | DNS Tunneler | 768 x 312 | Operador de exfiltracao ocultando dados em tuneis DNS holograficos, linhas de trafego azul e vermelho atravessando a cidade noturna, estetica tatica cyberpunk estilo card Magic, sem texto, sem logo, sem watermark |
| RED TEAM | C2 Beacon | 768 x 312 | Beacon de comando e controle pulsando no topo de antena futurista, ondas de sincronizacao coordenando agentes remotos, neon magenta e ciano, arte de ferramenta ofensiva estilo Magic cyberpunk, sem texto, sem logo, sem watermark |
| RED TEAM | Ransom Encryptor | 768 x 312 | Entidade de ransomware cifrando blocos de dados com correntes digitais e cadeados flamejantes, clima de pressao extrema, paleta vermelho escuro e preto, arte de malware estilo card Magic cyberpunk, sem texto, sem logo, sem watermark |
| RED TEAM | Privilege Escalation | 768 x 312 | Escalada de privilegios representada por avatar invadindo camadas de acesso em torre de seguranca quebrada, energia agressiva em vermelho neon, arte de feitico tatico estilo Magic cyberpunk, sem texto, sem logo, sem watermark |
| BLUE TEAM | EDR Sentinel | 768 x 312 | Sentinela EDR com visor analitico e drones de telemetria varrendo processos maliciosos, centro de defesa brilhando em azul e branco, arte heroica de card Magic cyberpunk, sem texto, sem logo, sem watermark |
| BLUE TEAM | SOAR Automation | 768 x 312 | Nucleo de automacao SOAR orquestrando playbooks como engrenagens holograficas, respostas automaticas em cadeia, tons ciano e azul eletrico, arte de ferramenta defensiva estilo Magic cyberpunk, sem texto, sem logo, sem watermark |
| BLUE TEAM | Threat Intel Feed | 768 x 312 | Fluxo de inteligencia de ameacas como paineis de noticias taticas e indicadores brilhantes conectados globalmente, atmosfera de vigilancia proativa, arte de magia utilitaria estilo Magic cyberpunk, sem texto, sem logo, sem watermark |
| BLUE TEAM | Quarantine VLAN | 768 x 312 | Segmento de quarentena isolando trafego hostil em bolha hexagonal luminosa, barreiras de rede azul-claro e branco, visual de contencao precisa, arte de spell estilo card Magic cyberpunk, sem texto, sem logo, sem watermark |
| BLUE TEAM | Forensic Specialist | 768 x 312 | Especialista forense analisando vestigios digitais com scanner molecular e trilhas de evidencia holograficas, clima investigativo noturno, arte de agente defensivo estilo Magic cyberpunk, sem texto, sem logo, sem watermark |
| BLUE TEAM | Backup Restore | 768 x 312 | Processo de restauracao de backup recriando servidores a partir de fragmentos de luz e dados resilientes, sensacao de recuperacao controlada, paleta azul e dourado suave, arte de suporte estilo Magic cyberpunk, sem texto, sem logo, sem watermark |
| COMUM | Edge Sensor Grid | 768 x 312 | Grade de sensores de borda distribuidos por infraestrutura urbana high-tech, pontos de deteccao acesos em ciano, visao de cobertura total de perimetro, arte de node estilo Magic cyberpunk, sem texto, sem logo, sem watermark |
| COMUM | Dark Fiber Link | 768 x 312 | Link de fibra escura subterraneo com feixes opacos transportando dados sigilosos, tuneis tecnologicos com brilho violeta e azul profundo, atmosfera clandestina, arte de node estilo Magic cyberpunk, sem texto, sem logo, sem watermark |
| COMUM | Zero Trust Segment | 768 x 312 | Segmentacao zero trust como muralhas logicas e portoes de autenticacao continua, arquitetura de seguranca em camadas neon azul e prata, arte de tool defensiva estilo Magic cyberpunk, sem texto, sem logo, sem watermark |
| COMUM | Vulnerability Scanner | 768 x 312 | Scanner de vulnerabilidades varrendo sistema em visao termica digital, pontos fracos destacados em vermelho sobre interface azul, clima tecnico de prevencao, arte de agente utilitario estilo Magic cyberpunk, sem texto, sem logo, sem watermark |
| COMUM | Incident Timeline | 768 x 312 | Linha do tempo de incidente com eventos ciberneticos encadeados em hologramas cronologicos, nos de ataque e resposta conectados por trilhas luminosas, arte de script analitico estilo Magic cyberpunk, sem texto, sem logo, sem watermark |
| COMUM | Secure Bastion | 768 x 312 | Bastiao seguro como fortaleza digital com escudos multicamada e torres de monitoramento neon, presenca solida e protetora, paleta azul-aco e branco, arte de defensor estilo card Magic cyberpunk, sem texto, sem logo, sem watermark |

### Tabela 2 - Imagens do jogo e personagens

| Tamanho da imagem | Nome da imagem | Prompt |
|---|---|---|
| 16:9 | capa_apresentacao_card_arena | Ilustracao epica de arena digital cyberpunk para card game tatico, cidade neon ao fundo, ceu noturno com hologramas abstratos, atmosfera de guerra cibernetica, cabos de fibra optica e circuitos luminosos no chao, composicao cinematografica wide, arte detalhada estilo TCG fantasy cyberpunk, luz volumetrica, contraste alto, cores azul eletrico e magenta, sem personagens com rostos em destaque, sem texto, sem logo, sem watermark |
| 3:2 | team_red_apresentacao | Operador ofensivo de ciberseguranca em armadura tatica futurista, ambiente de invasao digital com paineis vermelhos e laranja neon, drones e glitches ao fundo, postura agressiva e estrategica, estilo ilustracao de card game cyberpunk, pintura digital ultra detalhada, dramatic lighting, depth of field, sem texto, sem logo, sem watermark |
| 3:2 | team_blue_apresentacao | Analista defensivo de ciberseguranca em centro de comando futurista, tons azul e ciano, telas holograficas de monitoramento e escudos digitais, postura calma e protetora, estilo ilustracao de card game cyberpunk, pintura digital ultra detalhada, cinematic lighting, sem texto, sem logo, sem watermark |
| 2:3 | red_doctrine_apt | Especialista APT infiltrado em infraestrutura corporativa futurista, stealth, sombras, cabos e servidores neon, clima de persistencia silenciosa e precisao, estilo arte de carta TCG cyberpunk, composicao vertical, detalhes finos, sem texto, sem logo, sem watermark |
| 2:3 | red_doctrine_ransom | Entidade de ransomware personificada como guerreiro digital caotico, arquivos e blocos de dados criptografados brilhando ao redor, energia vermelha intensa, sensacao de urgencia e impacto, estilo arte de carta TCG cyberpunk, pintura digital detalhada, sem texto, sem logo, sem watermark |
| 2:3 | red_doctrine_mercenario | Hacker mercenario oportunista em beco neon futurista, visual pragmatico, gadgets modulares, clima de contrato rapido e alto risco, estilo arte de carta TCG cyberpunk, iluminacao dramatica, sem texto, sem logo, sem watermark |
| 2:3 | red_doctrine_hacktivista | Figura hacktivista mascarada projetando simbolos abstratos de protesto digital em mural holografico, estetica cyberpunk urbana, energia social e disruptiva, estilo arte de carta TCG cyberpunk, pintura detalhada, sem texto, sem logo, sem watermark |
| 2:3 | blue_doctrine_zero_trust | Guardiao digital de zero trust cercado por barreiras hexagonais e microsegmentacao holografica, arquitetura de seguranca em camadas, tom defensivo avancado, estilo arte de carta TCG cyberpunk, composicao vertical, sem texto, sem logo, sem watermark |
| 2:3 | blue_doctrine_soc_paranoico | Operador SOC ultra vigilante em sala escura com multiplos monitores de ameaca, alertas visuais abstratos, clima de deteccao antecipada e alta tensao, estilo arte de carta TCG cyberpunk, luz fria, sem texto, sem logo, sem watermark |
| 2:3 | blue_doctrine_compliance | Estrategista de compliance futurista organizando trilhas de auditoria holograficas, ambiente limpo, precisao e governanca digital, estilo arte de carta TCG cyberpunk, visual elegante, sem texto, sem logo, sem watermark |
| 2:3 | blue_doctrine_militar | Comandante defensivo cibernetico em bunker de resposta rapida, escudos energeticos e isolamento de rede em tempo real, postura firme e decisiva, estilo arte de carta TCG cyberpunk, dramatic rim light, sem texto, sem logo, sem watermark |
| 2:3 | ia_setup_background | Cenario de configuracao de IA adversaria, terminal futurista com interface abstrata e fluxos de dados, ambiente limpo e high-tech, tons azul/ciano com toques magenta, composicao horizontal para tela de configuracao, estilo cyberpunk TCG, sem texto, sem logo, sem watermark |
| 1920x1080 (16:9) | vitoria_red_team.png | Cena cinematográfica cyberpunk de vitória do Red Team em uma arena digital tática, operadores ofensivos em destaque, painéis OSI comprometidos em vermelho, partículas neon, fumaça digital, clima de domínio ofensivo, alto contraste, iluminação dramática, estilo concept art AAA, ultra detalhado, sem texto, sem logotipos, composição horizontal. |
| 1920x1080 (16:9) | vitoria_blue_team.png | Cena cinematográfica cyberpunk de vitória do Blue Team em uma central SOC futurista, analistas defensivos celebrando contenção total, painéis OSI restaurados em azul/ciano, hologramas de escudo e telemetria limpa, atmosfera de resiliência e controle, iluminação fria, estilo concept art AAA, ultra detalhado, sem texto, sem logotipos, composição horizontal. |
| 1920x1080 (16:9) | derrota_red_team.png | Cena cyberpunk cinematográfica mostrando derrota do Red Team em arena digital, operadores ofensivos recuando após falha tática, painéis OSI em alerta crítico, trilhas de ataque interrompidas, tons frios e vermelhos apagados, atmosfera de colapso operacional, iluminação dramática, partículas e glitches sutis, estilo concept art AAA, ultra detalhado, sem texto, sem logotipo, composição horizontal. |
| 1920x1080 (16:9) | derrota_blue_team.png | Cena cyberpunk cinematográfica mostrando derrota do Blue Team em centro SOC futurista comprometido, monitores com múltiplos incidentes e contenção falha, escudos digitais quebrados, analistas sob pressão, tons azul/ciano desaturados com vermelho de alerta, clima de ruptura defensiva, iluminação dramática, estilo concept art AAA, ultra detalhado, sem texto, sem logotipo, composição horizontal. |


### Sugestao rapida de proporcao

1. Capa e IA setup: 16:9
2. Time Red e Time Blue: 3:2
3. Doutrinas: 2:3 (vertical de carta)

### Resultados obtidos

- Todas as imagens foram criadas com sucesso usando o Nano Banana e os prompts especificados.
- As imagens seguem um estilo visual consistente de card game cyberpunk, com alta qualidade e detalhes.
- As imagens foram salvas na pasta `img/` com os nomes correspondentes para uso no app.
- O processo de criacao de imagens foi eficiente, permitindo gerar um grande numero de assets visuais em pouco tempo.
- As imagens criadas enriqueceram significativamente a experiencia visual do Card Arena, contribuindo para a imersao e atratividade do jogo.

