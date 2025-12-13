from ..Domain.entities import UserEntity
from User.models import User


class UserRepository:
    def save(self, user: UserEntity) -> UserEntity:
        user_created = User.objects.create_user(
            email=user.email,
            password=user.password,
            use_id=user.id,
            use_name=user.name,
            use_status=user.status.value,
            use_phone=user.phone,
            use_login_type=user.login_type,
            use_ip_address=user.ip_address,
        )
        return UserEntity(
            id=user_created.use_id,
            name=user_created.use_name,
            status=user_created.use_status,
            email=user_created.use_email,
            phone=user_created.use_phone,
            login_type=user_created.use_login_type,
            ip_address=user_created.use_ip_address,
            created_at=user_created.created_at,
            updated_at=user_created.updated_at,
        )
    
    def find_all(self, user: UserEntity = None):
        users_founded = User.objects.all()
        users_domain = []
        for user in users_founded:
            users_domain.append(UserEntity(
                id=user.use_id,
                name=user.use_name,
                status=user.use_status,
                email=user.use_email,
                phone=user.use_phone,
                login_type=user.use_login_type,
                ip_address=user.use_ip_address,
                created_at=user.created_at,
                updated_at=user.updated_at,
            ))
            
        return users_domain