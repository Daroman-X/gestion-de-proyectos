from django.urls import path
from .views import RegistroViews
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

from .views import CustomPasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView
app_name="cuentas"

urlpatterns = [
    path('registro/',RegistroViews.as_view(),name="registro"),
    path('cambiar-contraseña/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('cambiar-contraseña/hecho/', PasswordChangeDoneView.as_view(
        template_name='password_change_done.html'
    ), name='password_change_done'),
]
