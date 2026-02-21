from celery import shared_task
from Task.application.use_cases.dispatch_alerts_use_case import DispatchAlertsUseCase
from Notifications.infra.jobs.send_email import send_emails

@shared_task
def send_alerts(): 
    use_case = DispatchAlertsUseCase()
    tasks_to_expired = use_case.execute()
    
    #if not tasks_to_expired.get("success"): send_emails() # Vai enviar e-mail para o admin no caso de erros
    