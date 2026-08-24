# 🎓 AI Study Buddy — Local RAG Application

AI Study Buddy is an offline, privacy-first Retrieval-Augmented Generation (RAG) study assistant built with Flask, LangChain, ChromaDB, and Ollama. It allows users to upload study materials (PDF, PPTX, TXT) and automatically generate concise summaries and flashcards.

---

## 🚀 Key Features

* **100% Local & Private:** Runs entirely on your machine using Ollama (`llama3.2` and `nomic-embed-text`) with zero API keys required.
* **Multi-Format Ingestion:** Supports text extraction from `.pdf`, `.pptx`, and `.txt` files.
* **Vector Search:** Automatically chunks text and generates vector embeddings stored in a local ChromaDB instance.
* **Automated Study Tools:** Generates structured core summaries and flashcards via customized prompt chains.

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Orchestration:** LangChain
* **LLM & Embeddings:** Ollama (`llama3.2`, `nomic-embed-text`)
* **Vector Store:** ChromaDB
* **Document Loaders:** PyPDF, python-pptx
* **Frontend:** HTML5, CSS3, JavaScript (Fetch API)

---

## 📦 Setup & Installation

### 1. Prerequisites
* Install [Python 3.10+](https://www.python.org/)
* Install [Ollama](https://ollama.com/) and pull the necessary local models:
  ```bash
  ollama pull llama3.2
  ollama pull nomic-embed-text