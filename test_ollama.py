from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0
)


response = llm.invoke(
    "Explain what an IT helpdesk does in two simple sentences."
)


print("\nTechAssist AI:")
print(response.content)