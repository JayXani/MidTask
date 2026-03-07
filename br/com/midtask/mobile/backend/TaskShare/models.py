from django.db import models
from django.conf import settings
from TaskRoles.models import TaskRoles
from Task.models import Task

# Create your models here.
class TaskShare(models.Model):
    fk_tts_use_id = models.ForeignKey(
        to= settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    fk_tts_tsr_id = models.ForeignKey(
        to=TaskRoles,
        on_delete=models.CASCADE
    )
    fk_tts_tsk_id = models.ForeignKey(
        to=Task,
        on_delete=models.CASCADE
    )
    class Meta():
        constraints = [ #Garanto que a chave primaria seja a combinacao das chaves estrangeiras
            models.UniqueConstraint(
                fields=["fk_tts_use_id", "fk_tts_tsr_id", "fk_tts_tsk_id"],
                name="unique_user_task_role"
            )
        ]