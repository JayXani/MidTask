from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class UserEntity:
    id: str | None = None # Precisamos da tipagem
    name: str | None = None
    status: str | None = None
    email: str | None = None
    phone: str | None = None
    login_type: str | None = None
    ip_address: str | None = None
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    password: str = ""  # senha EM TEXTO (hash é infra)
