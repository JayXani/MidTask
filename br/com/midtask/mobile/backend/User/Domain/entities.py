from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class PermissionEntity:
    id: str
    task_notification: bool
    calendar_home: bool
    task_email_notification: bool
    open_apps: bool


@dataclass
class UserEntity:
    id: str # Precisamos da tipagem
    name: str
    status: str
    email: str
    phone: str | None
    login_type: str
    ip_address: str
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    permissions: list[PermissionEntity] = field(default_factory=list)

    password: str = ""  # senha EM TEXTO (hash é infra)
