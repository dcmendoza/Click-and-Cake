# cakes/factories.py
import factory
from faker import Faker
from .models import Cake

fake = Faker()

class CakeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Cake

    name = factory.LazyAttribute(lambda _: fake.word())  # Genera un nombre aleatorio
    price = factory.LazyAttribute(lambda _: fake.random_number(digits=3))  # Precio aleatorio
    size = factory.Iterator(['small', 'medium', 'large'])  # Opciones predefinidas de tamaño
    flavor = factory.Iterator(['vanilla', 'chocolate', 'strawberry'])  # Opciones de sabor
    cream_flavor = factory.Iterator(['vanilla', 'chocolate', 'strawberry'])  # Opciones de crema
    shape = factory.Iterator(['round', 'square', 'heart'])  # Opciones de forma
    toppings = factory.LazyAttribute(lambda _: [fake.word() for _ in range(fake.random_int(min=1, max=5))])  # Toppings aleatorios
    description = factory.LazyAttribute(lambda _: fake.sentence())  # Descripción aleatoria
    picture = None  # Deja este campo vacío o asigna una imagen si es necesario

