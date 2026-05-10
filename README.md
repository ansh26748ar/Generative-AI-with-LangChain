# Generative AI with LangChain 🚀

A comprehensive repository demonstrating **Generative AI applications** using LangChain, with support for multiple LLM providers including OpenAI, Anthropic, Google Gemini, and open-source models via Ollama and Hugging Face.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![LangChain](https://img.shields.io/badge/LangChain-Latest-green)

## 📁 Project Structure

```
LANGCHAIN/
├── 1.Chatbot_Ollama_Local/          # Local Ollama chatbot implementation
│   └── app_local_ollama.py
│
├── 2.Chatbot_with_API_Ollama_local/ # API-based Ollama chatbot with client
│   ├── app.py                        # Server application
│   └── client.py                     # Client for testing
│
├── 3.RAG_Ollama_Local/              # Retrieval-Augmented Generation examples
│   ├── SimpleRAG.ipynb              # Basic RAG implementation
│   ├── retriever.ipynb              # Advanced retriever patterns
│   ├── speech.txt                   # Sample document
│   └── attention-is-all-you-need-Paper.pdf
│
├── 4.LLM_Vs_ChatModels_API/         # Comparison of LLM vs Chat Models
│   ├── 1.llm_openai.py              # OpenAI LLM
│   ├── 2.chatmodel_openai.py        # OpenAI Chat Model
│   ├── 3.chatmodel_anthropic.py     # Anthropic Chat Model
│   ├── 4.chatmodel_gemini.py        # Google Gemini Chat Model
│   ├── 5.chatmodel_HF.py            # Hugging Face Chat Model
│   └── 6.chatmodel_HF_local.py      # Local Hugging Face Model
│
├── requirements.txt                 # Python dependencies
├── README.md                        # This file
└── .env                             # Environment variables (API keys)
```

## 🛠 Tech Stack

| Technology | Purpose |
|-----------|---------|
| **Python** | Core programming language |
| **LangChain** | LLM orchestration framework |
| **OpenAI, Anthropic, Google GenAI** | LLM API integrations |
| **Ollama** | Local LLM support |
| **FastAPI & Streamlit** | Backend & Frontend frameworks |
| **ChromaDB & FAISS** | Vector databases for RAG |
| **python-dotenv** | Environment configuration |

## 💻 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/ansh26748ar/Generative-AI-with-LangChain.git
cd Generative-AI-with-LangChain
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

Create a `.env` file in the root directory with your API keys. You can use `.env.example` as a template:

```bash
cp .env.example .env
```

Then update the `.env` file with your actual credentials

**Happy Learning! 🎉**


