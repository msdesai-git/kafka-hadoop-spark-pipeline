#!/bin/bash

# Navigate to Hive folder
cd "$(dirname "$0")/hive"

# Run Hive CLI script
hive -f create_hive_table.hql
