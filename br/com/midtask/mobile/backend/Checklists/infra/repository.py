from ..domain.entities import ChecklistEntity
from ..models import CheckLists
from User.models import User
from Task.models import Task
from django.db.models import Q


class ChecklistRepository:
    dict_keys = {
        "che_name": "",
        "che_status": "",
        "che_date": "",
        "che_description": "",
        "fk_che_tsk_id": "",
    }

    def create(self, checklist: ChecklistEntity, user_id: str):
        checklist_created = CheckLists.objects.create(
            che_id=checklist.id,
            che_name=checklist.name,
            che_status=checklist.status,
            che_date=checklist.date,
            che_description=checklist.description,
            fk_che_use_id=User.objects.get(use_id=user_id),
            fk_che_tsk_id=Task.objects.get(tsk_id=checklist.task_id)
        )

        return [
            ChecklistEntity(
                id=checklist_created.che_id,
                name=checklist_created.che_name,
                status=checklist_created.che_status,
                date=checklist_created.che_date,
                description=checklist_created.che_description
            )
        ]

    def delete(self, checklists: list[ChecklistEntity], user_id: str):
        checklists_deleted = CheckLists.objects.filter(
            che_id__in=[v.id for v in checklists], fk_che_use_id=user_id
        )

        return checklists_deleted

    def findall(self, checklists: list[ChecklistEntity], user_id: str):
        query = Q()

        for check in checklists:
            if check.id:
                query |= Q(che_id=check.id)
            if check.date:
                query |= Q(che_date=check.date)
            if check.name:
                query |= Q(che_name=check.name)
            if check.status:
                query |= Q(che_status=check.status)
            if check.task_id:
                query |= Q(fk_che_tsk_id=check.task_id)
            if check.description:
                query |= Q(che_description__contains=check.description)

        checklists_founded = CheckLists.objects.filter(query, fk_che_use_id=user_id)

        return [
            ChecklistEntity(
                id=che.che_id,
                name=che.che_name,
                status=che.che_status,
                date=che.che_date,
                description=che.che_description,
                task_id=che.fk_che_tsk_id,
            )
            for che in checklists_founded
        ]

    def update(self, checklists: ChecklistEntity, user_id: str):
        if checklists.date:
            self.dict_keys["che_date"] = checklists.date
        if checklists.name:
            self.dict_keys["che_name"] = checklists.name
        if checklists.status:
            self.dict_keys["che_status"] = checklists.status
        if checklists.task_id:
            self.dict_keys["fk_che_tsk_id"] = checklists.task_id
        if checklists.description:
            self.dict_keys["che_description"] = checklists.description

        checklists_updated = CheckLists.objects.filter(
            che_id=checklists.id, fk_che_use_id=user_id
        ).update(**self.dict_keys)

        return checklists_updated
