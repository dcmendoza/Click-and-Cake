from django.db import models
from account.models import Cart
from django.contrib.auth.models import User

# Create your models here.
class Delivery (models.Model):
    """
    Model representing the delivery for an order.
    """

    class DeliveryStatusChoices(models.TextChoices):
        """
        Choices for the delivery status.
        """

        PENDING = 'pending', 'Pending'
        IN_TRANSIT = 'in_transit', 'In Transit'
        DELIVERED = 'delivered', 'Delivered'
        CANCELED = 'canceled', 'Canceled'

    dealer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dealer', null=True, blank=True)
    address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=16)
    arrival_date = models.DateField()
    delivery_status = models.CharField(max_length=32)
    delivery_price = models.IntegerField(default=10000)

    def __str__(self):
        return f'Delivery to {self.address} - {self.delivery_price}'

class Order(models.Model):
    """
    Model representing an order..
    """

    account = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', null=True, blank=True)
    delivery = models.OneToOneField(Delivery, on_delete=models.CASCADE, related_name='order')
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE, related_name='orders')  # Relación con Cart
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Precio total de la orden

    def save(self, *args, **kwargs):
        if self.cart and self.delivery:
            cart_total = self.cart.partial_price()  # Precio parcial del carrito
            delivery_price = self.delivery.delivery_price  # Precio de la entrega
            self.total_price = cart_total + delivery_price  # Precio total = subtotal del carrito + entrega
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Order #{self.order_id} - {self.total_price}'
