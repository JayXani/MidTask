from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class PermissionEntity:
    id: str
    task_notification: bool
    calendar_home: bool
    task_email_notification: bool
    open_apps: bool

@dataclass # Isso é um decorador que diminui minhas linhas de código implementando métodos etc que eu precisaria implementar na mao, ex: __init__
class UserEntity:
    id: str
    name: str
    status: str
    email: str
    phone: str
    login_type: str
    ip_address: str
    created_at:datetime = datetime.now() # A tipagem é importante
    updated_at:datetime = datetime.now()
    permissions: list = field(default_factory=list) # Precisamos adicionar default_factory para que ele permita retornar uma lista
    password_hash: str = ""
 
