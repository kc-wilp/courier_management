from django.contrib import admin

# Register your models here.
from .models import Bookings, Profile

admin.site.register(Bookings)
admin.site.register(Profile)
