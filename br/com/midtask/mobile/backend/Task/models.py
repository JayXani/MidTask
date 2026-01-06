from django.db import models
from uuid import uuid4
from django.conf import settings

class Task(models.Model):
    tsk_id=models.UUIDField(primary_key=True, editable=False, default=uuid4)
    tsk_title=models.CharField(max_length=30)
    tsk_description=models.TextField()
    tsk_recurrence=models.CharField(max_length=10)
    tsk_recurrence_end_in=models.DateTimeField()
    tsk_conclude_expected_at=models.DateTimeField()
    tsk_conclude_at=models.DateTimeField()
    tsk_background=models.CharField(max_length=15)
    fk_tsk_sta_id=models.ManyToManyField(
        "Status.Status",
        blank=True
    )
    fk_tsk_use_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    fk_tsk_ale_id=models.ManyToManyField(
        "Alerts.Alerts",
        blank=True
    )
    fk_tsk_lab_id=models.ManyToManyField(
        'Labels.Labels',
        blank=True
    )
    fk_tsk_asc_id=models.ManyToManyField(
        'LinksAssociates.LinksAssociates',
        blank=True
    )
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now_add=True)
