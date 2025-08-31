import os
from dotenv import load_dotenv

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from qdrant_client import QdrantClient
# LangChain Imports
from langchain_cohere import CohereEmbeddings
from langchain_community.vectorstores import Qdrant
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from langchain.prompts import ChatPromptTemplate
from langchain_cohere import CohereRerank
from langchain_groq import ChatGroq
# --- INITIAL SETUP ---

# Load environment variables from .env file
load_dotenv()

# Instantiate the FastAPI app
app = FastAPI()

# --- CORS MIDDLEWARE ---
# This allows your frontend (running on a different domain) to communicate with this backend.
# IMPORTANT: Replace "http://localhost:5500" and "http://127.0.0.1:5500" with the URL of your deployed frontend in production.
origins = [
    "http://localhost:5500",    # For local development with Live Server
    "http://127.0.0.1:5500",   # For local development
    "https://mini-rag-sepia.vercel.app/" # TODO: Add your deployed frontend URL here
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- GLOBAL VARIABLES & CONSTANTS ---
QDRANT_COLLECTION_NAME = "my_rag_collection_cohere"


# --- PYDANTIC MODELS ---
# These models define the expected request body structure for your endpoints.
class UploadData(BaseModel):
    text: str

class QueryData(BaseModel):
    question: str


# --- API ENDPOINTS ---

@app.get("/")
def read_root():
    """ A simple health check endpoint. """
    return {"status": "API is running"}

@app.post("/upload")
async def upload(data: UploadData):
    """
    Endpoint for uploading, chunking, embedding, and storing text in the vector database.
    """
    try:
        # 1. Chunking
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
        chunks = text_splitter.split_text(data.text)

        # 2. Create LangChain Document objects with metadata
        documents = [Document(page_content=chunk, metadata={"position": i + 1}) for i, chunk in enumerate(chunks)]

        # 3. Initialize OpenAI Embeddings
        embeddings = CohereEmbeddings(cohere_api_key=os.getenv("COHERE_API_KEY"), model="embed-english-v3.0")
        # 4. Upsert documents to Qdrant
        # This will create the collection if it doesn't exist, embed the documents, and store them.
        # NOTE: For `text-embedding-3-small`, the vector dimension is 1536.
        Qdrant.from_documents(
            documents,
            embeddings,
            url=os.getenv("QDRANT_URL"),
            api_key=os.getenv("QDRANT_API_KEY"),
            collection_name=QDRANT_COLLECTION_NAME,
            force_recreate=True,  # Set to True for development to start with a fresh DB each time.
        )
        
        return {"message": f"Successfully uploaded {len(documents)} chunks."}

    except Exception as e:
        # Return a more informative error message
        return {"error": f"An error occurred during upload: {str(e)}"}, 500


@app.post("/query")
async def query(data: QueryData):
    """
    Endpoint for querying the RAG pipeline.
    """
    try:
        # 1. Initialize Clients
        embeddings = CohereEmbeddings(cohere_api_key=os.getenv("COHERE_API_KEY"), model="embed-english-v3.0")
        llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama3-8b-8192", temperature=0)
        
        # Connect to the existing Qdrant collection
        # 1. First, create a direct client connection to Qdrant
        client = QdrantClient(
            url=os.getenv("QDRANT_URL"),
            api_key=os.getenv("QDRANT_API_KEY"),
        )

        # 2. Then, use that client to initialize the LangChain vector store
        vector_store = Qdrant(
            client=client,
            collection_name=QDRANT_COLLECTION_NAME,
            embeddings=embeddings,
        )
        
        # 2. Top-k Retrieval from Qdrant
        retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 10})
        retrieved_docs = retriever.get_relevant_documents(data.question)

        # 3. Apply Cohere Reranker
        reranker = CohereRerank(cohere_api_key=os.getenv("COHERE_API_KEY"), model="rerank-english-v3.0", top_n=3)
        reranked_docs = reranker.compress_documents(documents=retrieved_docs, query=data.question)
        
        # 4. Generation with OpenAI LLM
        context_text = "\n\n".join([f"[{doc.metadata['position']}] {doc.page_content}" for doc in reranked_docs])
        
        prompt_template = """
        You are an expert question-answering assistant. Your task is to answer the user's question based ONLY on the provided context.
        
        Here is the context, with each snippet numbered for citation:
        ---
        {context}
        ---
        
        Here is the user's question:
        {question}
        
        Instructions:
        1. Carefully read the context and the question.
        2. Formulate a clear and concise answer.
        3. If the context does not contain the information needed to answer the question, you MUST say "I do not have enough information to answer this question."
        4. For every piece of information you use in your answer, you MUST cite the corresponding source number(s) in brackets, like [1], [2], etc.
        
        Answer:
        """
        
        prompt = ChatPromptTemplate.from_template(prompt_template)
        
        chain = prompt | llm
        
        response_llm = chain.invoke({
            "context": context_text,
            "question": data.question
        })
        
        # 5. Format and return the response
        source_documents = [{"content": doc.page_content, "position": doc.metadata['position']} for doc in reranked_docs]
        
        return {"answer": response_llm.content, "sources": source_documents}

    except Exception as e:
        return {"error": f"An error occurred during query: {str(e)}"}, 500