from django.shortcuts import render
from django.http import HttpResponse
from .models import Song

# Create your views here.

def melody_home(request):
    return HttpResponse("This is Home for melody Songs")

def song_list(request):
    songs = Song.objects.all()
    print("Songs in DB:", songs)
    return render(request, 'melody/song_list.html', {'songs': songs})