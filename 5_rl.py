import chromadb


from chromadb import PersistentClient
client = PersistentClient(path="./chroma_storage")
collection = client.get_or_create_collection("book_chapters")


def compute_reward(text):
    text = text.lower()
    if "canoe" in text and "strategy" in text:
        return 1.0
    elif "canoe" in text:
        return 0.7
    else:
        return 0.2


def rl_ranked_query(query_text, top_k=3):
    try:
        results = collection.query(query_texts=[query_text], n_results=top_k)

        if not results["documents"] or not results["ids"]:
            print(" No matching documents found.")
            return []

        docs_with_scores = list(zip(results["documents"][0], results["ids"][0]))
        ranked = sorted(docs_with_scores, key=lambda x: -compute_reward(x[0]))
        return ranked

    except Exception as e:
        print(f"❌ Error during query: {e}")
        return []


if __name__ == "__main__":
    ranked = rl_ranked_query("canoe")

    print("\n📚 Ranked Chapter Versions:")
    if not ranked:
        print("⚠️ No results to display.")
    else:
        for idx, (doc, doc_id) in enumerate(ranked, 1):
            print(f"{idx}. {doc_id} — Score: {compute_reward(doc)}")
            print(doc[:300], "\n---")
