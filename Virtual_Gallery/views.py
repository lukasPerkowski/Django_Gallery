from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Obraz, Wiadomosc  #Zamowienie
from .forms import ObrazForm, CreateUserForm, EditUserForm, WiadomoscForm



def glownaObrazy(request):
    wszystkie = Obraz.objects.all().order_by('-id')
    
    return render(request, 'gallery_main.html',{'Obrazy':wszystkie})

@login_required
def nowyObraz(request):
    form = ObrazForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.wlasciciel = request.user

        obj.save()
        form.save()
        return redirect('glowna')
              
    return render(request, 'nowy_obraz.html', {'form':form}) 

@login_required
def edytujObraz(request,id):
    obraz = get_object_or_404(Obraz, pk = id)
    form = ObrazForm(request.POST or None, request.FILES or None, instance=obraz)
    if request.user == obraz.wlasciciel:
        if form.is_valid():
            obraz = form.save(commit=False)
            obraz.save()
            return redirect('glowna')
        return render(request, 'nowy_obraz.html',{'form':form})    
    else:
        return redirect('glowna')

@login_required
def usunObraz(request,id):
    obraz = get_object_or_404(Obraz, pk=id)
    if request.user == obraz.wlasciciel:
        if request.method == "POST":
            if obraz.grafika:
                obraz.grafika.delete()

            obraz.delete()
    
            return redirect('glowna')
        return render(request, 'usun.html', {'obraz':obraz})
    else:
        return redirect('glowna')

def RegisterPage(request):
    form = CreateUserForm(request.POST or None)
    if request.method == 'POST':
        
        if form.is_valid():
            form.save()
            return redirect('Login')

    context = {'form':form}
    return render(request, 'registration/register.html', context)

def opisObrazu(request,id):
    
    obraz = get_object_or_404(Obraz, pk=id) 
    form = WiadomoscForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(commit=False)
            obj.autor = obraz.wlasciciel
            obj.obraz = obraz
            obj.save()
            form.save()
            return redirect('glowna')
 

    return render(request, 'opis.html', {'obraz':obraz, 'form':form}) 

@login_required(login_url='Login')
def profileView(request):
    obrazy = Obraz.objects.filter(wlasciciel=request.user)
    
    return render(request, 'profil.html', {'obrazy':obrazy})


class editProfile(generic.UpdateView):
    form_class = EditUserForm
    template_name = 'registration/editprofile.html'
    success_url = reverse_lazy('glowna')
    
    def get_object(self):
        return self.request.user


def wiadomosciView(request):
    wiadmosci = Wiadomosc.objects.filter(autor = request.user)
    
    return render(request, 'wiadomosci.html', {'wiadomosci':wiadmosci})

def usunWiadomosc(request,id):
    wiadomosc = get_object_or_404(Wiadomosc, pk=id)

    if request.method == "POST":
        wiadomosc.delete()
        return redirect('glowna')    

    return render(request, 'usun_wiadomosc.html', {'wiadomosc':wiadomosc})



"""""
def zlozenieZamowienia(request, id):
    zamowienie = get_object_or_404(Zamowienie, pk=id)
    form = ZamowienieForm(request.POST or None, request.FILES or None, instance=zamowienie) 
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('glowna')
    return render(request, 'zamowienie.html', {'form':form,'zamowienie':zamowienie})       
    """""