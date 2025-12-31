from django.db import models
from uuid import uuid4
from Task.models import Task

class StatusChecklist(models.TextChoices):
    CONCLUDE= "CONCLUDE"
    PENDING = "PENDING"
    SCHEDULED="SCHEDULED"



# Create your models here.
class CheckLists(models.Model):
    che_id=models.UUIDField(primary_key=True, editable=False, default=uuid4)
    che_name=models.CharField(max_length=30)
    che_status=models.CharField(choices=StatusChecklist)
    che_date=models.DateTimeField()
    fk_che_tsk_id = models.ForeignKey(Task, on_delete=models.CASCADE)