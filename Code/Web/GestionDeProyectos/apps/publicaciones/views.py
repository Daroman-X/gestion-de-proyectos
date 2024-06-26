from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Publicacion


class PublicacionViews(LoginRequiredMixin,ListView):
    model=Publicacion
    template_name="publicacion/index.html"
    context_object_name="publicaciones"
    
    
class PublicacionDetailView(DetailView):
    model=Publicacion
    template_name="publicacion/detalle.html"
    context_object_name="publicacion_detalle"
    
class PublicacionCreateView(LoginRequiredMixin,CreateView):
    model=Publicacion
    template_name="publicacion/crear.html"
    fields=["titulo","texto"]
    
    def form_valid(self,form):
        form.instance.autor=self.request.user
        return super().form_valid(form)
    
    
class PublicacionUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Publicacion
    template_name="publicacion/editar.html"
    fields=["titulo","texto"]
    
    def test_func(self):
        obj=self.get_object()
        return obj.autor==self.request.user
    
    
class PublicacionDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Publicacion
    template_name="publicacion/eliminar.html"
    success_url=reverse_lazy("publicacion:inicio")
    
    def test_func(self):
        obj=self.get_object()
        return obj.autor==self.request.user