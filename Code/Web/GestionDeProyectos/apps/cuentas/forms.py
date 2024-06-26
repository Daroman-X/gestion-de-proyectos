from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import UsuarioPersonalizado

class UsuarioPersonalizadoCrearForm(UserCreationForm):
    class Meta(UserCreationForm):
        model=UsuarioPersonalizado
        fields=UserCreationForm.Meta.fields+('username','email','edad',)
        

class UsuarioPersonalizadoEditarForm(UserChangeForm):
    class Meta:
        model=UsuarioPersonalizado
        fields=UserChangeForm.Meta.fields
        
