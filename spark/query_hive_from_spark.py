from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Query Hive") \
    .enableHiveSupport() \
    .getOrCreate()

df = spark.sql("SELECT product, COUNT(*) as total FROM clickstream_clean GROUP BY product")
df.show()

spark.stop()
