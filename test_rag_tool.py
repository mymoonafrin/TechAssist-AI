from rag_tool import search_knowledge_base

query = "My printer is not printing."

result = search_knowledge_base.invoke({
    "query": query
})

print("\nTechAssist Knowledge Base:")
print(result)