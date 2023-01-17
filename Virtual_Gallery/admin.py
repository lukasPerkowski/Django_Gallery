from django.contrib import admin
from .models import Obraz, Wiadomosc

admin.site.register(Wiadomosc)
@admin.register(Obraz)

class ObrazAdmin(admin.ModelAdmin):
    list_display = ['tytul', 'cena', 'wlasciciel']

