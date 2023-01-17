from django.forms import ModelForm
from .models import Obraz, Wiadomosc
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class ObrazForm(ModelForm):
    class Meta:
        model = Obraz
        fields = ['grafika','tytul','cena', 'opis']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1','password2', 'email']

class EditUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email']        

class WiadomoscForm(ModelForm):
    class Meta:
        model = Wiadomosc
        fields = ['imie', 'wiadomosc','telefon','proponowana_cena']

"""""
class ZamowienieForm(ModelForm):
    class Meta:
        model: Zamowienie
        fields = ['wybrany_obraz', 'zamawiajcy','adres_dostawy','telfon','email']
        """""