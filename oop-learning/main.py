from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()
#now temporily we will use a list to store our data, but in real world we will use a database
document_database=[]

class DocRequest(BaseModel):
    title: str
    doc_type: str

@app.get("/get-all-docs")
def get_documents():
    return {"Total Count": len(document_database), "Documents": document_database}

@app.post("/save_doc")
async def save_document(data: DocRequest):
    document_database.append(data)
    return {"message": f"Document {data.title}saved successfully!"}