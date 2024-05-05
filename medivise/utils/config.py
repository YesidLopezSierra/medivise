
import os

mongo_uri = os.getenv("MONGO_URI")
mongo_db = os.getenv("MONGO_DB")
mongo_embeddings_collection = os.getenv("MONGO_COLLECTION_NAME")
mongo_index_collection = os.getenv("ATLAS_VECTOR_SEARCH_INDEX_NAME")
