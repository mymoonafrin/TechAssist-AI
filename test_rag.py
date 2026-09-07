from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_db = Chroma(
    persist_directory="data/chroma_db",
    embedding_function=embeddings
)

query = "My laptop is connected to Wi-Fi but I cannot access the internet."

results = vector_db.similarity_search(query, k=3)

print("\nUser Query:")
print(query)

print("\nRetrieved Knowledge:\n")

for i, result in enumerate(results, 1):
    print(f"--- Result {i} ---")
    print(result.page_content)
    print()