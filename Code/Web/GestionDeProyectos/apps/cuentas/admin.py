from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UsuarioPersonalizadoCrearForm, UsuarioPersonalizadoEditarForm
from .models import UsuarioPersonalizado


class UsuarioPersonalizadoAdmin(UserAdmin):
    add_form=UsuarioPersonalizadoCrearForm
    form=UsuarioPersonalizadoEditarForm
    model=UsuarioPersonalizado
    list_display=['email','username','edad','is_staff']

admin.site.register(UsuarioPersonalizado,UsuarioPersonalizadoAdmin)