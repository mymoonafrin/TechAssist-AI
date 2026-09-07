from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_db = Chroma(
    persist_directory="data/chroma_db",
    embedding_function=embeddings
)

llm = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0
)

query = input("\nDescribe your IT problem: ")

results = vector_db.similarity_search(query, k=3)

context = "\n\n".join(
    document.page_content for document in results
)

prompt = f"""
You are TechAssist AI, an IT helpdesk assistant.

Use the provided knowledge base to help the user troubleshoot their problem.

Knowledge Base:
{context}

User Problem:
{query}

Instructions:
- Give a clear and simple answer.
- Provide numbered troubleshooting steps.
- Use only information supported by the knowledge base.
- Do not invent technical solutions.
- If the knowledge base does not contain enough information, say that the issue should be escalated to IT support.
"""

response = llm.invoke(prompt)

print("\nTechAssist AI:")
print(response.content)