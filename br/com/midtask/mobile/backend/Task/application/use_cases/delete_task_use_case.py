from ...infra.repository import TaskRepository
from ...domain.entities import TaskEntity
from Notifications.infra.jobs.send_email import send_emails
from datetime import datetime

class DeleteTaskUseCase:
    def __init__(self):
        self.repository = TaskRepository()

    def execute(self, tasks_id: list[str],  data_user):
        task_entities = [TaskEntity(id=task) for task in tasks_id.get("id", [])]
        tasks_deleted = self.repository.delete(task_entities, data_user.use_id)

        if(len(tasks_deleted) and tasks_deleted[0] >= 1):
            send_emails(
                "emails/task_deleted.html",
                {
                    "subject": "Tarefa deletada !",
                    "user_name": data_user.use_name,
                    "deleted_by": data_user.use_name,
                    "deleted_at": datetime.now().strftime("%d/%m/%Y as %H:%M:%S"),
                    "ids_deleted": list(map(lambda x: x.id, task_entities))
                },
                data_user.use_email
            )
        return tasks_deleted
