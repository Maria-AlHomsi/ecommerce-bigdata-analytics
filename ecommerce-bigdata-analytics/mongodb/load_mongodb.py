from pymongo import MongoClient
import json

client = MongoClient("YOUR_ATLAS_CONNECTION_STRING")

db = client["ecommerce"]

def load_collection(file, collection_name):

    with open(file) as f:
        data = json.load(f)

    collection = db[collection_name]
    collection.insert_many(data)

    print(f"Inserted {len(data)} docs into {collection_name}")

load_collection("../sample_data/products_subset.json","products")
load_collection("../sample_data/users_subset.json","users")
load_collection("../sample_data/transactions_subset.json","transactions")