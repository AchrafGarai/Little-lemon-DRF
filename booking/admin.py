from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Booking, Menu

admin.site.register(Booking)
admin.site.register(Menu)