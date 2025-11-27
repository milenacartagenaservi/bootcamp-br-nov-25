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
   # The Large Language Model (LLM) that agent will use.
   # Please fill in the latest model id that supports live from
   # https://google.github.io/adk-docs/get-started/streaming/quickstart-streaming/#supported-models
   model="gemini-2.0-flash",  # for example: model="gemini-2.0-flash-live-001" or model="gemini-2.0-flash-live-preview-04-09"
   # A short description of the agent's purpose.
   description="Agent to answer questions using Google Search and use bigquery to look at the data.",
   # Instructions to set the agent's behavior.
   instruction="You are an expert researcher and an agent to answer questions about BigQuery data and models and execute, SQL queries. You always stick to the facts.You are a data science agent with access to several BigQuery tools. Make use of those tools to answer the user's questions",
   # Add google_search tool to perform grounding with Google search.
   tools=[bigquery_toolset]
)



# Instantiate a BigQuery toolset


# Agent Definition
#bigquery_agent = Agent(
#    model=GEMINI_MODEL,
#    name=AGENT_NAME,
#    description=(
#        "Agent to answer questions about BigQuery data and models and execute"
#        " SQL queries."
#    ),
#   instruction="""\
#        You are a data science agent with access to several BigQuery tools.
#        Make use of those tools to answer the user's questions.
#    """,
#    tools=[bigquery_toolset],
#)

