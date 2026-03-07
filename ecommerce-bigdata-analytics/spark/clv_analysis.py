from pyspark.sql import SparkSession
from pyspark.sql.functions import sum,count

spark = SparkSession.builder.appName("CLV").getOrCreate()

df = spark.read.json("../sample_data/transactions_subset.json")

clv = df.groupBy("user_id").agg(
    sum("total_amount").alias("total_spent"),
    count("*").alias("purchase_count")
)

clv.show()