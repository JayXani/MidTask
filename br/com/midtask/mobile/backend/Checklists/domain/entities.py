from dataclasses import dataclass, field
from uuid import uuid4, UUID

class ChecklistEntity:
    id:UUID | None = field(default_factory=uuid4)
    name: str | None = None
    status: str | None = None
    date: str | None = None
    task_id: UUID | None = None