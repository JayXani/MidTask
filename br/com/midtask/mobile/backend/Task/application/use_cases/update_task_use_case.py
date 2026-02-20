from ...infra.repository import TaskRepository
from ...domain.entities import TaskEntity
from Notifications.infra.jobs.send_email import send_emails
from ...domain.service.TaskServicePolicy import TaskServicePolicy

class UpdateTaskUseCase():
    def __init__(self):
        self.repository = TaskRepository()

    def execute(self, task_dict: dict, task_id: str, user_id: str, user_email: str):
        task_entity = TaskEntity(**task_dict)
        task_policy = TaskServicePolicy()
        task_entity.id = task_id
        task_policy.update_task_validation(task_entity, user_id)

        task_updated = self.repository.update(task_entity, user_id)
        task_founded = self.repository.findall([TaskEntity(id=task_id)], user_id)

        if len(task_founded):
            task_unique = task_founded[0]
            status_is_conclude = list(filter(lambda x: x.name.upper() == "CONCLUDE", task_unique.status))
            
            if len(status_is_conclude):
                send_emails(
                    "emails/task_conclude.html",
                    {
                        "subject": "Parabéns ! Você acaba de concluir uma tarefa.",
                        "task_name": task_unique.title,
                        "due_date": task_unique.expected_conclude_in.strftime("%d/%m/%Y") if task_unique.expected_conclude_in else "",
                        "completed_at": task_unique.conclude_at.strftime("%d/%m/%Y") if task_unique.conclude_at else "",
                        "task_description": task_unique.description
                    },
                    user_email
                )
                

        if(not task_updated): raise Exception("Error ! Anyone data updated")
        return task_updated