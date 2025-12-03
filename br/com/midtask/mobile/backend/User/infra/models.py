from django.db import models
from uuid import uuid4


# Create your models here.
class Status(models.TextChoices):
    ACTIVATE = "A", "ACTIVATE"  # Enum para status, é do tipo text choices
    BLOCKED = "B", "BLOCKED"
    DEACTIVATE = "D", "DEACTIVATE"


class Permission(models.Model):
    per_app_id = models.UUIDField(primary_key=True, default=uuid4(), editable=False)
    per_app_task_notification = models.BooleanField(default=False)
    per_app_calendar_home = models.BooleanField(default=False)
    per_app_task_email_notification = models.BooleanField(default=False)
    per_app_open_apps = models.BooleanField(default=False)


class User(models.Model):
    use_id = models.UUIDField(primary_key=True, default=uuid4(), editable=False)
    use_name = models.CharField(editable=True, null=False)
    use_status = models.CharField(choices=Status, editable=True, null=False)
    use_email = models.EmailField(editable=True, null=False, unique=True)
    use_password_hash = models.CharField(editable=True, null=True)
    use_phone = models.CharField(editable=True, null=True, max_length=20)
    use_login_type = models.CharField(editable=True, null=False)
    use_ip_address = models.GenericIPAddressField(editable=True, null=False)
    permissions = models.ManyToManyField(Permission, related_name="users")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)


# Create your models here.
class ChangeLog(models.Model):
    log_id = models.UUIDField(primary_key=True, default=uuid4(), editable=False)
    log_type = models.CharField(max_length=30, editable=False)
    log_date = models.DateField(editable=False, auto_now_add=True)
    log_endpoint = models.CharField(max_length=30, editable=False)
    log_description = models.TextField(editable=False)
    fk_log_use_id = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
