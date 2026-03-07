# E-Commerce Big Data Analytics

Technologies:
- MongoDB
- HBase
- Apache Spark
- Python

## Steps to Reproduce

1 Generate Dataset
python data_generator/generate_dataset.py

2 Load MongoDB
python mongodb/load_mongodb.py

3 Create Indexes
run mongodb/indexes.js in mongosh

4 Run Aggregations
run mongodb/aggregations.js

5 Start HBase (Docker)
docker run -d -p 16010:16010 harisekhon/hbase

6 Run Spark Jobs
spark-submit spark/product_affinity.py

7 Generate Visualizations
python visualization/charts.py