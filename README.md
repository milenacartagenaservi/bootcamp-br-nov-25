# BootCamp Nov 2025

# 🤖 Multi-Tool Agent (Google ADK)

Este repositório contém uma implementação de um agente utilizando o **Agent Development Kit (ADK)** do Google. O agente é capaz de responder perguntas sobre clima e fuso horário utilizando ferramentas específicas.

Abaixo está o guia passo a passo completo para configurar e rodar este projeto localmente.

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter instalado:
* **Python 3.10** ou superior.

## 🚀 Instalação Passo a Passo

### 1. Configurar o Ambiente Virtual
É altamente recomendável usar um ambiente virtual para isolar as dependências do projeto.

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

### 2\. Instalar o ADK

Com o ambiente virtual ativado, instale o kit de desenvolvimento do agente:

```bash
pip install google-adk
```

-----
## 📂 1. Criação do Código do Agente

1. Vamos criar no respositorio a pasta onde vamos contruir o nosso agente:

```bash
mkdir multi_tool_agent/
```
2. Nessa pasta vamos criar o arquivo `__init__.py` só com a linha `from . import agent`

```bash
echo "from . import agent" > multi_tool_agent/__init__.py
```
3.  Ainda na mesma pasta, crie o arquivo **`agent.py`** e cole o código abaixo:

**`multi_tool_agent/agent.py`**

```python
import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent

def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified city.

    Args:
        city (str): The name of the city for which to retrieve the weather report.

    Returns:
        dict: status and result or error msg.
    """
    if city.lower() == "new york":
        return {
            "status": "success",
            "report": (
                "The weather in New York is sunny with a temperature of 25 degrees"
                " Celsius (77 degrees Fahrenheit)."
            ),
        }
    else:
        return {
            "status": "error",
            "error_message": f"Weather information for '{city}' is not available.",
        }


def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city.

    Args:
        city (str): The name of the city for which to retrieve the current time.

    Returns:
        dict: status and result or error msg.
    """

    if city.lower() == "new york":
        tz_identifier = "America/New_York"
    else:
        return {
            "status": "error",
            "error_message": (
                f"Sorry, I don't have timezone information for {city}."
            ),
        }

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    report = (
        f'The current time in {city} is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
    )
    return {"status": "success", "report": report}


root_agent = Agent(
    name="weather_time_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions about the time and weather in a city."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about the time and weather in a city."
    ),
    tools=[get_weather, get_current_time],
)
```

-----

## 2. 🔑 Configuração de Autenticação (Crucial)
O agente precisa de credenciais para acessar o modelo Gemini. Como boas práticas de segurança, **não incluímos as chaves no código**. Você deve criar um arquivo local.

### 1\. Criar o arquivo `.env`

Navegue até a pasta do agente (`multi_tool_agent`) e crie um arquivo chamado `.env`.

**Estrutura de pastas esperada:**

```text
seu-repositorio/
├── multi_tool_agent/
│   ├── __init__.py
│   ├── agent.py
│   └── .env  <-- CRIE ESTE ARQUIVO AQUI
```

### 2\. Adicionar as Chaves

Abra o arquivo `.env` que você acabou de criar e cole a configuração abaixo, dependendo de qual serviço você está usando:

**Autenticação** rodar `gcloud auth application-default login` no terminal antes de prosseguir

**Usando Google Cloud Vertex AI**
Requer projeto no GCP e autenticação via `gcloud CLI`.

```env
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT=ID_DO_SEU_PROJETO
GOOGLE_CLOUD_LOCATION=us-central1
```


-----

## ▶️ Como Executar o Agente

Existem três formas de interagir com o agente. Certifique-se de estar na **raiz do projeto** (fora da pasta `multi_tool_agent`) para executar os comandos.

```text
seu-repositorio/     <-- se ubica na pasta
├── multi_tool_agent/
│   ├── __init__.py
│   ├── agent.py
│   └── .env  
```

### Opção 1: Interface Visual (Dev UI) - Recomendado

Esta opção abre uma interface no navegador onde você pode conversar, ver o histórico e inspecionar os "traces" (rastreamento) das ferramentas.

1.  Execute o comando:

    ```bash
    adk web
    ```

    *(Nota para Windows: Se houver erro de reload, use `adk web --no-reload`)*

2.  Abra seu navegador em a URL dada, usualmente é: `http://localhost:8000` ou http://127.0.0.1:8000

3.  No menu superior esquerdo, selecione **"multi\_tool\_agent"**.

4.  Comece a conversar (ex: "Qual o clima em Nova York?").

-----

