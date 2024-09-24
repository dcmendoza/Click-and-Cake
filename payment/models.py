from django.db import models
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator
from account.models import Account
from order.models import Order

# Create your models here.
class Card(models.Model):
    """
    Model representing a payment card associated with a user account.
    """

    CARD_TYPE_CHOICES = [
        ('debit', 'Débito'),
        ('credit', 'Crédito'),
    ]

    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='cards')
    card_number = models.CharField(max_length=16, validators=[MinLengthValidator(16)])
    expire_date = models.DateField(help_text="Expiration date in the format YYYY-MM-DD")
    cvc = models.IntegerField(validators=[MinValueValidator(100), MaxValueValidator(9999)])
    card_type = models.CharField(max_length=10, choices=CARD_TYPE_CHOICES)

    def __str__(self):
        # Mask the card number for security purposes (show only the last 4 digits)
        return f'**** **** **** {str(self.card_number)[-4:]} - Exp: {self.expire_date}'

class Payment(models.Model):
    """
    Model representing a payment for an order.
    """

    # Opciones para el estado del pago
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed')
    ]

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payments')
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='pending')
    method = models.CharField(max_length=32)

    @property
    def total_amount(self):
        return self.order.full_price

    def is_completed(self):
        return self.payment_status == 'completed'

    def __str__(self):
        return f'Payment {self.payment_status} for Order {self.order.order_id}'