from ...infra.repository import StatusRepository
from ...domain.entities import StatusEntity

class CreateStatusUseCase():
    def __init__(self):
        self.repository = StatusRepository()

    def execute(self, status: dict, user_id: str):
        status_entities = [
            StatusEntity(
                name=s
            ) for s in status.get("status", [])
        ]
        status_created = self.repository.create(status_entities, user_id)
        return status_created