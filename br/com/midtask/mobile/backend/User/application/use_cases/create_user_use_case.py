from infra.repository import UserRepository

class CreateUserUseCase:
    def __init__(self,  user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, data):
        
        print() # Serializa os dados aqui e envia para a repository !