## 🛠️ Solução de Problemas Comuns

  * **Erro "Module not found"**: Certifique-se de que ativou o ambiente virtual (`source .venv/bin/activate`) antes de rodar os comandos.
  * **Agente não aparece na lista da UI**: Verifique se você rodou o comando `adk web` a partir da pasta raiz do projeto, e não de dentro da pasta `multi_tool_agent`.
  * **Erro de Autenticação (403/401)**: Verifique se sua `GOOGLE_API_KEY` está correta no arquivo `.env` e se o arquivo está na pasta correta.

<!-- end list -->
Com certeza. Agora vou integrar o código que você forneceu na etapa correta de criação dos arquivos.

Para que o guia fique completo e funcione "de primeira", adicionei a etapa de criação da estrutura de pastas e do arquivo `__init__.py` (necessário para o Python reconhecer o pacote), seguido pelo código do `agent.py` que você enviou.

Aqui está o `README.md` completo e atualizado em português:

````markdown
# 🤖 Multi-Tool Agent (Google ADK)

Este repositório contém uma implementação de um agente utilizando o **Agent Development Kit (ADK)** do Google. O agente utiliza o modelo `gemini-2.0-flash` e ferramentas personalizadas para responder perguntas sobre clima e fuso horário.

Abaixo está o guia passo a passo completo para configurar e rodar este projeto.

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter instalado:
* **Python 3.10** ou superior.
* Uma conta no Google Cloud ou Google AI Studio para obter a **API Key**.

## 🚀 1. Instalação do Ambiente

É altamente recomendável usar um ambiente virtual para isolar as dependências.

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

Com o ambiente ativado, instale o ADK:

```bash
pip install google-adk
```

-----

## 📂 2. Criação do Código do Agente

Você precisará criar uma pasta para o pacote do agente e adicionar os arquivos de código.

1.  Crie uma pasta chamada `multi_tool_agent`.
2.  Dentro dela, crie um arquivo chamado `__init__.py` com apenas uma linha de conteúdo:
    ```python
    from . import agent
    ```
3.  Ainda na mesma pasta, crie o arquivo **`agent.py`** e cole o código abaixo:

**`multi_tool_agent/agent.py`**

```python
import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent

def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified city.

    Args:
        city (str): The name of the city for which to retrieve the weather report.

    Returns:
        dict: status and result or error msg.
    """
    if city.lower() == "new york":
        return {
            "status": "success",
            "report": (
                "The weather in New York is sunny with a temperature of 25 degrees"
                " Celsius (77 degrees Fahrenheit)."
            ),
        }
    else:
        return {
            "status": "error",
            "error_message": f"Weather information for '{city}' is not available.",
        }


def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city.

    Args:
        city (str): The name of the city for which to retrieve the current time.

    Returns:
        dict: status and result or error msg.
    """

    if city.lower() == "new york":
        tz_identifier = "America/New_York"
    else:
        return {
            "status": "error",
            "error_message": (
                f"Sorry, I don't have timezone information for {city}."
            ),
        }

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    report = (
        f'The current time in {city} is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
    )
    return {"status": "success", "report": report}


root_agent = Agent(
    name="weather_time_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions about the time and weather in a city."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about the time and weather in a city."
    ),
    tools=[get_weather, get_current_time],
)
```

-----

## 🔑 3. Configuração de Autenticação (Crucial)

O agente precisa de credenciais para acessar o modelo Gemini. **Não** versionamos este arquivo por segurança.

1.  Crie um arquivo chamado `.env` dentro da pasta `multi_tool_agent`.
2.  Adicione suas credenciais:

**Opção A: Google AI Studio (Padrão)**

```env
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=Sua_Chave_API_Aqui
```

**Opção B: Vertex AI**

```env
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT=Seu_ID_Do_Projeto
GOOGLE_CLOUD_LOCATION=us-central1
```

A estrutura final de arquivos deve ficar assim:

```text
seu-projeto/
├── .venv/
├── multi_tool_agent/
│   ├── __init__.py
│   ├── agent.py     <-- Código principal
│   └── .env         <-- Suas chaves (não subir p/ GitHub)
```

-----

## ▶️ 4. Como Executar

Volte para a pasta raiz do projeto (fora de `multi_tool_agent`) e escolha uma opção:

### Opção 1: Interface Visual (Dev UI)

Acesse uma interface web para testar o agente e visualizar o fluxo de execução.

```bash
adk web
```

  * Abra **http://localhost:8000**.
  * Selecione **"weather\_time\_agent"** no menu.

### Opção 2: Terminal

Interaja diretamente via linha de comando.

```bash
adk run multi_tool_agent
```

-----

## 🛠️ Solução de Problemas

  * **Erro `ModuleNotFoundError`:** Certifique-se de ter criado o arquivo `__init__.py`.
  * **Erro de API Key:** Verifique se o arquivo `.env` está dentro da pasta `multi_tool_agent` e se a chave é válida.
  * **Windows:** Se tiver problemas com o `adk web`, tente usar `adk web --no-reload`.

<!-- end list -->

```
```
