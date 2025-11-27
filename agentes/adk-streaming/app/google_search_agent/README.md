# 🎙️ Streaming Agent (Google ADK)

Este guia demonstra como configurar um agente com suporte a **Streaming Bidirecional** (interação em tempo real com áudio) usando o Google ADK. Este agente utiliza a ferramenta de busca do Google e o modelo Gemini 2.0 Live.

## 📋 Pré-requisitos

* **Python 3.10** ou superior.
* Uma **chave de API do Google** (necessário suporte ao Gemini 2.0 Flash Live).

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

Para o agente de streaming, precisamos de uma estrutura específica e do modelo correto (`gemini-2.0-flash-live-001` ou superior).

1.  Crie uma pasta principal para o projeto chamada `adk-streaming`.
2.  Dentro dela, crie uma subpasta chamada `Google Search_agent`.
3.  Crie os arquivos necessários seguindo a estrutura abaixo:

<!-- end list -->

```text
adk-streaming/
├── .env                  <-- Arquivo de credenciais (na raiz do projeto)
└── google_search_agent/
    ├── __init__.py       <-- Arquivo de inicialização do pacote
    └── agent.py          <-- Código do agente
```

### Criando os arquivos

**Arquivo `Google Search_agent/__init__.py`**
Crie este arquivo com o seguinte conteúdo:

```python
from . import agent
```

**Arquivo `Google Search_agent/agent.py`**
Crie este arquivo com o código abaixo. Note o uso do modelo `gemini-2.0-flash-live-001` e da ferramenta `Google Search`:

```python
from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    # Um nome único para o agente
    name="basic_search_agent",
    
    # O modelo LLM que o agente usará.
    # IMPORTANTE: Deve ser um modelo que suporta 'Live' (streaming bidirecional).
    model="gemini-2.0-flash-live-001",
    
    # Descrição do propósito do agente
    description="Agent to answer questions using Google Search.",
    
    # Instruções de comportamento
    instruction="You are an expert researcher. You always stick to the facts.",
    
    # Adiciona a ferramenta de busca do Google para 'grounding'
    tools=[google_search]
)
```

-----

## 🔑 3. Configuração de Autenticação

Configure suas credenciais no arquivo `.env` na raiz do projeto (`adk-streaming/.env`).

**Opção A: Google AI Studio (Recomendado)**

```env
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=Cole_Sua_Chave_API_Aqui
```

**Opção B: Vertex AI**

```env
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT=Seu_ID_Do_Projeto
GOOGLE_CLOUD_LOCATION=us-central1
```

-----

## ▶️ 4. Como Executar (Streaming)

Para testar as capacidades de voz e streaming, é necessário utilizar a interface web (`Dev UI`), pois o terminal não suporta a entrada/saída de áudio nativa do navegador.

1.  Navegue até a pasta raiz `adk-streaming`:

    ```bash
    cd adk-streaming
    ```

2.  Inicie a interface de desenvolvimento:

    ```bash
    adk web
    ```

    *(Nota para usuários Windows: Se encontrar erros de recarregamento, use `adk web --no-reload`)*

3.  Abra o navegador em: **http://localhost:8000**

4.  **Habilitando Áudio/Vídeo:**

      * No menu superior esquerdo, selecione **"basic\_search\_agent"**.
      * Clique no ícone de **Microfone** ou **Câmera** na interface para iniciar a sessão de streaming bidirecional.
      * Fale com o agente (ex: "Pesquise sobre as últimas notícias de tecnologia"). O agente responderá com voz em tempo real.

-----

## 🛠️ Solução de Problemas

  * **Modelo não suportado:** Se receber erro de modelo, verifique no `agent.py` se o `model` está definido como `gemini-2.0-flash-live-001` ou uma versão mais recente disponível no Google AI Studio.
  * **SSL/Certificados:** Em alguns ambientes corporativos ou Windows, se houver erros de conexão SSL, pode ser necessário configurar os certificados Python (`pip install certifi`).

<!-- end list -->
