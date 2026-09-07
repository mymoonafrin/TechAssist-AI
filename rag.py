from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = DirectoryLoader(
    "data/knowledge_base",
    glob="*.txt",
    loader_cls=TextLoader
)

documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = text_splitter.split_documents(documents)

print(f"Loaded documents: {len(documents)}")
print(f"Created chunks: {len(chunks)}")

for i, chunk in enumerate(chunks[:5]):
    print(f"\nChunk {i + 1}:")
    print(chunk.page_content)