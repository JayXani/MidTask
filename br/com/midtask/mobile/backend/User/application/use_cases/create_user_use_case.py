from ...infra.repository import UserRepository
from ...Domain.entities import UserEntity
from uuid import uuid4

class CreateUserUseCase:
    def __init__(self,  user_repository: UserRepository):
        self.user_repository = user_repository
        self.user_domain = None

    def execute(self, data: dict): # Os dados já sao recebidos tratados pel
        
        self.user_domain = UserEntity(
            id=uuid4(),
            **data
        )
        user_saved = self.user_repository.save(self.user_domain)
        
        return user_saved