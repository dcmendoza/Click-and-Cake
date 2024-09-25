from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cart(models.Model):
    """
    Model representing a shopping cart.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart', null=True, blank=True)  # Relación con el usuario
    cake_quantities = models.JSONField(default=dict)  # Diccionario que guarda {cake_id: cantidad}

    def add_cake(self, cake_id, quantity=1):
        """
        Adds or updates the quantity of a cake in the cart.
        """
        cake_id_str = str(cake_id)
        if cake_id_str in self.cake_quantities:
            self.cake_quantities[cake_id_str] += quantity
        else:
            self.cake_quantities[cake_id_str] = quantity
        self.save()

    def partial_price(self):
        """
        Calculates the partial price of all cakes in the cart.
        """
        total = 0
        for cake_id_str, quantity in self.cake_quantities.items():
            try:
                from cake.models import Cake
                cake = Cake.objects.get(id=int(cake_id_str))
                total += cake.price * quantity
            except Cake.DoesNotExist:
                pass
        return total

    def __str__(self):
        return f'Cart for {self.user.first_name}'

class FeedBack(models.Model):
    """
    Model representing general feedback left by a user about the website/platform.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedback', null=True, blank=True)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Feedback by {self.user.first_name} on {self.date.strftime("%Y-%m-%d")}'
