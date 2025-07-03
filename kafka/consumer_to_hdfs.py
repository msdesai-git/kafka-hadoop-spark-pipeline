from kafka import KafkaConsumer
import json
import time
import subprocess

# Kafka consumer setup
consumer = KafkaConsumer(
    'clickstream-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Unique local file
ts = int(time.time())
local_file = f'clickstream_{ts}.json'

with open(local_file, 'w') as f:
    for i, msg in enumerate(consumer):
        json.dump(msg.value, f)
        f.write('\n')
        print("Consumed:", msg.value)

        # Flush every 10 messages to HDFS
        if (i + 1) % 10 == 0:
            f.flush()  # ✅ force write buffer to disk
            hdfs_path = f'/data/clickstream/raw/{local_file}'
            subprocess.run(["hdfs", "dfs", "-put", "-f", local_file, hdfs_path])
            print(f"✅ Written to HDFS: {hdfs_path}")

            # Optional: clear local file for next batch
            f.truncate(0)
            f.seek(0)
