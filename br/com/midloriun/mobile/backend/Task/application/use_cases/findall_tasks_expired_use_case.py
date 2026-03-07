from ...infra.repository import TaskRepository


class FindAllTasksExpiredUseCase():
    def __init__(self):
        self.repository = TaskRepository()

    def execute(self, timezone: dict):
        tasks_expired = self.repository.findall_tasks_to_expired(timezone.get("timezone", "-3"))
        return tasks_expired