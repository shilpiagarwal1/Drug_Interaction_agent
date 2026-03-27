#from langchain_openai import ChatOpenAI#
#import os
#os.environ["OPENAI_API_KEY"] = "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"

from langchain_community.chat_models import ChatOllama

llm = ChatOllama(
    model="llama3"
)

#llm = ChatOpenAI(model="gpt-4o-mini")

print(llm.invoke("Hello"))