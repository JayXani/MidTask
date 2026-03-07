from ...infra.repository import ChecklistRepository
from ...domain.validators.checklists_validator import normalize_payload

class FindAllChecklistsUseCase():
    def __init__(self):
        self.repository = ChecklistRepository()

    def execute(self, checklists: dict, user_id: str):
        print(checklists)
        checklists_normalized = normalize_payload(checklists)
        checklists_founded = self.repository.findall(checklists_normalized, user_id)

        if(not checklists_founded): return []
        
        return checklists_founded