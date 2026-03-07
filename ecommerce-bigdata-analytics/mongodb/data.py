# load_to_atlas.py
import json
from pymongo import MongoClient

uri = "ATLAS_CONNECTION_STRING"
client = MongoClient(uri)
db = client['<dbname>']

def load_file(filename, collection_name):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)   # expects a JSON array
    if data:
        db[collection_name].drop()  # optional
        db[collection_name].insert_many(data)
        print(f"Inserted {len(data)} docs into {collection_name}")

load_file('products_subset.json', 'products')
load_file('users_subset.json', 'users')
load_file('transactions_subset.json', 'transactions')