import os
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

print("🚀 Starting ingestion...")

# Load PDFs
loader = PyPDFDirectoryLoader("C:\DS and python notes\GEN AI notes\Financial_Advisor_Chatbot")
docs = loader.load()

print(f"📄 Found {len(docs)} PDF documents")

if len(docs) == 0:
    print("❌ ERROR: No PDFs found in 'financial_docs/' folder!")
    print("   → Create the folder and add at least one .pdf file")
    exit()

# Split
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)

print(f"✂️  Split into {len(splits)} chunks")

# Embeddings (free local)
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Create Chroma
vectorstore = Chroma.from_documents(
    documents=splits,
    embedding=embeddings,
    persist_directory="./chroma_db"
)

print("✅ SUCCESS! ChromaDB created with", vectorstore._collection.count(), "documents")
print("   You can now run: streamlit run app.py")