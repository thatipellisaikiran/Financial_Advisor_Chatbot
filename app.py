import os
import streamlit as st
from smolagents import CodeAgent, OpenAIModel, Tool
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get GROQ API KEY safely
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# ========================== FREE RETRIEVER TOOL ==========================
class FinancialRetrieverTool(Tool):
    name = "financial_retriever"
    description = "Retrieves relevant financial documents using semantic search."
    inputs = {"query": {"type": "string", "description": "Financial query"}}
    output_type = "string"

    def __init__(self):
        super().__init__()
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        self.vectorstore = Chroma(
            persist_directory="./chroma_db",
            embedding_function=embeddings
        )

    def forward(self, query: str) -> str:
        docs = self.vectorstore.similarity_search(query, k=5)

        if not docs:
            return "No relevant financial documents found in the knowledge base."

        return "\n\n".join(
            [f"--- Doc {i+1} ---\n{doc.page_content}" for i, doc in enumerate(docs)]
        )

# ========================== SMOLAGENT WITH GROQ ==========================
@st.cache_resource
def load_agent():

    model = OpenAIModel(
        model_id="llama-3.3-70b-versatile",
        api_key=GROQ_API_KEY,
        api_base="https://api.groq.com/openai/v1",
        temperature=0.1,
        max_tokens=1024
    )

    retriever_tool = FinancialRetrieverTool()

    agent = CodeAgent(
        tools=[retriever_tool],
        model=model,
        add_base_tools=False,
        verbosity_level=2,
        max_steps=6
    )

    return agent


agent = load_agent()

# ========================== STREAMLIT UI ==========================
st.title("💰 Financial Chatbot PoC - 100% FREE")
st.caption("Groq (Llama 3.3 70B) + Local ChromaDB + SmolAgent + Streamlit")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask anything about finance..."):

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking + retrieving financial docs..."):

            history = "\n".join(
                [f"{m['role']}: {m['content']}" for m in st.session_state.messages[:-1]]
            )

            task = f"""
Previous conversation:
{history}

Current question:
{prompt}

Use the financial_retriever tool to get real data from documents when needed.
"""

            response = agent.run(task)

            st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})