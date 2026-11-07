from fastapi import FastAPI, HTTPException
from pydantic import BaseModel #what is pydantic and base model?
import chromadb

app = FastAPI(title="DocuQueryAI", description="A simple and easy to use local RAG API")

chroma_client = chromadb.Client()  #what is a client in this context
collection = chroma_client.get_or_create_collection(name="documents_collection")

class DocumentInput(BaseModel):
    doc_id: str
    text: str

class QueryInput(BaseModel):
    question: str

@app.get("/") #Could this be... an API?
def read_root():
    return {"status": "DocuQueryAI is running successfully!"}

@app.post("/upload")   #???????
def upload_document(doc: DocumentInput):    #doc?? was an object called doc created here as parameter for the function?
    try:
        collection.add(
            documents = [doc.text], #so, document becomes literally an object storing the text of the pdf or whatever I am using as material? Can python do that?
            ids = [doc.doc_id]
        )
        return {"message": f"Documenbt '{doc.doc_id}' successfully indexed."}
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))

@app.post("/query") #Waitttttttt, this is the API!!!!! Is this how APIs work? But I still can't understand the connection between this line of code and the ones below. When does this api loine finish? WHen the next one starts? It doesn't have a parenthesis start and finish...
def query_documents(query: QueryInput):
    try:
        results = collection.query(
            query_texts = [query.question],
            n_results = 1
        )

        matched_docs = results.get("documents", [[]])[0]  #WTF happened here?? why so many empty parenthesis? What does this mean?

        if not matched_docs:
            return {"answer": "No relevant context found in the database."}

        context = matched_docs[0]

        return {
            "question": query.question,
            "retreved_context": context,
            "note": "This is the RAG retrieval step. Ready to plug into an LLM API."
        }
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))  #status code 500? is it like the classic 401 forbidden page? shuld i learn status codes as a software dev? So i can use them all around?