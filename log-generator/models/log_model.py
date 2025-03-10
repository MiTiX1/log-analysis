import uuid

from datetime import datetime
from typing import Any, Literal, Optional, TypedDict

type LogLevel = Literal["INFO", "DEBUG", "WARN", "ERROR"]


class LogModel(TypedDict):
    id: uuid.UUID
    timestamp: datetime
    level: LogLevel
    message: Any
    source: Optional[str]
