#!/bin/bash

echo "Starting Zookeeper..."
~/bigdata/kafka/bin/zookeeper-server-start.sh -daemon ~/bigdata/kafka/config/zookeeper.properties
sleep 5

echo "Starting Kafka Broker..."
~/bigdata/kafka/bin/kafka-server-start.sh -daemon ~/bigdata/kafka/config/server.properties
sleep 5

echo "Kafka and Zookeeper are running!"
