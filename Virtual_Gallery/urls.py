from django.urls import path
from Virtual_Gallery.views import *

urlpatterns = [
    path('', glownaObrazy, name='glowna'),
    path('nowy/',nowyObraz, name='nowy'),
    path('edytuj/<int:id>/', edytujObraz, name='edytuj'),
    path('usun/<int:id>/', usunObraz, name='usun'),
    path('opis/<int:id>/', opisObrazu, name='opis'),
    path('profil/', profileView, name='profil'),
    #path('zamowienie/<int:id>/', zlozenieZamowienia, name='zamowienie'),
] 