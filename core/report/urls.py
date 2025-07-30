from django.urls import path
from .views import report_home

urlpatterns = [
    path('', report_home, name='report_home')
]