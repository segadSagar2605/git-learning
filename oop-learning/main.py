import sqlite3
from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from models import Document, ConfidentialDocument

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

conn = sqlite3.connect('documents.db', check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
 CREATE TABLE IF NOT EXISTS documents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    created_by TEXT NOT NULL,
    content_summary TEXT,
    doc_type TEXT NOT NULL,
    created_at TEXT NOT NULL,
    status TEXT DEFAULT 'Draft',
    version REAL DEFAULT 1.0
)''')
conn.commit()


class DocRequest(BaseModel):
    title: str
    doc_type: str
    content_summary: str


@app.get("/get-all-docs")
def get_documents():
    cursor.execute('SELECT id, title, created_by, content_summary, doc_type, created_at, status, version FROM documents')
    rows = cursor.fetchall()

    documents = []
    for row in rows:
        documents.append({
            "id": row[0],
            "title": row[1],
            "created_by": row[2],
            "content_summary": row[3],
            "doc_type": row[4],
            "created_at": row[5],
            "status": row[6],
            "version": row[7]
        })

    return {
        "Total Count": len(documents),
        "Documents": documents
    }


@app.post("/save_doc")
async def save_document(data: DocRequest):
    user_identiy = "John Doe"
    timeStamp = datetime.now().isoformat()

    new_doc = Document(
        title=data.title,
        created_by=user_identiy,
        content_summary=data.content_summary,
        doc_type=data.doc_type,
        created_at=timeStamp
    )

    cursor.execute('''
        INSERT INTO documents (title, created_by, content_summary, doc_type, created_at)
        VALUES (?, ?, ?, ?, ?)
    ''', (
        new_doc.title,
        new_doc.created_by,
        new_doc.content_summary,
        new_doc.doc_type,
        new_doc.created_at
    ))
    conn.commit()

    return {
        "message": f"Document {data.title} saved successfully by {user_identiy} at {timeStamp} in {data.doc_type} format."
    }