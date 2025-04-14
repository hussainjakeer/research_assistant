AI Research Paper Assistant

This is an intelligent web application that lets you upload academic PDFs (research papers, whitepapers, etc.) and interact with them using natural language. You can ask questions about the content and get summaries — powered by OpenAI, LangChain, and FAISS.

Built with:

🧠 LangChain + OpenAI (GPT-3.5/GPT-4)

📄 PDF ingestion & vector storage (FAISS)

⚙️ Flask + Blueprints (production-ready backend)

🎨 HTML + TailwindCSS + JavaScript (lightweight frontend)

🐳 Dockerized for easy deployment

—-------------------------------------------------

🚀 Features

✅ Upload research papers (PDFs)
✅ Extract text and generate embeddings
✅ Ask questions with context-aware answers
✅ Get intelligent summaries of the documents
✅ Session-based vector storage per user
✅ Simple & clean web UI (TailwindCSS)
✅ Modular Flask backend with Blueprints
✅ Docker-ready for containerized deployment

—-------------------------------------------------

📦 Folder Structure

research-assistant/
├── app/ → Flask app code
│ ├── init.py → App factory
│ ├── config.py → Environment config
│ ├── routes/ → Blueprint APIs (upload, ask, summarize)
│ ├── utils.py → Core LangChain/FAISS logic
│ └── vectorstores/ → Persistent FAISS sessions
├── templates/ → HTML frontend
│ └── index.html
├── static/ → TailwindCSS (or CDN)
├── uploads/ → Temporary file storage
├── .env → OpenAI keys + port
├── run.py → Flask entry point
├── Dockerfile → Docker setup
├── requirements.txt
└── README.md → You're here!

—-------------------------------------------------

📋 How It Works

Upload a PDF file

The server:

Extracts text using PyPDFLoader

Splits it into chunks

Embeds chunks via OpenAI embeddings

Stores them in FAISS (per session)

You can:

Ask questions (ConversationalRetrievalChain)

Summarize the paper (map-reduce summarization)

—-------------------------------------------------

💻 Run Locally

Clone the repo:

git clone https://github.com/hussainjakeer/research_assistant
cd research-assistant

Add your OpenAI key to .env:

OPENAI_API_KEY=your-api-key
FLASK_RUN_PORT=5000

Install dependencies:

pip install -r requirements.txt

Run the app:

python run.py

Visit http://localhost:5000 in your browser

—-------------------------------------------------

🐳 Run with Docker

docker build -t research-assistant .
docker run -p 5000:5000 --env-file .env research-assistant

—-------------------------------------------------

🧠 Key Dependencies

langchain

openai

faiss-cpu

pypdf

flask

python-dotenv

flask-cors

—-------------------------------------------------

📘 Sample Use Cases

Reading long academic papers quickly

Summarizing PhD theses or technical docs

Question-answering over scientific research

Preparing notes from uploaded papers

—-------------------------------------------------

📌 To-Do / Enhancements

Multi-PDF support per session

Login/auth with session storage

UI: Chat history, context view

Streaming responses with websockets

