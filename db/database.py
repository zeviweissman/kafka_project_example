from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

def get_mongo_client():
    return MongoClient(os.environ['MONGO_URL'])

def get_members_collection():
    db = get_mongo_client()['gym']
    return db['members']

def get_trainers_collection():
    db = get_mongo_client()['gym']
    return db['trainers']