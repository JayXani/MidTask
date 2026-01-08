from ...domain.entities import TaskEntity
from ...domain.validations.task_validations import (
    alerts_exists,
    labels_exists,
    links_exists,
    status_exists,
    date_valid
)
class TaskServicePolicy():
    def create_task_validation(self, task_entity: TaskEntity, user_id: str):
        if(task_entity.alert_id): alerts_exists(task_entity.alert_id, user_id)
        if(task_entity.labels_id): labels_exists(task_entity.labels_id, user_id)
        if(task_entity.links_id): links_exists(task_entity.links_id, user_id)
        if(task_entity.status_id): status_exists(task_entity.status_id, user_id)

        if(task_entity.recurrence):
            recurrence_is_date = date_valid(task_entity.recurrence)
            if(task_entity.recurrence not in ["null", "month", "week"] and not recurrence_is_date): 
                raise Exception("Recurrence is invalid, you should sended: week, null, month or day(Only dates: 2026-01-01 12:00:00)")

        
