from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Cleaning").getOrCreate()

df = spark.read.json("../sample_data/transactions_subset.json")

clean = df.filter(df.status == "completed")

clean.show()