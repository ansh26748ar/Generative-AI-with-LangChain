from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

documents = [
    "Virat Kohli is known for his aggressive batting style and consistency.",
    "MS Dhoni is admired for his calm captaincy and finishing skills.", 
    "Rohit Sharma is famous for scoring massive centuries in ODI cricket.", 
    "Jasprit Bumrah is known for his deadly yorkers and unique bowling action.", 
    "Sachin Tendulkar is called the God of Cricket for his legendary career."
]

query = 'tell me about Virat Kohli'

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

#print(cosine_similarity([query_embedding], doc_embeddings))

scores = cosine_similarity([query_embedding], doc_embeddings)

index, score = sorted(list(enumerate(scores)), key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print("Similarity Score is: ", score)

