import os
import time

from confluent_kafka import Producer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroSerializer
from confluent_kafka.serialization import SerializationContext, MessageField

from models.log_model import LogModel


class KafkaProducer:
    conf = {
        "bootstrap.servers": os.environ.get("BOOTSTRAP_SERVER", "kafka:29092"),
    }

    schema_registry_url = os.environ.get("SCHEMA_REGISTRY_URL", "http://schema-registry:8081")

    def __init__(self, topic: str) -> None:
        self.topic = topic
        self._init_producer()
        self.schema_registry_client = SchemaRegistryClient({"url": KafkaProducer.schema_registry_url})
        self.avro_schema = self._get_latest_schema()
        self.avro_serializer = AvroSerializer(self.schema_registry_client, self.avro_schema)

    def _init_producer(self):
        retries = 10
        while retries > 0:
            try:
                self.producer = Producer(KafkaProducer.conf)
                return
            except:
                print(f"Connection failed. Retrying...")
                retries -= 1
                time.sleep(5)
        raise Exception("Failed to connect to Kafka after retries.")

    def _get_latest_schema(self) -> str:
        subject = f"{self.topic}-value"
        retries = 10
        while retries > 0:
            try:
                schema_metadata = self.schema_registry_client.get_latest_version(subject)
                return schema_metadata.schema.schema_str
            except:
                retries -= 1
                time.sleep(5)
        raise Exception("Could not get schema.")

    def send_log(self, key: str, value: LogModel) -> None:
        value["id"] = str(value.get("id", ""))
        value["timestamp"] = value.get("timestamp").isoformat()
        avro_value = self.avro_serializer(value, SerializationContext(self.topic, MessageField.VALUE))
        self.producer.produce(self.topic, key=key, value=avro_value)
        self.producer.flush()
