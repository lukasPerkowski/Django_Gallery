from django.contrib import admin
from .models import Obraz

@admin.register(Obraz)

class ObrazAdmin(admin.ModelAdmin):
    list_display = ['tytul', 'cena', 'wlasciciel']
