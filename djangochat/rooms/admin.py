from django.contrib import admin
from .models import Message, Rooms
# Register your models here.

admin.site.register(Rooms)
admin.site.register(Message)