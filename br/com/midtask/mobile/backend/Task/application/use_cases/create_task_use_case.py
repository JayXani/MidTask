from ...infra.repository import TaskRepository
from ...domain.entities import TaskEntity
from ...domain.service.TaskServicePolicy import TaskServicePolicy

class CreateTaskUseCase():
    def __init__(self):
        self.repository = TaskRepository()

    def execute(self, task: dict, user_id: str):
        task_entity = TaskEntity(**task)
        service_policy = TaskServicePolicy()
        service_policy.create_task_validation(task_entity, user_id)

        task_created = self.repository.create(task_entity, user_id)
        return task_created