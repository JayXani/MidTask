from ...infra.repository import LabelRepository
from User.infra.repository import UserRepository
from ..entities import LabelEntity
from User.Domain.entities import UserEntity

def validate_user_exists(user_id: str, user_repository: UserRepository, ):
    user_exists = user_repository.find(
        UserEntity(
            id=user_id
        )
    )
    if(not user_exists): raise Exception("User not exists !")

def policy_to_create(
    user_id: str,
    user_repository: UserRepository, 
):
    validate_user_exists(user_id, user_repository)