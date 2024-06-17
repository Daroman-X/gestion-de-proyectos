from django.urls import path
from apps.core.views import InicioView,GestionView,FormatosView,TableroView

app_name="core"

urlpatterns = [
    path("", InicioView.as_view(),name="inicio"),
    path("gestion/", GestionView.as_view(),name="gestion"),
    path("formatos/", FormatosView.as_view(),name="formatos"),
    path("tablero/", TableroView.as_view(),name="tablero"),
]
