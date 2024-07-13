from src.helper import load_data,text_split,download_hugging_face_embedding
from langchain_pinecone import Pinecone
from pinecone import Pinecone as PineconeClient
import os

from dotenv import load_dotenv

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_ENV = os.environ.get('PINECONE_ENV')

# print(PINECONE_API_KEY)
# print(PINECONE_ENV)

extracted_data = load_data("data/")
text_chunks = text_split(extracted_data)
embedding = download_hugging_face_embedding()

index_name = "medical-chatbot"
pinecone = PineconeClient(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)


index = pinecone.Index(index_name)
# Creating Embeddings for Each of The Text Chunks & storing with metadata
if index.describe_index_stats().get('total_vector_count', 0) == 0:
    print("Upserting documents to the index...")
    vectors = [(str(i), embedding.embed_query(t.page_content), {"text": t.page_content}) for i, t in enumerate(text_chunks)]
    for i in range(0, len(vectors), 100):
        batch = vectors[i:i + 100]
        index.upsert(vectors=batch)
    print("Documents upserted.")
else:
    print("Pinecone index is already populated.")