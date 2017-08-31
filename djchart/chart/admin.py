from django.contrib import admin
from .models import RainFall

@admin.register(RainFall)
class RainFallAdmin(admin.ModelAdmin):
	list_display = ['month', 'centimeter']
