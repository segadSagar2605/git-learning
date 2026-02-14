class Document:
    def __init__(self, title, author, content):
        self.title = title
        self.author = author
        self.content = content
        self.status = "Draft" #Default status is Draft
        self.version = 1.0

    #A method to update the status of the document
    def update_status(self):
        if (self.status == "Published"):
            print(f"{self.title} is already published and cannot be updated.")
        else:
            self.status = "Published"
            print(f"{self.title} status updated to {self.status}.")

    #A method to update the version of the document
    def update_version(self):
        self.version += 0.1
        print(f"{self.title} version updated to {self.version:.1f}.")   

  #CHild class for specific document types
class ConfidentialDocument(Document):
    def __init__(self, title, author, content, confidentiality_level):
        super().__init__(title, author, content)
        self.confidentiality_level = confidentiality_level

    def update_status(self):
        if (self.confidentiality_level > 2):
            print(f"{self.title} is a high confidentiality document and cannot be published.")
        else:
            super().update_status()