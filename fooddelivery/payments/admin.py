from django.contrib import admin
from payments.models import Payment
# Register your models here.

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['amount','payment_method','status','order']
