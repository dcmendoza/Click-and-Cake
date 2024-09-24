from django.db import models
from account.models import Account
from order.models import *
# Create your models here.
class Card(models.Model):
    card_id = models.AutoField(primary_key=True)  # ID de la tarjeta autoincrementado
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='card_accounts')  # Relación con Account
    card_number = models.CharField(max_length=16)  # Número de tarjeta
    expire_date = models.DateField()  # Fecha de expiración de la tarjeta
    cvc = models.IntegerField()  # Código de verificación de la tarjeta

class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payments')
    payment_status = models.BooleanField()
    method = models.CharField(max_length=32)