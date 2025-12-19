from ..Domain.entities import UserEntity
from ..models import User


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
    
    def find(self, user: UserEntity):
        users_founded = User.objects.get(use_id=user.id)

        return UserEntity(
            id=users_founded.use_id,
            name=users_founded.use_name,
            status=users_founded.use_status,
            email=users_founded.use_email,
            phone=users_founded.use_phone,
            login_type=users_founded.use_login_type,
            ip_address=users_founded.use_ip_address,
            created_at=users_founded.created_at,
            updated_at=users_founded.updated_at,
        )
    
    def update(self, user: UserEntity):
        data_to_update = {}
        data_to_update["updated_at"] = user.updated_at
        
        if user.email is not None:
            data_to_update["use_email"] = user.email

        if user.password is not None:
            data_to_update["password"] = user.password

        if user.name is not None:
            data_to_update["use_name"] = user.name

        if user.status is not None:
            data_to_update["use_status"] = user.status

        if user.phone is not None:
            data_to_update["use_phone"] = user.phone

        if user.ip_address is not None:
            data_to_update["use_ip_address"] = user.ip_address

        if not data_to_update:
            raise Exception("Data to update is not sended !")

        User.objects.filter(use_id=user.id).update(**data_to_update)

        # Busca o usuário atualizado
        user_db = User.objects.get(use_id=user.id)

        return UserEntity(
            id=user_db.use_id,
            name=user_db.use_name,
            status=user_db.use_status,
            email=user_db.use_email,
            phone=user_db.use_phone,
            login_type=user_db.use_login_type,
            ip_address=user_db.use_ip_address,
            created_at=user_db.created_at,
            updated_at=user_db.updated_at,
        )

