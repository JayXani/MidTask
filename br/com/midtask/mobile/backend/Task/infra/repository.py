from ..domain.entities import TaskEntity
from ..models import Task
from Status.models import Status
from User.models import User
from Alerts.models import Alerts
from Labels.models import Labels
from LinksAssociates.models import LinksAssociates
from django.db.models import Q

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
            fk_tsk_sta_id=Status.objects.get(sta_id=task_entity.status_id[0]),
            fk_tsk_use_id = User.objects.get(use_id=user_id),
            created_at=task_entity.created_at,
            updated_at=task_entity.updated_at,
        )

        if task_entity.alert_id:
            task_created.fk_tsk_ale_id.add(
                *Alerts.objects.filter(
                    ale_id__in=task_entity.alert_id
                )
            )

        if task_entity.labels_id:
            task_created.fk_tsk_lab_id.add(
                *Labels.objects.filter(
                    lab_id__in=task_entity.labels_id
                )
            )

        if task_entity.links_id:
            task_created.fk_tsk_asc_id.add(
                *LinksAssociates.objects.filter(
                    asc_id__in=task_entity.links_id
                )
            )

        
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
    
    def findall(self, task_entities: list[TaskEntity], user_id: str):
        query = Q()

        for task in task_entities:
            if task.id: query |= Q(tsk_id=task.id)
            if task.title: query = Q(tsk_title__contains=task.title or "")
            if task.background: query = Q(tsk_background__contains=task.background or "")
            if task.recurrence: query = Q(tsk_recurrence=task.recurrence)
            if task.recurrence_end_in: query = Q(tsk_recurrence_end_in=task.recurrence_end_in)
            if task.expected_conclude_in: query = Q(tsk_conclude_expected_at=task.expected_conclude_in)
            if task.conclude_at: query = Q(tsk_conclude_at=task.conclude_at)

        task_founded = Task.objects.filter(
            query,
            fk_tsk_use_id=user_id
        )
        
        return [
            TaskEntity(
                id=tsk.tsk_id,
                title = tsk.tsk_title,
                description = tsk.tsk_description,
                recurrence = tsk.tsk_recurrence,
                recurrence_end_in = tsk.tsk_recurrence_end_in,
                expected_conclude_in = tsk.tsk_conclude_expected_at,
                conclude_at = tsk.tsk_conclude_at,
                background = tsk.tsk_background,
                status_id = tsk.fk_tsk_sta_id,
                created_at =tsk.created_at,
                updated_at =tsk.updated_at
            ) for tsk in task_founded
        ]