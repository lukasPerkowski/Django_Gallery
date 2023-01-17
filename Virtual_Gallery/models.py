from django.db import models
from django.contrib.auth.models import User

class Obraz(models.Model):
    grafika = models.ImageField(upload_to="grafiki", null=True, blank=True)
    tytul = models.CharField(max_length=30, null=True, blank=False)
    cena = models.FloatField(null=True, blank=True)
    wlasciciel = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    opis = models.TextField(max_length=200, blank=True, null=True) 

    def __str__(self):
        return self.tytul


class Wiadomosc(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    imie = models.CharField(verbose_name='Imię',max_length=20, null=True, blank=False)
    obraz = models.ForeignKey(Obraz, on_delete=models.CASCADE, null=True, blank=False)
    wiadomosc = models.TextField(verbose_name='Wiadomość',max_length=200,null=True, blank=False)
    telefon = models.PositiveSmallIntegerField(blank=False, null=True)
    proponowana_cena = models.PositiveIntegerField(verbose_name='Zaproponuj cenę',blank=True, null=True)


  

