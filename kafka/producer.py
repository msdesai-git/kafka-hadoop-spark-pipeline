from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

products = ['Phone', 'Laptop', 'Shoes', 'Book']
events = ['click', 'view', 'purchase']

while True:
    message = {
        'user_id': random.randint(100, 105),
        'product': random.choice(products),
        'event': random.choice(events),
        'timestamp': time.time()
    }
    producer.send('clickstream-topic', message)
    print("Sent:", message)
    time.sleep(1)
