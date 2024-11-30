#!/bin/bash

# Exit on any error
set -e

# Step 1: Substitute env variables in the SQL script
# echo "Substituting environment variables in SQL script..."
# envsubst < ./sql/init_template.sql > ./sql/init_script.sql

# docker-compose up preprosseor
docker-compose up preprocessor

# Step 2: Initialize the database
echo "Initializing MySQL database..."
docker-compose up mysql
