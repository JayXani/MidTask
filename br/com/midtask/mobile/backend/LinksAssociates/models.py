from django.db import models
from uuid import uuid4
from django.conf import settings


class LinksAssociates(models.Model):
    asc_id=models.UUIDField(primary_key=True, editable=False, default=uuid4)
    asc_name=models.CharField(unique=True, null=True)
    asc_link_reference=models.TextField(unique=True)
    asc_type=models.CharField(max_length=10)
    asc_icon=models.TextField(null=True)
    fk_asc_use_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
