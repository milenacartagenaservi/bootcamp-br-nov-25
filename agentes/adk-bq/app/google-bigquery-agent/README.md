# 📊 BigQuery Agent (Google ADK)

Este guia demonstra como integrar a ferramenta **BigQuery** ao seu agente. Isso permite que o modelo Gemini execute consultas SQL, analise metadados e faça previsões diretamente em seus datasets do Google Cloud.

## 🛠️ Capacidades da Ferramenta

A integração com o BigQuery fornece um conjunto de funções prontas para que o agente interaja com seus dados:

* **`list_dataset_ids`**: Busca os IDs dos datasets presentes no projeto GCP.
* **`get_dataset_info`**: Busca metadados sobre um dataset específico do BigQuery.
* **`list_table_ids`**: Busca os IDs das tabelas presentes em um dataset.
* **`get_table_info`**: Busca metadados (schema e detalhes) de uma tabela específica.
* **`execute_sql`**: Executa uma consulta SQL no BigQuery e retorna o resultado.
* **`forecast`**: Executa uma previsão de série temporal (time series forecast) usando a função `AI.FORECAST` do BigQuery.
* **`ask_data_insights`**: Responde perguntas sobre os dados nas tabelas usando linguagem natural (Data Insights).

---

## 📋 Pré-requisitos do Google Cloud

Diferente dos agentes simples, o BigQuery exige um projeto no Google Cloud (GCP) ativo:

1.  **Projeto GCP:** Tenha um ID de projeto (ex: `meu-projeto-dados`).
2.  **API Habilitada:** Ative a BigQuery API no console do Google Cloud.
3.  **Dataset:** Tenha um dataset e tabelas criadas no BigQuery para consultar.

## 🚀 1. Instalação com Dependências Extras


**macOS / Linux:**
```bash
python -m venv .venv
source .venv/bin/activate
pip install google-adk
````

-----

## 🔐 2. Autenticação (Application Default Credentials)

Para que o agente acesse o BigQuery, ele precisa das credenciais do seu usuário ou de uma Service Account (apenas a API Key do Gemini não é suficiente para ler o banco de dados).

Precisamos criar uma credencial em APIs e servicos no Google Cloud, e fazemos clic em Credeciais.
<img width="658" height="256" alt="image" src="https://github.com/user-attachments/assets/6a53c027-7e01-4083-9766-10d71352a989" />

Depois, clicamos em Criar credenciais em ID de cliente de OAuth
<img width="677" height="430" alt="image" src="https://github.com/user-attachments/assets/73d05676-8a78-411f-9506-60d08a7a8f0a" />

e escolhemos aplicacao web e damos um nome
<img width="657" height="208" alt="image" src="https://github.com/user-attachments/assets/2cec8d7d-96fd-4012-8968-3d420198f819" />

e criamos. É importante salvar ou baixar o json do ID do cliente e o Secret do cliente.

-----

## 📂 3. Estrutura e Código

Crie a estrutura de pastas para o agente de dados.

1.  Crie uma pasta do projeto com  a hierarquia que se amostra a continuacao.
2.  Crie o arquivo `__init__.py`.
3.  Crie o arquivo `agent.py`.

**Estrutura:**

```text
adk-bq/  # Project folder
└── app/ # the web app folder
    ├── .env # Gemini API key + ClientID + Secret 
    └── google_bigquery_agent/ # Agent folder
        ├── __init__.py # Python package
        └── agent.py # Agent definition
```

### O Código

**Arquivo `bigquery_agent/__init__.py`**
Crie este arquivo com o seguinte conteúdo:

```python
from . import agent
```

**Arquivo `bigquery_agent/agent.py`**
Aqui configuramos a ferramenta `BigQuery` apontando para o seu projeto e dataset específicos.

```python

import asyncio
import os
from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools.bigquery import BigQueryCredentialsConfig
from google.adk.tools.bigquery import BigQueryToolset
from google.adk.tools.bigquery.config import BigQueryToolConfig
from google.adk.tools.bigquery.config import WriteMode
from google.genai import types
import google.auth

# Define constants for this example agent
AGENT_NAME = "bigquery_agent"
APP_NAME = "bigquery_app"
USER_ID = "user1234"
SESSION_ID = "1234"
GEMINI_MODEL = "gemini-2.0-flash"

from google.adk.agents import Agent
from google.adk.tools import google_search  # Import the tool

# Define a tool configuration to block any write operations
tool_config = BigQueryToolConfig(write_mode=WriteMode.BLOCKED)

# Uses externally-managed Application Default Credentials (ADC) by default.
# This decouples authentication from the agent / tool lifecycle.
# https://cloud.google.com/docs/authentication/provide-credentials-adc
#credentials_config = BigQueryCredentialsConfig()
credentials_config = BigQueryCredentialsConfig(client_id=os.environ.get("GOOGLE_CLIENT_ID"), client_secret=os.environ.get("GOOGLE_CLIENT_SECRET"))

bigquery_toolset = BigQueryToolset(
    credentials_config=credentials_config, bigquery_tool_config=tool_config
)


root_agent = Agent(
   # A unique name for the agent.
   name="basic_search_bq_agent",
   model="gemini-2.0-flash",  # escolha seu modelo
   # A short description of the agent's purpose.
   description="Agent to use bigquery to look at the data.",
   # Instructions to set the agent's behavior.
   instruction="You are an expert researcher and an agent to answer questions about BigQuery data and models and execute, SQL queries. You always stick to the data information. You are a data science agent with access to several BigQuery tools. Make use of those tools to answer the user's questions",
   # Add bigquery tool
   tools=[bigquery_toolset]
)

```

-----

## 🔑 4. Configuração do Modelo (.env)

Ainda precisamos do arquivo `.env` para autenticar o modelo LLM (Gemini). Crie o arquivo `.env` na raiz do projeto.

**Arquivo `.env`:**

```env
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT="YOUR_PROJECT_ID"
GOOGLE_CLOUD_LOCATION="us-central1" # e.g., southamerica-east1
# Inside your .env file
GOOGLE_CLIENT_ID="YOUR_CLIENT_ID"
GOOGLE_CLIENT_SECRET="YOUR_CLIENT_SECRET"
```

-----

## ▶️ 5. Como Executar

Para interagir com o agente e visualizar os dados, use a Dev UI ou o Terminal.

```bash
cd app
```

**Opção Recomendada (Dev UI):**

```bash
adk web
```

1.  Acesse `http://localhost:8000`.
2.  Faça uma pergunta: *"Quantas vendas tivemos no ultimo mês?"* ou *"Faça uma previsão de vendas para a próxima semana"*.

É possivel que voce receba o seguinte erro: <img width="598" height="648" alt="image" src="https://github.com/user-attachments/assets/8d900fa3-eee0-4c2b-a80f-2feb00e9fa51" />


Se clicar em detalhes do erro, voce pode copiar a URL que recebeu:
<img width="731" height="682" alt="image" src="https://github.com/user-attachments/assets/2727437a-edfb-4281-8971-60f3247f10df" />

e, voltamos para as credeciais que criamos anteriormente, escolha a credencial, adicione a URL e salve:

<img width="672" height="390" alt="image" src="https://github.com/user-attachments/assets/e7003412-1186-4b3d-a161-2396ce7b084a" />


-----

<!-- end list -->

