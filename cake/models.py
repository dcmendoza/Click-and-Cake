from django.db import models
from account.models import *

# Create your models here.

class Cake(models.Model):
    cake_id = models.AutoField(primary_key=True)

class FeedBack(models.Model):
    feedback_id = models.AutoField(primary_key=True)  # Campo de ID autogenerado
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='feedbacks')  # Relación con Account
    comment = models.TextField()  # Campo para el comentario
    date = models.DateField(auto_now_add=True)  # Fecha del comentario, se autoasigna la fecha actual

