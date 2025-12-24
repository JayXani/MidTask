from dataclasses import field, dataclass
from uuid import uuid4

@dataclass
class LinksEntity():
    id: str | None = field(default_factory=uuid4)
    name: str | None = None
    link_reference: str | None = None
    link_type: str | None = None
    icon: str | None = None