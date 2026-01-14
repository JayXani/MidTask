from ...infra.repository import TaskRepository
from ...domain.entities import TaskEntity


class DeleteTaskUseCase:
    def __init__(self):
        self.repository = TaskRepository()

    def execute(self, tasks_id: list[str], user_id: str):
        task_entities = [TaskEntity(id=task) for task in tasks_id.get("id", [])]

        tasks_deleted = self.repository.delete(task_entities, user_id)
        return tasks_deleted
