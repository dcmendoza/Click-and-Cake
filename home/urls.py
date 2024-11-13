from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('menu/',views.menu_view, name='menu'),
    path('report/<str:report_type>/', views.generate_report, name='generate_report'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
]
