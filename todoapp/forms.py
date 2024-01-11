from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.forms import widgets



class Todo_Ekle(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ("baslik","aciklama","resim","kategori","alt_kategoriler")

        widgets = {
            'baslik':forms.TextInput(attrs={"class":"form-control","placeholder":"Başlık"}),
            'aciklama': forms.Textarea(attrs={"class":"form-control","placeholder":"açıklama"}),
            'resim':forms.FileInput(attrs={"class":"form-control"}),
            'kategori':forms.Select(attrs={"class":"form-select"}),
            'alt_kategoriler': forms.SelectMultiple(attrs={"class":"form-select"}),
        }

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username','password')


    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = widgets.TextInput(attrs={'class':'form-control'})
        self.fields['password'].widget = widgets.PasswordInput(attrs={'class':'form-control'})




