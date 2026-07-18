from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

loader = TextLoader('data/shakespeare.txt', encoding='utf-8')
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

chunks = text_splitter.split_documents(documents)

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory="./chroma_db"
)

query = "Who is Romeo?"
results = vector_store.similarity_search(query, k=3)

for doc in results:
    print(doc.page_content)
    print("-" * 50)
    
# User Question
#         ↓
# Embedding
#         ↓
# ChromaDB
#         ↓
# Cosine Similarity
#         ↓
# Top 3 Chunk


# print(len(chunks))
# print(type(documents))
# print(len(documents))
# print(type(documents[0]))
# print(documents[0])