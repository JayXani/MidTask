from ...infra.repository import TaskRepository
from ...domain.entities import TaskEntity
from ...domain.service.TaskServicePolicy import TaskServicePolicy
from Notifications.infra.jobs.send_email import send_welcome_email_task

class CreateTaskUseCase():
    def __init__(self):
        self.repository = TaskRepository()

    def execute(self, task: dict, user_id: str):
        task_entity = TaskEntity(**task)
        service_policy = TaskServicePolicy()
        service_policy.create_task_validation(task_entity, user_id)

        task_created = self.repository.create(task_entity, user_id)
        # if(len(task_created)): #Atualizar depois
        #     new_task = task_created[0]
        #     send_welcome_email_task.delay(
        #         "emails/welcome.html",
        #         {
        #             "task_name": new_task.title,
        #             "created_at": new_task.created_at.strftime("%d/%m/%Y"),
        #             "description": new_task.description, 
        #             "due_date": new_task.conclude_at.strftime("%d/%m/%Y") if new_task.conclude_at else "",
        #         },
        #         #new_task.
        #     )
        return task_created