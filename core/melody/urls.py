from django.urls import path
from . import views

urlpatterns = [
    path('', views.melody_home, name='melody_home')
]