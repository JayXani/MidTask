from ...infra.repository import ChecklistRepository
from ...domain.entities import ChecklistEntity
from ...domain.service.ChecklistPolicyService import CheckListPolicyService

class UpdateChecklistUseCase():
    def __init__(self):
        self.repository = ChecklistRepository()

    def execute(self, checklist: dict, checklist_id: str, user_id: str):
        checklist_entity = ChecklistEntity(
            id=checklist_id,
            **checklist
        )
        checklist_policy = CheckListPolicyService(checklist_entity)
        checklist_policy.validate_to_create()
    
        checklist_updated = self.repository.update(checklist_entity, user_id)
        return checklist_updated