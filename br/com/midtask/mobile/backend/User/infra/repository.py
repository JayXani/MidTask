from ..Domain.entities import UserEntity
from .models import User

class UserRepository:
    def save(self, userDomain: UserEntity):
        user_created = User.objects.create(
            use_id = userDomain.id,
            use_name = userDomain.name,
            use_status = userDomain.status.value,
            use_email = userDomain.email,
            use_password_hash =userDomain.password_hash,
            use_phone = userDomain.phone,
            use_login_type = userDomain.login_type,
            use_ip_address = userDomain.ip_address
        )

        return UserEntity(
            id=user_created.use_id,
            name=user_created.use_name,
            status=user_created.use_status,
            email=user_created.use_email,
            phone=user_created.use_phone,
            login_type=user_created.use_login_type,
            ip_address=user_created.use_ip_address,
            password_hash=user_created.use_password_hash,
            created_at=user_created.created_at,
            updated_at=user_created.updated_at
        )