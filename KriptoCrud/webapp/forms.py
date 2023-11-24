from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from . models import Cerita

from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
# register / create new user

class CreateUser(UserCreationForm):
    
    class Meta : 
        model = User
        fields = ['username', 'password1', 'password2']
    
# login 
class Login(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

# add cerita
class AddCeritaForm(forms.ModelForm):
    class Meta : 
        model = Cerita
        fields = ['judul', 'konten']
     
        
# update cerita
class UpdateCeritaForm(forms.ModelForm):
    class Meta : 
        model = Cerita
        fields = ['judul', 'konten', ]