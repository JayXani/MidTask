from ...infra.repository import LabelRepository
from User.infra.repository import UserRepository
from ...domain.entities import LabelEntity
from ...domain.service.labelPolicy import policy_to_create
from uuid import uuid4

class CreateLabelUseCase():
    def __init__(self):
        self.labelRepository = LabelRepository()
        self.userRepository = UserRepository()

    def execute(self, labels: dict, user_id: str):
        entities = [LabelEntity(
            id=uuid4(),
            title=label
        ) for label in labels.get("labels", [])]
      
        policy_to_create(user_id, self.userRepository)
        labels_inserted = self.labelRepository.create(entities, user_id)
        return labels_inserted
