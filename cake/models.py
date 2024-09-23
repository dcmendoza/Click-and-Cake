from django.db import models

# Create your models here.

class Cake(models.Model):
    cake_id = models.AutoField(primary_key=True)

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)

class Account(models.Model):
    account_id = models.AutoField(primary_key=True)  # ID de la cuenta autoincrementado
    username = models.CharField(max_length=255, unique=True)  # Nombre de usuario
    password = models.CharField(max_length=128)  # Contraseña
    email = models.EmailField(unique=True)  # Email único
    phone = models.BigIntegerField(null=True, blank=True)  # Número de teléfono
    is_staff = models.BooleanField(default=False)  # Define si el usuario es parte del personal
    cards_saved = models.ManyToManyField('Card', blank=True, related_name='saved_by')  # Relación con Card

class Card(models.Model):
    card_id = models.AutoField(primary_key=True)  # ID de la tarjeta autoincrementado
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='card_accounts')  # Relación con Account
    card_number = models.CharField(max_length=16)  # Número de tarjeta
    expire_date = models.DateField()  # Fecha de expiración de la tarjeta
    cvc = models.IntegerField()  # Código de verificación de la tarjeta

    
class FeedBack(models.Model):
    feedback_id = models.AutoField(primary_key=True)  # Campo de ID autogenerado
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='feedbacks')  # Relación con Account
    comment = models.TextField()  # Campo para el comentario
    date = models.DateField(auto_now_add=True)  # Fecha del comentario, se autoasigna la fecha actual

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE, related_name='cake_reviews')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='reviews_given')
    comment = models.TextField()
    rating = models.FloatField()
    date = models.DateField(auto_now_add=True)

class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payments')
    payment_status = models.BooleanField()
    method = models.CharField(max_length=32)

class Delivery (models.Model):
    delivery_id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='deliveries')
    address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=16)
    arrival_date = models.DateField()
    delivery_man_info = models.JSONField(default=dict)
    delivery_status= models.CharField(max_length=32)

