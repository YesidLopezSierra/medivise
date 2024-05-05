from langchain_mongodb import MongoDBAtlasVectorSearch

from medivise.utils.config import mongo_embeddings_collection, mongo_index_collection
from medivise.utils.embeddings import embeddings
from medivise.utils.mongo_client import db

vector_store = MongoDBAtlasVectorSearch(
    db[mongo_embeddings_collection],
    embeddings,
    index_name=mongo_index_collection
)

retriever = vector_store.as_retriever()
