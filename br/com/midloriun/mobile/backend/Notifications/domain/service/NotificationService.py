# user/application/services/notification_service.py
from ...infra.jobs.send_email import send_welcome_email_task

class NotificationService:
    def send_welcome_email(self, user):
        context = {
            "name": user.use_name,
            "email": user.use_email,
            "date_start": user.created_at
        }

        send_welcome_email_task.delay(context, user.use_email)
