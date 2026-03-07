from ...infra.repository import LabelRepository
from User.infra.repository import UserRepository
from ...domain.service.labelPolicy import validate_user_exists

class FindLabelUseCase():
    def __init__(self):
        self.labelRepository = LabelRepository()

    def execute(self, label_id: str, user_id: str):
        validate_user_exists(user_id, UserRepository())
        label_founded = self.labelRepository.find(label_id, user_id)
        return label_founded