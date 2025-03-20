from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage

llm = ChatOllama(
    model="gemma3:1b",
    temperature=0
)

messages = [
        SystemMessage("Translate the following from English to Portuguese"),
        HumanMessage("What do you do for living?"),
]

response = llm.invoke(messages)
print(response)

