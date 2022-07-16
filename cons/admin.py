from django.contrib import admin
from .models import Cup

@admin.register(Cup)
class CupAdmin(admin.ModelAdmin):
    pass
