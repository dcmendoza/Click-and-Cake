from django.db import models
from account.models import Account

# Create your models here.
class Cake(models.Model):
    """
    Model representing a customizable cake.
    """

    # Opciones para el tamaño del pastel
    SIZE_CHOICES = [
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    ]

    # Opciones para el sabor del pastel
    FLAVOR_CHOICES = [
        ('vanilla', 'Vanilla'),
        ('chocolate', 'Chocolate'),
        ('strawberry', 'Strawberry'),
        ('red_velvet', 'Red Velvet'),
        ('lemon', 'Lemon'),
    ]

    # Opciones para el sabor de la crema
    CREAM_FLAVOR_CHOICES = [
        ('vanilla', 'Vanilla'),
        ('chocolate', 'Chocolate'),
        ('cream_cheese', 'Cream Cheese'),
        ('buttercream', 'Buttercream'),
        ('lemon', 'Lemon'),
    ]

    # Opciones para la forma del pastel
    SHAPE_CHOICES = [
        ('round', 'Round'),
        ('square', 'Square'),
        ('heart', 'Heart'),
        ('rectangle', 'Rectangle'),
    ]

    # Opciones para los toppings
    TOPPING_CHOICES = [
        ('sprinkles', 'Sprinkles'),
        ('chocolate_chips', 'Chocolate Chips'),
        ('fruits', 'Fruits'),
        ('nuts', 'Nuts'),
        ('whipped_cream', 'Whipped Cream'),
    ]

    name = models.CharField(max_length=255)  # Nombre del pastel
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Precio del pastel
    size = models.CharField(max_length=10, choices=SIZE_CHOICES, default='medium')  # Tamaño seleccionado
    flavor = models.CharField(max_length=20, choices=FLAVOR_CHOICES, default='vanilla')  # Sabor principal del pastel
    cream_flavor = models.CharField(max_length=20, choices=CREAM_FLAVOR_CHOICES, default='vanilla')  # Sabor de la crema
    shape = models.CharField(max_length=10, choices=SHAPE_CHOICES, default='round')  # Forma del pastel
    toppings = models.JSONField(default=list)  # Toppings seleccionables
    description = models.TextField(blank=True)  # Descripción del pastel
    picture = models.ImageField(upload_to='img/cake/', blank=True, null=True)  # Imagen del pastel

    def __str__(self):
        return f'{self.name} ({self.flavor} flavor) - {self.size} size'

class Review(models.Model):
    """
    Model representing a review of a cake made by a user.
    """

    cake = models.ForeignKey(Cake, on_delete=models.CASCADE, related_name='reviews')  # Relación con Cake
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='reviews')  # Relación con User
    comment = models.TextField()  # Comentario de la reseña
    rating = models.FloatField()  # Puntuación de la reseña (de 0 a 5)
    date = models.DateTimeField(auto_now_add=True)  # Fecha de la reseña (se asigna automáticamente cuando se crea)

    def __str__(self):
        return f'Review by {self.user.user.username} for {self.cake.name} - Rating: {self.rating}'
