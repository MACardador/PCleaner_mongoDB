from pymongo import MongoClient


class DatabaseConfig:
    client = MongoClient('mongodb://localhost:27017/')

    db = client["imageShow"]
