from ...infra.repository import TaskRepository
from ...domain.entities import TaskEntity
from ...domain.service.TaskServicePolicy import TaskServicePolicy

class FindUniqueTaskUseCase():
    def __init__(self):
        self.repository = TaskRepository()

    def execute(self, task_id:str, user_id: str):
        task_entity = TaskEntity(id=task_id)
        task_founded = self.repository.findall([task_entity], user_id)
        return task_founded