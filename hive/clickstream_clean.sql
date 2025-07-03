CREATE EXTERNAL TABLE IF NOT EXISTS clickstream_clean (
    user_id INT,
    product STRING,
    event STRING,
    timestamp DOUBLE
)
STORED AS PARQUET
LOCATION 'hdfs://localhost:9000/data/clickstream/clean/';
