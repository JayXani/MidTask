from django.db import models
from uuid import uuid4
from User.models import User

# Create your models here.
class Labels(models.Model):
    lab_id=models.UUIDField(primary_key=True, editable=False, default=uuid4())
    lab_name=models.CharField(max_length=20, unique=True)

class Alerts(models.Model):
    ale_id=models.UUIDField(primary_key=True, editable=False, default=uuid4())
    ale_date=models.DateTimeField()
    ale_repeat=models.CharField(max_length=10)

class LinksAssociates(models.Model):
    asc_id=models.UUIDField(primary_key=True, editable=False, default=uuid4())
    asc_name=models.CharField(unique=True, null=True)
    asc_link_reference=models.TextField(unique=True)
    asc_type=models.CharField(max_length=10)
    asc_icon=models.TextField(null=True)

class Task(models.Model):
    tsk_id=models.UUIDField(primary_key=True, editable=False, default=uuid4())
    tsk_title=models.CharField(max_length=30)
    tsk_description=models.TextField()
    tsk_status=models.CharField(max_length=20)
    tsk_recurrence=models.CharField(max_length=10)
    tsk_conclude_expected_at=models.DateTimeField()
    tsk_conclude_at=models.DateTimeField()
    tsk_background=models.CharField(max_length=15)
    tsk_is_running=models.BooleanField(default=False)
    fk_tsk_use_id=models.ForeignKey(User, on_delete=models.CASCADE)
    fk_tsk_ale_id=models.ForeignKey(Alerts, on_delete=models.CASCADE)
    labels=models.ManyToManyField(Labels)
    associateLinks=models.ManyToManyField(LinksAssociates)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now_add=True)
