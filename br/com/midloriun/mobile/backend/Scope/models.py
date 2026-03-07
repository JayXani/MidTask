from django.db import models

class Types(models.TextChoices):
    TASK="Task"
    USER="User"

# Create your models here.
class Scope(models.Model):
    scp_id = models.UUIDField(primary_key=True, editable=False, unique=True)
    scp_description = models.CharField(max_length=255)
    scp_identifier_code = models.CharField(max_length=100)
    scp_type = models.CharField(choices=Types, editable=False, null=False)