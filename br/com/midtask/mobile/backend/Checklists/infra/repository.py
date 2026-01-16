from ..domain.entities import ChecklistEntity
from ..models import CheckLists

class ChecklistRepository():
    def create(self, checklist: ChecklistEntity, user_id: str):
        checklist_created = CheckLists.objects.create(
            che_id=checklist.id,
            che_name=checklist.name,
            che_status=checklist.status,
            che_date=checklist.date,
            fk_che_tsk_id_id=checklist.task_id,
            fk_che_use_id=user_id
        )

        return [
            ChecklistEntity(
                id=checklist_created.che_id,
                name=checklist_created.che_name,
                status=checklist_created.che_status,
                date=checklist_created.che_date,
            )
        ]
    
    def delete(self, checklists: list[ChecklistEntity], user_id: str):
        print()
