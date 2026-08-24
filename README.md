# AI Study Buddy — Local RAG Application

AI Study Buddy is a local study assistant that uses Retrieval-Augmented Generation (RAG) to work with uploaded study materials. Users can upload documents and generate summaries, flashcards, and answers based on their content.

## Overview

The application processes documents locally and uses a vector database to retrieve relevant sections before sending them to a local language model.

The system supports:

* PDF files
* PowerPoint presentations
* Text files

No external API key is required.

## How It Works

```text
Document Upload
      ↓
Text Extraction
      ↓
Document Chunking
      ↓
Vector Embeddings
      ↓
ChromaDB
      ↓
Semantic Retrieval
      ↓
Local LLM (Ollama)
      ↓
Summary / Flashcards / Q&A
```

## Features

### Document Processing

Uploaded documents are extracted and divided into smaller chunks for retrieval.

### Semantic Search

Document chunks are converted into embeddings using `nomic-embed-text` and stored locally in ChromaDB.

### Local LLM

The application uses Ollama to run the `llama3.2` model locally for generating responses.

### Study Tools

The application can generate:

* Concise summaries
* Flashcards
* Context-based answers

## Tech Stack

**Backend**

* Python
* Flask

**RAG & AI**

* LangChain
* Ollama
* ChromaDB

**Models**

* `llama3.2`
* `nomic-embed-text`

**Document Processing**

* PyPDF
* python-pptx

**Frontend**

* HTML5
* CSS3
* JavaScript
* Fetch API

## Setup

### 1. Install Python

Python 3.10 or later is recommended.

### 2. Install Ollama

Install Ollama and download the required local models:

```bash
ollama pull llama3.2
ollama pull nomic-embed-text
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

The Flask application will then be available locally in your browser.

## Privacy

Document processing and model inference are performed locally. The application does not require external AI API keys for its core functionality.

## Project Structure

```text
├── app.py
├── rag_engine.py
├── templates/
│   └── index.html
├── static/
│   └── ...
├── requirements.txt
└── README.md
```
