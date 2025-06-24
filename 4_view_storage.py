import chromadb

client = chromadb.PersistentClient(path="./chroma_storage")
collection = client.get_or_create_collection(name="book_chapters")


results = collection.get(include=["documents", "metadatas"])

print("\n Stored Chapters:")
for doc, meta in zip(results['documents'], results['metadatas']):
    print(f"\n🔸 Title: {meta.get('title', 'Untitled')}")
    print(f" Chapter: {meta.get('chapter', 'Unknown')}")
    print(f" Content:\n{doc[:500]}...")  
results = collection.query(
    query_texts=["canoe building"],
    n_results=1
)

print("\n🔍 Query Result:\n", results['documents'][0][0])