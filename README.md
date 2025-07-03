# 🚀 Kafka + Hadoop + Spark Hybrid Data Pipeline (Clickstream Analytics)

A hybrid batch + streaming pipeline that processes simulated clickstream events using Apache Kafka, stores raw data in HDFS, performs cleaning and transformation with PySpark, and runs analytics queries on Hive.

---

## 📌 Project Highlights

- 🔄 Designed a **hybrid data pipeline** combining real-time streaming (Kafka) with hourly batch processing (HDFS + Spark).
- 🎯 Simulated **1M+ clickstream events** over 3 Kafka topics for web events, user behavior, and transactions.
- 🧹 Cleaned raw JSON files using PySpark, extracting key metrics like session paths, drop-offs, and product trends.
- 📁 Stored both raw and cleaned data in HDFS (JSON and Parquet format respectively).
- 🔍 Created a Hive external table on top of cleaned Parquet files for querying with SparkSQL.
- 🕒 Automated the ingestion-cleaning-query cycle using Unix shell scripts, supporting reproducibility.

---

## 🧱 Tech Stack

| Component  | Technology Used |
|------------|-----------------|
| Messaging  | Apache Kafka    |
| Storage    | HDFS (Hadoop)   |
| Processing | Apache Spark    |
| Querying   | Hive            |
| Language   | Python (PySpark)|
| OS         | WSL2 + Ubuntu   |

---

## 📂 Project Structure

```
kafka-hadoop-spark-pipeline/
│
├── kafka/
│   ├── producer.py                # Sends simulated events to Kafka
│   └── consumer_to_hdfs.py       # Consumes Kafka stream & stores raw JSON in HDFS
│
├── spark/
│   ├── clean_clickstream.py      # Reads raw JSON from HDFS and writes cleaned Parquet
│   └── query_hive_from_spark.py  # Connects to Hive and runs Spark SQL queries
│
├── hive/
│   └── hive_commands.sql         # Hive DDL for creating external table on cleaned data
│
└── shell/
    ├── start_kafka.sh            # Starts Kafka + Zookeeper services
    ├── run_pipeline.sh           # One-click runner for ingestion + processing
    ├── run_spark_job.sh          # Runs Spark job for cleaning and querying clickstream data
    └── run_hive_script.sh        # Runs predefined Hive commands to create external tables
```

---

## 🧪 Sample Flow

1. **Producer** sends clickstream JSONs to Kafka topics (`clickstream_raw`, `user_events`, `transactions`).
2. **Consumer** pulls messages and stores in HDFS `/data/clickstream/raw/` as `clickstream_*.json`.
3. **PySpark** job reads raw files → cleans and flattens → writes Parquet to `/data/clickstream/clean/`.
4. **Hive** table (`clickstream_clean`) reads Parquet files via external table.
5. **Spark SQL** job runs queries on top of Hive table and prints insights.

---

## 📊 Sample Output (from Spark SQL)

```
+-----------------+-------+
| product         | total |
+-----------------+-------+
| Mobile          | 19345 |
| Electronics     | 18674 |
| Groceries       | 21012 |
| Fashion         | 18241 |
+-----------------+-------+
```

---

## 🧠 Key Learnings

- Setting up a full local pipeline with Kafka, HDFS, Spark & Hive from scratch on WSL2
- Managing schema-on-read with Hive external tables
- Handling real-time Kafka stream ingestion + batch cleanup in PySpark
- Structuring re-usable data pipelines with Python and shell scripts

---

## ✅ How to Run

1. Start Kafka & HDFS:
   ```bash
   ./shell/start_kafka.sh
   ```

2. Run pipeline:
   ```bash
   ./shell/run_pipeline.sh
   ```

---

## 🔗 Connect

Want to collaborate or discuss more projects?  
Reach me at [LinkedIn](https://linkedin.com/in/mitesh-s-desai)