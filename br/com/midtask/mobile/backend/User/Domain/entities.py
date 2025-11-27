
class Permission:
    id: str
    task_notification: bool
    calendar_home: bool
    task_email_notification: bool
    open_apps: bool

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
 
