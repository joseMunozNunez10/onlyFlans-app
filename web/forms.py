from django import forms
from django.forms import ModelForm
from .models import ContactForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ContactFormForm(forms.Form):
    email = forms.EmailField(label="Correo")
    name = forms.CharField(max_length=64, label="Nombre")
    message = forms.CharField(widget=forms.Textarea, label="Mensaje")

class ContactFormModelForm(ModelForm):
    class Meta:
        model = ContactForm
        fields = ['email', 'name', 'message']    

class SuscriptionForm():
    email = forms.EmailField(label="Correo")
    class Meta:
        model = User
        fields =['username', 'email']

class RegistroForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField()


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
   
        