from django.contrib import admin
from addresses.models import Address
# Register your models here.

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['address', 'district','province','department','country','postal_code']