# 💰 Financial Advisor Chatbot 

A Financial Advisor Chatbot built using **Streamlit, SmolAgents, Groq Llama 3.3 70B, and ChromaDB**.
The chatbot retrieves financial knowledge from stored documents using **semantic search** and answers user queries intelligently.

---

## 🚀 Features

* 💬 Chat interface using Streamlit
* 🧠 AI reasoning using SmolAgents
* ⚡ Fast inference using Groq LLM (Llama 3.3 70B)
* 📚 Financial knowledge retrieval using ChromaDB
* 🔍 Semantic search using HuggingFace embeddings
* 🆓 Uses free APIs and open-source tools

---

## 🛠️ Tech Stack

* Python
* Streamlit
* SmolAgents
* Groq LLM
* Chroma Vector Database
* HuggingFace Embeddings

---

## 📂 Project Structure

```
Financial_Advisor_Chatbot
│
├── app.py                # Main Streamlit application
├── chroma_db/            # Vector database
├── .env                  # API keys (not pushed to GitHub)
├── .gitignore            # Ignore secret files
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/thatipellisaikiran/Financial_Advisor_Chatbot.git
```

Move into the project folder:

```
cd Financial_Advisor_Chatbot
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file and add your API key:

```
GROQ_API_KEY=your_groq_api_key_here
```

---

## ▶️ Run the Application

Start the Streamlit app:

```
streamlit run app.py
```

The chatbot will open in your browser.

---

## 💡 Example Questions

* What is compound interest?
* Explain mutual funds.
* What is diversification in investment?
* How does inflation affect savings?

---

## 📊 Architecture

User → Streamlit Chat UI → SmolAgent → Financial Retriever Tool → ChromaDB → Groq LLM → Response

---

## 🔒 Security

API keys are stored in `.env` and excluded using `.gitignore` to prevent exposure.

---

## 📌 Future Improvements

* Add stock market API integration
* Multi-agent financial tools
* Portfolio analysis
* Financial news summarization
* Deployment using Docker

---



