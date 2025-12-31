from django.db import models
from django.conf import settings

# Create your models here.
class Status(models.Model):
    sta_id=models.UUIDField(primary_key=True, editable=False)
    sta_name=models.CharField(
        max_length=10,
        unique=True,
    )
    fk_sta_use_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE      
    )
    
    