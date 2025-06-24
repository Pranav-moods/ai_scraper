import chromadb

client = chromadb.PersistentClient(path="./chroma_storage")  # <-- NEW client method

collection = client.get_or_create_collection(name="book_chapters")

with open("final_version.txt", "r", encoding="utf-8") as f:
    final_chapter = f.read()

try:
    collection.add(
        documents=[final_chapter],
        ids=["chapter1_v1"],
        metadatas=[{
            "chapter": 1,
            "version": "final",
            "title": "The Canoe Builder"
        }]
    )
    print("✅ Chapter 1 added.")
except Exception as e:
    print("❌ Error adding Chapter 1:", e)

print(" Total documents in collection:", collection.count())
