class Document:
    def __init__(self, title, created_by, content_summary, doc_type, created_at):
        self.title = title
        self.created_by = created_by
        self.content_summary = content_summary  # Renamed for clarity
        self.doc_type = doc_type
        self.created_at = created_at
        self.status = "Draft"
        self.version = 1.0

class ConfidentialDocument(Document):
    def __init__(self, title, created_by, content_summary, doc_type, created_at, confidentiality_level):
        super().__init__(title, created_by, content_summary, doc_type, created_at)
        self.confidentiality_level = confidentiality_level