from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import UsuarioPersonalizadoCrearForm

class RegistroViews(CreateView):
    form_class=UsuarioPersonalizadoCrearForm
    success_url=reverse_lazy('login')
    template_name="registration/registro.html"
    
# views.py
# views.py
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'password_change_form.html'
    success_url = reverse_lazy('registro')
