from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import chromadb

app = FastAPI(title="DocuQueryAI", description="A simple and easy to use local RAG API")

chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection(name="documents_collection")

class DocumentInput(BaseModel):
    doc_id: str
    text: str

class QueryInput(BaseModel):
    question: str

@app.get("/")
def read_root():
    return {"status": "DocuQueryAI is running successfully!"}

@app.post("/upload")
def upload_document(doc: DocumentInput):
    try:
        collection.add(
            documents = [doc.text],
            ids = [doc.doc_id]
        )
        return {"message": f"Documenbt '{doc.doc_id}' successfully indexed."}
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))

@app.post("/query")
def query_documents(query: QueryInput):
    try:
        results = collection.query(
            query_texts = [query.question],
            n_results = 1
        )

        matched_docs = results.get("documents", [[]])[0]

        if not matched_docs:
            return {"answer": "No relevant context found in the database."}

        context = matched_docs[0]

        return {
            "question": query.question,
            "retreved_context": context,
            "note": "This is the RAG retrieval step. Ready to plug into an LLM API."
        }
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))