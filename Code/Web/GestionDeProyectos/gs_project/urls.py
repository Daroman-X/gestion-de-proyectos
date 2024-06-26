from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/",include('django.contrib.auth.urls'),name="login"),
    path("",include("apps.core.urls"), name="core"),
    path("cuentas/",include("apps.cuentas.urls"), name="cuentas"),
    path("publicaciones/",include("apps.publicaciones.urls"), name="publicaciones"),
]
