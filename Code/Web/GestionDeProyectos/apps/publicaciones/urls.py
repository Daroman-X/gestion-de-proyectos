from django.urls import path
from .views import PublicacionDeleteView, PublicacionViews,PublicacionDetailView,PublicacionCreateView,PublicacionUpdateView

app_name="publicacion"

urlpatterns = [
    path("", PublicacionViews.as_view(),name="inicio"),
    path("<int:pk>/", PublicacionDetailView.as_view(),name="detalle"),
    path("crear/", PublicacionCreateView.as_view(),name="crear"),
    path("<int:pk>/editar", PublicacionUpdateView.as_view(),name="editar"),
    path("<int:pk>/eliminar", PublicacionDeleteView.as_view(),name="eliminar"),

]

