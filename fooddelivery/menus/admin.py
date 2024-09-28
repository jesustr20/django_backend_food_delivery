from django.contrib import admin
from menus.models import Menu

# Register your models here.
@admin.register(Menu)
class MenuADmin(admin.ModelAdmin):
    list_display = ['name','description']
