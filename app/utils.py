import os
import shutil
from uuid import uuid4
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA, ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.chains.summarize import load_summarize_chain
from app.config import Config

# Save uploaded PDF to disk
def save_pdf(file, filename):
    os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)
    path = os.path.join(Config.UPLOAD_FOLDER, filename)
    file.save(path)
    return path

# Process and store vector embeddings
def process_and_store_pdf(session_id, pdf_path):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings(openai_api_key=Config.OPENAI_API_KEY)
    db = FAISS.from_documents(chunks, embeddings)

    store_path = os.path.join(Config.VECTORSTORE_FOLDER, session_id)
    os.makedirs(Config.VECTORSTORE_FOLDER, exist_ok=True)
    db.save_local(store_path)

# Load vector store for session
def load_vectorstore(session_id):
    embeddings = OpenAIEmbeddings(openai_api_key=Config.OPENAI_API_KEY)
    store_path = os.path.join(Config.VECTORSTORE_FOLDER, session_id)
    if not os.path.exists(store_path):
        raise FileNotFoundError("Session vector store not found")
    return FAISS.load_local(store_path, embeddings, allow_dangerous_deserialization=True)

# Ask question to vector DB using ConversationalRetrievalChain
def ask_question(session_id, question):
    vectorstore = load_vectorstore(session_id)
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    llm = OpenAI(temperature=0.5, openai_api_key=Config.OPENAI_API_KEY)
    qa = ConversationalRetrievalChain.from_llm(llm=llm, retriever=vectorstore.as_retriever(), memory=memory)

    result = qa.run(question)
    return {"response": result}

# Summarize the paper using map-reduce summarization
def summarize_paper(session_id):
    vectorstore = load_vectorstore(session_id)
    docs = vectorstore.similarity_search("summarize the paper", k=10)

    llm = OpenAI(temperature=0.3, openai_api_key=Config.OPENAI_API_KEY)
    chain = load_summarize_chain(llm, chain_type="map_reduce")

    summary = chain.run(docs)
    return summary
