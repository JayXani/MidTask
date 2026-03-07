from dataclasses import dataclass, field
from uuid import uuid4, UUID
from datetime import datetime
@dataclass
class ChecklistEntity:
    id:UUID | None = field(default_factory=uuid4)
    name: str | None = None
    status: str | None = None
    date: datetime | None = None
    description: str | None = None
    task_id: UUID | None | list = None