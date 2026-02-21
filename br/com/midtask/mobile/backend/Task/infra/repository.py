from ..domain.entities import TaskEntity
from ..models import Task
from Status.models import Status
from Status.domain.entities import StatusEntity
from User.models import User
from Alerts.models import Alerts
from Alerts.domain.entities import AlertEntity
from Labels.models import Labels
from LinksAssociates.models import LinksAssociates
from django.db.models import Q, Case, When, F, DateTimeField
from datetime import timedelta
from dateutil.relativedelta import relativedelta

class TaskRepository():
    dict_keys = {}

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
            fk_tsk_sta_id=Status.objects.get(sta_id=task_entity.status[0]),
            fk_tsk_use_id = User.objects.get(use_id=user_id),
            created_at=task_entity.created_at,
            updated_at=task_entity.updated_at,
        )

        if task_entity.alerts:
            task_created.fk_tsk_ale_id.add(
                *Alerts.objects.filter(
                    ale_id__in=task_entity.alerts
                )
            )

        if task_entity.labels:
            task_created.fk_tsk_lab_id.add(
                *Labels.objects.filter(
                    lab_id__in=task_entity.labels
                )
            )

        if task_entity.links:
            task_created.fk_tsk_asc_id.add(
                *LinksAssociates.objects.filter(
                    asc_id__in=task_entity.links
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
                status = task_created.fk_tsk_sta_id,
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
                status = [StatusEntity(
                    id=tsk.fk_tsk_sta_id.sta_id,
                    name=tsk.fk_tsk_sta_id.sta_name
                )],
                alerts= [AlertEntity(
                    id=x.ale_id,
                    date=x.ale_date,
                    repeat=x.ale_repeat
                ) for x in tsk.fk_tsk_ale_id.all()],
                created_at =tsk.created_at,
                updated_at =tsk.updated_at
            ) for tsk in task_founded
        ]
    
    def delete(self, task_entities: list[TaskEntity], user_id: str):
        tasks_deleted = Task.objects.filter(
            tsk_id__in=[task.id for task in task_entities],
            fk_tsk_use_id=user_id
        ).delete()

        return tasks_deleted
    
    def update(self, task_entity: TaskEntity, user_id: str):
        task_founded = Task.objects.get(tsk_id=task_entity.id)
        if task_entity.background: self.dict_keys["tsk_background"] = task_entity.background 
        if task_entity.title: self.dict_keys["tsk_title"] = task_entity.title 
        if task_entity.expected_conclude_in: self.dict_keys["tsk_conclude_expected_at"] = task_entity.expected_conclude_in
        if task_entity.conclude_at: self.dict_keys["tsk_conclude_at"] = task_entity.conclude_at
        if task_entity.description: self.dict_keys["tsk_description"] = task_entity.description
        if task_entity.recurrence: self.dict_keys["tsk_recurrence"] = task_entity.recurrence
        if task_entity.recurrence_end_in: self.dict_keys["tsk_recurrence_end_in"] = task_entity.recurrence_end_in
        if task_entity.updated_at: self.dict_keys["updated_at"] = task_entity.updated_at
        if len(task_entity.status): self.dict_keys["fk_tsk_sta_id"] = str(task_entity.status[0])
        self.dict_keys["updated_at"] = task_entity.updated_at

        if(isinstance(task_entity.alerts, list)):
            self.update_alerts_to_task(task_entity.alerts, task_founded, user_id)

        if(isinstance(task_entity.labels, list)): 
            self.update_labels_to_task(task_entity.labels, task_founded, user_id)

        if(isinstance(task_entity.links, list)): 
            self.update_links_to_task(task_entity.links, task_founded, user_id)

        task_updated = Task.objects.filter(
            tsk_id=task_entity.id,
            fk_tsk_use_id=user_id
        ).update(**self.dict_keys)

        return task_updated

    
    def update_alerts_to_task(self, alerts_id: list[str], task_founded: Task ,user_id):
        alerts = task_founded.fk_tsk_ale_id.all()
        alerts_to_task_id = [ale.ale_id for ale in alerts]

        alerts_to_remove = list(filter(lambda x: x not in alerts_id, alerts_to_task_id))
        alerts_to_add = list(filter(lambda x: x not in alerts_to_task_id, alerts_id))

        if len(alerts_to_remove): task_founded.fk_tsk_ale_id.remove(*Alerts.objects.filter(ale_id__in=alerts_to_remove))
        if len(alerts_to_add): task_founded.fk_tsk_ale_id.add(*Alerts.objects.filter(ale_id__in=alerts_to_add, fk_ale_use_id=user_id))


    def update_labels_to_task(self, labels_id: list[str], task_founded: Task, user_id: str):
        labels = task_founded.fk_tsk_lab_id.all()
        labels_to_task_id = [lb.lab_id for lb in labels]

        labels_to_remove = list(filter(lambda x: x not in labels_id, labels_to_task_id))
        labels_to_add = list(filter(lambda x: x not in labels_to_task_id, labels_id))

        if len(labels_to_remove): task_founded.fk_tsk_lab_id.remove(*Labels.objects.filter(lab_id__in=labels_to_remove))
        if len(labels_to_add): task_founded.fk_tsk_lab_id.add(*Labels.objects.filter(lab_id__in=labels_to_add, fk_lab_use_id=user_id))


    def update_links_to_task(self, links_id: list[str], task_founded: Task, user_id: str):
        links = task_founded.fk_tsk_asc_id.all()
        links_to_task_id = [link.asc_id for link in links]

        links_to_remove = list(filter(lambda x: x not in links_id, links_to_task_id))
        links_to_add = list(filter(lambda x: x not in links_to_task_id, links_id))

        if len(links_to_remove): task_founded.fk_tsk_asc_id.remove(*LinksAssociates.objects.filter(asc_id__in=links_to_remove))
        if len(links_to_add): task_founded.fk_tsk_asc_id.add(*LinksAssociates.objects.filter(asc_id__in=links_to_add, fk_asc_use_id=user_id))

    
    def findall_tasks_to_expired(self):

        #Query para buscar todas as tarefas que estao com os alertas para vencer.
        query = """ 
            SELECT 
                tsk.tsk_id,
                tsk.tsk_description,
                tsk.tsk_conclude_at,
                tsk.created_at,
                tsk.tsk_title,
                ale.ale_date,
                ale.ale_id,
                use.use_email,
                use.use_name,
                use.use_id
            FROM "Task_task" AS tsk
            INNER JOIN "Task_task_fk_tsk_ale_id" AS ts_ale ON ts_ale.task_id = tsk.tsk_id
            INNER JOIN "Alerts_alerts" AS ale ON ale.ale_id = ts_ale.alerts_id
            INNER JOIN "Status_status" AS sta ON sta.sta_id = tsk.fk_tsk_sta_id_id
            INNER JOIN "User_user" AS use ON use.use_id = tsk.fk_tsk_use_id_id
            WHERE 
                sta.sta_name != 'CONCLUDE' AND
                ale.ale_date >= date_trunc('day', now() - interval '3 hours') + interval '1 day'
                AND ale.ale_date <  date_trunc('day', now() - interval '3 hours') + interval '2 day';
        """

        tickets_to_expired = Task.objects.raw(query)

        return tickets_to_expired
    


    def update_task_alerts(self, alert_ids: list[str]):

        alerts_updated = (
            Alerts.objects
            .filter(
                ale_id__in=alert_ids
            )
            .update(
                #F = Pega o registro da tabela sem precisar de query
                ale_date=Case(
                    When(ale_repeat="DAY", then=F("ale_date") + timedelta(days=1)),
                    When(ale_repeat="WEEK", then=F("ale_date") + timedelta(weeks=1)),
                    When(ale_repeat="MONTH", then=F("ale_date") + timedelta(days=30)),
                    When(ale_repeat="TRIMESTER", then=F("ale_date") + timedelta(days=90)),
                    When(ale_repeat="SEMESTER", then=F("ale_date") + timedelta(days=180)),
                    When(ale_repeat="YEAR", then=F("ale_date") + timedelta(days=365)),
                    default=F("ale_date"),
                    output_field=DateTimeField(),
                )
            )
        )

        return alerts_updated
