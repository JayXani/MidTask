from ...infra.repository import ChecklistRepository
from ...domain.entities import ChecklistEntity

class DeleteChecklistUseCase():
    def __init__(self):
        self.repository = ChecklistRepository()

    def execute(self, checklist: str, user_id: str):
        checklist_entity = [ChecklistEntity(id=che_id) for che_id in checklist.get("id", [])]
        checklist_deleted = self.repository.delete(checklist_entity, user_id)
        return checklist_deleted