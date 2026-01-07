from ...infra.repository import TaskRepository
from ...domain.entities import TaskEntity
from ...domain.service.TaskServicePolicy import TaskServicePolicy

class CreateTaskUseCase():
    def __init__(self):
        self.repository = TaskRepository()

    def execute(self, task: dict, user_id: str):
        task_entity = TaskEntity(**task)
        service_policy = TaskServicePolicy(user_id)

        if(task.get("alert_id")): service_policy.alerts_exists(task.get("alert_id"))
        if(task.get("label_id")): service_policy.labels_exists(task.get("label_id"))
        if(task.get("links_id")): service_policy.links_exists(task.get("links_id"))
        if(task.get("status_id")): service_policy.status_exists(task.get("status_id"))

        task_created = self.repository.create(task_entity, user_id)
        return task_created