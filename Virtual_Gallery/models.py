from django.db import models
from django.contrib.auth.models import User

class Obraz (models.Model):
    grafika = models.ImageField(upload_to="grafiki", null=True, blank=True)
    tytul = models.CharField(max_length=30, null=True, blank=False)
    cena = models.FloatField(null=True, blank=True)
    wlasciciel = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    #User.objects.get(id=user_id)
    #wlasciciel = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.tytul
"""""
class Zamowienie (models.Model):
    wybrany_obraz = models.OneToOneField(Obraz, on_delete=models.CASCADE, null=True, blank=True)
    zamawiajcy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    adres_dostawy = models.CharField(max_length=100, null=True, blank=False)
    telefon = models.PositiveSmallIntegerField(null=True, blank=False)
    email = models.CharField(max_length=50, null=True, blank=False)
    """""