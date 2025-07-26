# Simple Multilingual Retrieval Augmented Generation RAG System



# 📚 Bangla-English RAG System (Offline, Ollama + FAISS)

A fully offline Retrieval-Augmented Generation (RAG) pipeline for answering **Bangla and English** queries using a PDF document (e.g., Bangla HSC Book). This system uses FAISS for vector search and **Ollama** (with Mistral) for answer generation.

---

## 🔧 Features

- 🔍 Query understanding in **Bangla and English**
- 📖 PDF-to-Chunk pre-processing (sentence-level for accuracy)
- 🌐 Multilingual Embedding via `intfloat/multilingual-e5-base`
- 📦 FAISS vector store for fast semantic retrieval
- 🤖 Local LLM support via **Ollama** (e.g., gemma:2b, LLaMA)
- 🛜 Optional FastAPI server for API-based interaction

---

## 🧰 Tools & Libraries

| Purpose        | Tool/Library                       |
|----------------|------------------------------------|
| Embedding      | `intfloat/multilingual-e5-base`    |
| LLM            | `Ollama` with `mistral` model      |
| Vector Search  | `FAISS`                            |
| PDF Parsing    | `PyMuPDF` (fitz)                   |
| API Server     | `FastAPI`, `Uvicorn`               |

---

## 📁 Project Structure

```

offline\_rag\_ollama/
├── data/                       ← Place your PDF file here
├── preprocess/
│   └── extract\_pdf\_pages.py   ← Extracts + chunks each page
├── embed\_and\_store.py         ← Embeds chunks into FAISS
├── rag\_pipeline.py            ← RAG query pipeline (terminal)
├── api/
│   └── main.py                ← FastAPI server
├── requirements.txt
└── README.md

````

---

## 🚀 Setup Instructions

### 1. Install [Ollama](https://ollama.com/download) and run your LLM:
```bash
ollama run mistral
````

### 2. Clone the repository

```bash
git clone https://github.com/your-username/offline_rag_ollama.git
cd offline_rag_ollama
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 4. Put your Bangla Book PDF

Place your PDF file (e.g., `HSC26_Bangla_1st.pdf`) in the `data/` folder.

---

## ⚙️ Running the Pipeline

### Step 1: Preprocess and Split PDF (into small sentence-based chunks)

```bash
python preprocess/extract_pdf_pages.py
```

### Step 2: Create FAISS Embeddings

```bash
python embed_and_store.py
```

### Step 3: Run RAG for a Question

```bash
python rag_pipeline.py
```

> Example input:

```text
অনুপমের ভাষায় সুপুরুষ কাকে বলা হয়েছে?
```

---

## 🌐 Run the API Server

```bash
uvicorn api.main:app --reload
```

Then open:

```
http://localhost:8000/docs
```

---

## 🧪 Sample Test Questions

| Bangla Question                                 | Expected Answer |
| ----------------------------------------------- | --------------- |
| অনুপমের ভাষায় সুপুরুষ কাকে বলা হয়েছে?            | শুম্ভুনাথ       |
| কাকে অনুপমের ভাগ্য দেবতা বলে উল্লেখ করা হয়েছে?    | মামাকে          |
| বিয়ের সময় কল্যাণীর প্রকৃত বয়স কত ছিল?             | ১৫ বছর          |

---

## ❓ FAQ

**Q: What chunking strategy is used?**
A: Sentence-based chunking (\~2-4 sentences per chunk) to maintain semantic focus in Bangla texts.

**Q: Which embedding model is used and why?**
A: `intfloat/multilingual-e5-base` — provides accurate multilingual (Bangla+English) semantic representations.

**Q: How does it match a question to context?**
A: FAISS compares the E5 embedding of the query to precomputed chunk embeddings (cosine similarity).

**Q: What if the question is vague or lacks context?**
A: The system may return less relevant chunks. Future enhancement: query rewriting or context expansion.

---

---


