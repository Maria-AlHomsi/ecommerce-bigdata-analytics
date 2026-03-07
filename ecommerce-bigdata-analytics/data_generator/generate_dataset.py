import json
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

NUM_USERS = 100
NUM_PRODUCTS = 50
NUM_TRANSACTIONS = 200

products = []
users = []
transactions = []

# Generate products
for i in range(NUM_PRODUCTS):
    product = {
        "_id": f"prod_{i}",
        "name": fake.word(),
        "category": {
            "category_id": f"cat_{random.randint(1,5)}",
            "category_name": random.choice(["Electronics","Clothing","Books"])
        },
        "base_price": round(random.uniform(10,200),2),
        "creation_date": str(fake.date_time_this_year())
    }
    products.append(product)

# Generate users
for i in range(NUM_USERS):
    user = {
        "_id": f"user_{i}",
        "name": fake.name(),
        "email": fake.email(),
        "registration_date": str(fake.date_time_this_year()),
        "total_spent": 0,
        "purchase_count": 0
    }
    users.append(user)

# Generate transactions
for i in range(NUM_TRANSACTIONS):
    user = random.choice(users)
    items = []
    total = 0

    for _ in range(random.randint(1,4)):
        product = random.choice(products)
        qty = random.randint(1,3)
        subtotal = product["base_price"] * qty

        items.append({
            "product_id": product["_id"],
            "quantity": qty,
            "subtotal": subtotal
        })

        total += subtotal

    transaction = {
        "_id": f"txn_{i}",
        "user_id": user["_id"],
        "timestamp": str(fake.date_time_this_year()),
        "items": items,
        "total_amount": total,
        "status": "completed"
    }

    transactions.append(transaction)

with open("products_subset.json","w") as f:
    json.dump(products,f,indent=2)

with open("users_subset.json","w") as f:
    json.dump(users,f,indent=2)

with open("transactions_subset.json","w") as f:
    json.dump(transactions,f,indent=2)

print("Dataset generated.")