from django.urls import path
from .views import cake_list, cake_detail_view

urlpatterns = [
    path('api/cakes/', cake_list, name='cake_list'),
    path('cake/<int:cake_id>/', cake_detail_view, name='cake_detail'),
]
