from ...infra.repository import ChecklistRepository
from ...domain.entities import ChecklistEntity
from ...domain.service.ChecklistPolicyService import CheckListPolicyService

class CreateChecklistsUseCase():
    def __init__(self):
        self.repository = ChecklistRepository()

    def execute(self, checklist: dict, user_id: str):
        checklist_entity = ChecklistEntity(**checklist)
        checklist_policy = CheckListPolicyService(checklist_entity)
        checklist_policy.validate_to_create()
        checklist_created = self.repository.create(checklist_entity, user_id)

        if(not checklist_created): raise Exception("Cannot be created the checklist")

        return checklist_created