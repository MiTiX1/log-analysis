#!/bin/sh

# while ! nc -z kafka 9092; do
#     echo "Waiting for Kafka to be ready..."
#     sleep 2
# done

BOOTSTRAP_SERVER="localhost:9092"
REPLICATION_FACTOR=1
PARTITIONS=1
TOPIC="logs"

docker exec -it kafka kafka-topics --create --if-not-exists \
    --bootstrap-server $BOOTSTRAP_SERVER \
    --replication-factor $REPLICATION_FACTOR \
    --partitions $PARTITIONS \
    --topic $TOPIC