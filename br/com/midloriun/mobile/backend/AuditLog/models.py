from uuid import uuid4
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.
class ChangeLog(models.Model):
    log_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    log_old_data = models.JSONField(null=True, blank=True)
    log_new_data = models.JSONField(null=True, blank=True)
    log_action = models.CharField(max_length=20)
    log_object_id = models.CharField(max_length=50) #Registro alterado
    log_use_id = models.UUIDField(editable=False) #Nao posso vincular com o user pois quando apagar o user, preciso manter os logs
    log_use_name = models.CharField(editable=False)
    log_use_ip = models.GenericIPAddressField(editable=False)
    
    fk_log_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE) #Permite vincular qualquer tabela dinamicamente
    fk_log_content_object = GenericForeignKey("fk_log_content_type", "log_object_id") #Vincula o object id e o meu modelo dinamicamente, sem precisar referenciar

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
