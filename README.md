# AI Document Query Engine (Mini RAG)

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100-009688?style=for-the-badge&logo=fastapi)
![Vercel](https://img.shields.io/badge/Deployed%20on-Vercel-000000?style=for-the-badge&logo=vercel)
![Render](https://img.shields.io/badge/Backend%20on-Render-46E3B7?style=for-the-badge&logo=render)

A full-stack Retrieval-Augmented Generation (RAG) application that allows users to upload a document, ask questions about it, and receive accurate, cited answers from a large language model.

---

### **[🚀 Live Demo](https://mini-rag-sepia.vercel.app/) &nbsp;&nbsp; | &nbsp;&nbsp; [📂 GitHub Repository](https://github.com/AditRajSrivastava/mini_rag) &nbsp;&nbsp; | &nbsp;&nbsp; [👨‍💻 My LinkedIn Profile](https://linkedin.com/in/aditya-raj-srivastava-2570a7254/)**

---

## Overview

This project is a comprehensive implementation of a modern RAG pipeline, built as part of an AI Engineer assessment. It features a sleek, responsive frontend and a powerful Python backend. A user can paste any block of text, which is then chunked, embedded, and stored in a vector database. Subsequently, the user can ask questions, and the system will retrieve the most relevant context, rerank it for accuracy, and use a powerful LLM to generate a grounded answer with citations to the original source text.

## ✨ Features

* **Dynamic Document Ingestion:** Accepts any block of text and processes it for querying in real-time.
* **Advanced RAG Pipeline:** Implements a state-of-the-art Retrieve-Rerank-Generate pipeline for high-quality, relevant answers.
* **Cited & Grounded Answers:** The LLM is instructed to answer *only* from the provided context and to cite its sources, significantly reducing hallucinations.
* **Modern & Responsive UI:** A sleek, dark-themed frontend built with vanilla HTML, CSS, and JavaScript provides a great user experience with smooth animations.
* **Separated Frontend/Backend Deployment:** Follows industry best practices by deploying the static frontend to Vercel and the stateful backend service to Render.

## 🛠️ Architecture & Tech Stack

The application follows a decoupled architecture, with the frontend and backend hosted on separate, specialized platforms.

**Data Flow:**
`Frontend (Vercel) -> Backend API (Render) -> RAG Pipeline -> [Qdrant -> Cohere -> Groq] -> Response`

**Key Providers & Technologies:**

| Component | Technology/Provider | Purpose |
| :--- | :--- | :--- |
| **Frontend** | HTML, CSS, Vanilla JavaScript | User Interface & API Communication |
| **Backend** | Python 3.11, FastAPI | API Logic & RAG Orchestration |
| **Frontend Hosting** | Vercel | Global CDN for a fast static site |
| **Backend Hosting** | Render | Service hosting for the Python application |
| **Vector Database**| **Qdrant Cloud** | Storing Text Embeddings |
| **Embeddings** | **Cohere** (`embed-english-v3.0`) | Converting Text to Vectors |
| **Reranker** | **Cohere** (`rerank-english-v3.0`) | Improving relevance of retrieved documents |
| **LLM** | **Groq** (Llama3 `llama3-8b-8192`) | Generating the final answer |
| **Orchestration** | LangChain | Connecting all AI components |

### Index Configuration

* **Vector Database:** Qdrant Cloud
* **Embedding Model:** Cohere (`embed-english-v3.0`)
* **Vector Dimensionality:** **1024**

## ⚙️ Local Setup

To run this project on your local machine, follow these steps:

### Prerequisites
* Git
* Python 3.10+
* A code editor like VS Code with the "Live Server" extension.

### 1. Clone & Setup Backend
```bash
# Clone the repository
git clone [https://github.com/AditRajSrivastava/mini_rag.git](https://github.com/AditRajSrivastava/mini_rag.git)
cd mini_rag

# Set up the Python environment
cd backend
python -m venv venv
# On Windows
venv\Scripts\activate
# On MacOS/Linux
# source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create your environment file from the example
cp .env.example .env
Of course. Here is the complete and fully corrected README.md file with all the fixes applied.

I have:

Removed all the duplicated content.

Corrected the LinkedIn and GitHub links in the 'Contact' section to be direct links.

Fixed the formatting of the git clone command in the 'Local Setup' instructions.

You can now replace the entire content of your README.md file with the text below. This is the final version, ready for submission.

Markdown

# AI Document Query Engine (Mini RAG)

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100-009688?style=for-the-badge&logo=fastapi)
![Vercel](https://img.shields.io/badge/Deployed%20on-Vercel-000000?style=for-the-badge&logo=vercel)
![Render](https://img.shields.io/badge/Backend%20on-Render-46E3B7?style=for-the-badge&logo=render)

A full-stack Retrieval-Augmented Generation (RAG) application that allows users to upload a document, ask questions about it, and receive accurate, cited answers from a large language model.

---

### **[🚀 Live Demo](https://mini-rag-sepia.vercel.app/) &nbsp;&nbsp; | &nbsp;&nbsp; [📂 GitHub Repository](https://github.com/AditRajSrivastava/mini_rag) &nbsp;&nbsp; | &nbsp;&nbsp; [👨‍💻 My LinkedIn Profile](https://linkedin.com/in/aditya-raj-srivastava-2570a7254/)**

---

## Overview

This project is a comprehensive implementation of a modern RAG pipeline, built as part of an AI Engineer assessment. It features a sleek, responsive frontend and a powerful Python backend. A user can paste any block of text, which is then chunked, embedded, and stored in a vector database. Subsequently, the user can ask questions, and the system will retrieve the most relevant context, rerank it for accuracy, and use a powerful LLM to generate a grounded answer with citations to the original source text.

## ✨ Features

* **Dynamic Document Ingestion:** Accepts any block of text and processes it for querying in real-time.
* **Advanced RAG Pipeline:** Implements a state-of-the-art Retrieve-Rerank-Generate pipeline for high-quality, relevant answers.
* **Cited & Grounded Answers:** The LLM is instructed to answer *only* from the provided context and to cite its sources, significantly reducing hallucinations.
* **Modern & Responsive UI:** A sleek, dark-themed frontend built with vanilla HTML, CSS, and JavaScript provides a great user experience with smooth animations.
* **Separated Frontend/Backend Deployment:** Follows industry best practices by deploying the static frontend to Vercel and the stateful backend service to Render.

## 🛠️ Architecture & Tech Stack

The application follows a decoupled architecture, with the frontend and backend hosted on separate, specialized platforms.

**Data Flow:**
`Frontend (Vercel) -> Backend API (Render) -> RAG Pipeline -> [Qdrant -> Cohere -> Groq] -> Response`

**Key Providers & Technologies:**

| Component | Technology/Provider | Purpose |
| :--- | :--- | :--- |
| **Frontend** | HTML, CSS, Vanilla JavaScript | User Interface & API Communication |
| **Backend** | Python 3.11, FastAPI | API Logic & RAG Orchestration |
| **Frontend Hosting** | Vercel | Global CDN for a fast static site |
| **Backend Hosting** | Render | Service hosting for the Python application |
| **Vector Database**| **Qdrant Cloud** | Storing Text Embeddings |
| **Embeddings** | **Cohere** (`embed-english-v3.0`) | Converting Text to Vectors |
| **Reranker** | **Cohere** (`rerank-english-v3.0`) | Improving relevance of retrieved documents |
| **LLM** | **Groq** (Llama3 `llama3-8b-8192`) | Generating the final answer |
| **Orchestration** | LangChain | Connecting all AI components |

### Index Configuration

* **Vector Database:** Qdrant Cloud
* **Embedding Model:** Cohere (`embed-english-v3.0`)
* **Vector Dimensionality:** **1024**

## ⚙️ Local Setup

To run this project on your local machine, follow these steps:

### Prerequisites
* Git
* Python 3.10+
* A code editor like VS Code with the "Live Server" extension.

### 1. Clone & Setup Backend
```bash
# Clone the repository
git clone [https://github.com/AditRajSrivastava/mini_rag.git](https://github.com/AditRajSrivastava/mini_rag.git)
cd mini_rag

# Set up the Python environment
cd backend
python -m venv venv
# On Windows
venv\Scripts\activate
# On MacOS/Linux
# source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create your environment file from the example
cp .env.example .env 
Next, open the backend/.env file and add your secret API keys from Qdrant, Cohere, and Groq.

# 2. Run the Backend Server
# From the backend/ directory, start the API server
uvicorn main:app --reload
The backend will be running at http://127.0.0.1:8000.

# 3. Run the Frontend Server
Open the project's root folder (mini_rag) in VS Code.

Right-click on the public/index.html file.

Select "Open with Live Server".

Your browser will open the application, ready to communicate with your local backend.

🎯 Evaluation
The RAG pipeline was tested on several texts to evaluate its accuracy, citation capability, and robustness.

Test Case 1: Tech History
Context Provided:

The resurgence of artificial intelligence in the 21st century is largely thanks to breakthroughs in deep learning. After a period of reduced funding and interest known as the "AI winter," progress began to accelerate in the 2000s...

Question: What was the name of the deep neural network that won the ImageNet challenge in 2012?

✅ Result: "The name of the deep neural network that won the ImageNet challenge in 2012 was AlexNet, created by Alex Krizhevsky, Ilya Sutskever, and Geoffrey Hinton. [1]"

Analysis: Correctly retrieved the specific name and associated entities from the text.

Test Case 2: Scientific Facts
Context Provided:

The James Webb Space Telescope (JWST) is the most powerful space telescope ever built, launched in December 2021...

Question: Who is the lead scientist on the James Webb Space Telescope project?

✅ Result: "I do not have enough information to answer this question."

Analysis: Correctly identified that the answer was not in the provided context, successfully avoiding hallucination.

Remarks (Limitations & Future Work)
Limitations
Single Document Context: The application currently handles a single pasted text at a time. It does not support file uploads or multiple documents.

No Chat History: Each query is independent. The model does not remember previous questions in a conversation.

API Rate Limits: The application relies on the free tiers of various services, which come with rate limits that could affect performance in a high-traffic scenario.

Future Work
File Uploads: Implement support for uploading .pdf, .txt, and .md files to make the application more versatile.

Chat Interface: Convert the Q&A format to a conversational chat interface with memory, allowing for follow-up questions.

Streaming Responses: Stream the LLM response token by token to the frontend to improve the perceived performance and user experience.

📄 Contact
Feel free to connect with me and explore my other projects.

LinkedIn: linkedin.com/in/aditya-raj-srivastava-2570a7254/

GitHub: github.com/AditRajSrivastava