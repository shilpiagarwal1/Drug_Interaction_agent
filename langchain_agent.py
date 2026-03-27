from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOllama


#import os
#os.environ["OPENAI_API_KEY"] = "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"
from tools.langchain_tools import (
    interaction_tool,
    dosage_tool,
    allergy_tool,
    alternatives_tool
)

# LLM
#llm = ChatOpenAI(
 #   model="gpt-4o-mini",
  #  temperature=0
#)


llm = ChatOllama(
    model="llama3"
)

# Tools
tools = [
    interaction_tool,
    dosage_tool,
    allergy_tool,
    alternatives_tool
]

# System Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a medical safety assistant.

STRICT RULES:
- NEVER invent drug interactions
- ONLY use tool outputs
- If unsure, say "Consult a healthcare professional"
- Highlight severe risks clearly
- Always prioritize patient safety
"""),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}")
])

# Create Agent
agent = create_openai_functions_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)

# Executor
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)

# Run function
def run_agent(query: str):
    result = agent_executor.invoke({"input": query})
    return result["output"]