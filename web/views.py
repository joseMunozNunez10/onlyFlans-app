from django.shortcuts import render
from .models import Flan
from django.http import HttpResponseRedirect, HttpResponse
from .forms import ContactFormForm, RegistroForm, ContactFormModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

def indice(request):
    public_flans = Flan.objects.filter(es_privado=False)

    return render(request,'index.html', {'public_flans': public_flans})                    

def acerca(request):
    return render(request, 'about.html', {})

@login_required
def bienvenido(request):
    private_flans = Flan.objects.filter(es_privado=True)

    return render(request, 'welcome.html', {'private_flans': private_flans})


def contacto(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/exito')
        
    else:
         form = ContactFormModelForm()

    return render(request, 'contactus.html', {'form': form})        

def exito(request):
    return render(request, 'success.html', {})

def suscribete(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            contact_form = ContactFormForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/')
        
    else:
        form = ContactFormForm()

    return render(request, 'success.html', {'form': form})          


def register(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        print(form.is_valid())
        print(form.cleaned_data)
        print(form.errors) 
        if form.is_valid():                       
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/bienvenido')
        
    else:
        form = RegistroForm()

    return render(request, 'register.html', {'form': form})
