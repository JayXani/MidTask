from django.db import models
from uuid import uuid4
from django.conf import settings


class StatusTask(models.TextChoices):
    CONCLUDE= "CONCLUDE"
    PENDING = "PENDING"
    SCHEDULED="SCHEDULED"


class Task(models.Model):
    tsk_id=models.UUIDField(primary_key=True, editable=False, default=uuid4)
    tsk_title=models.CharField(max_length=30)
    tsk_description=models.TextField()
    tsk_status=models.CharField(max_length=20)
    tsk_recurrence=models.CharField(max_length=10)
    tsk_conclude_expected_at=models.DateTimeField()
    tsk_conclude_at=models.DateTimeField()
    tsk_background=models.CharField(max_length=15)
    tsk_is_running=models.BooleanField(default=False)
    fk_tsk_use_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    fk_tsk_ale_id=models.ForeignKey(
        "Alerts.Alerts",
        on_delete=models.CASCADE
    )
    labels=models.ManyToManyField(
        'Labels.Labels',
        blank=True
    )
    associateLinks=models.ManyToManyField(
        'LinksAssociates.LinksAssociates',
        blank=True
    )
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now_add=True)


class CheckLists(models.Model):
    che_id=models.UUIDField(primary_key=True, editable=False, default=uuid4)
    che_name=models.CharField(max_length=30)
    che_status=models.CharField(choices=StatusTask)
    che_date=models.DateTimeField()
    fk_che_tsk_id = models.ForeignKey(Task, on_delete=models.CASCADE)