from django.contrib import admin
from drivers.models import Driver
# Register your models here.

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ['name','phone_number','email','location','vehicle_model','vehicle_plate','vehicle_color']