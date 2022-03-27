from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from .models import Rooms

# Create your views here.
@login_required()
def rooms(request):
    all_rooms = Rooms.objects.all()
    context = {'rooms': all_rooms}
    return render(request, "rooms/index.html", context)

@login_required()
def room (request, room_slug):
    room  = Rooms.objects.get(slug=room_slug)
    context  = {'room': room}
    return render(request, "rooms/room.html", context)
 