from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('cart/', views.cart_view, name='cart'),
    path('cart/update-item/', views.update_cart_item, name='update_cart_item'),
    path('cart/remove-item/', views.remove_from_cart, name='remove_from_cart'),
]
