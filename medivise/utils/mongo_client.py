from pymongo import MongoClient

from medivise.utils.config import mongo_db, mongo_uri


def create_mongo_client():
    client = MongoClient(mongo_uri)
    return client


client = create_mongo_client()
db = client[mongo_db]
