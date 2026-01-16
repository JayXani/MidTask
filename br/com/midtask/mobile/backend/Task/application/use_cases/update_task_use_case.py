from ...infra.repository import TaskRepository
from ...domain.entities import TaskEntity

class UpdateTaskUseCase():
    def __init__(self):
        self.repository = TaskRepository()

    def execute(self, task_dict: dict, task_id: str, user_id: str):
        task_entity = TaskEntity(**task_dict)
        task_entity.id = task_id

        task_updated = self.repository.update(task_entity, user_id)
        if(not task_updated): raise Exception("Error ! Anyone data updated")
        return task_updated