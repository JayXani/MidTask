from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class LabelEntity():
    id: str | None = None
    title: str | None = None
    created_at:datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)