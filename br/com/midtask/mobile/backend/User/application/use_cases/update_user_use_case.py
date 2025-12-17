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
        return user_updated