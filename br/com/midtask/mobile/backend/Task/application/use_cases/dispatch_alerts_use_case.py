from ...infra.repository import TaskRepository
from ...infra.messages import format_response
from Notifications.infra.jobs.send_email import send_emails

class DispatchAlertsUseCase():
    def __init__(self):
        self.repository = TaskRepository()

    def execute(self):
        try:
            tasks_to_expired = self.repository.findall_tasks_to_expired()
            ids = []
            if(len(tasks_to_expired)):
                for task in tasks_to_expired:
                    ids.append(task.ale_id)
                    send_emails(
                        "emails/task_to_expired.html",
                        {
                            "subject": "OPA...Suas tarefas estão expirando",
                            "task_description": task.tsk_description,
                            "due_date": task.tsk_conclude_at,
                            "created_at": task.created_at,
                            "task_name": task.tsk_title
                        },
                        task.use_email
                    )

            tasks_updated = self.repository.update_task_alerts(ids)
            
            return format_response(
                success=True,
                message="Success ! tasks founded to alerts",
                data=tasks_updated
            )
        except Exception as e:
            return format_response(
                success=False,
                message=e
            )


use_case = DispatchAlertsUseCase()
tasks_to_expired = use_case.execute()

    