from langchain_core.tools import tool
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_db = Chroma(
    persist_directory="data/chroma_db",
    embedding_function=embeddings
)

@tool
def search_knowledge_base(query: str):
    """Search the IT troubleshooting knowledge base for relevant information."""

    results = vector_db.similarity_search_with_score(query, k=3)

    if not results:
        return "No relevant information was found in the knowledge base."

    query_words = set(query.lower().split())

    best_document = results[0][0]
    best_score = -1

    for document, distance in results:
        text = document.page_content.lower()

        title = ""
        problem = ""

        for line in document.page_content.splitlines():
            if line.lower().startswith("title:"):
                title = line[6:].strip().lower()

            if line.lower().startswith("problem:"):
                problem = line[8:].strip().lower()

        title_words = set(title.split())
        problem_words = set(problem.split())

        title_matches = len(query_words.intersection(title_words))
        problem_matches = len(query_words.intersection(problem_words))

        score = title_matches * 3 + problem_matches

        if score > best_score:
            best_score = score
            best_document = document

    return best_document.page_content