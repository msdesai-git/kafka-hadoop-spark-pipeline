#!/bin/bash

# Navigate to Spark job folder
cd "$(dirname "$0")/spark"

# Run Spark job to clean data
spark-submit clean_clickstream.py
