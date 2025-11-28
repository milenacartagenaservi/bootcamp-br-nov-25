# 🎙️ Streaming Agent (Google ADK)

Este guia demonstra como configurar um agente com suporte a **Streaming Bidirecional** (interação em tempo real com áudio) usando o Google ADK. Este agente utiliza a ferramenta de busca do Google e o modelo Gemini 2.0 Live.

## 📋 Pré-requisitos

* **Python 3.10** ou superior.

## 🚀 1. Instalação do Ambiente

Crie e ative um ambiente virtual para isolar as dependências:

**macOS / Linux:**
```bash
python -m venv .venv
source .venv/bin/activate
````

**Windows (CMD):**

```cmd
.venv\Scripts\activate.bat
```

**Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

Instale a biblioteca do ADK:

```bash
pip install google-adk
```

-----

## 📂 2. Estrutura e Código

Para o agente de streaming, precisamos de uma estrutura específica e do modelo correto (`gemini-live-2.5-flash-preview-native-audio-09-2025` ou superior).

1.  Crie uma pasta principal para o projeto chamada `adk-streaming`.
2.  Dentro dela, crie uma subpasta chamada `Google Search_agent`.
3.  Crie os arquivos necessários seguindo a estrutura abaixo:

<!-- end list -->

```text
adk-streaming/  # Project folder
└── app/ # the web app folder
    ├── .env # Gemini API key
    └── google_search_agent/ # Agent folder
        ├── __init__.py # Python package
        └── agent.py # Agent definition
```

### Criando os arquivos

**Arquivo `google_search_agent/__init__.py`**
Crie este arquivo com o seguinte conteúdo:

```python
from . import agent
```

**Arquivo `google_search_agent/agent.py`**
Crie este arquivo com o código abaixo. Note o uso do modelo `gemini-live-2.5-flash-preview-native-audio-09-20251` e da ferramenta `Google Search`:

```python
from google.adk.agents import Agent
from google.adk.tools import google_search  # Import the tool

root_agent = Agent(
   # A unique name for the agent.
   name="basic_search_agent",
   # The Large Language Model (LLM) that agent will use.
   # Please fill in the latest model id that supports live from
   # https://google.github.io/adk-docs/get-started/streaming/quickstart-streaming/#supported-models
   model="gemini-2.0-flash",  # for example: model="gemini-2.0-flash-live-001" or model="gemini-2.0-flash-live-preview-04-09"
   # A short description of the agent's purpose.
   description="Agent to answer questions using Google Search.",
   # Instructions to set the agent's behavior.
   instruction="You are an expert researcher. You always stick to the facts.",
   # Add google_search tool to perform grounding with Google search.
   tools=[google_search]
)
```

-----

## 🔑 3. Configuração de Autenticação

Configure suas credenciais no arquivo `.env` na raiz do projeto (`app/.env`).

**Vertex AI**

```env
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT=Seu_ID_Do_Projeto
GOOGLE_CLOUD_LOCATION=us-central1
```

-----

## ▶️ 4. Como Executar (Streaming)

Para testar as capacidades de voz e streaming, é necessário utilizar a interface web (`Dev UI`), pois o terminal não suporta a entrada/saída de áudio nativa do navegador.

1.  Navegue até a pasta raiz `app`:

    ```bash
    cd app
    ```

2.  Inicie a interface de desenvolvimento:

    ```bash
    adk web
    ```

    *(Nota para usuários Windows: Se encontrar erros de recarregamento, use `adk web --no-reload`)*

3.  Abra o navegador em: **http://localhost:8000**
4.  Testa o agente!
<!-- end list -->
