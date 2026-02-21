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

# Calculate stats
published_count = sum(1 for doc in my_docs if doc.status == "Published")
draft_count = sum(1 for doc in my_docs if doc.status == "Draft")
total_count = len(my_docs)
confidential_count = sum(1 for doc in my_docs if hasattr(doc, 'confidentiality_level') and doc.confidentiality_level != 'N/A')

print("\n--- Generating Web Report ---")
my_docs = [doc1, doc2, conf_doc]

with open("report.html", "w") as f:
    f.write("<html>\n")
    
    # NEW: Add a head section to link the CSS
    f.write("<head>\n")
    f.write("  <link rel='stylesheet' href='style.css'>\n")
    f.write("</head>\n")
    
    f.write("<body>\n")
    f.write("<h1>OpenText Document Report</h1>\n")
    # We removed the ugly border='1' because CSS handles it now
    f.write("<table>\n") 
    f.write("<tr><th>Title</th><th>Author</th><th>Status</th><th>Version</th></tr>\n")
    
    for doc in my_docs:
        # We can still use inline styles for dynamic data like status colors!
        color = "green" if doc.status == "Published" else "red"
        
        f.write("<tr>\n")
        f.write(f"<td>{doc.title}</td>\n")
        f.write(f"<td>{doc.author}</td>\n")
        f.write(f"<td style='color:{color}; font-weight:bold;'>{doc.status}</td>\n")
        f.write(f"<td>v{doc.version:.1f}</td>\n")
        f.write("</tr>\n")
        
    f.write("</table>\n")
    f.write("</body>\n</html>")

print("✅ Modern report generated: report.html")