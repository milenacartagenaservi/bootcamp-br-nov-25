# 🤖 BootCamp Nov 2025: Google ADK - Exemplos de Agentes

Este repositório contém exemplos práticos de implementação de agentes de IA utilizando o **Google Agent Development Kit (ADK)**. Aqui você encontrará códigos para diferentes casos de uso, desde ferramentas simples até análise de dados e streaming de voz.

## 📂 Conteúdo do Repositório

O projeto está dividido em três agentes principais:

| Pasta | Descrição | Principais Recursos |
| :--- | :--- | :--- |
| **`multi_tool_agent/`** | **Agente de Clima e Tempo** | Exemplo básico de *Function Calling* com ferramentas personalizadas (`get_weather`, `get_current_time`). |
| **`Google Search_agent/`** | **Agente de Streaming (Live)** | Focado em interação de voz em tempo real usando o modelo **Gemini 2.0 Live** e Google Search. |
| **`bigquery_agent/`** | **Agente de Dados (BigQuery)** | Integração avançada para consultar datasets, listar tabelas e gerar insights via SQL e linguagem natural. |

---

## 🛠️ Instalação Geral

Para rodar qualquer um dos exemplos, você precisará do **Python 3.10+**.

1.  **Prepare o ambiente virtual:**
    ```bash
    # Linux/macOS
    python -m venv .venv
    source .venv/bin/activate

    # Windows
    .venv\Scripts\activate.bat
    ```

2.  **Instale as dependências:**
    Para garantir que todos os exemplos funcionem (incluindo o de dados), instale o pacote completo:
    ```bash
    pip install "google-adk[bigquery]"
    ```

---

## 🔑 Configuração (Antes de Rodar)

Todos os agentes precisam de uma API Key. Crie um arquivo `.env` na raiz do projeto (ou dentro da pasta do agente específico) com suas credenciais:

```env
# Exemplo para Google AI Studio
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=sua_chave_aqui
````

> **Nota para BigQuery:** Se for rodar o `bigquery_agent`, lembre-se de autenticar também no Google Cloud via terminal:
> `gcloud auth application-default login`

-----

## ▶️ Como Executar os Exemplos

Você pode rodar os agentes via terminal ou interface web (`Dev UI`). Certifique-se de estar na raiz deste repositório.

### 1\. Agente de Clima (Básico)

```bash
adk web
# Na interface, selecione: "weather_time_agent"
```

*Ou via terminal:* `adk run multi_tool_agent`

### 2\. Agente de Streaming (Voz/Live)

Requer a interface web para funcionar o áudio bidirecional.

```bash
adk web
# Na interface, selecione: "basic_search_agent"
```

### 3\. Agente BigQuery (Dados)

```bash
adk web
# Na interface, selecione: "data_analyst_agent"
```

*Ou via terminal:* `adk run bigquery_agent`

-----

## 📚 Documentação Oficial

Para mais detalhes sobre o kit de desenvolvimento, visite a documentação oficial do [Google ADK](https://google.github.io/adk-docs/).

```
```
