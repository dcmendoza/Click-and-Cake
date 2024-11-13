from django.urls import path
from .views import cake_list

urlpatterns = [
    path('api/cakes/', cake_list, name='cake_list'),
]
