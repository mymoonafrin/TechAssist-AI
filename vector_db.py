from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

loader = DirectoryLoader(
    "data/knowledge_base",
    glob="*.txt",
    loader_cls=TextLoader
)

documents = loader.load()

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_db = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    persist_directory="data/chroma_db"
)

print(f"Documents loaded: {len(documents)}")
print("ChromaDB created successfully!")