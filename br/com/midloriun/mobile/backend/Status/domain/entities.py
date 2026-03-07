from dataclasses import dataclass, field
from uuid import uuid4

@dataclass
class StatusEntity():
    id: str | None = field(default_factory=uuid4)
    name: str | None = None