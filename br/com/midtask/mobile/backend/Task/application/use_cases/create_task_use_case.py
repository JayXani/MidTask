from ...infra.repository import TaskRepository
from ...domain.entities import TaskEntity
from ...domain.service.TaskServicePolicy import TaskServicePolicy
from Notifications.infra.jobs.send_email import send_emails
from User.infra.repository import UserRepository, UserEntity

class CreateTaskUseCase():
    def __init__(self):
        self.repository = TaskRepository()
        self.user_repository = UserRepository()

    def execute(self, task: dict, user_id: str):
        task_entity = TaskEntity(**task)
        service_policy = TaskServicePolicy()
        service_policy.create_task_validation(task_entity, user_id)
        task_created = self.repository.create(task_entity, user_id)
        user = self.user_repository.find(UserEntity(id=user_id))

        if(len(task_created)): #Atualizar depois
            new_task = task_created[0]
            send_emails.delay(
                "emails/new_task.html",
                {
                    "subject": "Nova task criada !",
                    "task_name": new_task.title,
                    "created_at": new_task.created_at.strftime("%d/%m/%Y"),
                    "task_description": new_task.description, 
                    "due_date": new_task.expected_conclude_in.strftime("%d/%m/%Y") if new_task.expected_conclude_in else "",
                },
                user.email
            )
        return task_created