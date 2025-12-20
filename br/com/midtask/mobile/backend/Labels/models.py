from django.db import models
from uuid import uuid4
from django.conf import settings

class Labels(models.Model):
    lab_id=models.UUIDField(primary_key=True, editable=False, default=uuid4)
    lab_name=models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    fk_lab_use_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
