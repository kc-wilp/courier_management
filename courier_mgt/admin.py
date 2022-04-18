from django.contrib import admin

# Register your models here.
from .models import Bookings, Profile, Consignment

admin.site.register(Consignment)
admin.site.register(Bookings)
admin.site.register(Profile)
