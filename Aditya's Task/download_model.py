from sentence_transformers import SentenceTransformer

print("Downloading 'all-MiniLM-L6-v2' model... This may take a few minutes.")
model = SentenceTransformer('all-MiniLM-L6-v2')
print("Model downloaded and cached successfully!")
