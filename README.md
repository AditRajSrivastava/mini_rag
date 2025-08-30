# AI Document Query Engine (Mini RAG)

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100-009688?style=for-the-badge&logo=fastapi)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel)

A full-stack Retrieval-Augmented Generation (RAG) application that allows users to upload a document, ask questions about it, and receive accurate, cited answers from a large language model.

## 🚀 Live Demo

**You can access the live, deployed application here:**
### [https://mini-rag-five.vercel.app/](https://mini-rag-five.vercel.app/)

---

## Overview

This project is a comprehensive implementation of a modern RAG pipeline. It features a sleek, responsive frontend and a powerful serverless Python backend. A user can paste any block of text, which is then chunked, embedded, and stored in a vector database. Subsequently, the user can ask questions, and the system will retrieve the most relevant context, rerank it for accuracy, and use a powerful LLM to generate a grounded answer with citations to the original source text.

## ✨ Features

* **Dynamic Document Ingestion:** Accepts any block of text and processes it for querying.
* **Advanced RAG Pipeline:** Implements a state-of-the-art Retrieve-Rerank-Generate pipeline for high-quality answers.
* **Cited & Grounded Answers:** The LLM is instructed to answer *only* from the provided context and to cite its sources, reducing hallucinations.
* **Modern & Responsive UI:** A sleek, dark-themed frontend with animations provides a great user experience.
* **Serverless Deployment:** The entire application is deployed on Vercel, showcasing modern cloud-native development practices.

## 🛠️ Architecture & Tech Stack

The application follows a monorepo structure, deployed entirely on Vercel.

**Data Flow:**
`Frontend (Vercel) -> Serverless Function (/api/index) -> RAG Pipeline -> [Qdrant -> Cohere -> Groq] -> Response`

**Key Providers & Technologies:**

| Component          | Technology/Provider                                        | Purpose                                          |
| ------------------ | ---------------------------------------------------------- | ------------------------------------------------ |
| **Frontend** | HTML, CSS, Vanilla JavaScript                              | User Interface & API Communication               |
| **Backend** | Python 3.11, FastAPI                                       | API Logic & RAG Orchestration                    |
| **Hosting** | Vercel                                                     | Frontend Hosting & Serverless Backend Deployment |
| **Vector Database**| **Qdrant Cloud** | Storing Text Embeddings                          |
| **Embeddings** | **Cohere** (`embed-english-v3.0`)                          | Converting Text to Vectors                       |
| **Reranker** | **Cohere** (`rerank-english-v3.0`)                         | Improving relevance of retrieved documents       |
| **LLM** | **Groq** (Llama3 `llama3-8b-8192`)                           | Generating the final answer                      |
| **Orchestration** | LangChain                                                  | Connecting all AI components                     |

### Index Configuration

* **Vector Database:** Qdrant Cloud
* **Embedding Model:** Cohere (`embed-english-v3.0`)
* **Vector Dimensionality:** **1024**

## ⚙️ Local Setup

To run this project on your local machine, follow these steps:

### Prerequisites
* Git
* Python 3.10+
* A code editor like Visual Studio Code with the "Live Server" extension.

### 1. Clone & Setup Backend
```bash
# Clone the repository
git clone [https://github.com/AditRajSrivastava/mini_rag.git] cd mini-rag-project

# Set up the Python environment
cd api
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install dependencies from the root directory
pip install -r ../requirements.txt

# Create your environment file
cp ../.env.example ../.env