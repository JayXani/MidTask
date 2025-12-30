from dataclasses import dataclass, field
from uuid import uuid4
from datetime import datetime

@dataclass
class AlertEntity():
    id: str | None = field(default_factory=uuid4)
    date: datetime | None = None
    repeat: str | None = None