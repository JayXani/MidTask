from ...infra.repository import UserRepository
from ...Domain.entities import UserEntity
from ...Domain.Services.UserPolicyService import UserPolicyService

class UpdateUserUseCase():
    def __init__(self):
        self.repository = UserRepository()

    def execute(self, dataUser: dict, id: str): # Recebe os dados em formato dict (Serializados)
        user_entity = UserEntity(
            **dataUser
        )
        user_entity.id = id
        user_policy = UserPolicyService(self.repository)
        user_policy.validate_update(user_entity)

        user_updated = self.repository.update(user_entity)
        user_entity = UserEntity(
            id=user_updated.use_id,
            name=user_updated.use_name,
            status=user_updated.use_status,
            email=user_updated.use_email,
            phone=user_updated.use_phone,
            login_type=user_updated.use_login_type,
            ip_address=user_updated.use_ip_address,
            created_at=user_updated.created_at,
            updated_at=user_updated.updated_at,
        )
        return user_updated