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

## 🔑 Configuração de Autenticação (Crucial)

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

*(Nota: Se usar Vertex AI, lembre-se de).*

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

