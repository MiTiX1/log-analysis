from dotenv import load_dotenv
load_dotenv()  # nopep8

import os
import random
import time

from services.log_service import LogService
from services.kafka_service import KafkaProducer


def main():
    log_service = LogService()
    kafka_service = KafkaProducer("logs")

    end = time.time() + int(os.environ.get("DURATION", 30))
    while time.time() < end:
        logs = log_service.generate_random_logs(random.randint(1, 10))
        for log in logs:
            kafka_service.send_log(str(log.get("id")), log)
        time.sleep(1)


if __name__ == "__main__":
    main()
