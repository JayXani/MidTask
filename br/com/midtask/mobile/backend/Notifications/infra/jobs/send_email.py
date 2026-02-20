# notifications/tasks.py
from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

@shared_task(bind=True, autoretry_for=(Exception,), retry_kwargs={'max_retries': 3, 'countdown': 10})
def send_emails(self, path, context: dict, recipient: str):
    html_content = render_to_string(
        path,
        context
    )

    email = EmailMultiAlternatives(
        subject=context.get("subject", ""),
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[recipient],
    )

    email.attach_alternative(html_content, "text/html")
    email.send()
