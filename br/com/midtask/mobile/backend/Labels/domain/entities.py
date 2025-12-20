from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class LabelEntity():
    id: str | None
    title: str | None
    created_at:datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)