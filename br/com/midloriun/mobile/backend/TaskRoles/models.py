from django.db import models
from Scope.models import Scope

class TaskRoles(models.Model):
    tsr_id = models.UUIDField(primary_key=True, unique=True, editable=False)
    tsr_name = models.CharField(null=False, editable=True, unique=True, max_length=30)
    tsr_description = models.CharField(null=True, editable=True, max_length=255)

    fk_tsr_scp_id = models.ManyToManyField(Scope, blank=True)