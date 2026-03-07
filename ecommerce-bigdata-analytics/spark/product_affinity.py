from pyspark.sql import SparkSession
from pyspark.sql.functions import explode

spark = SparkSession.builder.appName("Affinity").getOrCreate()

df = spark.read.json("../sample_data/transactions_subset.json")

items = df.select("transaction_id", explode("items").alias("item"))

pairs = items.alias("a").join(
    items.alias("b"),
    "transaction_id"
).filter("a.item.product_id < b.item.product_id")

pairs.groupBy(
    "a.item.product_id",
    "b.item.product_id"
).count().show()