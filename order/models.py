from django.db import models
from account.models import *
# Create your models here.
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)

class Delivery (models.Model):
    delivery_id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='deliveries')
    address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=16)
    arrival_date = models.DateField()
    delivery_man_info = models.JSONField(default=dict)
    delivery_status= models.CharField(max_length=32)