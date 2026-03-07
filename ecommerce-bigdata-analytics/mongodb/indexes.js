use ecommerce

db.products.createIndex({"category.category_id":1})
db.products.createIndex({"creation_date":1})

db.users.createIndex({"registration_date":1})

db.transactions.createIndex({"user_id":1})
db.transactions.createIndex({"timestamp":1})
db.transactions.createIndex({"user_id":1,"timestamp":1})