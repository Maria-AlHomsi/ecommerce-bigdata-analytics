from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SQL").getOrCreate()

df = spark.read.json("../sample_data/transactions_subset.json")

df.createOrReplaceTempView("transactions")

result = spark.sql("""
SELECT
month(timestamp) as month,
sum(total_amount) as revenue
FROM transactions
GROUP BY month
ORDER BY month
""")

result.show()