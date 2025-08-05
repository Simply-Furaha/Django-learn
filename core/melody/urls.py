from django.urls import path
from . import views

urlpatterns = [
    # path('', views.melody_home, name='melody_home'),
    path('', views.song_list, name='song_list' )
]