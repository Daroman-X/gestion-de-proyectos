from django.shortcuts import render
from django.views.generic import TemplateView

"""
Clase InicioView
Redirecciona a la pagina de inicio principal de la aplicacion
"""
class InicioView(TemplateView):
    template_name="core/index.html"
    

"""
Clase GestionView
Redirecciona a la pagina de gestion de proyectos, usuarios y demas
"""
class GestionView(TemplateView):
    template_name="core/gestion.html"


"""
Clase FormatosView
Redirecciona a la pagina de formatos (SRs, HU, Diccionario de datos, etc.)
"""
class FormatosView(TemplateView):
    template_name="core/formatos.html"


"""
Clase TableroView
Redirecciona a la pagina donde esta el tablero de quehaceres
"""
class TableroView(TemplateView):
    template_name="core/tablero.html"

