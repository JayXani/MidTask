from uuid import uuid4
from ...infra.repository import UserRepository
from ...Domain.entities import UserEntity


class CreateUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, data: dict) -> UserEntity:
        user = UserEntity(
            id=uuid4(),
            **data
        )

        return self.user_repository.save(user)
