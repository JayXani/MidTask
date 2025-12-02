from ...infra.repository import UserRepository
from ...Domain.entities import UserEntity

class CreateUserUseCase:
    def __init__(self,  user_repository: UserRepository):
        self.user_repository = user_repository
        self.user_domain = None

    def execute(self, data): # Os dados já sao recebidos tratados pel
        self.user_domain = UserEntity()
        