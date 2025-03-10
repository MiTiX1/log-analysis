#!/bin/sh

curl -X POST -H "Content-Type: application/vnd.schemaregistry.v1+json" \
    --data '{"schema": "{\"type\":\"record\",\"name\":\"LogModel\",\"fields\":[{\"name\":\"id\",\"type\":\"string\"},{\"name\":\"timestamp\",\"type\":\"string\"},{\"name\":\"level\",\"type\":{\"type\":\"enum\",\"name\":\"LogLevel\",\"symbols\":[\"INFO\",\"DEBUG\",\"WARN\",\"ERROR\"]}},{\"name\":\"message\",\"type\":[\"null\",\"string\"],\"default\":null},{\"name\":\"source\",\"type\":[\"null\",\"string\"],\"default\":null}]}"}' \
    http://localhost:8081/subjects/logs-value/versions