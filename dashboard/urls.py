from django.urls import path
from . import views

APP_NAME = 'dashboard'

urlpatterns = [
    path('dash/', views.dashboard_home, name='dashboard'),
    path('dash/<str:model_name>/', views.model_list, name='model_list'),
    path('dash/<str:model_name>/create/', views.create_object, name='create_object'),
    path('dash/<str:model_name>/<int:object_id>/', views.model_detail, name='model_detail'),
]
