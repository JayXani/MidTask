from Domain.entities import UserEntity
from models import User, Permission

class UserRepository:
    def save(self, userDomain: UserEntity):
        permission = Permission.objects.create(
            per_app_task_notification = userDomain.permissions.task_notification,
            per_app_calendar_home =  userDomain.permissions.calendar_home,
            per_app_task_email_notification =  userDomain.permissions.task_email_notification,
            per_app_open_apps =  userDomain.permissions.open_apps,
        )

        user_created = User.objects.create(
            use_name = userDomain.name,
            use_status = userDomain.status,
            use_email = userDomain.email,
            use_password_hash =userDomain.password_hash,
            use_phone = userDomain.phone,
            use_login_type = userDomain.login_type,
            use_ip_address = userDomain.ip_address,
            created_at = userDomain.status,
            updated_at = userDomain.status,
        )

        user_created.permissions.add(permission)

        return user_created