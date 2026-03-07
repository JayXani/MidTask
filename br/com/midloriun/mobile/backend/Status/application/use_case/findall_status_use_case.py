from ...infra.repository import StatusRepository
from ...domain.entities import StatusEntity
from ...domain.service.StatusPolicy import normalize_status

class FindAllStatusUseCase():
    def __init__(self):
        self.repository = StatusRepository()

    def execute(self, status: dict, user_id: str):
        status_normalized = normalize_status(status.get("status", {}))
        status_entities = [StatusEntity(**v) for v in status_normalized]
    
        status_founded = self.repository.findall(status_entities, user_id)

        if(not len(status_founded)): return []

        return status_founded