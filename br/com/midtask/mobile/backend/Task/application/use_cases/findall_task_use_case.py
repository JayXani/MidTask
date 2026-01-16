from ...infra.repository import TaskRepository
from ...domain.validations.task_validations import normalize_payload
from ...domain.entities import TaskEntity

class FindAllTaskUseCase():
    def __init__(self):
        self.repository = TaskRepository()

    def execute(self, task: dict, user_id: str):
        task_normalized = normalize_payload(task) if task else []
        task_updated = self.repository.findall(task_normalized, user_id)

        if(not len(task_updated)): return []
        return task_updated