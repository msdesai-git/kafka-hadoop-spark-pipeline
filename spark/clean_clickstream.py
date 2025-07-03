from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_unixtime

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Clickstream Cleaner") \
    .getOrCreate()

# Input path: raw JSON files
input_path = "hdfs://localhost:9000/data/clickstream/raw/"
output_path = "hdfs://localhost:9000/data/clickstream/clean/"

# Read JSON from HDFS
df_raw = spark.read.json(input_path)

# Basic data cleaning
df_clean = df_raw.select(
    col("user_id").cast("int"),
    col("product").cast("string"),
    col("event").cast("string"),
    from_unixtime(col("timestamp")).alias("event_time")
)

# Show sample data
df_clean.show(5, truncate=False)

# Write to HDFS as Parquet
df_clean.write.mode("overwrite").parquet(output_path)

print("✅ Cleaned data written to:", output_path)

# Stop session
spark.stop()
