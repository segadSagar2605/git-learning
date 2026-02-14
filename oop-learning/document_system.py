from models import Document, ConfidentialDocument
#Example usage
doc1 = Document("OOP in Python", "John Doe","PDF")
doc2 = Document("Data Structures", "Jane Smith","Word")

#check initial status and version
print(f"{doc1.title} - Status: {doc1.status}, Version: {doc1.version}")
print(f"{doc2.title} - Status: {doc2.status}, Version: {doc2.version}")

#Update status and version
doc1.update_status()
doc1.update_version()
doc1.update_version()

#check doc2 status and version
print(f"{doc2.title} - Status: {doc2.status}, Version: {doc2.version}")

##Create a confidential document
conf_doc = ConfidentialDocument("Company Strategy", "Alice Brown", "PDF", 3)
print(f"{conf_doc.title} - Status: {conf_doc.status}, Confidentiality Level: {conf_doc.confidentiality_level}")
conf_doc.update_status() #This should print a message that the document cannot be published due to high confidentiality level


##Print a html report of the documents
#open a file to write the report
my_docs = [doc1, doc2, conf_doc]  
with open("report.html", "w") as f:
    f.write("<html><body>")
    f.write("<h1>OpenText Document Report</h1>")
    f.write("<table border='1'>")
    f.write("<tr><th>Title</th><th>Author</th><th>Status</th><th>Version</th><th>Confidentiality Level</th></tr>")
    
    # LOOP through your objects and write HTML rows
    for doc in my_docs:
        # Determine color based on status
        color = "green" if doc.status == "Published" else "red"
        confidentiality_level = getattr(doc, 'confidentiality_level', 'N/A')
        
        f.write(f"<tr>")
        f.write(f"<td>{doc.title}</td>")
        f.write(f"<td>{doc.author}</td>")
        f.write(f"<td style='color:{color}'>{doc.status}</td>")
        f.write(f"<td>{doc.version:.1f}</td>")
        f.write(f"<td>{confidentiality_level}</td>")
        f.write(f"</tr>")
        
    f.write("</table>")
    f.write("</body></html>")

print("✅ Report generated: report.html")