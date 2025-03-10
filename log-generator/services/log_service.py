import json
import random
import uuid

from datetime import datetime

from models.log_model import LogLevel, LogModel


class LogService:
    log_levels_prob = (
        ("INFO", "DEBUG", "WARN", "ERROR"),
        (0.4, 0.3, 0.2, 0.1)
    )

    sources = ["auth-service", "payment-service", "notification-service",
               "analytics-service", "user-service", None]

    message_by_level = {
        "INFO": [
            "User successfully logged in",
            "User successfully logged out",
            "Scheduled task executed successfully",
            "Cache refreshed successfully",
            "System health check passed"
        ],
        "DEBUG": [
            "Fetching user details from database",
            "Processing request with correlation ID 12345",
            "Cache miss for key user_567",
            "Retrying connection to payment service",
            "Parsing configuration file: config.yaml"
        ],
        "WARN": [
            "High memory usage detected",
            "Database connection pool running low",
            "Failed login attempt detected",
            "Slow response from external API",
            "Retry limit reached for background job"
        ],
        "ERROR": [
            "Null pointer exception in payment processor",
            "Database connection timeout",
            "Failed to load configuration file",
            "Unhandled exception in request handler",
            "User session invalid, forcing logout"
        ]
    }

    def __init__(self) -> None:
        pass

    def _get_random_level(self) -> str:
        return random.choices(
            population=LogService.log_levels_prob[0],
            weights=LogService.log_levels_prob[1],
            k=1
        )[0]

    def _get_random_source(self) -> str | None:
        return random.choice(LogService.sources)

    def _get_random_message(self, level: LogLevel) -> str:
        return random.choice(LogService.message_by_level.get(level, [""]))

    def generate_random_log(self) -> LogModel:
        level = self._get_random_level()
        return {
            "id": uuid.uuid4(),
            "timestamp": datetime.now(),
            "level": level,
            "message": self._get_random_message(level),
            "source": self._get_random_source()
        }

    def generate_random_logs(self, n: int) -> list[LogModel]:
        return [self.generate_random_log() for _ in range(0, n)]

    def stringify(self, log: LogModel) -> str:
        log["id"] = str(log.get("id"))
        log["timestamp"] = log.get("timestamp").isoformat()
        return json.dumps(log)
