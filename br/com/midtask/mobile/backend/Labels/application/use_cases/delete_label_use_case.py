from User.infra.repository import UserRepository
from ...infra.repository import LabelRepository
from ...domain.service.labelPolicy import validate_user_exists
from ...domain.entities import LabelEntity

class DeleteLabelUseCase():
    def __init__(self):
        self.repository = LabelRepository()

    def execute(self, labels: dict, user_id: str):
        labels_entities = [LabelEntity(
            id=v
        ) for v in labels.get("labels",  [])]
        
        labels_deleted = self.repository.delete(labels_entities, user_id)
        return labels_deleted[0]