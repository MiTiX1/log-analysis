#!/bin/sh

docker build -t log-generator:latest .

docker compose up -d

sleep 10

./scripts/kafka-setup.sh

sleep 10

./scripts/schema-registry-setup.sh