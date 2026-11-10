# DocuQuery AI

A lightweight, local Retrieval-Augmented Generation (RAG) API built with **FastAPI**, **ChromaDB**, and **Docker**. Designed as a high-performance boilerplate for semantic search and document querying.

## Tech Stack
* **Framework:** FastAPI (Python)
* **Vector Database:** ChromaDB (Local persistent vector storage)
* **Embeddings:** Sentence-Transformers (Running locally on CPU)
* **Containerization:** Docker



## Quick Start

- [Local Development](#local-development)
- [Running with Docker](#running-with-docker-)
- [API Endpoints](#api-endpoints-)


## Local Development 🖥️

1. Clone the repository:
   ```bash
   git clone https://github.com/cristianxdesantis/DocuQuery-AI.git
   cd DocuQuery-AI
   ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

*If you encounter problems creating a virtual python environment, you might have to install `python3-venv` on your system with your package installer of choice.*

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the development server:
    ```bash
    uvicorn main:app --reload
    ```

5. Access the interactive Swagger UI at: `http://127.0.0.1:8000/docs`



## Running with Docker 🐳

1. Clone the repository:
   ```bash
   git clone https://github.com/cristianxdesantis/DocuQuery-AI.git
   cd DocuQuery-AI
   ```

2. Build the Docker Image:
    ```bash
    docker build -t docuquery-ai .
    ```

3. Run the container:
    ```bash
    docker run -d -p 8000:8000 --name docuquery-app docuquery-ai
    ```

4. Access the interactive Swagger UI at: `http://127.0.0.1:8000/docs`


## API Endpoints 📡

- `GET /`: Health check
- `POST /upload`: Ingests and vectorizes documents into ChromaDB.
    - Payload Example:
    ```bash
    {
        "doc_id": "doc1",
        "text": "Your document content here..."
    }
    ```
- `POST /query`:Performs semantic similarity search against indexed documents.
    - Payload Example:
    ```bash
    {
        "question": "What is covered in the document?"
    }
    ```