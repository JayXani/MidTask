from django.db import models
from django.conf import settings
from uuid import uuid4 
class Alerts(models.Model):
    ale_id=models.UUIDField(primary_key=True, editable=False, default=uuid4)
    ale_date=models.DateTimeField()
    ale_repeat=models.CharField(max_length=20)
    ale_name=models.CharField(max_length=30)
    fk_ale_use_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )