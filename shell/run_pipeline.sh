#!/bin/bash

echo "Step 1: Running Kafka Producer..."
python3 ../kafka/producer.py &
sleep 3

echo "Step 2: Running Kafka Consumer to store data in HDFS..."
python3 ../kafka/consumer_to_hdfs.py
sleep 3

echo "Step 3: Cleaning data using PySpark..."
spark-submit ../spark/clean_clickstream.py
sleep 3

echo "Step 4: Querying Hive table using PySpark..."
spark-submit ../spark/query_hive_from_spark.py

echo "Pipeline execution complete!"
