from dataclasses import dataclass
class Permission:
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
    password_hash: str
    phone: str
    login_type: str
    ip_address: str
    permissions: Permission
 
