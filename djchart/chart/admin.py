# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from models import RainFall

class RainFallAdmin(admin.ModelAdmin):
	list_display = ['month', 'centimeter']

admin.site.register(RainFall, RainFallAdmin)
