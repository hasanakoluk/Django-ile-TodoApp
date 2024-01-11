from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets





class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username','password')


    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = widgets.TextInput(attrs={'class':'form-control'})
        self.fields['password'].widget = widgets.PasswordInput(attrs={'class':'form-control'})

