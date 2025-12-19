from ..entities import UserEntity
from ...infra.repository import UserRepository
from ...models import User

# Na service deve ir as regras de negocio que exigem de banco, digamos que a service é minha Facade de validacoes
class UserPolicyService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def validate_creation():
        print() # Aqui deve ser as validacoes para criar o usuário

    def validate_update(self, user_entity: UserEntity):
        user_exists = User.objects.filter(use_id=user_entity.id)
        if(not user_exists): raise Exception("User not exists")

    def validate_find(self, user_entity: UserEntity):
        if(not user_entity.id): raise Exception("The id is required !")