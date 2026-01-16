from dataclasses import dataclass, field #dataclasses sao usado para boilerplate (evitar código repetivo)
from uuid import UUID, uuid4
from datetime import datetime

@dataclass
class TaskEntity():
    id: UUID | None = field(default_factory=uuid4)
    title: str | None = None
    description: str | None = None
    recurrence: datetime | None = None
    recurrence_end_in: datetime | None = None
    expected_conclude_in: datetime | None = None
    conclude_at: datetime | None = None
    background: str | None = None
    status: list[str] | None = None
    alerts: list[str] | None = None
    labels: list[str] | None = None
    links: list[str] | None = None
    created_at: datetime | None = field(default_factory=datetime.now)
    updated_at: datetime | None = field(default_factory=datetime.now)
