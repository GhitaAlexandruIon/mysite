from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_addres', views.add_address, name='add_address'),
]
