# 🩺 Guia Saúde + 

Assistente digital inteligente, construído com IA generativa, processamento de linguagem natural e simulações em Phyton, voltado para o novo ecossistema integrado da Bradsaúde. 

Projeto desenvolvido como desafio final do Bootcamp **GenAI & Dados - Bradesco + DIO**.

## Objetivo

Melhorar significativamente a experiência do beneficiário, oferecendo informações claras, seguras, contextuais e integradas, alinhadas a nova estrutura, utilizando:

- compreensão de linguagem natural
- respostas contextualizadas
- simulações simples
- boas práticas de UX

O assistente ajuda usuários a entender melhor seu plano de saúde, respondendo dúvidas comuns sobre:

- cobertura
- reembolso
- carência
- rede credenciada
- funcionamento do plano

## Funcionalidades

### Chat inteligente
Usuário pode perguntar em linguagem natural:

Exemplos:

- "Meu plano cobre ressonância?"
- "Como funciona reembolso?"
- "Tenho direito a consulta com especialista?"

### Classificação de intenção

O sistema identifica automaticamente o tipo de pergunta:

- cobertura
- reembolso
- rede médica
- carência
- geral

### Simulação de reembolso

Usuário pode informar o valor de uma consulta e receber uma estimativa de reembolso.

Exemplo:

Consulta: R$500  
Plano: Premium

Resposta:

Estimativa de reembolso: R$350

### Memória de contexto

O sistema mantém informações durante a conversa:

- plano informado
- última pergunta
- histórico

### Acessibilidade

O sistema também inclui recursos para tornar a experiência mais inclusiva:

- modo de alto contraste
- opção de fonte ampliada
- leitura em voz da última resposta (TTS em PT-BR)
- botão para interromper a leitura em voz
- integração com VLibras para suporte em Libras

## Tecnologias utilizadas

- Python
- Streamlit
- Scikit-learn
- Pandas
- JSON

## Estrutura do projeto

```bash
healthguide-ai/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── data/
│   ├── faq_data.json
│   └── planos.json
├── models/
│   └── intent_classifier.py
├── services/
│   ├── chat_service.py
│   └── simulador_reembolso.py
└── utils/
    └── context_manager.py
```


## Como executar

### 1 Instalar dependências

pip install -r requirements.txt

### 2 Rodar o projeto

streamlit run app.py

### 3 Abrir no navegador

[https://guiasaudemais.streamlit.app/]

## Exemplos de perguntas

- "Meu plano cobre exame?"
- "Quanto recebo de reembolso numa consulta de 400?"
- "Tenho carência para exames?"
- "Como funciona autorização?"

## Melhorias futuras

- integração com modelos LLM open-source
- recomendação de rede credenciada
- análise de histórico de perguntas
- personalização por perfil do usuário

## 👩‍💻 Autora

Juliane Nascimento  
Estagiária na Bradesco Saúde
Bootcamp GenAI & Dados

"Projeto educacional desenvolvido no contexto do Bootcamp GenAI & Dados (DIO). Uso da marca Bradsaúde apenas como referência pública ao ecossistema anunciado pelo Grupo Bradesco."
