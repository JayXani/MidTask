from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from uuid import uuid4
from django.conf import settings


# Create your models here.
class Status(models.TextChoices):
    ACTIVATE = "A", "ACTIVATE"  # Enum para status, é do tipo text choices
    BLOCKED = "B", "BLOCKED"
    DEACTIVATE = "D", "DEACTIVATE"

class UserManager(BaseUserManager): 
    def create_user(self, email: str, password: str, **extra_fields): # Método para criar o user padrao
        email = self.normalize_email(email)
        user = self.model(use_email=email, **extra_fields)
        user.set_password(password) # Já cria a senha com o hash (nativo)
        user.save(using=self.db)

        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self.create_user(email, password, **extra_fields)

#Para o auth funcionar, eu preciso instanciar as classes nativas do django que já fazem isso
class User(AbstractBaseUser, PermissionsMixin):
    username = None  # REMOVE username padrão, pois nao posso user ele + email login
    last_login = None # REMOVE o last_login, pois nao usamos ele
    
    use_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    use_name = models.CharField(max_length=150)
    use_avatar=models.CharField(default="")
    use_status = models.CharField(choices=Status, max_length=10)
    use_email = models.EmailField(unique=True)
    use_phone = models.CharField(max_length=20, null=True)
    use_login_type = models.CharField(max_length=30)
    use_ip_address = models.GenericIPAddressField()
    use_google_id=models.CharField(unique=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "use_email"
    REQUIRED_FIELDS = ["use_name"]
    

    objects = UserManager() # Instancia correta para salvar o usuário já com as validacoes e tratamentos

    def __str__(self):
        return self.use_email # Tem que ser o mesmo campo de email que está nos atributos
    


# Create your models here.
class ChangeLog(models.Model):
    log_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    log_type = models.CharField(max_length=30, editable=False)
    log_date = models.DateField(editable=False, auto_now_add=True)
    log_endpoint = models.CharField(max_length=30, editable=False)
    log_description = models.TextField(editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        editable=False
    )
