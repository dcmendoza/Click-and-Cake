from django.contrib.auth.models import User
from django import forms
from cake.models import Cake
from order.models import Order

class CakeForm(forms.ModelForm):
    class Meta:
        model = Cake
        fields = ['name', 'price', 'size', 'flavor', 'cream_flavor', 'shape', 'toppings', 'description', 'picture']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['account', 'delivery', 'cart']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
