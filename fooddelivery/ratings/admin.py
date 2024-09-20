from django.contrib import admin
from ratings.models import Rating
# Register your models here.

@admin.register(Rating)
class RaringAdmin(admin.ModelAdmin):
    list_display = ['score', 'comment','user']
