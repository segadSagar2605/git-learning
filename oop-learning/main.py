import sqlite3
from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from models import Document # Assuming your models.py is in the same folder

app = FastAPI()

# Enable CORS so your HTML file can talk to this Python server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database Setup
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
    )
''')
conn.commit()

class DocRequest(BaseModel):
    title: str
    doc_type: str
    content_summary: str

@app.get("/get-all-docs")
def get_documents():
    cursor.execute('SELECT id, title, created_by, content_summary, doc_type FROM documents')
    rows = cursor.fetchall()
    documents = [{"id": r[0], "title": r[1], "created_by": r[2], "content_summary": r[3], "doc_type": r[4]} for r in rows]
    return {"Documents": documents}

@app.post("/save_doc")
async def save_document(data: DocRequest):
    user_identity = "John Doe" 
    timeStamp = datetime.now().isoformat()

    cursor.execute('''
        INSERT INTO documents (title, created_by, content_summary, doc_type, created_at)
        VALUES (?, ?, ?, ?, ?)
    ''', (data.title, user_identity, data.content_summary, data.doc_type, timeStamp))
    conn.commit()

    return {"message": f"SimpleText: Document '{data.title}' saved successfully!"}