from ..domain.entities import TaskEntity
from ..models import Task
from Status.models import Status
from User.models import User
from Alerts.models import Alerts
from Labels.models import Labels
from LinksAssociates.models import LinksAssociates

class TaskRepository():

    def create(self, task_entity: TaskEntity, user_id: str):
        task_created = Task.objects.create(
            tsk_id=task_entity.id,
            tsk_title=task_entity.title,
            tsk_description=task_entity.description,
            tsk_recurrence=task_entity.recurrence,
            tsk_recurrence_end_in=task_entity.recurrence_end_in,
            tsk_conclude_expected_at=task_entity.expected_conclude_in,
            tsk_conclude_at=task_entity.conclude_at,
            tsk_background=task_entity.background,
            fk_tsk_sta_id=Status.objects.get(sta_id=task_entity.status_id),
            fk_tsk_use_id = User.objects.get(use_id=user_id),
            created_at=task_entity.created_at,
            updated_at=task_entity.updated_at,
        )

        if task_entity.alert_id:
            task_created.fk_tsk_ale_id.add(Alerts.objects.filter(
                ale_id__in=[v for v in task_entity.alert_id]
            ))

        if task_entity.labels_id:
            task_created.fk_tsk_lab_id.add(Labels.objects.filter(
                lab_id__in=[v for v in task_entity.labels_id]
            ))

        if task_entity.links_id:
            task_created.fk_tsk_asc_id.add(LinksAssociates.objects.filter(
                lab_id__in=[v for v in task_entity.links_id]
            ))
        
        return [
            TaskEntity(
                id=task_created.tsk_id,
                title = task_created.tsk_title,
                description = task_created.tsk_description,
                recurrence = task_created.tsk_recurrence,
                recurrence_end_in = task_created.tsk_recurrence_end_in,
                expected_conclude_in = task_created.tsk_conclude_expected_at,
                conclude_at = task_created.tsk_conclude_at,
                background = task_created.tsk_background,
                status_id = task_created.fk_tsk_sta_id,
                created_at =task_created.created_at,
                updated_at =task_created.updated_at
            )
        ]
            
        