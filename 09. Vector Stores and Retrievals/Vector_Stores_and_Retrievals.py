
# Install required libraries
# !pip install faiss-cpu

import os
import warnings
from dotenv import load_dotenv



# Document Loader
from langchain_community.document_loaders import PyMuPDFLoader

pdfs = []
for root, dirs, files in os.walk("rag-dataset/health supplements"):
    for file in files:
        if file.endswith(".pdf"):
            pdfs.append(os.path.join(root, file))

docs = []
for pdf in pdfs:
    loader = PyMuPDFLoader(pdf)
    temp = loader.load()
    docs.extend(temp)

# Document Chunking
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunks = text_splitter.split_documents(docs)

# Tokenization
import tiktoken

encoding = tiktoken.encoding_for_model("gpt-4o-mini")
len(encoding.encode(chunks[0].page_content)), len(encoding.encode(chunks[1].page_content)), len(encoding.encode(docs[1].page_content))

# Document Vector Embedding
from langchain_ollama import OllamaEmbeddings
import faiss
from langchain_community.vectorstores import FAISS
from langchain_community.docstore.in_memory import InMemoryDocstore

embeddings = OllamaEmbeddings(model='nomic-embed-text', base_url='http://localhost:11434')
vector = embeddings.embed_query("Hello World")

index = faiss.IndexFlatL2(len(vector))
vector_store = FAISS(
    embedding_function=embeddings,
    index=index,
    docstore=InMemoryDocstore(),
    index_to_docstore_id={},
)

# Add documents to vector store
ids = vector_store.add_documents(documents=chunks)

# Retrieval
question = "how to gain muscle mass?"
docs = vector_store.search(query=question, k=5, search_type="similarity")

# Save vector store locally
db_name = "../health_supplements"
vector_store.save_local(db_name)
