from django.db import models

# Create your models here.
class Account(models.Model):
    account_id = models.AutoField(primary_key=True)  # ID de la cuenta autoincrementado
    username = models.CharField(max_length=255, unique=True)  # Nombre de usuario
    password = models.CharField(max_length=128)  # Contraseña
    email = models.EmailField(unique=True)  # Email único
    phone = models.BigIntegerField(null=True, blank=True)  # Número de teléfono
    is_staff = models.BooleanField(default=False)  # Define si el usuario es parte del personal
    #cards_saved = models.ManyToManyField('Card', blank=True, related_name='saved_by')  # Relación con Card
