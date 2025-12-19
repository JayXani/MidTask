from ...infra.repository import UserRepository
from ...Domain.entities import UserEntity
from ...Domain.Services.UserPolicyService import UserPolicyService

class GetUserUseCase:
    def __init__(self):
        self.repository = UserRepository()
    
    def execute(self, id:str):
        user_entity = UserEntity()
        user_entity.id = id
        user_policy = UserPolicyService(self.repository)

        user_policy.validate_find(user_entity)
        user_founded = self.repository.find(user_entity)

        return user_founded