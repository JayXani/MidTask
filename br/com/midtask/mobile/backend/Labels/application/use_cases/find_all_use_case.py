from ...infra.repository import LabelRepository
from User.infra.repository import UserRepository
from ...domain.service.labelPolicy import validate_user_exists
from ...domain.entities import LabelEntity

class FindAllLabelsUseCase():
    def __init__(self):
        self.repository = LabelRepository()

    def execute(self, labels: dict, user_id: str):
        validate_user_exists(user_id, UserRepository())

        labels_entities: list[LabelEntity] = []
        if(labels.get("id", [])):
            labels_entities.extend([LabelEntity(id=v) for v in labels.get("id")])

        if(labels.get("name", [])):
            labels_entities.extend([LabelEntity(title=v) for v in labels.get("name")])

        labels_founded = self.repository.find_all(labels_entities, user_id)
        return labels_founded